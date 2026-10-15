# Phản biện độc lập vòng 5: Đề cương "Hợp nhất sàn chứng khoán và trung tâm tài chính Hà Nội: Chất lượng thị trường và khả năng đầu tư quanh việc chuyển cổ phiếu HNX sang HOSE"

Người phản biện: Claude, tác tử phản biện độc lập, không tham gia viết đề cương. Ngày: 15/10/2026.
Bản được phản biện: `scratchpad/r5/v5.md` (markdown, phương trình TeX) và `scratchpad/r5/v5-libreoffice.pdf` (đã xem Hình 1–3 ở trang 7, 13 và 15 của PDF).
Đây là bản nháp làm việc. Người dùng và người hướng dẫn chịu trách nhiệm cuối cùng, nên cần kiểm lại mọi vị trí, số liệu và nguồn trước khi sửa.

Quy ước: "dòng" là số dòng trong `v5.md`. Mã nguyên tắc: **PR** (peer-review), **RG** (research-grants), **SW** (scientific-writing), **SCW** (sciwrite, Pass 1–5), **M#/S#** (bộ lọc máy móc và bộ lọc ngữ nghĩa của paper-writing-vn), **EW** (econ-write), **CC** (credible-claims), **MHE** (mhe-identification, chế độ Critic), **SP** (statistical-power), **CK** (consistency-checker, mục 1–10), **FC** (fact-checker).

**Tổng hợp: 3 CRITICAL, 11 MAJOR, 16 MINOR, 5 mục Chờ duyệt.** Vòng 4 có 19 lỗi C/M. Trong số đó, 13 lỗi đã sửa, 5 lỗi sửa một phần, và 1 lỗi không còn áp dụng vì thiết kế đã đổi. Không lỗi C/M nào bị bỏ nguyên.

---

## 1. Trạng thái các lỗi vòng 4

| Mã | Nội dung vòng 4 | Trạng thái | Ghi chú kiểm chứng (vị trí trong v5) |
|---|---|---|---|
| C1 | HNX niêm yết chấm dứt từ 28/12/2026 | **Đã sửa** | Sự kiện chuyển sàn thành trung tâm của đề cương (dòng 182–190, 4.3.7–4.3.8). Phạm vi sau 2026 ghi rõ là UPCoM và HOSE (dòng 539–540, 738–740, 828). |
| C2 | H2/H3 là giả thuyết ghép đôi | **Đã sửa** | Bốn giả thuyết đơn (Bảng 2). Phân tích theo giai đoạn căng thẳng và theo quy mô được ghi là mô tả (dòng 457–459). |
| C3 | Phân rã quy phần dư cho "độ sâu" | **Đã sửa, còn tàn dư** | Bỏ phân rã tuần tự và bỏ "độ sâu". Tuy vậy, dòng 411–413 và 728–731 vẫn giữ lập luận "phần khoảng cách thuộc về sàn, phần còn lại thuộc về doanh nghiệp" (xem MJ4). |
| C4 | MQ ở (5) khác cấu trúc với Chỉ số ở (1) | **Đã sửa** | Đổi thành *SMD*~c(i),t−1~, có định nghĩa c(i) và câu "không được quy đổi" (dòng 705–711). Câu "xếp thứ tự ưu tiên" đã bị xóa. |
| M1 | Khả thi dữ liệu GFCI | **Sửa một phần** | Đã nêu nguồn số hóa, điểm z theo kỳ, cách gán năm sang kỳ và cảnh báo về nhân tố đầu vào (dòng 476–480, 703–713). Chưa xử lý ý (v): độ phủ của chuỗi chỉ báo thị trường cổ phiếu trong Cơ sở dữ liệu Phát triển Tài chính Toàn cầu sau 2021. Ký hiệu "t−1" cũng chưa khớp với quy tắc gán năm (m3). |
| M2 | GFCI cũ; Nghị quyết 222 | **Đã sửa** | Dòng 177–182. Fact-checker xác nhận các số 67/117, 692 điểm và Đà Nẵng 71 trên báo chí (mục 5). |
| M3 | Công suất so sánh theo giai đoạn | **Sửa một phần** | Phần này đã hạ xuống mô tả. Lý do ở dòng 766 ("đợt 2008–2009 chủ yếu nằm trong cửa sổ ước lượng") là tàn dư của v4: dữ liệu v5 bắt đầu từ 6/2009 (xem MJ11). |
| M4 | Khác biệt thể chế, biên độ, chọn lọc | **Sửa một phần** | Đã nêu biên độ ±7%/±10% cho H2 và "tác động gộp" cho H3. Còn thiếu ba điểm: biên độ và bước giá tác động cơ học lên chính biến kết quả của H3 (MJ3); biên độ ±15% của UPCoM, tức nhóm đối chứng; quy tắc gán sàn cho các mã tự chuyển sàn trước năm 2026 khi tính H2. |
| M5 | Câu hỏi 3 dùng ngôn ngữ phản thực | **Đã sửa** | Câu hỏi 3 hiện là câu hỏi nhân quả có thiết kế khác biệt kép đi kèm (dòng 239–241). |
| M6 | Thuật ngữ "khả năng đầu tư" | **Sửa một phần** | Đã phân biệt với nghĩa giới hạn sở hữu (dòng 171–173). Định nghĩa "khả năng đầu tư của một sàn … rổ cổ phiếu thanh khoản nhất của sàn đó" (dòng 168–171) lại không khớp với cách đo ở H4, vốn dùng rổ CS cố định và rổ HOSE ghép (MJ5). |
| M7 | Đặc tả (2)–(4) | **Đã sửa** | Tần suất tuần, quy năm ×52, chi phí = c × vòng quay, bootstrap trên lợi suất tuần, tập M và chỉ số k (dòng 617–623, 689–691). "Tái cân bằng hằng tháng" trong cửa sổ 3 tháng vẫn chưa rõ là ước lượng lại trọng số hay chỉ đưa trọng số về mức mục tiêu (m4). |
| M8 | Biện minh chỉ báo | **Đã sửa** | Dòng 511–518. |
| M9 | Quy tắc ghép của đối sánh tuần tự | **Không còn áp dụng; vấn đề mới** | Phân rã tuần tự đã bỏ. Quy tắc ghép của rổ HOSE cho H4 đã có (dòng 643–645), nhưng nhóm đối chứng HOSE của H3 chưa có quy tắc ghép (MJ10). |
| M10 | Tỷ số Sharpe giảm phát | **Đã sửa** | Đã bỏ. Dòng 693–694 viết đúng. |
| M11 | Mức khớp bài toán 19 | **Đã sửa** | Dòng 156–161 và 826–839. Còn một chỗ kéo dãn mới ở hàm ý chuyên môn hóa (MJ6). |
| M12 | Phương án dự phòng không khớp | **Đã sửa** | 4.3.10 và 7.4 cùng nêu ba phương án. Thiếu phương án cho trường hợp sự kiện bị lùi (MJ7). |
| M13 | Rủi ro đăng ký trước | **Đã sửa** | Dòng 594–600. Thời điểm đăng ký vẫn là vấn đề (MJ8). |
| M14 | Hình 1 không khớp | **Đã sửa** | Hình 1 đã vẽ lại. Còn một mũi tên chưa được giải thích (m6). |
| M15 | Tiêu chí mẫu | **Đã sửa** | Dòng 493–496. |

Các lỗi MINOR vòng 4:

| Mã | Trạng thái | Ghi chú |
|---|---|---|
| m1 (viết đầy đủ chữ viết tắt) | Một phần | HOSE, HNX, UPCoM đã viết đầy đủ. MQI chưa được giải nghĩa. Chưa có danh mục chữ viết tắt. |
| m2 (J, trọng số) | Đã sửa | Dòng 530–532. |
| m3 (ký hiệu) | Một phần | `\sum_{m \in M}^{}` ở (4) vẫn còn chỉ số trên rỗng. λ′ đã có định nghĩa véc-tơ W. |
| m4, m5, m6, m7, m8, m10, m12, m13, m18 | Đã sửa | |
| m9 (câu văn trong Hình 2) | Chưa sửa | PDF trang 13: "Mỗi cửa sổ đánh giá: tính lợi suất tương đương…" vẫn nằm trong hình. |
| m11 (đoạn đặt sai chỗ) | Chưa sửa | "Đóng góp dự kiến." và "Về sản phẩm" vẫn ở 4.4 (dòng 815–834). Nhãn "Từ bằng chứng đến định hướng cho Hà Nội." vẫn chạy liền, chưa định dạng, và nằm trong 4.3.8 vốn mang tên "Thiết kế khác biệt kép". |
| m14 (câu dài) | Một phần | Vẫn còn 40 câu trên 45 âm tiết (m9 dưới đây). |
| m15 (gạch nối) | Một phần | Black-Litterman đã sửa. Còn "mua--bán" (dòng 274, 435, 446, 510), "Moore--Penrose" (dòng 592), "phiếu--tháng" (dòng 665). |
| m16 (số liệu thứ cấp) | Một phần | Naeem đã gắn nhãn [CẦN ĐỌC TOÀN VĂN]. |
| m17 (mục lục) | Chưa sửa | Mục lục vẫn bắt đầu từ mục 4. |

