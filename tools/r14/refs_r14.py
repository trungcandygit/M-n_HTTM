import sys, copy, re
sys.path.insert(0, sys.argv[2])
from edit import *
from lxml import etree
doc = sys.argv[1]; tree = etree.parse(doc); root = tree.getroot()
q = lambda t: f"{{{W}}}{t}"
paras = lambda: list(root.iter(q("p")))
def rep(o, n, allp=False, need=True):
    c = 0
    for p in paras():
        while o in ptext(p):
            replace_in_para(p, o, n); c += 1
            if not allp: break
        if c and not allp: break
    print("rep", c, o[:50]); assert c or not need
rep("FTSE Russell, 2026)", "FTSE Russell, 2026b)", allp=True, need=False)
rep("FTSE Russell. (2026, August).", "FTSE Russell. (2026b, August).")
rep("4138–4156. [CẦN XÁC MINH tập, số và trang]", "4138–4156. https://doi.org/10.1111/1475-6773.12993")
rep(" [CẦN XÁC MINH thứ tự tác giả trên trang bài của tạp chí]", "")
TOK = re.compile(r"(\*.+?\*)")
def newref(anchor_start, text):
    tgt = [p for p in paras() if ptext(p).startswith(anchor_start)]
    assert len(tgt) == 1, (anchor_start, len(tgt)); p = tgt[0]
    n = copy.deepcopy(p)
    for a in list(n.attrib):
        if a.endswith("}paraId") or a.endswith("}textId"): del n.attrib[a]
    runs = n.findall(q("r")); base = None
    for r in runs:
        rp = r.find(q("rPr"))
        if rp is not None and rp.find(q("i")) is None: base = rp; break
    for r in runs: n.remove(r)
    for seg in TOK.split(text):
        if not seg: continue
        it = seg.startswith("*")
        if it: seg = seg[1:-1]
        r = etree.SubElement(n, q("r"))
        rp = copy.deepcopy(base) if base is not None else etree.Element(q("rPr"))
        for e in rp.findall(q("i")) + rp.findall(q("iCs")): rp.remove(e)
        if it: rp.insert(0, etree.Element(q("iCs"))); rp.insert(0, etree.Element(q("i")))
        if len(rp): r.append(rp)
        t = etree.SubElement(r, q("t")); t.text = seg; t.set(XML_SPACE, "preserve")
    p.addprevious(n); print("new ref before", anchor_start[:40])
newref("Bộ Tài chính. (2020).", "Báo Đầu tư Chứng khoán. (2026). HNX nhập HOSE, UPCoM còn doanh nghiệp nào đang chia cổ tức tốt với P/E rẻ? [Bài báo ngày 06/10/2026].")
newref("Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh. (2026).", "Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh. (2025). *Quy định giao dịch đăng website HOSE* [Kèm theo Tờ trình số 51/TTr-HTGD ngày 26/4/2025].")
newref("FTSE Russell. (2026b, August).", "FTSE Russell. (2026a, September). *FTSE Global Equity Index Series ground rules* (Version 14.4). LSEG.")
tree.write(doc, xml_declaration=True, encoding="UTF-8", standalone=True)
