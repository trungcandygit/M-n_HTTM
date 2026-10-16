import json
E = []
def rep(i, old, new): E.append({"id": i, "op": "replace", "old": old, "new": new})
def md(i, anchor, text): E.append({"id": i, "op": "para_md", "anchor": anchor, "text": text})
def after(i, anchor, text): E.append({"id": i, "op": "new_para_md_after", "anchor": anchor, "text": text})
def split(i, anchor): E.append({"id": i, "op": "split_before", "anchor": anchor})
def dele(i, anchor): E.append({"id": i, "op": "delete_para", "anchor": anchor})

# ===== 1. Nội dung từ tài liệu mới (reports/doi-chieu-tai-lieu-vong8.md) =====
rep("S-GFCI",
    "Ở kỳ GFCI 40 (tháng 9/2026), Thành phố Hồ Chí Minh xếp thứ 67 trên 117 trung tâm, còn Đà Nẵng lần đầu vào chỉ số ở vị trí 71 (VietnamPlus, 2026a, 2026b) [CẦN ĐỐI CHIẾU báo cáo gốc]; thí sinh chưa thấy Hà Nội trong bảng xếp hạng.",
    "Ở kỳ GFCI 40 (tháng 9/2026), Thành phố Hồ Chí Minh xếp thứ 67 trên 117 trung tâm, Đà Nẵng lần đầu vào chỉ số ở vị trí 71, còn Hà Nội không có trong bảng xếp hạng (Wardle & Mainelli, 2026).")
rep("S-VNX",
    "Theo Thời báo Tài chính Việt Nam (2026), lịch do Sở Giao dịch Chứng khoán Việt Nam (VNX) công bố ngày 30/9/2026 ấn định phiên giao dịch cuối của cổ phiếu niêm yết tại HNX là ngày 23/12/2026 và ngày bắt đầu giao dịch trên HOSE là ngày 28/12/2026 [CẦN ĐỐI CHIẾU thông báo gốc của VNX].",
    "Theo thông báo của Sở Giao dịch Chứng khoán Việt Nam (VNX) ngày 30/9/2026, toàn bộ cổ phiếu niêm yết tại HNX giao dịch phiên cuối ngày 23/12/2026, tạm ngừng giao dịch hai ngày 24 và 25/12/2026, và giao dịch tại HOSE từ ngày 28/12/2026 (Sở Giao dịch Chứng khoán Việt Nam, 2026).")
rep("S-UPCoM",
    "Lịch chuyển UPCoM chưa được công bố tại thời điểm viết đề cương [CẦN XÁC MINH kế hoạch chuyển cổ phiếu đăng ký giao dịch do VNX xây dựng và báo cáo Ủy ban Chứng khoán Nhà nước theo khoản 4 Điều 4 Thông tư số 57/2021/TT-BTC].",
    "Thông báo của VNX chỉ áp dụng cho cổ phiếu niêm yết và nêu rõ giao dịch tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành; lịch chuyển cổ phiếu UPCoM chưa được công bố tại thời điểm viết đề cương [CẦN XÁC MINH kế hoạch chuyển cổ phiếu đăng ký giao dịch theo khoản 4 Điều 4 Thông tư số 57/2021/TT-BTC].")
rep("S-299",
    "Đợt hợp nhất ở Việt Nam đổi sàn của khoảng 300 doanh nghiệp trong cùng một ngày [CẦN ĐỐI CHIẾU danh sách VNX].",
    "Đợt hợp nhất ở Việt Nam đổi sàn của toàn bộ cổ phiếu niêm yết tại HNX, gồm 299 mã tính đến phiên 30/9/2026 (Tuổi Trẻ Online, 2026), trong cùng một ngày.")
rep("S-BSE",
    "Bắc Kinh là một trung tâm tài chính lớn dù không có sở giao dịch chứng khoán tầm quốc gia trong phần lớn giai đoạn phát triển của mình (Naeem, 2023) [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh].",
    "Bắc Kinh là một trung tâm tài chính lớn dù không có sở giao dịch chứng khoán tầm quốc gia trong phần lớn giai đoạn phát triển của mình (Naeem, 2023).")
rep("S-bien-do",
    "và do biên độ dao động giá khác nhau (HOSE ±7%, HNX ±10%, UPCoM ±15%) [CẦN XÁC MINH theo từng thời kỳ], nên",
    "và do biên độ dao động giá khác nhau giữa các sàn, hiện là ±7% ở HOSE, ±10% ở HNX và ±15% ở UPCoM; theo Điều 4 Thông tư số 120/2020/TT-BTC, biên độ do Sở giao dịch quyết định sau khi Ủy ban Chứng khoán Nhà nước chấp thuận (Bộ Tài chính, 2020) [CẦN XÁC MINH các lần thay đổi biên độ trong giai đoạn 2009–2025], nên")
