# Cổng đóng 1, agent B: xác minh pháp lý, dữ kiện, trích dẫn và nhất quán nội bộ của đề cương v14

Văn bản rà: `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r14/v14-text.txt` (đánh số [idx]). Ngày rà: 17/10/2026.
Agent không sửa tệp đề cương, không gọi mạng với câu chữ đề cương và không chạy script nào của dự án hay của skill. Chỉ đọc tệp bằng Read/grep/sed. Riêng bước kiểm tính duy nhất của chuỗi gốc dùng `grep -F` trên v14-text.txt.

Tóm tắt: **0 CRITICAL, 3 MAJOR, 18 MINOR.** Mọi khẳng định pháp lý về lộ trình (TT 57/2021, TT 69/2023, TT 139/2025), lịch VNX, TT 120/2020, NQ 222/2025, NQ 57/2026 (Điều 11.3, 12.3, 13, 15.2.e) và QĐ 1193/2026 đều KHỚP với văn bản gốc. Ba lỗi MAJOR là:
- trích dẫn con số 299 mã trỏ nhầm bài báo;
- quy tắc ngưỡng Amihud mới của v14 sai ở cổ phiếu giá rất thấp;
- trình tự thời gian của phương án UPCoM ở mục 4.3.10 không khớp với chính mốc 31/12/2026.

---

## 1. Bằng chứng tuân thủ

Gọi các skill tuần tự qua công cụ Skill, theo đúng thứ tự được giao. Không skill nào báo lỗi khi tải.

| # | Skill | Việc đã làm | Giới hạn, lỗi |
|---|---|---|---|
| 1 | vn-legal-verify | Làm đủ Bước 1–6. Liệt kê mọi khẳng định pháp lý và quy chế sở giao dịch. Định danh văn bản và dựng chuỗi sửa đổi TT 57 → TT 69 → TT 139. Trích nguyên văn TT 57 (caselaw.vn), TT 69 và TT 139 (bản quét có OCR), VBHN 19, thông báo VNX trên vnx.vn, TT 120 Điều 4, NQ 222, QĐ 737 (OCR). Đọc trực tiếp bản PDF NQ 57/2026 (sao y ngày 24/6/2026, trang 1, 11–13) và QĐ 1193/2026 (trang 1–2, 8). Đọc V1, V3, V4, V5, V6. Gắn trạng thái ở Mục 2. | Không có |
| 2 | fact-checker | Thang TRUE/MIXED/UNVERIFIABLE được quy về KHỚP/LỆCH/CHƯA CÓ NGUỒN ở Mục 2. Tính lại các con số: 193 tháng, 18 tháng, 24 tháng, 20 và 8 cửa sổ, J = 6 cùng tổng trọng số bằng 1, MDE 0,64σ/1,24σ/1,76σ, hệ số 1,3, mức 0,25 tương đương 22%. Kiểm bước giá, biên độ, xếp hạng GFCI, 299 mã, lịch VNX, lịch FTSE. | Không gọi mạng |
| 3 | credible-claims | Soát xem nhận định có vượt bằng chứng không. Soát từng chỗ dùng báo chí: idx73, 75, 185, 187, 204. Tách phần suy diễn (FTSE idx171, bước giá idx117, VN-Index idx185) khỏi phần đã có nguồn. | Không có |
| 4 | consistency-checker | Áp checklist 10 nhóm bằng tay: bảng, hình, phương trình (1)–(7), mục, ký hiệu, cỡ mẫu, ngày tháng, mục lục, danh mục bảng/hình, chữ viết tắt, nhãn [CẦN…]. | Không chạy `scripts/latex_extractor.py` vì đề cương là .docx và lệnh cấm chạy script |
| 5 | citation-management | Chỉ đọc. Khớp hai chiều trích dẫn trong bài với danh mục, kiểm APA 7, a/b cùng năm, DOI theo metadata Crossref có sẵn (mục X trong Vòng 12). | Bỏ qua Phase 1–2.5 và mọi script (cần mạng). Không bổ sung DOI nào ngoài hồ sơ. Không chèn trích dẫn K-Dense vào đề cương. |
| 6 | research-grants | Đối chiếu tiêu chí xét chọn (mục tiêu đo được, khả thi, sản phẩm, đơn vị tiếp nhận) với NQ 57/2026 (Điều 11.3, 12.2, 12.3, 13, 15.2.e), QĐ 1193 (bài toán 19, Điều 3) và Thông báo 7215 qua bản tóm tắt PTIT. | Các mẫu NSF/NIH không áp dụng |
| 7 | scientific-critical-thinking | Xếp mức bằng chứng cho từng nhóm khẳng định: bậc 1 là văn bản ký số hoặc trang cơ quan; bậc 5 là báo chí (cột "Bậc" ở Mục 2). Soát logic thiết kế (ngưỡng Amihud, trình tự UPCoM, kênh biên độ). | Không vẽ hình; không dùng OpenRouter |
| 8 | academic-paper (citation-check) | Nạp `agents/citation_compliance_agent.md` và áp mục 1–4 của Verification Checklist. Phát hiện thứ tự trích dẫn nhiều nguồn trong ngoặc chưa theo bảng chữ cái, thiếu DOI và thiếu ngày của bài báo. | Không auto-correct vào tệp (chế độ chỉ đọc); không kiểm Retraction Watch (cần mạng) |
| 9 | deep-research (fact-check) | Chạy chế độ fact-check, chỉ trên các tệp trong `ho-so/`. Áp checklist của source_verification_agent trong cùng ngữ cảnh: xếp bậc nguồn, đặt cờ nguồn thứ cấp (V3/V4 của công ty chứng khoán, W02 báo chí). | Môi trường không có công cụ tạo agent con, nên không dispatch được agent riêng; đã áp checklist trong một ngữ cảnh |
| 10 | peer-review | Kiểm claim–evidence. Chủ sở hữu tài liệu là thí sinh (đề cương của chính người dùng), xử lý cục bộ. Ma trận claim–evidence nằm ở Mục 2 và 4. | Không chạy `validate_review_intake.py`, `validate_claim_evidence.py`, `lint_review.py` (cấm chạy script); đã áp checklist thủ công |
| 11 | proposal-revise | Chỉ đánh giá, không ghi tệp, không tạo .bak. Đánh giá mức khớp với hồ sơ đề nghị hỗ trợ (Mục 5). | Không đọc `~/.claude-assistant/donors/` vì hạn chế cục bộ S5 và người dùng không yêu cầu; dùng NQ 57, QĐ 1193 và TB 7215 làm "donor profile" |

---

## 2. Bảng đối chiếu pháp lý và dữ kiện

Bậc nguồn: 1 = bản ký số hoặc trang chính thức; 2 = toàn văn đăng lại; 3 = OCR bản quét; 4 = tóm tắt của công ty chứng khoán; 5 = báo chí; X = metadata Crossref.

