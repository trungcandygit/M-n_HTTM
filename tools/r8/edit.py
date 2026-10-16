"""Áp danh sách sửa (JSON) lên word/document.xml đã giải nén, không tracked changes.
Mỗi mục: {"id":..., "op":"replace", "old":..., "new":...}
         {"id":..., "op":"new_para_after", "anchor":..., "text":...}  (nhân bản đoạn chứa anchor, đặt text mới)
         {"id":..., "op":"delete_para", "anchor":...}
old/anchor phải xuất hiện đúng 1 lần trong toàn văn bản (theo đoạn).
"""
import json, sys, copy
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


def own_ts(p):
    out = []
    for t in p.iter(f"{{{W}}}t"):
        anc = t.getparent()
        while anc is not None and anc.tag != f"{{{W}}}p":
            anc = anc.getparent()
        if anc is p:
            out.append(t)
    return out


def ptext(p):
    return "".join(t.text or "" for t in own_ts(p))


def find_unique(paras, s):
    hits = [(p, ptext(p).count(s)) for p in paras]
    hits = [(p, c) for p, c in hits if c]
    total = sum(c for _, c in hits)
    return hits[0][0] if total == 1 else None, total


def replace_in_para(p, old, new):
    ts = own_ts(p)
    full = "".join(t.text or "" for t in ts)
    start = full.index(old)
    end = start + len(old)
    pos = 0
    first = True
    for t in ts:
        txt = t.text or ""
        a, b = pos, pos + len(txt)
        pos = b
        if b <= start or a >= end:
            continue
        s0, e0 = max(start, a) - a, min(end, b) - a
        if first:
            t.text = txt[:s0] + new + txt[e0:]
            first = False
        else:
            t.text = txt[:s0] + txt[e0:]
        t.set(XML_SPACE, "preserve")


def set_runs_md(p, text):
    """Viết lại toàn bộ run của đoạn; *...* là in nghiêng. Giữ pPr và rPr gốc (bỏ i/iCs)."""
    runs = [r for r in p.findall(f"{{{W}}}r")]
    base = None
    for r in runs:
        rp = r.find(f"{{{W}}}rPr")
        if rp is not None and rp.find(f"{{{W}}}i") is None and rp.find(f"{{{W}}}vertAlign") is None:
            base = rp
            break
    for r in runs:
        p.remove(r)
    for i, seg in enumerate(text.split("*")):
        if not seg:
            continue
        r = etree.SubElement(p, f"{{{W}}}r")
        rp = copy.deepcopy(base) if base is not None else None
        if rp is not None:
            for va in rp.findall(f"{{{W}}}vertAlign"): rp.remove(va)
        if i % 2 == 1:
            if rp is None:
                rp = etree.Element(f"{{{W}}}rPr")
            for tag in ("i", "iCs"):
                if rp.find(f"{{{W}}}{tag}") is None:
                    rp.append(etree.Element(f"{{{W}}}{tag}"))
        if rp is not None:
            r.append(rp)
        t = etree.SubElement(r, f"{{{W}}}t")
        t.text = seg
        t.set(XML_SPACE, "preserve")


def split_para(p, anchor):
    """Tách đoạn p thành hai: phần trước anchor giữ ở p, từ anchor trở đi sang đoạn mới ngay sau."""
    full = ptext(p)
    pos = full.index(anchor)
    q = copy.deepcopy(p)
    for el in list(q.iter()):
        for a in list(el.attrib):
            if a.endswith("}paraId") or a.endswith("}textId"):
                del el.attrib[a]
    for tag in ("bookmarkStart", "bookmarkEnd"):
        for b in q.findall(f".//{{{W}}}{tag}"):
            b.getparent().remove(b)
    def cut(par, keep_before):
        acc = 0
        for t in own_ts(par):
            txt = t.text or ""
            a, b = acc, acc + len(txt)
            acc = b
            if keep_before:
                if a >= pos: t.text = ""
                elif b > pos: t.text = txt[:pos - a]
            else:
                if b <= pos: t.text = ""
                elif a < pos: t.text = txt[pos - a:]
            t.set(XML_SPACE, "preserve")
        # bỏ khoảng trắng ở rìa
        ts = [t for t in own_ts(par) if t.text]
        if keep_before and ts: ts[-1].text = ts[-1].text.rstrip()
        if not keep_before and ts: ts[0].text = ts[0].text.lstrip()
    cut(p, True); cut(q, False)
    p.addnext(q)


def main(docxml, editsfile):
    tree = etree.parse(docxml)
    root = tree.getroot()
    edits = json.load(open(editsfile, encoding="utf-8"))
    import html
    for e in edits:
        for k in ("old", "new", "anchor", "text"):
            if k in e:
                e[k] = html.unescape(e[k])
    ok, bad = 0, []
    for e in edits:
        paras = list(root.iter(f"{{{W}}}p"))
        key = e.get("old") or e.get("anchor")
        if e["op"] == "replace_all":
            cnt = 0
            for pp in paras:
                while e["old"] in ptext(pp):
                    replace_in_para(pp, e["old"], e["new"]); cnt += 1
            if cnt == 0:
                bad.append((e["id"], "found 0 times", key[:90]))
            else:
                ok += 1; print(e["id"], "replaced", cnt)
            continue
        p, n = find_unique(paras, key)
        if p is None:
            bad.append((e["id"], f"found {n} times", key[:90]))
            continue
        if e["op"] == "replace":
            replace_in_para(p, e["old"], e["new"])
        elif e["op"] == "new_para_after":
            np_ = copy.deepcopy(p)
            ts = own_ts(np_)
            for t in ts[1:]:
                t.getparent().remove(t)
            ts[0].text = e["text"]
            ts[0].set(XML_SPACE, "preserve")
            # bỏ các run rỗng còn lại (giữ run đầu)
            p.addnext(np_)
        elif e["op"] in ("para_md", "new_para_md_after"):
            target = p
            if e["op"] == "new_para_md_after":
                target = copy.deepcopy(p)
                p.addnext(target)
            set_runs_md(target, e["text"])
        elif e["op"] == "split_before":
            split_para(p, e["anchor"])
        elif e["op"] == "delete_para":
            p.getparent().remove(p)
        ok += 1
    tree.write(docxml, xml_declaration=True, encoding="UTF-8", standalone=True)
    print(f"applied {ok}/{len(edits)}")
    for b in bad:
        print("FAIL", b)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
