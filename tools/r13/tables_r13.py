"""Vòng 13: bỏ nền xám dòng tiêu đề bảng; bảng chữ viết tắt 3 cột (viết tắt | tiếng Anh | tiếng Việt)."""
import sys, copy
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:f"{{{W}}}{t}"; XS="{http://www.w3.org/XML/1998/namespace}space"
d=sys.argv[1]
# 1. style Table: bỏ shd ở firstRow
st=etree.parse(f"{d}/word/styles.xml"); n=0
for s in st.getroot().findall(q("style")):
    if s.get(q("styleId"))=="Table":
        for shd in s.iter(q("shd")): shd.getparent().remove(shd); n+=1
st.write(f"{d}/word/styles.xml",xml_declaration=True,encoding="UTF-8",standalone=True)
print("removed shd",n)
# 2. bảng chữ viết tắt
ROWS=[
("ARIMA","Autoregressive Integrated Moving Average","Mô hình tự hồi quy tích hợp trung bình trượt"),
("CS","Không có","Rổ cổ phiếu chuyển sàn (ký hiệu của đề tài)"),
("GDP","Gross Domestic Product","Tổng sản phẩm trong nước"),
("GFCI","Global Financial Centres Index","Chỉ số Trung tâm Tài chính Toàn cầu"),
("H","Không có","Rổ cổ phiếu HOSE được ghép với rổ CS (ký hiệu của đề tài, khác với H1–H4 là ký hiệu các giả thuyết)"),
("HNX","Hanoi Stock Exchange","Sở Giao dịch Chứng khoán Hà Nội"),
("HOSE","Ho Chi Minh City Stock Exchange","Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh"),
("MQI","Market Quality Index","Chỉ số chất lượng thị trường vốn"),
("OECD","Organisation for Economic Co-operation and Development","Tổ chức Hợp tác và Phát triển Kinh tế"),
("OSF","Open Science Framework","Nền tảng khoa học mở"),
("SMD","Stock Market Development","Chỉ báo phát triển thị trường cổ phiếu"),
("UPCoM","Unlisted Public Company Market","Thị trường giao dịch cổ phiếu của công ty đại chúng chưa niêm yết"),
("VNX","Vietnam Exchange","Sở Giao dịch Chứng khoán Việt Nam"),
]
WID=[1400,3700,3688]
tree=etree.parse(f"{d}/word/document.xml"); root=tree.getroot()
tbl=None
for t in root.iter(q("tbl")):
    h=''.join(x.text or '' for x in t.find(q("tr")).iter(q("t")))
    if h.startswith("Chữ viết tắt"): tbl=t; break
old=tbl.findall(q("tr"))
tmpl_head, tmpl_row = old[0], old[1]
def mkrow(tmpl, vals):
    tr=copy.deepcopy(tmpl)
    tcs=tr.findall(q("tc"))
    for extra in tcs[1:]: tr.remove(extra)
    base=tcs[0]
    tr.remove(base)
    for v,w in zip(vals,WID):
        tc=copy.deepcopy(base)
        tc.find(q("tcPr")).find(q("tcW")).set(q("w"),str(w))
        p=tc.find(q("p")); runs=p.findall(q("r"))
        for r_ in runs[1:]: p.remove(r_)
        tt=runs[0].findall(q("t"))
        for t_ in tt[1:]: runs[0].remove(t_)
        tt[0].text=v; tt[0].set(XS,"preserve")
        tr.append(tc)
    return tr
for r_ in old: tbl.remove(r_)
tbl.append(mkrow(tmpl_head,["Chữ viết tắt","Tiếng Anh","Tiếng Việt"]))
for row in ROWS: tbl.append(mkrow(tmpl_row,list(row)))
grid=tbl.find(q("tblGrid"))
for gc in grid.findall(q("gridCol")): grid.remove(gc)
for w in WID: gc=etree.SubElement(grid,q("gridCol")); gc.set(q("w"),str(w))
tree.write(f"{d}/word/document.xml",xml_declaration=True,encoding="UTF-8",standalone=True)
print("abbr rows",len(ROWS))
