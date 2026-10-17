import re,copy,sys
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:f"{{{W}}}{t}"; XS="{http://www.w3.org/XML/1998/namespace}space"
p=sys.argv[1]; tr=etree.parse(p); root=tr.getroot()
for run in root.iter(q('r')):
    rp=run.find(q('rPr'))
    if rp is None: continue
    va=rp.find(q('vertAlign')); t=''.join(z.text or '' for z in run.findall(q('t')))
    if va is not None and ' ' in t: rp.remove(va)
UNI={'ᵢ':'i','ₜ':'t','ₛ':'s','ⱼ':'j','ₖ':'k','ₘ':'m'}
PAT=re.compile(r"(?<![A-Za-zÀ-ỹ0-9])([HM])([1-7])(?![0-9])|([ᵢₜₛⱼₖₘ]+)")
AFT=[q(x) for x in ("rtl","cs","em","lang","eastAsianLayout","specVanish","oMath")]; n=0
for r in list(root.iter(q("r"))):
    rpr=r.find(q("rPr"))
    if rpr is not None and rpr.find(q("vertAlign")) is not None: continue
    ts=r.findall(q("t"))
    if len(ts)!=1 or not ts[0].text or not PAT.search(ts[0].text) or len(r)-(rpr is not None)!=1: continue
    text=ts[0].text; parts=[]; last=0
    for m in PAT.finditer(text):
        if m.group(1): parts.append((text[last:m.start()]+m.group(1),0)); parts.append((m.group(2),1))
        else: parts.append((text[last:m.start()],0)); parts.append(("".join(UNI[c] for c in m.group(3)),1))
        last=m.end()
    parts.append((text[last:],0))
    par=r.getparent(); i=par.index(r); par.remove(r)
    for seg,sub in [x for x in parts if x[0]]:
        nr=etree.Element(q("r")); npr=copy.deepcopy(rpr) if rpr is not None else etree.Element(q("rPr"))
        if sub:
            v=etree.Element(q("vertAlign")); v.set(q("val"),"subscript")
            pos=next((k for k,ch in enumerate(npr) if ch.tag in AFT),len(npr)); npr.insert(pos,v); n+=1
        if len(npr): nr.append(npr)
        t=etree.SubElement(nr,q("t")); t.text=seg; t.set(XS,"preserve"); par.insert(i,nr); i+=1
tr.write(p,xml_declaration=True,encoding="UTF-8",standalone=True)
x=open(p,encoding='utf-8').read(); print("subscripts",n,'unicode left',sum(x.count(c) for c in 'ᵢₜₛⱼₖₘ'))
