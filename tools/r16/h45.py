import re,sys; sys.path.insert(0,'../../r8tools')
from edit import *
from lxml import etree
q=lambda t:f'{{{W}}}{t}'
# styles
st=open('word/styles.xml').read()
def mk(sid,name,base,lvl,num):
    m=re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>'%base,st,re.S).group(0)
    ppr=re.search(r'<w:pPr>(.*?)</w:pPr>',m,re.S).group(1); rpr=re.search(r'<w:rPr>(.*?)</w:rPr>',m,re.S).group(1)
    return (f'<w:style w:type="paragraph" w:styleId="{sid}"><w:name w:val="{name}"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="9"/><w:unhideWhenUsed/><w:qFormat/>'
            f'<w:pPr>{ppr.replace("<w:keepNext/>","<w:keepNext/><w:numPr><w:numId w:val=\""+str(num)+"\"/></w:numPr>")}<w:outlineLvl w:val="{lvl}"/></w:pPr><w:rPr>{rpr}<w:i w:val="0"/><w:iCs w:val="0"/></w:rPr></w:style>')
st=st.replace('</w:styles>',mk('Heading4','heading 4','FigureCaption',3,90)+mk('Heading5','heading 5','TableCaption',4,91)+'</w:styles>')
open('word/styles.xml','w').write(st)
# numbering
n=open('word/numbering.xml').read()
def absn(aid,txt,sid):
    return (f'<w:abstractNum w:abstractNumId="{aid}"><w:multiLevelType w:val="singleLevel"/><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:pStyle w:val="{sid}"/>'
            f'<w:suff w:val="space"/><w:lvlText w:val="{txt} %1."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="0" w:firstLine="0"/></w:pPr></w:lvl></w:abstractNum>')
abst=absn(90,'Hình','Heading4')+absn(91,'Bảng','Heading5')
i=n.index('<w:num ')
n=n[:i]+abst+n[i:]
n=n.replace('</w:numbering>','<w:num w:numId="90"><w:abstractNumId w:val="90"/></w:num><w:num w:numId="91"><w:abstractNumId w:val="91"/></w:num></w:numbering>')
open('word/numbering.xml','w').write(n)
# document
t=etree.parse('word/document.xml'); b=t.getroot().find(q('body'))
cnt={'Heading4':0,'Heading5':0}
for p in b.iter(q('p')):
    ps=p.find(q('pPr')+'/'+q('pStyle'))
    if ps is None or ps.get(q('val')) not in ('FigureCaption','TableCaption'): continue
    new='Heading4' if ps.get(q('val'))=='FigureCaption' else 'Heading5'
    tx=ptext(p); m=re.match(r'(Hình|Bảng) \d+\. ',tx); assert m,tx
    k=len(m.group(0))
    for node in [x for x in p if x.tag in (q('r'),q('fldSimple'),q('hyperlink'))]:
        if k<=0: break
        ts=list(node.iter(q('t'))); L=sum(len(x.text or '') for x in ts)
        if L<=k: p.remove(node); k-=L
        else:
            for x in ts:
                l=len(x.text or '')
                if k>=l: k-=l; x.text=''
                else: x.text=x.text[k:]; k=0; break
    ps.set(q('val'),new); cnt[new]+=1
s=etree.tostring(t,xml_declaration=True,encoding='UTF-8',standalone=True).decode()
s=s.replace('TOC \\h \\z \\c "Bảng"','TOC \\o "5-5" \\h \\z').replace('TOC \\h \\z \\c "Hình"','TOC \\o "4-4" \\h \\z')
open('word/document.xml','w').write(s)
sp=open('word/settings.xml').read()
import re as _r
if 'updateFields' not in sp:
    m=_r.search(r'<w:(hdrShapeDefaults|footnotePr|endnotePr|compat)\b',sp); sp=sp[:m.start()]+'<w:updateFields w:val="true"/>'+sp[m.start():]
open('word/settings.xml','w').write(sp)
print(cnt)
