# Báo cáo Agent B, vòng 10: kiểm chứng, nhất quán và độ khớp với đề án Hà Nội

Đề cương được kiểm: v10, "Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội" (`scratchpad/r10/dump-v10.txt`, idx 0–598). Ngày lập: 16/10/2026. Đây là bản nháp làm việc để thí sinh và người hướng dẫn tự kiểm lại. Báo cáo không sửa đề cương.

---

## (1) Bằng chứng tuân thủ

**Các skill đã gọi, theo thứ tự (Skill tool):**
1. `vn-legal-verify`: đối chiếu từng khẳng định pháp lý với văn bản gốc trong hồ sơ, gắn KHỚP/LỆCH/KHỚP MỘT PHẦN/CHƯA CÓ NGUỒN, ghi bậc nguồn.
2. `fact-checker`: chấm số liệu và mô tả văn liệu theo thang TRUE / MOSTLY TRUE / MIXED / MOSTLY FALSE / FALSE / UNVERIFIABLE.
3. `credible-claims`: lập claim record cho H1–H4, phân tích theo kênh, phân tích theo trụ sở Hà Nội và các khẳng định khớp với bài toán 19/NQ 57; xem ngôn ngữ báo cáo có vượt bằng chứng không.
4. `consistency-checker`: làm theo checklist 10 nhóm. **Không chạy** `latex_extractor.py`/`crossref_validator.py`.
5. `citation-management`: chỉ đọc `SKILL.md`. **Không chạy** script nào, không gọi OpenAlex/CrossRef.
6. `research-grants`: chấm độ khớp với NQ 57, Thông báo 7215 và bài toán 19, dùng các tiêu chí "phù hợp sứ mệnh", "chỉ tiêu đo được", "đơn vị tiếp nhận" và nhóm lỗi "Mismatch with Agency Mission / Overly Ambitious".
7. `peer-review`: viết nhận xét tổng thể theo kiểu phản biện hội đồng. Người dùng là tác giả nên quyền xem được bảo đảm. Mọi xử lý chạy cục bộ; không chạy các script của skill.

**Tệp đã đọc (chỉ đọc):** `dump-v10.txt` (đọc hết); `ho-so/TaiLieu_Vong8_GopTXT_16-10-2026.txt` (mục lục, sau đó tìm theo mục: [01] TT57, [02] TT69, [04] Thời báo TC, [05] VNX, [07] TT139, [09] QĐ 737, [10] QĐ 738, [12] TT120, [13]–[14] biên độ, [17] Tuổi Trẻ, [19] NQ 222, [21]–[25] NQ 57/TB 7215, [30] FTSE FAQ v1.3, [33] GFCI 40, [37] Nielsson, [49] Roth và cộng sự, [57] Hisada); `ho-so/TONG_HOP_TAI_LIEU_HNX_HOSE.txt` (VBHN 19, Naeem 2023); `ho-so/tai-lieu-gop.txt` (Amihud, Mendelson & Lauterbach 1997, bản WP NYU); `scratchpad/r8/qd1193.txt` (Điều 1–4 và bài toán 19); `reports/doi-chieu-bai-toan-19.md` (bản chép NQ 57 Điều 11–18, 34, 35); `reports/doi-chieu-tai-lieu-vong8.md`; `reports/r8-review-B.md`; `outputs/checklist-dieu-kien.md`; `scratchpad/r10/edits-r10.json` (để biết đoạn nào mới ở v10).

**Ràng buộc:** không tra web; không gửi câu chữ đề cương ra ngoài; không chạy script của skill nào. Chỉ dùng `grep`/`sed` để tìm và đọc văn bản cục bộ. Chuỗi gốc trong mục (5) đã được kiểm bằng `grep -F`: mỗi chuỗi xuất hiện đúng 1 lần trong dump v10. Không đổi tên đề tài.

---

## (2) Tổng hợp

| Mức | Số lượng | Mã |
|---|---|---|
| CRITICAL | 0 | — |
| MAJOR | 3 | MJ1 (kênh chỉ số FTSE không có biến thiên), MJ2 (dẫn Amihud 1997 ngược chiều), MJ3 (diễn giải phân tích trụ sở Hà Nội vượt thiết kế) |
| MINOR | 17 | m1–m17 |

Phần pháp lý của v10 đứng vững. Toàn bộ mốc của TT57, TT69, TT139, VBHN 19, lịch VNX, NQ 222, NQ 57 Điều 11.3 và Điều 13, QĐ 1193 Điều 3 đều KHỚP với văn bản gốc. Ba lỗi MAJOR đều nằm ở các đoạn mới thêm ở v10 (idx 322–325, 334), mỗi lỗi sửa được bằng một thay câu chữ.

---

## (3) Bảng đối chiếu pháp lý và số liệu

### 3a. Pháp lý (vn-legal-verify)

Bậc nguồn: 1 = bản ký số hoặc trang chính thức; 2 = toàn văn đăng lại; 3 = OCR bản quét; 5 = báo chí.