| # | Khẳng định | idx | Nguồn | Bậc | Trạng thái | Trích nguyên văn ngắn |
|---|---|---|---|---|---|---|
| 1 | Hạn chuyển cổ phiếu niêm yết là năm 2023 theo TT 57/2021 | 72 | TT 57 Điều 4.3.d | 2 | KHỚP | "Từ ngày 01 tháng 7 năm 2023 đến hết ngày 31 tháng 12 năm 2023: Sở Giao dịch Chứng khoán Hà Nội thực hiện chuyển cổ phiếu của tổ chức niêm yết" |
| 2 | Hạn là hết năm 2025 theo TT 69/2023 | 72 | TT 69 Điều 1.3 (sửa điểm d khoản 3 Điều 4) | 3 | KHỚP | "d) Chậm nhất đến hết ngày 31 tháng 12 năm 2025: … hoàn thành việc chuyển cổ phiếu của tổ chức niêm yết" |
| 3 | Hạn là 31/12/2026 theo TT 139/2025 | 72 | TT 139 Điều 1.2 | 3 (ký số 05/01/2026) | KHỚP | "d) Chậm nhất đến hết ngày 31 tháng 12 năm 2026: Sở Giao dịch Chứng khoán Hà Nội hoàn thành việc chuyển cổ phiếu của tổ chức niêm yết" |
| 4 | Hạn UPCoM 31/12/2026 do TT 69 đặt, TT 139 không sửa | 73, 204 | TT 69 Điều 1.3.e; TT 139 chỉ sửa điểm đ khoản 2 và điểm d khoản 3 | 3 | KHỚP | TT 69: "e) Chậm nhất đến hết ngày 31 tháng 12 năm 2026: … hoàn thành việc chuyển cổ phiếu của tổ chức đăng ký giao dịch". Câu ở idx73 chỉ dẫn (Bộ Tài chính, 2023); vế "không bị TT 139 sửa" nên dẫn thêm 2025 (m2) |
| 5 | VNX xây dựng kế hoạch theo khoản 4 Điều 4 TT 57 (nhãn) | 73 | TT 57 Điều 4.4 (TT 69 và TT 139 không sửa khoản này) | 2 | KHỚP | "Sở Giao dịch Chứng khoán Việt Nam xây dựng kế hoạch chuyển cổ phiếu của tổ chức niêm yết, đăng ký giao dịch … và báo cáo Ủy ban Chứng khoán Nhà nước trước khi triển khai." |
| 6 | VNX 30/9/2026: phiên cuối 23/12, tạm ngừng 24–25/12, sang HOSE từ 28/12/2026 | 72 | Thông báo trên vnx.vn, 08:51 30/09/2026 | 1 | KHỚP | "Ngày giao dịch cuối cùng của toàn bộ cổ phiếu niêm yết tại HNX: ngày 23/12/2026" … "là ngày 28/12/2026" |
| 7 | Thông báo VNX chỉ áp dụng cho cổ phiếu niêm yết | 73 | như trên | 1 | KHỚP | "Giao dịch chứng khoán tại HOSE và giao dịch chứng khoán tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành." |
| 8 | Đợt 28/12/2026 không gồm UPCoM | 73 (có rào đón), 204 (khẳng định) | W02 Báo ĐTCK, 06/10/2026, tác giả Nguyễn Huyền | 5 | KHỚP (báo chí); nguồn chính là VNX #7 | "Việc chuyển cổ phiếu từ HNX sang HOSE không bao gồm UPCoM"; "UPCoM không thuộc diện chuyển giao". Ở idx204 báo chí đứng một mình cho một khẳng định chắc chắn (m1) |
| 9 | Chưa có văn bản công bố lịch chuyển UPCoM | 73 | Ghi chú Vòng 12 mục [73]; W03–W06 | – | KHỚP (vắng nguồn, nhãn còn đúng) | "Không tìm thấy lịch chuyển UPCoM do VNX công bố" |
| 10 | HNX ngừng nhận niêm yết mới từ 01/7/2025 | 125 | TT 69 Điều 1.3.c | 3 | KHỚP, nhưng thiếu trích dẫn (m3) | "c) Từ ngày 01 tháng 7 năm 2025: Sở Giao dịch Chứng khoán Hà Nội không tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới của tổ chức" |
| 11 | Thị trường do HNX tiếp tục vận hành: trái phiếu, phái sinh, UPCoM | 70 | TT 57 Điều 5, 6; TT 69 Điều 1.3.e | 2 | KHỚP | "Sở Giao dịch Chứng khoán Hà Nội tổ chức thị trường giao dịch chứng khoán phái sinh" |
| 12 | Tiêu đề VBHN 19/VBHN-BTC ngày 25/12/2023 | 265 | TONG_HOP mục 03 (hethongphapluat) | 2 | KHỚP | "Số hiệu: 19/VBHN-BTC … Ngày ban hành: 25/12/2023". VBHN chưa gồm TT 139, và đề cương đã dẫn TT 139 riêng (đúng) |
| 13 | Trích yếu TT 139/2025 | 266 | TT 139 (OCR) + tiêu đề thông báo VNX | 3, 1 | KHỚP | "sửa đổi, bổ sung một số điều của Thông tư số 57/2021/TT-BTC … được sửa đổi, bổ sung bởi Thông tư số 69/2023/TT-BTC ngày 15 tháng 11 năm 2023" |
| 14 | Biên độ do VNX quyết định sau khi UBCKNN chấp thuận; UBCKNN được điều chỉnh khi cần | 116 | TT 120/2020 Điều 4 | 2 | KHỚP | "1. Sở giao dịch chứng khoán Việt Nam quyết định biên độ dao động giá sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận. 2. Trong trường hợp cần thiết để ổn định thị trường, Ủy ban Chứng khoán Nhà nước quyết định điều chỉnh biên độ" |
| 15 | Biên độ ±7% HOSE, ±10% HNX, ±15% UPCoM | 116, 119 | V1 mục 4; V3 mục 5.B; V4 mục 6; V5 mục 6 | 4 | KHỚP (mức hiện hành); lịch sử 2009–2025 vẫn để nhãn | V1: "+/-7% so với giá tham chiếu"; V3: "niêm yết là ± 10% và trên sàn Upcom là ± 15%" |
| 16 | Bước giá HOSE: 10/50/100 đồng (dưới 10.000 / 10.000–49.950 / từ 50.000) | 117 | V1 mục 3 | 4 (văn bản HOSE đăng lại qua FPTS) | KHỚP | "<10.000 10 đồng; 10.000-49.950 50 đồng; ≥ 50.000 100 đồng" |
| 17 | Bước giá HNX 100 đồng cho mọi mức giá (nhãn CẦN ĐỐI CHIẾU) | 117 | V3 mục 4.B; V4 mục 5; V6 (QĐ 529/QĐ-SGDHN ngày 25/8/2016, hiệu lực 12/9/2016, chỉ đổi bước giá ETF) | 4 | KHỚP MỘT PHẦN, giữ nhãn đúng | V3: "Giao dịch khớp lệnh 100 đồng"; V4: "Cổ phiếu: 100 đồng" |
| 18 | Chuyển sàn làm bước giá giảm mười lần / một nửa / không đổi | 117 | Suy ra từ #16 và #17 | – | SUY DIỄN đúng số học (100→10, 100→50, 100→100) | Phụ thuộc nhãn #17. Trước 12/9/2016 HOSE cũng dùng 100 đồng cho mã dưới 10.000 (W07, CafeF 25/8/2016: "Với cổ phiếu có mức giá từ 50.000 đồng trở lên, đơn vị yết giá sẽ giống với HNX là 100 đồng"; ví dụ giá 9.000 chỉ có các mức 9,1; 9,2…), nên chênh lệch bước giá giữa hai sàn chỉ có từ 9/2016 (m11) |
| 19 | Làm tròn giá trần xuống, giá sàn lên theo đơn vị yết giá của HOSE | 120 | V1 mục 5.1 | 4 | KHỚP về quy tắc; câu suy ra "mức lợi suất lớn nhất" chưa đúng ở mã giá thấp (M2) | "làm tròn xuống đối với giá trần, làm tròn lên đối với giá sàn theo đơn vị yết giá"; 5.1.b: "Giá trần điều chỉnh = Giá tham chiếu + 01 đơn vị yết giá" |
| 20 | FTSE Ground Rules coi cả HOSE và HNX (Main market) là sàn đủ điều kiện | 171 | V7, Ground Rules v14.4, 9/2026, Appendix A | 1 | KHỚP | "Vietnam   Ho Chi Minh Stock Exchange   Main market / Hanoi Stock Exchange   Main market" |
| 21 | Vì vậy việc đổi sàn tự nó không đổi tư cách sàng lọc | 171 | suy diễn từ #20 | – | SUY DIỄN hợp lý | Đề cương đã có phương án loại mã nếu được đưa vào chỉ số ở kỳ sau |
| 22 | Danh sách đủ điều kiện, dữ liệu đến 30/6/2026, chỉ gồm mã HOSE | 171 | FAQ v1.3 (8/2026) Q6; W15 | 1 / 5 | KHỚP | FAQ: "based on data cut-off as of 30 June 2026"; cột Exchange: "HSX"; W15: "All the stocks are listed on the Ho Chi Minh Stock Exchange (HoSE)." |
| 23 | Bốn đợt từ 9/2026 đến 9/2027 | 185 | FAQ Q4 | 1 | KHỚP | "four‑tranche phased implementation beginning in September 2026 and concluding in September 2027" |
| 24 | FTSE (2026a) là Ground Rules, (2026b) là FAQ | 298, 299 | Tiêu đề hai tài liệu | 1 | KHỚP; thứ tự a/b đúng APA (F… trước R…) | "FTSE Global Equity Index Series, v14.4, September 2026"; "FAQ, v1.3, August 2026" |
| 25 | GFCI 40: TP.HCM hạng 67/117, Đà Nẵng lần đầu ở hạng 71, không có Hà Nội | 71 | Báo cáo GFCI 40 | 1 | KHỚP | "number of centres in the main index is 117"; "Da Nang entered the index for the first time in 71st position"; không có "Hanoi" trong văn bản |
| 26 | 3 trong 144 nhân tố là vốn hóa, giá trị và khối lượng giao dịch cổ phiếu của WFE | 182 | GFCI 40, Table 26 | 1 | KHỚP | "GFCI 40 was compiled using 144 instrumental factors"; "Capitalisation Of Stock Exchanges … Value Of Share Trading, Volume Of Share Trading" |
| 27 | Z/Yen công bố GFCI từ năm 2007 | 123 | GFCI 40 | 1 | KHỚP | "In March 2007, Z/Yen and the City Of London released the first edition" |
| 28 | NQ 222/2025: TTTCQT đặt tại TP.HCM và Đà Nẵng; ngày 27/6/2025 | 71, 84, 269 | NQ 222 toàn văn | 2 | KHỚP | "đặt tại Thành phố Hồ Chí Minh và thành phố Đà Nẵng"; "thông qua ngày 27 tháng 6 năm 2025" (báo cáo vòng 8) |
| 29 | Hồ sơ có 299 mã niêm yết tại HNX tính đến phiên 30/9/2026 | 75 | W05, Tuổi Trẻ 30/09/2026, "Toàn bộ cổ phiếu trên HNX sẽ chuyển sang HOSE từ 28-12" | 5 | Con số KHỚP; trích dẫn LỆCH (M1) | "Tính đến phiên 30-9, HNX có 299 mã cổ phiếu niêm yết". Mục Tuổi Trẻ Online (2026) duy nhất trong danh mục là bài Prime Board; bài đó không chứa "299" |
| 30 | HOSE dự kiến công bố phân bảng lần đầu ngày 28/12/2026, theo dự thảo | 185 | Tuổi Trẻ (Prime Board), Vòng 8 [17] | 5 | KHỚP (dự thảo, đã rào đón) | "HOSE dự kiến công bố kết quả phân loại lần đầu vào ngày 28-12-2026" |
| 31 | VN-Index tự cập nhật danh mục sau ngày giao dịch đầu tiên của cổ phiếu niêm yết mới; không điều chỉnh free-float | 170, 185 | QĐ 737 (OCR) mục 2 | 3 | KHỚP. Áp quy tắc sang mã chuyển sàn là suy diễn, nhãn còn đúng | "Danh mục cổ phiếu thành phần của chỉ số được tự động cập nhật sau ngày giao dịch đầu tiên của cổ phiếu niêm yết mới"; "không điều chỉnh tỷ lệ free-float" |
| 32 | Số hiệu và ngày QĐ 737 | 271 | QĐ 737 (OCR đọc "3157 … 23 tháng 9"); tên tệp VNX: 737, 29/9/2026 | 3 | CHƯA GIẢI, nhãn còn đúng | Căn cứ CV 1314 ngày 25/9/2026 nên ngày ký không thể là 23/9 |
| 33 | UBCKNN nghiên cứu nới biên độ và giao dịch xuyên trưa | 187 | Thời báo Tài chính (họp báo BTC 6/10/2026) | 5 | KHỚP (đã rào đón "đang nghiên cứu") | "Ủy ban Chứng khoán Nhà nước đang nghiên cứu nhiều nội dung như: giao dịch xuyên trưa, nới biên độ dao động giá" |
| 34 | NQ 57/2026: số hiệu, ngày 15/6/2026, trích yếu | 267 | PDF NQ 57 (sao y 24/6/2026), trang 1 | 1 | Số và ngày KHỚP; trích yếu LỆCH nhẹ (m5) | "Quy định một số chính sách phát triển nguồn nhân lực chất lượng cao của thành phố Hà Nội" |
| 35 | Điều 11.3: tập trung toàn thời gian | 251 | NQ 57, trang 12 | 1 | KHỚP | "3. Theo học chương trình đào tạo tiến sĩ và tương đương, tập trung toàn thời gian, có chuyên ngành đào tạo và nội dung nghiên cứu của luận án tiến sĩ phục vụ giải quyết bài toán lớn của Thành phố" |
| 36 | Điều 13: tối đa 48 tháng | 234 | NQ 57, trang 12 | 1 | KHỚP | "là thời gian đào tạo trình độ tiến sĩ theo quy định của cơ sở đào tạo nhưng không vượt quá 48 tháng" |
| 37 | Mục tiêu ≥1 bài WoS Q1/Q2, thí sinh là tác giả chính | 90, 232 | NQ 57 Điều 12.3 | 1 | KHỚP | "nếu người học là tác giả chính được đăng trên tạp chí khoa học hạng Q2 thuộc cơ sở dữ liệu Web of Science" |
| 38 | "Một đến hai báo cáo hội thảo" | 90, 232 | NQ 57 Điều 12.2 | 1 | KHỚP MỘT PHẦN: chưa nêu loại kỷ yếu được hỗ trợ (m12) | "đăng trong kỷ yếu hội nghị, hội thảo được Hội đồng Giáo sư nhà nước tính điểm"; "thuộc cơ sở dữ liệu Scopus hoặc Web of Science" |
| 39 | Nghĩa vụ điểm e khoản 2 Điều 15 | 255 | NQ 57, trang 13 | 1 | KHỚP (diễn đạt lại, giữ nghĩa) | "e) Tham gia mạng lưới chuyên gia khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số của thành phố Hà Nội sau khi hoàn thành chương trình đào tạo; tham gia tư vấn, phản biện, cung cấp luận cứ khoa học hỗ trợ chuyên môn đối với bài toán lớn …" |
| 40 | QĐ 1193 ngày 18/3/2026, trích yếu | 275 | PDF QĐ 1193, trang 1 | 2 | KHỚP | "về việc công bố Danh mục các bài toán lớn của thành phố Hà Nội giai đoạn 2026 - 2030 (đợt 1)" |
| 41 | Bài toán 19, câu hỏi 1–4, sản phẩm "Hệ thống dữ liệu tài chính đô thị" và "Trung tâm tài chính quốc tế tại Hà Nội" | 68, 84, 213 | QĐ 1193 Phụ lục, trang 8 | 2 | KHỚP | "Phương thức nào để xây dựng Hà Nội thành trung tâm tài chính và dịch vụ chất lượng cao quốc tế?"; "3. Những nền tảng công nghệ nào giúp tăng cường minh bạch và hiệu quả của thị trường tài chính?" |
| 42 | Sở KH&CN là cơ quan đầu mối theo dõi, đánh giá (Điều 3) | 213 | QĐ 1193 Điều 3.1 | 2 | KHỚP | "Sở Khoa học và Công nghệ là cơ quan đầu mối … theo dõi, đánh giá tiến độ và kết quả thực hiện" |
| 43 | Naeem (2023): 196 trung tâm, 2007–2020, 17 yếu tố, cây quyết định, không có chỉ báo cổ phiếu | 94 | TONG_HOP mục 09 | 2 | KHỚP MỘT PHẦN | "Data is collected for 196 countries and paper used Decision tree approach"; "we used only 17 variables due to data availability" (nguồn tự ghi 197 ở một chỗ) |
| 44 | Hisada (2018): hợp nhất 16/7/2013; thanh khoản tăng ngắn hạn rồi giảm sau một năm; hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ | 97 | TONG_HOP mục 08 | 1 | KHỚP | "integrated on July 16, 2013"; "liquidity decreases 1 year after the merger"; "The investor sentiment effect occurs more strongly in small stocks." |
| 45 | Nielsson (2009): lợi ích ở doanh nghiệp lớn và có doanh thu nước ngoài | 97 | Vòng 8 [37] (working paper) | 2 | KHỚP | "concentrated among big firms and firms with foreign sales" |
| 46 | Amihud và cộng sự (1997): CAR khoảng 5,5% | 96 | – | – | CHƯA CÓ NGUỒN trong hồ sơ (C4: bài bị khóa) | Không sửa; cần bản bài để đối chiếu |
| 47 | Eichengreen & Shah (2020) chia yếu tố thành năm nhóm | 93 | W13 (vLex, chỉ phần mở đầu) | – | CHƯA CÓ NGUỒN đầy đủ | Thứ tự tác giả và chi tiết thư mục KHỚP Crossref: "Eichengreen, Barry [first] ; Shah, Nachiket"; RIE 28(1) 62–81 |
| 48 | Daw & Hatfield (2018), DOI 10.1111/1475-6773.12993 | 293 | Crossref (X), PubMed (W12) | X | KHỚP | "Health Services Research, Vol 53, Issue 6, Pages 4138-4156" |
| 49 | Mẫu bắt đầu 6/2009, khi UPCoM bắt đầu giao dịch | 125 | Không có văn bản HNX; W10 (blog) ghi "Sàn chứng khoán Upcom ra đời ngày 01/01/2009" | 5 | CHƯA CÓ NGUỒN bậc cao; nguồn bậc thấp có câu khác (m4) | – |
| 50 | Thời gian đào tạo 4 năm; giảng dạy bằng tiếng Anh hoặc tiếng Việt; Nhóm 1, 9 tín chỉ | 221, 222, 228, 234 | Thông báo tuyển sinh không có trong hồ sơ (Vòng 8 A11: KHÔNG) | – | CHƯA CÓ NGUỒN (m18) | – |
| 51 | Các con số MDE ở idx198–199 | 198, 199 | Tính lại theo AR(1), α = 0,05/3 một phía, lực kiểm định 80% | – | KHỚP | φ=0: 2,97·√(1/24+1/193) = 0,643σ; φ=0,6: ≈1,24σ; φ=0,8: ≈1,76σ; cửa sổ trước 24 tháng thì MDE gấp ≈1,33 lần; 1,24×0,2 = 0,248; e^(−0,25) ≈ 0,78, tức giảm 22% |
| 52 | Số cửa sổ và độ dài các giai đoạn | 155, 164, 169, 198 | Tính lại | – | KHỚP | Q3/2020–Q2/2025 = 20; Q1/2027–Q4/2028 = 8; 7/2023–6/2025 = 24; 7/2025–12/2026 = 18; 6/2009–6/2025 = 193 |
| 53 | Trọng số w_j = 1/(3·n_d(j)), J = 6 | 134 | Tính lại | – | KHỚP | 3·(1/9) + 2·(1/6) + 1·(1/3) = 1 |

