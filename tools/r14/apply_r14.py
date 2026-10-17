import sys, json, copy, re
sys.path.insert(0, sys.argv[3])
from edit import *
from lxml import etree
doc, plan = sys.argv[1], json.load(open(sys.argv[2]))
tree = etree.parse(doc); body = tree.getroot().find(f"{{{W}}}body")
q = lambda t: f"{{{W}}}{t}"
TOK = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")
def set_md(p, text):
    runs = p.findall(q("r")); base = None
    for r in runs:
        rp = r.find(q("rPr"))
        if rp is None: base = None; break
        if all(rp.find(q(x)) is None for x in ("i","b","vertAlign")): base = rp; break
    for r in runs: p.remove(r)
    for seg in TOK.split(text):
        if not seg: continue
        kind = None
        if seg.startswith("**") and seg.endswith("**"): kind, seg = "b", seg[2:-2]
        elif seg.startswith("*") and seg.endswith("*"): kind, seg = "i", seg[1:-1]
        r = etree.SubElement(p, q("r"))
        rp = copy.deepcopy(base) if base is not None else etree.Element(q("rPr"))
        for x in ("b","bCs","i","iCs","vertAlign"):
            for e in rp.findall(q(x)): rp.remove(e)
        if kind:
            tags = ("b","bCs") if kind == "b" else ("i","iCs")
            for k, tg in enumerate(tags): rp.insert(k, etree.Element(q(tg)))
        if len(rp): r.append(rp)
        t = etree.SubElement(r, q("t")); t.text = seg; t.set(XML_SPACE, "preserve")
def set_style(p, val):
    ppr = p.find(q("pPr")); ps = ppr.find(q("pStyle")) if ppr is not None else None
    if ps is not None and ps.get(q("val")) == "FirstParagraph": ps.set(q("val"), val)
els = list(body)
items = sorted(set(map(int, plan["P"])) | set(map(int, plan["R"])), reverse=True)
for i in items:
    el = els[i]; txt = ptext(el)
    if str(i) in plan["R"]:
        pre, pairs, split = plan["R"][str(i)]
        assert txt.startswith(pre), (i, txt[:40])
        for o, n in pairs:
            assert txt.count(o) == 1, (i, o[:40]); replace_in_para(el, o, n); txt = ptext(el)
        if split:
            split_para(el, split); set_style(el.getnext(), "BodyText")
        continue
    pre, new = plan["P"][str(i)]
    assert txt.startswith(pre), (i, pre, txt[:40])
    if new is None: body.remove(el); continue
    chunks = new.split("\n\n"); set_md(el, chunks[0]); prev = el
    for c in chunks[1:]:
        n = copy.deepcopy(el); set_md(n, c); set_style(n, "BodyText")
        for a in list(n.attrib):
            if a.endswith("}paraId") or a.endswith("}textId"): del n.attrib[a]
        prev.addnext(n); prev = n
tree.write(doc, xml_declaration=True, encoding="UTF-8", standalone=True)
print("ok", len(items))