---

## 2. Lỗi mới

### 2.1. CRITICAL

**CR1. H4 không kiểm định được như cách đang thiết kế: chi phí cố định đã tắt kênh thanh khoản, còn công suất gần bằng 0.**
- *Vị trí:* 4.3.6 (dòng 617–655), 4.3.7 (dòng 687–689), 4.3.10 (dòng 763–765), Bảng 2 (H4).
- *Mô tả:*
  1. *Cơ chế bị chặn.* Chi phí giao dịch bằng "tỷ lệ cố định c nhân với vòng quay danh mục và không lấy từ các chỉ báo của Chỉ số chất lượng" (dòng 622–623). Vì c không đổi theo sàn và theo thời gian, việc chuyển sàn không thể làm *U* tăng qua kênh chi phí. Đây lại là kênh duy nhất mà khung lý thuyết (dòng 384–389) và H3 nối "thanh khoản tốt hơn" với "khả năng đầu tư tốt hơn". Khi đó H4 chỉ còn đo thay đổi của trung bình và phương sai lợi suất giữa hai rổ. Cách sửa M7 vòng 4 đúng cho H2 (tránh trùng chỉ báo), nhưng khi áp nguyên cho H4 thì nó cắt mất cơ chế của H4.
  2. *Công suất.* Thành phần μ của (2) được ước lượng từ 13 lợi suất tuần rồi nhân 52. Phản biện tính tay theo kịch bản sau: biến động tuần của mỗi rổ 2,5–3,5%, tương quan giữa hai rổ 0,6–0,9, 23 cửa sổ trước và 8 cửa sổ sau, các cửa sổ độc lập. Khi đó độ lệch chuẩn của *G*~t~ khoảng 16–45 điểm phần trăm mỗi năm. Hiệu ứng nhỏ nhất phát hiện được (công suất 80%) là **18–52 điểm %/năm ở α = 5%** và **22–62 điểm %/năm ở mức Holm chặt nhất α = 1,25%** (bảng ở mục 4.3). Hiệu ứng hợp lý của việc đổi sàn lên lợi suất tương đương chắc chắn chỉ ở mức vài điểm %/năm. Amihud và cộng sự (1997) ghi nhận mức tăng giá một lần khoảng 5,5%, và mức tăng này rơi vào quý 4/2026, tức quý đã bị loại. Đề cương hứa "tính trước hiệu ứng nhỏ nhất phát hiện được" (dòng 653–655) nhưng chưa cho người đọc thấy rằng con số đó lớn hơn hiệu ứng hợp lý cả một bậc độ lớn.
  3. *Hệ quả cho họ Holm.* Một giả thuyết gần như không có công suất vẫn được xếp vào họ kiểm định xác nhận. Điều này làm Holm chặt hơn cho H1–H3 mà H4 không có cơ hội đóng góp gì.
- *Phát hiện bởi:* SP (MDE tính tay, mục 4.3), MHE (bước 3: thiết kế khử thành phần nào), PR (bước 5.4 công suất), CC (ngôn ngữ vượt bằng chứng).
- *Cách sửa trong phạm vi đã chốt (giữ bảy mô hình):* (a) Thêm cấu hình chi phí thứ hai, trong đó chi phí theo cổ phiếu và theo tháng lấy từ một nguồn độc lập với Chỉ số chất lượng, ví dụ biểu phí và thuế giao dịch cộng nửa chênh lệch giá chào mua–chào bán đóng cửa nếu có dữ liệu. Câu viết lại cho dòng 622–623: "Đề tài dùng hai cấu hình chi phí. Cấu hình A dùng tỷ lệ cố định c và chỉ đo kênh lợi suất–rủi ro. Cấu hình B dùng chi phí theo cổ phiếu và theo tháng, lấy từ [nguồn], và đo thêm kênh chi phí giao dịch. H~4~ được kiểm định trên cấu hình B; cấu hình A là phân tích so sánh." (b) Thêm vào 4.3.10 câu nêu thẳng con số: "Với 23 và 8 cửa sổ 13 tuần, hiệu ứng nhỏ nhất phát hiện được ước tính trên 15 điểm phần trăm mỗi năm; vì vậy kết quả H~4~ được đọc chủ yếu qua khoảng tin cậy, và kết luận 'không thu hẹp' chỉ được rút ra khi khoảng tin cậy loại trừ mức thu hẹp có ý nghĩa kinh tế." (c) Phương án đưa H4 ra khỏi họ Holm nằm ở mục Chờ duyệt (P1).

**CR2. Suy luận cho H3 đặt sai mức: việc chuyển sàn được gán cho một sàn tại một ngày, nhưng sai số chuẩn lại phân cụm theo cổ phiếu. Câu "H3 có công suất cao vì dùng khoảng 299 cổ phiếu" vì vậy sai.**
- *Vị trí:* dòng 678–680, 760–763, phương trình (5).
- *Mô tả:* Biến xử lý *D*~i~·*Post*~t~ thay đổi ở cấp "sàn × ngày", tức chỉ có một lần thay đổi chính sách. Phần nhiễu quan trọng là cú sốc chung theo tháng tác động lên cả nhóm cổ phiếu chuyển sàn so với nhóm đối chứng. Ví dụ là dòng vốn theo quy mô hoặc theo ngành, hay tâm lý với các mã "gốc HNX". Phân cụm theo cổ phiếu chỉ xử lý tương quan chuỗi trong từng mã. Nó không xử lý được cú sốc chung, nên đánh giá độ chính xác quá cao (Conley và Taber, 2011; nguyên tắc "phân cụm ở cấp gán xử lý"). Phản biện đã tính tay với kịch bản sau: độ lệch chuẩn tháng của chênh lệch log Amihud bình quân giữa nhóm xử lý và nhóm đối chứng là 0,1–0,3, có 24–198 tháng trước sự kiện và 24 tháng sau, hệ số tự tương quan 0–0,5. Hiệu ứng nhỏ nhất phát hiện được là **0,06–0,42 điểm log** ở α = 5% và **0,07–0,50** ở α = 1,25%. Sai số chuẩn phân cụm theo cổ phiếu cho con số chỉ khoảng 0,02–0,04, tức nhỏ hơn từ 3 đến 10 lần. Công suất của H3 vì vậy phụ thuộc vào số tháng và độ lớn của cú sốc chung, không phụ thuộc vào số 299 cổ phiếu. H3 vẫn có thể đủ công suất nếu tác động thật vào khoảng 20–30%, nhưng lý do đề cương nêu ra là sai.
- *Phát hiện bởi:* MHE (bước 5, heuristic 10; finance calibration: "không hợp lệ khi xử lý ở cấp thời gian"), EW (Standard Errors and Inference), SP (mục 4.3).
- *Cách sửa:* Viết lại dòng 678–680: "Vì mọi cổ phiếu chuyển sàn cùng một ngày, suy luận chính dựa trên chuỗi chênh lệch theo tháng giữa nhóm xử lý và nhóm đối chứng. Đề tài dùng sai số chuẩn chịu được tự tương quan trên chuỗi này và suy luận hoán vị trên các ngày giả định trong giai đoạn trước ngày 30/12/2025 (Conley và Taber, 2011). Sai số chuẩn phân cụm theo cổ phiếu và theo tháng chỉ được báo cáo để so sánh." Viết lại dòng 760–763: "Công suất của H~3~ phụ thuộc vào số tháng trước và sau sự kiện và vào độ lớn của cú sốc chung theo tháng, không phụ thuộc vào số cổ phiếu. Thí sinh tính hiệu ứng nhỏ nhất phát hiện được trên chuỗi chênh lệch của giai đoạn 2009–2025 và ghi vào tệp đăng ký." Ghi thêm số ngày giả định dùng cho phép hoán vị và độ dài cửa sổ của mỗi phép thử.

