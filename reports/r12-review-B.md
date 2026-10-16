# Báo cáo Agent B, vòng 12: kiểm chứng, nhất quán và độ khớp với đề án Hà Nội

Đề cương được kiểm: v11, "Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội" (`scratchpad/r12/dump-v11.txt`, idx 0–611). Ngày lập: 16/10/2026. Đây là bản nháp làm việc để thí sinh và người hướng dẫn tự kiểm lại. Báo cáo không sửa đề cương và không đổi tên đề tài.

---

## (1) Bằng chứng tuân thủ

**Các skill đã gọi bằng Skill tool, theo thứ tự:**
1. `vn-legal-verify`: đối chiếu các khẳng định pháp lý mới hoặc đã sửa ở v11 với văn bản gốc trong hồ sơ; gắn KHỚP / LỆCH / KHỚP MỘT PHẦN / CHƯA CÓ NGUỒN kèm bậc nguồn.
2. `fact-checker`: chấm số liệu, DOI mới thêm và mô tả văn liệu theo thang TRUE … UNVERIFIABLE.
3. `credible-claims`: cập nhật claim record; soát các câu mới xem có nói quá bằng chứng không.
4. `consistency-checker`: làm theo checklist 10 nhóm. **Không chạy** `latex_extractor.py` hay `crossref_validator.py`.
5. `citation-management`: chỉ đọc `SKILL.md`. **Không chạy** script nào, không gọi OpenAlex hay CrossRef.
6. `research-grants`: chấm lại độ khớp với NQ 57 (Điều 11.3, 12, 13, 15.2.e), Thông báo 7215 và bài toán 19, theo các nhóm lỗi "Mismatch with Agency Mission", "Vague Objectives" và "Overly Ambitious".
7. `peer-review`: viết nhận xét tổng thể và câu hỏi theo kiểu hội đồng. Người dùng là tác giả nên quyền xem được bảo đảm. Mọi xử lý chạy cục bộ; không chạy script của skill.

**Tệp đã đọc (chỉ đọc):** `dump-v11.txt` (đọc hết, idx 0–611); `reports/r10-review-B.md`; `outputs/round-11/nhat-ky-thay-doi-round-11.md`; `ho-so/TaiLieu_Vong8_GopTXT_16-10-2026.txt` (mục lục, sau đó tìm theo mục: [02] TT69, [03] Người Quan Sát, [04] Thời báo TC, [05] VNX, [07] TT139, [09] QĐ 737, [12] TT120, [22] PTIT/TB 7215, [30] FTSE FAQ v1.3, [33] GFCI 40, dòng C4 và C9 của bảng tình trạng); `ho-so/tai-lieu-gop.txt` (Amihud, Mendelson & Lauterbach 1997, bản WP); `reports/doi-chieu-bai-toan-19.md` (bản chép NQ 57 Điều 11–16); `reports/r8-review-B.md` (chỉ để tra DOI và thứ tự tác giả).

**Ràng buộc:** không tra web; không gửi câu chữ đề cương ra ngoài; không chạy script của skill nào. Chỉ dùng `grep`, `sed` và `wc` để tìm và đọc văn bản cục bộ. Mọi chuỗi gốc ở mục (6) đã kiểm bằng `grep -F`: mỗi chuỗi xuất hiện đúng 1 lần trong dump v11.

---

## (2) Tổng hợp

| Mức | Số lượng | Mã |
|---|---|---|
| CRITICAL | 0 | — |
| MAJOR | 1 | MJ1: phân tích tương tác theo mức chịu cú sốc biên độ cần mã UPCoM sau sự kiện, nhưng chính đề cương coi việc UPCoM chuyển sang HOSE trước đó là khả năng chính |
| MINOR | 9 | m1–m9 |

Vòng 11 đã sửa đủ 3 MAJOR và 15/17 MINOR của Agent B vòng 10. Hai mục không áp dụng (m6 Arnold, m12 ngày đăng) có lý do hợp lệ. Mọi câu pháp lý mới đều KHỚP với văn bản gốc. Lỗi MAJOR còn lại không thuộc phần pháp lý. Lỗi này nằm ở chỗ hai đoạn đều do vòng 11 sửa (idx 331 và idx 364) nhưng chưa được đối chiếu với nhau. Sửa bằng hai câu là đủ.

---

## (3) Kiểm các sửa vòng 11