| # | Khẳng định (idx) | Văn bản & điều khoản | Bậc | Trạng thái | Trích nguyên văn nguồn |
|---|---|---|---|---|---|
| L1 | TT57: HNX ngừng nhận niêm yết mới từ 01/7/2023, chuyển xong trong năm 2023 (100) | TT57 Điều 4 khoản 3 điểm c, d | 2 | KHỚP | "c) Từ ngày 01 tháng 7 năm 2023: Sở Giao dịch Chứng khoán Hà Nội không tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới"; "d) Từ ngày 01 tháng 7 năm 2023 đến hết ngày 31 tháng 12 năm 2023: … thực hiện chuyển cổ phiếu của tổ chức niêm yết" |
| L2 | TT69 lùi hai mốc thành 01/7/2025 và hết năm 2025 (100, 229) | TT69 Điều 1 khoản 3 điểm c, d | 3 | KHỚP | "c) Từ ngày 01 tháng 7 năm 2025: Sở Giao dịch Chứng khoán Hà Nội không tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới"; "d) Chậm nhất đến hết ngày 31 tháng 12 năm 2025: … hoàn thành việc chuyển cổ phiếu của tổ chức niêm yết" |
| L3 | TT139 ngày 30/12/2025 lùi hạn đến hết 31/12/2026 (100) | TT139 Điều 1 khoản 1, 2 | 1 (OCR) | KHỚP | "d) Chậm nhất đến hết ngày 31 tháng 12 năm 2026: Sở Giao dịch Chứng khoán Hà Nội hoàn thành việc chuyển cổ phiếu của tổ chức niêm yết". Ngày ký: "Hà Nội, ngày 30 tháng Á2 năm 2025" (OCR), khớp với tiêu đề thông báo của VNX "ngày 30/12/2025". |
| L4 | UPCoM: hạn 31/12/2026 do TT69 đặt, thay khung 01/01–30/6/2025 của TT57; TT139 không sửa (101) | TT57 Điều 4.3.e; TT69 Điều 1.3.e; TT139 Điều 1 | 1–3 | KHỚP | TT57: "e) Từ ngày 01 tháng 01 năm 2025 đến hết ngày 30 tháng 6 năm 2025"; TT69: "e) Chậm nhất đến hết ngày 31 tháng 12 năm 2026 … chuyển cổ phiếu của tổ chức đăng ký giao dịch"; TT139 chỉ sửa "điểm đ khoản 2" và "điểm d khoản 3". |
| L5 | Kế hoạch chuyển UPCoM theo khoản 4 Điều 4 TT57 (101, nhãn) | TT57 Điều 4.4 | 2 | KHỚP (dẫn đúng điều khoản; nội dung kế hoạch CHƯA CÓ NGUỒN) | "4. Sở Giao dịch Chứng khoán Việt Nam xây dựng kế hoạch chuyển cổ phiếu của tổ chức niêm yết, đăng ký giao dịch … và báo cáo Ủy ban Chứng khoán Nhà nước trước khi triển khai." |
| L6 | Sau hợp nhất, HNX tổ chức thị trường trái phiếu và phái sinh (102, 336) | TT57 Điều 5, 6 (không bị TT69, TT139 sửa) | 2 | KHỚP | "Sở Giao dịch Chứng khoán Hà Nội thống nhất tổ chức thị trường giao dịch trái phiếu"; "Sở Giao dịch Chứng khoán Hà Nội tổ chức thị trường giao dịch chứng khoán phái sinh" |
| L7 | VBHN 19/VBHN-BTC ngày 25/12/2023 (danh mục 520) | Trang thông tin VBHN | 2 | KHỚP | "Số hiệu: 19/VBHN-BTC … Ngày ban hành: 25/12/2023"; trích yếu "hợp nhất Thông tư quy định lộ trình sắp xếp lại thị trường giao dịch cổ phiếu, thị trường giao dịch trái phiếu, …" |
| L8 | Lịch VNX 30/9/2026: phiên cuối 23/12, tạm ngừng 24–25/12, giao dịch tại HOSE từ 28/12/2026 (100) | Thông báo VNX 30/9/2026 | 1 | KHỚP | "Ngày giao dịch cuối cùng của toàn bộ cổ phiếu niêm yết tại HNX: ngày 23/12/2026"; "Tạm ngừng giao dịch trong 02 ngày 24/12/2026 và 25/12/2026"; "Ngày giao dịch đầu tiên tại HOSE … là ngày 28/12/2026" |
| L9 | Thông báo VNX "nêu rõ giao dịch tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành" (101) | Như trên | 1 | KHỚP MỘT PHẦN | Câu gốc nằm trong gạch đầu dòng về hai ngày tạm ngừng: "Tạm ngừng giao dịch trong 02 ngày … Giao dịch chứng khoán tại HOSE và giao dịch chứng khoán tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành." Xem m1. |
| L10 | Biên độ ±7/±10/±15%; theo TT120 Điều 4, biên độ do Sở giao dịch quyết định sau khi UBCKNN chấp thuận (222) | TT120 Điều 4; VnExpress | 2, 5 | KHỚP MỘT PHẦN | "1. Sở giao dịch chứng khoán Việt Nam quyết định biên độ dao động giá sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận. 2. Trong trường hợp cần thiết để ổn định thị trường, Ủy ban Chứng khoán Nhà nước quyết định điều chỉnh biên độ…". TT120 có hiệu lực từ 15/02/2021, nên không quy định giai đoạn 2009–2020; nhãn [CẦN XÁC MINH] hiện có đã bao trường hợp này. Xem m2. |
| L11 | Danh mục TT120 (519) | TT120, phần đầu | 2 | KHỚP | "Thông tư số 120/2020/TT-BTC ngày 31/12/2020 … Quy định về giao dịch cổ phiếu niêm yết, đăng ký giao dịch và chứng chỉ quỹ, trái phiếu doanh nghiệp, chứng quyền có bảo đảm niêm yết trên hệ thống giao dịch chứng khoán" |
| L12 | NQ 222: TTTCQT đặt tại TP.HCM và Đà Nẵng; thông qua 27/6/2025 (99, 114, 524) | NQ 222 | 2 | KHỚP | "Trung tâm tài chính quốc tế … đặt tại Thành phố Hồ Chí Minh và thành phố Đà Nẵng"; "thông qua ngày 27 tháng 6 năm 2025"; "có hiệu lực thi hành từ ngày 01 tháng 9 năm 2025" |
| L13 | NQ 57: tập trung toàn thời gian, khoản 3 Điều 11 (507) | NQ 57 Điều 11.3 (bản chép từ scan) | 3 | KHỚP | "3. Theo học chương trình đào tạo tiến sĩ và tương đương, tập trung toàn thời gian, …" |
| L14 | NQ 57: hỗ trợ tối đa 48 tháng, Điều 13 (401) | NQ 57 Điều 13 | 3 | KHỚP | "… thời gian đào tạo trình độ tiến sĩ theo quy định của cơ sở đào tạo nhưng không vượt quá 48 tháng." |
| L15 | NQ 57 ngày 15/6/2026, trích yếu (522) | PTIT, Dân trí | 5 | KHỚP (thứ cấp) | "Ngày 15/6/2026, HĐND thành phố Hà Nội thông qua Nghị quyết số 57/2026/NQ-HĐND quy định một số chính sách phát triển nguồn nhân lực chất lượng cao của Thành phố, có hiệu lực từ ngày 01/7/2026." |
| L16 | QĐ 1193: tên bài toán 19; câu hỏi 1 và 3; sản phẩm (95, 114) | QĐ 1193, Phụ lục | 2 | KHỚP | "Phương thức nào để xây dựng Hà Nội thành trung tâm tài chính và dịch vụ chất lượng cao quốc tế?"; "1. Những mô hình trung tâm tài chính nào phù hợp với điều kiện phát triển của Hà Nội?"; "3. Những nền tảng công nghệ nào giúp tăng cường minh bạch và hiệu quả của thị trường tài chính?"; sản phẩm "Trung tâm tài chính quốc tế tại Hà Nội", "Hệ thống dữ liệu tài chính đô thị" |
| L17 | QĐ 1193 Điều 3: Sở KH&CN là cơ quan đầu mối theo dõi, đánh giá (359) | QĐ 1193 Điều 3.1 | 2 | KHỚP | "Sở Khoa học và Công nghệ là cơ quan đầu mối, có trách nhiệm tham mưu, theo dõi, điều phối việc triển khai Danh mục …; đồng thời tổ chức vận hành hệ thống theo dõi, đánh giá tiến độ và kết quả thực hiện" |
| L18 | QĐ 737/QĐ-SGDHCM ngày 29/9/2026; VN-Index tự cập nhật sau ngày giao dịch đầu tiên của cổ phiếu niêm yết mới (333, 525) | QĐ 737 (OCR) | 3 | KHỚP MỘT PHẦN (nội dung KHỚP; số và ngày chưa giải) | "Danh mục cổ phiếu thành phần của chỉ số được tự động cập nhật sau ngày giao dịch đầu tiên của cổ phiếu niêm yết mới". OCR đọc "Số: 3157 /QĐ-SGDHCM … ngày 23 tháng 9 năm 2026", trong khi văn bản căn cứ CV 1314 "ngày 25 tháng 9 năm 2026"; tên tệp VNX là "20260929_QD737". Nhãn [CẦN XÁC MINH] hiện có là đúng. Việc áp quy tắc "cổ phiếu niêm yết mới" cho mã chuyển sàn là suy diễn và đã được gắn nhãn. |
| L19 | Phân bảng Bảng Chính/Tiêu chuẩn, công bố lần đầu 28/12/2026, theo dự thảo (333) | Tuổi Trẻ | 5 | KHỚP (dự thảo, báo chí) | "VNX vừa gửi dự thảo quy chế phân loại cổ phiếu niêm yết …"; "HOSE dự kiến công bố kết quả phân loại lần đầu vào ngày 28-12-2026" |
| L20 | UBCKNN nghiên cứu nới biên độ, giao dịch xuyên trưa (333) | Thời báo TC, họp báo ngày 6/10 | 5 | KHỚP; còn thiếu một nội dung | "Ủy ban Chứng khoán Nhà nước đang nghiên cứu nhiều nội dung như: giao dịch xuyên trưa, nới biên độ dao động giá..."; Thứ trưởng còn "đặt vấn đề nghiên cứu khả năng giao dịch xuyên trưa và rút ngắn chu kỳ thanh toán từ T+2 xuống mức thấp hơn". Xem m4. |
| L21 | Thông báo tuyển sinh 2026: Nhóm 1, 9 tín chỉ, bốn năm, Hành vi tổ chức và Lãnh đạo (389, 395, 401) | — | — | CHƯA CÓ NGUỒN trong hồ sơ (mục A11 "[KHÔNG]") | — |

**Chuỗi sửa đổi:** TT57/2021/TT-BTC (ký 12/7/2021, hiệu lực 20/7/2021; niêm yết: 01/7–31/12/2023; UPCoM: 01/01–30/6/2025) → TT69/2023/TT-BTC (ký 15/11/2023, hiệu lực 30/12/2023; niêm yết: ngừng nhận từ 01/7/2025, chuyển xong trước 31/12/2025; UPCoM: chậm nhất 31/12/2026; Điều 4.1: HOSE thống nhất chậm nhất 31/12/2026) → VBHN 19/VBHN-BTC (25/12/2023, gồm TT57 và TT69) → TT139/2025/TT-BTC (ký 30/12/2025, ký số 05/01/2026; chỉ sửa điểm đ khoản 2 và điểm d khoản 3: hạn chuyển niêm yết đến 31/12/2026; ngày hiệu lực OCR đọc không rõ) → Thông báo VNX 30/9/2026 (lịch 23/12–28/12/2026, chỉ áp dụng cho cổ phiếu niêm yết). Hệ quả cho thiết kế: theo văn bản hiện hành, UPCoM cũng phải sang HOSE chậm nhất 31/12/2026 (xem m5).

### 3b. Số liệu và mô tả văn liệu (fact-checker)