**CR3. Nhóm đối chứng HOSE cũng chịu tác động của sự kiện và của các cú sốc đồng thời. Kiểm tra "so sánh hai nhóm đối chứng với nhau" không đủ để loại tác động lan tỏa.**
- *Vị trí:* dòng 674–676, 718–723, 467–469.
- *Mô tả:* Đề cương chỉ nêu một kênh lan tỏa là "dòng lệnh chuyển từ cổ phiếu HOSE đối sánh sang cổ phiếu chuyển sàn". Fact-checker tìm thêm ba cú sốc trùng thời điểm, đều tác động khác nhau lên nhóm đối chứng HOSE:
  1. FTSE Russell nâng hạng Việt Nam từ ngày 21/9/2026 và đưa tỷ trọng vào chỉ số theo bốn đợt (10%, 20%, 35%, 35%) từ tháng 9/2026 đến tháng 9/2027. Danh sách dự kiến có khoảng 28 mã, chủ yếu là mã vốn hóa lớn trên HOSE. Như vậy 9 trong 24 tháng sau sự kiện có dòng vốn chỉ số đổ vào chính những cổ phiếu HOSE có thể được ghép làm đối chứng theo vốn hóa.
  2. HOSE dự kiến công bố kết quả phân loại lần đầu vào Bảng Chính và Bảng Tiêu chuẩn đúng ngày 28/12/2026. Thay đổi quy tắc này tác động lên cả cổ phiếu HOSE đối chứng.
  3. HOSE tiếp nhận khoảng 300 mã trong một ngày. Điều này thay đổi thành phần các chỉ số toàn thị trường của HOSE, phân bố sự chú ý của nhà đầu tư và tải hệ thống [CẦN XÁC MINH quy tắc đưa mã chuyển sàn vào VN-Index và VNAllshare].
  
  Nhóm UPCoM cũng bị tác động: HNX mất tầng niêm yết, còn mã UPCoM đủ chuẩn sẽ niêm yết thẳng lên HOSE, nên thành phần nhóm đối chứng UPCoM thay đổi theo thời gian. Nếu cả hai nhóm đối chứng cùng bị lệch theo một chiều, việc so sánh chúng với nhau không phát hiện được gì.
- *Phát hiện bởi:* MHE (bước 3–4: điều kiện không lan tỏa; heuristic 13), FC (mục 5), PR (bước 5.3: đối chứng và thời điểm).
- *Cách sửa:* Thêm vào 4.3.8, giả định thứ hai: "Ba thay đổi trùng thời gian tác động lên nhóm đối chứng HOSE: việc FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số theo bốn đợt từ tháng 9/2026, việc HOSE phân loại cổ phiếu vào Bảng Chính và Bảng Tiêu chuẩn từ ngày 28/12/2026, và việc HOSE tiếp nhận khoảng 300 mã. Vì vậy, nhóm đối chứng HOSE loại các mã thuộc danh sách dự kiến của FTSE Russell, và δ được ước lượng thêm với biến kiểm soát là nhóm bảng phân loại của từng mã. Thành phần nhóm đối chứng UPCoM được cố định tại ngày tham chiếu; mã rời UPCoM được giữ đến tháng cuối cùng giao dịch trên UPCoM. Đề tài báo cáo riêng thay đổi thanh khoản của từng nhóm đối chứng so với xu hướng trước sự kiện của chính nhóm đó." Thêm FTSE Russell và quy chế phân bảng của HOSE vào danh mục tài liệu, kèm [CẦN ĐỐI CHIẾU văn bản gốc].

### 2.2. MAJOR

**MJ1. Mốc thời gian phản ứng trước không nhất quán, và hai rổ cùng nhóm đối chứng được ghép bằng đặc điểm đo sau khi lộ trình đã công bố.**
- *Vị trí:* dòng 491–493, 640–645, 676–678, 4.3.8.
- *Mô tả:* Văn bản thừa nhận "lộ trình đã được biết từ khi Thông tư 139/2025/TT-BTC ban hành" (dòng 677–678). Fact-checker cho thấy lộ trình sắp xếp lại thị trường có từ Thông tư 57/2021/TT-BTC (12/7/2021), đã sửa bằng Thông tư 69/2023/TT-BTC và Thông tư 139/2025/TT-BTC. Ngày ban hành của Thông tư 139 ghi khác nhau giữa các nguồn: 29/12/2025 hoặc 30/12/2025. Tuy vậy: (i) giai đoạn trước sự kiện kết thúc ngày 29/9/2026, tức 9 tháng sau Thông tư 139; (ii) rổ CS, rổ HOSE và nhóm đối chứng đều được xác định theo vốn hóa và giá trị giao dịch "tại ngày 29/9/2026". Vốn hóa và thanh khoản lúc đó có thể đã phản ánh kỳ vọng chuyển sàn, nên đây là biến kiểm soát xấu theo nghĩa của Angrist và Pischke. (iii) Kỳ tham chiếu bị loại trong phiên bản nghiên cứu sự kiện chưa được nêu. (iv) Tháng 12/2026 chứa phiên cuối ở HNX (23/12), hai ngày tạm ngừng (24–25/12) và bốn phiên đầu ở HOSE, nhưng chưa được xếp vào trước hay sau sự kiện.
- *Phát hiện bởi:* MHE (Model 4: bad control; Model 7), FC, CK mục 5 (giai đoạn mẫu).
- *Cách sửa:* "Ngày tham chiếu để ghép và lập rổ là 30/11/2025, trước khi Thông tư 139/2025/TT-BTC ban hành. Phiên bản nghiên cứu sự kiện lấy tháng 11/2025 làm kỳ tham chiếu. Các tháng từ 12/2025 đến 11/2026 được ước lượng thành hệ số riêng để đo phản ứng trước. Tháng 12/2026 bị loại." Ghi ngày ban hành Thông tư 139 sau khi đối chiếu Công báo.

**MJ2. Rổ CS và rổ HOSE giữ nguyên thành phần nên không chịu thiên lệch do đổi thành phần, nhưng lại chịu bốn thiên lệch khác. Câu dòng 645–647 vì vậy khẳng định quá mức.**
- *Vị trí:* dòng 640–647, 650–653.
- *Mô tả:*
  1. *Nhìn trước:* rổ CS gồm 30 mã có giá trị giao dịch ba tháng lớn nhất *tại ngày 29/9/2026*, rồi được dùng ngược về các cửa sổ từ quý 1/2021 (ước lượng từ quý 1/2019). Đây là thông tin chưa có tại thời điểm từng cửa sổ.
  2. *Sống sót:* mã phải tồn tại đến tháng 9/2026 mới vào rổ, và mã niêm yết sau năm 2019 không đủ 104 tuần dữ liệu cho các cửa sổ đầu. Đề cương chưa có quy tắc xử lý cho trường hợp này.
  3. *Hồi quy về trung bình:* chọn mã theo giá trị giao dịch ba tháng quanh đợt nâng hạng FTSE là chọn theo cú sốc thanh khoản và sự chú ý nhất thời. Những mã này thường có lợi suất bất thường trước đó và đảo chiều sau đó, nên *G*~t~ có thể "thu hẹp" ngay cả khi không đổi sàn.
  4. *Thành phần trạng thái thị trường:* 23 cửa sổ trước có biến cố trái phiếu doanh nghiệp năm 2022, còn 8 cửa sổ sau có thể là giai đoạn bình thường. Nếu khoảng cách rộng ra trong giai đoạn căng thẳng thì trung bình trước sự kiện bị đẩy lên một cách cơ học.
  
  Ngoài ra, rổ HOSE chỉ được ghép theo vốn hóa và ngành, không ghép theo thanh khoản. Khoảng cách ban đầu vì vậy chứa luôn khác biệt thanh khoản giữa hai rổ. Câu "thay đổi của khoảng cách quanh sự kiện phản ánh thay đổi của sàn" bỏ qua cả bốn điểm trên.
- *Phát hiện bởi:* MHE (bước 3), PR (common_issues: selection), CC (narrower language), S18.
- *Cách sửa:* Viết lại dòng 645–647: "Hai rổ giữ nguyên thành phần nên thay đổi của khoảng cách không đến từ việc đổi thành phần rổ. Tuy vậy, khoảng cách vẫn có thể thay đổi do cú sốc riêng của từng nhóm cổ phiếu, do hồi quy về trung bình và do trạng thái thị trường khác nhau giữa hai giai đoạn. Đề tài kiểm tra các nguồn này bằng cách lặp lại phép so sánh tại các ngày giả định trong giai đoạn 2021–2025, với rổ lập theo cùng quy tắc tại mỗi ngày giả định." Lập rổ theo giá trị giao dịch bình quân 12 tháng tính đến ngày tham chiếu ở MJ1, không dùng 3 tháng. Ghi quy tắc cho mã thiếu lịch sử (loại khỏi cửa sổ, hoặc rút cửa sổ ước lượng xuống còn tối thiểu N tuần).