| Mã vòng 10 | Vị trí v11 | Trạng thái | Ghi chú |
|---|---|---|---|
| MJ1 (kênh FTSE không có biến thiên) | idx 330, 345, 364 | **ĐÃ SỬA** | Đổi sang tỷ số vốn hóa tự do chuyển nhượng / giá trị giao dịch; FTSE chỉ dùng để làm sạch nhóm đối chứng. Thuật ngữ còn lệch nhẹ (m6). Còn bỏ ngỏ khả năng mã chuyển sàn vào FTSE ở các kỳ sau (m3). |
| MJ2 (Amihud 1997 ngược chiều) | idx 347 | **ĐÃ SỬA** | Đã chuyển sang trường hợp δ bị đánh giá thấp; mô tả "loại cổ phiếu còn lại của cùng doanh nghiệp cũng tăng giá" KHỚP với nguồn (F-n2). |
| MJ3 (trụ sở Hà Nội nói quá) | idx 334–336 | **ĐÃ SỬA** | Có ba cách đọc kết quả, câu "không đo lượng thanh khoản mà Hà Nội mất", số mã và MDE ghi vào tệp đăng ký. Đúng mức. |
| m1 (VNX, hai ngày tạm ngừng) | idx 101 | ĐÃ SỬA | KHỚP (L-n4) |
| m2 (TT120 Điều 4) | idx 224 | ĐÃ SỬA | KHỚP nguyên văn (L-n1) |
| m3 (nới biên độ "như nhau") | idx 346 | ĐÃ SỬA | — |
| m4 (chu kỳ thanh toán) | idx 346 | ĐÃ SỬA | KHỚP (L-n6) |
| m5 (UPCoM là khả năng chính) | idx 364 | ĐÃ SỬA, nhưng kéo theo MJ1 mới | Xem MJ1 |
| m6 (Arnold) | idx 130 | KHÔNG ÁP DỤNG, lý do hợp lệ | — |
| m7 (GFCI Bảng 26) | idx 342 | ĐÃ SỬA | KHỚP (F-n4) |
| m8 (ghi chú Bảng 2) | idx 223 | ĐÃ SỬA | — |
| m9 ("theo từng kênh") | idx 113 | ĐÃ SỬA ở mục tiêu | Còn sót ở Bảng 4 (idx 397) và idx 332 (m4, m5) |
| m10 (GFCI "không được phép") | idx 363, 433 | ĐÃ SỬA | Năm phương án dự phòng khớp giữa hai chỗ |
| m11 (ngày ký) | idx 609 | ĐÃ SỬA | "… tháng 10 năm 2026"; các mốc "tại ngày 30/9/2026" giữ nguyên, hợp lý |
| m12 (APA Tuổi Trẻ, Thời báo) | idx 541–542 | ĐÃ SỬA MỘT PHẦN, lý do hợp lệ | Tên bài và việc bỏ tên trang đã đúng; ngày đăng chuyển sang mục (8) |
| m13 (4 DOI) | idx 546, 558, 563, 582 | ĐÃ SỬA | Cả 4 DOI KHỚP với hồ sơ (F-n1) |
| m14 (URL, tháng của GFCI và FTSE) | idx 566, 605 | ĐÃ SỬA MỘT PHẦN | GFCI đủ URL và tháng; FTSE có tháng nhưng chưa có URL, dù nhật ký nói đã thêm (m7) |
| m15 (Daw & Hatfield) | idx 561 | ĐÃ SỬA | — |
| m16 (OSF) | idx 85 | ĐÃ SỬA | — |
| m17 (chỉ số dưới) | idx 323–334 | ĐÃ SỬA (theo nhật ký) | Bản dump văn bản không thể hiện định dạng, nhưng "Di·Postt" hiển thị giống idx 324, nên nhất quán |
| Đề xuất NQ 57 số 1 (đơn vị ưu tiên, văn bản) | idx 123 | ĐÃ SỬA | Mốc thời gian của văn bản chưa thống nhất với idx 373 (m9) |
| Đề xuất NQ 57 số 2 (Điều 15.2.e) | idx 525 | ĐÃ SỬA, diễn đạt hẹp hơn văn bản | Xem m1 |
| Đề xuất NQ 57 số 3 (khuôn mẫu cho trái phiếu và phái sinh) | idx 526 | ĐÃ SỬA (ở hướng nghiên cứu) | Đúng mức |

---

## (4) Bảng đối chiếu pháp lý và số liệu (chỉ mục mới hoặc đổi trạng thái)

### 4a. Pháp lý (vn-legal-verify)

Bậc nguồn: 1 = bản chính thức hoặc ký số; 2 = toàn văn đăng lại; 3 = OCR hoặc bản chép từ ảnh quét; 5 = báo chí.

