import copy, re
from edit import *
from lxml import etree
import apply_r14_core as C
def apply_prefix(doc, ops):
    tree = etree.parse(doc); body = tree.getroot().find(f"{{{W}}}body")
    for kind, pre, arg in ops:
        hits = [el for el in body if el.tag == f"{{{W}}}p" and ptext(el).startswith(pre)]
        assert len(hits) == 1, (pre, len(hits)); el = hits[0]
        if kind == "del": body.remove(el)
        elif kind == "rp":
            for o, n in arg:
                assert ptext(el).count(o) == 1, (pre, o[:40]); replace_in_para(el, o, n)
        else:
            chunks = arg.split("\n\n"); C.set_md(el, chunks[0]); prev = el
            for c in chunks[1:]:
                n = copy.deepcopy(el); C.set_md(n, c); C.set_style(n, "BodyText"); prev.addnext(n); prev = n
    tree.write(doc, xml_declaration=True, encoding="UTF-8", standalone=True); print("ok", len(ops))