**MJ3. Biên độ dao động giá và bước giá thay đổi tạo tác động cơ học lên chính biến kết quả của H3.**
- *Vị trí:* dòng 671 (biến *A*~i,t~), 680–682, Bảng 2 (H3).
- *Mô tả:* Biên độ giảm từ ±10% (HNX) xuống ±7% (HOSE). Biên độ hẹp hơn cắt |r| ở những ngày chạm trần hoặc chạm sàn, nên tỷ số Amihud |r|/giá trị giao dịch giảm một cách cơ học. Với chênh lệch Corwin–Schultz, biên độ hẹp hơn thu hẹp khoảng giá cao–thấp. Bước giá cũng khác nhau giữa hai sàn: HNX một bậc, HOSE nhiều bậc theo mức giá [CẦN XÁC MINH]. Thay đổi này tác động trực tiếp lên chênh lệch ước lượng và tỷ lệ ngày lợi suất bằng 0. Vì vậy H3 có thể được "ủng hộ" chỉ do quy tắc giá thay đổi. Câu "δ đo tác động gộp" là đúng, nhưng chưa nói rằng một phần của khoản gộp này là hệ quả cơ học, không phải thanh khoản. Nhóm đối chứng UPCoM có biên độ ±15% (fact-checker xác nhận ±15% áp dụng từ 01/7/2015), nên đường xu hướng của nó cũng chịu ảnh hưởng của biên độ theo cách khác.
- *Phát hiện bởi:* PR (5.9 diễn giải), MHE (định nghĩa biến kết quả), FC.
- *Cách sửa:* Thêm sau dòng 682: "Biên độ hẹp hơn làm giảm |r| ở những ngày chạm trần hoặc chạm sàn, nên làm Amihud giảm một cách cơ học. Đề tài vì vậy báo cáo tỷ lệ ngày chạm biên trước và sau sự kiện, và ước lượng lại (5) với Amihud tính trên những ngày không chạm biên. Với tỷ lệ ngày lợi suất bằng 0 và chênh lệch ước lượng, đề tài báo cáo thêm kết quả theo nhóm mức giá để tách tác động của bước giá."

**MJ4. Tàn dư của phép phân rã: các đại lượng khác đơn vị được trừ cho nhau.**
- *Vị trí:* dòng 411–413 ("đo phần khoảng cách thuộc về sàn"), dòng 728–731 ("H~3~ và H~4~ cho biết phần khoảng cách thuộc về sàn. Phần còn lại gắn với đặc điểm doanh nghiệp").
- *Mô tả:* Khoảng cách ở H2 là chênh lệch của MQI, tức điểm z gộp sáu chỉ báo của toàn sàn. δ ở H3 là chênh lệch log Amihud của các mã chuyển sàn. Khoảng cách ở H4 là chênh lệch lợi suất tương đương chắc chắn tính bằng điểm %/năm. Ba đại lượng này khác đơn vị và khác tập cổ phiếu, nên không thể lấy một đại lượng làm "phần" của đại lượng kia. Đây là cùng loại lỗi với C4 vòng 4, chuyển từ phân rã sang lời diễn giải.
- *Phát hiện bởi:* S9 (bất biến của phép phân rã), CC (claim C05 *unsupported*), PR (claim–evidence).
- *Cách sửa:* Viết lại dòng 728–731: "H~2~ mô tả khoảng cách chất lượng giữa hai sàn trước hợp nhất. Với thanh khoản, phần khoảng cách gắn với sàn được đo trong cùng một đơn vị: tỷ lệ giữa δ và chênh lệch log Amihud trước sự kiện giữa nhóm cổ phiếu chuyển sàn và nhóm HOSE đối chứng. Phần còn lại của chênh lệch này gắn với đặc điểm doanh nghiệp và được mô tả theo nhóm quy mô và mức minh bạch công bố." Sửa dòng 411–413 tương ứng: "Sự kiện chuyển sàn cho phép đo tác động của sàn lên thanh khoản (H~3~) và lên khả năng đầu tư (H~4~) của cùng các cổ phiếu".

**MJ5. Định nghĩa "khả năng đầu tư của một sàn" không khớp với cách đo ở H4.**
- *Vị trí:* dòng 168–171 so với dòng 617–647 và Bảng 2 (H4).
- *Mô tả:* Định nghĩa nói đến "rổ cổ phiếu thanh khoản nhất của sàn đó". H4 lại đo hai rổ cố định: rổ CS gồm các mã sẽ chuyển sàn, và rổ HOSE gồm các mã được ghép theo vốn hóa và ngành, không phải các mã thanh khoản nhất của HOSE. Sau sự kiện, cả hai rổ đều nằm trên HOSE. Như vậy H4 đo khả năng đầu tư của *một rổ cổ phiếu cố định*, không đo khả năng đầu tư *của một sàn*. Theo Banana Rule, một khái niệm dùng hai nghĩa sẽ khiến hội đồng hỏi H4 đang đo cái gì.
- *Phát hiện bởi:* SCW Pass 4, S8, S12.
- *Cách sửa:* Dòng 168–171: "Khả năng đầu tư của một rổ cổ phiếu là lợi suất tương đương chắc chắn sau chi phí giao dịch mà nhà đầu tư đa dạng hóa đạt được khi chỉ dùng các cổ phiếu trong rổ đó. Đề tài so sánh khả năng đầu tư của rổ cổ phiếu chuyển sàn với rổ cổ phiếu HOSE tương đồng về vốn hóa và ngành."

**MJ6. Hàm ý "mảng thị trường mà HNX nên chuyên môn hóa" không có phân tích định lượng tương ứng. "Thị trường vốn Hà Nội" chưa được định nghĩa.**
- *Vị trí:* mục tiêu tổng quát (dòng 243–246), dòng 416–417, 734, 826–831, Bảng 4 (6.3), phạm vi nội dung (dòng 803–806).
- *Mô tả:* Sau sự kiện, các cổ phiếu được phân tích (CS) nằm trên HOSE. Trái phiếu và phái sinh, hai mảng HNX tiếp tục vận hành, đã bị loại khỏi phân tích định lượng (dòng 804–806). UPCoM có MQI và là nhóm đối chứng, nhưng không có kết quả nào được dành cho chính UPCoM. Vì vậy đề xuất chuyên môn hóa cho "thị trường vốn Hà Nội" chỉ dựa trên so sánh văn bản chính sách. Cụm "thị trường vốn Hà Nội" xuất hiện khoảng 8 lần nhưng chưa được định nghĩa: nó có thể là thị trường do HNX vận hành, doanh nghiệp đặt trụ sở ở Hà Nội, hoặc hệ thống tài chính của thành phố. Mức khớp với câu hỏi số 1 của bài toán 19 phụ thuộc vào cầu nối này, nên Hội đồng tư vấn theo Điều 11.3 và Điều 18.1 của Nghị quyết 57 sẽ đọc đúng chỗ này.
- *Phát hiện bởi:* CC (claim C06 *unsupported*, scope), PR (bước 4), RG (Significance/fit), S1.
- *Cách sửa:* Thêm vào khối định nghĩa ở dòng 163: "Thị trường vốn Hà Nội trong đề cương là các thị trường do HNX vận hành: cổ phiếu niêm yết đến ngày 23/12/2026, UPCoM, trái phiếu và chứng khoán phái sinh." Thêm vào 4.3.7 một kết quả mô tả: "Đề tài báo cáo thay đổi của MQI và của thanh khoản UPCoM sau sự kiện so với xu hướng trước sự kiện. Đây là bằng chứng trực tiếp về thị trường cổ phiếu mà HNX tiếp tục vận hành." Thêm vào dòng 734: "Đề xuất về trái phiếu và phái sinh là đề xuất định tính, dựa trên văn bản chính sách và so sánh quốc tế."