| # | Khẳng định (idx) | Văn bản & điều khoản | Bậc | Trạng thái | Trích nguyên văn nguồn |
|---|---|---|---|---|---|
| L-n1 | "theo Điều 4 Thông tư số 120/2020/TT-BTC, biên độ do Sở Giao dịch Chứng khoán Việt Nam quyết định sau khi Ủy ban Chứng khoán Nhà nước chấp thuận, và Ủy ban Chứng khoán Nhà nước có thể điều chỉnh biên độ khi cần ổn định thị trường" (224) | TT120 Điều 4 khoản 1, 2 | 2 | **KHỚP** (trước đây KHỚP MỘT PHẦN) | "1. Sở giao dịch chứng khoán Việt Nam quyết định biên độ dao động giá sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận. 2. Trong trường hợp cần thiết để ổn định thị trường, Ủy ban Chứng khoán Nhà nước quyết định điều chỉnh biên độ dao động giá…". Nhãn [CẦN XÁC MINH các lần thay đổi biên độ trong giai đoạn 2009–2025] vẫn cần, vì TT120 chỉ có hiệu lực từ năm 2021. |
| L-n2 | "Theo văn bản hiện hành, cổ phiếu UPCoM phải được chuyển sang HOSE chậm nhất đến hết ngày 31/12/2026 (Bộ Tài chính, 2023), nên đề tài coi trường hợp sau là khả năng chính" (364) | TT69 Điều 1, điểm e khoản 2 và điểm e khoản 3 Điều 4 TT57 (qua VBHN 19); TT139 không sửa | 3 | **KHỚP** (pháp lý). **SUY DIỄN chưa đi hết** (thiết kế, xem MJ1) | TT69: "e) Chậm nhất đến hết ngày 31 tháng 12 năm 2026: Sở Giao dịch Chứng khoán Hà Nội hoàn thành việc chuyển cổ phiếu của tổ chức đăng ký giao dịch từ Sở Giao dịch Chứng khoán Hà Nội sang Sở Giao dịch Chứng khoán thành phố Hồ Chí Minh." TT139 (ghi chú hồ sơ): "Chỉ sửa điểm đ khoản 2 và điểm d khoản 3 Điều 4 …, không sửa điểm e (UPCoM)". Lưu ý thêm: TT69 sửa khoản 1 Điều 4 thành "HOSE thống nhất tổ chức … thị trường giao dịch cổ phiếu của tổ chức đăng ký giao dịch", tức là sau khi chuyển, UPCoM vẫn là một thị trường riêng nhưng do HOSE tổ chức. Đề cương chưa tận dụng điểm này (MJ1). |
| L-n3 | "Thí sinh sẵn sàng thực hiện nghĩa vụ tại điểm e khoản 2 Điều 15 Nghị quyết số 57/2026/NQ-HĐND: tham gia mạng lưới chuyên gia của Thành phố và cung cấp luận cứ khoa học cho bài toán số 19 khi được mời" (525) | NQ 57 Điều 15.2.e; Điều 16.1.c | 3 | **KHỚP MỘT PHẦN** | "e) Tham gia mạng lưới chuyên gia khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số của thành phố Hà Nội sau khi hoàn thành chương trình đào tạo; tham gia tư vấn, phản biện, cung cấp luận cứ khoa học hỗ trợ chuyên môn đối với bài toán lớn, chương trình, nhiệm vụ … của Thành phố khi được cơ quan có thẩm quyền mời hoặc giao nhiệm vụ phù hợp với chuyên môn." Điều 16.1.c buộc bồi hoàn toàn bộ nếu "không thực hiện nghĩa vụ quy định tại điểm e khoản 2 Điều 15". Câu của đề cương thu hẹp nghĩa vụ về bài toán số 19 và viết như một lựa chọn ("sẵn sàng"), trong khi đây là nghĩa vụ bắt buộc. Xem m1. |
| L-n4 | "Thông báo của VNX chỉ áp dụng cho cổ phiếu niêm yết và nêu rõ trong hai ngày tạm ngừng, giao dịch tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành" (101) | Thông báo VNX ngày 30/9/2026 | 1 | **KHỚP** (trước đây KHỚP MỘT PHẦN) | Tiêu đề: "Sắp xếp lại thị trường giao dịch cổ phiếu niêm yết …"; "Tạm ngừng giao dịch trong 02 ngày 24/12/2026 và 25/12/2026 đối với các cổ phiếu niêm yết tại HNX thuộc phạm vi chuyển giao. Giao dịch chứng khoán tại HOSE và giao dịch chứng khoán tại các thị trường khác do HNX tổ chức vẫn thực hiện theo quy định hiện hành." |
| L-n5 | Danh sách FTSE "lập với dữ liệu đến ngày 30/6/2026, chỉ gồm mã niêm yết tại HOSE" (330) | FTSE FAQ v1.3, câu hỏi 6 và 13 | 1 | **KHỚP**, còn một điểm chưa xét | Q6: "passed the FTSE GEIS index eligibility screen … based on data cut-off as of 30 June 2026"; cột sàn của cả 27 mã đều là "HSX". Q13: "Newly eligible stocks … assessed at a subsequent quarterly or semi‑annual review, will be added to FTSE GEIS using the same tranching factor". Mã chuyển sàn có thể được xét ở các kỳ sau ngày 28/12/2026. Xem m3. |
| L-n6 | "Bộ Tài chính đặt vấn đề nghiên cứu rút ngắn chu kỳ thanh toán" (346) | Thời báo TC, họp báo ngày 6/10/2026 | 5 | **KHỚP** | "Thứ trưởng cũng đặt vấn đề nghiên cứu khả năng giao dịch xuyên trưa và rút ngắn chu kỳ thanh toán từ T+2 xuống mức thấp hơn" (Thứ trưởng Bộ Tài chính Nguyễn Đức Chi) |
| L-n7 | VN-Index "gồm toàn bộ cổ phiếu niêm yết trên HOSE và tự động cập nhật danh mục sau ngày giao dịch đầu tiên của cổ phiếu niêm yết mới"; "các mã chuyển sàn nhiều khả năng vào chỉ số từ phiên thứ hai" (344) | QĐ 737/QĐ-SGDHCM (OCR) | 3 | KHỚP (nội dung); phần áp cho mã chuyển sàn là SUY DIỄN đã gắn nhãn | "của tất cả cổ phiều niêm yết và giao dịch trên HOSE"; "Danh mục cổ phiếu thành phần của chỉ số được tự động cập nhật sau ngày giao dịch đầu tiên của cổ phiếu niêm yết mới". Không đổi so với vòng 10. |
| L-n8 | NQ 57 Điều 12.3: hỗ trợ công bố WoS Q1/Q2 (122, 413) | NQ 57 Điều 12.3.a–b | 3 | **KHỚP MỘT PHẦN** | "… cho 01 công trình khoa học phục vụ giải quyết bài toán lớn của Thành phố nếu người học là tác giả chính được đăng trên tạp chí khoa học hạng Q2 [Q1] thuộc cơ sở dữ liệu Web of Science". Đề cương không nêu điều kiện "tác giả chính". Xem m2. |

**Chuỗi sửa đổi (không đổi so với vòng 10):** TT57/2021 → TT69/2023 (UPCoM chậm nhất 31/12/2026; HOSE thống nhất tổ chức cả thị trường niêm yết lẫn thị trường đăng ký giao dịch) → VBHN 19/VBHN-BTC (25/12/2023) → TT139/2025 (chỉ sửa điểm đ khoản 2 và điểm d khoản 3, đưa hạn chuyển cổ phiếu niêm yết đến 31/12/2026) → Thông báo VNX 30/9/2026 (áp dụng cho cổ phiếu niêm yết). Hệ quả cho thiết kế: theo văn bản hiện hành, cổ phiếu UPCoM phải rời HNX trong vòng 3 ngày sau ngày 28/12/2026. Nếu không có lần lùi nào khác, nhóm đối chứng UPCoM "do HNX vận hành" không có tháng nào sau sự kiện.

### 4b. Số liệu, DOI và mô tả văn liệu (fact-checker)