| # | Khẳng định (idx) | Kết luận | Căn cứ trích nguyên văn |
|---|---|---|---|
| F1 | GFCI 40 (9/2026): TP.HCM hạng 67/117 (99) | TRUE | "number of centres in the main index is 117"; Bảng 1, các hạng 59–67: Hangzhou … Wuhan, Ho Chi Minh City (hạng 67) |
| F2 | Đà Nẵng lần đầu vào chỉ số ở hạng 71 (99) | TRUE | "Da Nang entered the index for the first time in 71st position." |
| F3 | Hà Nội không có trong bảng xếp hạng (99) | TRUE | Tìm "Hanoi"/"Ha Noi" trong toàn bộ báo cáo GFCI 40: 0 kết quả, kể cả trong danh sách 22 trung tâm liên kết (associate centres) |
| F4 | 144 nhân tố; 3 nhân tố vốn hóa, giá trị và khối lượng giao dịch cổ phiếu lấy từ WFE, Bảng 26 (330, 347) | MOSTLY TRUE | "GFCI 40 was compiled using 144 instrumental factors"; Table 26: "Capitalisation Of Stock Exchanges … The World Federation of Stock Exchanges / Value Of Share Trading / Volume Of Share Trading / Broad Stock Index Levels …". Cùng bảng còn nhân tố mức chỉ số cổ phiếu, mà bản chữ không cho biết nguồn. Xem m7. |
| F5 | Z/Yen công bố từ 2007, hợp tác với CDI từ 2016 (227) | TRUE | "In March 2007, Z/Yen and the City Of London released the first edition"; "In July 2016, Z/Yen and the China Development Institute (CDI) … established a strategic partnership". Lưu ý: kỳ đầu do Z/Yen phát hành cùng City of London; câu đề cương vẫn đúng. |
| F6 | Wardle & Mainelli là tác giả GFCI 40 (591) | TRUE | "The authors of this report, Mike Wardle and Professor Michael Mainelli" |
| F7 | FTSE Russell đưa cổ phiếu Việt Nam vào theo 4 đợt: 9/2026, 3/2027, 6/2027, 9/2027 (333) | TRUE | "four‑tranche phased implementation beginning in September 2026 and concluding in September 2027"; các mốc March 2027, June 2027, September 2027 |
| F8 | Danh sách dự kiến của FTSE dùng làm "mức chịu cú sốc chỉ số" của mã chuyển sàn, đo bằng dữ liệu đến 30/6/2025 (322) | **MOSTLY FALSE (giả định thiết kế sai thực tế)** | FAQ v1.3 Q6: danh sách "passed the FTSE GEIS index eligibility screen … based on data cut-off as of 30 June 2026"; cả 27 mã đều ghi sàn "HSX" (có SHB, đã chuyển từ HNX sang trước đây). Không có mã nào niêm yết tại HNX. Xem MJ1. |
| F9 | 299 mã tính đến phiên 30/9/2026 (106, 333) | TRUE (bậc 5) | Tuổi Trẻ: "Tính đến phiên 30-9, HNX có 299 mã cổ phiếu niêm yết với tổng vốn hóa gần 463.000 tỉ đồng" |
| F10 | Hisada (2018): hợp nhất ngày 16/7/2013; mẫu cổ phiếu TSE không niêm yết kép tại OSE; thanh khoản tăng ngắn hạn nhờ cộng hưởng và tâm lý; tâm lý mạnh hơn ở cổ phiếu nhỏ; giảm sau một năm; đo bằng vòng quay và ILLIQ (105, 128) | TRUE | "the stock exchanges were integrated on July 16, 2013. This study uses daily data on common stocks of the TSE, excluding those double listed on the OSE"; "Synergy and the investor sentiment effect occur in the short run with liquidity increases. The investor sentiment effect occurs more strongly in small stocks"; "liquidity decreases one year after the merger"; "Yit indicates liquidity, which is turnover or ILLIQ"; IJEFI "2018, 8(2), 315-318" |
| F11 | Arnold và cộng sự (1999, dẫn theo Hisada) thấy hợp nhất sàn làm thanh khoản tăng (128) | MOSTLY TRUE | Hisada: "Arnold et al. (1999) find that US regional stock exchange mergers lead to liquidity increases that result from economies of scale." Đề cương bỏ mất chi tiết "sàn khu vực ở Hoa Kỳ" (m6). |
| F12 | Amihud và cộng sự (1997): Tel Aviv; CAR khoảng 5,5% từ 5 ngày trước công bố đến 30 ngày sau; thanh khoản tăng đi cùng giá tăng (104, 127) | TRUE (bản WP NYU; bản JFE không có trong hồ sơ) | "The cumulative average market-adjusted return over a period that started five days prior to the announcement and ended 30 days after the stocks started trading by the new method was approximately 5.5%"; "positive association between liquidity gains and price appreciation" |
| F13 | Amihud và cộng sự (1997) được dùng làm căn cứ cho khả năng nhóm đối chứng HOSE **mất** thanh khoản (334) | **MIXED (dẫn sai chiều)** | "an improvement in the trading mechanism for security A will have a positive effect on the liquidity of B"; "the price of the secondary stock should increase … Our results support this hypothesis." Bài này ủng hộ lan tỏa dương, tức δ bị đánh giá thấp, không phải bị phóng đại. Xem MJ2. |
| F14 | Nielsson (2009): thanh khoản tăng ở doanh nghiệp lớn và doanh nghiệp có doanh thu nước ngoài, không tăng ở doanh nghiệp nhỏ (105, 128) | TRUE (bản WP 2007) | "positive effects are concentrated among big firms and firms with foreign sales"; "regression (3) reports no merger effect for small firms" |
| F15 | Naeem (2023): 196 trung tâm theo khu vực tài phán, 2007–2020, 17 yếu tố chọn bằng cây quyết định, hồi quy bảng trên thứ hạng GFCI, không có chỉ báo thị trường cổ phiếu (107, 124, 137) | TRUE | "196 IFCs (unique financial jurisdictions) … (2007 till 2020) … panel regression … adopts 17 most relevant determinants … by using a Decision Tree approach"; danh sách 17 yếu tố không có chỉ báo thị trường cổ phiếu |
| F16 | Bắc Kinh là trung tâm tài chính lớn dù không có sở giao dịch tầm quốc gia (103) | TRUE | Naeem: "Despite the lack of a stock exchange, Beijing is a significant financial centre in China." |
| F17 | Eichengreen & Shah (2020): năm nhóm yếu tố, một nhóm là vốn hóa (123) | TRUE (thứ cấp) | Naeem: "divided into five different categories by Eichengreen and Shah (2020)"; "set of indicators that measure market capitalisation and financial progress". Thứ tự tác giả trong danh mục khớp với danh mục của Naeem ("Eichengreen, B., & Shah, N. (2020)"); ghi chú A/C9 của hồ sơ ghi "Shah & Eichengreen", cần đối chiếu DOI 10.1111/roie.12441. |
| F18 | Daw & Hatfield (2018): ghép theo kết quả trễ tạo hồi quy về trung bình (317) | TRUE (thứ cấp) | Roth và cộng sự: "Daw and Hatfield (2018) show that … matching the treated and control groups on lagged outcomes … can then induce bias owing to a mean-reversion effect"; danh mục của bài này ghi "Health Services Research, 2018" |
| F19 | Coval & Moskowitz (1999): nhà đầu tư ưa cổ phiếu của doanh nghiệp ở gần mình (324) | UNVERIFIABLE (không có bản gốc trong hồ sơ) | Thông tin thư mục và mô tả phù hợp với hiểu biết chung của người kiểm, nhưng không xác minh được bằng hồ sơ. Nhãn [CẦN ĐỐI CHIẾU] là đúng. |
| F20 | Loughran & Schultz (2005): thanh khoản phụ thuộc vị trí trụ sở (324) | UNVERIFIABLE | Như F19. Theo hiểu biết chung, bài so sánh doanh nghiệp đô thị và nông thôn, tức khoảng cách tới nhà đầu tư, không nói về vị trí sàn (xem MJ3). |
| F21 | Bae và cộng sự (2004) "Investibility" (97); Yao (2012) định nghĩa năng lực cạnh tranh (96) | UNVERIFIABLE | Hồ sơ chỉ có Bae, Karolyi & Stulz (NBER 2000), là bài khác; không có bản Yao (2012). |
| F22 | Vo & Phan (2017): 299 công ty HOSE 2005–2015; Nguyen và cộng sự (2020): 468 tuần (130) | UNVERIFIABLE (không đổi so với vòng 8, B18) | — |
| F23 | Hiệu ứng nhỏ nhất phát hiện được: 0,64σ (φ = 0); khoảng 1,3 lần khi cửa sổ trước 24 tháng; σ = 0,2, φ = 0,6 → 0,25, tức khoảng 22% (345) | TRUE (tự tính lại) | φ = 0: se = σ·√(1/24 + 1/193) = 0,2164σ; (z₀,₉₈₃ + z₀,₈) = 2,128 + 0,842 = 2,970 → 0,643σ. Tỷ số √(2/24)/√(1/24 + 1/193) = 1,33. exp(−0,248) = 0,78 → giảm khoảng 22%. Giá trị 1,24σ và 1,76σ hợp lý vì gần với hệ số phương sai dài hạn (1+φ)/(1−φ), có hiệu chỉnh cho mẫu nhỏ; chưa mô phỏng lại. |
| F24 | Đếm thời gian: 193 tháng (6/2009–6/2025); 18 tháng chuyển tiếp; 24 tháng sau; 20 và 8 cửa sổ (119, 279, 345) | TRUE (tự kiểm) | 16×12+1 = 193; 7/2025–12/2026 = 18; Q3/2020–Q2/2025 = 20; Q1/2027–Q4/2028 = 8 |