**MJ7. Không có phương án dự phòng cho trường hợp sự kiện bị lùi hoặc chỉ thực hiện một phần.**
- *Vị trí:* 4.3.10 (dòng 775–779), 7.4 (dòng 1013–1016).
- *Mô tả:* Toàn bộ câu hỏi 3 (H3, H4) dựa vào việc sự kiện diễn ra đúng ngày 28/12/2026. Lộ trình này đã được sửa ít nhất hai lần (Thông tư 69/2023 và Thông tư 139/2025). Văn bản cũng cho phép hoàn tất "chậm nhất đến hết ngày 31/12/2026", và VNX nói tiêu chí phân bảng còn có thể điều chỉnh. Ba phương án dự phòng hiện có không bao gồm trường hợp này.
- *Phát hiện bởi:* RG (Feasibility; "Technical mistakes: no contingency"), CC (blocked-route rule).
- *Cách sửa:* Thêm phương án thứ tư ở 4.3.10 và 7.4: "Nếu ngày chuyển sàn thay đổi, thiết kế giữ nguyên với ngày mới, và ngày tham chiếu được dời theo. Nếu sự kiện lùi sang sau tháng 6/2027, thời gian sau sự kiện trong thời hạn học không đủ 18 tháng; khi đó H~3~ dùng các tháng có sẵn, H~4~ được báo cáo ở dạng mô tả, và luận án tăng trọng số cho H~2~ cùng phân tích phản ứng trước." Ghi cả trường hợp một phần số mã không chuyển, ví dụ do hủy niêm yết hoặc chuyển xuống UPCoM.

**MJ8. Thời điểm đăng ký trước và lịch thực hiện chưa khớp với ngày sự kiện.**
- *Vị trí:* dòng 596–600, Bảng 5 (năm 1 quý 1; năm 2 quý 3–4; năm 3 quý 1–2).
- *Mô tả:* (i) Đề cương không nêu thời điểm bắt đầu khóa học. Nếu năm 1 bắt đầu năm 2027 thì việc đăng ký ở "năm 1, quý 1" diễn ra sau ngày 28/12/2026. Lúc đó thanh khoản sau sự kiện đã được báo chí đưa tin hằng ngày, nên đăng ký mất phần lớn giá trị "trước khi thấy dữ liệu". (ii) Bảng 5 đặt việc kiểm định H3 ở năm 2, quý 3–4, nhưng 24 tháng sau sự kiện chỉ đủ vào tháng 1/2029. Kế hoạch chưa nói H3 ở năm 2 là ước lượng tạm hay kết quả chính, và nếu ước lượng hai lần thì lần nào được báo cáo là xác nhận. (iii) Bảng 5 đặt chuyên đề 1 (về H1) là sản phẩm năm 1, trong khi H1 được kiểm định ở năm 2.
- *Phát hiện bởi:* CC (changes after seeing results), EW (Pre-registration), RG (timeline), CK mục 8.
- *Cách sửa:* "Thí sinh nộp tệp đăng ký trước lên OSF Registries trước ngày 28/12/2026, độc lập với thời điểm nhập học; tệp được cập nhật dưới dạng bản sửa có ghi ngày nếu Nhà trường hoặc người hướng dẫn yêu cầu." (Việc làm trước khi nhập học là quyết định của người dùng: Chờ duyệt P3.) Sửa Bảng 5, năm 2: "ước lượng H~3~ tạm thời trên 12–18 tháng (không phải kiểm định xác nhận)". Kiểm định xác nhận H3 chuyển sang năm 3, quý 1. Ghi ngày dự kiến bắt đầu khóa học.

**MJ9. Đặc tả bootstrap của H2 sai đối tượng; quy tắc lấy giá trị p cho Holm chưa nêu.**
- *Vị trí:* dòng 536–537, 689–691, 457–458.
- *Mô tả:* Dòng 689–691 viết "Khoảng tin cậy của H~2~ và H~4~ được tính bằng bootstrap khối dừng … trên chuỗi lợi suất tuần của hai rổ". H2 không dùng rổ, cũng không dùng lợi suất. H2 dùng chuỗi MQI theo tháng của toàn sàn. Ngoài ra, H3 yêu cầu bác bỏ "so với cả hai nhóm đối chứng", còn H4 yêu cầu khoảng tin cậy và thêm điều kiện "ít nhất năm trong bảy mô hình cùng dấu". Đề cương chưa nói giá trị p nào được đưa vào thủ tục Holm.
- *Phát hiện bởi:* SW (bước 6: đối chiếu phương pháp với kết quả), CK mục 6, PR (5.7).
- *Cách sửa:* "Khoảng tin cậy của H~2~ được tính bằng bootstrap khối dừng trên chuỗi chênh lệch MQI theo tháng. Khoảng tin cậy của H~4~ được tính bằng bootstrap khối dừng trên chuỗi lợi suất tuần của hai rổ, lấy mẫu riêng trong giai đoạn trước và giai đoạn sau sự kiện." Thêm vào ghi chú Bảng 2: "Giá trị p của H~3~ là giá trị lớn hơn trong hai so sánh với hai nhóm đối chứng. Giá trị p của H~4~ lấy từ khoảng tin cậy bootstrap; điều kiện năm trên bảy mô hình là điều kiện bổ sung, không đi vào thủ tục Holm."

**MJ10. Phương trình nghiên cứu sự kiện và nhóm đối chứng của H3 chưa được đặc tả.**
- *Vị trí:* dòng 664–685.
- *Mô tả:* (i) Phiên bản nghiên cứu sự kiện được nhắc đến hai lần nhưng không có phương trình, kỳ tham chiếu hay cửa sổ. (ii) Nhóm đối chứng HOSE "ghép theo vốn hóa và ngành" chưa có tỷ lệ ghép, chưa nói ghép có hoàn lại hay không, chưa có ngưỡng khoảng cách hay vùng hỗ trợ chung. Phần lớn mã HNX nhỏ hơn hẳn mã HOSE nhỏ nhất cùng ngành [CẦN XÁC MINH trên dữ liệu]. (iii) Chưa nói hai nhóm đối chứng được ước lượng trong hai hồi quy riêng hay trong một hồi quy gộp. (iv) Chưa nói *A*~i,t~ được xử lý thế nào khi một tháng không có giao dịch, lúc đó log Amihud không xác định. (v) Mẫu 2009–2026 rất dài so với 24 tháng sau sự kiện, nên chưa rõ tác động trước sự kiện được ước lượng trên cửa sổ nào.
- *Phát hiện bởi:* MHE (DiD checks: pre-trends phải vẽ được), EW ("viết ra được phương trình từ bảng"), CK mục 6.
- *Cách sửa:* Thêm phương trình (5′): $A_{i,t} = \alpha_i + \tau_t + \sum_{k \neq -1} \delta_k \cdot D_i \cdot 1[t = e + k] + \varepsilon_{i,t}$, trong đó e là tháng 12/2026, k chạy từ −36 đến +24, và k = −1 được thay bằng kỳ tham chiếu nêu ở MJ1. Thêm câu: "Mỗi nhóm đối chứng được ước lượng trong một hồi quy riêng. Mẫu của (5) gồm 36 tháng trước và 24 tháng sau sự kiện. Nhóm đối chứng HOSE được ghép 1:1, có hoàn lại, trong ngưỡng khoảng cách ghi ở tệp đăng ký; mã chuyển sàn không có cặp bị loại và tỷ lệ bị loại được báo cáo. Tháng không có giao dịch được ghi là thiếu, và tỷ lệ tháng thiếu được báo cáo theo nhóm."

**MJ11. Còn tàn dư của thiết kế cũ về "giai đoạn căng thẳng" ở 4.3.3, 4.3.10, mục 6 và mục 10.**
- *Vị trí:* dòng 497–498, 765–767, 929–931, 1191–1193.
- *Mô tả:* (i) Dòng 497–498 tính "khủng hoảng tài chính toàn cầu đến năm 2009" là một trong ba đợt căng thẳng, nhưng dữ liệu chỉ bắt đầu từ 6/2009, sau đáy tháng 3/2009, nên đợt này gần như nằm ngoài mẫu. (ii) Dòng 765–767 giải thích bằng "chủ yếu nằm trong cửa sổ ước lượng". Đây là lý do của v4. Ở v5, giai đoạn căng thẳng chỉ dùng mô tả cho H2, mà H2 không có cửa sổ ước lượng. (iii) Mục 6 viết mục tiêu là "kiểm định giả thuyết trên chuỗi thời gian tài chính khi mẫu có ít giai đoạn căng thẳng". (iv) Mục 10 viết hướng của người hướng dẫn "trùng với ba cấu phần của đề tài: chất lượng thị trường vốn, biến động trong giai đoạn căng thẳng và quyết định danh mục". Cấu phần trung tâm hiện nay, tức thiết kế khác biệt kép quanh sự kiện, không xuất hiện trong câu này.
- *Phát hiện bởi:* S7 (thesis-tie), S9, rà tàn dư (grep "giai đoạn căng thẳng": 10 lần).
- *Cách sửa:* Dòng 497–500: "…và gồm hai đợt: đại dịch COVID-19 năm 2020 (Dao và cộng sự, 2021) và biến cố thị trường trái phiếu doanh nghiệp từ quý 4/2022…; giai đoạn cuối khủng hoảng tài chính toàn cầu (6–12/2009) chỉ được mô tả." Xóa câu ở dòng 765–767. Mục 6: "…thiết kế một nghiên cứu sự kiện có đăng ký trước, đánh giá tác động của một thay đổi cấu trúc thị trường, và báo cáo trung thực cả những kết quả chưa đủ cơ sở kết luận." Mục 10: "…trùng với ba cấu phần của đề tài: chất lượng thị trường vốn ở thị trường mới nổi, tác động của thay đổi cấu trúc sàn và quyết định danh mục."