| # | Khẳng định (idx) | Kết luận | Căn cứ |
|---|---|---|---|
| F-n1 | 4 DOI mới: Amihud và cộng sự 1997 `10.1016/S0304-405X(97)00021-4`; Corwin & Schultz `10.1111/j.1540-6261.2012.01729.x`; Eichengreen & Shah `10.1111/roie.12441`; Lai `10.1177/0042098011408143` (546, 558, 563, 582) | **TRUE** (cả 4 có trong hồ sơ) | Hồ sơ C4: "DOI 10.1016/S0304-405X(97)00021-4, JFE 45(3) 365–390"; mục [40]: "JF 2012, 67(2) 719–760, DOI 10.1111/j.1540-6261.2012.01729.x"; C9: "(RIE 28, 62–81, DOI 10.1111/roie.12441)", "Lai 2012 (Urban Studies 49(6) 1275–1296, DOI 10.1177/0042098011408143)" |
| F-n2 | Amihud và cộng sự (1997): khi một loại cổ phiếu chuyển sang cơ chế tốt hơn, loại còn lại của cùng doanh nghiệp cũng tăng giá; lan tỏa dương (347) | **TRUE** | "twin stocks where the primary stock … was transferred to the V-Method, while the secondary stock continued to be traded"; "the price of the secondary stock should increase upon the transfer announcement of the primary stock"; "improvement in the trading mechanism for security A will have a positive effect on the liquidity of B" |
| F-n3 | Coval & Moskowitz (1999): "nhà quản lý quỹ ưa nắm giữ cổ phiếu của doanh nghiệp có trụ sở gần mình"; Loughran & Schultz (2005): thanh khoản phụ thuộc vị trí trụ sở (334) | **UNVERIFIABLE** trong hồ sơ (cả hai bài không có trong hồ sơ) | Nhãn [CẦN ĐỐI CHIẾU bản gốc của hai bài] đặt đúng chỗ. Cách diễn đạt mới hợp với tên bài "Local equity preference in domestic portfolios" và "Urban versus rural firms". Không phải lỗi. |
| F-n4 | GFCI 40 Bảng 26: 3 nhân tố lấy từ WFE, "cùng bảng với nhân tố mức chỉ số cổ phiếu" (342) | **TRUE** | Table 26: "Capitalisation Of Stock Exchanges / The World Federation of Stock Exchanges / Value Of Share Trading / Volume Of Share Trading / Broad Stock Index Levels / Value Of Bond Trading …". Bản chữ không cho biết nguồn từng dòng sau dòng đầu; câu của đề cương đã viết đúng mức. |
| F-n5 | Thứ tự tác giả "Eichengreen, B., & Shah, N. (2020)" (563; trích ở 107, 115, 125) | **MIXED** (hai nguồn thứ cấp trong hồ sơ nói khác nhau) | Bảng tình trạng hồ sơ C9 ghi "Shah & Eichengreen 2020 (RIE 28, 62–81 …)"; danh mục của Naeem (2023) theo vòng 8 và vòng 10 ghi "Eichengreen, B., & Shah …". Cần xem trang bài trên tạp chí. Xem m8. |
| F-n6 | FTSE FAQ v1.3, tháng 8/2026 (566) | **TRUE** | "Reclassification of Vietnam from Frontier to Secondary Emerging Market Status - FAQ, v1.3, August 2026"; URL nguồn: https://www.lseg.com/content/dam/ftse-russell/en_us/documents/policy-documents/ftse-faq-document-vietnam-reclassification.pdf |
| F-n7 | GFCI 40, tháng 9/2026, URL (605) | **TRUE** | "Nguồn: https://www.longfinance.net/media/documents/GFCI_40_Report_2026.09.16_v1.2.pdf"; "September 2026" |
| F-n8 | MDE: mức một phía 0,05/3 (358) và giá trị p một phía đưa vào Holm (360) | **TRUE** (nhất quán nội bộ) | Các con số không đổi so với vòng 10 (F23 đã tự tính lại) |

**Claim record cập nhật (credible-claims):**

| Khẳng định | Căn cứ | Phần chưa giải | Ngôn ngữ được phép |
|---|---|---|---|
| H1 | Dữ liệu bảng GFCI, hiệu ứng cố định, phân cụm theo quốc gia | Trùng lặp cơ học với nhân tố WFE (đã nêu ở idx 361); quyền dùng dữ liệu | "liên hệ có điều kiện" (đúng mức) |
| H2 | Bootstrap khối dừng | Biên độ và bước giá (đã có nhãn) | "thấp hơn", có điều kiện (đúng mức) |
| H3 | Khác biệt kép trên một sự kiện, bootstrap tự hồi quy | Nhóm đối chứng UPCoM nhiều khả năng không có dữ liệu sau sự kiện; ước lượng chính chỉ còn dựa vào nhóm HOSE | "tác động gộp của sàn" (đúng mức) |
| Tương tác theo mức chịu cú sốc | Đo trước 30/6/2025; suy luận giống δ | **Kênh biên độ có thể không ước lượng được nếu UPCoM chuyển đi (MJ1)**; mã chuyển sàn có thể vào FTSE ở các kỳ sau (m3) | "khác biệt của tác động theo mức chịu cú sốc"; idx 332 và Bảng 4 còn dùng "theo từng kênh" và "Tác động theo …" (m4, m5) |
| Tương tác theo trụ sở Hà Nội | Tương tác với biến trụ sở; ba cách đọc kết quả | Cần biết số mã và MDE (đã cam kết ghi vào tệp đăng ký) | Đúng mức sau vòng 11 |
| Khớp với NQ 57 Điều 15.2.e | idx 525 | Thu hẹp và làm mềm nghĩa vụ (m1) | Diễn đạt sát văn bản |

Câu mới không nói quá: idx 336 ("không đo lượng thanh khoản mà thị trường vốn Hà Nội mất") và idx 330 (FTSE "không được coi là một kênh") đều đúng mức với nguồn. Có một ngoại lệ ở m3.

---

## (5) Bảng độ khớp và kết luận (research-grants)