---

## (4) Độ khớp với NQ 57, Thông báo 7215 và bài toán 19 (research-grants)

| Yêu cầu | Nguồn (trích) | Vị trí trong đề cương | Đánh giá |
|---|---|---|---|
| Chỉ rõ bài toán lớn | TB 7215 (Dân trí): "nghiên cứu sinh cần chỉ rõ bài toán lớn của Hà Nội mà luận án dự kiến góp phần giải quyết" | idx 95, 108–111, 359 | **KHỚP** |
| Vấn đề thực tiễn hoặc khoảng trống | Như trên: "vấn đề thực tiễn hoặc khoảng trống khoa học - công nghệ cần nghiên cứu" | idx 95, 99–101, 107, Bảng 1 | **KHỚP**. Đợt hợp nhất ngày 28/12/2026 là một vấn đề thực tiễn có lịch chính thức. |
| Sản phẩm đầu ra, kết quả dự kiến | "xác định cụ thể sản phẩm đầu ra, kết quả dự kiến" | idx 114, 337, Bảng 5 | **KHỚP** |
| Chỉ tiêu có thể kiểm chứng | "các chỉ tiêu có thể kiểm chứng" | idx 115–121 (sáu chỉ tiêu, có mốc thời gian và bằng chứng công khai) | **KHỚP**. Đây là phần v9–v10 đã cải thiện rõ so với vòng 8. |
| Khả năng đưa vào thực tế, phục vụ hoạch định chính sách | TB 7215 (PTIT): "khả năng ứng dụng, chuyển giao hoặc phục vụ công tác hoạch định chính sách, quản trị và phát triển Thành phố" | idx 114, 121, 336–337, 511 | **KHỚP MỘT PHẦN**. Có báo cáo định hướng gửi Sở KH&CN và chỉ số mã nguồn mở, nhưng sau 2026 chỉ số chủ yếu đo HOSE; nếu UPCoM cũng chuyển trước 31/12/2026 (TT69) thì phần "Hà Nội" của chỉ số sau 2026 gần như không còn (xem m5). |
| Đơn vị phối hợp, tiếp nhận, sử dụng; văn bản cam kết | "xác định cơ quan, tổ chức, doanh nghiệp hoặc đơn vị có khả năng phối hợp, tiếp nhận, thử nghiệm hay sử dụng"; "văn bản cam kết phối hợp, tiếp nhận …" | idx 359 (danh sách người dùng; cam kết xin văn bản của ít nhất một đơn vị) | **KHỚP MỘT PHẦN**. Chưa có văn bản; chưa nêu đơn vị ưu tiên. |
| Tập trung toàn thời gian (NQ 57 Điều 11.3) | "tập trung toàn thời gian" | idx 401, 507 | **KHỚP** (có cam kết); rủi ro thực tế vì đang học song song ba chương trình (`outputs/checklist-dieu-kien.md`). |
| Thời gian hỗ trợ ≤ 48 tháng (Điều 13) | "không vượt quá 48 tháng" | idx 401 | **KHỚP**, nhưng không còn dư địa thời gian. |
| Công bố WoS Q1/Q2, tác giả chính (Điều 12.3) | "tạp chí khoa học hạng Q2 [Q1] thuộc cơ sở dữ liệu Web of Science … nếu người học là tác giả chính" | idx 120, 399 | **KHỚP** (mục tiêu ít nhất một bài WoS Q1/Q2) |
| Nghĩa vụ sau tốt nghiệp (Điều 15.2.e) | "Tham gia mạng lưới chuyên gia … tham gia tư vấn, phản biện, cung cấp luận cứ khoa học … đối với bài toán lớn" | idx 511–512 | **CHƯA KHỚP** (không nhắc tới). Nên thêm một câu cam kết. |
| Bài toán 19, hiện trạng | "Hà Nội là trung tâm tài chính lớn của cả nước, tuy nhiên hệ thống dịch vụ tài chính vẫn chưa đạt tầm khu vực, cần phát triển các khu thương mại tự do và dịch vụ tài chính thế hệ mới" | idx 95, 99 (GFCI) | **KHỚP MỘT PHẦN**. Có số liệu GFCI cho nửa đầu câu; nửa sau (khu thương mại tự do, dịch vụ thế hệ mới) nằm ngoài đề tài, đã nói rõ ở idx 359. |
| Câu hỏi 1 (mô hình trung tâm tài chính) | "Những mô hình trung tâm tài chính nào phù hợp với điều kiện phát triển của Hà Nội?" | idx 95, 109, H1, idx 336 | **KHỚP MỘT PHẦN**. Đề tài cung cấp bối cảnh định lượng (H1) và tổng hợp định tính, không đề xuất mô hình; idx 95 đã tự nói vậy. |
| Câu hỏi 2 (FinTech) | "Những công nghệ tài chính (PinTech) nào …" | idx 359 | **CHƯA KHỚP**, đã khai rõ là ngoài phạm vi |
| Câu hỏi 3 (minh bạch, hiệu quả thị trường) | "Những nền tảng công nghệ nào giúp tăng cường minh bạch và hiệu quả của thị trường tài chính?" | idx 110, MQI (chiều minh bạch và hiệu quả thông tin) | **KHỚP MỘT PHẦN**. Có thước đo nền, không có nền tảng công nghệ (idx 359 nói đúng). |
| Câu hỏi 4 (dịch vụ thế hệ mới) | "Làm thế nào phát triển các dịch vụ tài chính thế hệ mới dựa trên Fintech và kinh tế số?" | idx 359 | **CHƯA KHỚP**, đã khai rõ |
| Sản phẩm "Hệ thống dữ liệu tài chính đô thị" | Danh mục sản phẩm của bài toán 19 | idx 114 ("có thể là một cấu phần") | **KHỚP MỘT PHẦN**. Dùng chữ "có thể" là đúng mức; MQI là chỉ số thị trường quốc gia, không phải dữ liệu đô thị. |
| Sản phẩm "Trung tâm tài chính quốc tế tại Hà Nội" | Như trên | idx 114 ("đầu vào phân tích … đề tài không thiết kế sản phẩm này"; nhắc NQ 222) | **KHỚP MỘT PHẦN**, cách viết đúng mức |
| Căn cứ danh mục dùng để xét chọn | NQ 57 không nói danh mục bài toán lớn ở Điều 11 là QĐ 1193 hay danh mục mới theo Điều 35.1.c | idx 95, 529 | **CHƯA RÕ** [CẦN XÁC MINH với cơ quan quản lý], không do đề cương quyết định |

**Kết luận (không nói quá).** Đề cương v10 đáp ứng đủ các yêu cầu hình thức mà TB 7215 nêu: bài toán lớn, vấn đề thực tiễn, sản phẩm, chỉ tiêu kiểm chứng, người dùng dự kiến. Đề cương cũng tuân thủ hai điều kiện chính của NQ 57 (Điều 11.3, Điều 13). Về nội dung, đề tài góp phần **một phần** vào câu hỏi 1 và 3 của bài toán 19 bằng thước đo và bằng chứng định lượng nền. Đề tài không trả lời câu hỏi 2 và 4, và tự khai điều này đúng mức. Hai điểm hạn chế độ khớp có thật: (i) chưa có đơn vị tiếp nhận có văn bản; (ii) phần "Hà Nội" của sản phẩm sau 2026 mỏng nếu UPCoM sang HOSE đúng hạn TT69.

**Đề xuất tăng độ khớp (không mở rộng phạm vi, không nói quá):**
1. Nêu một đơn vị tiếp nhận ưu tiên (ví dụ HNX, đơn vị sẽ vận hành thị trường trái phiếu và phái sinh) và xin văn bản trước khi nộp hồ sơ. Ghi vào chỉ tiêu (6): "kèm văn bản xác nhận nhu cầu của ít nhất một đơn vị".
2. Thêm một câu ở mục 9 (idx 511): "Thí sinh sẵn sàng thực hiện nghĩa vụ tại điểm e khoản 2 Điều 15 Nghị quyết số 57/2026/NQ-HĐND: tham gia mạng lưới chuyên gia và cung cấp luận cứ khoa học cho bài toán số 19 khi được mời."
3. Ở idx 114 hoặc 337, nói rõ sau 2026 chỉ số tiếp tục phục vụ Hà Nội theo cách nào. Cách đúng mức là coi mã nguồn và chuẩn đo như một khuôn mẫu có thể áp cho thị trường trái phiếu và phái sinh do HNX vận hành, và giữ việc áp dụng thực tế ở mục hướng nghiên cứu (idx 512). Không nên hứa xây chỉ số trái phiếu trong luận án.
4. Sửa MJ3 trước khi dùng phân tích trụ sở Hà Nội làm điểm nối với bài toán 19; nếu để nguyên lời diễn giải hiện tại, hội đồng có thể cho là nói quá.