rep("S-CDI",
    "(từ năm 2015 cùng China Development Institute)",
    "(hợp tác với China Development Institute từ năm 2016)")
rep("S-WFE",
    "trong đó có nhóm phát triển khu vực tài chính như khối lượng giao dịch, một phần lấy từ Liên đoàn các Sở Giao dịch Thế giới (Naeem, 2023),",
    "trong đó nhóm phát triển khu vực tài chính có vốn hóa, giá trị và khối lượng giao dịch cổ phiếu lấy từ Liên đoàn các Sở Giao dịch Thế giới (3 trong 144 nhân tố của kỳ GFCI 40; Wardle & Mainelli, 2026),")
rep("S-H1-overlap",
    "nếu trùng lặp ở phần lớn các kỳ, kết quả H1 được trình bày như liên hệ mô tả.",
    "vì kỳ GFCI 40 đã có trùng lặp (Wardle & Mainelli, 2026), đề tài ước lượng lại H1 trên các kỳ không trùng lặp nếu số kỳ đủ lớn, và trong mọi trường hợp gọi β là liên hệ có điều kiện, gồm cả phần cơ học này.")
rep("S-FTSE",
    "FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số theo bốn đợt từ tháng 9/2026 đến tháng 9/2027;",
    "FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số theo bốn đợt vào các tháng 9/2026, 3/2027, 6/2027 và 9/2027 (FTSE Russell, 2026);")
rep("S-bang",
    "HOSE phân loại cổ phiếu vào Bảng Chính và Bảng Tiêu chuẩn từ ngày 28/12/2026;",
    "theo dự thảo quy chế mà VNX đang lấy ý kiến, HOSE dự kiến công bố kết quả phân loại cổ phiếu vào Bảng Chính và Bảng Tiêu chuẩn lần đầu ngày 28/12/2026 (Tuổi Trẻ Online, 2026);")
rep("S-299b", "và HOSE tiếp nhận khoảng 300 mã,", "và HOSE tiếp nhận 299 mã,")
rep("S-labels",
    "[CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn] [CẦN XÁC MINH các mốc FTSE và phân bảng].",
    "[CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong VN-Index và quy chế phân bảng chính thức].")
rep("S-UBCK", "so với xu hướng trước của chính nhóm đó.",
    "so với xu hướng trước của chính nhóm đó. Ngoài ra, Ủy ban Chứng khoán Nhà nước cho biết đang nghiên cứu nới biên độ dao động giá và giao dịch xuyên trưa (Thời báo Tài chính Việt Nam, 2026); nếu các thay đổi này được áp dụng trong cửa sổ sau sự kiện, chúng tác động như nhau lên cổ phiếu chuyển sàn và nhóm đối chứng HOSE, và ngưỡng lợi suất chung khi tính Amihud được đặt thấp hơn biên độ hẹp nhất có hiệu lực trong toàn mẫu.")
rep("S-MDE1", "giai đoạn trước dài 193 tháng (6/2009–6/2025),", "cửa sổ trước dài 193 tháng (6/2009–6/2025),")
rep("S-MDE2", "1,24σ khi φ = 0,6 và 1,76σ khi φ = 0,8.",
    "1,24σ khi φ = 0,6 và 1,76σ khi φ = 0,8. Nếu cửa sổ trước được rút ngắn do điểm gãy cấu trúc, hiệu ứng nhỏ nhất phát hiện được tăng lên, khoảng 1,3 lần khi cửa sổ trước chỉ còn 24 tháng.")

# ===== 2. Độ khớp với NQ 57 và Thông báo 7215 =====
rep("F-users",
    "Người dùng dự kiến của kết quả gồm Ủy ban nhân dân thành phố Hà Nội, Ủy ban Chứng khoán Nhà nước, HNX, HOSE và các tổ chức đầu tư.",
    "Người dùng dự kiến của kết quả gồm Sở Khoa học và Công nghệ Hà Nội, cơ quan đầu mối theo dõi và đánh giá kết quả thực hiện Danh mục các bài toán lớn (Ủy ban nhân dân thành phố Hà Nội, 2026, Điều 3), Ủy ban nhân dân thành phố Hà Nội, Ủy ban Chứng khoán Nhà nước, HNX, HOSE và các tổ chức đầu tư. Trước khi nộp hồ sơ đề nghị hỗ trợ, thí sinh sẽ xin văn bản xác nhận nhu cầu sử dụng kết quả của ít nhất một đơn vị trong số này.")