| Yêu cầu | Nguồn (trích) | Vị trí trong đề cương v11 | Đánh giá v11 (so với v10) |
|---|---|---|---|
| Tập trung toàn thời gian; nội dung phục vụ bài toán lớn (Điều 11.3) | "tập trung toàn thời gian, có chuyên ngành đào tạo và nội dung nghiên cứu của luận án tiến sĩ phục vụ giải quyết bài toán lớn của Thành phố" | idx 521, 95, 108–111, 373 | **KHỚP** (không đổi). Rủi ro thực tế do đang học song song vẫn còn; cam kết ở idx 521 đúng mức. |
| Công bố WoS Q1/Q2, tác giả chính (Điều 12.3) | "nếu người học là tác giả chính được đăng trên tạp chí khoa học hạng Q2 [Q1] thuộc cơ sở dữ liệu Web of Science" | idx 122, 413 | **KHỚP MỘT PHẦN**: chưa nêu "tác giả chính" (m2) |
| Hội thảo (Điều 12.2) | "tác giả chính (tác giả đầu tiên hoặc tác giả liên hệ) của báo cáo phục vụ giải quyết bài toán lớn" | idx 122, 413 ("một đến hai báo cáo hội thảo") | KHỚP (chưa cần sửa) |
| ≤ 48 tháng (Điều 13) | "không vượt quá 48 tháng" | idx 415 | **KHỚP** |
| Nghĩa vụ sau tốt nghiệp (Điều 15.2.e) | Trích ở L-n3 | idx 525 | **CHƯA KHỚP → KHỚP MỘT PHẦN** (đã có câu; nên diễn đạt sát văn bản, m1) |
| Điều chỉnh đề tài vẫn phải phục vụ bài toán lớn (Điều 15.1.b) | "phải phục vụ giải quyết bài toán lớn của Thành phố để được tiếp tục nhận hỗ trợ" | idx 363–364 (phương án dự phòng) | KHỚP: các phương án dự phòng không làm đề tài rời bài toán 19 |
| TB 7215: "mục tiêu, tính mới, tính khả thi, sản phẩm dự kiến và khả năng ứng dụng, chuyển giao hoặc phục vụ công tác hoạch định chính sách" | PTIT tóm tắt TB 7215 | idx 112–123, 115, 356–365, 116, 373 | **KHỚP** |
| Đơn vị tiếp nhận, văn bản xác nhận | TB 7215 (Dân trí): "văn bản cam kết phối hợp, tiếp nhận …" | idx 123 (ưu tiên HNX), 373 | **KHỚP MỘT PHẦN → KHỚP** về cam kết; chưa có văn bản thật; mốc xin văn bản cần thống nhất (m9) |
| Bài toán 19, câu hỏi 1 và 3 | QĐ 1193 Phụ lục | idx 95, 109–111, 373 | **KHỚP MỘT PHẦN**, tự khai đúng mức (không đổi) |
| Câu hỏi 2 và 4 | QĐ 1193 | idx 373 | **CHƯA KHỚP**, đã khai rõ ngoài phạm vi (không đổi) |
| Sản phẩm "Hệ thống dữ liệu tài chính đô thị", "Trung tâm tài chính quốc tế tại Hà Nội" | QĐ 1193 | idx 116 | **KHỚP MỘT PHẦN**, cách viết đúng mức |
| Phần "Hà Nội" của chỉ số sau 2026 | — | idx 242, 350, 526 | **KHỚP MỘT PHẦN**: sau năm 2026 chỉ số đo HOSE; hướng mở rộng sang trái phiếu và phái sinh của HNX nằm ở mục 9, đúng mức |
| Danh mục dùng để xét chọn (QĐ 1193 hay danh mục theo Điều 35) | — | idx 95, 543 | **CHƯA RÕ** [CẦN XÁC MINH với cơ quan quản lý]; đề cương không quyết định được |

**Kết luận (không nói quá).** So với v10, độ khớp tăng ở ba điểm có kiểm chứng: (i) chỉ tiêu (6) đã nêu đơn vị ưu tiên (HNX) và yêu cầu văn bản xác nhận; (ii) mục 9 đã nhắc nghĩa vụ ở Điều 15.2.e; (iii) phân tích theo trụ sở Hà Nội đã được diễn giải đúng mức, nên không còn rủi ro hội đồng cho là nói quá. Đề cương đáp ứng mọi yêu cầu hình thức của TB 7215 và các điều kiện ở Điều 11.3 và Điều 13. Về nội dung, đề tài vẫn chỉ góp phần **một phần** vào câu hỏi 1 và 3 của bài toán 19, và tự khai như vậy là đúng. Chưa có văn bản xác nhận thật; đây là việc ngoài đề cương.

**Đề xuất tăng độ khớp mà không nói quá:**
1. Viết lại câu Điều 15.2.e cho sát văn bản và bỏ chữ "sẵn sàng" (m1).
2. Thêm "với thí sinh là tác giả chính" vào chỉ tiêu (5) và mục 7.3 (m2), để chỉ tiêu trùng với điều kiện hỗ trợ ở Điều 12.3.
3. Thống nhất một mốc xin văn bản xác nhận: trước khi nộp hồ sơ, ưu tiên HNX (m9).
4. Không thêm cấu phần FinTech hay nền tảng công nghệ. Mở rộng như vậy sẽ thuộc nhóm lỗi "Overly Ambitious" trong 48 tháng.

---

## (6) Phát hiện theo mức

### CRITICAL
Không có.

### MAJOR

**MJ1. Phân tích tương tác theo mức chịu cú sốc biên độ dựa vào mã UPCoM sau sự kiện, trong khi đề cương coi việc UPCoM rời HNX trước khi có dữ liệu sau sự kiện là khả năng chính.**
- idx: 331 (kéo theo 325, 347, 364). Skill: vn-legal-verify, consistency-checker, credible-claims.
- Căn cứ:
  - idx 331 ước lượng các số hạng Es,i·τt "trên những mã đối chứng đo được cùng thước đo, tức mã UPCoM với mức chịu cú sốc biên độ". Mã HOSE không đo được tỷ lệ ngày có lợi suất tuyệt đối từ 7% đến dưới 10%, vì HOSE có biên độ ±7%.
  - idx 364 nói UPCoM "phải được chuyển sang HOSE chậm nhất đến hết ngày 31/12/2026", là "khả năng chính", và khi đó "nhóm đối chứng UPCoM chỉ được dùng đến tháng liền trước ngày chuyển của UPCoM".
  - TT69 (L-n2): "e) Chậm nhất đến hết ngày 31 tháng 12 năm 2026: Sở Giao dịch Chứng khoán Hà Nội hoàn thành việc chuyển cổ phiếu của tổ chức đăng ký giao dịch …". Như vậy, nếu hạn không bị lùi, không có tháng UPCoM nào sau tháng 1/2027. Khi đó hiệu ứng theo tháng của mức chịu cú sốc biên độ trong giai đoạn sau không ước lượng được, nên hệ số tương tác của kênh biên độ không nhận dạng được. Đây là cùng loại lỗi với MJ1 vòng 10 (một kênh của mục tiêu (iii) không có biến thiên hay không có đối chứng).
  - Câu "trong 24 tháng sau sự kiện" ở idx 364 cũng chỉ đúng khi hạn 31/12/2026 được lùi tiếp.
  - TT69 sửa khoản 1 Điều 4 thành HOSE "thống nhất tổ chức … thị trường giao dịch cổ phiếu của tổ chức đăng ký giao dịch". Nghĩa là sau khi chuyển, mã UPCoM vẫn thuộc một thị trường riêng do HOSE tổ chức. Nếu thị trường này giữ biên độ riêng, mã UPCoM vẫn có thể làm đối chứng cho kênh biên độ.
