# -*- coding: utf-8 -*-
"""Viết lại 7 công thức OMML theo kiểu kinh tế lượng cổ điển (chỉ số dưới viết liền, không dấu phẩy)."""
import sys, copy
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; M="http://schemas.openxmlformats.org/officeDocument/2006/math"
w=lambda t:f'{{{W}}}{t}'; m=lambda t:f'{{{M}}}{t}'
XS="{http://www.w3.org/XML/1998/namespace}space"
def font(parent):
    rp=etree.SubElement(parent,w('rPr')); f=etree.SubElement(rp,w('rFonts')); f.set(w('ascii'),'Cambria Math'); f.set(w('hAnsi'),'Cambria Math')
def R(text,plain=False):
    r=etree.Element(m('r'))
    if plain:
        rp=etree.SubElement(r,m('rPr')); s=etree.SubElement(rp,m('sty')); s.set(m('val'),'p')
    font(r); t=etree.SubElement(r,m('t')); t.text=text; t.set(XS,'preserve'); return r
def ctrl(pr):
    c=etree.SubElement(pr,m('ctrlPr')); font(c)
def SUB(base,sub,bplain=False):
    e=etree.Element(m('sSub')); ctrl(etree.SubElement(e,m('sSubPr')))
    b=etree.SubElement(e,m('e')); [b.append(x) for x in (base if isinstance(base,list) else [R(base,bplain)])]
    s=etree.SubElement(e,m('sub')); [s.append(x) for x in (sub if isinstance(sub,list) else [R(sub)])]
    return e
def SUP(base,sup):
    e=etree.Element(m('sSup')); ctrl(etree.SubElement(e,m('sSupPr')))
    b=etree.SubElement(e,m('e')); [b.append(x) for x in (base if isinstance(base,list) else [R(base)])]
    s=etree.SubElement(e,m('sup')); [s.append(x) for x in (sup if isinstance(sup,list) else [R(sup,True)])]
    return e
def FRAC(num,den):
    e=etree.Element(m('f')); ctrl(etree.SubElement(e,m('fPr')))
    n=etree.SubElement(e,m('num')); [n.append(x) for x in num]
    d=etree.SubElement(e,m('den')); [d.append(x) for x in den]
    return e
def SUM(sub,body):
    e=etree.Element(m('nary')); pr=etree.SubElement(e,m('naryPr'))
    c=etree.SubElement(pr,m('chr')); c.set(m('val'),'∑')
    l=etree.SubElement(pr,m('limLoc')); l.set(m('val'),'undOvr')
    h=etree.SubElement(pr,m('supHide')); h.set(m('val'),'1'); ctrl(pr)
    s=etree.SubElement(e,m('sub')); [s.append(x) for x in sub]
    etree.SubElement(e,m('sup'))
    b=etree.SubElement(e,m('e')); [b.append(x) for x in body]
    return e
P=lambda t:R(t,True)
EQ={
 "(1)":[SUB("MQI","jt",True),P(" = "),FRAC([SUB("TK","jt",True),P(" + "),SUB("HQ","jt",True),P(" + "),SUB("MB","jt",True)],[P("3")])],
 "(2)":[R("U"),P(" = "),R("μ"),P(" − "),FRAC([R("ρ")],[P("2")]),SUP("σ","2")],
 "(3)":[SUB("G","m"),P(" = "),SUB("U","m"),P("(H) − "),SUB("U","m"),P("(CS)")],
 "(4)":[[R("Ḡ")][0],P(" = "),FRAC([SUB("G","1",False),P(" + "),SUB("G","2"),P(" + … + "),SUB("G","7")],[P("7")])],
 "(5)":[SUB("A","it"),P(" = "),SUB("α","i"),P(" + "),SUB("τ","t"),P(" + "),R("δ"),SUB("D","i"),SUB("Post","t"),P(" + "),SUB("ε","it")],
 "(6)":[SUB("A","it"),P(" = "),SUB("α","i"),P(" + "),SUB("τ","t"),P(" + "),SUM([R("k")],[SUB("δ","k"),SUB("D","i"),SUB("T","kt")]),P(" + "),SUB("ε","it")],
 "(7)":[SUB("Z","it"),P(" = "),SUB("γ","i"),P(" + "),SUB("θ","t"),P(" + "),R("β"),SUB("SMD","it",True),P(" + "),R("λ"),SUB("W","it"),P(" + "),SUB("u","it")],
}
# chỉ số dưới số và chữ hoa đứng thẳng
for k in EQ: pass
doc=sys.argv[1]; tree=etree.parse(doc); body=tree.getroot().find(w('body')); n=0
for p in body.iter(w('p')):
    om=p.find(m('oMath'))
    if om is None: continue
    num=''.join(t.text or '' for t in p.iter(w('t'))).strip()
    key=num[-3:]
    new=etree.Element(m('oMath'))
    for x in EQ[key]: new.append(x)
    om.addprevious(new); p.remove(om); n+=1
tree.write(doc,xml_declaration=True,encoding='UTF-8',standalone=True); print('equations replaced',n)
