import sys, re, copy, shutil
sys.path.insert(0,'../r8tools')
from edit import *
from lxml import etree
q=lambda t:f'{{{W}}}{t}'
D='w/word/'
# ---------- SmartArt clone ----------
NEW=["6/2009–6/2025: giai đoạn tham chiếu","Bắt đầu khi UPCoM khai trương (24/6/2009)","Dùng cho H2 và cửa sổ trước của H3",
"1/7/2025: HNX ngừng nhận niêm yết mới","Giai đoạn tham chiếu kết thúc ngày 30/6/2025","Ngày tham chiếu để lập rổ và ghép đối chứng",
"7/2025–12/2026: giai đoạn chuyển tiếp","Không dùng trong kiểm định chính","Chỉ dùng trong phiên bản nghiên cứu sự kiện",
"28/12/2026: phiên đầu tại HOSE","Phiên cuối tại HNX ngày 23/12; tạm ngừng 24–25/12","Tệp đăng ký trước được khóa trước ngày này",
"1/2027–12/2028: giai đoạn sau sự kiện","24 tháng dữ liệu cho H3","8 cửa sổ đánh giá cho H4"]
for f in ['data','layout','quickStyle','colors','drawing']:
    shutil.copy(D+f'diagrams/{f}1.xml',D+f'diagrams/{f}2.xml')
for f in ['data2.xml','drawing2.xml']:
    s=open(D+'diagrams/'+f).read(); olds=re.findall(r'<a:t>([^<]*)</a:t>',s); assert len(olds)==15
    it=iter(NEW); s=re.sub(r'<a:t>[^<]*</a:t>',lambda m:'<a:t>'+next(it)+'</a:t>',s)
    s=s.replace('r:id="rId14"','r:id="rId914"').replace('relId="rId14"','relId="rId914"')
    open(D+'diagrams/'+f,'w').write(s)
rels=open(D+'_rels/document.xml.rels').read()
add=''.join(f'<Relationship Id="rId9{n}" Type="{t}" Target="diagrams/{f}2.xml"/>' for n,t,f in [
 (10,"http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramData","data"),
 (11,"http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramLayout","layout"),
 (12,"http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramQuickStyle","quickStyle"),
 (13,"http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramColors","colors"),
 (14,"http://schemas.microsoft.com/office/2007/relationships/diagramDrawing","drawing")])
open(D+'_rels/document.xml.rels','w').write(rels.replace('</Relationships>',add+'</Relationships>'))
ct=open('w/[Content_Types].xml').read()
for f,t in [('data','application/vnd.openxmlformats-officedocument.drawingml.diagramData+xml'),('layout','application/vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml'),('quickStyle','application/vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml'),('colors','application/vnd.openxmlformats-officedocument.drawingml.diagramColors+xml'),('drawing','application/vnd.ms-office.drawingml.diagramDrawing+xml')]:
    ct=ct.replace('</Types>',f'<Override PartName="/word/diagrams/{f}2.xml" ContentType="{t}"/></Types>')
open('w/[Content_Types].xml','w').write(ct)
# ---------- document ----------
tree=etree.parse(D+'document.xml'); body=tree.getroot().find(q('body'))
P=lambda: [e for e in body if e.tag==q('p')]
def sty(x):
    st=x.find('.//'+q('pStyle')); return st.get(q('val')) if st is not None else None
def find(pre,style=None):
    h=[e for e in P() if ptext(e).startswith(pre) and (style is None or sty(e)==style)]; assert len(h)==1,(pre,len(h)); return h[0]
# renumber existing Bảng/Hình in all w:t
BM={1:2,2:3,3:4,4:8,5:9,6:10,7:11}; HM={2:3,3:4}
for par in body.iter(q('p')):
    ts=[t for t in par.iter(q('t'))]
    full=''.join(t.text or '' for t in ts)
    if 'Bảng' not in full and 'Hình' not in full: continue
    pos=[];o=0
    for t in ts: pos.append(o); o+=len(t.text or '')
    edits=[]
    for m in re.finditer(r'(Bảng|Hình) (\d+)',full):
        n=int(m.group(2)); mp=BM if m.group(1)=='Bảng' else HM
        if n in mp: edits.append((m.start(2),m.end(2),str(mp[n])))
    for st,en,rep in reversed(edits):
        k=max(i for i,p0 in enumerate(pos) if p0<=st)
        t=ts[k]; ls=st-pos[k]; le=en-pos[k]
        assert le<=len(t.text), 'digit split'
        t.text=t.text[:ls]+rep+t.text[le:]