- Sửa (ba thay thế):
  - "tức mã UPCoM với mức chịu cú sốc biên độ và mã HOSE với hai mức còn lại." → "tức mã UPCoM với mức chịu cú sốc biên độ và mã HOSE với hai mức còn lại. Nếu cổ phiếu UPCoM rời HNX trước khi có dữ liệu sau sự kiện, khả năng chính nêu ở mục 4.3.10, thì sau khi chuyển, các mã này vẫn được dùng làm đối chứng cho mức chịu cú sốc biên độ nếu thị trường giao dịch cổ phiếu đăng ký giao dịch do HOSE tổ chức giữ biên độ riêng, và ngày chuyển được ghi là một cú sốc trùng thời gian [CẦN XÁC MINH quy chế giao dịch cổ phiếu đăng ký giao dịch tại HOSE]. Nếu không, số hạng hiệu ứng theo tháng riêng của mức chịu cú sốc biên độ được bỏ, hệ số tương tác của kênh này được báo cáo ở dạng mô tả, và các mã đã tự chuyển từ HNX sang HOSE trước năm 2026 là phép kiểm tra chính cho kênh biên độ."
  - "nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt hoặc trong 24 tháng sau sự kiện," → "nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt, hoặc trong 24 tháng sau sự kiện khi mốc ngày 31/12/2026 được lùi tiếp,"
  - "nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác." → "nên ước lượng với nhóm đối chứng UPCoM, nếu nhóm này còn dữ liệu sau sự kiện, được trình bày như một cận khác."

### MINOR

| Mã | idx | Skill | Căn cứ | Chuỗi gốc → chuỗi thay thế |
|---|---|---|---|---|
| m1 | 525 | vn-legal-verify, research-grants | L-n3: Điều 15.2.e là nghĩa vụ bắt buộc (Điều 16.1.c buộc bồi hoàn), phạm vi rộng hơn bài toán 19, kích hoạt "khi được cơ quan có thẩm quyền mời hoặc giao nhiệm vụ" | "Thí sinh sẵn sàng thực hiện nghĩa vụ tại điểm e khoản 2 Điều 15 Nghị quyết số 57/2026/NQ-HĐND: tham gia mạng lưới chuyên gia của Thành phố và cung cấp luận cứ khoa học cho bài toán số 19 khi được mời" → "Thí sinh cam kết thực hiện nghĩa vụ tại điểm e khoản 2 Điều 15 Nghị quyết số 57/2026/NQ-HĐND: sau khi hoàn thành chương trình đào tạo, tham gia mạng lưới chuyên gia khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số của Thành phố, và tham gia tư vấn, phản biện, cung cấp luận cứ khoa học cho bài toán số 19 và các nhiệm vụ khác phù hợp với chuyên môn khi được cơ quan có thẩm quyền mời hoặc giao nhiệm vụ" |
| m2 | 122, 413 | research-grants | L-n8: Điều 12.3 chỉ hỗ trợ khi "người học là tác giả chính" | "với mục tiêu ít nhất một bài thuộc cơ sở dữ liệu Web of Science hạng Q1 hoặc Q2" → "với mục tiêu ít nhất một bài, do thí sinh là tác giả chính, thuộc cơ sở dữ liệu Web of Science hạng Q1 hoặc Q2"; và "Mục tiêu là ít nhất một bài thuộc cơ sở dữ liệu Web of Science hạng Q1 hoặc Q2." → "Mục tiêu là ít nhất một bài, do thí sinh là tác giả chính, thuộc cơ sở dữ liệu Web of Science hạng Q1 hoặc Q2." |
| m3 | 330 | vn-legal-verify, credible-claims | L-n5: FAQ Q13 cho phép mã mới đủ điều kiện được thêm "at a subsequent quarterly or semi‑annual review". Mã chuyển sàn, khi đã thành mã HOSE, có thể vào FTSE trong cửa sổ sau. Đó là cú sốc trùng thời gian lên chính nhóm xử lý. | "chỉ được dùng để loại mã khỏi nhóm đối chứng HOSE ở mục 4.3.8." → "chỉ được dùng để loại mã khỏi nhóm đối chứng HOSE ở mục 4.3.8; nếu mã chuyển sàn nào được FTSE Russell đưa vào chỉ số ở các kỳ xét duyệt sau ngày 28/12/2026, ngày đó được ghi lại và δ được ước lượng thêm khi loại các mã này [CẦN XÁC MINH phạm vi sàn mà FTSE Russell sàng lọc trước ngày chuyển sàn]." |
| m4 | 397 (Bảng 4) | consistency-checker | Nhật ký vòng 11 nói Bảng 4 đã dùng "khác biệt theo mức chịu cú sốc", nhưng Bảng 4 chưa đổi; mục tiêu (idx 113) đã đổi | "6.1.1 Tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số" → "6.1.1 Khác biệt của tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số" |
| m5 | 332 | credible-claims | Chính câu này nói hệ số "không đo riêng tác động của từng quy tắc"; nên nói "theo mức chịu cú sốc" như idx 113 | "Hệ số tương tác cho biết tác động thay đổi thế nào theo từng kênh," → "Hệ số tương tác cho biết tác động thay đổi thế nào theo mức chịu cú sốc của từng kênh," |
| m6 | 345 | consistency-checker | idx 330 gọi là "danh sách cổ phiếu đủ điều kiện"; idx 345 gọi là "danh sách dự kiến" | "loại các mã thuộc danh sách dự kiến của FTSE Russell" → "loại các mã thuộc danh sách cổ phiếu đủ điều kiện của FTSE Russell" |
| m7 | 566 | citation-management | F-n6: hồ sơ có URL chính thức; nhật ký vòng 11 nói đã thêm URL cho FTSE | "(Version 1.3). LSEG." → "(Version 1.3). LSEG. https://www.lseg.com/content/dam/ftse-russell/en_us/documents/policy-documents/ftse-faq-document-vietnam-reclassification.pdf" |
| m8 | 563 | fact-checker, citation-management | F-n5: hai nguồn thứ cấp trong hồ sơ ghi thứ tự tác giả khác nhau | "https://doi.org/10.1111/roie.12441" → "https://doi.org/10.1111/roie.12441 [CẦN XÁC MINH thứ tự tác giả trên trang bài của tạp chí]" (nếu tạp chí ghi Shah đứng đầu, sửa cả 4 chỗ trích ở idx 107, 115, 125 và danh mục) |
| m9 | 373 so với 123 | consistency-checker, research-grants | Chỉ tiêu (6) gắn văn bản xác nhận với báo cáo năm thứ tư; idx 373 nói xin văn bản trước khi nộp hồ sơ. Hai mốc nên được nối với nhau. | "xin văn bản xác nhận nhu cầu sử dụng kết quả của ít nhất một đơn vị trong số này." → "xin văn bản xác nhận nhu cầu sử dụng kết quả của ít nhất một đơn vị trong số này, ưu tiên HNX; văn bản này cũng là căn cứ của chỉ tiêu (6)." |

