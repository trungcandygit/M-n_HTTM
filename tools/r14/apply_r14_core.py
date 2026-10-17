import sys, json, copy, re
from edit import *
from lxml import etree
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
