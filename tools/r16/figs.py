import re
from xml.sax.saxutils import escape
W14='w14:paraId' 
def runs(text,bold=False,sz=20):
    out=[]
    for seg in re.split(r'(?<=H)(\d)',text):
        if not seg: continue
        sub = seg.isdigit() and out and out[-1][0].endswith('H')
        out.append((seg,sub))
    x=''
    for seg,sub in out:
        rp=('<w:b/><w:bCs/>' if bold else '')+'<w:color w:val="000000"/>'+f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'+('<w:vertAlign w:val="subscript"/>' if sub else '')
        x+=f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>{rp}</w:rPr><w:t xml:space="preserve">{escape(seg)}</w:t></w:r>'
    return x
def para(text,bold=False,sz=20):
    return f'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>{runs(text,bold,sz)}</w:p>'
nid=[100]
def box(x,y,cx,cy,lines,border=True,boldfirst=True):
    nid[0]+=1
    ln='<a:ln w="9525"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:ln>' if border else '<a:ln><a:noFill/></a:ln>'
    fill='<a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>' if border else '<a:noFill/>'
    body=''.join(para(l,bold=(i==0 and border and boldfirst),sz=18 if border else 16) for i,l in enumerate(lines))
    return (f'<wps:wsp><wps:cNvPr id="{nid[0]}" name="Hop {nid[0]}"/><wps:cNvSpPr txBox="1"/><wps:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>{fill}{ln}</wps:spPr><wps:txbx><w:txbxContent>{body}</w:txbxContent></wps:txbx>'
            f'<wps:bodyPr rot="0" vert="horz" wrap="square" lIns="36000" tIns="18000" rIns="36000" bIns="18000" anchor="ctr" anchorCtr="0"><a:noAutofit/></wps:bodyPr></wps:wsp>')
def arrow(x,y,cx,cy,dash=False,flipV=False):
    nid[0]+=1
    fv=' flipV="1"' if flipV else ''
    d='<a:prstDash val="dash"/>' if dash else '<a:prstDash val="solid"/>'
    return (f'<wps:wsp><wps:cNvPr id="{nid[0]}" name="Mui ten {nid[0]}"/><wps:cNvCnPr/><wps:spPr><a:xfrm{fv}><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom><a:noFill/><a:ln w="12700"><a:solidFill><a:srgbClr val="000000"/></a:solidFill>{d}<a:tailEnd type="triangle" w="med" len="med"/></a:ln></wps:spPr><wps:bodyPr/></wps:wsp>')

def drawing(sh,TW,TH,did,name):
    return (f'<w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{TW}" cy="{TH}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="{did}" name="{name}"/><wp:cNvGraphicFramePr/>'
     f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"><wpg:wgp><wpg:cNvGrpSpPr/><wpg:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{TW}" cy="{TH}"/><a:chOff x="0" y="0"/><a:chExt cx="{TW}" cy="{TH}"/></a:xfrm></wpg:grpSpPr>{sh}</wpg:wgp></a:graphicData></a:graphic></wp:inline></w:drawing>')
def block(dr,cap,src):
    return (f'<w:p><w:pPr><w:keepNext/><w:spacing w:before="120" w:after="60"/><w:jc w:val="center"/></w:pPr><w:r>{dr}</w:r></w:p>'
     f'<w:p><w:pPr><w:pStyle w:val="Heading4"/></w:pPr><w:r><w:t xml:space="preserve">{cap}</w:t></w:r></w:p>'
     f'<w:p><w:pPr><w:pStyle w:val="SourceNote"/></w:pPr><w:r><w:t xml:space="preserve">{src}</w:t></w:r></w:p>')
TW=4680000
# ---- Hình 1
BW,GAP,BH,VG=1440000,180000,792000,396000
X=[0,BW+GAP,2*(BW+GAP)]; Y2=BH+VG
sh=box(X[0],0,BW,BH,["Trước hợp nhất","HNX so với HOSE (H2)","6/2009–6/2025"])
sh+=box(X[1],0,BW,BH,["Sự kiện 28/12/2026","Thanh khoản (H3)","Khả năng đầu tư (H4)"])
sh+=box(X[2],0,BW,BH,["Hàm ý cho Hà Nội","Chuyên môn hóa thị trường","Hạ tầng dữ liệu"])
sh+=box(X[1],Y2,BW,BH,["Nhóm đối chứng","Cổ phiếu HOSE đối sánh","Cổ phiếu UPCoM"])
sh+=box(X[2],Y2,BW,BH,["Bằng chứng quốc tế","Điểm GFCI (H1)","Thể chế, thu nhập"])
sh+=arrow(BW,BH//2,GAP,0)+arrow(X[1]+BW,BH//2,GAP,0,dash=True)
c1=X[1]+BW//2; c2=X[2]+BW//2
sh+=arrow(c1,BH,0,VG,flipV=True)+arrow(c2,BH,0,VG,dash=True,flipV=True)
sh+=box(c1+36000,BH+36000,BW//2,VG-72000,["khác biệt kép"],border=False)
sh+=box(c2+36000,BH+36000,BW//2,VG-72000,["bối cảnh"],border=False)
f1=block(drawing(sh,TW,Y2+BH,701,"Hình khung phân tích"),"Khung phân tích của đề tài","Nguồn: Thí sinh đề xuất. Nét liền: kiểm định hoặc ước lượng; nét đứt: tổng hợp định tính.")
# ---- Hình 2 cửa sổ
SFT=828000; VW=SFT; EW=TW-3*SFT; RH=396000; SH=468000
sh=''
for i in range(3):
    x=i*SFT; y=i*SH
    sh+=box(x,y,EW,RH,[f"Cửa sổ {i+1}: ước lượng 104 tuần"],boldfirst=False)
    sh+=box(x+EW,y,VW,RH,["Đánh giá","3 tháng"])
ya=2*SH+RH+108000
sh+=arrow(0,ya,TW,0)
sh+=box(TW-1080000,ya+36000,1080000,216000,["thời gian"],border=False)
f2=block(drawing(sh,TW,ya+288000,702,"Hình cửa sổ"),"Cửa sổ ước lượng và cửa sổ đánh giá","Nguồn: Thí sinh đề xuất.")
# ---- Hình 3 quy trình: một hàng ngang
BW3,G3,H3=828000,135000,756000
steps=[["Bước 1","Dữ liệu GFCI và ba sàn"],["Bước 2","Chỉ số chất lượng; H2"],["Bước 3","Bằng chứng quốc tế; H1"],["Bước 4","Chuyển sàn; H3, H4"],["Bước 5","Hàm ý cho Hà Nội"]]
sh=''
for i,st in enumerate(steps):
    x=i*(BW3+G3); sh+=box(x,0,BW3,H3,st)
    if i<4: sh+=arrow(x+BW3,H3//2,G3,0)
f3=block(drawing(sh,TW,H3,703,"Hình quy trình"),"Quy trình nghiên cứu","Nguồn: Thí sinh đề xuất. Kế hoạch phân tích được đăng ký trước ngày 28/12/2026.")
d=open('fig1/word/document.xml').read()
b0=d.index('<w:body>')+len('<w:body>'); sect=d.rfind('<w:sectPr')
d=d[:b0]+f1+f2+f3+d[sect:]
open('fig1/word/document.xml','w').write(d)
print('ok')