**Kiểm tra nhất quán (consistency-checker), các mục không thấy lỗi:**
- Mục lục (idx 19–47), danh mục Bảng 1–7 (50–56) và Hình 1–3 (59–61) khớp với tiêu đề trong thân bài (134, 207, 245, 376, 416, 437, 456; 204, 319, 354).
- Dẫn chiếu mục: "cuối mục 4.2" (107 → 151), "mục 4.1" (133, 406), "mục 4.3.10" (230, 335, 433), "mục 4.3.8" (330, 336, 372), "mục 4.3.7" (349, 357) đều trỏ đúng chỗ. "Cuối mục 4.3.8" (336) trỏ tới đoạn "Từ bằng chứng đến định hướng cho Hà Nội" (349), đúng.
- Phương trình (1)–(7) và các dẫn chiếu "(5)–(7)", "(5)", "(6)", "(1)" đúng.
- Bảng chữ viết tắt: mọi chữ viết tắt dùng trong thân bài đều có trong bảng hoặc được giải nghĩa ngay tại chỗ (VSTEP, VN-Index). ISSN, DOI, ESG, CAPM, ABC-MCMC chỉ xuất hiện trong tên bài hoặc thông tin tạp chí, chấp nhận được.
- Mốc thời gian: 6/2009, 30/6/2025, 7/2025–12/2026, 23–28/12/2026, 1/2027, 24 tháng, 7/2023–6/2025, 1/2024–12/2028, Q3/2020–Q2/2025, Q1/2027–Q4/2028 thống nhất trong toàn bài.
- Holm: họ H1–H3, mức 5%, giá trị p một phía (360), mức 0,05/3 một phía khi tính MDE (358), các phân tích tương tác không vào Holm (223, 333). Nhất quán.
- Năm phương án dự phòng: idx 363–364 khớp với idx 433.
- Trích dẫn hai chiều: đã `grep` 70 tác giả hoặc cơ quan trong danh mục trên idx 0–530. Mục nào cũng được trích ít nhất 1 lần. Arnold và cộng sự (1999) chỉ được trích gián tiếp nên không vào danh mục là đúng.
- Thứ tự danh mục theo APA 7: tiếng Việt (Bộ Tài chính 2020 → 2023 → 2025 → Hội đồng → Nguyễn → Quốc hội → Sở … Thành phố → Sở … Việt Nam → Thời báo → Tuổi Trẻ → Ủy ban) và tiếng Anh (Amihud 2002 trước Amihud và cộng sự 1997; Christie → Čihák → Conley → Corwin → Coval; Hoang → Holm → Hou → Huang; Ledoit 2004 → 2008; Lesmond 2005 → Lesmond và cộng sự 1999) đều đúng.
- Ngày ký: "Hà Nội, ngày … tháng 10 năm 2026" (609). Các mốc "tại ngày 30/9/2026" ở Bảng 6, Bảng 7 và idx 151 vẫn hợp lý vì là ngày chốt số liệu.

**APA 7 (citation-management, chỉ đọc SKILL.md):** ngoài m7 và m8, các mục báo chí đã đúng dạng. Còn thiếu ngày đăng (đưa vào mục 8). Gehrig (2000) thiếu trang và Daw & Hatfield (2018) thiếu tập, số, trang; cả hai đã có nhãn. SKILL.md ghi "NEVER leave an @article entry without volume, pages, and DOI". Khoảng 40 bài tạp chí còn thiếu DOI. Đây là việc nên làm trước khi nộp, nhưng không tính là lỗi, vì APA 7 chỉ yêu cầu DOI khi có, và hồ sơ hiện không chứa các DOI này.

---

## (7) Câu hỏi hội đồng (peer-review)

**Nhận xét tổng thể (bản nháp làm việc).**

*Điểm mạnh:*
- Phần pháp lý đã đối chiếu tới câu chữ của TT57, TT69, TT139, TT120, thông báo VNX và NQ 57.
- Thiết kế được viết cho đúng một sự kiện có ngày xác định.
- Có đăng ký trước, có tính MDE trung thực, có quy tắc gọi kết quả là chưa đủ cơ sở kết luận.
- Phần Hà Nội nay được diễn giải đúng mức.

