"""Định dạng v9: H1–H4 chỉ số dưới; bảng chữ viết tắt; chuẩn hóa bảng."""
import sys, re, copy
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XS = "{http://www.w3.org/XML/1998/namespace}space"
def q(t): return f"{{{W}}}{t}"

root_dir = sys.argv[1]
doc_p = f"{root_dir}/word/document.xml"
sty_p = f"{root_dir}/word/styles.xml"
tree = etree.parse(doc_p); root = tree.getroot()

# ---------- 1. H1–H4 chỉ số dưới ----------
PAT = re.compile(r"(?<![A-Za-zÀ-ỹ0-9])H([1-4])(?![0-9])")
nsub = 0
for r in list(root.iter(q("r"))):
    rpr = r.find(q("rPr"))
    if rpr is not None and rpr.find(q("vertAlign")) is not None:
        continue
    ts = r.findall(q("t"))
    if len(ts) != 1 or not ts[0].text or not PAT.search(ts[0].text):
        continue
    if len(r) - (1 if rpr is not None else 0) != 1:
        continue  # run có phần tử khác ngoài t
    text = ts[0].text
    parts = []; last = 0
    for m in PAT.finditer(text):
        parts.append((text[last:m.start()] + "H", False)); parts.append((m.group(1), True)); last = m.end()
    parts.append((text[last:], False))
    parent = r.getparent(); idx = parent.index(r)
    new = []
    for seg, sub in parts:
        if not seg: continue
        nr = etree.Element(q("r"))
        npr = copy.deepcopy(rpr) if rpr is not None else etree.Element(q("rPr"))
        if sub:
            va = etree.Element(q("vertAlign")); va.set(q("val"), "subscript"); nsub += 1
            after_tags = [q(x) for x in ("rtl", "cs", "em", "lang", "eastAsianLayout", "specVanish", "oMath")]
            pos = next((i for i, ch in enumerate(npr) if ch.tag in after_tags), len(npr))
            npr.insert(pos, va)
        if len(npr): nr.append(npr)
        t = etree.SubElement(nr, q("t")); t.text = seg; t.set(XS, "preserve")
        new.append(nr)
    parent.remove(r)
    for k, nr in enumerate(new): parent.insert(idx + k, nr)
print("H subscripts:", nsub)

# ---------- helpers ----------
def ptext(p): return "".join(t.text or "" for t in p.iter(q("t")))
TEXTW = 11906 - 1984 - 1134  # 8788 dxa

def cell(text_runs, width, header=False, center=False):
    tc = etree.Element(q("tc"))
    tcpr = etree.SubElement(tc, q("tcPr"))
    w = etree.SubElement(tcpr, q("tcW")); w.set(q("w"), str(width)); w.set(q("type"), "dxa")
    p = etree.SubElement(tc, q("p"))
    ppr = etree.SubElement(p, q("pPr")); ps = etree.SubElement(ppr, q("pStyle")); ps.set(q("val"), "Compact")
    if center:
        jc = etree.SubElement(ppr, q("jc")); jc.set(q("val"), "center")
    for txt in text_runs:
        r = etree.SubElement(p, q("r"))
        if header:
            rp = etree.SubElement(r, q("rPr")); etree.SubElement(rp, q("b"))
        t = etree.SubElement(r, q("t")); t.text = txt; t.set(XS, "preserve")
    return tc

# ---------- 2. Bảng chữ viết tắt ----------
body = root.find(q("body"))
paras = list(body)
start = None
for i, el in enumerate(paras):
    if el.tag == q("p") and ptext(el).strip() == "DANH MỤC CHỮ VIẾT TẮT":
        start = i; break
abbr = []
j = start + 1
while j < len(paras) and paras[j].tag == q("p") and ":" in ptext(paras[j]):
    abbr.append(paras[j]); j += 1
widths = [1700, TEXTW - 1700]
tbl = etree.Element(q("tbl"))
tp = etree.SubElement(tbl, q("tblPr"))
e = etree.SubElement(tp, q("tblStyle")); e.set(q("val"), "Table")
e = etree.SubElement(tp, q("tblW")); e.set(q("w"), str(TEXTW)); e.set(q("type"), "dxa")
e = etree.SubElement(tp, q("tblLook")); e.set(q("val"), "0020"); e.set(q("firstRow"), "1")
g = etree.SubElement(tbl, q("tblGrid"))
for wv in widths:
    gc = etree.SubElement(g, q("gridCol")); gc.set(q("w"), str(wv))