### 2.3. MINOR

**m1. Khoảng trống K3 ("chưa có bằng chứng về hợp nhất hai sàn trong một quốc gia ở thị trường mới nổi") đã có phản ví dụ.** Ba sở giao dịch Karachi, Lahore và Islamabad hợp nhất thành Pakistan Stock Exchange vào tháng 1/2016, và đã có ít nhất một bài tạp chí so sánh thanh khoản, biến động và hiệu quả trước và sau hợp nhất (xem mục 3 của bảng nguồn). Việc chuyển cổ phiếu từ Osaka sang Tokyo ngày 16/7/2013 là tiền lệ gần nhất về thiết kế (cả một sàn chuyển sang sàn kia trong một ngày), dù xảy ra ở thị trường phát triển. *S21 (định vị trung thực), FC.* Sửa Bảng 1 (K3) và dòng 297–298: "K3. Bằng chứng về hợp nhất các sàn trong một quốc gia ở thị trường mới nổi còn ít (ví dụ Pakistan năm 2016) và chưa đo khả năng đầu tư." Bổ sung hai nguồn ở mục 3 sau khi đọc toàn văn.

**m2. Lập luận "cấu trúc tương tự Bắc Kinh và Thượng Hải" (dòng 200–202) là phép so sánh chưa có căn cứ.** Bắc Kinh không có sàn cổ phiếu tầm quốc gia cho đến khi Sở Giao dịch Chứng khoán Bắc Kinh ra đời năm 2021, nên phép so sánh có thể đi theo hai chiều. *S18.* Đổi "có cấu trúc tương tự" thành "có thể so sánh với".

**m3. Ký hiệu.** (i) k dùng cho sàn ở (1) ({HNX niêm yết, UPCoM, HOSE}) nhưng dùng cho rổ ở (2)–(3) ({HOSE, CS}); "HOSE" ở (3) là rổ ghép, không phải sàn. Nên đổi thành b ∈ {H, CS}. (ii) i, α~i~, τ~t~ và ε~i,t~ ở (5) là cổ phiếu–tháng, còn ở (6) là trung tâm–kỳ GFCI. Nên dùng γ~i~, θ~t~, u~i,t~ cho (6), hoặc ghi rõ. (iii) "t−1" ở (6) không phải kỳ trước: biến theo năm được gán cho hai kỳ của năm sau. Nên viết *SMD*~c(i),y(t)−1~. (iv) MQI chưa được giải nghĩa. (v) Chỉ số trên rỗng ở (4) (`\sum_{m \in M}^{}`). *EW (Numbers and Notation), CK mục 4.*

**m4. "Tái cân bằng hằng tháng" trong cửa sổ đánh giá 3 tháng** (ghi chú Bảng 3) chưa rõ là ước lượng lại trọng số hay chỉ đưa trọng số về mức mục tiêu đã ước lượng ở đầu cửa sổ. *PR 5.6.*

**m5. Câu hỏi 3 viết "chính các cổ phiếu chuyển sàn" (khoảng 300 mã), nhưng H4 chỉ đo rổ 30 mã thanh khoản nhất.** Theo Nielsson (2009), lợi ích tập trung ở doanh nghiệp lớn, nên kết quả H4 khó áp cho cả nhóm. Thêm vào 4.4, mục giới hạn: "kết luận về H~4~ chỉ áp dụng cho rổ 30 cổ phiếu chuyển sàn có thanh khoản cao nhất". *CK mục 5, S18.*

**m6. Hình 1** (PDF trang 7): mũi tên nét liền từ "Trước hợp nhất" sang "Sự kiện 28/12/2026" chưa được ghi chú giải thích. Nếu đó là trình tự thời gian, ghi chú cần nói vậy. *CK mục 3.*

**m7. Thứ tự giữa Hình 3, 4.3.9 và Bảng 5 lệch nhau.** Hình 3 và 4.3.9 đặt H1 (bước 2) trước H2 (bước 3), còn Bảng 5 kiểm định H2 ở năm 1 và H1 ở năm 2. Chuyên đề 1 (H1) là sản phẩm năm 1 trước khi H1 được ước lượng. *CK mục 8.*

**m8. Dữ kiện cần ghi chính xác hơn.** (i) Mục Thông tư 139/2025/TT-BTC trong danh mục tài liệu chưa có ngày ban hành; các nguồn ghi khác nhau (29/12/2025 và 30/12/2025). (ii) Số "khoảng 299 mã": báo chí ghi "gần 300" và "hơn 300 mã". Nên trích danh sách của VNX. Con số 299 cũng trùng với số công ty trong mẫu của Vo và Phan (2017) ở dòng 315, dễ gây nhầm, nên ghi "khoảng 300 mã (danh sách VNX ngày …)". *FC.*

**m9. Câu quá 45 âm tiết: 40 câu** (đếm trên dòng 147–1198; độ dài trung bình 27,5 âm tiết/câu, nằm trong khoảng 25–35). Các câu dài nhất ở dòng 703 (77), 911 (76), 927 (69), 594 (65), 271 (63), 760 (61), 1189 (60). Ví dụ tách câu ở dòng 703–711: "*Z*~i,t~ là điểm GFCI chuẩn hóa thành điểm z trong từng kỳ. Đề tài chuẩn hóa vì điểm GFCI được ước lượng lại mỗi kỳ và số trung tâm thay đổi giữa các kỳ." *Văn phong paper-writing-vn; SCW Pass 3.*

**m10. Gạch nối (M1).** "mua--bán" (dòng 274, 435, 446, 510), "Moore--Penrose" (dòng 592) và "phiếu--tháng" (dòng 665) sẽ thành gạch ngang khi dựng. Nên dùng gạch nối thường.

**m11. Hai đoạn đặt sai chỗ (m11 vòng 4, chưa sửa).** Chuyển "Đóng góp dự kiến" và "Về sản phẩm" ra khỏi 4.4. Đoạn "Từ bằng chứng đến định hướng cho Hà Nội" và đoạn về mã nguồn mở nên chuyển khỏi 4.3.8, có thể thành tiểu mục 4.3.11. *S7, S23.*

**m12. Câu văn trong Hình 2 (m9 vòng 4, chưa sửa).** Chuyển câu "Mỗi cửa sổ đánh giá: …" xuống chú thích hình. *S25.*

**m13. Mục lục và danh mục chữ viết tắt (m1, m17 vòng 4).** Mục lục vẫn bắt đầu từ mục 4, và chưa có danh mục chữ viết tắt (HNX, HOSE, UPCoM, VNX, GFCI, MQI, SMD, CS, OSF).

**m14. Chỉ báo minh bạch "số ngày trễ hạn công bố báo cáo tài chính" là chỉ báo theo quý, nhưng MQI được tính theo tháng.** Cần ghi cách gán sang tháng: giữ nguyên giá trị đến kỳ công bố tiếp theo. *CK mục 4.*

**m15. Câu "thành phần mẫu ổn định" ở 4.3.8 (dòng 723–724) gọi tên sai giả định.** Giữ mã hủy niêm yết đến tháng cuối cùng tạo ra bảng không cân bằng; nó không bảo đảm thành phần ổn định. Sửa: "Thứ ba, việc rời mẫu không liên quan đến sự kiện: đề tài báo cáo tỷ lệ mã hủy niêm yết sau sự kiện ở nhóm xử lý và ở nhóm đối chứng, và ước lượng lại trên bảng cân bằng."