*Điểm yếu còn lại:*
1. Nhóm đối chứng UPCoM, và cùng với nó là kênh biên độ, phụ thuộc vào việc hạn 31/12/2026 có bị lùi hay không (MJ1).
2. Toàn bộ ước lượng chính dựa vào nhóm đối chứng HOSE, nhóm cùng lúc chịu nhiều cú sốc: FTSE, phân bảng, có thêm 299 mã.
3. Đóng góp cho bài toán 19 là thước đo nền, không phải giải pháp. Đề cương đã tự nói vậy.

| # | Câu hỏi khó | Gợi ý trả lời ngắn |
|---|---|---|
| 1 | Theo TT69, UPCoM phải rời HNX chậm nhất ngày 31/12/2026, tức 3 ngày sau sự kiện. Vậy kênh biên độ ước lượng bằng gì? | Nếu thị trường đăng ký giao dịch tại HOSE giữ biên độ riêng, vẫn dùng mã UPCoM sau khi chuyển, có ghi cú sốc trùng thời gian. Nếu không, báo cáo kênh này ở dạng mô tả và dùng các mã đã tự chuyển sàn trước năm 2026 (MJ1). |
| 2 | Nhóm đối chứng HOSE cùng lúc chịu FTSE, phân bảng và việc tiếp nhận 299 mã. Vì sao vẫn tin δ? | Loại mã FTSE; thêm biến chỉ nhóm bảng; báo cáo xu hướng riêng của từng nhóm; hai chiều lan tỏa đã nêu (idx 344–347). Kết luận được giới hạn ở "tác động gộp của sàn". |
| 3 | Nếu một số mã chuyển sàn vào FTSE trong năm 2027 thì sao? | Ghi ngày, ước lượng lại khi loại các mã này (m3). |
| 4 | MDE khoảng 22% với φ = 0,6. Đề tài có đủ công suất không? | Con số này là minh họa. Giá trị thật sẽ ước lượng trên dữ liệu tham chiếu và ghi vào tệp đăng ký trước ngày 28/12/2026. Nếu khoảng tin cậy rộng, kết quả được gọi là chưa đủ cơ sở kết luận (idx 362). |
| 5 | Luận án giúp gì cho câu hỏi "phương thức xây dựng Hà Nội thành trung tâm tài chính"? | Chỉ một phần: thước đo nền và bằng chứng về vai trò của sàn cho câu hỏi 1 và 3; phần định hướng chuyên môn hóa là tổng hợp định tính (idx 95, 373). |
| 6 | Thí sinh đang học song song ba chương trình. Cam kết toàn thời gian có thực hiện được không? | Cam kết hoàn thành, bảo lưu hoặc dừng trước khi nhập học (idx 521). Hội đồng có thể yêu cầu minh chứng. |
| 7 | Đề tài có phải nghĩa vụ ở Điều 15.2.e chỉ gồm bài toán 19 không? | Không. Nghĩa vụ bao gồm mọi nhiệm vụ phù hợp chuyên môn khi được mời hoặc giao (m1). |
| 8 | Danh mục bài toán lớn dùng để xét chọn là QĐ 1193 hay một danh mục mới? | Chưa rõ; cần hỏi Sở KH&CN. |
| 9 | Đồng tác giả trong các bài liên quan là ai, và luận án khác bài Nguyễn & Nguyễn (2026a) ở đâu? | M5 được xử lý như mọi mô hình khác, báo cáo cả khi có và khi không có M5; phạm vi sàn của các bài trước được khai trong tệp đăng ký (idx 271–272). |

---

## (8) Tài liệu cần tìm mới

| Tên tài liệu | Cơ quan / năm | Vì sao cần (mã) | Dùng ở đâu | Cần phần nào | Nơi tìm hợp pháp | Từ khóa | Ưu tiên |
|---|---|---|---|---|---|---|---|
| Quy chế giao dịch (hoặc dự thảo) cho cổ phiếu đăng ký giao dịch tại HOSE sau khi nhận từ HNX; kế hoạch chuyển UPCoM theo khoản 4 Điều 4 TT57 | VNX / HOSE / UBCKNN, 2026 | MJ1 | idx 101, 331, 364 | Biên độ, hệ thống giao dịch, ngày chuyển | vnx.vn, hsx.vn, ssc.gov.vn | "chuyển cổ phiếu đăng ký giao dịch sang HOSE", "UPCoM HOSE 2026 biên độ" | Cao |
| Trang bài Eichengreen & Shah (2020) trên Review of International Economics | Wiley, 2020 | m8 | idx 107, 115, 125, 563 | Thứ tự tác giả | onlinelibrary.wiley.com qua DOI 10.1111/roie.12441 | "correlates of international financial-center status" | Trung bình |
| FTSE GEIS Ground Rules, mục 6 (các bước sàng lọc), và phạm vi sàn Việt Nam được sàng lọc | FTSE Russell / LSEG, 2026 | m3 | idx 330, 345 | Sàn đủ điều kiện, kỳ xét duyệt sau | lseg.com/ftse-russell | "FTSE GEIS ground rules eligible exchanges Vietnam" | Trung bình |
| Bản giấy NQ 57/2026/NQ-HĐND, Điều 12, 15, 16 (soát bản chép) | HĐND TP Hà Nội, 2026 | m1, m2 | idx 415, 521, 525 | Câu chữ Điều 12.3, 15.2.e, 16.1.c | Công báo Hà Nội, cổng thông tin HĐND | "Nghị quyết 57/2026/NQ-HĐND" | Trung bình |
| Ngày đăng bài Tuổi Trẻ Online và Thời báo TC VN (từ vòng 10) | Báo chí, 10/2026 | APA | idx 541, 542 | Ngày đăng | Trang bài báo | — | Thấp |
| Coval & Moskowitz (1999); Loughran & Schultz (2005), bản gốc (từ vòng 10) | JF; JFE | F-n3 | idx 334 | Tóm tắt, kết quả chính | Thư viện | "Home bias at home"; "Urban versus rural firms" | Thấp |

Quyết định về câu chữ cuối cùng thuộc về thí sinh và người hướng dẫn.