---

## (5) Phát hiện theo mức

### CRITICAL
Không có.

### MAJOR

**MJ1. Kênh chỉ số dựa trên danh sách FTSE không có biến thiên trong nhóm chuyển sàn.**
- idx: 322 (kéo theo 268, 323). Skill: fact-checker, credible-claims, vn-legal-verify.
- Căn cứ: FTSE Russell FAQ v1.3 (8/2026), Q6: "The table below lists the Vietnamese securities that passed the FTSE GEIS index eligibility screen … based on data cut-off as of 30 June 2026". Cả 27 mã đều có cột Exchange là "HSX". Như vậy (a) không mã HNX nào thuộc danh sách, nên biến chỉ bằng 0 với mọi mã chuyển sàn và hệ số tương tác không ước lượng được; (b) danh sách lập với dữ liệu đến 30/6/2026, nên câu "đo … bằng dữ liệu đến ngày 30/6/2025" mâu thuẫn với chính nguồn của danh sách. Việc loại các mã FTSE khỏi nhóm đối chứng HOSE (idx 333, 350) vẫn đúng và nên giữ. VN-Index cũng không dùng làm kênh được, vì theo QĐ 737 mọi mã chuyển sàn đều vào VN-Index. Kênh có biến thiên thực sự là các chỉ số có sàng lọc tỷ lệ tự do chuyển nhượng và vòng quay (QĐ 738, Quy tắc chỉ số VNAllshare 4.1: "cổ phiếu niêm yết trên HOSE đáp ứng tư cách tham gia và các tiêu chí sàng lọc"; "tỷ lệ free-float … Tỷ suất quay vòng").
- Sửa:
  - "và việc vào chỉ số FTSE chỉ liên quan đến mã có trong danh sách dự kiến." → "và việc vào các chỉ số của HOSE có sàng lọc, ngoài VN-Index, chỉ liên quan đến mã đáp ứng tiêu chí về tỷ lệ cổ phiếu tự do chuyển nhượng và vòng quay."
  - "và biến chỉ mã thuộc danh sách dự kiến của FTSE Russell (mức chịu cú sốc chỉ số)." → "và biến chỉ mã đáp ứng tiêu chí sàng lọc của chỉ số VNAllshare khi áp các tiêu chí này cho dữ liệu đến ngày 30/6/2025 (mức chịu cú sốc chỉ số) [CẦN XÁC MINH cách Quy tắc chỉ số VNAllshare áp dụng cho mã chuyển sàn]. Danh sách cổ phiếu Việt Nam đủ điều kiện vào chỉ số FTSE Russell, lập với dữ liệu đến ngày 30/6/2026, chỉ gồm mã niêm yết tại HOSE (FTSE Russell, 2026), nên kênh FTSE không có biến thiên giữa các mã chuyển sàn và chỉ được dùng để loại mã khỏi nhóm đối chứng HOSE."
  - Nếu dẫn Quy tắc VNAllshare thành tài liệu tham khảo, thêm QĐ 738/QĐ-SGDHCM vào danh mục với nhãn [CẦN XÁC MINH số hiệu và ngày], vì bản OCR cùng đợt với QĐ 737.

**MJ2. Dẫn Amihud và cộng sự (1997) cho chiều lan tỏa ngược với kết quả của bài.**
- idx: 334. Skill: fact-checker, credible-claims.
- Căn cứ (tai-lieu-gop.txt, bản WP): "an improvement in the trading mechanism for security A will have a positive effect on the liquidity of B"; "the price of the secondary stock should increase upon the transfer announcement of the primary stock … Our results support this hypothesis." Bài ủng hộ lan tỏa **dương**. Nếu điều đó xảy ra với nhóm đối chứng HOSE, δ bị **đánh giá thấp**. Đề cương lại đặt trích dẫn này ngay trước kịch bản nhóm đối chứng **mất** thanh khoản (δ phóng đại). Vòng 8 (B2) đã chấm TRUE cho câu "ghi nhận thanh khoản lan tỏa" nhưng chưa xét chiều mà đề cương dùng.
- Sửa: "Amihud và cộng sự (1997) ghi nhận thanh khoản lan tỏa giữa các cổ phiếu liên quan; nếu nhóm đối chứng HOSE mất thanh khoản do dòng lệnh chuyển sang cổ phiếu chuyển sàn, δ phóng đại tác động, nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác." → "Nếu nhóm đối chứng HOSE mất thanh khoản do dòng lệnh chuyển sang cổ phiếu chuyển sàn, δ phóng đại tác động, nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác."
- Và: "Ngược lại, Hisada (2018) cho thấy thanh khoản của cổ phiếu sẵn có trên sàn tiếp nhận cũng tăng trong ngắn hạn quanh đợt hợp nhất Tokyo–Osaka; nếu điều tương tự xảy ra với nhóm đối chứng HOSE, δ đánh giá thấp tác động." → "Ngược lại, tác động lan tỏa có thể theo chiều dương: Amihud và cộng sự (1997) thấy khi một loại cổ phiếu của doanh nghiệp được chuyển sang cơ chế giao dịch tốt hơn, loại cổ phiếu còn lại của cùng doanh nghiệp cũng tăng giá, phù hợp với thanh khoản lan tỏa dương giữa các chứng khoán có giá trị tương quan; Hisada (2018) cho thấy thanh khoản của cổ phiếu sẵn có trên sàn tiếp nhận cũng tăng trong ngắn hạn quanh đợt hợp nhất Tokyo–Osaka. Nếu điều tương tự xảy ra với nhóm đối chứng HOSE, δ đánh giá thấp tác động."

**MJ3. Phân tích theo trụ sở Hà Nội được diễn giải vượt quá điều thiết kế đo được.**
- idx: 324–325. Skill: credible-claims, peer-review.
- Căn cứ: (a) Thiết kế chỉ ước lượng **khác biệt** của δ giữa hai nhóm doanh nghiệp. Khác biệt đó không phải "phần thanh khoản mà thị trường vốn Hà Nội mất": cả hai nhóm có thể cùng tăng thanh khoản, và thanh khoản của một mã không thuộc về địa phương nào. (b) Chênh lệch bằng 0 không chứng tỏ "vị trí sàn ít quan trọng" khi chưa có khoảng tin cậy hẹp; đề cương lại chưa nêu số mã có trụ sở tại Hà Nội trong 299 mã, cũng chưa có hiệu ứng nhỏ nhất phát hiện được cho tương tác này. (c) Hai bài được dẫn (F19–F20, UNVERIFIABLE) nói về khoảng cách giữa nhà đầu tư và doanh nghiệp. Khi sàn đổi, nhà đầu tư không đổi chỗ, nên cơ chế cần gọi tên là sự chú ý và thông tin gắn với sàn. (d) Idx 323 nói "các hệ số tương tác … không đưa vào thủ tục Holm", nhưng câu này đứng trước đoạn về trụ sở, nên chưa rõ tương tác trụ sở có thuộc loại đó không.
- Sửa:
  - "Phân tích theo trụ sở doanh nghiệp cho biết Hà Nội mất gì khi cổ phiếu niêm yết rời HNX." → "Phân tích theo trụ sở doanh nghiệp kiểm tra xem tác động của việc chuyển sàn có khác nhau giữa doanh nghiệp có trụ sở tại Hà Nội và doanh nghiệp ở nơi khác hay không."
  - "[CẦN ĐỐI CHIẾU bản gốc của hai bài]." → "[CẦN ĐỐI CHIẾU bản gốc của hai bài]. Hai bài này nói về khoảng cách giữa nhà đầu tư và doanh nghiệp, không nói về vị trí của sàn; khi sàn đổi, nhà đầu tư không đổi chỗ, nên kênh mà đề tài kiểm tra là sự chú ý và thông tin gắn với sàn niêm yết, chẳng hạn mức độ đưa tin và việc có mặt trong HNX-Index."
  - "Nếu chênh lệch khác 0, kết quả cho biết phần thanh khoản mà thị trường vốn Hà Nội mất cùng với sàn cổ phiếu niêm yết; nếu chênh lệch bằng 0, kết quả cho thấy vị trí sàn ít quan trọng với doanh nghiệp Hà Nội khi giao dịch đã điện tử hóa toàn quốc." → "Nếu chênh lệch khác 0, kết quả gợi ý vị trí sàn có liên hệ với thanh khoản của doanh nghiệp có trụ sở tại Hà Nội; nếu khoảng tin cậy hẹp quanh 0, kết quả không ủng hộ vai trò của vị trí sàn khi giao dịch đã điện tử hóa toàn quốc; nếu khoảng tin cậy rộng, kết quả được gọi là chưa đủ cơ sở kết luận. Tệp đăng ký ghi số mã có trụ sở tại Hà Nội trong các mã chuyển sàn và hiệu ứng nhỏ nhất phát hiện được của hệ số tương tác này; hệ số này là phân tích phụ, không đưa vào thủ tục Holm."