tr = etree.SubElement(tbl, q("tr"))
tr.append(cell(["Chữ viết tắt"], widths[0], header=True, center=True))
tr.append(cell(["Nghĩa đầy đủ"], widths[1], header=True, center=True))
for p in abbr:
    k, v = ptext(p).split(":", 1)
    tr = etree.SubElement(tbl, q("tr"))
    tr.append(cell([k.strip()], widths[0]))
    tr.append(cell([v.strip()], widths[1]))
abbr[0].addprevious(tbl)
for p in abbr: body.remove(p)
print("abbr rows:", len(abbr))

# ---------- 3. Chuẩn hóa mọi bảng ----------
WID = {
    "Nhóm nghiên cứu": [2000, 3600, 3188],
    "Giả thuyết": [3400, 3000, 2388],
    "Mã": [900, 4600, 3288],
    "Chương": [1100, 2900, 4788],
    "Năm": [1000, 4900, 2888],
    "TT|Công trình": [600, 3900, 2600, 1688],
    "TT|Tên bài báo": [550, 2900, 800, 2150, 1500, 888],
    "Chữ viết tắt": widths,
}
for tbl in root.iter(q("tbl")):
    rows = tbl.findall(q("tr"))
    heads = [ptext(tc) for tc in rows[0].findall(q("tc"))]
    key = heads[0] if heads[0] != "TT" else "TT|" + heads[1]
    ws = WID.get(key)
    tp = tbl.find(q("tblPr"))
    if ws and len(ws) == len(heads):
        tw = tp.find(q("tblW")); tw.set(q("w"), str(TEXTW)); tw.set(q("type"), "dxa")
        if tp.find(q("tblLayout")) is None:
            lay = etree.Element(q("tblLayout")); lay.set(q("type"), "fixed")
            tw.addnext(lay)
        grid = tbl.find(q("tblGrid"))
        for gc, wv in zip(grid.findall(q("gridCol")), ws): gc.set(q("w"), str(wv))
        for row in rows:
            for tc, wv in zip(row.findall(q("tc")), ws):
                tcpr = tc.find(q("tcPr"))
                if tcpr is None:
                    tcpr = etree.Element(q("tcPr")); tc.insert(0, tcpr)
                w_ = tcpr.find(q("tcW"))
                if w_ is None:
                    w_ = etree.SubElement(tcpr, q("tcW"))
                w_.set(q("w"), str(wv)); w_.set(q("type"), "dxa")
    else:
        print("WARN no widths for", heads)
    for k, row in enumerate(rows):
        trpr = row.find(q("trPr"))
        if trpr is None:
            trpr = etree.Element(q("trPr")); row.insert(0, trpr)
        if trpr.find(q("cantSplit")) is None: etree.SubElement(trpr, q("cantSplit"))
        if k == 0 and trpr.find(q("tblHeader")) is None: etree.SubElement(trpr, q("tblHeader"))
        if k == 0:
            for p in row.iter(q("p")):
                ppr = p.find(q("pPr"))
                if ppr.find(q("jc")) is None:
                    jc = etree.Element(q("jc")); jc.set(q("val"), "center")
                    rp = ppr.find(q("rPr"))
                    if rp is not None: rp.addprevious(jc)
                    else: ppr.append(jc)
tree.write(doc_p, xml_declaration=True, encoding="UTF-8", standalone=True)

# ---------- 4. Style "Table": nền tiêu đề, lề ô, căn trên ----------
st = etree.parse(sty_p); sr = st.getroot()
for s in sr.findall(q("style")):
    if s.get(q("styleId")) == "Table":
        tp = s.find(q("tblPr")); mar = tp.find(q("tblCellMar"))
        for side, v in (("top", 57), ("left", 100), ("bottom", 57), ("right", 100)):
            mar.find(q(side)).set(q("w"), str(v))
        fr = [x for x in s.findall(q("tblStylePr")) if x.get(q("type")) == "firstRow"][0]
        if fr.find(q("tcPr")) is None:
            tcpr = etree.SubElement(fr, q("tcPr"))
            shd = etree.SubElement(tcpr, q("shd")); shd.set(q("val"), "clear"); shd.set(q("color"), "auto"); shd.set(q("fill"), "E7E6E6")
            va = etree.SubElement(tcpr, q("vAlign")); va.set(q("val"), "center")
        if s.find(q("tcPr")) is None:
            tcpr = etree.Element(q("tcPr")); va = etree.SubElement(tcpr, q("vAlign")); va.set(q("val"), "top")
            s.find(q("tblStylePr")).addprevious(tcpr)
st.write(sty_p, xml_declaration=True, encoding="UTF-8", standalone=True)
print("done")