A92 = "Hai chỉ số và tệp đăng ký trước là sản phẩm có được dù kết quả kiểm định ra sao."
items = [
    "Kết quả của đề tài được kiểm chứng bằng sáu chỉ tiêu; mỗi chỉ tiêu có mốc thời gian và bằng chứng công khai:",
    "(1) Tệp đăng ký trước kế hoạch phân tích trên OSF Registries, khóa có dấu thời gian trước ngày 28/12/2026.",
    "(2) Chỉ số chất lượng thị trường vốn theo tháng cho sàn niêm yết HNX, UPCoM và HOSE từ tháng 6/2009, công bố cùng mã nguồn trên kho lưu trữ mở.",
    "(3) Ước lượng tác động của việc chuyển sàn lên thanh khoản với 24 tháng dữ liệu sau sự kiện, báo cáo kèm hiệu ứng nhỏ nhất phát hiện được và khoảng tin cậy, theo đúng tệp đăng ký.",
    "(4) Chỉ số khả năng đầu tư của rổ cổ phiếu chuyển sàn trên bảy mô hình phân bổ, cho 20 cửa sổ trước và 8 cửa sổ sau sự kiện.",
    "(5) Ba bài báo trên tạp chí có phản biện, với mục tiêu ít nhất một bài thuộc cơ sở dữ liệu Web of Science hạng Q1 hoặc Q2, và một đến hai báo cáo hội thảo.",
    "(6) Báo cáo định hướng chuyên môn hóa cho các thị trường do HNX tiếp tục vận hành, gửi Sở Khoa học và Công nghệ Hà Nội trong năm thứ tư.",
]
prev = A92
for k, t in enumerate(items):
    E.append({"id": f"F-item{k}", "op": "new_para_md_after", "anchor": prev, "text": t})
    prev = t
rep("F-papers", "Số bài là mục tiêu;", "Mục tiêu là ít nhất một bài thuộc cơ sở dữ liệu Web of Science hạng Q1 hoặc Q2. Số bài là mục tiêu;")
rep("F-bang5", "Bài báo 3; luận án; hai chỉ số mã nguồn mở",
    "Bài báo 3; báo cáo định hướng chuyên môn hóa gửi Sở Khoa học và Công nghệ Hà Nội; luận án; hai chỉ số mã nguồn mở")

# ===== 3. Danh mục =====
md("R-NQ222", "Quốc hội. (2025). Nghị quyết số 222/2025/QH15",
   "Quốc hội. (2025). *Nghị quyết số 222/2025/QH15 ngày 27/6/2025 về Trung tâm tài chính quốc tế tại Việt Nam*.")
md("R-NQ57", "Hội đồng nhân dân thành phố Hà Nội. (2026).",
   "Hội đồng nhân dân thành phố Hà Nội. (2026). *Nghị quyết số 57/2026/NQ-HĐND ngày 15/6/2026 quy định một số chính sách phát triển nguồn nhân lực chất lượng cao của Thành phố*.")
md("R-TBTC", "Thời báo Tài chính Việt Nam. (2026).",
   "Thời báo Tài chính Việt Nam. (2026). Chuyển toàn bộ cổ phiếu HNX sang HOSE trong năm 2026, nghiên cứu giao dịch xuyên trưa và nới biên độ. *Thời báo Tài chính Việt Nam*. https://thoibaotaichinhvietnam.vn/chuyen-toan-bo-co-phieu-hnx-sang-hose-trong-nam-2026-nghien-cuu-giao-dich-xuyen-trua-va-noi-bien-do-204943.html")
after("R-TTO", "Thời báo Tài chính Việt Nam. (2026). Chuyển toàn bộ",
      "Tuổi Trẻ Online. (2026). HOSE chia cổ phiếu thành hai bảng Prime Board và Standard Board. *Tuổi Trẻ Online*. https://tuoitre.vn/hose-du-kien-chia-co-phieu-thanh-hai-bang-prime-board-va-standard-board-100261002092239776.htm")
after("R-VNX", "Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh. (2026).",
      "Sở Giao dịch Chứng khoán Việt Nam. (2026). *Sắp xếp lại thị trường giao dịch cổ phiếu niêm yết theo Thông tư số 139/2025/TT-BTC ngày 30/12/2025 của Bộ Tài chính* [Thông báo ngày 30/9/2026]. https://vnx.vn/vi/thong-tin-tu-sgdck/VNX_QLHD/10005421")
