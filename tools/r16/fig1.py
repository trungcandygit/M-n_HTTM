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
def box(x,y,cx,cy,lines,border=True):
    nid[0]+=1
    ln='<a:ln w="9525"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:ln>' if border else '<a:ln><a:noFill/></a:ln>'
    fill='<a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>' if border else '<a:noFill/>'
    body=''.join(para(l,bold=(i==0 and border),sz=20 if border else 18) for i,l in enumerate(lines))
    return (f'<wps:wsp><wps:cNvPr id="{nid[0]}" name="Hop {nid[0]}"/><wps:cNvSpPr txBox="1"/><wps:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>{fill}{ln}</wps:spPr><wps:txbx><w:txbxContent>{body}</w:txbxContent></wps:txbx>'
            f'<wps:bodyPr rot="0" vert="horz" wrap="square" lIns="54000" tIns="36000" rIns="54000" bIns="36000" anchor="ctr" anchorCtr="0"><a:noAutofit/></wps:bodyPr></wps:wsp>')
def arrow(x,y,cx,cy,dash=False,flipV=False):
    nid[0]+=1
    fv=' flipV="1"' if flipV else ''
    d='<a:prstDash val="dash"/>' if dash else '<a:prstDash val="solid"/>'
    return (f'<wps:wsp><wps:cNvPr id="{nid[0]}" name="Mui ten {nid[0]}"/><wps:cNvCnPr/><wps:spPr><a:xfrm{fv}><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom><a:noFill/><a:ln w="12700"><a:solidFill><a:srgbClr val="000000"/></a:solidFill>{d}<a:tailEnd type="triangle" w="med" len="med"/></a:ln></wps:spPr><wps:bodyPr/></wps:wsp>')
BW,BH,GAP,VG=1584000,1116000,396000,612000
X=[0,BW+GAP,2*(BW+GAP)]; Y2=BH+VG; TW=X[2]+BW; TH=Y2+BH
sh=''
sh+=box(X[0],0,BW,BH,["Trước hợp nhất","Chỉ số chất lượng","HNX so với HOSE (H2)","6/2009–6/2025"])
sh+=box(X[1],0,BW,BH,["Sự kiện 28/12/2026","Chuyển sàn sang HOSE","Thanh khoản (H3)","Khả năng đầu tư (H4)"])
sh+=box(X[2],0,BW,BH,["Hàm ý cho Hà Nội","Chuyên môn hóa thị trường","Trái phiếu, phái sinh, UPCoM","Hạ tầng dữ liệu"])
sh+=box(X[1],Y2,BW,BH,["Nhóm đối chứng","Cổ phiếu HOSE đối sánh","Cổ phiếu UPCoM"])
sh+=box(X[2],Y2,BW,BH,["Bằng chứng quốc tế","Điểm GFCI (H1)","Phát triển thị trường","Thể chế, thu nhập"])
sh+=arrow(BW,BH//2,GAP,0)
sh+=arrow(X[1]+BW,BH//2,GAP,0,dash=True)
cx1=X[1]+BW//2; cx2=X[2]+BW//2
sh+=arrow(cx1,BH,0,VG,flipV=True)
sh+=arrow(cx2,BH,0,VG,dash=True,flipV=True)
sh+=box(cx1+54000,BH+90000,BW//2+180000,VG-180000,["so sánh","(khác biệt kép)"],border=False)
sh+=box(cx2+54000,BH+90000,BW//2,VG-180000,["bối cảnh"],border=False)
drawing=(f'<w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{TW}" cy="{TH}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="601" name="Hình 1. Khung phân tích của đề tài"/><wp:cNvGraphicFramePr/>'
 f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"><wpg:wgp><wpg:cNvGrpSpPr/><wpg:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{TW}" cy="{TH}"/><a:chOff x="0" y="0"/><a:chExt cx="{TW}" cy="{TH}"/></a:xfrm></wpg:grpSpPr>{sh}</wpg:wgp></a:graphicData></a:graphic></wp:inline></w:drawing>')
d=open('fig1/word/document.xml').read()
b0=d.index('<w:body>')+len('<w:body>'); sect=d.rfind('<w:sectPr'); 
body=(f'<w:p><w:pPr><w:spacing w:before="0" w:after="120"/><w:jc w:val="center"/></w:pPr><w:r>{drawing}</w:r></w:p>'
 '<w:p><w:pPr><w:pStyle w:val="Heading4"/></w:pPr><w:r><w:t>Khung phân tích của đề tài</w:t></w:r></w:p>'
 '<w:p><w:pPr><w:pStyle w:val="SourceNote"/></w:pPr><w:r><w:t xml:space="preserve">Nguồn: Thí sinh đề xuất. Nét liền: kiểm định hoặc ước lượng; nét đứt: tổng hợp định tính.</w:t></w:r></w:p>')
# keep only last sectPr (body-level)
d=d[:b0]+body+d[sect:]
open('fig1/word/document.xml','w').write(d)
print(TW,TH)