Chuỗi sửa đổi: TT 57/2021 (ký 12/7/2021, hiệu lực 20/7/2021; niêm yết chuyển 01/7–31/12/2023; UPCoM chuyển 01/01–30/6/2025) → TT 69/2023 (ký 15/11/2023, hiệu lực 30/12/2023; khoản 1: thống nhất chậm nhất 31/12/2026; điểm đ khoản 2 và điểm d khoản 3: niêm yết chậm nhất 31/12/2025; điểm e: UPCoM chậm nhất 31/12/2026; HNX ngừng nhận niêm yết mới từ 01/7/2025) → VBHN 19/VBHN-BTC (25/12/2023) → TT 139/2025 (ký 30/12/2025, ký số 05/01/2026; chỉ sửa điểm đ khoản 2 và điểm d khoản 3: niêm yết chậm nhất 31/12/2026; ngày hiệu lực đọc không rõ trên OCR, đề cương không khẳng định ngày này).

---

## 3. Trích dẫn mồ côi hai chiều

**Trích dẫn trong bài nhưng thiếu trong danh mục:** không có tác giả nào bị thiếu. Có hai trường hợp dẫn sai hoặc dẫn không đủ:
- "Tuổi Trẻ Online, 2026" ở idx75 trỏ tới bài không chứa con số được dẫn. Cần thêm mục Tuổi Trẻ Online (2026b) (M1).
- "Thông báo tuyển sinh năm 2026" (idx221, 222) được dẫn như văn bản nhưng không có mục trong danh mục (m18).
- "Arnold và cộng sự (1999, dẫn theo Hisada, 2018)" là trích dẫn thứ cấp đúng APA. Chỉ Hisada có trong danh mục, đúng quy định.