### MINOR

| Mã | idx | Skill | Căn cứ | Chuỗi gốc → chuỗi thay thế |
|---|---|---|---|---|
| m1 | 101 | vn-legal-verify | L9: câu gốc của VNX nằm trong gạch đầu dòng về hai ngày tạm ngừng | "và nêu rõ giao dịch tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành;" → "và nêu rõ trong hai ngày tạm ngừng, giao dịch tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành;" |
| m2 | 222 | vn-legal-verify | L10: TT120 Điều 4.1 ghi "Sở giao dịch chứng khoán Việt Nam"; khoản 2 cho UBCKNN quyền điều chỉnh | "biên độ do Sở giao dịch quyết định sau khi Ủy ban Chứng khoán Nhà nước chấp thuận (Bộ Tài chính, 2020)" → "biên độ do Sở Giao dịch Chứng khoán Việt Nam quyết định sau khi Ủy ban Chứng khoán Nhà nước chấp thuận, và Ủy ban Chứng khoán Nhà nước có thể điều chỉnh biên độ khi cần ổn định thị trường (Bộ Tài chính, 2020)" |
| m3 | 333 | credible-claims | Nới biên độ ràng buộc mạnh hơn ở mã hay chạm biên độ, mà mã chuyển sàn có biến động lớn hơn (chính idx 322 đã nói vậy), nên "như nhau" là nói quá | "chúng tác động như nhau lên cổ phiếu chuyển sàn và nhóm đối chứng HOSE, và ngưỡng lợi suất chung" → "chúng áp dụng chung cho cổ phiếu chuyển sàn và nhóm đối chứng HOSE nhưng có thể tác động mạnh hơn ở mã thường chạm biên độ, nên ngày áp dụng được ghi là một cú sốc trùng thời gian, ước lượng được báo cáo thêm với cửa sổ sau cắt tại ngày đó, và ngưỡng lợi suất chung" |
| m4 | 333 | vn-legal-verify | L20: Thứ trưởng "đặt vấn đề nghiên cứu khả năng … rút ngắn chu kỳ thanh toán từ T+2 xuống mức thấp hơn" | "đang nghiên cứu nới biên độ dao động giá và giao dịch xuyên trưa (Thời báo Tài chính Việt Nam, 2026)" → "đang nghiên cứu nới biên độ dao động giá và giao dịch xuyên trưa, và Bộ Tài chính đặt vấn đề nghiên cứu rút ngắn chu kỳ thanh toán (Thời báo Tài chính Việt Nam, 2026)" |
| m5 | 350 | vn-legal-verify, credible-claims | L4: TT69 điểm e đặt hạn UPCoM "chậm nhất đến hết ngày 31 tháng 12 năm 2026", nên trường hợp này là khả năng chính, không phải ngoại lệ. Kéo theo: cận UPCoM ở idx 334 và ô "Cổ phiếu UPCoM" ở Hình 1 có thể không dùng được cho giai đoạn sau. | "Nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt hoặc trong 24 tháng sau sự kiện," → "Theo văn bản hiện hành, cổ phiếu UPCoM phải được chuyển sang HOSE chậm nhất đến hết ngày 31/12/2026 (Bộ Tài chính, 2023), nên đề tài coi trường hợp sau là khả năng chính: nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt hoặc trong 24 tháng sau sự kiện," |
| m6 | 128 | fact-checker | F11 | "chẳng hạn, Arnold và cộng sự (1999, dẫn theo Hisada, 2018) thấy hợp nhất sàn làm thanh khoản tăng." → "chẳng hạn, Arnold và cộng sự (1999, dẫn theo Hisada, 2018) thấy việc hợp nhất các sàn khu vực ở Hoa Kỳ làm thanh khoản tăng nhờ lợi thế quy mô." |
| m7 | 330 | fact-checker | F4: Bảng 26 còn có "Broad Stock Index Levels" | "(3 trong 144 nhân tố của kỳ GFCI 40; Wardle & Mainelli, 2026)" → "(3 trong 144 nhân tố của kỳ GFCI 40, cùng bảng với nhân tố mức chỉ số cổ phiếu; Wardle & Mainelli, 2026)" |
| m8 | 221 | consistency-checker | Ghi chú Bảng 2 gọi so sánh theo quy mô là "mô tả", trong khi idx 323 đưa tương tác với quy mô vào hồi quy có suy diễn hoán vị | "so sánh theo giai đoạn căng thẳng và theo quy mô doanh nghiệp là phân tích mô tả." → "so sánh theo giai đoạn căng thẳng là phân tích mô tả; các tương tác theo kênh, theo quy mô và theo trụ sở doanh nghiệp là phân tích phụ đăng ký trước, không đưa vào thủ tục Holm." |
| m9 | 112 | credible-claims | Idx 323 nói rõ hệ số tương tác "không đo riêng tác động của từng quy tắc", nên mục tiêu không nên hứa "tác động theo từng kênh" | "kể cả tác động theo từng kênh biên độ, bước giá và chỉ số," → "kể cả khác biệt của tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số," |
| m10 | 349, 419 | consistency-checker | Idx 227 chuyển trường hợp "không được phép" dùng dữ liệu GFCI sang phương án thứ nhất, nhưng phương án thứ nhất chỉ nói "không số hóa được" | "Nếu không số hóa được điểm GFCI theo kỳ," → "Nếu không số hóa được hoặc không được phép dùng điểm GFCI theo kỳ,"; và "không số hóa được điểm GFCI;" → "không số hóa được hoặc không được phép dùng điểm GFCI;" |
| m11 | 595 | consistency-checker | Đề cương ký ngày 30/9/2026 nhưng dẫn sự kiện sau ngày đó (họp báo ngày 6/10/2026 trên Thời báo TC; bài Tuổi Trẻ tháng 10/2026) | "Hà Nội, ngày 30 tháng 9 năm 2026" → "Hà Nội, ngày … tháng 10 năm 2026" (thí sinh điền ngày nộp thật; giữ các mốc "tính đến ngày 30/9/2026" ở Bảng 6, Bảng 7 và idx 149) |
| m12 | 527, 528 | citation-management (APA 7) | Tên trang trùng tên tác giả thì APA bỏ tên trang; Tuổi Trẻ: tiêu đề bài là "HOSE dự kiến chia …" (cũng là slug của URL); hai mục thiếu ngày đăng | "Tuổi Trẻ Online. (2026). HOSE chia cổ phiếu thành hai bảng Prime Board và Standard Board. Tuổi Trẻ Online. https://" → "Tuổi Trẻ Online. (2026) [CẦN BỔ SUNG ngày đăng]. HOSE dự kiến chia cổ phiếu thành hai bảng Prime Board và Standard Board. https://"; "Thời báo Tài chính Việt Nam. (2026). Chuyển toàn bộ cổ phiếu HNX sang HOSE trong năm 2026, nghiên cứu giao dịch xuyên trưa và nới biên độ. Thời báo Tài chính Việt Nam. https://" → "Thời báo Tài chính Việt Nam. (2026) [CẦN BỔ SUNG ngày đăng]. Chuyển toàn bộ cổ phiếu HNX sang HOSE trong năm 2026, nghiên cứu giao dịch xuyên trưa và nới biên độ. https://" |
| m13 | 532, 544, 549, 568 | citation-management | SKILL.md: "NEVER leave an @article entry without volume, pages, and DOI". Hồ sơ có sẵn DOI của 4 bài. | "Journal of Financial Economics, 45(3), 365–390." → "Journal of Financial Economics, 45(3), 365–390. https://doi.org/10.1016/S0304-405X(97)00021-4"; "The Journal of Finance, 67(2), 719–760." → "The Journal of Finance, 67(2), 719–760. https://doi.org/10.1111/j.1540-6261.2012.01729.x"; "Review of International Economics, 28(1), 62–81." → "Review of International Economics, 28(1), 62–81. https://doi.org/10.1111/roie.12441"; "Urban Studies, 49(6), 1275–1296." → "Urban Studies, 49(6), 1275–1296. https://doi.org/10.1177/0042098011408143". Các bài tạp chí còn lại chưa có DOI trong hồ sơ: đưa vào mục (7). |
| m14 | 552, 591 | citation-management | Báo cáo có tháng phát hành và URL chính thức (hồ sơ [33], [30]) | "Wardle, M., & Mainelli, M. (2026). The Global Financial Centres Index 40. Z/Yen Group & China Development Institute." → "Wardle, M., & Mainelli, M. (2026, September). The Global Financial Centres Index 40. Z/Yen Group & China Development Institute. https://www.longfinance.net/media/documents/GFCI_40_Report_2026.09.16_v1.2.pdf"; "FTSE Russell. (2026). Reclassification" → "FTSE Russell. (2026, August). Reclassification" |
| m15 | 547 | fact-checker | F18: tác giả, tên bài, tạp chí và năm đã khớp qua Roth và cộng sự; chỉ còn tập, số và trang chưa có nguồn gốc | "Health Services Research, 53(6), 4138–4156. [CẦN XÁC MINH]" → "Health Services Research, 53(6), 4138–4156. [CẦN XÁC MINH tập, số và trang]" |
| m16 | 85 | consistency-checker | Bảng chữ viết tắt ghi tiếng Việt cho mọi mục khác, riêng OSF chỉ có tên tiếng Anh | "Open Science Framework" → "nền tảng khoa học mở (Open Science Framework)" |
| m17 | 323–325 so với 316 | consistency-checker | Đoạn mới viết "Dᵢ·Postₜ" bằng ký tự chỉ số dưới Unicode; idx 316 viết Di, Postt bằng chỉ số dưới định dạng của Word | Trong docx, đổi "Dᵢ·Postₜ" (3 chỗ) thành Di·Postt với i, t định dạng chỉ số dưới như idx 316 |