# check no split "Bảng" + digit across runs
for e in P():
    tx=ptext(e)
    for m in re.finditer(r'(Bảng|Hình) ?\d',tx): pass
# templates
cap_t=find('Bảng 4. Bảy','TableCaption'); tbl_t=find('Bảng 2. Các nhóm','TableCaption').getnext(); src_t=cap_t.getnext().getnext()
figbox=find('Hình 4. Quy trình','FigureCaption').getprevious(); figcap=find('Hình 4. Quy trình','FigureCaption'); figsrc=figcap.getnext()
body_t=find('Đề tài đo khả năng đầu tư bằng bảy')
bmid=[900]
def settext(p,text,sz=None):
    for r in p.findall(q('r'))+p.findall(q('hyperlink')): p.remove(r)
    for x in p.findall(q('bookmarkStart'))+p.findall(q('bookmarkEnd')): p.remove(x)
    for seg in re.split(r'(?<=[HM])(\d)(?!\d)',text):
        if not seg: continue
        r=etree.SubElement(p,q('r'))
        sub=seg.isdigit() and len(seg)==1 and r.getprevious() is not None and (r.getprevious().findtext(q('t')) or '').endswith(('H','M'))
        if sub or sz:
            rp=etree.SubElement(r,q('rPr'))
            if sub: etree.SubElement(rp,q('vertAlign')).set(q('val'),'subscript')
            if sz:
                etree.SubElement(rp,q('sz')).set(q('val'),str(sz)); etree.SubElement(rp,q('szCs')).set(q('val'),str(sz))
        tt=etree.SubElement(r,q('t')); tt.text=seg; tt.set(XML_SPACE,'preserve')
def caption(tpl,text,name):
    c=copy.deepcopy(tpl)
    for x in list(c):
        if x.tag!=q('pPr'): c.remove(x)
    m=re.match(r'(Bảng|Hình) (\d+)\. (.*)',text); lab,num,title=m.groups()
    bmid[0]+=1
    bs=etree.SubElement(c,q('bookmarkStart')); bs.set(q('id'),str(bmid[0])); bs.set(q('name'),name)
    r=etree.SubElement(c,q('r')); t=etree.SubElement(r,q('t')); t.text=lab+' '; t.set(XML_SPACE,'preserve')
    f=etree.SubElement(c,q('fldSimple')); f.set(q('instr'),' SEQ %s \\* ARABIC '%lab)
    r=etree.SubElement(f,q('r')); rp=etree.SubElement(r,q('rPr')); etree.SubElement(rp,q('noProof')); t=etree.SubElement(r,q('t')); t.text=num
    r=etree.SubElement(c,q('r')); t=etree.SubElement(r,q('t')); t.text='. '+title; t.set(XML_SPACE,'preserve')
    be=etree.SubElement(c,q('bookmarkEnd')); be.set(q('id'),str(bmid[0]))
    return c
def mktable(rows):
    t=copy.deepcopy(tbl_t); trs=t.findall(q('tr')); hdr,row=trs[0],trs[1]
    for r in trs[1:]: t.remove(r)
    def fill(tr,vals):
        for tc,v in zip(tr.findall(q('tc')),vals):
            ps=tc.findall(q('p'))
            for p in ps[1:]: tc.remove(p)
            settext(ps[0],v,sz=22)
    fill(hdr,rows[0])
    for v in rows[1:]:
        r=copy.deepcopy(row); fill(r,v); t.append(r)
    return t
def para(text):
    p=copy.deepcopy(body_t); settext(p,text)
    st=p.find('.//'+q('pStyle'))
    if st is not None and st.get(q('val'))=='FirstParagraph': st.set(q('val'),'BodyText')
    return p
def src(text):
    s=copy.deepcopy(src_t); settext(s,text); return s
def insert_after(anchor,items):
    for it in items: anchor.addnext(it); anchor=it
    return anchor