**Mục trong danh mục không còn được trích:** không có. Đã kiểm cả 13 mục tiếng Việt và 64 mục tiếng Anh. Mọi mục đều có ít nhất một trích dẫn trong thân bài hoặc bảng, kể cả các mục mới ở v14: Báo Đầu tư Chứng khoán (2026) ở idx73 và 204; Sở GDCK TP.HCM (2025) ở idx117 và 120; FTSE Russell (2026a) ở idx171; Daw & Hatfield (2018) ở idx165; Eichengreen & Shah (2020) ở idx76, 83 và 93. Nguyễn & Nguyễn (2026b) chỉ được trích trong Bảng 6, như vậy là hợp lệ. **Không có mục nào cần XÓA.**

**a/b cùng năm:**
- FTSE Russell 2026a/b đúng thứ tự tiêu đề.
- Nguyễn & Nguyễn 2026a ("Black-Litterman…") và 2026b ("Tiền gửi…") đúng thứ tự.
- Tuổi Trẻ Online có hai bài năm 2026 nên cần a/b. Theo tiêu đề, "HOSE dự kiến…" là a, "Toàn bộ cổ phiếu…" là b (M1).

**APA 7, các điểm còn lệch (MINOR):**
- (i) Nhiều nguồn trong một ngoặc đang xếp theo năm. APA 7 §8.12 yêu cầu xếp theo bảng chữ cái (m14).
- (ii) Nhiều bài tạp chí thiếu DOI, ví dụ Amihud (2002) và Bae và cộng sự (2004). Hồ sơ không có DOI cho các bài này, nên ghi CHƯA CÓ NGUỒN; không tự bổ sung.
- (iii) Mục báo chí thiếu ngày đăng theo dạng APA: Thời báo Tài chính, Tuổi Trẻ (2026a). Báo ĐTCK thiếu URL. Tệp W02 không lưu URL, nên CHƯA CÓ NGUỒN cho URL.
- (iv) Sở GDCK TP.HCM (2025) không ghi nơi truy cập; bản trong hồ sơ được lấy qua FPTS.

