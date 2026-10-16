# Phản biện vòng 8, Agent B: kiểm chứng pháp lý, số liệu, văn liệu và tính nhất quán

Đề cương: "Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội" (bản v7, `scratchpad/r8/dump-v7.txt`, mỗi dòng một đoạn có idx). Ngày kiểm: 16/10/2026. Người kiểm: Agent B. Agent B không sửa đề cương và chỉ viết báo cáo này.

**Quy ước chuỗi.** Trong dump, ký tự "&" được mã hóa thành "&amp;". Các chuỗi gốc dưới đây ghi "&", tức là đúng ký tự trong tệp docx. Ngoài điểm này, mọi chuỗi gốc được chép nguyên văn từ dump.

---

## (1) Bằng chứng tuân thủ

| Bước | Skill / việc | Đã làm | Bằng chứng |
|---|---|---|---|
| 1 | `vn-legal-verify` | Đã gọi trước tiên. Tôi đã liệt kê các khẳng định pháp lý (bước 1), định danh văn bản (bước 2), dựng chuỗi sửa đổi (bước 3), đối chiếu nguyên văn bằng grep (bước 4), kiểm danh mục (bước 5) và lập danh sách tài liệu cần tìm (bước 6). | Mục (3), bảng A và chuỗi sửa đổi. Đã grep `TONG_HOP_TAI_LIEU_HNX_HOSE.txt`: dòng 22–43 (TT139), 160–225 (TT57 gốc), 360–476 (VBHN19 và chú thích 1–13), 527–563 (NQ222), 2518–2680 (QĐ 737). Đã đọc `qd1193.txt` dòng 28–70 và 855–900. NQ 57 lấy từ bản chép trong `doi-chieu-bai-toan-19.md` mục a.1. |
| 2 | `fact-checker` | Đã gọi. Mỗi khẳng định được xếp hạng theo thang TRUE / MOSTLY TRUE / MIXED / UNVERIFIABLE. | Mục (3), bảng B. Nguồn: Amihud và cộng sự (`tai-lieu-gop.txt` dòng 50–60, 144–147), Hisada (TONG_HOP dòng 2977–3140), Naeem (TONG_HOP dòng 3262–3336, 4184–4192, 4628–4634, 5150–5160, 6545–6568). |
| 3 | `credible-claims` | Đã gọi. Có claim record cho H1–H4 và cho các khẳng định khớp bài toán 19, kèm cờ nói quá. | Mục (4), tiểu mục "Claim record". |
| 4 | `consistency-checker` | Đã gọi ở chế độ checklist, **không chạy script**. Đã kiểm đủ 10 nhóm: đánh số, mục lục, danh mục bảng/hình/chữ viết tắt, phương trình, mốc thời gian, biến, giả thuyết, Holm, phương án dự phòng, trích dẫn hai chiều. | Mục (4), bảng "Checklist nhất quán". Dùng grep để đếm mốc và trích dẫn, không dùng script của skill. |
| 5 | `citation-management` | Chỉ đọc SKILL.md, **không chạy script**, không tra web. Phase 2.5 (tra DOI qua web) bị bỏ qua có chủ đích vì quy tắc cấm tra web. Không DOI nào được thêm từ trí nhớ: DOI chưa có trong hồ sơ được chuyển sang mục (8). | Mục (5). |
| 6 | 20 nhãn [CẦN ...] | Đã làm. | Mục (6). |
| 7 | MJ6 (NQ 57, học tập trung toàn thời gian) | Đã làm. | Mục (7). |
| — | Ràng buộc | Không tra web. Không gửi câu chữ đề cương ra ngoài. Không chạy script. Không sửa đề cương. Không đổi tên đề tài. | — |

**Kiểm các sửa đổi của vòng 7 (r7-review.md).** Các sửa CR1, MJ1–MJ5, MJ7, MJ8 và m1–m8, m10, m11 đã có trong v7 và **khớp nguồn**. Riêng m11 đã thêm Daw và Hatfield (2018) vào danh mục, vẫn mang nhãn. Tôi đã đối chiếu lại từng chỗ:
- idx 79: chuỗi TT57 → TT69 → TT139 và điểm e về UPCoM.
- idx 78: định nghĩa thị trường vốn Hà Nội.
- idx 91 và 273: Naeem dùng thứ hạng GFCI.
- idx 275 và 286: yếu tố cơ học giữa SMD và GFCI.
- idx 270: cửa sổ mẫu của phương trình (5).
- idx 189: mốc thực hiện bị lùi hai lần.
- idx 77, 89, 295: bài toán 19.
- idx 277 và 456: QĐ 737.
- idx 87 và 289: mục tiêu tổng quát và đối tượng nghiên cứu.

Còn hai việc chưa xong. Thứ nhất, **MJ6** chưa đưa vào đề cương, vì phải chờ người dùng quyết; nay người dùng đã quyết, câu đề xuất ở mục (7). Thứ hai, **m9(ii)** về cách viết Nguyen/Nguyễn chưa sửa (xem m11). Vòng này có một phát hiện mới về Hisada (MJ2), vượt ra ngoài phần r7 đã sửa ở m2.

---

## (2) Tổng hợp

**0 CRITICAL, 4 MAJOR, 14 MINOR.**

| Mã | Mức | Tóm tắt |
|---|---|---|
| MJ1 | MAJOR | Đề cương chưa có cam kết học tập trung toàn thời gian và chưa trích NQ 57/2026/NQ-HĐND, trong khi idx 441 kê ba chương trình học song song. Người dùng đã quyết cam kết; câu thay ở mục (7). |
| MJ2 | MAJOR | Hisada (2018) bị mô tả sai đối tượng: mẫu của bài là cổ phiếu sẵn có trên Tokyo, không phải cổ phiếu chuyển từ Osaka sang. |
| MJ3 | MAJOR | Câu nối với bài toán 19 ở idx 77 nói đề tài đo "chất lượng thị trường vốn của Hà Nội". Câu này mâu thuẫn với định nghĩa ở idx 78 và với phạm vi định lượng ở idx 293, nên đang nói quá. |
| MJ4 | MAJOR | H2 là kiểm định xác nhận nhưng chưa được đặc tả thống nhất. Giai đoạn mẫu ghi "2009–2026", trong khi giai đoạn tham chiếu kết thúc 6/2025. Quy tắc quyết định ghi "khoảng tin cậy loại trừ 0", trong khi Holm dùng giá trị p. |
| m1–m14 | MINOR | Xem mục (4). |

---

## (3) Bảng đối chiếu pháp lý và số liệu

### A. Pháp lý (vn-legal-verify)

Bậc nguồn: (1) bản chép từ ảnh văn bản có ký số; (2) trang thư viện văn bản (thuvienphapluat, hethongphapluat, caselaw); (3) OCR không dấu của văn bản Sở giao dịch; (4) bản chép tay từ scan sao y; (5) báo chí.