TB={}
# Bảng 1 mốc thời gian
rows=[("Thời điểm","Sự kiện","Vai trò"),
("24/6/2009","UPCoM khai trương","Bắt đầu mẫu"),
("2016","Quy chế giao dịch HOSE (QĐ 341) và HNX (QĐ 529)","Bước giá"),
("2021–2025","Thông tư 57/2021, 69/2023, 139/2025: hạn chuyển sàn lùi từ 2023 đến 31/12/2026","Lộ trình"),
("30/6/2025","Hết giai đoạn tham chiếu","Lập rổ, ghép đối chứng"),
("1/7/2025","HNX ngừng nhận niêm yết mới","Bắt đầu chuyển tiếp"),
("9/2026–9/2027","FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số","Cú sốc trùng thời gian"),
("30/9/2026","VNX công bố lịch chuyển sàn","Xác định ngày sự kiện"),
("28/12/2026","Phiên đầu tại HOSE","Ngày sự kiện"),
("1/2027–12/2028","24 tháng sau sự kiện","Kiểm định H3, ước lượng H4")]
a=find('Hạn chuyển cổ phiếu UPCoM sang HOSE cũng là')
insert_after(a,[para("Bảng 1 xếp các mốc pháp lý và thời gian dùng trong thiết kế nghiên cứu theo thứ tự thời gian."),caption(cap_t,"Bảng 1. Các mốc pháp lý và thời gian của đề tài","_Toc9001"),mktable(rows),src("Nguồn: Thí sinh tổng hợp.")])
# Hình 2 SmartArt
a=find('Mẫu bắt đầu từ tháng 6/2009')
fb=copy.deepcopy(figbox); xs=etree.tostring(fb).decode()
xs=xs.replace('r:dm="rId10"','r:dm="rId910"').replace('r:lo="rId11"','r:lo="rId911"').replace('r:qs="rId12"','r:qs="rId912"').replace('r:cs="rId13"','r:cs="rId913"')
xs=re.sub(r'(<wp:docPr id=")503(" name=")[^"]*"',r'\g<1>504\g<2>Hình 2. Ba giai đoạn (SmartArt)"',xs)
fb=etree.fromstring(xs)
insert_after(a,[fb,caption(figcap,"Hình 2. Ba giai đoạn thời gian của mẫu dữ liệu Việt Nam","_Toc9002"),src("Nguồn: Thí sinh đề xuất.")])
replace_in_para(a,"giai đoạn sau sự kiện kéo dài 24 tháng từ tháng 1/2027.","giai đoạn sau sự kiện kéo dài 24 tháng từ tháng 1/2027 (Hình 2).")
# Bảng 5 cú sốc
a=find('Ba mức chịu cú sốc tương ứng được đo')
insert_after(a,[caption(cap_t,"Bảng 5. Ba thay đổi quy tắc khi chuyển sàn và thước đo mức chịu cú sốc","_Toc9005"),mktable([("Thay đổi","Chịu mạnh nhất","Thước đo"),("Biên độ ±10% → ±7%","Mã hay tăng giảm 7–10%","Tỷ lệ ngày |lợi suất| 7–10%"),("Bước giá nhỏ đi","Mã giá thấp","1/giá bình quân"),("Vào chỉ số HOSE","Mã vốn hóa lớn so với giao dịch","Vốn hóa/giá trị giao dịch")]),src("Nguồn: Thí sinh đề xuất.")])
replace_in_para(a,"Ba mức chịu cú sốc tương ứng được đo","Ba mức chịu cú sốc tương ứng (Bảng 5) được đo")
# Bảng 6 trùng thời gian
a=find('Vì vậy, nhóm đối chứng HOSE loại các mã')
insert_after(a,[caption(cap_t,"Bảng 6. Thay đổi trùng thời gian ở HOSE và cách xử lý","_Toc9006"),mktable([("Thay đổi","Ảnh hưởng","Cách xử lý"),("FTSE Russell (9/2026–9/2027)","Mã HOSE đủ điều kiện","Loại khỏi nhóm đối chứng"),("Phân bảng HOSE","Hai nhóm bảng","Thêm biến giả nhóm bảng"),("VN-Index nhận mã mới","Mã chuyển sàn vốn hóa lớn","Đo bằng mức chịu cú sốc (Bảng 5)"),("Nới biên độ, xuyên trưa","Mọi mã HOSE","Cắt cửa sổ sau tại ngày áp dụng (phụ)")]),src("Nguồn: Thí sinh tổng hợp.")])
# bootstrap sentence
a=find('Vì mọi cổ phiếu chuyển sàn cùng một ngày, suy luận chính')
replace_in_para(a,"Vì mọi cổ phiếu chuyển sàn cùng một ngày, suy luận chính dựa trên chuỗi","Vì mọi cổ phiếu chuyển sàn cùng một ngày, về bản chất chỉ có một lần chuyển sàn; coi hàng trăm mã là hàng trăm quan sát độc lập sẽ làm sai số chuẩn quá nhỏ (Conley & Taber, 2011). Suy luận chính vì vậy dựa trên chuỗi")
# Bảng 7 rủi ro
a=find('Nếu cả hai nhóm đối chứng không đạt kiểm tra xu hướng song song')
R=[("Rủi ro","Cách xử lý","Mục"),
("Không dùng được điểm GFCI theo kỳ","Câu hỏi 1 trả lời dạng mô tả","4.3.10"),
("Chuyển sàn bị lùi hoặc nhiều đợt","DiD xử lý so le (Callaway & Sant’Anna, 2021)","4.3.10"),
("Sự kiện không diễn ra","Dùng mã đã tự chuyển sàn trước 2026","4.3.10"),
("UPCoM chuyển sàn sớm","Dừng nhóm đối chứng UPCoM; dựa vào nhóm HOSE","4.3.10"),
("Không đạt xu hướng song song","Nhóm đối chứng tổng hợp","4.3.10"),
("Biên độ, bước giá đổi cơ học","Ngưỡng lợi suất chung; báo cáo theo nhóm giá","4.3.2"),
("Sai số chuẩn quá nhỏ","Bootstrap tự hồi quy trên dₜ","4.3.7"),
("Chọn kết quả sau khi xem dữ liệu","Đăng ký trước trên OSF","4.3.5")]
insert_after(a,[para("Bảng 7 tóm tắt các rủi ro chính và cách xử lý."),caption(cap_t,"Bảng 7. Rủi ro và cách xử lý","_Toc9007"),mktable(R),src("Nguồn: Thí sinh tổng hợp.")])
# ---------- danh mục bảng/hình ----------
lst=[e for e in P() if sty(e)=='TableofFigures']
def entry(after_txt_prefix,text,anchor,before=False):
    base=[e for e in lst if ptext(e).startswith(after_txt_prefix)][0]
    n=copy.deepcopy(base)
    h=n.find(q('hyperlink')); h.set(q('anchor'),anchor)
    ts=h.findall('.//'+q('t')); ts[0].text=text
    for x in ts[1:]:
        if x.getparent().find(q('rPr'))is not None and x.getparent().find(q('rPr')).find(q('webHidden')) is None: x.text=''
    for it in h.iter(q('instrText')): it.text=f' PAGEREF {anchor} \\h '
    (base.addprevious if before else base.addnext)(n); return n