---

## 4. Phát hiện theo mức

Mọi CHUỖI GỐC đã được kiểm bằng `grep -F`: xuất hiện đúng một lần trong đoạn, không chứa "_" và không vắt qua ký hiệu có chỉ số dưới.

### CRITICAL
Không có.

### MAJOR

**M1. MAJOR. idx75, 185, 274 (danh mục). Trích dẫn con số 299 mã trỏ nhầm bài báo.**
Lý do: con số "299 mã tính đến phiên 30/9/2026" lấy từ bài Tuổi Trẻ ngày 30/09/2026 "Toàn bộ cổ phiếu trên HNX sẽ chuyển sang HOSE từ 28-12" (W05, tác giả Quân Nguyễn). Danh mục chỉ có một mục Tuổi Trẻ Online (2026) là bài Prime Board, và bài đó không chứa "299". Người đọc tra theo danh mục sẽ không tìm thấy con số.
- idx75. CHUỖI GỐC: `(Tuổi Trẻ Online, 2026), trong cùng một ngày` → CHUỖI THAY THẾ: `(Tuổi Trẻ Online, 2026b), trong cùng một ngày`
- idx185. CHUỖI GỐC: `theo dự thảo quy chế đang lấy ý kiến (Tuổi Trẻ Online, 2026)` → CHUỖI THAY THẾ: `theo dự thảo quy chế đang lấy ý kiến (Tuổi Trẻ Online, 2026a)`
- idx274. CHUỖI GỐC: `Tuổi Trẻ Online. (2026). HOSE dự kiến` → CHUỖI THAY THẾ: `Tuổi Trẻ Online. (2026a). HOSE dự kiến`
- CHÈN MỤC MỚI ngay sau idx274: `Tuổi Trẻ Online. (2026b). Toàn bộ cổ phiếu trên HNX sẽ chuyển sang HOSE từ 28-12 [Bài báo ngày 30/9/2026]. [CẦN BỔ SUNG URL]`. Tệp W05 không lưu URL nên phải để nhãn; không được bịa URL.

**M2. MAJOR. idx120. Quy tắc ngưỡng chung cho Amihud không đúng ở cổ phiếu giá rất thấp.**
Lý do: không có một "mức lợi suất lớn nhất đạt được ở biên độ ±7%" chung cho mọi mã. Khi giá trần được làm tròn xuống theo đơn vị yết giá (V1 mục 5.1), mức này phụ thuộc vào giá.
- Ví dụ: giá tham chiếu 1.140 đồng, bước 10 đồng. 1.140 × 1,07 = 1.219,8, làm tròn xuống 1.210, tức lợi suất tối đa 6,14%.
- Giá tham chiếu 10.650 đồng, bước 50 đồng: lợi suất tối đa 6,57%.
- Ở giá vài trăm đồng, lợi suất tối đa còn thấp hơn nhiều. Ngược lại, khi giá trần sau làm tròn bằng giá tham chiếu, V1 mục 5.1.b cộng thêm một đơn vị yết giá, nên lợi suất tối đa có thể vượt 7%.