**Kiểm tra nhất quán (consistency-checker), các mục không thấy lỗi:**
- Mục lục, đánh số mục 4.1–11 và 4.3.1–4.3.10 khớp với thân bài.
- Bảng 1–7 và Hình 1–3 đánh số liên tục; mỗi bảng và hình đều được nhắc trong bài.
- Dẫn chiếu "cuối mục 4.2" (107), "mục 4.3.10" (227, 419), "cuối mục 4.3.8" (325), "mục 4.3.7" (336), "mục 4.3.8" (358), "mục 4.1" (392) đều đúng chỗ.
- Phương trình (1)–(7) và các dẫn chiếu "(5)–(7)", "(6)", "(1)" đúng.
- Mốc thời gian: 6/2009, 30/6/2025, 7/2025–12/2026, 28/12/2026, 1/2027, 24 tháng, Q3/2020–Q2/2025, Q1/2027–Q4/2028 thống nhất trong toàn bài.
- Giả thuyết H1–H4 thống nhất giữa idx 154, Bảng 2, idx 204, 4.3.7, 4.3.10, 4.4, 7.3 và Bảng 5.
- Holm: họ H1–H3 ở mức 5%, mức một phía 0,05/3 trong tính hiệu ứng nhỏ nhất phát hiện được, giá trị p theo từng giả thuyết (346) nhất quán.
- Năm phương án dự phòng: idx 349–350 khớp với idx 419, chỉ lệch chữ ở m10.
- Trích dẫn hai chiều: mọi tác giả và năm trong danh mục đều được trích trong bài và ngược lại. Kiểm bằng `grep` trên idx 0–517. Arnold và cộng sự (1999) chỉ được trích gián tiếp nên đúng là không có trong danh mục. Các mục mới (TT120, VNX 2026, Tuổi Trẻ Online 2026, FTSE Russell 2026, Wardle & Mainelli 2026, Coval & Moskowitz 1999, Loughran & Schultz 2005, Thời báo TC VN 2026) đều có trong danh mục và được trích. VietnamPlus: 0 lần xuất hiện trong bài.
- Thứ tự chữ cái: danh mục tiếng Việt (Bộ Tài chính → Hội đồng → Nguyễn → Quốc hội → Sở … Thành phố → Sở … Việt Nam → Thời báo → Tuổi Trẻ → Ủy ban) và tiếng Anh (Amihud 2002 trước Amihud và cộng sự 1997; Coval sau Corwin; Loughran sau Lo; Nguyen, N. trước Nguyễn, T. B.) đều đúng APA.
- Chữ viết tắt mới: WoS không dùng dạng viết tắt; OSF và VNX đã có trong bảng; không thấy chữ viết tắt nào được dùng mà chưa định nghĩa. "Q1/Q2" là hạng tạp chí thông dụng; nếu muốn chặt chẽ có thể thêm vào bảng.

---

## Claim record (credible-claims, tóm tắt)

| Khẳng định | Căn cứ | Phần chưa giải | Ngôn ngữ được phép |
|---|---|---|---|
| H1: phát triển thị trường cổ phiếu liên hệ với điểm GFCI | Hồi quy bảng (7), hiệu ứng cố định theo trung tâm và theo kỳ, sai số phân cụm theo quốc gia | Trùng lặp cơ học với nhân tố WFE trong GFCI (F4); quyền dùng dữ liệu lịch sử | "liên hệ có điều kiện" (đề cương đã dùng đúng) |
| H2: MQI của HNX thấp hơn HOSE | Chênh lệch theo tháng, bootstrap khối dừng | Biên độ và bước giá khác nhau giữa sàn (đã có nhãn); thành phần mẫu | "thấp hơn", có điều kiện theo mẫu đối sánh. Đúng mức. |
| H3: Amihud giảm sau khi chuyển sàn | Khác biệt kép trên một sự kiện, bootstrap tự hồi quy | Cú sốc trùng thời gian; UPCoM có thể không còn làm đối chứng (m5); lan tỏa theo cả hai chiều (MJ2) | "tác động gộp của sàn", chỉ cho một sự kiện. Đúng mức. |
| H4: khoảng cách khả năng đầu tư thu hẹp | Ước lượng kèm khoảng tin cậy | Hiệu ứng nhỏ nhất phát hiện được lớn | "ước lượng". Đúng mức. |
| Phân tích theo kênh | Tương tác với mức chịu cú sốc đo trước sự kiện | Kênh FTSE không có biến thiên (MJ1) | "khác biệt theo mức chịu cú sốc", không phải "tác động của từng quy tắc" (m9) |
| Phân tích theo trụ sở Hà Nội | Tương tác với biến trụ sở | Cơ chế, hiệu ứng nhỏ nhất phát hiện được, số mã (MJ3) | Mô tả dị biệt; **không** dùng "Hà Nội mất gì" |
| Khớp với bài toán 19 | QĐ 1193 Phụ lục | Danh mục dùng để xét chọn chưa rõ | "góp phần một phần vào câu hỏi 1 và 3" (đề cương đã dùng đúng) |

Quyết định về câu chữ cuối cùng thuộc về thí sinh và người hướng dẫn.

---

## (6) Câu hỏi hội đồng có thể hỏi và gợi ý trả lời ngắn (peer-review)

**Nhận xét tổng thể (bản nháp).** *Điểm mạnh:* đợt hợp nhất có ngày xác định do văn bản quy định; câu hỏi gắn với chính sách thời sự; phần pháp lý được đối chiếu tới văn bản gốc; đăng ký trước kèm tính công suất trung thực; suy luận được chọn phù hợp với một sự kiện duy nhất; giới hạn và phạm vi khai rõ. *Điểm yếu chính:* (1) phần nối với Hà Nội sau 2026 còn mỏng, và hai đoạn mới (kênh chỉ số, trụ sở Hà Nội) có lỗi thực tế hoặc diễn giải (MJ1, MJ3); (2) thiết kế phụ thuộc vào nhóm đối chứng HOSE, vì UPCoM nhiều khả năng sang HOSE cùng lúc (m5); (3) khối lượng công việc lớn so với thời gian 48 tháng, trong khi thí sinh đang học song song nhiều chương trình.