**m16. H1 (phương trình 6) là liên hệ có điều kiện, và nguồn biến thiên còn mỏng.** Hiệu ứng cố định theo trung tâm hấp thụ phần lớn biến thiên của *SMD*, một biến thay đổi chậm. Nhiều quốc gia chỉ có một trung tâm. Chiều nhân quả ngược (trung tâm mạnh kéo theo giao dịch cổ phiếu) chưa được nhắc. Thêm một câu: "Vì *SMD* thay đổi chậm, β chủ yếu được xác định từ biến thiên theo thời gian trong từng quốc gia; đề tài báo cáo thêm ước lượng không có hiệu ứng cố định theo trung tâm." Bảng 2 nên bổ sung nguồn phương pháp cho H3: Conley và Taber (2011) và Rambachan và Roth (2023) (mục 3). *MHE (Finance calibration: biến chậm bị FE hấp thụ), EW.*

---

## 3. Chờ duyệt (vượt phạm vi đã chốt; không xếp vào lỗi)

- **P1. Đưa H4 ra khỏi họ kiểm định xác nhận.** Theo CR1, H4 gần như không có công suất. Phương án là giữ bảy mô hình làm công cụ đo, giữ H4 là giả thuyết, nhưng báo cáo nó ở dạng ước lượng có khoảng tin cậy và hiệu ứng nhỏ nhất phát hiện được, và để họ Holm chỉ còn H1–H3. Thay đổi này đổi cấu trúc kiểm định nên cần người dùng duyệt.
- **P2. Nhóm đối chứng tổng hợp.** Nếu các cú sốc ở CR3 khiến cả hai nhóm đối chứng không đạt, có thể dùng phương pháp kiểm soát tổng hợp trên chuỗi thanh khoản tổng của nhóm xử lý, với nhóm cho mượn gồm mã HOSE ngoài danh sách FTSE và mã UPCoM. Đây là nhánh thiết kế mới.
- **P3. Đăng ký trước trước ngày 28/12/2026**, tức trước khi nhập học (MJ8). Đây là quyết định về quy trình và về quan hệ với người hướng dẫn.
- **P4. Thêm UPCoM thành một kết quả nghiên cứu chính** (không chỉ là nhóm đối chứng) để trả lời trực tiếp "thị trường vốn Hà Nội sau hợp nhất" (MJ6). Thay đổi này thêm một đối tượng phân tích.
- **P5. Tách tác động của biên độ giá** bằng các mã đã tự chuyển từ HNX sang HOSE trước năm 2026 (một sự kiện so le). Thiết kế này đòi hỏi bộ ước lượng khác biệt kép cho xử lý so le và là một nhánh mới.

(Vấn đề học toàn thời gian theo Điều 11.3 Nghị quyết 57 là vấn đề hồ sơ đã được loại khỏi phạm vi, nên không ghi ở đây.)

### Bảng nguồn đề xuất thêm (đã thấy ở các URL dưới đây; chưa đọc toàn văn)

| # | Nguồn | Nơi đã thấy | Trạng thái | Dùng vào chỗ nào |
|---|---|---|---|---|
| 1 | Conley, T. G., Taber, C. R. (2011), "Inference with 'Difference in Differences' with a Small Number of Policy Changes", *Review of Economics and Statistics*, 93(1), 113–125, DOI 10.1162/REST_a_00049 | https://nber.org/papers/t0312 ; https://users.ssc.wisc.edu/~ctaber/Papers/ctabdd.pdf | Đã kiểm thư mục qua chỉ mục | CR2: suy luận khi chỉ có một lần thay đổi chính sách. |
| 2 | Rambachan, A., Roth, J. (2023), "A More Credible Approach to Parallel Trends", *Review of Economic Studies*, 90(5), 2555–2591, DOI 10.1093/restud/rdad018 | https://ideas.repec.org/a/oup/restud/v90y2023i5p2555-2591..html ; https://economics.mit.edu/research/publications/more-credible-approach-parallel-trends | Đã kiểm thư mục | 4.3.8: độ nhạy khi xu hướng song song bị vi phạm, phù hợp với tình huống phản ứng trước. |
| 3 | Ali và Sharif (2022), bài về hợp nhất ba sở giao dịch thành Pakistan Stock Exchange, *Afro-Asian Journal of Finance and Accounting* 12(4), 455–478 [CẦN XÁC MINH tên bài, tên đầy đủ tác giả và tên tạp chí] | https://ideas.repec.org/a/ids/afasfa/v12y2022i4p455-478.html | Chưa kiểm đủ | m1: phản ví dụ cho K3. Kết quả hỗn hợp, và giai đoạn sau hợp nhất có bất ổn chính trị. |
| 4 | Hisada, "The Effect of Investor Sentiment toward an Exchange Merger on Liquidity", bài làm việc của CARF, Đại học Tokyo [CẦN XÁC MINH năm và tên đầy đủ] | https://www.carf.e.u-tokyo.ac.jp/wp/wp-content/uploads/2021/12/01hisada.pdf | Chưa kiểm đủ (bài làm việc) | m1: tiền lệ về thiết kế (Osaka sang Tokyo ngày 16/7/2013). Thanh khoản tăng ngắn hạn, mạnh hơn ở cổ phiếu nhỏ. |
| 5 | Japan Exchange Group, lịch sử tích hợp thị trường cổ phiếu (16/7/2013) | https://www.jpx.co.jp/english/corporate/about-jpx/history/01.html | Thông tin tổ chức | m1. |

---

## 4. Bằng chứng tuân thủ

### 4.1. Skill đã gọi (bằng công cụ Skill), kèm dòng trả về
1. `peer-review` → "Launching skill: peer-review"
2. `research-grants` → "Launching skill: research-grants"
3. `scientific-writing` → "Launching skill: scientific-writing"
4. `sciwrite` → "Launching skill: sciwrite"
5. `anthropic-skills:paper-writing-vn` → "Launching skill: anthropic-skills:paper-writing-vn"
6. `econ-write` → "Launching skill: econ-write"
7. `credible-claims` → "Launching skill: credible-claims"
8. `mhe-identification` (chế độ Critic) → "Launching skill: mhe-identification"
9. `statistical-power` → "Launching skill: statistical-power"
10. `consistency-checker` → "Launching skill: consistency-checker"
11. `fact-checker` → "Launching skill: fact-checker"

Không skill nào báo lỗi.

### 4.2. Công cụ và script đã chạy
- **peer-review:** đã đọc toàn bộ `scripts/_common.py`, `validate_review_intake.py` và `validate_claim_evidence.py` (thư viện chuẩn, không gọi mạng) trước khi chạy.
  - `validate_review_intake.py r5rev/intake.json` → `READY_FOR_LOCAL_REVIEW`. Cảnh báo: `CONFIDENTIAL_NOTES_CHANNEL_UNAVAILABLE`, `COMPETENCE_LIMITS_MUST_BE_DISCLOSED`. Giới hạn năng lực đã khai: chưa mở văn bản gốc của Thông tư 139 và lịch VNX (chỉ có báo chí); chưa kiểm quy chế tuyển sinh; chưa biết chi tiết phương pháp GFCI.
  - `validate_claim_evidence.py r5rev/claims.csv` → `VALID_WITH_ALIGNMENT_GAPS`: 8 khẳng định, 3 *partly_supported*, 5 *unsupported* (C02 rổ cố định, C03 công suất H3, C05 tàn dư phân rã, C06 hàm ý chuyên môn hóa, C08 bootstrap H2).
  - Không chạy `select_reporting_guidelines.py`, `audit_statistics_reproducibility.py`, `audit_citations.py`, `lint_review.py` và `generate_review_scaffold.py`. Các script này chưa được đọc hết trong phiên này. Danh mục hướng dẫn báo cáo của skill cũng thuộc lĩnh vực y sinh, và báo cáo này theo khuôn do người giao việc quy định.
  - Lệnh chạy dùng `python3 -E -s`, không dùng `-I`, vì `-I` chặn việc import `_common` cùng thư mục. Các tệp đầu vào là tệp do phản biện tự viết.