Hệ quả: với mã giá thấp, ngày vượt ngưỡng trước chuyển sàn có thể trở thành ngày bị cắt dưới ngưỡng sau chuyển sàn. Như vậy câu "tập ngày bị loại không đổi theo sàn" (cùng đoạn) không còn đúng cho các mã này, và kênh cơ học mà thiết kế muốn loại bỏ lại quay về đúng thước đo chính của H3.
- CHUỖI GỐC: `Ngưỡng thấp hơn mức lợi suất lớn nhất đạt được ở biên độ ±7%, tính sau khi giá trần được làm tròn xuống và giá sàn được làm tròn lên theo đơn vị yết giá của HOSE (Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh, 2025).`
- CHUỖI THAY THẾ: `Ngưỡng thấp hơn mức lợi suất lớn nhất đạt được ở biên độ ±7% với mọi mức giá đưa vào phép tính, sau khi giá trần được làm tròn xuống và giá sàn được làm tròn lên theo đơn vị yết giá của HOSE (Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh, 2025). Vì mức lợi suất lớn nhất này giảm rõ ở cổ phiếu giá thấp (với giá tham chiếu 1.140 đồng và bước giá 10 đồng, giá trần là 1.210 đồng, tức chỉ tăng được 6,14%), các mã có giá dưới một mức tối thiểu ghi trong tệp đăng ký được loại khỏi phép tính Amihud và được báo cáo riêng.`

**M3. MAJOR. idx204 và idx172. Trình tự thời gian của phương án UPCoM (mới ở v14) không khớp với mốc 31/12/2026.**
Lý do: cửa sổ sau bắt đầu từ tháng 1/2027. Nếu UPCoM được chuyển đúng hạn TT 69 (chậm nhất 31/12/2026), việc chuyển xảy ra trước cửa sổ sau, không phải trong cửa sổ sau. UPCoM chỉ chuyển trong cửa sổ sau khi mốc bị lùi hoặc không được thực hiện đúng hạn. Câu hiện tại đặt "một đợt riêng" vào cửa sổ sau, ngược với lý do vừa nêu ở vế trước ("hạn … vẫn là hết ngày 31/12/2026"). Hệ quả cho thiết kế cũng bị viết thiếu: nếu UPCoM chuyển trước ngày 1/1/2027, nhóm đối chứng UPCoM và thước đo biên độ trên mã UPCoM mất toàn bộ giai đoạn sau sự kiện, không chỉ một phần.
- idx204. CHUỖI GỐC: `nên UPCoM có thể chuyển sàn trong cửa sổ sau, theo một đợt riêng hoặc sau khi mốc này được lùi` → CHUỖI THAY THẾ: `nên UPCoM có thể chuyển sàn theo một đợt riêng trước hết ngày 31/12/2026, tức trước cửa sổ sau, hoặc trong cửa sổ sau nếu mốc này được lùi`
- idx172. CHUỖI GỐC: `Nếu cổ phiếu UPCoM chuyển sang HOSE trong cửa sổ sau (mục 4.3.10)` → CHUỖI THAY THẾ: `Nếu cổ phiếu UPCoM chuyển sang HOSE trước hoặc trong cửa sổ sau (mục 4.3.10)`

### MINOR

**m1. MINOR. idx204. Báo chí đứng một mình cho một khẳng định chắc chắn**, trong khi nguồn chính thức (thông báo VNX) đã có trong danh mục.
CHUỖI GỐC: `Đợt chuyển ngày 28/12/2026 không gồm UPCoM (Báo Đầu tư Chứng khoán, 2026)` → CHUỖI THAY THẾ: `Thông báo của VNX chỉ áp dụng cho cổ phiếu niêm yết, nên đợt chuyển ngày 28/12/2026 không gồm UPCoM (Báo Đầu tư Chứng khoán, 2026; Sở Giao dịch Chứng khoán Việt Nam, 2026)`

**m2. MINOR. idx73. Vế "không bị TT 139 sửa" chỉ dẫn được bằng chính TT 139**, nên cần dẫn thêm năm 2025.
CHUỖI GỐC: `và không bị Thông tư số 139/2025/TT-BTC sửa (Bộ Tài chính, 2023)` → CHUỖI THAY THẾ: `và không bị Thông tư số 139/2025/TT-BTC sửa (Bộ Tài chính, 2023, 2025)`

**m3. MINOR. idx125. Mốc pháp lý chưa có trích dẫn, và diễn đạt chưa sát văn bản** (TT 69: "không tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới").
CHUỖI GỐC: `Vì HNX ngừng nhận niêm yết mới từ ngày 01/7/2025,` → CHUỖI THAY THẾ: `Vì HNX ngừng tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới từ ngày 01/7/2025 (Bộ Tài chính, 2023),`

**m4. MINOR. idx125. Ngày bắt đầu giao dịch của UPCoM CHƯA CÓ NGUỒN.** Nguồn duy nhất trong hồ sơ là một blog (W10), và blog này ghi một ngày khác.
CHUỖI GỐC: `Mẫu bắt đầu từ tháng 6/2009, khi UPCoM bắt đầu có giao dịch.` → CHUỖI THAY THẾ: `Mẫu bắt đầu từ tháng 6/2009, khi UPCoM bắt đầu có giao dịch [CẦN XÁC MINH ngày giao dịch đầu tiên của UPCoM trên văn bản của HNX].`

**m5. MINOR. idx267. Trích yếu NQ 57/2026 lệch bản gốc.** Bản PDF ghi "của thành phố Hà Nội".
CHUỖI GỐC: `chất lượng cao của Thành phố.` → CHUỖI THAY THẾ: `chất lượng cao của thành phố Hà Nội.`

**m6. MINOR. idx64 (Bảng chữ viết tắt). Tên tiếng Anh của HOSE.** FTSE Ground Rules (V7) và logo trong QĐ 737 dùng "Ho Chi Minh Stock Exchange". Tên tiếng Anh chính thức của VNX ("Vietnam Exchange") CHƯA CÓ NGUỒN trong hồ sơ.
CHUỖI GỐC: `Ho Chi Minh City Stock Exchange` → CHUỖI THAY THẾ: `Ho Chi Minh Stock Exchange`

**m7. MINOR. idx64. Chữ viết tắt ARIMA không xuất hiện ở đâu trong thân bài.**
XÓA DÒNG BẢNG: `ARIMA | Autoregressive Integrated Moving Average | Mô hình tự hồi quy tích hợp trung bình trượt`

**m8. MINOR. idx84. "Sản phẩm thứ hai" dễ bị hiểu thành sản phẩm thứ hai trong danh sách của QĐ 1193** (danh sách đó là "Nền tảng tài chính số và thanh toán thông minh").
CHUỖI GỐC: `Đề tài không thiết kế sản phẩm thứ hai` → CHUỖI THAY THẾ: `Đề tài không thiết kế sản phẩm “Trung tâm tài chính quốc tế tại Hà Nội”`