| # | Khẳng định (idx) | Văn bản và điều khoản | Bậc | Trạng thái | Trích nguyên văn nguồn | Chuỗi thay thế |
|---|---|---|---|---|---|---|
| A1 | TT57 đặt mốc ban đầu: HNX ngừng nhận niêm yết mới từ 01/7/2023 và chuyển cổ phiếu niêm yết trong năm 2023 (79) | TT57 gốc, Điều 4 khoản 3 điểm c, d | 2 | KHỚP | "c) Từ ngày 01 tháng 7 năm 2023: Sở Giao dịch Chứng khoán Hà Nội không tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới của tổ chức;" / "d) Từ ngày 01 tháng 7 năm 2023 đến hết ngày 31 tháng 12 năm 2023: Sở Giao dịch Chứng khoán Hà Nội thực hiện chuyển cổ phiếu của tổ chức niêm yết…" | — |
| A2 | TT69 lùi hai mốc thành 01/7/2025 và hết năm 2025 (79) | VBHN19 Điều 4 khoản 3 điểm c, d; chú thích 9, 10 | 2 | KHỚP | "c)9 Từ ngày 01 tháng 7 năm 2025: Sở Giao dịch Chứng khoán Hà Nội không tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới của tổ chức;" / "d)10 Chậm nhất đến hết ngày 31 tháng 12 năm 2025: …"; "Điểm này được sửa đổi theo quy định tại khoản 3 Điều 1 Thông tư số 69/2023/TT-BTC, có hiệu lực kể từ ngày 30 tháng 12 năm 2023." | — |
| A3 | TT139 ngày 30/12/2025 lùi hạn đến hết 31/12/2026 (79, 453) | TT139 Điều 1 khoản 2, Điều 2 khoản 1 | 1 | KHỚP | "Hà Nội, ngày 30 tháng 12 năm 2025"; "d) Chậm nhất đến hết ngày 31 tháng 12 năm 2026: Sở Giao dịch Chứng khoán Hà Nội hoàn thành việc chuyển cổ phiếu của tổ chức niêm yết…"; "Thông tư này có hiệu lực thi hành kể từ ngày 30 tháng 12 năm 2025." | — |
| A4 | UPCoM: hạn hết 31/12/2026 theo VBHN; TT139 không sửa (79) | VBHN19 Điều 4 khoản 3 điểm e (chú thích 11); TT139 chỉ sửa điểm đ khoản 2 và điểm d khoản 3 | 2 | KHỚP. Có thể nói chính xác hơn: hạn UPCoM do TT69 đặt, lùi từ khung 01/01/2025–30/6/2025 của TT57 gốc (m3) | "e)11 Chậm nhất đến hết ngày 31 tháng 12 năm 2026: Sở Giao dịch Chứng khoán Hà Nội hoàn thành việc chuyển cổ phiếu của tổ chức đăng ký giao dịch…"; TT57 gốc: "e) Từ ngày 01 tháng 01 năm 2025 đến hết ngày 30 tháng 6 năm 2025: Sở Giao dịch Chứng khoán Hà Nội thực hiện chuyển cổ phiếu của tổ chức đăng ký giao dịch…" | Xem m3 |
| A5 | Lịch chuyển UPCoM chưa công bố (79) | VBHN19 Điều 4 khoản 4 | 2 | KHỚP MỘT PHẦN. Có căn cứ pháp lý cho kế hoạch, chưa có văn bản kế hoạch | "4. Sở Giao dịch Chứng khoán Việt Nam xây dựng kế hoạch chuyển cổ phiếu của tổ chức niêm yết, đăng ký giao dịch … theo quy định tại điểm đ, e khoản 2, điểm d, e khoản 3 Điều này và báo cáo Ủy ban Chứng khoán Nhà nước trước khi triển khai." | Nhãn hẹp hơn ở mục (6), nhãn #2 |
| A6 | Sau hợp nhất HNX tổ chức thị trường trái phiếu và phái sinh (79, 278) | VBHN19 Điều 5 khoản 2 điểm a; Điều 6 | 2 | KHỚP | "Sở Giao dịch Chứng khoán Hà Nội tổ chức thị trường giao dịch trái phiếu Chính phủ…"; "Sở Giao dịch Chứng khoán Hà Nội tổ chức thị trường giao dịch chứng khoán phái sinh…" | — |
| A7 | HNX ngừng nhận niêm yết mới từ 01/7/2025; mốc thực hiện bị lùi hai lần (189) | Như A1–A3 | 2 | KHỚP | Xem A1–A3 | — |
| A8 | Mốc 30/6/2025 là ngày tham chiếu (189, 192, 233, 270) | Lựa chọn thiết kế, liền trước điểm c (A2) | — | KHỚP (hợp lý) | VBHN Điều 4 khoản 1 còn mốc "Chậm nhất đến hết ngày 30 tháng 6 năm 2025, Sở Giao dịch Chứng khoán thành phố Hồ Chí Minh thống nhất tổ chức thị trường…". TT139 không sửa khoản này. Đề cương không dùng mốc đó; chỉ lưu ý nếu hội đồng hỏi. | — |
| A9 | Tài liệu VBHN19 (452) | VBHN19, phần thông tin | 2 | KHỚP MỘT PHẦN. Số hiệu và ngày đúng; trích yếu bị rút gọn | "Văn bản hợp nhất 19/VBHN-BTC năm 2023 hợp nhất Thông tư quy định lộ trình sắp xếp lại thị trường giao dịch cổ phiếu, thị trường giao dịch trái phiếu, thị trường giao dịch chứng khoán phái sinh và thị trường giao dịch các loại chứng khoán khác"; "Ngày ban hành: 25/12/2023" | Mục (5), idx 452 |
| A10 | Tài liệu TT139 (453) | TT139, trích yếu | 1 | KHỚP MỘT PHẦN. Trích yếu bị rút gọn | Trích yếu đầy đủ ở dòng 27 của nguồn | Mục (5), idx 453 |
| A11 | NQ222: trung tâm tài chính quốc tế đặt tại TP.HCM và Đà Nẵng (79, 89) | NQ222 Điều 3 khoản 1 | 2 | KHỚP | "Trung tâm tài chính quốc tế là khu vực có ranh giới địa lý xác định do Chính phủ thành lập đặt tại Thành phố Hồ Chí Minh và thành phố Đà Nẵng" | — |
| A12 | NQ222 "ngày 27/6/2025" (455) | Bản trích không có phần thông qua | 2 | CHƯA CÓ NGUỒN | Phần đầu chỉ có "Nghị quyết số: 222/2025/QH15 … Về Trung tâm tài chính quốc tế tại Việt Nam" | m4 |
| A13 | Lịch VNX: phiên cuối 23/12/2026, giao dịch HOSE từ 28/12/2026 (79, nhiều chỗ khác) | Chưa có văn bản VNX | 5 | CHƯA CÓ NGUỒN gốc. Ngày 28/12/2026 nằm trong hạn của TT139 | — | m2 (ghi rõ nguồn là báo chí) |
| A14 | VN-Index gồm toàn bộ cổ phiếu niêm yết HOSE và tự cập nhật sau ngày giao dịch đầu tiên của mã niêm yết mới (277) | QĐ 737, mục 2.1 và 2.3 | 3 | KHỚP. Phần áp cho mã chuyển sàn là SUY DIỄN và đã có nhãn | "2.1. Chi so VNINDEX la chi so tong hop … cua tat ca co phieu niem yet va giao dich tren HOSE." "2.3. Danh muc co phieu thanh phan cua chi so duoc tu dong cap nhat sau ngay giao dich dau tien cua co phieu niem yet moi…" | — |
| A15 | QĐ 737/QĐ-SGDHCM ngày 29/9/2026 (456) | Phần đầu QĐ 737 (OCR) | 3 | KHỚP MỘT PHẦN. Số hiệu chỉ suy ra từ tên tệp. Ngày không đọc được, chỉ đọc được tháng 9/2026. Căn cứ có "Cong van so 1314/SGDVN-CLPT ngay 25 thang 9 nam 2026", nên ngày ký từ 25/9 trở đi. QĐ 736 và 738 cùng bộ ghi "ngay 29 thang 9 nam 2026". Trang bìa Quy tắc OCR ra "Thang3 - 2026", nhiều khả năng là lỗi OCR | "S6: ^3^/QD-SGDHCM … ngayMthdng 9 ndm 2026"; "Ban hanh Quy tac chi so VNINDEX phien ban 1.0"; "Quy£t dinh nay co hieu lire ke tu ngay ky." | Giữ nhãn (mục 6, nhãn #18) |
| A16 | QĐ 1193/QĐ-UBND ngày 18/3/2026, đợt 1 (77, 458) | QĐ 1193 (thuvienphapluat) | 2 | KHỚP. Trích yếu thiếu "về việc" | "Số: 1193/QĐ-UBND Hà Nội, ngày 18 tháng 3 năm 2026"; "VỀ VIỆC CÔNG BỐ DANH MỤC CÁC BÀI TOÁN LỚN CỦA THÀNH PHỐ HÀ NỘI GIAI ĐOẠN 2026 - 2030 (ĐỢT 1)" | Mục (5), idx 458 |
| A17 | Hiện trạng, câu hỏi 1, 3 và các sản phẩm của bài toán 19 (77, 89, 295) | QĐ 1193, Phụ lục, bài 19 | 2 | KHỚP | "Hà Nội là trung tâm tài chính lớn của cả nước, tuy nhiên hệ thống dịch vụ tài chính vẫn chưa đạt tầm khu vực"; "1. Những mô hình trung tâm tài chính nào phù hợp với điều kiện phát triển của Hà Nội?"; "3. Những nền tảng công nghệ nào giúp tăng cường minh bạch và hiệu quả của thị trường tài chính?"; "- Trung tâm tài chính quốc tế tại Hà Nội", "- Hệ thống dữ liệu tài chính đô thị" | — |
| A18 | NQ 57/2026/NQ-HĐND: điều kiện học tập trung toàn thời gian, hỗ trợ tối đa 48 tháng | NQ 57 Điều 11 khoản 3, Điều 13, Điều 34 khoản 1 | 4 | **Đề cương không nhắc** (MJ1) | "3. Theo học chương trình đào tạo tiến sĩ và tương đương, tập trung toàn thời gian, có chuyên ngành đào tạo và nội dung nghiên cứu của luận án tiến sĩ phục vụ giải quyết bài toán lớn của Thành phố…"; "…không vượt quá 48 tháng."; "Nghị quyết này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026." | Mục (7) |
| A19 | Thời gian đào tạo bốn năm (337, Bảng 5) và 48 tháng (NQ 57 Điều 13) | — | — | KHỚP (4 năm = 48 tháng) | — | Câu bổ sung ở mục (7) |
| A20 | Biên độ HOSE ±7%, HNX ±10%, UPCoM ±15% (186) | Quy chế giao dịch, chưa có trong hồ sơ | — | CHƯA CÓ NGUỒN, đã có nhãn | — | Nhãn #6 |

**Chuỗi sửa đổi.**
1. TT 57/2021/TT-BTC: ký 12/7/2021, hiệu lực 20/7/2021. Mốc cổ phiếu niêm yết: HNX ngừng nhận niêm yết mới từ 01/7/2023 và chuyển cổ phiếu trong khoảng 01/7–31/12/2023. Mốc UPCoM: chuyển trong khoảng 01/01–30/6/2025.
2. TT 69/2023/TT-BTC: ký 15/11/2023, hiệu lực 30/12/2023. Sửa khoản 1 và các điểm c, d, đ, e (khoản 2), b, c, d, e (khoản 3) Điều 4, cùng khoản 2 Điều 7. Mốc niêm yết mới thành 01/7/2025. Hạn chuyển cổ phiếu niêm yết thành hết 31/12/2025. Hạn UPCoM thành hết 31/12/2026.
3. VBHN 19/VBHN-BTC ngày 25/12/2023 hợp nhất hai thông tư trên. VBHN này chưa gồm TT139.
4. TT 139/2025/TT-BTC: ký và có hiệu lực 30/12/2025. Chỉ sửa điểm đ khoản 2 (phía HOSE tiếp nhận) và điểm d khoản 3 (phía HNX chuyển) thành hết 31/12/2026. **Không sửa** điểm e (UPCoM) và khoản 1.

Như vậy, mốc của cổ phiếu niêm yết bị lùi hai lần, còn mốc của UPCoM bị lùi một lần. Theo các văn bản trong hồ sơ, hai hạn hiện trùng nhau là 31/12/2026.

### B. Số liệu và mô tả văn liệu (fact-checker)

| # | Khẳng định (idx) | Xếp hạng | Căn cứ (trích) | Ghi chú |
|---|---|---|---|---|
| B1 | Amihud và cộng sự (1997): Tel Aviv chuyển từ một phiên khớp lệnh định kỳ sang cơ chế có thêm phiên liên tục; CAR khoảng 5,5% từ 5 ngày trước công bố đến 30 ngày sau; thanh khoản tăng đi cùng giá tăng (81) | TRUE | "transferred gradually from a daily call auction to a mechanism where the call auction was followed by iterated continuous trading sessions … started five days prior to the announcement and ended 30 days after the stocks started trading by the new method was approximately 5.5% … a positive association between liquidity gains and price appreciation" | Nguồn là working paper FIN-98-004. Thông tin JFE 45(3) chưa có trong hồ sơ (C4). |
| B2 | Amihud và cộng sự (1997) ghi nhận thanh khoản lan tỏa (277) | TRUE | "positive liquidity externalities (spillovers) across related stocks" | — |
| B3 | Hisada (2018): cổ phiếu chuyển từ Osaka sang Tokyo ngày 16/7/2013 (81, 93) | **MIXED** | "the stock exchanges were integrated on July 16, 2013. This study uses daily data on common stocks of the TSE, excluding those double listed on the OSE, from July 1, 2010, to June 30, 2016" | Ngày đúng. Mẫu là cổ phiếu sẵn có trên Tokyo, không phải cổ phiếu chuyển sàn. Xem **MJ2**. |
| B4 | Hisada: tăng ngắn hạn nhờ cộng hưởng và tâm lý; tâm lý mạnh hơn ở cổ phiếu nhỏ; giảm sau một năm; dùng vòng quay và ILLIQ (81, 93, 108) | TRUE | "Synergy and the investor sentiment effect occur in the short run with liquidity increases. The investor sentiment effect occurs more strongly in small stocks."; "liquidity decreases 1 year after the merger"; "Yit indicates liquidity, which is turnover or ILLIQ" | — |
| B5 | Hisada: IJEFI 8(2), 315–318 (485) | TRUE | "International Journal of Economics and Financial Issues, 2018, 8(2), 315-318." | — |
| B6 | Nielsson (2009): thanh khoản tăng ở doanh nghiệp lớn và doanh nghiệp có doanh thu nước ngoài, không tăng ở doanh nghiệp nhỏ (81) | MOSTLY TRUE (nguồn thứ cấp) | Hisada viết: "She finds that liquidity increases among large firms and firms with foreign sales." | Vế "không tăng ở doanh nghiệp nhỏ" chưa có nguồn gốc trong hồ sơ (C3). |
| B7 | Naeem (2023): 196 trung tâm theo khu vực tài phán, 2007–2020, 17 yếu tố, cây quyết định (82, 91, 102) | TRUE | "196 IFCs (unique financial jurisdictions) … (2007 till 2020) … 17 most relevant determinants … by using a Decision Tree approach" | — |
| B8 | Naeem dùng thứ hạng GFCI (78, 91, 273) | TRUE (đã sửa ở v7) | "The study uses GFCI ranking as a dependent variable." | — |
| B9 | GFCI có nhân tố "khối lượng giao dịch", một phần lấy từ WFE (275) | TRUE | "financial sector development (such as the volume of trading and availability of capital)"; "the World Federation of Stock Exchange" | — |
| B10 | Bắc Kinh là trung tâm tài chính lớn khi chưa có sở giao dịch (80) | TRUE | "Despite the lack of a stock exchange, Beijing is a significant financial centre in China." | Năm 2021 vẫn chưa có nguồn (nhãn #3). |
| B11 | Eichengreen và Shah (2020) chia yếu tố thành năm nhóm, một nhóm là vốn hóa và mức phát triển tài chính (91) | TRUE (nguồn thứ cấp, qua Naeem) | "divided into five different categories by Eichengreen and Shah (2020) … The third category consists of the set of indicators that measure market capitalisation and financial progress." | — |
| B12 | Moosa và cộng sự (2016) dùng phân tích giới hạn cực trị (91) | TRUE (nguồn thứ cấp) | "test the robustness of included variables using the extreme bound analysis (EBA)" | — |
| B13 | GFCI các kỳ 1–40 "do Z/Yen và China Development Institute công bố" (188) | **MIXED** | "The first index was released in March 2007. It has been published twice a year since 2015 by the China Development Institute in Shenzhen and Z/Yen Group in London." | Các kỳ trước năm 2015 không do CDI đồng công bố (m1). |
| B14 | GFCI 40 vào tháng 9/2026 (79) | MOSTLY TRUE (suy từ nguồn) | Theo Naeem, GFCI 31 công bố ngày 24/3/2022 và GFCI ra hai lần mỗi năm. Suy ra GFCI 40 vào tháng 9/2026. | Thứ hạng 67/117 và 71 vẫn UNVERIFIABLE (nhãn #1). |
| B15 | "khoảng 300" doanh nghiệp (81, 277) | UNVERIFIABLE | — | Nhãn #4. |
| B16 | 23/12 và 28/12/2026 (79) | UNVERIFIABLE (chỉ có báo chí) | — | Ngày 28/12/2026 là thứ Hai, 23/12/2026 là thứ Tư. Tháng 12/2026 có 4 phiên trên HOSE (28–31/12), trừ khi có ngày nghỉ. Các tháng 7/2025–12/2026 đã bị loại khỏi phương trình (5), nên việc này không ảnh hưởng ước lượng chính. |
| B17 | UPCoM có giao dịch từ tháng 6/2009 (189) | UNVERIFIABLE trong hồ sơ | — | Mục (8), A12 mới. |
| B18 | Vo và Phan (2017): 299 công ty, 2005–2015; Nguyen và cộng sự (2020): 468 tuần, 2011–2019 (95) | UNVERIFIABLE trong hồ sơ | — | Không đổi chữ, chỉ đưa vào danh sách cần tìm (C12 mới, ưu tiên thấp). |
| B19 | Đếm cửa sổ: quý 3/2020–quý 2/2025 là 20 cửa sổ; quý 1/2027–quý 4/2028 là 8 cửa sổ (234) | TRUE (tự kiểm) | 2 + 16 + 2 = 20; 4 + 4 = 8 | — |
| B20 | Trọng số MQI wj = 1/(3·nd(j)) với J = 6 (194) | TRUE (tự kiểm) | Chiều thanh khoản 3 chỉ báo × 1/9, chiều thông tin 2 × 1/6, chiều minh bạch 1 × 1/3; tổng bằng 1 | — |
| B21 | Câu hỏi 1, 3 và các sản phẩm của bài toán 19 (77, 89) | TRUE | Xem A17 | — |

---

## (4) Phát hiện theo mức

### MAJOR

**MJ1. Đề cương chưa có cam kết học tập trung toàn thời gian và chưa trích NQ 57/2026/NQ-HĐND.**
- *Mức:* MAJOR. *Vị trí:* idx 441 (mục 8.2), idx 337 (mục 7.4), danh mục. *Skill:* vn-legal-verify, credible-claims, consistency-checker.
- *Căn cứ:* NQ 57 Điều 11 khoản 3: "Theo học chương trình đào tạo tiến sĩ và tương đương, tập trung toàn thời gian, …". Điều 13: "…không vượt quá 48 tháng." Đề cương idx 441: "Thí sinh đang theo học ngành Kế toán hệ vừa làm vừa học tại Đại học Kinh tế Quốc dân (năm thứ ba), ngành Công nghệ thông tin hệ đào tạo từ xa tại Học viện Công nghệ Bưu chính Viễn thông (năm thứ ba), và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 07/2026."
- *Vì sao MAJOR:* Hồ sơ dùng để xin hỗ trợ theo NQ 57. Hội đồng tư vấn theo Điều 17 sẽ đọc thấy ba chương trình học song song mà không thấy cam kết nào, và điều kiện tại Điều 11.3 là điều kiện loại.
- *Sửa:* thêm các câu ở mục (7) vào idx 441 (bắt buộc), idx 337 (nên có) và idx 328 (tùy chọn), và thêm mục NQ 57 vào danh mục.

**MJ2. Hisada (2018) bị mô tả sai đối tượng nghiên cứu.**
- *Mức:* MAJOR. *Vị trí:* idx 81, 93; nên bổ sung ở 88 và 277; Bảng 1 idx 108 (tùy chọn). *Skill:* fact-checker (MIXED), credible-claims.
- *Căn cứ:* Hisada, mục 4.1: "the stock exchanges were integrated on July 16, 2013. This study uses daily data on common stocks of the TSE, excluding those double listed on the OSE". Mẫu của Hisada là cổ phiếu **sẵn có trên Tokyo, sàn tiếp nhận**, không phải cổ phiếu chuyển từ Osaka sang. Bài không có nhóm đối chứng; thiết kế là hồi quy hiệu ứng cố định với biến chỉ sự kiện.
- *Vì sao MAJOR:* Đề cương dùng Hisada làm bằng chứng gần nhất cho H3, tức tác động lên cổ phiếu chuyển sàn. Thực ra bằng chứng này nói về nhóm tương ứng với **nhóm đối chứng HOSE**. Một thành viên hội đồng đã đọc bài sẽ nhận ra. Phát hiện này cũng có ích cho đề cương: (i) nó cho thấy giả định không lan tỏa ở mục 4.3.8 có nguy cơ thật; (ii) nó làm rõ thêm đóng góp của đề tài, vì đề tài đo trực tiếp các mã được chuyển.
- *Sửa:*
  - idx 81. Chuỗi gốc: "Ngược lại, Hisada (2018) nghiên cứu việc chuyển cổ phiếu từ Sở Giao dịch Chứng khoán Osaka sang Sở Giao dịch Chứng khoán Tokyo ngày 16/7/2013 và thấy thanh khoản tăng trong ngắn hạn nhờ hiệu ứng cộng hưởng và tâm lý nhà đầu tư, trong đó hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, rồi thanh khoản giảm sau một năm."
    → "Ngược lại, Hisada (2018) nghiên cứu việc hợp nhất Sở Giao dịch Chứng khoán Tokyo và Sở Giao dịch Chứng khoán Osaka, với thị trường cổ phiếu của hai sở được hợp nhất ngày 16/7/2013, trên mẫu các cổ phiếu niêm yết tại Tokyo không niêm yết kép tại Osaka, và thấy thanh khoản của nhóm cổ phiếu này tăng trong ngắn hạn nhờ hiệu ứng cộng hưởng và tâm lý nhà đầu tư, trong đó hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, rồi giảm sau một năm."
  - idx 93. Chuỗi gốc: "còn Hisada (2018) thấy việc chuyển cổ phiếu từ Osaka sang Tokyo năm 2013 làm thanh khoản tăng trong ngắn hạn, hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, với thước đo là vòng quay và độ phi thanh khoản Amihud."
    → "còn Hisada (2018) thấy thanh khoản của các cổ phiếu sẵn có trên Sở Giao dịch Chứng khoán Tokyo tăng trong ngắn hạn sau khi thị trường cổ phiếu của Osaka được hợp nhất vào Tokyo năm 2013, hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, với thước đo là vòng quay và độ phi thanh khoản Amihud."
  - idx 88. Chuỗi gốc: "với suy luận phù hợp cho một sự kiện duy nhất, và ước lượng thêm tác động lên khả năng đầu tư."
    → "với suy luận phù hợp cho một sự kiện duy nhất, đo trực tiếp các cổ phiếu được chuyển sàn so với nhóm đối chứng, và ước lượng thêm tác động lên khả năng đầu tư."
  - idx 277. Chuỗi gốc: "nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác."
    → "nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác. Hisada (2018) cho thấy thanh khoản của cổ phiếu sẵn có trên sàn tiếp nhận cũng tăng trong ngắn hạn quanh đợt hợp nhất Tokyo–Osaka; nếu điều tương tự xảy ra với nhóm đối chứng HOSE, δ đánh giá thấp tác động."
  - idx 108 (tùy chọn). Chuỗi gốc: "Tokyo–Osaka: hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ"
    → "Tokyo–Osaka (cổ phiếu của sàn tiếp nhận): hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ"

**MJ3. Câu nối với bài toán 19 ở idx 77 nói đề tài đo "chất lượng thị trường vốn của Hà Nội". Câu này mâu thuẫn với định nghĩa ở idx 78 và với phạm vi định lượng.**
- *Mức:* MAJOR. *Vị trí:* idx 77. *Skill:* credible-claims (cần thu hẹp cách diễn đạt), consistency-checker (định nghĩa).
- *Căn cứ:* idx 78 định nghĩa: "Thị trường vốn Hà Nội là các thị trường do HNX tiếp tục vận hành sau hợp nhất: trái phiếu và chứng khoán phái sinh, cùng UPCoM…". idx 293: "Phân tích định lượng không xét thị trường trái phiếu và phái sinh". Như vậy, cái đề tài thực sự đo là chất lượng giao dịch cổ phiếu trên HNX so với HOSE, và thay đổi khi cổ phiếu **rời** Hà Nội. Nó không đo chất lượng của "thị trường vốn Hà Nội" theo nghĩa đã định nghĩa. Đây là câu nối duy nhất giữa đề tài và câu hỏi 1, 3 của bài toán 19, nên Hội đồng xét theo Điều 11.3 NQ 57 sẽ đọc kỹ câu này.
- *Sửa (idx 77).* Chuỗi gốc: "Đề tài cung cấp thước đo nền cho hai câu hỏi này: chất lượng thị trường vốn của Hà Nội thay đổi thế nào khi cấu trúc sàn giao dịch thay đổi."
  → "Đề tài cung cấp thước đo nền cho hai câu hỏi này: chất lượng giao dịch cổ phiếu khác nhau thế nào giữa sàn niêm yết của Hà Nội và sàn của Thành phố Hồ Chí Minh, và thay đổi thế nào khi cổ phiếu niêm yết chuyển từ HNX sang HOSE."

**MJ4. H2 là kiểm định xác nhận trong họ Holm, nhưng giai đoạn mẫu và quy tắc quyết định chưa được đặc tả thống nhất.**
- *Mức:* MAJOR. *Vị trí:* idx 176 (Bảng 2), idx 123 và 146 (Hình 1), idx 194. *Skill:* consistency-checker (nhóm 5 và 6), credible-claims.
- *Căn cứ:*
  - Giai đoạn: idx 176 ghi "H2: Trong giai đoạn 2009–2026". Hình 1 ghi "Giai đoạn 2009–2026". Nhưng idx 189 nói giai đoạn tham chiếu kết thúc 30/6/2025 và giai đoạn 7/2025–12/2026 là chuyển tiếp; idx 192 chuẩn hóa z trên giai đoạn tham chiếu; idx 286 tính MDE trên "giai đoạn 2009–2025". Trong giai đoạn chuyển tiếp, HNX không nhận niêm yết mới (A2), nên thành phần sàn thay đổi theo hướng có hệ thống.
  - Quy tắc quyết định: idx 194 ghi "H2 được ủng hộ khi chênh lệch bình quân dương với khoảng tin cậy bootstrap khối dừng trên chuỗi tháng loại trừ 0", còn idx 185 và 286 đưa "giá trị p bootstrap khối cho H2" vào thủ tục Holm. Khoảng tin cậy 95% chưa hiệu chỉnh và ngưỡng Holm (α/3, α/2 hoặc α) có thể cho hai kết luận khác nhau.
  - Hệ quả: tệp đăng ký trước sẽ có hai đặc tả cho cùng một giả thuyết, tức là có lối rẽ phân tích.
- *Sửa:*
  - idx 176. Chuỗi gốc: "H2: Trong giai đoạn 2009–2026, Chỉ số chất lượng thị trường vốn của sàn niêm yết HNX thấp hơn của HOSE (câu hỏi 2)"
    → "H2: Trong giai đoạn tham chiếu từ tháng 6/2009 đến tháng 6/2025, Chỉ số chất lượng thị trường vốn của sàn niêm yết HNX thấp hơn của HOSE (câu hỏi 2)"
  - idx 123 và 146 (Hình 1). Chuỗi gốc: "Giai đoạn 2009–2026" → "Giai đoạn 6/2009–6/2025"
  - idx 194. Chuỗi gốc: "H2 được ủng hộ khi chênh lệch bình quân dương với khoảng tin cậy bootstrap khối dừng trên chuỗi tháng loại trừ 0 (Politis & Romano, 1994)."
    → "H2 được ủng hộ khi chênh lệch bình quân trong giai đoạn tham chiếu dương và giá trị p bootstrap khối dừng trên chuỗi tháng (Politis & Romano, 1994) nhỏ hơn ngưỡng Holm tương ứng; khoảng tin cậy được báo cáo kèm theo. Chênh lệch trong giai đoạn chuyển tiếp từ tháng 7/2025 đến tháng 12/2026 được báo cáo riêng ở dạng mô tả."
  - Nếu thí sinh muốn giữ mẫu đến 12/2026, thì phải ghi điều đó thống nhất ở idx 176, 189, 194 và 286, và nêu cách xử lý việc thành phần sàn thay đổi. Đây là lựa chọn thiết kế nên cần người dùng quyết.

### MINOR

**m1. Đơn vị công bố GFCI (idx 188).** fact-checker. Căn cứ: B13. Chuỗi gốc: "do Z/Yen và China Development Institute công bố công khai và được thí sinh số hóa từ báo cáo từng kỳ" → "do Z/Yen công bố công khai từ năm 2007 (từ năm 2015 cùng China Development Institute) và được thí sinh số hóa từ báo cáo từng kỳ"

**m2. Lịch chuyển sàn dựa vào báo chí nhưng câu viết như dẫn văn bản của VNX (idx 79).** vn-legal-verify, nguyên tắc 1 (báo chí chỉ là manh mối). Chuỗi gốc: "Theo lịch do Sở Giao dịch Chứng khoán Việt Nam (VNX) công bố ngày 30/9/2026, cổ phiếu niêm yết tại HNX giao dịch phiên cuối ngày 23/12/2026 và giao dịch trên HOSE từ ngày 28/12/2026 (Thời báo Tài chính Việt Nam, 2026)."
→ "Theo Thời báo Tài chính Việt Nam (2026), lịch do Sở Giao dịch Chứng khoán Việt Nam (VNX) công bố ngày 30/9/2026 ấn định phiên giao dịch cuối của cổ phiếu niêm yết tại HNX là ngày 23/12/2026 và ngày bắt đầu giao dịch trên HOSE là ngày 28/12/2026 [CẦN ĐỐI CHIẾU thông báo gốc của VNX]."
Ghi chú: khi có thông báo gốc (mục 8, A2), thay nguồn và bỏ nhãn.

**m3. Hạn UPCoM do TT69 đặt (idx 79), tùy chọn.** vn-legal-verify, bước 3. Chuỗi gốc: "Thông tư số 139/2025/TT-BTC không sửa mốc này." → "Mốc này do Thông tư số 69/2023/TT-BTC đặt, thay cho khung từ ngày 01/01/2025 đến hết ngày 30/6/2025 của Thông tư số 57/2021/TT-BTC, và Thông tư số 139/2025/TT-BTC không sửa mốc này."

**m4. Ngày của NQ 222 chưa có nguồn (idx 455).** Căn cứ: A12. Chuỗi gốc: "Quốc hội (2025), Nghị quyết số 222/2025/QH15 ngày 27/6/2025 về Trung tâm tài chính quốc tế tại Việt Nam." Có hai cách. (a) Bỏ ngày: dùng chuỗi APA ở mục (5) không có ngày. (b) Giữ ngày và thêm "[CẦN XÁC MINH ngày thông qua]" đến khi có Công báo (mục 8, A7).

**m5. idx 82 nói "ba vấn đề", nhưng Bảng 1 và idx 114, 119 nói "bốn khoảng trống" K1–K4.** consistency-checker, nhóm 7a. K2 (chưa quy đổi thành tổn thất của nhà đầu tư) đến từ mục 4.2(B), không có trong ba vấn đề ở 4.1. Chuỗi gốc (idx 96): "Bảng 1 đối chiếu bốn nhóm công trình gần nhất với đề tài và nêu khoảng trống của từng nhóm." → "Bảng 1 đối chiếu bốn nhóm công trình gần nhất với đề tài và nêu khoảng trống của từng nhóm; khoảng trống K2 bổ sung cho ba vấn đề nêu ở mục 4.1."

**m6. Cập nhật MQI cho UPCoM ở idx 279 thiếu điều kiện so với idx 194.** consistency-checker. Chuỗi gốc: "Chỉ số chất lượng thị trường vốn được cập nhật theo tháng cho UPCoM và HOSE khi có dữ liệu mới." → "Chỉ số chất lượng thị trường vốn được cập nhật theo tháng cho HOSE, và cho UPCoM trong thời gian UPCoM còn do HNX vận hành, khi có dữ liệu mới."

**m7. Kích thước rổ ở idx 294 chưa thống nhất với "tối đa 30" (idx 233) và với rổ 20 mã của phương án dự phòng (idx 287).** Chuỗi gốc: "chỉ áp dụng cho rổ 30 cổ phiếu chuyển sàn có thanh khoản cao nhất" → "chỉ áp dụng cho rổ CS, gồm tối đa 30 cổ phiếu chuyển sàn có thanh khoản cao nhất"

**m8. Mục 7.3 và Bảng 5 lệch về nội dung bài báo 3.** idx 335 nói bài báo 3 gồm "định hướng cho Hà Nội", nhưng Bảng 5 xếp việc viết bài báo 3 (H1) vào năm 3, quý 3–4, còn việc đề xuất định hướng vào năm 4, quý 1–2. Chuỗi gốc (idx 335): "bài báo 3 trình bày bằng chứng quốc tế (H1) và định hướng cho Hà Nội." → "bài báo 3 trình bày bằng chứng quốc tế (H1) và so sánh vai trò của Hà Nội với các trung tâm trong khu vực."

**m9. Danh mục chữ viết tắt chưa đủ và có một ký hiệu trùng.**
- Thiếu: GDP (idx 174, 275), ARIMA (idx 95), OECD (idx 178, 192), FTSE (idx 277).
- Trùng ký hiệu: "H" vừa là rổ cổ phiếu HOSE (idx 66) vừa là tiền tố của H1–H4.
- Sửa: thêm "GDP: tổng sản phẩm trong nước (Gross Domestic Product)", "ARIMA: mô hình tự hồi quy tích hợp trung bình trượt (Autoregressive Integrated Moving Average)", "OECD: Tổ chức Hợp tác và Phát triển Kinh tế (Organisation for Economic Co-operation and Development)".
- Chuỗi gốc (idx 66): "H: rổ cổ phiếu HOSE được ghép với rổ CS" → "H: rổ cổ phiếu HOSE được ghép với rổ CS (khác với H1–H4, ký hiệu các giả thuyết)"

**m10. Định dạng ngày chưa thống nhất.** Hiện có "30/09/2026" (idx 56, 114, 375, 376, 378), "30/9/2026" (idx 79), "tháng 07/2026" (idx 441), "18/03/2026" (idx 458) cùng với "01/7/2025". Đề xuất một quy ước: ngày không có số 0 đứng đầu, tháng không có số 0 đứng đầu, ví dụ "30/9/2026", "18/3/2026", "tháng 7/2026". Riêng "01/7/2025" và "01/7/2023" giữ như văn bản pháp luật hoặc đổi thành "1/7/2025", miễn là thống nhất. Các chuỗi cần thay: "30/09/2026" → "30/9/2026" (5 chỗ); "tháng 07/2026" → "tháng 7/2026"; "ngày 18/03/2026" → "ngày 18/3/2026".

**m11. Nguyen/Nguyễn ở 2026a và 2026b (m9(ii) của r7, chưa sửa).** Hậu tố a/b chỉ có nghĩa khi hai mục có cùng chuỗi tác giả.
- Chọn một cách: **Nguyễn** có dấu, vì APA 7 giữ dấu trong tên riêng và cả hai tác giả là người Việt.
- Thứ tự a/b giữ nguyên, vì APA xếp theo tiêu đề: "Black-Litterman…" (a) đứng trước "Tiền gửi…" (b).
- Thay các chuỗi trong bài:
  - idx 88: "(Vo & Phan, 2017; Goutte và cộng sự, 2025; Nguyen & Nguyen, 2026a)" → "(Vo & Phan, 2017; Goutte và cộng sự, 2025; Nguyễn & Nguyễn, 2026a)"
  - idx 95: "(Nguyen & Nguyen, 2026a)" → "(Nguyễn & Nguyễn, 2026a)"
  - idx 110: "Nguyen & Nguyen, 2026a)" → "Nguyễn & Nguyễn, 2026a)"
  - idx 215: "Mở rộng từ Nguyen và Nguyen (2026a)" → "Mở rộng từ Nguyễn và Nguyễn (2026a)"
  - idx 224: "Nguyen và Nguyen (2026a)" → "Nguyễn và Nguyễn (2026a)"
  - idx 369: "(Nguyen & Nguyen, 2026a)" → "(Nguyễn & Nguyễn, 2026a)"
  - idx 442: "Bài báo Nguyen và Nguyen (2026a)" → "Bài báo Nguyễn và Nguyễn (2026a)"
  - Mục danh mục: xem mục (5).
- Không đổi "Nguyen và cộng sự (2020)": đó là tác giả khác.

**m12. Danh mục tài liệu tham khảo chưa theo APA 7.** Cụ thể: thiếu "&" trước tác giả cuối, dùng "pp.", năm không đứng giữa hai dấu chấm, tên tạp chí và tập không in nghiêng, trích yếu văn bản pháp luật bị rút gọn. Từng mục ở mục (5).

**m13. Hai mục báo chí thiếu ngày đăng.** VietnamPlus 2026a và 2026b (idx 514, 515), Thời báo Tài chính Việt Nam (idx 457). APA 7 cần (năm, tháng ngày) cho bài báo trực tuyến. Đã gắn nhãn [CẦN BỔ SUNG ngày đăng] trong chuỗi APA ở mục (5).

**m14. Tám nhãn có thể gỡ bằng cách viết lại thành câu kế hoạch, không cần thêm dữ kiện.** idx 93, 188 (hai nhãn), 227, 275, 278, 286, 295. Chuỗi thay ở mục (6).

### Claim record (credible-claims)

| Khẳng định | Căn cứ hỗ trợ | Thay đổi sau khi xem kết quả | Còn mở | Cách diễn đạt được phép | Ai quyết |
|---|---|---|---|---|---|
| H1: SMD liên hệ dương với điểm GFCI | Phương trình (7), dữ liệu bảng, phân cụm theo quốc gia; GFCI có nhân tố khối lượng giao dịch (B9) | Không (chưa có dữ liệu) | Phần cơ học giữa SMD và GFCI; phương án mô tả nếu trùng lặp ở phần lớn các kỳ | "liên hệ có điều kiện". Đề cương đang dùng đúng cách này (idx 275, 294) | Người dùng (đã duyệt ở vòng 7) |
| H2: MQI của HNX thấp hơn của HOSE | Phương trình (1), bootstrap khối | Không | **Giai đoạn mẫu và quy tắc quyết định chưa thống nhất (MJ4)** | So sánh mô tả có kiểm định; không gọi là "tác động" | Người dùng quyết phạm vi mẫu |
| H3: tác động lên log Amihud của mã chuyển sàn | Khác biệt kép trên chuỗi chênh lệch, hoán vị, Holm | Không | Lan tỏa sang nhóm đối chứng HOSE (MJ2 làm rủi ro này rõ hơn); ba cú sốc trùng thời gian; cách HOSE xử lý mã chuyển sàn trong VN-Index (nhãn) | "tác động gộp của sàn". Đã đúng ở idx 277, 294 | — |
| H4: khoảng cách khả năng đầu tư thu hẹp | 8 cửa sổ sau và 20 cửa sổ trước, bootstrap | Không | MDE lớn | "ước lượng". Đã đúng | — |
| "Bằng chứng đầu tiên" (88) | Phạm vi tìm kiếm ở idx 114 | — | Chưa tìm trên Scopus, WoS và tạp chí trong nước | Đã giới hạn trong phạm vi tìm kiếm, chấp nhận được | — |
| Thước đo nền cho câu hỏi 1 và 3 của bài toán 19 (77) | Định nghĩa ở idx 78; phạm vi ở idx 293 | — | **Đang nói quá (MJ3)** | Thu hẹp như MJ3 | Người dùng |
| Sản phẩm: cấu phần của "Hệ thống dữ liệu tài chính đô thị"; đầu vào cho "Trung tâm tài chính quốc tế tại Hà Nội" (89) | A17, A11 | Đã sửa ở vòng 7 | — | Như hiện tại | — |
| Đủ điều kiện NQ 57 | A18 | Người dùng đã quyết cam kết toàn thời gian | Phương án với ba chương trình song song; danh mục bài toán áp dụng là QĐ 1193 hay danh mục mới (NQ 57 Điều 35) | Câu ở mục (7), có nhãn [CẦN XÁC NHẬN] | **Người dùng (đã quyết)** |

Không có tuyến nào bị chặn hoàn toàn. Một tuyến bị chặn có điều kiện: nếu UPCoM chuyển trong cửa sổ sau sự kiện, nhóm đối chứng UPCoM bị cắt. Đề cương đã có phương án dự phòng cho tình huống này (idx 287).

### Checklist nhất quán (consistency-checker, không chạy script)

| Nhóm | Kết quả |
|---|---|
| 1a–1c Bảng, hình, phương trình | ✓ Bảng 1–7 đều được dẫn trong bài, đúng thứ tự, tên trùng với danh mục bảng. ✓ Hình 1–3 được dẫn ở idx 119, 168, 234, 281, tên trùng với danh mục hình. ✓ Phương trình (1)–(7) đều tồn tại; các chỗ dẫn (1), (5)–(7) và (6) đều đúng. |
| 1d Dẫn mục | ✓ "mục 4.3.10" (355), "mục 4.3.8" (294), "mục 4.1" (328) và "mục 4.2" (82, 113) đều trỏ đúng. |
| 1e Trích dẫn hai chiều | ✓ 68 mục trong danh mục (7 tiếng Việt, 61 tiếng Anh). Mọi trích dẫn trong bài có mục tương ứng và mọi mục đều được trích (đã grep từng tác giả). ✓ Quy tắc "&" trong ngoặc, "và" ngoài ngoặc đều đúng. "Taylor & Francis" và "Cogent Business & Management" là tên riêng. ✗ Nguyen/Nguyễn (m11). |
| 2 Bảng | ✓ Ghi chú Bảng 2 (Holm cho H1–H3; H4 là ước lượng) khớp idx 270, 275, 286. ✓ Ghi chú Bảng 3 (104 tuần, chỉ mua) khớp idx 234 và 293. ✗ Bảng 2 H2 ghi "2009–2026" (MJ4). |
| 3 Hình | ✓ Ghi chú Hình 1 khớp H1–H4. ✗ Hình 1 ghi "Giai đoạn 2009–2026" (MJ4). ✓ Hình 3 có năm bước, khớp idx 281. |
| 4 Biến | ✓ Amihud loại ngày chạm biên độ và ngày liền sau: nhất quán ở idx 179, 180, 186, 270. ✓ J = 6 và sáu chỉ báo khớp Bảng 2. ✓ SMD gồm vòng quay và vốn hóa/GDP: khớp giữa Bảng 2 và idx 275. ✓ Rổ CS/H và ngày 30/6/2025 khớp ở idx 233 và 270. ✗ Kích thước rổ "30" và "tối đa 30" (m7). |
| 5 Mẫu và mốc | ✓ 6/2009 (189, 292); 30/6/2025 (189, 233, 270); 7/2025–12/2026 (189, 270); từ 1/2027 (189, 270); 24 tháng (189, 287, 292, 349, 355); k từ 1/2024 đến 12/2028 khớp 24 tháng sau sự kiện và các cửa sổ đến quý 4/2028. ✓ Bảng 5: 12 tháng dữ liệu sau sự kiện ở năm 2 và 24 tháng ở năm 3 là khả thi nếu năm 1 là năm 2027. ✗ Giai đoạn của H2 (MJ4). |
| 6 Phương pháp | ✓ Holm cho H1–H3 nhất quán ở idx 185, 270, 275, 286. ✗ Quy tắc quyết định H2 (MJ4). ✓ Phân cụm: theo quốc gia cho H1; theo cổ phiếu và tháng chỉ để so sánh cho H3. ✓ Bốn giả thuyết, ba câu hỏi, bốn mục tiêu nhất quán (idx 83, 87, 119). |
| 7 Cấu trúc | ✓ Mục lục 4–11, 4.3.1–4.3.10, 7.1–7.4, 8.1–8.2 khớp các tiêu đề. ✓ "năm khái niệm" ở idx 78 đếm đúng năm. ✓ "năm phương án dự phòng" ở idx 287 có đúng năm phương án và khớp năm mục ở idx 355. ✗ "ba vấn đề" so với K1–K4 (m5). ✗ Danh mục chữ viết tắt (m9). ✗ Định dạng ngày (m10). |
| 8 Liên văn bản (r7 → v7) | ✓ Các sửa đổi đã cam kết ở vòng 7 đều có trong bản, trừ MJ6 (chờ người dùng) và m9(ii). |
| 9 Ngôn ngữ, nói quá | ✗ MJ3. ✓ "liên hệ có điều kiện" và "tác động gộp" dùng nhất quán. |
| 10 Lỗi hay gặp | ✓ Không có tài liệu mồ côi. ✓ Không có đánh số bảng lệch một. ✗ m8 (7.3 lệch Bảng 5). |

---

## (5) Bảng sửa danh mục theo APA 7 (từng mục)

**Quy ước chung.**
- APA 7 dùng **một danh mục xếp theo bảng chữ cái**. Nếu mẫu của Trường yêu cầu tách tiếng Việt và tiếng Anh, có thể giữ hai phần, nhưng nên ghi rõ đó là yêu cầu của Trường.
- Chỉ dùng DOI đã có trong hồ sơ. Không thêm DOI hay số trang nào từ trí nhớ: các trường còn thiếu đã chuyển sang mục (8), nhóm C13.
- Dấu `*…*` nghĩa là in nghiêng. Văn bản pháp luật theo mẫu: Cơ quan. (Năm). *Loại văn bản, số hiệu, ngày, trích yếu*.
- Tên tạp chí dùng đúng tên chính thức, kể cả "The" khi tên chính thức có "The": *The Review of Financial Studies*, *The Journal of Finance*, *The Review of Economics and Statistics*, *The Review of Economic Studies*.
- Thứ tự APA trong một danh mục: Amihud (2002); Amihud, Mendelson, & Lauterbach (1997); Bae; Bai; Bekaert; Bessler; Black; Bộ Tài chính (2023); Bộ Tài chính (2025); Callaway; Cetorelli; Chen; Christie; Čihák; Conley; Corwin; Dao; Daw; DeMiguel; Eichengreen; Elliott; Fong; Garlappi; Gehrig; Goutte; Griffin; Hamilton; Hisada; Hoang; Hội đồng nhân dân thành phố Hà Nội (mục mới); Holm; Hou; Huang; International Monetary Fund; Kan; Kaufmann; Kindleberger; Kritzman; Lai; Lang; Ledoit (2004); Ledoit (2008); Lesmond (2005); Lesmond và cộng sự (1999); Lo; Markowitz; Michaud; Moosa; Naeem; Nguyen, N. (2020); Nguyễn, T. B. (2026a); Nguyễn, T. B. (2026b); Nielsson; OECD; Pflug; Politis; Quốc hội; Rambachan; Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh; Ta; Thời báo Tài chính Việt Nam; Ủy ban nhân dân thành phố Hà Nội; VietnamPlus (2026a); VietnamPlus (2026b); Vo; Vu; Wang; Wójcik; Yao.

**Tài liệu tiếng Việt**

| idx | Chuỗi gốc | Chuỗi APA 7 thay thế |
|---|---|---|
| 452 | Bộ Tài chính (2023), Văn bản hợp nhất số 19/VBHN-BTC ngày 25/12/2023 hợp nhất Thông tư số 57/2021/TT-BTC ngày 12/7/2021 và Thông tư số 69/2023/TT-BTC ngày 15/11/2023 quy định lộ trình sắp xếp lại thị trường giao dịch cổ phiếu, trái phiếu, chứng khoán phái sinh và các loại chứng khoán khác. | Bộ Tài chính. (2023). *Văn bản hợp nhất số 19/VBHN-BTC ngày 25/12/2023 hợp nhất Thông tư quy định lộ trình sắp xếp lại thị trường giao dịch cổ phiếu, thị trường giao dịch trái phiếu, thị trường giao dịch chứng khoán phái sinh và thị trường giao dịch các loại chứng khoán khác* (hợp nhất Thông tư số 57/2021/TT-BTC ngày 12/7/2021 và Thông tư số 69/2023/TT-BTC ngày 15/11/2023). |
| 453 | Bộ Tài chính (2025), Thông tư số 139/2025/TT-BTC ngày 30/12/2025 sửa đổi, bổ sung một số điều của Thông tư số 57/2021/TT-BTC được sửa đổi, bổ sung bởi Thông tư số 69/2023/TT-BTC. | Bộ Tài chính. (2025). *Thông tư số 139/2025/TT-BTC ngày 30/12/2025 sửa đổi, bổ sung một số điều của Thông tư số 57/2021/TT-BTC ngày 12 tháng 7 năm 2021 của Bộ trưởng Bộ Tài chính quy định lộ trình sắp xếp lại thị trường giao dịch cổ phiếu, thị trường giao dịch trái phiếu, thị trường giao dịch chứng khoán phái sinh và thị trường giao dịch các loại chứng khoán khác được sửa đổi, bổ sung bởi Thông tư số 69/2023/TT-BTC ngày 15 tháng 11 năm 2023 của Bộ trưởng Bộ Tài chính*. |
| 454 | Nguyễn Thanh Bình, Nguyễn Văn Trung (2026b), “Tiền gửi không kỳ hạn, hiệu quả hoạt động và ổn định tài chính ngân hàng: Bằng chứng từ mô hình ngưỡng tại Việt Nam”, Tạp chí Kinh tế - Luật và Ngân hàng, 28(9), tr. 52–64, DOI: 10.59276/3030-4199/jelb.bav.895. | Nguyễn, T. B., & Nguyễn, V. T. (2026b). Tiền gửi không kỳ hạn, hiệu quả hoạt động và ổn định tài chính ngân hàng: Bằng chứng từ mô hình ngưỡng tại Việt Nam. *Tạp chí Kinh tế - Luật và Ngân hàng*, *28*(9), 52–64. https://doi.org/10.59276/3030-4199/jelb.bav.895 |
| 455 | Quốc hội (2025), Nghị quyết số 222/2025/QH15 ngày 27/6/2025 về Trung tâm tài chính quốc tế tại Việt Nam. | Quốc hội. (2025). *Nghị quyết số 222/2025/QH15 về Trung tâm tài chính quốc tế tại Việt Nam*. (Chỉ thêm "ngày 27/6/2025" sau khi đối chiếu Công báo; xem m4.) |
| 456 | Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh (2026), Quyết định số 737/QĐ-SGDHCM ngày 29/9/2026 ban hành Quy tắc chỉ số VNINDEX phiên bản 1.0 [CẦN XÁC MINH số hiệu và ngày trên bản gốc]. | Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh. (2026). *Quyết định số 737/QĐ-SGDHCM ngày 29/9/2026 ban hành Quy tắc chỉ số VNINDEX phiên bản 1.0* [CẦN XÁC MINH số hiệu và ngày trên bản gốc; bản OCR chỉ đọc được tháng 9/2026]. |
| 457 | Thời báo Tài chính Việt Nam (2026), “Chốt thời điểm chuyển toàn bộ cổ phiếu niêm yết về HOSE”, https://thoibaotaichinhvietnam.vn/chot-thoi-diem-chuyen-toan-bo-co-phieu-niem-yet-ve-hose-204623.html. | Thời báo Tài chính Việt Nam. (2026, [CẦN BỔ SUNG ngày đăng]). Chốt thời điểm chuyển toàn bộ cổ phiếu niêm yết về HOSE. *Thời báo Tài chính Việt Nam*. https://thoibaotaichinhvietnam.vn/chot-thoi-diem-chuyen-toan-bo-co-phieu-niem-yet-ve-hose-204623.html |
| 458 | Ủy ban nhân dân thành phố Hà Nội (2026), Quyết định số 1193/QĐ-UBND ngày 18/03/2026 công bố Danh mục các bài toán lớn của thành phố Hà Nội giai đoạn 2026–2030 (đợt 1), Hà Nội. | Ủy ban nhân dân thành phố Hà Nội. (2026). *Quyết định số 1193/QĐ-UBND ngày 18/3/2026 về việc công bố Danh mục các bài toán lớn của thành phố Hà Nội giai đoạn 2026–2030 (đợt 1)*. |
| mới | (chưa có) | Hội đồng nhân dân thành phố Hà Nội. (2026). *Nghị quyết số 57/2026/NQ-HĐND ngày 15/6/2026* [CẦN BỔ SUNG trích yếu đầy đủ theo bản chính]. Xem mục (7). |

**Tài liệu tiếng Anh**

| idx | Chuỗi gốc | Chuỗi APA 7 thay thế |
|---|---|---|
| 460 | Amihud, Y. (2002), “Illiquidity and stock returns: Cross-section and time-series effects”, Journal of Financial Markets, 5(1), pp. 31–56. | Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. *Journal of Financial Markets*, *5*(1), 31–56. |
| 461 | Amihud, Y., Mendelson, H., Lauterbach, B. (1997), “Market microstructure and securities values: Evidence from the Tel Aviv Stock Exchange”, Journal of Financial Economics, 45(3), pp. 365–390. | Amihud, Y., Mendelson, H., & Lauterbach, B. (1997). Market microstructure and securities values: Evidence from the Tel Aviv Stock Exchange. *Journal of Financial Economics*, *45*(3), 365–390. (Hồ sơ chỉ có bản working paper; tập, số và trang cần đối chiếu bản JFE, mục 8, C4.) |
| 462 | Bae, K.-H., Chan, K., Ng, A. (2004), “Investibility and return volatility”, Journal of Financial Economics, 71(2), pp. 239–263. | Bae, K.-H., Chan, K., & Ng, A. (2004). Investibility and return volatility. *Journal of Financial Economics*, *71*(2), 239–263. |
| 463 | Bai, J., Perron, P. (1998), “Estimating and testing linear models with multiple structural changes”, Econometrica, 66(1), pp. 47–78. | Bai, J., & Perron, P. (1998). Estimating and testing linear models with multiple structural changes. *Econometrica*, *66*(1), 47–78. |
| 464 | Bekaert, G., Harvey, C. R., Lundblad, C. (2007), “Liquidity and expected returns: Lessons from emerging markets”, Review of Financial Studies, 20(6), pp. 1783–1831. | Bekaert, G., Harvey, C. R., & Lundblad, C. (2007). Liquidity and expected returns: Lessons from emerging markets. *The Review of Financial Studies*, *20*(6), 1783–1831. |
| 465 | Bessler, W., Opfer, H., Wolff, D. (2017), “Multi-asset portfolio optimization and out-of-sample performance: An evaluation of Black-Litterman, mean-variance, and naïve diversification approaches”, European Journal of Finance, 23(1), pp. 1–30. | Bessler, W., Opfer, H., & Wolff, D. (2017). Multi-asset portfolio optimization and out-of-sample performance: An evaluation of Black-Litterman, mean-variance, and naïve diversification approaches. *The European Journal of Finance*, *23*(1), 1–30. |
| 466 | Black, F., Litterman, R. (1992), “Global portfolio optimization”, Financial Analysts Journal, 48(5), pp. 28–43. | Black, F., & Litterman, R. (1992). Global portfolio optimization. *Financial Analysts Journal*, *48*(5), 28–43. |
| 467 | Callaway, B., Sant’Anna, P. H. C. (2021), “Difference-in-differences with multiple time periods”, Journal of Econometrics, 225(2), pp. 200–230. | Callaway, B., & Sant’Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, *225*(2), 200–230. |
| 468 | Cetorelli, N., Peristiani, S. (2013), “Prestigious stock exchanges: A network analysis of international financial centers”, Journal of Banking & Finance, 37(5), pp. 1543–1551. | Cetorelli, N., & Peristiani, S. (2013). Prestigious stock exchanges: A network analysis of international financial centers. *Journal of Banking & Finance*, *37*(5), 1543–1551. |
| 469 | Chen, K., Chen, G. (2015), “The rise of international financial centers in mainland China”, Cities, 47, pp. 10–22. | Chen, K., & Chen, G. (2015). The rise of international financial centers in mainland China. *Cities*, *47*, 10–22. |
| 470 | Christie, W. G., Huang, R. D. (1994), “Market structures and liquidity: A transactions data study of exchange listings”, Journal of Financial Intermediation, 3(3), pp. 300–326. | Christie, W. G., & Huang, R. D. (1994). Market structures and liquidity: A transactions data study of exchange listings. *Journal of Financial Intermediation*, *3*(3), 300–326. |
| 471 | Čihák, M., Demirgüç-Kunt, A., Feyen, E., Levine, R. (2012), “Benchmarking financial systems around the world”, Policy Research Working Paper 6175, World Bank, Washington, DC. | Čihák, M., Demirgüç-Kunt, A., Feyen, E., & Levine, R. (2012). *Benchmarking financial systems around the world* (Policy Research Working Paper No. 6175). World Bank. |
| 472 | Conley, T. G., Taber, C. R. (2011), “Inference with “difference in differences” with a small number of policy changes”, Review of Economics and Statistics, 93(1), pp. 113–125. | Conley, T. G., & Taber, C. R. (2011). Inference with "difference in differences" with a small number of policy changes. *The Review of Economics and Statistics*, *93*(1), 113–125. |
| 473 | Corwin, S. A., Schultz, P. (2012), “A simple way to estimate bid-ask spreads from daily high and low prices”, Journal of Finance, 67(2), pp. 719–760. | Corwin, S. A., & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *The Journal of Finance*, *67*(2), 719–760. |
| 474 | Dao, V. H., Nguyen, T. M. H., Vu, T. D. (2021), “The impact of COVID-19 on stock market returns in Vietnam”, Journal of Risk and Financial Management, 14(9), Article 441, DOI: 10.3390/jrfm14090441. | Dao, V. H., Nguyen, T. M. H., & Vu, T. D. (2021). The impact of COVID-19 on stock market returns in Vietnam. *Journal of Risk and Financial Management*, *14*(9), Article 441. https://doi.org/10.3390/jrfm14090441 |
| 475 | Daw, J. R., Hatfield, L. A. (2018), “Matching and regression to the mean in difference-in-differences analysis”, Health Services Research, 53(6), pp. 4138–4156 [CẦN XÁC MINH]. | Daw, J. R., & Hatfield, L. A. (2018). Matching and regression to the mean in difference-in-differences analysis. *Health Services Research*, *53*(6), 4138–4156. [CẦN XÁC MINH: hồ sơ chưa có bản gốc; giữ nhãn] |
| 476 | DeMiguel, V., Garlappi, L., Uppal, R. (2009), “Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy?”, Review of Financial Studies, 22(5), pp. 1915–1953. | DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? *The Review of Financial Studies*, *22*(5), 1915–1953. |
| 477 | Eichengreen, B., Shah, N. (2020), “The correlates of international financial-center status”, Review of International Economics, 28(1), pp. 62–81. | Eichengreen, B., & Shah, N. (2020). The correlates of international financial-center status. *Review of International Economics*, *28*(1), 62–81. |
| 478 | Elliott, D. J. (2011), Building a Global Financial Center in Shanghai: Observations from Other Centers, Brookings Institution, Washington, DC. | Elliott, D. J. (2011). *Building a global financial center in Shanghai: Observations from other centers*. Brookings Institution. |
| 479 | Fong, K. Y. L., Holden, C. W., Trzcinka, C. A. (2017), “What are the best liquidity proxies for global research?”, Review of Finance, 21(4), pp. 1355–1401. | Fong, K. Y. L., Holden, C. W., & Trzcinka, C. A. (2017). What are the best liquidity proxies for global research? *Review of Finance*, *21*(4), 1355–1401. |
| 480 | Garlappi, L., Uppal, R., Wang, T. (2007), “Portfolio selection with parameter and model uncertainty: A multi-prior approach”, Review of Financial Studies, 20(1), pp. 41–81. | Garlappi, L., Uppal, R., & Wang, T. (2007). Portfolio selection with parameter and model uncertainty: A multi-prior approach. *The Review of Financial Studies*, *20*(1), 41–81. |
| 481 | Gehrig, T. (2000), “Cities and the geography of financial centers”, trong Huriot, J.-M., Thisse, J.-F. (Eds.), Economics of Cities: Theoretical Perspectives, Cambridge University Press, Cambridge [CẦN BỔ SUNG số trang]. | Gehrig, T. (2000). Cities and the geography of financial centers. In J.-M. Huriot & J.-F. Thisse (Eds.), *Economics of cities: Theoretical perspectives* (pp. [CẦN BỔ SUNG số trang]). Cambridge University Press. |
| 482 | Goutte, S., Le, H.-V., Liu, F., von Mettenheim, H.-J. (2025), “MCDA strategies for portfolio optimization: A case study on Vietnamese stock market dynamics”, Annals of Operations Research, 353(1), pp. 321–351. | Goutte, S., Le, H.-V., Liu, F., & von Mettenheim, H.-J. (2025). MCDA strategies for portfolio optimization: A case study on Vietnamese stock market dynamics. *Annals of Operations Research*, *353*(1), 321–351. |
| 483 | Griffin, J. M., Kelly, P. J., Nardari, F. (2010), “Do market efficiency measures yield correct inferences? A comparison of developed and emerging markets”, Review of Financial Studies, 23(8), pp. 3225–3277. | Griffin, J. M., Kelly, P. J., & Nardari, F. (2010). Do market efficiency measures yield correct inferences? A comparison of developed and emerging markets. *The Review of Financial Studies*, *23*(8), 3225–3277. |
| 484 | Hamilton, J. D. (1989), “A new approach to the economic analysis of nonstationary time series and the business cycle”, Econometrica, 57(2), pp. 357–384. | Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle. *Econometrica*, *57*(2), 357–384. |
| 485 | Hisada, T. (2018), “The effect of investor sentiment toward an exchange merger on liquidity”, International Journal of Economics and Financial Issues, 8(2), pp. 315–318. | Hisada, T. (2018). The effect of investor sentiment toward an exchange merger on liquidity. *International Journal of Economics and Financial Issues*, *8*(2), 315–318. |
| 486 | Hoang, V.-M. D., Luu, D. T. (2024), “Modelling volatility dynamics and identifying regime switching in a frontier stock market: The case of Vietnam”, SSRN Working Paper No. 4867203, đăng 25/06/2024, sửa 17/09/2025. | Hoang, V.-M. D., & Luu, D. T. (2024). *Modelling volatility dynamics and identifying regime switching in a frontier stock market: The case of Vietnam* (SSRN Working Paper No. 4867203; bản sửa ngày 17/9/2025). SSRN. [CẦN BỔ SUNG URL hoặc DOI của bản SSRN] |
| 487 | Holm, S. (1979), “A simple sequentially rejective multiple test procedure”, Scandinavian Journal of Statistics, 6(2), pp. 65–70. | Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, *6*(2), 65–70. |
| 488 | Hou, K., Moskowitz, T. J. (2005), “Market frictions, price delay, and the cross-section of expected returns”, Review of Financial Studies, 18(3), pp. 981–1020. | Hou, K., & Moskowitz, T. J. (2005). Market frictions, price delay, and the cross-section of expected returns. *The Review of Financial Studies*, *18*(3), 981–1020. |
| 489 | Huang, R. D., Stoll, H. R. (1996), “Dealer versus auction markets: A paired comparison of execution costs on NASDAQ and the NYSE”, Journal of Financial Economics, 41(3), pp. 313–357. | Huang, R. D., & Stoll, H. R. (1996). Dealer versus auction markets: A paired comparison of execution costs on NASDAQ and the NYSE. *Journal of Financial Economics*, *41*(3), 313–357. |
| 490 | International Monetary Fund (2023), Vietnam: 2023 Article IV Consultation, IMF Country Report No. 23/338, Washington, DC, https://www.elibrary.imf.org/view/journals/002/2023/338/article-A001-en.xml (truy cập 30/09/2026). | International Monetary Fund. (2023). *Vietnam: 2023 Article IV consultation* (IMF Country Report No. 23/338). https://www.elibrary.imf.org/view/journals/002/2023/338/article-A001-en.xml |
| 491 | Kan, R., Zhou, G. (2007), “Optimal portfolio choice with parameter uncertainty”, Journal of Financial and Quantitative Analysis, 42(3), pp. 621–656. | Kan, R., & Zhou, G. (2007). Optimal portfolio choice with parameter uncertainty. *Journal of Financial and Quantitative Analysis*, *42*(3), 621–656. |
| 492 | Kaufmann, D., Kraay, A., Mastruzzi, M. (2011), “The Worldwide Governance Indicators: Methodology and analytical issues”, Hague Journal on the Rule of Law, 3(2), pp. 220–246. | Kaufmann, D., Kraay, A., & Mastruzzi, M. (2011). The Worldwide Governance Indicators: Methodology and analytical issues. *Hague Journal on the Rule of Law*, *3*(2), 220–246. |
| 493 | Kindleberger, C. P. (1974), The Formation of Financial Centers: A Study in Comparative Economic History, Princeton Studies in International Finance No. 36, Princeton University, Princeton. | Kindleberger, C. P. (1974). *The formation of financial centers: A study in comparative economic history* (Princeton Studies in International Finance No. 36). Princeton University. |
| 494 | Kritzman, M., Page, S., Turkington, D. (2012), “Regime shifts: Implications for dynamic strategies”, Financial Analysts Journal, 68(3), pp. 22–39. | Kritzman, M., Page, S., & Turkington, D. (2012). Regime shifts: Implications for dynamic strategies. *Financial Analysts Journal*, *68*(3), 22–39. |
| 495 | Lai, K. P. Y. (2012), “Differentiated markets: Shanghai, Beijing and Hong Kong in China’s financial centre network”, Urban Studies, 49(6), pp. 1275–1296. | Lai, K. P. Y. (2012). Differentiated markets: Shanghai, Beijing and Hong Kong in China’s financial centre network. *Urban Studies*, *49*(6), 1275–1296. |
| 496 | Lang, M., Lins, K. V., Maffett, M. (2012), “Transparency, liquidity, and valuation: International evidence on when transparency matters most”, Journal of Accounting Research, 50(3), pp. 729–774. | Lang, M., Lins, K. V., & Maffett, M. (2012). Transparency, liquidity, and valuation: International evidence on when transparency matters most. *Journal of Accounting Research*, *50*(3), 729–774. |
| 497 | Ledoit, O., Wolf, M. (2004), “A well-conditioned estimator for large-dimensional covariance matrices”, Journal of Multivariate Analysis, 88(2), pp. 365–411. | Ledoit, O., & Wolf, M. (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, *88*(2), 365–411. |
| 498 | Ledoit, O., Wolf, M. (2008), “Robust performance hypothesis testing with the Sharpe ratio”, Journal of Empirical Finance, 15(5), pp. 850–859. | Ledoit, O., & Wolf, M. (2008). Robust performance hypothesis testing with the Sharpe ratio. *Journal of Empirical Finance*, *15*(5), 850–859. |
| 499 | Lesmond, D. A. (2005), “Liquidity of emerging markets”, Journal of Financial Economics, 77(2), pp. 411–452. | Lesmond, D. A. (2005). Liquidity of emerging markets. *Journal of Financial Economics*, *77*(2), 411–452. |
| 500 | Lesmond, D. A., Ogden, J. P., Trzcinka, C. A. (1999), “A new estimate of transaction costs”, Review of Financial Studies, 12(5), pp. 1113–1141. | Lesmond, D. A., Ogden, J. P., & Trzcinka, C. A. (1999). A new estimate of transaction costs. *The Review of Financial Studies*, *12*(5), 1113–1141. |
| 501 | Lo, A. W., MacKinlay, A. C. (1988), “Stock market prices do not follow random walks: Evidence from a simple specification test”, Review of Financial Studies, 1(1), pp. 41–66. | Lo, A. W., & MacKinlay, A. C. (1988). Stock market prices do not follow random walks: Evidence from a simple specification test. *The Review of Financial Studies*, *1*(1), 41–66. |
| 502 | Markowitz, H. (1952), “Portfolio selection”, Journal of Finance, 7(1), pp. 77–91. | Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, *7*(1), 77–91. |
| 503 | Michaud, R. O. (1989), “The Markowitz optimization enigma: Is ‘optimized’ optimal?”, Financial Analysts Journal, 45(1), pp. 31–42. | Michaud, R. O. (1989). The Markowitz optimization enigma: Is 'optimized' optimal? *Financial Analysts Journal*, *45*(1), 31–42. |
| 504 | Moosa, I., Li, L., Jiang, R. (2016), “Determinants of the status of an international financial centre”, The World Economy, 39(12), pp. 2074–2096. | Moosa, I., Li, L., & Jiang, R. (2016). Determinants of the status of an international financial centre. *The World Economy*, *39*(12), 2074–2096. |
| 505 | Naeem, M. M. F. (2023), What makes an International Financial Centre (IFC) Competitive? An empirical study of the determinants responsible for the competitiveness of an IFC, Luận án Tiến sĩ Quản trị kinh doanh (DBA), Durham University, https://etheses.durham.ac.uk/id/eprint/15102/. | Naeem, M. M. F. (2023). *What makes an International Financial Centre (IFC) competitive? An empirical study of the determinants responsible for the competitiveness of an IFC* [Luận án Tiến sĩ Quản trị kinh doanh (DBA), Durham University]. Durham E-Theses. https://etheses.durham.ac.uk/id/eprint/15102/ |
| 506 | Nguyen, N., Nguyen, T., Tran, T., Mai, A. (2020), “Shrinkage model selection for portfolio optimization on Vietnam stock market”, Journal of Asian Finance, Economics and Business, 7(9), pp. 135–145. | Nguyen, N., Nguyen, T., Tran, T., & Mai, A. (2020). Shrinkage model selection for portfolio optimization on Vietnam stock market. *The Journal of Asian Finance, Economics and Business*, *7*(9), 135–145. |
| 507 | Nguyen, T. B., Nguyen, V. T. (2026a), “Black-Litterman portfolio optimization using regime switching CAPM and ABC-MCMC: Empirical evidence from the Vietnamese stock market period 2019 - 2025”, Tạp chí Nghiên cứu Chính sách và Phát triển (Journal of Policy and Development Research), 3(1), pp. 81–99, DOI: 10.63640/3030-4091/jpd.apd.194. | Nguyễn, T. B., & Nguyễn, V. T. (2026a). Black-Litterman portfolio optimization using regime switching CAPM and ABC-MCMC: Empirical evidence from the Vietnamese stock market period 2019–2025. *Tạp chí Nghiên cứu Chính sách và Phát triển*, *3*(1), 81–99. https://doi.org/10.63640/3030-4091/jpd.apd.194 (Nếu giữ hai phần danh mục thì chuyển mục này sang ngay trước idx 454, vì tạp chí là tạp chí trong nước, để 2026a và 2026b đứng liền nhau.) |
| 508 | Nielsson, U. (2009), “Stock exchange merger and liquidity: The case of Euronext”, Journal of Financial Markets, 12(2), pp. 229–267. | Nielsson, U. (2009). Stock exchange merger and liquidity: The case of Euronext. *Journal of Financial Markets*, *12*(2), 229–267. |
| 509 | OECD (2008), Handbook on Constructing Composite Indicators: Methodology and User Guide, OECD Publishing, Paris. | OECD. (2008). *Handbook on constructing composite indicators: Methodology and user guide*. OECD Publishing. |
| 510 | Pflug, G. C., Pichler, A., Wozabal, D. (2012), “The 1/N investment strategy is optimal under high model ambiguity”, Journal of Banking & Finance, 36(2), pp. 410–417. | Pflug, G. C., Pichler, A., & Wozabal, D. (2012). The 1/N investment strategy is optimal under high model ambiguity. *Journal of Banking & Finance*, *36*(2), 410–417. |
| 511 | Politis, D. N., Romano, J. P. (1994), “The stationary bootstrap”, Journal of the American Statistical Association, 89(428), pp. 1303–1313. | Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. *Journal of the American Statistical Association*, *89*(428), 1303–1313. |
| 512 | Rambachan, A., Roth, J. (2023), “A more credible approach to parallel trends”, Review of Economic Studies, 90(5), pp. 2555–2591. | Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. *The Review of Economic Studies*, *90*(5), 2555–2591. |
| 513 | Ta, B. Q., Vuong, T. (2020), “The Black-Litterman model for portfolio optimization on Vietnam stock market”, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 28(Supp01), pp. 99–111. | Ta, B. Q., & Vuong, T. (2020). The Black-Litterman model for portfolio optimization on Vietnam stock market. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, *28*(Supp01), 99–111. |
| 514 | VietnamPlus (2026a), “Ho Chi Minh City jumps 17 places in Global Financial Centres Index”, https://en.vietnamplus.vn/ho-chi-minh-city-jumps-17-places-in-global-financial-centres-index-post352894.vnp. | VietnamPlus. (2026a, [CẦN BỔ SUNG ngày đăng]). Ho Chi Minh City jumps 17 places in Global Financial Centres Index. *VietnamPlus*. https://en.vietnamplus.vn/ho-chi-minh-city-jumps-17-places-in-global-financial-centres-index-post352894.vnp |
| 515 | VietnamPlus (2026b), “Vietnam International Financial Centre in Da Nang ranked 71st globally”, https://en.vietnamplus.vn/vietnam-international-financial-centre-in-da-nang-ranked-71st-globally-post352933.vnp. | VietnamPlus. (2026b, [CẦN BỔ SUNG ngày đăng]). Vietnam International Financial Centre in Da Nang ranked 71st globally. *VietnamPlus*. https://en.vietnamplus.vn/vietnam-international-financial-centre-in-da-nang-ranked-71st-globally-post352933.vnp |
| 516 | Vo, X. V., Phan, D. B. A. (2017), “Further evidence on the herd behavior in Vietnam stock market”, Journal of Behavioral and Experimental Finance, 13, pp. 33–41. | Vo, X. V., & Phan, D. B. A. (2017). Further evidence on the herd behavior in Vietnam stock market. *Journal of Behavioral and Experimental Finance*, *13*, 33–41. |
| 517 | Vu, T. L., Luong, N. H., Nguyen, P. N. (2024), “Stock crash and how it spreads over the Vietnamese stock market”, VNU Journal of Economics and Business, 4(3), pp. 107–116, DOI: 10.57110/vnu-jeb.v4i3.339. | Vu, T. L., Luong, N. H., & Nguyen, P. N. (2024). Stock crash and how it spreads over the Vietnamese stock market. *VNU Journal of Economics and Business*, *4*(3), 107–116. https://doi.org/10.57110/vnu-jeb.v4i3.339 |
| 518 | Wang, D. T., Zhao, S. X., Wang, D. (2007), “‘Information hinterland’: A base for financial centre development. The case of Beijing versus Shanghai in China”, Tijdschrift voor Economische en Sociale Geografie, 98(1), pp. 102–120. | Wang, D. T., Zhao, S. X., & Wang, D. (2007). "Information hinterland": A base for financial centre development. The case of Beijing versus Shanghai in China. *Tijdschrift voor Economische en Sociale Geografie*, *98*(1), 102–120. |
| 519 | Wójcik, D. (2007), “Geography and the future of stock exchanges: Between real and virtual space”, Growth and Change, 38(2), pp. 200–223. | Wójcik, D. (2007). Geography and the future of stock exchanges: Between real and virtual space. *Growth and Change*, *38*(2), 200–223. |
| 520 | Yao, J.-M. (2012), Compétitivité et attractivité des places financières internationales: Application à l’industrie des fonds d’investissement au Luxembourg, Luận án tiến sĩ Kinh tế học, Université de Strasbourg, Strasbourg. | Yao, J.-M. (2012). *Compétitivité et attractivité des places financières internationales: Application à l’industrie des fonds d’investissement au Luxembourg* [Luận án tiến sĩ Kinh tế học, Université de Strasbourg]. |

**Đối chiếu hai chiều:** đạt (xem checklist 1e). Sau khi thêm NQ 57 thì có 69 mục, và NQ 57 được trích ở mục (7).

**Daw và Hatfield (2018):** hồ sơ không có bản gốc, nên giữ nhãn [CẦN XÁC MINH] (mục 8, C7).

---

## (6) Bảng 20 nhãn [CẦN ...]

| # | idx | Nhãn hiện có | Giải được bằng hồ sơ? | Chuỗi thay thế, hoặc tài liệu còn cần |
|---|---|---|---|---|
| 1 | 79 | [CẦN ĐỐI CHIẾU báo cáo gốc] (GFCI 40: TP.HCM 67/117, Đà Nẵng 71) | Không. Chỉ xác nhận được GFCI 40 vào tháng 9/2026 (B14) | Cần báo cáo GFCI 40 (B2). Giữ nhãn. |
| 2 | 79 | [CẦN XÁC MINH văn bản hoặc kế hoạch của VNX về UPCoM] | Một phần: căn cứ pháp lý của kế hoạch là khoản 4 Điều 4 (A5) | Thay nhãn bằng: "[CẦN XÁC MINH kế hoạch chuyển cổ phiếu đăng ký giao dịch do VNX xây dựng và báo cáo Ủy ban Chứng khoán Nhà nước theo khoản 4 Điều 4 Thông tư số 57/2021/TT-BTC]". Cần văn bản A1. |
| 3 | 80 | [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh] | Không (Naeem chỉ xác nhận vế "chưa có sở giao dịch") | Cần B3. Nếu không tìm được, xóa vế "và chỉ có sở giao dịch tầm quốc gia từ năm 2021 [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh]" và giữ vế có nguồn Naeem. |
| 4 | 81 | [CẦN ĐỐI CHIẾU danh sách VNX] ("khoảng 300") | Không | Cần A2. |
| 5 | 93 | [CẦN XÁC MINH nguồn] (Pakistan 2016) | **Có, nếu thay ví dụ.** Hisada trích Arnold và cộng sự (1999) | Chuỗi gốc: "Bằng chứng về hợp nhất các sàn trong một quốc gia ở thị trường mới nổi còn ít, ví dụ trường hợp Pakistan hợp nhất ba sở giao dịch năm 2016 [CẦN XÁC MINH nguồn], và chưa đo khả năng đầu tư." → "Bằng chứng về hợp nhất các sàn trong một quốc gia chủ yếu đến từ thị trường phát triển, chẳng hạn việc hợp nhất các sàn khu vực ở Mỹ làm thanh khoản tăng nhờ lợi thế quy mô (Arnold và cộng sự, 1999, dẫn theo Hisada, 2018); bằng chứng ở thị trường mới nổi còn ít và chưa đo khả năng đầu tư." Chỉ Hisada (2018) nằm trong danh mục (trích thứ cấp theo APA). Nếu sau này tìm được Arnold và cộng sự (1999) (C1) thì trích trực tiếp. |
| 6 | 186 | [CẦN XÁC MINH theo từng thời kỳ] (biên độ) | Không | Cần A5. Giữ nhãn: biên độ thay đổi trong giai đoạn mẫu 2009–2025 ảnh hưởng trực tiếp tới H2. |
| 7 | 188 | [CẦN XÁC MINH] (giấy phép Long Finance) | **Có (viết lại thành câu kế hoạch)** | Chuỗi gốc: "thí sinh liên hệ Long Finance về giấy phép dùng bộ dữ liệu lịch sử [CẦN XÁC MINH]." → "thí sinh sẽ xin phép Long Finance dùng bộ dữ liệu lịch sử trước khi phân tích; nếu không được phép, phương án dự phòng thứ nhất ở mục 4.3.10 được áp dụng." |
| 8 | 188 | [CẦN XÁC MINH nguồn và điều khoản sử dụng] (thời điểm công bố báo cáo tài chính) | **Có (viết lại thành câu kế hoạch, khớp Bảng 5 năm 1 quý 1)** | Chuỗi gốc: "Dữ liệu minh bạch gồm thời điểm công bố báo cáo tài chính [CẦN XÁC MINH nguồn và điều khoản sử dụng]." → "Dữ liệu minh bạch gồm thời điểm công bố báo cáo tài chính theo quý, lấy từ trang công bố thông tin của HNX và HOSE hoặc từ nhà cung cấp dữ liệu thương mại; nguồn, điều khoản sử dụng và hạn công bố theo quy định được xác nhận trong quý 1 năm thứ nhất (Bảng 5)." Hạn công bố pháp lý vẫn cần A10. |
| 9 | 224 | [CẦN XÁC MINH phạm vi sàn của từng bài] | Không. Chỉ có tên bài: 2026a "Vietnamese stock market period 2019 - 2025"; bản thảo 5 "Vietnamese stock market liquidity"; bản thảo 7 "Vietnam’s FTSE Russell reclassification" | Người dùng tự xác nhận (E1). |
| 10 | 224 | [CẦN XÁC NHẬN] (góp ý của người hướng dẫn cho đăng ký trước) | Không | Người dùng xác nhận (E2). Nếu chưa có thì viết: "thí sinh dự kiến xin góp ý của người hướng dẫn trước khi đăng ký" và bỏ nhãn. |
| 11 | 227 | [CẦN XÁC MINH dữ liệu lệnh] | **Có (dùng thước đo đã có trong đề cương)** | Chuỗi gốc: "gồm phí giao dịch, thuế và một nửa chênh lệch giá chào mua và chào bán đóng cửa [CẦN XÁC MINH dữ liệu lệnh]," → "gồm phí giao dịch, thuế và một nửa chênh lệch giá chào mua và chào bán, lấy từ giá chào đóng cửa nếu nhà cung cấp dữ liệu có, nếu không thì dùng chênh lệch ước lượng từ giá cao nhất và thấp nhất theo tháng (Corwin & Schultz, 2012)," |
| 12 | 275 | [CẦN XÁC MINH] (WFE thay GFDD sau năm 2021) | **Có (câu điều kiện đã là kế hoạch)** | Chuỗi gốc: "đề tài dùng số liệu của Liên đoàn các Sở Giao dịch Thế giới [CẦN XÁC MINH]." → "đề tài dùng số liệu của Liên đoàn các Sở Giao dịch Thế giới, sau khi kiểm tra độ phủ và điều khoản sử dụng." Việc kiểm tra độ phủ vẫn cần D4. |
| 13 | 277 | [CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn] | Một phần (QĐ 737 mục 2.3, A14) | Giữ nhãn; cần A4 và A2. |
| 14 | 277 | [CẦN XÁC MINH các mốc FTSE và phân bảng] | Không | Cần B1 và A6. |
| 15 | 278 | [CẦN XÁC NHẬN với người hướng dẫn] (ý kiến chuyên gia) | **Có (viết lại thành câu kế hoạch)** | Chuỗi gốc: "Nếu được các tổ chức đồng ý, thí sinh lấy ý kiến chuyên gia không chính thức [CẦN XÁC NHẬN với người hướng dẫn]." → "Nếu người hướng dẫn và các tổ chức liên quan đồng ý, thí sinh lấy ý kiến chuyên gia không chính thức." |
| 16 | 286 | [CẦN XÁC MINH danh sách nhân tố từng kỳ] | **Có (đây là bước kiểm tra dự kiến, không phải khẳng định)**; Naeem 4.4.18 xác nhận có nhân tố khối lượng giao dịch (B9) | Chuỗi gốc: "nếu trùng lặp ở phần lớn các kỳ, kết quả H1 được trình bày như liên hệ mô tả [CẦN XÁC MINH danh sách nhân tố từng kỳ]." → "nếu trùng lặp ở phần lớn các kỳ, kết quả H1 được trình bày như liên hệ mô tả." Danh sách nhân tố vẫn cần B2 khi thực hiện. |
| 17 | 295 | [CẦN XÁC MINH] (người dùng dự kiến) | **Có**, vì câu đã nói là "dự kiến" | Chuỗi gốc: "Ủy ban Chứng khoán Nhà nước, HNX, HOSE và các tổ chức đầu tư [CẦN XÁC MINH]." → "Ủy ban Chứng khoán Nhà nước, HNX, HOSE và các tổ chức đầu tư." Nếu muốn nói có thư xác nhận của các tổ chức này thì phải có thư (E2). |
| 18 | 456 | [CẦN XÁC MINH số hiệu và ngày trên bản gốc] | Một phần: tháng 9/2026, sau ngày 25/9/2026 (A15) | Thu hẹp nhãn như ở mục (5). Cần A4. |
| 19 | 475 | [CẦN XÁC MINH] (Daw và Hatfield, 2018) | Không | Cần C7. Giữ nhãn. |
| 20 | 481 | [CẦN BỔ SUNG số trang] (Gehrig, 2000) | Không | Cần C9. Giữ nhãn. |

Tổng kết: 8 nhãn gỡ được bằng cách viết lại (#5, 7, 8, 11, 12, 15, 16, 17). 3 nhãn thu hẹp được (#2, 13, 18). 9 nhãn cần tài liệu hoặc xác nhận của người dùng (#1, 3, 4, 6, 9, 10, 14, 19, 20). Ngoài ra, m2 thêm 1 nhãn mới (thông báo gốc của VNX) và mục (7) thêm 2 nhãn mới.

---

## (7) Câu MJ6 (người dùng đã quyết: cam kết học tập trung toàn thời gian)

Căn cứ (bản chép NQ 57 trong `doi-chieu-bai-toan-19.md`, mục a.1; bậc 4):
- Điều 11 khoản 3: "Theo học chương trình đào tạo tiến sĩ và tương đương, tập trung toàn thời gian, có chuyên ngành đào tạo và nội dung nghiên cứu của luận án tiến sĩ phục vụ giải quyết bài toán lớn của Thành phố…".
- Điều 13: "…không vượt quá 48 tháng."
- Ngày ban hành 15/6/2026; Điều 34 khoản 1: hiệu lực từ 01/7/2026.

**Vị trí đúng.** Mục 8.2 gồm idx 440 (tiêu đề), 441 và 442. Câu về các chương trình học song song nằm ở **idx 441**. idx 328 thuộc **mục 6**, không phải 8.2, và chỉ là chỗ thêm tùy chọn. idx 337 thuộc mục 7.4.

**(a) Bắt buộc: idx 441, mục 8.2.** Chuỗi gốc: "và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 07/2026."
→ "và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 7/2026. Nếu trúng tuyển, thí sinh cam kết theo học chương trình đào tạo tiến sĩ theo hình thức tập trung toàn thời gian, đáp ứng điều kiện tại khoản 3 Điều 11 Nghị quyết số 57/2026/NQ-HĐND (Hội đồng nhân dân thành phố Hà Nội, 2026), và trước khi nhập học sẽ sắp xếp các chương trình đang theo học nêu trên để không trùng với thời gian học tập và nghiên cứu tập trung [CẦN XÁC NHẬN phương án cụ thể với từng chương trình: hoàn thành, bảo lưu hoặc dừng học]."

**(b) Nên có: idx 337, mục 7.4.** Chuỗi gốc: "Thời gian đào tạo đối với người có bằng đại học là bốn năm."
→ "Thời gian đào tạo đối với người có bằng đại học là bốn năm, theo hình thức tập trung toàn thời gian; thời gian này không vượt quá 48 tháng, là thời gian hỗ trợ tối đa theo Điều 13 Nghị quyết số 57/2026/NQ-HĐND (Hội đồng nhân dân thành phố Hà Nội, 2026)."

**(c) Tùy chọn: idx 328, mục 6.** Chuỗi gốc: "đúng vào thời điểm thị trường vốn Hà Nội thay đổi cấu trúc."
→ "đúng vào thời điểm thị trường vốn Hà Nội thay đổi cấu trúc. Thí sinh đề nghị được xét hỗ trợ theo Nghị quyết số 57/2026/NQ-HĐND với đề tài gắn bài toán số 19 [CẦN XÁC MINH danh mục bài toán lớn áp dụng khi xét hỗ trợ]."
Lý do giữ nhãn: NQ 57 Điều 35 khoản 1 điểm c giao UBND ban hành danh mục bài toán lớn, nhưng không nói danh mục đó là QĐ 1193 (ban hành trước NQ 57) hay một danh mục mới.

**(d) Mục danh mục (đặt theo thứ tự chữ cái, sau "Hoang" và trước "Holm" nếu gộp một danh mục; nếu giữ hai phần thì đặt trong "Tài liệu tiếng Việt", sau "Bộ Tài chính (2025)").**
- Bản APA 7: "Hội đồng nhân dân thành phố Hà Nội. (2026). *Nghị quyết số 57/2026/NQ-HĐND ngày 15/6/2026* [CẦN BỔ SUNG trích yếu đầy đủ theo bản chính]."
- Nếu giữ kiểu trình bày hiện tại của danh mục: "Hội đồng nhân dân thành phố Hà Nội (2026), Nghị quyết số 57/2026/NQ-HĐND ngày 15/6/2026 [CẦN BỔ SUNG trích yếu đầy đủ theo bản chính]."

Lý do nhãn: hồ sơ chỉ có tên Mục 1 Chương III ("CHÍNH SÁCH HỖ TRỢ NGHIÊN CỨU SINH ĐI HỌC TẬP TẠI CÁC CƠ SỞ ĐÀO TẠO TRONG NƯỚC ĐỂ GIẢI QUYẾT BÀI TOÁN LỚN CỦA THÀNH PHỐ"), không có trích yếu của cả Nghị quyết. Bản chép là bản đọc từ ảnh scan sao y và chưa đối chiếu từng ký tự, nên cần soát với bản giấy trước khi trích (A8).

---

## (8) Tài liệu cần tìm (chỉ mục mới hoặc mục đổi trạng thái so với `danh-sach-tai-lieu-can-tim-r8.md`)

| # | Tài liệu | Trạng thái mới / lý do | Dùng ở (idx) | Ưu tiên |
|---|---|---|---|---|
| A2 | Thông báo gốc của VNX ngày 30/9/2026 | **Thêm lý do:** m2 thêm nhãn [CẦN ĐỐI CHIẾU thông báo gốc của VNX] ở idx 79 | 79, 81, 277 | CAO |
| A4 | QĐ 737/QĐ-SGDHCM | **Đổi trạng thái:** đã biết tháng 9/2026 và ngày ký không sớm hơn 25/9/2026 (căn cứ Công văn 1314/SGDVN-CLPT ngày 25/9/2026). Vẫn cần số hiệu và ngày trên bản gốc | 277, 456 | CAO |
| A7 | Công báo NQ 222/2025/QH15 | **Hạ ưu tiên** nếu chọn bỏ ngày ở idx 455 (m4a) | 455 | THẤP |
| A8 | Bản chính NQ 57/2026/NQ-HĐND | **Đổi trạng thái:** người dùng đã quyết MJ6. Nay cần (i) **trích yếu đầy đủ** cho mục danh mục, (ii) soát Điều 11, 13 với bản giấy, (iii) xác định danh mục bài toán áp dụng (Điều 35) | 328, 337, 441, danh mục | CAO |
| A12 (mới) | Văn bản hoặc thông báo khai trương thị trường UPCoM (tháng 6/2009) | Mốc bắt đầu mẫu ở idx 189 và 292 chưa có nguồn | 189, 292 | THẤP |
| B2 | Báo cáo GFCI 40 và các kỳ trước | **Thêm:** xác nhận đơn vị công bố từng kỳ (Z/Yen từ năm 2007; cùng CDI từ năm 2015) cho m1 | 79, 188, 275, 286 | CAO |
| C1 | Arnold, Hersch, Mulherin & Netter (1999) | **Thêm lý do:** cho phép gỡ nhãn Pakistan (nhãn #5) bằng trích dẫn trực tiếp thay cho trích thứ cấp | 93 | CAO |
| C3 | Nielsson (2009), toàn văn | **Thêm lý do:** vế "không tăng ở doanh nghiệp nhỏ" (idx 81) hiện chỉ có nguồn thứ cấp (B6) | 81, 108 | TB |
| C12 (mới) | Vo & Phan (2017); Nguyen và cộng sự (2020); Goutte và cộng sự (2025); Ta & Vuong (2020): kiểm số liệu mẫu và thông tin xuất bản | Số "299 công ty, 2005–2015" và "468 tuần, 2011–2019" chưa có trong hồ sơ (B18) | 95, 482, 506, 513 | THẤP |
| C13 (mới) | DOI của các bài tạp chí trong danh mục chưa có DOI (đối chiếu Crossref) | APA 7 yêu cầu DOI khi có. Phase 2.5 của citation-management chưa làm được vì không tra web; không thêm DOI từ trí nhớ | 460–520 | TB |
| C14 (mới) | Ngày đăng của VietnamPlus 2026a, 2026b và bài của Thời báo Tài chính Việt Nam; URL hoặc DOI SSRN của Hoang và Luu (2024) | m13; APA 7 cho bài báo trực tuyến và working paper | 457, 486, 514, 515 | THẤP |
| E1 | Phạm vi dữ liệu bài 2026a và các bản thảo số 5, 7 | Không đổi (nhãn #9) | 224 | CAO |
| E3 | MJ6 | **Đổi trạng thái: ĐÃ QUYẾT** (cam kết học tập trung toàn thời gian). Còn lại: phương án cụ thể với từng chương trình đang học (nhãn mới ở idx 441) | 441 | CAO |