entry('Bảng 2. Các nhóm','Bảng 1. Các mốc pháp lý và thời gian của đề tài','_Toc9001',before=True)
e5=entry('Bảng 4. Bảy','Bảng 5. Ba thay đổi quy tắc khi chuyển sàn và thước đo mức chịu cú sốc','_Toc9005')
e6=entry('Bảng 4. Bảy','Bảng 6. Thay đổi trùng thời gian ở HOSE và cách xử lý','_Toc9006'); e5.addprevious(e6) if False else None
e5.addnext(e6)
e7=entry('Bảng 4. Bảy','Bảng 7. Rủi ro và cách xử lý','_Toc9007'); e6.addnext(e7)
entry('Hình 1.','Hình 2. Ba giai đoạn thời gian của mẫu dữ liệu Việt Nam','_Toc9002')

NOTES={"Nguồn: Thí sinh tổng hợp. Ghi chú: K1":"Nguồn: Thí sinh tổng hợp.",
"Nguồn: Thí sinh đề xuất. Ghi chú: mũi tên":"Nguồn: Thí sinh đề xuất. Mũi tên nét đứt chỉ hàm ý chính sách.",
"Nguồn: Thí sinh đề xuất. Ghi chú: H1":"Nguồn: Thí sinh đề xuất. H1–H3 hiệu chỉnh Holm ở mức 5%; H4 chỉ ước lượng.",
"Nguồn: Thí sinh tổng hợp. Ghi chú: cả bảy":"Nguồn: Thí sinh tổng hợp. Cả bảy mô hình chỉ mua, ước lượng lại hằng tháng trên cửa sổ 104 tuần.",
"Nguồn: Thí sinh đề xuất. Ghi chú: ở mỗi":"Nguồn: Thí sinh đề xuất.",
"Ghi chú: (*) Tác giả liên hệ.":"Ghi chú: (*) Tác giả liên hệ. Trạng thái tính đến 30/9/2026; bài số 4 cập nhật đến 09/10/2026."}
for e in P():
    if sty(e)=='SourceNote':
        for k,v in NOTES.items():
            if ptext(e).startswith(k): settext(e,v)