**m9. MINOR. idx169. Ký hiệu k trùng nghĩa:** ở phương trình (1), k là sàn; ở phương trình (6), k là tháng sự kiện.
CHUỖI GỐC: `trong đó k chạy từ tháng 1/2024 đến tháng 12/2028` → CHUỖI THAY THẾ: `trong đó k, khác với k chỉ sàn ở phương trình (1), chạy từ tháng 1/2024 đến tháng 12/2028`

**m10. MINOR. idx116. Lựa chọn thiết kế "hai chỉ báo bị biên độ cắt trực tiếp" đứng vững** (Amihud dùng |r|, Corwin–Schultz dùng biên cao–thấp, cả hai đều bị cắt). Tuy vậy, câu này để ngỏ việc biên độ tác động gián tiếp lên tỷ số phương sai và độ trễ giá qua việc giá điều chỉnh chậm. Nên nói rõ phép kiểm tra đã có ở mục 4.3.4.
CHUỖI GỐC: `và chênh lệch Corwin–Schultz.` → CHUỖI THAY THẾ: `và chênh lệch Corwin–Schultz; tỷ số phương sai và độ trễ giá chỉ chịu biên độ gián tiếp qua việc giá điều chỉnh chậm, nên được kiểm tra bằng phép tính lại khi bỏ chiều hiệu quả thông tin (mục 4.3.4).`

**m11. MINOR. idx117. Nhãn bước giá nên nêu số quyết định đã biết (V6) và hệ quả của bước giá HOSE trước 12/9/2016** đối với giai đoạn tham chiếu của H2 (W07, báo chí).
CHUỖI GỐC: `[CẦN ĐỐI CHIẾU quy chế giao dịch gốc của HNX và bước giá của HOSE trước ngày 12/9/2016]` → CHUỖI THAY THẾ: `[CẦN ĐỐI CHIẾU quy chế giao dịch gốc của HNX (Quyết định số 529/QĐ-SGDHN ngày 25/8/2016, theo bản tóm tắt của công ty chứng khoán) và bước giá của HOSE trước ngày 12/9/2016, khi theo báo chí mã giá dưới 10.000 đồng cũng có bước giá 100 đồng như HNX]`

**m12. MINOR. idx90. Chỉ tiêu (5) chưa nêu loại báo cáo hội thảo đủ điều kiện theo Điều 12.2 NQ 57.**
CHUỖI GỐC: `và một đến hai báo cáo hội thảo.` → CHUỖI THAY THẾ: `và một đến hai báo cáo hội thảo đăng trong kỷ yếu được Hội đồng Giáo sư nhà nước tính điểm hoặc thuộc cơ sở dữ liệu Scopus hoặc Web of Science.`

**m13. MINOR. idx91. Chỉ tiêu (6) dùng thuật ngữ khác với hướng dẫn của Sở KH&CN.** Thông báo 7215, qua bản tóm tắt PTIT (bậc 5), viết: "văn bản cam kết phối hợp, tiếp nhận, thử nghiệm và sử dụng kết quả nghiên cứu". Thí sinh tự quyết, vì một văn bản "cam kết" có thể khó xin hơn văn bản "xác nhận".
CHUỖI GỐC: `kèm văn bản xác nhận nhu cầu sử dụng kết quả của ít nhất một đơn vị` → CHUỖI THAY THẾ: `kèm văn bản cam kết tiếp nhận hoặc sử dụng kết quả của ít nhất một đơn vị`

**m14. MINOR. Thứ tự nhiều nguồn trong cùng một ngoặc chưa theo bảng chữ cái (APA 7 §8.12).**

| idx | CHUỖI GỐC | CHUỖI THAY THẾ |
|---|---|---|
| 74 | `(Kindleberger, 1974; Gehrig, 2000)` | `(Gehrig, 2000; Kindleberger, 1974)` |
| 76 | `(Moosa và cộng sự, 2016; Eichengreen & Shah, 2020)` | `(Eichengreen & Shah, 2020; Moosa và cộng sự, 2016)` |
| 76 | `(Nielsson, 2009; Hisada, 2018)` | `(Hisada, 2018; Nielsson, 2009)` |
| 76 | `(Vo & Phan, 2017; Hoang & Luu, 2024; Goutte và cộng sự, 2025)` | `(Goutte và cộng sự, 2025; Hoang & Luu, 2024; Vo & Phan, 2017)` |
| 83 | `(Vo & Phan, 2017; Goutte và cộng sự, 2025; Nguyễn & Nguyễn, 2026a)` | `(Goutte và cộng sự, 2025; Nguyễn & Nguyễn, 2026a; Vo & Phan, 2017)` |
| 95 | `(Lesmond và cộng sự, 1999; Bekaert và cộng sự, 2007)` | `(Bekaert và cộng sự, 2007; Lesmond và cộng sự, 1999)` |
| 98 | `(Black & Litterman, 1992; Bessler và cộng sự, 2017)` | `(Bessler và cộng sự, 2017; Black & Litterman, 1992)` |
| 107 | `(Kindleberger, 1974; Gehrig, 2000; Yao, 2012; Lai, 2012)` | `(Gehrig, 2000; Kindleberger, 1974; Lai, 2012; Yao, 2012)` |
| 107 | `(Markowitz, 1952; Michaud, 1989; Kan & Zhou, 2007)` | `(Kan & Zhou, 2007; Markowitz, 1952; Michaud, 1989)` |
| 129 | `(Lesmond, 2005; Bekaert và cộng sự, 2007)` | `(Bekaert và cộng sự, 2007; Lesmond, 2005)` |
| 102 (Bảng 1) | `(Yao, 2012; Naeem, 2023; Lai, 2012)` | `(Lai, 2012; Naeem, 2023; Yao, 2012)` |
| 102 (Bảng 1) | `(Amihud, 2002; Lesmond, 2005; Fong và cộng sự, 2017)` | `(Amihud, 2002; Fong và cộng sự, 2017; Lesmond, 2005)` |
| 102 (Bảng 1) | `(Huang & Stoll, 1996; Nielsson, 2009; Hisada, 2018)` | `(Hisada, 2018; Huang & Stoll, 1996; Nielsson, 2009)` |
| 102 (Bảng 1) | `(Vo & Phan, 2017; Goutte và cộng sự, 2025; Nguyễn & Nguyễn, 2026a)` | `(Goutte và cộng sự, 2025; Nguyễn & Nguyễn, 2026a; Vo & Phan, 2017)` |

**m15. MINOR. Danh mục: thiếu DOI và thiếu ngày ở mục báo chí (APA 7).** Hồ sơ không chứa DOI cho các bài tạp chí đang thiếu, không chứa URL của Báo ĐTCK (W02) và Tuổi Trẻ (W05), cũng không chứa ngày đăng của bài Thời báo Tài chính và bài Prime Board. Tất cả ghi CHƯA CÓ NGUỒN; chưa đưa chuỗi thay thế để tránh bịa. Việc cần làm: thí sinh tra DOI và URL rồi bổ sung theo dạng "(2026, ngày tháng)".