- **statistical-power:** không chạy `scripts/` của skill. MDE được tính bằng `r5rev/mde.py`, một script do phản biện tự viết, chỉ dùng `statistics.NormalDist` và `math` của thư viện chuẩn, chạy với `python3 -I`. Công thức: MDE = (z~1−α/2~ + z~0,8~)·SE. Ở H4, SE = SD(*G*)·√(1/23 + 1/8) với SD(*G*) = 52·σ~w~√(2(1−r))/√13. Ở H3, SE = σ~c~·√((1+ρ)/(1−ρ))·√(1/T~pre~ + 1/24). Mọi đầu vào là giả định dùng để phân tích độ nhạy, không phải số liệu.

  Kết quả H4 (điểm %/năm):

  | σ~w~ | r | SD(*G*~t~) | MDE α=5% | MDE α=1,25% |
  |---|---|---|---|---|
  | 2,5% | 0,6 | 32,2 | 37,1 | 44,2 |
  | 2,5% | 0,9 | 16,1 | 18,5 | 22,1 |
  | 3,5% | 0,6 | 45,1 | 51,9 | 61,9 |
  | 3,5% | 0,9 | 22,6 | 26,0 | 30,9 |

  Kết quả H3 (log Amihud): với σ~c~ = 0,1–0,3, T~pre~ = 24–198 tháng và ρ = 0–0,5, MDE là 0,061–0,420 ở α = 5% và 0,072–0,501 ở α = 1,25%. Với sai số chuẩn phân cụm theo cổ phiếu (σ~i~ = 0,5–0,8, bỏ qua cú sốc chung), MDE chỉ khoảng 0,023–0,037.
- **consistency-checker:** chỉ dùng checklist 10 mục, không chạy `scripts/`.
- **paper-writing-vn:** đã đọc `red_team_protocol.md`, `author_profile/gate_mechanical.md`, `author_profile/gate_semantic.md` và `writing_checklists/design_questions.md` trong `/home/user/M-n_HTTM/.claude/skills/paper-writing-skill/`. Bộ lọc máy móc đã được chuyển sang tiếng Việt và chạy bằng grep trên dòng 147–1198. Kết quả thô:
  - M1 (gạch ngang trong tên ghép): 6 lần, ở dòng 274, 435, 446, 510, 592, 665.
  - M2 (đối lập tu từ): 8 lần ("thay vì" ×2, "không để", "không phải" ×3, "không phản ánh", "không đo riêng"). Cả 8 lần đều mang nội dung thực nên được giữ. Riêng dòng 646 bị sửa vì khẳng định quá mức (MJ2).
  - M5: "tối ưu" ×3 và "vượt trội" ×2 đều là thuật ngữ kỹ thuật, được giữ.
  - M6: 0. M12: "một cách" ×1, "trong bối cảnh" ×1. M15: 0.
  - Bị động "được/bị": 64 lần trên 310 câu, đúng văn phong khoa học tiếng Việt, không che tác nhân quan trọng.
  - Độ dài câu trung bình 27,5 âm tiết; 40 câu vượt 45 âm tiết.
  - Grep tàn dư: "phân rã", "độ sâu", "thứ tự ưu tiên", "rổ HNX", "đối sánh tuần tự", "hối tiếc", "robo", "S_t" và "Markov" đều trả về 0. "Giai đoạn căng thẳng" trả về 10 lần (MJ11). "Chế độ" trả về 3 lần, đều trong M5 và nhóm tài liệu (E), là hợp lệ.
- **Script khác do phản biện tự viết** (`r5rev/sent.py` đếm câu, `r5rev/cite.py` đối chiếu trích dẫn hai chiều; thư viện chuẩn, `python3 -I`): 59 mục tài liệu. Mọi cảnh báo của script đều là dương tính giả, do script không tách được tác giả thứ hai, mã ISSN hoặc dạng "2026a; 2026b". Không có trích dẫn mồ côi.
- Đã dựng PDF trang 10, 16 và 18 (tức trang in 7, 13 và 15) thành ảnh bằng `pdftoppm` để xem Hình 1–3.

### 4.3. File đã đọc
- `scratchpad/r5/v5.md` (toàn văn); `scratchpad/r5/v5-libreoffice.pdf` (ảnh các trang có Hình 1–3).
- `/home/user/M-n_HTTM/reports/r4-review.md` (toàn văn); `/home/user/M-n_HTTM/outputs/round-5/nhat-ky-thay-doi-round-5.md`.
- `scratchpad/nq57/trich-qd1193.md`, `scratchpad/nq57/trich-dieu-11-18.md`.
- `SKILL.md` của 11 skill đã gọi; các script của peer-review nêu ở 4.2; các file của paper-writing-skill nêu ở 4.2.
- File làm việc tạm trong `scratchpad/r5rev/`: `intake.json`, `claims.csv`, `mde.py`, `sent.py`, `cite.py`, `body.md` và ảnh `pg10-10.png`, `pg16-16.png`, `pg18-18.png`.

### 4.4. Truy vấn WebSearch đã chạy (chỉ từ khóa và thông tin thư mục)
1. Thông tư 139/2025/TT-BTC sửa đổi Thông tư 57/2021/TT-BTC lộ trình sắp xếp thị trường cổ phiếu HNX HOSE ngày ban hành
2. chuyển toàn bộ cổ phiếu niêm yết HNX sang HOSE 28/12/2026 phiên cuối 23/12 299 mã
3. GFCI 40 Ho Chi Minh City 67th 692 points Da Nang 71st
4. biên độ dao động giá HOSE 7% HNX 10% UPCoM 15% từ năm
5. HOSE Bảng Chính Bảng Tiêu chuẩn phân loại cổ phiếu niêm yết 28/12/2026
6. Nghị quyết 222/2025/QH15 trung tâm tài chính quốc tế thông qua ngày 27/6/2025 hiệu lực 1/9/2025
7. FTSE Russell Vietnam upgrade secondary emerging effective 21 September 2026
8. Tokyo Stock Exchange Osaka Securities Exchange cash equity market integration July 2013 liquidity study journal
9. Pakistan Stock Exchange merger Karachi Lahore Islamabad 2016 liquidity market quality study
10. Rambachan Roth 2023 A More Credible Approach to Parallel Trends Review of Economic Studies
11. Conley Taber 2011 Inference with difference in differences with a small number of policy changes Review of Economics and Statistics

Không dùng WebFetch.

### 4.5. Kết quả fact-checker

| Dữ kiện trong đề cương | Kết luận | Căn cứ (nguồn đã thấy) |
|---|---|---|
| Thông tư 139/2025/TT-BTC sửa Thông tư 57/2021 | ĐÚNG phần lớn; ngày ban hành chưa thống nhất (29/12 hoặc 30/12/2025) | hcc.nghean.gov.vn (tên văn bản, 29/12/2025); các báo ghi 30/12/2025 |
| Phiên cuối ở HNX 23/12/2026, phiên đầu ở HOSE 28/12/2026 | ĐÚNG; thêm chi tiết tạm ngừng 24–25/12 và hạn hoàn tất 31/12/2026 | vietnamplus.vn, vietnamnews.vn, thoibaotaichinhvietnam.vn, cafef.vn |
| Khoảng 299 mã | CHƯA KIỂM ĐƯỢC; báo chí ghi "gần 300" và "hơn 300" | vcci.com.vn, các nguồn trên |
| Nghị quyết 222/2025/QH15, 27/6/2025, Thành phố Hồ Chí Minh và Đà Nẵng | ĐÚNG; ngày hiệu lực 01/9/2025 chưa xác nhận được (đề cương không nêu ngày này) | thuvienphapluat.vn, luatvietnam.vn |
| GFCI 40: Thành phố Hồ Chí Minh 67/117, 692 điểm; Đà Nẵng 71 | ĐÚNG theo báo chí; chưa đối chiếu báo cáo gốc | en.vietnamplus.vn, vietnamnet.vn |
| Biên độ HOSE ±7%, HNX ±10% | ĐÚNG ở hiện tại; năm bắt đầu áp dụng chưa xác định; UPCoM ±15% từ 01/7/2015 | dsc.com.vn, nhandan.vn, cts.vn |
| (Phát hiện thêm) FTSE Russell nâng hạng từ 21/9/2026, đưa vào chỉ số qua bốn đợt đến 9/2027 | Dùng cho CR3 | vietnamnews.vn, en.vietstock.vn |
| (Phát hiện thêm) HOSE phân loại Bảng Chính và Bảng Tiêu chuẩn, kết quả lần đầu 28/12/2026 | Dùng cho CR3 | cafef.vn, thoibaotaichinhvietnam.vn |

### 4.6. Xác nhận bảo mật
Không câu, bảng, phương trình, tên giả thuyết hay số liệu riêng nào của đề cương được gửi ra dịch vụ ngoài. Mười một truy vấn ở 4.4 chỉ chứa tên văn bản pháp luật, tên tác giả, tên bài, tên tạp chí, sự kiện công khai đã đưa tin và từ khóa chủ đề. Mọi phân tích văn bản và mọi phép tính đều chạy cục bộ.