| # | Câu hỏi | Gợi ý trả lời ngắn |
|---|---|---|
| 1 | Luận án trả lời "phương thức xây dựng Hà Nội thành trung tâm tài chính" thế nào nếu kết quả chỉ là thay đổi thanh khoản? | Không trả lời trọn. Luận án cung cấp thước đo nền và bằng chứng về vai trò của sàn cho câu hỏi 1 và 3, rồi tổng hợp định tính định hướng chuyên môn hóa cho các thị trường HNX tiếp tục vận hành (idx 95, 359). |
| 2 | Giao dịch đã điện tử hóa toàn quốc, vậy vị trí sàn ảnh hưởng gì tới doanh nghiệp Hà Nội? | Đây là câu hỏi thực nghiệm; kênh có thể có là sự chú ý và thông tin gắn với sàn. Kết quả bằng 0 cũng là thông tin chính sách, nếu khoảng tin cậy đủ hẹp (MJ3). |
| 3 | Theo TT69, UPCoM phải sang HOSE trước 31/12/2026. Nhóm đối chứng UPCoM còn dùng được không? | Coi là khả năng chính. Ước lượng chính dựa vào nhóm đối chứng HOSE đã loại mã FTSE; UPCoM chỉ dùng cho giai đoạn trước (m5, idx 350). |
| 4 | Không mã HNX nào thuộc danh sách FTSE, vậy kênh chỉ số đo thế nào? | Đổi sang tiêu chí sàng lọc của chỉ số có điều kiện free-float và vòng quay (MJ1); danh sách FTSE chỉ dùng để làm sạch nhóm đối chứng. |
| 5 | Một sự kiện, một ngày: suy luận có đáng tin không? | Suy luận dựa trên chuỗi chênh lệch theo tháng, giá trị p từ bootstrap tự hồi quy; kích thước kiểm định được kiểm bằng mô phỏng trước khi đăng ký; suy luận hoán vị chỉ để bổ sung vì có xu hướng bác bỏ quá nhiều (idx 318–319). |
| 6 | Mức tác động nhỏ nhất mà thiết kế phát hiện được là bao nhiêu? | Khoảng 0,64σ đến 1,76σ tùy mức tự tương quan; con số minh họa là giảm khoảng 22% độ phi thanh khoản; sẽ ước lượng lại và ghi vào tệp đăng ký (idx 345). |
| 7 | Biên độ ±10% xuống ±7% có làm Amihud giảm cơ học không? | Có; vì vậy Amihud được tính trên các ngày có lợi suất dưới một ngưỡng chung và không liền sau ngày chạm biên độ, đối chiếu với vòng quay (idx 224). |
| 8 | Điểm GFCI có chứa sẵn số liệu giao dịch cổ phiếu, vậy H1 có phải là phép lặp không? | Có trùng lặp một phần (3 trong 144 nhân tố); vì vậy β được gọi là liên hệ có điều kiện và có ước lượng lại trên các kỳ không trùng lặp (idx 330, 347). |
| 9 | Đã có quyền dùng dữ liệu GFCI lịch sử và dữ liệu thương mại chưa? | Chưa; sẽ xin Long Finance và xác nhận giấy phép trong quý 1 năm thứ nhất; có phương án dự phòng (idx 227–228, 349). |
| 10 | M5 do chính thí sinh phát triển, có thiên vị không? | M5 được xử lý như mọi mô hình khác, cùng ngân sách tinh chỉnh, và kết quả được báo cáo cả khi có lẫn khi không có M5 (idx 266). |
| 11 | Thí sinh đang học song song ba chương trình và có chín bản thảo, làm sao bảo đảm học toàn thời gian? | Cam kết hoàn thành, bảo lưu hoặc dừng các chương trình trước khi nhập học (idx 507); nên chuẩn bị minh chứng cụ thể. |
| 12 | Đề tài tài chính định lượng hợp với chương trình Kinh tế và Quản lý (thiên về kinh tế hành vi) ở điểm nào? | Phần định hướng chuyên môn hóa và chính sách thị trường vốn; Hisada (2018) có kênh tâm lý nhà đầu tư. Cần dẫn đúng văn bản tuyển sinh, hiện chưa có trong hồ sơ (L21). |
| 13 | Đăng ký trước ngày 28/12/2026, khi chưa nhập học, thì người hướng dẫn góp ý ở đâu? | Đăng ký sau khi xin góp ý của người hướng dẫn dự kiến (idx 267); mọi thay đổi sau đó được ghi là lệch khỏi kế hoạch. |
| 14 | Sau 2026, ai dùng Chỉ số chất lượng thị trường vốn và để làm gì? | HOSE, UBCKNN, nhà nghiên cứu; với Hà Nội, khuôn mẫu đo có thể áp cho thị trường trái phiếu và phái sinh do HNX vận hành, nhưng đó là hướng mở rộng sau luận án (idx 512). |

---

## (7) Tài liệu cần tìm mới (vòng 10)

| # | Tài liệu | Vì sao cần (mã) | Dùng ở idx | Cần phần nào | Nơi tìm hợp pháp | Từ khóa | Ưu tiên |
|---|---|---|---|---|---|---|---|
| T1 | Danh sách 299 mã niêm yết HNX kèm địa chỉ trụ sở đăng ký | MJ3: biến trụ sở, số mã tại Hà Nội | 324–325 | Danh sách mã, địa chỉ tại 30/6/2025 | hnx.vn, cổng công bố thông tin, báo cáo thường niên, nhà cung cấp dữ liệu | "danh sách cổ phiếu niêm yết HNX", "trụ sở chính" | CAO |
| T2 | Quy tắc chỉ số VNAllshare 4.1 (QĐ 738/QĐ-SGDHCM): bản PDF gốc, số và ngày đọc được | MJ1: kênh chỉ số thay thế | 322 | Mục 4.1 các bước sàng lọc; điều khoản cho mã niêm yết mới hoặc chuyển sàn | stream.vnx.vn (hồ sơ đã có OCR) | "Quy tắc chỉ số VNAllshare phiên bản 4.1" | CAO |
| T3 | Kế hoạch chuyển cổ phiếu UPCoM của VNX theo khoản 4 Điều 4 TT57, hoặc văn bản lùi hạn 31/12/2026 | m5, nhãn ở idx 101 | 101, 317, 350 | Lịch chuyển, phạm vi | vnx.vn, ssc.gov.vn, mof.gov.vn | "chuyển cổ phiếu đăng ký giao dịch UPCoM sang HOSE", "kế hoạch VNX" | CAO |
| T4 | Hướng dẫn của HOSE/VNX về giá tham chiếu, biên độ ngày đầu và bước giá của mã chuyển sàn ngày 28/12/2026 | Nhãn ở idx 223, 333 | 223, 322, 333 | Quy tắc ngày đầu, bước giá | vnx.vn, hsx.vn | "giá tham chiếu ngày giao dịch đầu tiên cổ phiếu chuyển sàn" | CAO |
| T5 | Bản gốc Coval & Moskowitz (1999) và Loughran & Schultz (2005) | F19–F20, MJ3, nhãn ở idx 324 | 217, 324 | Tóm tắt, kết quả chính | Thư viện (JSTOR/ScienceDirect), SSRN | "Home bias at home", "Liquidity: Urban versus rural firms" | TRUNG BÌNH–CAO |
| T6 | Danh sách FTSE Russell các kỳ review tháng 3/2027 trở đi (newly eligible), để xem mã chuyển sàn có vào không | MJ1 (kênh FTSE sau sự kiện); nhóm đối chứng | 322, 333 | Danh sách thành phần | lseg.com/ftse-russell (cần tài khoản) | "FTSE GEIS Vietnam review March 2027" | TRUNG BÌNH |
| T7 | Ngày đăng chính xác của bài Tuổi Trẻ và bài Thời báo TC | m12 | 527–528 | Dòng ngày đăng | Trang báo | — | THẤP |
| T8 | DOI và trang của các bài tạp chí còn lại trong danh mục; tập, số và trang của Daw & Hatfield (2018) | m13, m15 | danh mục | DOI, trang | Trang nhà xuất bản, CrossRef (người dùng tự tra) | Tên bài | THẤP |
| T9 | Thông báo tuyển sinh tiến sĩ 2026 của Trường Quốc tế và Phụ lục 1 (vẫn thiếu từ vòng 8, A11) | L21 | 389, 395, 401 | Nhóm ngành, tín chỉ bổ sung, thời gian đào tạo | is.vnu.edu.vn | "thông báo tuyển sinh tiến sĩ 2026 Trường Quốc tế" | CAO |
| T10 | Bản gốc TB 7215/SKHCN và quyết định của UBND về quản lý hoạt động hỗ trợ NCS (thành phần hồ sơ, biểu mẫu) | Mục (4) | 359 | Thành phần hồ sơ, mẫu thuyết minh, mẫu văn bản cam kết | Cổng Sở KH&CN Hà Nội | "Thông báo 7215/SKHCN", "quản lý hoạt động hỗ trợ nghiên cứu sinh" | CAO |
| T11 | Bản gốc Bae, Chan & Ng (2004) và Yao (2012) | F21 | 96–97 | Định nghĩa | Thư viện; HAL/theses.fr | "Investibility and return volatility"; "Compétitivité et attractivité des places financières" | THẤP |

---

*Bản nháp làm việc. Thí sinh cần tự kiểm lại mọi trích dẫn, số liệu và vị trí trước khi dùng. Báo cáo này không sửa đề cương.*