**m16. MINOR. idx185. Nhãn trùng một phần với nhãn ở idx170** (cách HOSE xử lý mã chuyển sàn trong chỉ số).
CHUỖI GỐC: `[CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong VN-Index và quy chế phân bảng chính thức]` → CHUỖI THAY THẾ: `[CẦN XÁC MINH quy chế phân bảng chính thức; cách xử lý mã chuyển sàn trong VN-Index xem nhãn ở mục 4.3.7]`

**m17. MINOR. Nhãn còn lại và nhật ký.** v14 còn 9 nhãn [CẦN…] ở idx73, 116, 117, 142, 170, 175, 185, 271 và 301. Nhật ký vòng 13 ghi "Còn 13 nhãn", và không có nhật ký vòng 14 để giải thích bốn nhãn đã gỡ. Mục này không đổi văn bản đề cương. Việc cần làm: nhật ký v14 phải ghi rõ nhãn nào đã gỡ và gỡ dựa trên nguồn nào: [73] được thu hẹp nhờ W02; [121] và [123] được giải nhờ V1, V3, V4; [174] được giải nhờ V7 và FAQ; [291] và [293] được giải nhờ Crossref.

**m18. MINOR. idx221. "Thông báo tuyển sinh năm 2026" được dẫn như văn bản nhưng không có mục trong danh mục và không có trong hồ sơ** (CHƯA CÓ NGUỒN; Vòng 8 A11). Cùng tình trạng: "bốn năm" (idx234), "tiếng Anh hoặc tiếng Việt" (idx222) và "9 tín chỉ" (idx228).
CHUỖI GỐC: `theo Thông báo tuyển sinh năm 2026,` → CHUỖI THAY THẾ: `theo Thông báo tuyển sinh năm 2026 [CẦN BỔ SUNG số hiệu, ngày của Thông báo và mục tương ứng trong danh mục tài liệu],`

---

## 5. Mức khớp với hồ sơ đề nghị hỗ trợ của Hà Nội (research-grants, proposal-revise)

| Yêu cầu | Căn cứ | Đề cương v14 | Đánh giá |
|---|---|---|---|
| Nội dung luận án phục vụ bài toán lớn | NQ 57 Điều 11.3; QĐ 1193 bài toán 19 | idx68, 77–80, 84, 213: nêu rõ câu hỏi số 1 và 3 được phục vụ, câu số 2 và 4 nằm ngoài phạm vi | KHỚP |
| Học tập trung toàn thời gian | NQ 57 Điều 11.3 | idx234, 251: cam kết; idx250–251: các chương trình đang học sẽ hoàn thành, bảo lưu hoặc dừng trước khi nhập học | KHỚP |
| Thời gian hỗ trợ ≤ 48 tháng | NQ 57 Điều 13 | idx234, Bảng 5 (4 năm) | KHỚP; "bốn năm" của cơ sở đào tạo CHƯA CÓ NGUỒN (m18) |
| Công bố được hỗ trợ: WoS Q1/Q2, tác giả chính | NQ 57 Điều 12.3 | idx90, 232 | KHỚP |
| Hội thảo được hỗ trợ (tối đa 2 lần/năm, loại kỷ yếu) | NQ 57 Điều 12.2 | idx90 chưa nêu loại kỷ yếu | KHỚP MỘT PHẦN (m12) |
| Nghĩa vụ sau tốt nghiệp | NQ 57 Điều 15.2.e | idx255 | KHỚP |
| Chỉ tiêu có thể kiểm chứng | TB 7215 (qua PTIT, bậc 5) | idx85–91: sáu chỉ tiêu có mốc và bằng chứng công khai; khớp Bảng 5 (Năm 1: tệp đăng ký; Năm 3: (3) và (4); Năm 4: (2) mã nguồn và (6)) | KHỚP. Ghi chú: chỉ tiêu (3) và (4) cần dữ liệu đến hết 12/2028, trong khi Bảng 5 đặt ở Năm 3 (Q1–2). Hai mốc này khớp với nhau nếu nhập học khoảng đầu năm 2027 |
| Đơn vị phối hợp, tiếp nhận, sử dụng kết quả | TB 7215 | idx213–214, 91: Sở KH&CN (đầu mối theo QĐ 1193 Điều 3), ưu tiên HNX; văn bản xin trước khi nộp hồ sơ | KHỚP về ý; thuật ngữ nên theo TB 7215 (m13). Hồ sơ hiện chưa có văn bản nào, tức là cam kết của thí sinh, chưa phải bằng chứng |
| Sản phẩm nối với sản phẩm của bài toán 19 | QĐ 1193 Phụ lục | idx84: "Hệ thống dữ liệu tài chính đô thị" (cấu phần), "Trung tâm tài chính quốc tế tại Hà Nội" (đầu vào phân tích) | KHỚP; câu "sản phẩm thứ hai" mơ hồ (m8) |

Mức khớp tổng thể: cao. Không có điểm nào trái NQ 57 hay QĐ 1193. Hai việc thí sinh còn phải tự làm: văn bản của đơn vị tiếp nhận và Thông báo tuyển sinh làm nguồn.

---

## 6. Điểm đã kiểm và không có lỗi (để agent khác khỏi kiểm lại)

- **Đánh số và tham chiếu chéo:** Bảng 1–7 và Hình 1–3 khớp danh mục bảng và hình. Phương trình (1)–(7) đều được tham chiếu đúng; "(5)–(7)" ở idx143 đúng. Mục 4.3.2, 4.3.4, 4.3.7, 4.3.8 và 4.3.10 được tham chiếu đúng. Mục lục khớp tiêu đề; số trang chưa kiểm được trên bản text.
- **Cỡ mẫu và thời gian thống nhất trong cả bài:**
  - giai đoạn tham chiếu 6/2009–6/2025;
  - giai đoạn chuyển tiếp 7/2025–12/2026;
  - giai đoạn sau 1/2027–12/2028 (24 tháng);
  - rổ CS gồm tối đa 30 mã, phương án dự phòng 20 mã;
  - cửa sổ 104 tuần;
  - 20 cửa sổ trước và 8 cửa sổ sau;
  - ρ = 5 (kiểm tra ở 3 và 10);
  - Holm 5%, α/3.
- **Bảng 7:** 9 bản thảo, 3 bản "Có" (số 1, 5, 7), khớp idx244 và idx253.
- **Giả thuyết và câu hỏi:** H1↔câu hỏi 1, H2↔câu hỏi 2, H3 và H4↔câu hỏi 3 khớp giữa idx109, Bảng 2 và Bảng 4.
- **FTSE và VN-Index:** đoạn idx171 và idx185–186 nhất quán với nhau và với V7, FAQ, QĐ 737.