# TT120: viết đè mục VBHN 2023 thành TT120 rồi chèn lại VBHN sau nó
VBHN = "Bộ Tài chính. (2023). *Văn bản hợp nhất số 19/VBHN-BTC ngày 25/12/2023 hợp nhất Thông tư quy định lộ trình sắp xếp lại thị trường giao dịch cổ phiếu, thị trường giao dịch trái phiếu, thị trường giao dịch chứng khoán phái sinh và thị trường giao dịch các loại chứng khoán khác* (hợp nhất Thông tư số 57/2021/TT-BTC ngày 12/7/2021 và Thông tư số 69/2023/TT-BTC ngày 15/11/2023)."
md("R-TT120", "Bộ Tài chính. (2023). Văn bản hợp nhất số 19",
   "Bộ Tài chính. (2020). *Thông tư số 120/2020/TT-BTC ngày 31/12/2020 quy định giao dịch cổ phiếu niêm yết, đăng ký giao dịch và chứng chỉ quỹ, trái phiếu doanh nghiệp, chứng quyền có bảo đảm niêm yết trên hệ thống giao dịch chứng khoán*.")
after("R-VBHN", "Bộ Tài chính. (2020). Thông tư số 120", VBHN)
dele("R-VNP-a", "VietnamPlus. (2026a).")
dele("R-VNP-b", "VietnamPlus. (2026b).")
after("R-FTSE", "Fong, K. Y. L., Holden, C. W., & Trzcinka",
      "FTSE Russell. (2026). *Reclassification of Vietnam from Frontier to Secondary Emerging market status: Frequently asked questions* (Version 1.3). LSEG.")
after("R-GFCI", "Wang, D. T., Zhao, S. X., & Wang, D. (2007).",
      "Wardle, M., & Mainelli, M. (2026). *The Global Financial Centres Index 40*. Z/Yen Group & China Development Institute.")

# ===== 4. Tách đoạn dài (mỗi đoạn một ý) =====
for i, a in enumerate([
    "Chất lượng thị trường vốn gồm ba chiều",
    "Hợp nhất sàn là việc chuyển toàn bộ cổ phiếu niêm yết",
    "Lộ trình sắp xếp lại thị trường được quy định",
    "Văn bản hợp nhất cũng quy định HNX hoàn thành việc chuyển cổ phiếu của tổ chức đăng ký",
    "Cặp Hà Nội và Thành phố Hồ Chí Minh có thể so sánh",
    "Nielsson (2009) thấy việc hình thành Euronext",
    "Đợt hợp nhất ở Việt Nam đổi sàn",
    "Naeem (2023) dùng dữ liệu 196",
    "Về hiệu quả thông tin, Lo và MacKinlay",
    "Nielsson (2009) thấy lợi ích thanh khoản",
    "Bước giá cũng khác nhau giữa các sàn",
    "Với H3, biên độ giảm",
    "Với H4, quy tắc 1/N",
    "Bộ dữ liệu Việt Nam gồm giá",
    "Chiều hiệu quả thông tin gồm",
    "Các chỉ báo cổ phiếu được gộp",
    "Đề tài kiểm định H2 bằng chuỗi",
    "Tệp đăng ký cố định các nội dung sau",
    "Rổ CS gồm tối đa 30",
    "Nhóm đối chứng chính gồm cổ phiếu HOSE",
    "Vì mọi cổ phiếu chuyển sàn cùng một ngày, suy luận chính",
    "Suy luận trên các ngày giả định",
    "Sai số chuẩn được phân cụm theo quốc gia.",
    "Thứ hai, nhóm đối chứng không chịu",
    "Amihud và cộng sự (1997) ghi nhận thanh khoản lan tỏa",
    "Thứ ba, việc rời mẫu",
    "Với giả định chuỗi chênh lệch",
    "H4 có ít cửa sổ nên",
    "Ở H1, đề tài kiểm tra độ bền",
    "Nếu dữ liệu không ủng hộ giả thuyết",
    "Nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt",
    "Các mã đã tự chuyển sàn trước năm 2026 còn",
    "Thí sinh đang theo học ngành Kế toán",
    "Nếu trúng tuyển, thí sinh cam kết",
    "Về ngoại ngữ, thí sinh",
]):
    split(f"SP{i:02d}", a)

json.dump(E, open("/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r9/edits-r9.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E))