for tb in body.iter(q('tbl')):
    for r in tb.iter(q('r')):
        rp=r.find(q('rPr'))
        if rp is None: rp=etree.Element(q('rPr')); r.insert(0,rp)
        for tag in ('sz','szCs'):
            x=rp.find(q(tag))
            if x is None: x=etree.SubElement(rp,q(tag))
            x.set(q('val'),'22')
for ex in body.iter('{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent'):
    gd=ex.getparent().find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}graphicData')
    if gd is not None and 'diagram' in gd.get('uri',''):
        ex.set('cy',str(int(int(ex.get('cy'))*0.7)))

for c in P():
    if sty(c) in ('TableCaption','FigureCaption') and c.find(q('fldSimple')) is None:
        tx=ptext(c); m=re.match(r'(Bảng|Hình) (\d+)\. ',tx)
        if not m: continue
        r0=[r for r in c.findall(q('r')) if r.findtext(q('t'))][0]; t0=r0.find(q('t'))
        pre=m.group(0)
        assert t0.text.startswith(pre), (t0.text,pre)
        t0.text=t0.text[len(pre)-2:]; t0.set(XML_SPACE,'preserve')   # keep ". "
        r1=etree.Element(q('r')); tt=etree.SubElement(r1,q('t')); tt.text=m.group(1)+' '; tt.set(XML_SPACE,'preserve')
        f=etree.Element(q('fldSimple')); f.set(q('instr'),' SEQ %s \\* ARABIC '%m.group(1))
        rr=etree.SubElement(f,q('r')); rp=etree.SubElement(rr,q('rPr')); etree.SubElement(rp,q('noProof')); etree.SubElement(rr,q('t')).text=m.group(2)
        r0.addprevious(r1); r0.addprevious(f)
        print('SEQ added',tx[:40])

tree.write(D+'document.xml',xml_declaration=True,encoding='UTF-8',standalone=True)
s2=open(D+'document.xml').read().replace('val="D9D9D9"','val="FFFFFF"'); open(D+'document.xml','w').write(s2)
for f in ['drawing1.xml','drawing2.xml']:
    x=open(D+'diagrams/'+f).read()
    x=re.sub(r'(</a:prstGeom>)<a:solidFill>.*?</a:solidFill>',r'\1<a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>',x)
    x=re.sub(r'(<a:ln [^>]*>)<a:solidFill>.*?</a:solidFill>',r'\1<a:solidFill><a:srgbClr val="000000"/></a:solidFill>',x)
    x=x.replace('<a:fontRef idx="minor"><a:schemeClr val="lt1"/></a:fontRef>','<a:fontRef idx="minor"><a:schemeClr val="dk1"/></a:fontRef>')
    x=re.sub(r'(<a:rPr [^>]*>)(?!<a:solidFill>)',r'\1<a:solidFill><a:srgbClr val="000000"/></a:solidFill>',x)
    open(D+'diagrams/'+f,'w').write(x)
for f in ['colors1.xml','colors2.xml']:
    x=open(D+'diagrams/'+f).read()
    x=re.sub(r'<dgm:fillClrLst([^>/]*)>.*?</dgm:fillClrLst>',r'<dgm:fillClrLst\1><a:srgbClr val="FFFFFF"/></dgm:fillClrLst>',x)
    x=re.sub(r'<dgm:linClrLst([^>/]*)>.*?</dgm:linClrLst>',r'<dgm:linClrLst\1><a:srgbClr val="000000"/></dgm:linClrLst>',x)
    x=re.sub(r'<dgm:txFillClrLst([^>/]*)>.*?</dgm:txFillClrLst>',r'<dgm:txFillClrLst\1><a:srgbClr val="000000"/></dgm:txFillClrLst>',x)
    open(D+'diagrams/'+f,'w').write(x)
st=open(D+'settings.xml').read()
if 'updateFields' not in st: st=st.replace('<w:zoom','<w:updateFields w:val="true"/><w:zoom',1)
open(D+'settings.xml','w').write(st)
print('ok')
