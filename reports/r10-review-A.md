# Phản biện vòng 10, Agent A (phương pháp, nhận dạng, cách viết)

Đề cương: "Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội" (bản v10). Người phản biện: Claude, Agent A. Ngày: 16/10/2026. Báo cáo chỉ đọc đề cương và không sửa đề cương. Trọng tâm của vòng này là H3, gồm phần mở rộng theo mức chịu cú sốc (idx 322, 323) và phân tích theo trụ sở (idx 324, 325).

---

## (1) Bằng chứng tuân thủ

**File đã đọc (chỉ đọc):**
- `scratchpad/r10/dump-v10.txt`: đọc toàn văn, idx 0–598.
- `outputs/round-10/de-cuong-v10-round-10.docx`: dùng `zipfile` của Python để đọc `word/document.xml` và trích 7 công thức OMML. Công thức (1)–(4) và (7) giống v8. Công thức (4) có mẫu số `|M|`. Công thức (6) đã có số hạng `δpre·Di·1[t<1/2024]`. Phần mở rộng theo mức chịu cú sốc ở idx 323 **không có công thức hiển thị**.
- `reports/r8-review-A.md`, `outputs/round-8/nhat-ky-thay-doi-round-8.md`, `outputs/round-9/nhat-ky-thay-doi-round-9.md`: đọc toàn bộ để đối chiếu.
- `ho-so/TaiLieu_Vong8_GopTXT_16-10-2026.txt`: grep có chủ đích ở các mục sau.
  - Mục [30], FTSE Russell FAQ v1.3, câu hỏi 6. Danh sách mã đủ điều kiện từ ngày 21/9/2026, tính trên dữ liệu đến 30/6/2026, gồm khoảng 27 mã. Cột sàn của mọi mã đều là "HSX"; không có mã HNX nào. Đây là căn cứ của MJ4.
  - Rambachan và Roth (2023), mục 2.4.1, dòng 69024–69040: ràng buộc RM giới hạn **thay đổi giữa hai kỳ liên tiếp**, không giới hạn mức của hệ số. Đây là căn cứ của m4.
  - Coval và Moskowitz (1999), Loughran và Schultz (2005): không có trong hồ sơ, nên tôi chỉ ghi vào mục 5.
  - Bước giá: hồ sơ không có biểu bước giá gốc của HOSE và HNX (chỉ có một câu báo chí ở dòng 3788).

**Thứ tự gọi skill (bằng Skill tool, tuần tự):**
1. academic-paper-reviewer;
2. mhe-identification (Critic);
3. aer-identification;
4. review-methodology;
5. liquidity-measures;
6. statistical-power;
7. scientific-critical-thinking;
8. review-pap (chỉ đọc SKILL.md);
9. econ-write;
10. sciwrite.

**Lỗi và cách xử lý:**
- **academic-paper-reviewer.** Chế độ methodology-focus đòi sprint contract và agent con. Lỗi nguyên văn khi tìm contract: `ls: cannot access '/home/user/M-n_HTTM/.claude/skills/academic-paper-reviewer/shared/contracts/reviewer/': No such file or directory`. Phiên này cũng không có công cụ Agent. Vì vậy tôi tự đóng năm vai (Journal-Fit, Methodology, Domain, Perspective, Devil's Advocate) trong một ngữ cảnh. Năm vai này không độc lập và không được hiệu chuẩn (NOT_CALIBRATED). Tôi không chạy `check_acronyms.py`.
- **review-pap.** SKILL.md đòi 6 agent song song (`allowed-tools: … Agent`) và lưu file `reviews/PAP_REVIEW_*.md`. Phiên này không có công cụ Agent, nên tôi chỉ đọc SKILL.md và tự áp checklist của 6 agent trong cùng ngữ cảnh. Tôi không tạo file `reviews/`.
- **statistical-power.** Tôi không dùng `scripts/power.py` hay `simulate_power.py`, và không cài gói. Tôi tự viết ba script NumPy trong `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r10/sim/`: `interact_size.py`, `mde_interact.py` và `series_size.py`. Các script không dùng dữ liệu thật; mọi tham số đều là giả định.
- **mhe-identification.** Không có `references/sources/` (đã ghi ở đầu skill), nên tôi không dẫn trang sách MHE.
- Tôi không tra web và không gửi câu chữ của đề cương ra ngoài.

**Đối chiếu lỗi vòng 8:**
- Đã sửa đúng: CR1 (ngưỡng chung), CR2 (bootstrap tự hồi quy, hoán vị chỉ là kiểm tra bổ sung), MJ1 (Bai–Perron, cửa sổ 24 tháng), MJ2 (bước giá), MJ3 (MDE), cùng m1–m11.
- Còn sót từ CR1: quy tắc loại "ngày liền sau ngày chạm biên độ" vẫn phụ thuộc vào sàn (xem MJ1 dưới đây).

---

## (2) Tổng hợp

**0 CRITICAL, 5 MAJOR, 7 MINOR.**

Thiết kế H3 chính (δ, chuỗi dₜ, bootstrap tự hồi quy, MDE) nay đã vững. Các vấn đề còn lại tập trung ở phần mới của v10:

| Mã | Mức | idx | Một dòng |
|---|---|---|---|
| MJ1 | MAJOR | 224, 316, 215, 216 | Quy tắc loại "ngày liền sau ngày chạm biên độ" đổi theo sàn, nên tập ngày bị loại của nhóm xử lý thay đổi đúng lúc sự kiện xảy ra. |
| MJ2 | MAJOR | 323 | Giả định nhận dạng của các tương tác viết chưa đúng; thiếu hiệu ứng theo tháng riêng cho từng mức chịu cú sốc; chưa xử lý việc rời mẫu khác nhau theo mức chịu cú sốc. |
| MJ3 | MAJOR | 323, 344, 268 | Sai số chuẩn phân cụm theo cổ phiếu và hoán vị giữa các mã bác bỏ quá thường xuyên (mô phỏng: 13–64% ở mức danh nghĩa 5%). |
| MJ4 | MAJOR | 322, 112, 383 | Mức chịu cú sốc FTSE không có biến thiên trong nhóm chuyển sàn (danh sách FTSE chỉ có mã HOSE), lại được đo sau ngày tham chiếu, và mâu thuẫn với idx 333 và 335. |
| MJ5 | MAJOR | 324, 325 | Phân tích theo trụ sở nói quá ("Hà Nội mất gì") và đọc kết quả bằng 0 thành bằng chứng không có tác động. |
| m1 | MINOR | 112, 383 | "Tác động theo từng kênh" mâu thuẫn với câu "không đo riêng tác động của từng quy tắc". |
| m2 | MINOR | 221 | Ghi chú Bảng 2 gọi phân tích theo quy mô là mô tả, trong khi idx 323 ước lượng tương tác. |
| m3 | MINOR | 322 | Thước đo mức chịu cú sốc bước giá (1/giá) chưa phản ánh bước giá thay đổi theo vùng giá. |
| m4 | MINOR | 321 | Mô tả Rambachan–Roth chưa đúng ràng buộc RM; chưa nói tới 18 tháng chuyển tiếp. |
| m5 | MINOR | 324 | Mô tả Coval và Moskowitz (1999): đối tượng là nhà quản lý quỹ. |
| m6 | MINOR | 346 | Chưa nói giá trị p đưa vào Holm là một phía. |
| m7 | MINOR | nhiều | 17 đoạn dài hơn 180 âm tiết; đề xuất điểm tách. |

---

## (3) Phát hiện theo mức

### MAJOR

**MJ1. Quy tắc loại "ngày liền sau ngày chạm biên độ" phụ thuộc vào sàn, nên tập ngày bị loại của nhóm xử lý đổi đúng lúc chuyển sàn.**
- *idx:* 224, 316, 215, 216.
- *Skill:* liquidity-measures (mục 4.1–4.2), mhe-identification (đo lường, chọn mẫu theo quy tắc chịu ảnh hưởng của xử lý).
- *Lý do:*
  - Ngưỡng chung đã loại được độ chệch do lợi suất bị cắt. Tuy vậy, quy tắc thứ hai, "không liền sau một ngày chạm biên độ", vẫn định nghĩa theo biên độ của sàn đang giao dịch.
  - Trước sự kiện, mã chuyển sàn chỉ mất ngày liền sau một ngày chạm ±10%. Sau sự kiện, mã đó mất ngày liền sau mọi ngày có |r| từ khoảng 7%. Nhóm đối chứng HOSE áp cùng một quy tắc ở cả hai giai đoạn.
  - Vì vậy, chỉ ở nhóm xử lý, tập ngày tính Amihud thay đổi theo thời điểm xử lý. Những ngày liền sau một biến động lớn thường có giá trị giao dịch và |r| khác ngày thường, nên chiều của độ chệch không xác định trước.
  - Tỷ lệ ngày bị ảnh hưởng xấp xỉ chính mức chịu cú sốc biên độ ở idx 322. Mức này cao nhất ở mã nhỏ của HNX, nên độ chệch tập trung đúng ở hệ số tương tác theo biên độ.
  - Cách sửa: dùng một ngưỡng tuyệt đối 7%, áp như nhau cho mọi mã và mọi giai đoạn.
- *Sửa:*
  - idx 224. CHUỖI GỐC: `chỉ trên các ngày có lợi suất tuyệt đối dưới một ngưỡng chung thấp hơn biên độ ±7% (giá trị cụ thể ghi trong tệp đăng ký) và không liền sau một ngày chạm biên độ; giá trị giao dịch chỉ gồm giao dịch khớp lệnh;`
    → CHUỖI THAY THẾ: `chỉ trên các ngày có lợi suất tuyệt đối dưới một ngưỡng chung thấp hơn biên độ ±7% (giá trị cụ thể ghi trong tệp đăng ký) và không liền sau một ngày có lợi suất tuyệt đối từ 7% trở lên; quy tắc loại ngày liền sau áp dụng như nhau cho mọi cổ phiếu và mọi giai đoạn, kể cả khi cổ phiếu chuyển sàn còn giao dịch với biên độ ±10%, để tập ngày bị loại không thay đổi theo sàn; giá trị giao dịch chỉ gồm giao dịch khớp lệnh;`
  - idx 316. CHUỖI GỐC: `(thấp hơn biên độ ±7%) và không liền sau một ngày chạm biên độ;`
    → CHUỖI THAY THẾ: `(thấp hơn biên độ ±7%) và không liền sau một ngày có lợi suất tuyệt đối từ 7% trở lên;`
  - idx 215. CHUỖI GỐC: `tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày chạm biên độ, giảm so với nhóm đối chứng`
    → CHUỖI THAY THẾ: `tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày có lợi suất tuyệt đối từ 7% trở lên, giảm so với nhóm đối chứng`
  - idx 216. CHUỖI GỐC: `loại ngày liền sau ngày chạm biên độ (chính)`
    → CHUỖI THAY THẾ: `loại ngày liền sau ngày có lợi suất tuyệt đối từ 7% trở lên (chính)`

**MJ2. Giả định nhận dạng của các tương tác theo mức chịu cú sốc viết chưa đúng, và đặc tả còn thiếu hai thành phần.**
- *idx:* 323.
- *Skill:* mhe-identification, aer-identification (phần "Mechanism vs. Identification"), review-pap (Agent 2 và Agent 4: phân tích dị biệt phải được đặc tả cụ thể), econ-write (phương trình phải được nêu).
- *Lý do:*
  - Hệ số của Dᵢ·Postₜ·Eₛ,ᵢ so sánh mã chuyển sàn chịu cú sốc mạnh với mã chuyển sàn chịu cú sốc yếu. Hiệu ứng τₜ khử được cú sốc chung cho mọi mã, nhưng không khử được cú sốc chung **tác động khác nhau theo Eₛ,ᵢ**. Ví dụ, dòng tiền nhà đầu tư cá nhân năm 2027 có thể làm tăng thanh khoản của mã nhỏ, giá thấp và biến động mạnh nhiều hơn mã khác.
  - Câu "biến động song song với nhóm đối chứng" ở idx 323 không nói giả định nào thực sự cần. Giả định cần là: nếu không chuyển sàn, khoảng cách giữa mã chuyển sàn có E cao và mã chuyển sàn có E thấp sẽ biến động như khoảng cách tương ứng ở nhóm đối chứng.
  - Muốn dùng nhóm đối chứng cho giả định này, phương trình cần thêm số hạng Eₛ,ᵢ·τₜ, ước lượng trên các mã đối chứng đo được cùng thước đo. Lưu ý: với mã HOSE, tỷ lệ ngày có |r| từ 7% đến dưới 10% luôn bằng 0. Vì vậy mức chịu cú sốc biên độ chỉ đo được trên mã UPCoM (biên độ ±15%).
  - Mã chịu cú sốc biên độ mạnh cũng là mã mất nhiều ngày nhất khi tính Amihud sau sự kiện, nên dễ bị ghi là tháng thiếu. Đây là rời mẫu khác nhau theo đúng biến tương tác.
  - Phương trình mở rộng hiện chưa được viết ra, nên một người thứ ba chưa tái lập được phân tích từ tệp đăng ký.
- *Sửa (idx 323).* CHUỖI GỐC: `Phương trình (5) được mở rộng bằng các số hạng tương tác giữa Dᵢ·Postₜ và từng mức chịu cú sốc đã chuẩn hóa. Giả định nhận dạng là: nếu không chuyển sàn, chênh lệch thanh khoản giữa mã chịu cú sốc mạnh và mã chịu cú sốc yếu biến động song song với nhóm đối chứng; giả định này được kiểm tra bằng các hệ số trước sự kiện của cùng các tương tác.`
  → CHUỖI THAY THẾ: `Phương trình (5) được mở rộng bằng các số hạng Dᵢ·Postₜ·Eₛ,ᵢ, trong đó Eₛ,ᵢ là mức chịu cú sốc s của cổ phiếu i, chuẩn hóa theo độ lệch chuẩn giữa các mã chuyển sàn, và bằng các số hạng Eₛ,ᵢ·τₜ để mỗi mức chịu cú sốc có hiệu ứng theo tháng riêng; các số hạng Eₛ,ᵢ·τₜ được ước lượng trên những mã đối chứng đo được cùng thước đo, tức mã UPCoM với mức chịu cú sốc biên độ và mã HOSE với hai mức còn lại. Giả định nhận dạng là: nếu không chuyển sàn, chênh lệch thanh khoản giữa mã chuyển sàn chịu cú sốc mạnh và mã chuyển sàn chịu cú sốc yếu sẽ biến động như chênh lệch tương ứng giữa các mã đối chứng; giả định này được kiểm tra bằng các hệ số trước sự kiện của cùng các tương tác. Tỷ lệ ngày bị loại và tỷ lệ tháng thiếu được báo cáo theo ba nhóm mức chịu cú sốc biên độ, và các hệ số tương tác được ước lượng lại trên những mã đủ số ngày hợp lệ ở cả hai giai đoạn.`

**MJ3. Suy luận cho hệ số tương tác (phân cụm theo cổ phiếu, hoán vị giữa các mã) bác bỏ quá thường xuyên trong thiết kế một sự kiện.**
- *idx:* 323, 344, 268.
- *Skill:* statistical-power (mô phỏng), mhe-identification (phần Finance calibration: phân cụm theo doanh nghiệp không hợp lệ khi biến thiên xử lý nằm ở cấp thời gian), econ-write (phân cụm theo cấp gán xử lý).
- *Lý do:*
  - Biến thiên theo Eₛ,ᵢ nằm giữa các mã, nhưng mọi mã chịu chung một chuỗi cú sốc theo tháng. Nếu mức tác động của cú sốc chung tương quan với Eₛ,ᵢ, ước lượng tương tác chứa một sai số chung cho mọi mã.
  - Sai số chuẩn phân cụm theo cổ phiếu không thấy sai số chung này. Hoán vị Eₛ,ᵢ giữa các mã cũng không thấy, vì phân phối hoán vị xoay quanh 0. Đây cùng loại lỗi đã sửa cho δ ở vòng 8 (CR2).
  - Mô phỏng (`interact_size.py`, 1.000 lần, giả thuyết không đúng, không có dị biệt thật):
    - Thiết lập: 299 mã; 24 tháng trước và 24 tháng sau; nhân tố chung AR(1) với φ = 0,6; nhiễu riêng AR(1) với φ = 0,5 và độ lệch chuẩn 0,5; hệ số tải của mã i bằng c·Eᵢ cộng nhiễu.
    - Tỷ lệ bác bỏ ở mức danh nghĩa 5%:

      | c | Phân cụm theo cổ phiếu | Hoán vị |
      |---|---|---|
      | 0 | 0,052 | 0,043 |
      | 0,02 | 0,129 | 0,116 |
      | 0,05 | 0,358 | 0,350 |
      | 0,10 | 0,641 | 0,629 |

    - Cách khác: ước lượng hệ số tương tác riêng cho từng tháng, rồi kiểm định trên chuỗi tháng bằng mô hình AR (`series_size.py`). Với 193 tháng trước, tỷ lệ bác bỏ là 0,052 (c = 0,05) và 0,053 (c = 0). Với 60 tháng trước, tỷ lệ là 0,096 khi chỉ dùng ước lượng AR thay thẳng vào, tức bootstrap có hiệu chỉnh độ chệch như đề cương đã nêu cho δ là cần thiết.
  - idx 344 nói công suất "chỉ phụ thuộc yếu vào số cổ phiếu". Câu này đúng cho δ, nhưng chưa nói gì về các hệ số tương tác.
- *Sửa:*
  - idx 323. CHUỖI GỐC: `Vì biến thiên này nằm giữa các mã trong cùng một sự kiện, sai số chuẩn của hệ số tương tác được phân cụm theo cổ phiếu và kèm suy diễn hoán vị, trong đó mức chịu cú sốc được xáo trộn giữa các mã chuyển sàn. Các hệ số tương tác là phân tích phụ được đăng ký trước và không đưa vào thủ tục Holm.`
    → CHUỖI THAY THẾ: `Sai số chuẩn phân cụm theo cổ phiếu và suy luận hoán vị xáo trộn mức chịu cú sốc giữa các mã chuyển sàn đều coi các mã là độc lập, nên bác bỏ quá thường xuyên khi cú sốc chung theo tháng tác động mạnh hơn lên mã chịu cú sốc mạnh. Suy luận chính cho mỗi hệ số tương tác vì vậy dùng cùng thủ tục với δ: đề tài ước lượng hệ số tương tác riêng cho từng tháng, rồi áp dụng bootstrap tự hồi quy cho chuỗi hệ số theo tháng này; sai số chuẩn phân cụm theo cổ phiếu và giá trị p hoán vị chỉ được báo cáo kèm. Hiệu ứng nhỏ nhất phát hiện được của từng hệ số tương tác được tính theo cùng thủ tục và ghi vào tệp đăng ký. Các hệ số tương tác, kể cả tương tác theo trụ sở dưới đây, là phân tích phụ được đăng ký trước và không đưa vào thủ tục Holm.`
  - idx 344. CHUỖI GỐC: `và phần nhiễu riêng của từng mã đã được bình quân trong chuỗi chênh lệch.`
    → CHUỖI THAY THẾ: `và phần nhiễu riêng của từng mã đã được bình quân trong chuỗi chênh lệch. Với các hệ số tương tác ở mục 4.3.7, số cổ phiếu chỉ quyết định phần nhiễu riêng; nếu cú sốc chung theo tháng tác động khác nhau theo mức chịu cú sốc, công suất của các hệ số này cũng bị giới hạn bởi số tháng như với δ.`
  - idx 268. CHUỖI GỐC: `định nghĩa ba mức chịu cú sốc và biến trụ sở tại Hà Nội;`
    → CHUỖI THAY THẾ: `định nghĩa ba mức chịu cú sốc và biến trụ sở tại Hà Nội, đặc tả và thủ tục suy luận cho các hệ số tương tác;`

**MJ4. Mức chịu cú sốc "chỉ số FTSE" không có biến thiên trong nhóm chuyển sàn, được đo sau ngày tham chiếu, và nhầm một cú sốc trùng thời gian thành một kênh của việc chuyển sàn.**
- *idx:* 322; liên quan tới 323, 333, 335, 112, 383.
- *Skill:* mhe-identification (nguồn biến thiên), review-pap (Agent 2: biến phân nhóm phải đo được), scientific-critical-thinking.
- *Lý do:*
  - FTSE Russell FAQ v1.3 (mục [30] của hồ sơ, câu hỏi 6) liệt kê các mã đủ điều kiện từ ngày 21/9/2026. Danh sách tính trên dữ liệu đến 30/6/2026, và mọi mã đều có cột sàn "HSX". Biến "mã thuộc danh sách dự kiến của FTSE Russell" vì vậy bằng 0 với mọi mã chuyển sàn, và hệ số tương tác không ước lượng được.
  - idx 323 nói "Mọi mức chịu cú sốc được đo trước ngày 30/6/2025". Danh sách FTSE lại dựa trên dữ liệu đến 30/6/2026.
  - idx 322 coi việc vào chỉ số FTSE là một trong "ba quy tắc" mà việc chuyển sàn thay đổi. Ngược lại, idx 333 coi FTSE là cú sốc trùng thời gian tác động lên nhóm đối chứng, và idx 335 kể ba quy tắc là "biên độ dao động giá, hệ thống giao dịch và tư cách thành phần chỉ số".
  - Kênh chỉ số thực sự do việc chuyển sàn gây ra là việc vào VN-Index và các chỉ số của HOSE (idx 333).
- *Sửa:*
  - idx 322. CHUỖI GỐC: `và việc vào chỉ số FTSE chỉ liên quan đến mã có trong danh sách dự kiến.`
    → CHUỖI THAY THẾ: `và việc vào VN-Index cùng các chỉ số khác do HOSE xây dựng có thể tạo áp lực cầu lớn hơn ở mã có vốn hóa tự do chuyển nhượng lớn so với giá trị giao dịch [CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong VN-Index].`
  - idx 322. CHUỖI GỐC: `và biến chỉ mã thuộc danh sách dự kiến của FTSE Russell (mức chịu cú sốc chỉ số).`
    → CHUỖI THAY THẾ: `và tỷ số giữa vốn hóa tự do chuyển nhượng và giá trị giao dịch bình quân ngày (mức chịu cú sốc chỉ số). Việc FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số không được coi là một kênh của việc chuyển sàn, vì danh sách cổ phiếu đủ điều kiện từ ngày 21/9/2026 chỉ gồm mã niêm yết tại HOSE (FTSE Russell, 2026); sự kiện này được xử lý như một cú sốc trùng thời gian ở mục 4.3.8.`
  - idx 335. CHUỖI GỐC: `Việc chuyển sàn đổi cùng lúc biên độ dao động giá, hệ thống giao dịch và tư cách thành phần chỉ số,`
    → CHUỖI THAY THẾ: `Việc chuyển sàn đổi cùng lúc biên độ dao động giá, bước giá, hệ thống giao dịch và tư cách thành phần chỉ số của HOSE,`

**MJ5. Phân tích theo trụ sở nói quá điều thiết kế đo được, và đọc kết quả bằng 0 thành bằng chứng không có tác động.**
- *idx:* 324, 325.
- *Skill:* scientific-critical-thinking (phân biệt bằng chứng chống một khẳng định với bằng chứng ủng hộ giả thuyết không), review-methodology (ngôn ngữ nhân quả), econ-write (cách trình bày kết quả bằng 0), statistical-power.
- *Lý do:*
  - Tương tác Dᵢ·Postₜ·HNᵢ so sánh mã có trụ sở tại Hà Nội với mã ở nơi khác, khi **cả hai cùng chuyển sang HOSE**. Hệ số này không đo được "phần thanh khoản mà thị trường vốn Hà Nội mất". Lượng giao dịch chuyển sang HOSE với mọi mã, và không có nhóm nào giữ sàn ở Hà Nội.
  - Câu "nếu chênh lệch bằng 0, kết quả cho thấy vị trí sàn ít quan trọng" trái với quy tắc ở idx 348.
  - Ước tính minh họa (`mde_interact.py`): giả định độ lệch chuẩn của thay đổi logarit Amihud ở cấp mã là 0,5, 299 mã, một nửa có trụ sở tại Hà Nội, không có cú sốc chung tác động khác nhau theo trụ sở, kiểm định hai phía 5% và công suất 80%. Khi đó MDE ≈ 0,16 log điểm, tương đương khoảng 15% Amihud. Với độ lệch chuẩn 0,7, MDE ≈ 0,23. Đây chỉ là cận dưới; nếu có cú sốc chung tác động khác nhau theo trụ sở, MDE lớn hơn (xem MJ3).
  - Ngoài ra, idx 324 chưa nói phân tích này nằm ngoài thủ tục Holm. Câu thay thế ở MJ3 đã bổ sung.
- *Sửa:*
  - idx 324. CHUỖI GỐC: `Phân tích theo trụ sở doanh nghiệp cho biết Hà Nội mất gì khi cổ phiếu niêm yết rời HNX.`
    → CHUỖI THAY THẾ: `Phân tích theo trụ sở doanh nghiệp kiểm tra xem việc chuyển sàn có tác động khác nhau đến doanh nghiệp có trụ sở tại Hà Nội và doanh nghiệp ở nơi khác hay không.`
  - idx 325. CHUỖI GỐC: `Nếu chênh lệch khác 0, kết quả cho biết phần thanh khoản mà thị trường vốn Hà Nội mất cùng với sàn cổ phiếu niêm yết; nếu chênh lệch bằng 0, kết quả cho thấy vị trí sàn ít quan trọng với doanh nghiệp Hà Nội khi giao dịch đã điện tử hóa toàn quốc. Cả hai trường hợp đều là đầu vào định lượng cho định hướng chuyên môn hóa ở cuối mục 4.3.8.`
    → CHUỖI THAY THẾ: `Hệ số tương tác dương, tức độ phi thanh khoản của doanh nghiệp Hà Nội giảm ít hơn, phù hợp với giả thuyết sàn đặt cùng thành phố tạo lợi thế cho doanh nghiệp địa phương, nhưng không đo lượng thanh khoản mà thị trường vốn Hà Nội mất, vì mọi mã trong phép so sánh đều chuyển sang HOSE. Chênh lệch chỉ được coi là không đáng kể khi khoảng tin cậy loại trừ những giá trị lớn hơn hiệu ứng nhỏ nhất phát hiện được ghi trong tệp đăng ký; nếu không, kết quả được gọi là chưa đủ cơ sở kết luận theo quy tắc ở mục 4.3.10. Trong mọi trường hợp, kết quả là đầu vào định lượng cho định hướng chuyên môn hóa ở cuối mục 4.3.8.`

### MINOR

**m1. "Tác động theo từng kênh" trái với câu ở idx 323 rằng hệ số tương tác "không đo riêng tác động của từng quy tắc".** idx 112, 383. Skill: review-methodology, sciwrite (pass 4: thống nhất thuật ngữ).
- idx 112. CHUỖI GỐC: `kể cả tác động theo từng kênh biên độ, bước giá và chỉ số, và khác biệt`
  → CHUỖI THAY THẾ: `kể cả mức thay đổi của tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số, và khác biệt`
- idx 383. CHUỖI GỐC: `6.1.1 Tác động theo kênh biên độ, bước giá và chỉ số`
  → CHUỖI THAY THẾ: `6.1.1 Tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số`

**m2. Ghi chú Bảng 2 gọi so sánh theo quy mô là phân tích mô tả, trong khi idx 323 ước lượng tương tác với quy mô và coi các tương tác là phân tích phụ đăng ký trước.** idx 221. Skill: review-pap (Agent 2: phân biệt mô tả, phụ và xác nhận).
- CHUỖI GỐC: `so sánh theo giai đoạn căng thẳng và theo quy mô doanh nghiệp là phân tích mô tả.`
  → CHUỖI THAY THẾ: `so sánh theo giai đoạn căng thẳng là phân tích mô tả; tương tác của tác động H3 với mức chịu cú sốc, quy mô và trụ sở doanh nghiệp là phân tích phụ đăng ký trước, không đưa vào thủ tục Holm.`

**m3. Mức chịu cú sốc bước giá (nghịch đảo giá) chưa phản ánh việc bước giá có thể thay đổi theo vùng giá.** idx 322. Skill: liquidity-measures (mục 4.3).
- Lý do: thay đổi bước giá tương đối khi chuyển sàn bằng (bước giá HNX − bước giá HOSE tại mức giá p)/p. Nếu bước giá của HOSE thay đổi theo vùng giá, thay đổi này không tỷ lệ với 1/p [CẦN XÁC MINH quy định bước giá theo từng thời kỳ]. Ngoài ra, bước giá tác động chủ yếu lên tỷ lệ ngày lợi suất bằng 0, ít tác động lên Amihud.
- CHUỖI GỐC: `nghịch đảo của giá đóng cửa bình quân (mức chịu cú sốc bước giá)`
  → CHUỖI THAY THẾ: `nghịch đảo của giá đóng cửa bình quân (mức chịu cú sốc bước giá; kết quả được báo cáo thêm với mức thay đổi của bước giá tương đối khi chuyển sàn, tính từ quy định bước giá của hai sàn tại ngày 30/6/2025, và trên tỷ lệ ngày lợi suất bằng 0)`

**m4. Mô tả Rambachan–Roth chưa đúng ràng buộc RM.** idx 321. Skill: aer-identification (Honest DiD).
- Lý do: theo Rambachan và Roth (2023, mục 2.4.1), RM(M̄) giới hạn thay đổi giữa hai kỳ liên tiếp của độ lệch sau xử lý bằng M̄ lần thay đổi lớn nhất giữa hai kỳ liên tiếp trước xử lý. Ràng buộc không giới hạn "độ lệch lớn nhất của các hệ số". Ngoài ra, 18 tháng chuyển tiếp nằm giữa tháng gốc và giai đoạn sau, nên khoảng tin cậy có thể rất rộng.
- CHUỖI GỐC: `và báo cáo độ nhạy của kết luận khi xu hướng song song bị vi phạm ở mức tương đương độ lệch lớn nhất của các hệ số này, tức các tháng trước giai đoạn chuyển tiếp (Rambachan & Roth, 2023).`
  → CHUỖI THAY THẾ: `và báo cáo độ nhạy của kết luận khi thay đổi giữa hai tháng liên tiếp của độ lệch khỏi xu hướng song song sau tháng gốc không vượt M̄ lần thay đổi lớn nhất giữa hai tháng liên tiếp trong các tháng 1/2024–6/2025, kèm giá trị M̄ nhỏ nhất làm kết luận thay đổi (Rambachan & Roth, 2023); vì giữa tháng gốc và giai đoạn sau có 18 tháng chuyển tiếp, khoảng tin cậy theo cách này có thể rất rộng.`

**m5. Mô tả Coval và Moskowitz (1999).** idx 324. Skill: econ-write (độ chính xác của trích dẫn), sciwrite (pass 5). Đối tượng của bài là nhà quản lý quỹ ở Mỹ, không phải "nhà đầu tư" nói chung. Nhãn [CẦN ĐỐI CHIẾU] được giữ.
- CHUỖI GỐC: `nhà đầu tư ưa nắm giữ cổ phiếu của doanh nghiệp ở gần mình (Coval & Moskowitz, 1999)`
  → CHUỖI THAY THẾ: `nhà quản lý quỹ ưa nắm giữ cổ phiếu của doanh nghiệp có trụ sở gần mình (Coval & Moskowitz, 1999)`

**m6. Chưa nói giá trị p đưa vào Holm là một phía.** idx 346. Skill: review-pap (Agent 4). idx 345 tính MDE với "mức ý nghĩa một phía", nên quy tắc Holm cần nói cùng điều đó.
- CHUỖI GỐC: `là giá trị p phân cụm theo quốc gia cho H1, giá trị p bootstrap khối cho H2 và giá trị p bootstrap tự hồi quy cho H3.`
  → CHUỖI THAY THẾ: `là giá trị p một phía theo chiều của từng giả thuyết: giá trị p phân cụm theo quốc gia cho H1, giá trị p bootstrap khối cho H2 và giá trị p bootstrap tự hồi quy cho H3.`

**m7. Có 17 đoạn dài hơn 180 âm tiết.** Skill: sciwrite (pass 3), econ-write (mỗi đoạn một ý). Các đoạn: idx 95, 112, 114, 129, 152, 224, 229, 268, 271, 278, 279, 316, 323, 324, 333, 345, 389. Ký hiệu ¶ đánh dấu chỗ xuống đoạn mới. Không cần thêm chữ.
- **idx 316.** Hiện là một câu duy nhất, chứa cả định nghĩa biến và quy tắc điểm gãy.
  - CHUỖI GỐC: `chỉ được ước lượng trong phương trình (6); vì giai đoạn tham chiếu dài 16 năm,`
    → CHUỖI THAY THẾ: `chỉ được ước lượng trong phương trình (6); αi và τt là hiệu ứng cố định theo cổ phiếu và theo tháng.¶Vì giai đoạn tham chiếu dài 16 năm,`
  - Đồng thời, CHUỖI GỐC: `(7/2023–6/2025); αi và τt là hiệu ứng cố định theo cổ phiếu và theo tháng.`
    → CHUỖI THAY THẾ: `(7/2023–6/2025).`
  - Lưu ý: "i" và "t" là chỉ số dưới, như trong bản Word.
- **idx 323** (sau khi áp MJ2 và MJ3): xuống đoạn trước `Hệ số tương tác cho biết tác động thay đổi thế nào` và trước `Sai số chuẩn phân cụm theo cổ phiếu và suy luận hoán vị`.
- **idx 333:** xuống đoạn trước `Vì vậy nhóm đối chứng HOSE loại các mã` và trước `Ngoài ra, Ủy ban Chứng khoán Nhà nước cho biết`.
- **idx 224:** xuống đoạn trước `Đề tài vì vậy tính Amihud, ở cả hai nhóm và cả hai giai đoạn`.
- **idx 229:** xuống đoạn trước `Ngày cổ phiếu bị đình chỉ giao dịch bị loại` và trước `Giai đoạn căng thẳng chỉ dùng cho phân tích mô tả`.
- **idx 345:** xuống đoạn trước `Chẳng hạn, với σ = 0,2 và φ = 0,6`.
- **idx 112:** xuống đoạn trước `Đề tài có bốn mục tiêu cụ thể.` và trước `Trong bốn giả thuyết, H3 là kiểm định trọng tâm`.
- **idx 271:** xuống đoạn trước `Đề tài dùng hai cấu hình chi phí.`
- **idx 279:** xuống đoạn trước `Vì số cửa sổ ít và lợi suất tương đương chắc chắn có phương sai lớn`.
- **idx 278:** xuống đoạn trước `Giữ nguyên thành phần rổ giúp so sánh`.
- **idx 268:** đây là danh sách, nên giữ nguyên hoặc chuyển thành gạch đầu dòng.
- **idx 95, 114, 129, 152, 324, 389:** mỗi đoạn vượt ngưỡng ít (dưới 205 âm tiết) và chỉ có một ý, nên có thể giữ nguyên.

---

## (4) Nhận định ngắn theo từng skill

**1. academic-paper-reviewer** (năm vai trong một ngữ cảnh, không độc lập, NOT_CALIBRATED).
- *Journal-Fit:* Ở mức tạp chí vi cấu trúc thị trường (JFM, RF, JFQA), H3 với δ, bootstrap tự hồi quy và MDE công khai đã đủ chặt. Phần mở rộng theo mức chịu cú sốc là phần một biên tập viên sẽ hỏi đầu tiên, vì đây là chỗ bài báo trả lời được câu hỏi "vì sao". Phần này cần cùng độ chặt suy luận với δ (MJ2, MJ3).
- *Methodology:* MJ1, MJ2, MJ3.
- *Domain:* MJ4 (FTSE không phải kênh của việc chuyển sàn), m3 (bước giá).
- *Perspective:* MJ5. Ý nối với Hà Nội có giá trị chính sách, nhưng hiện nói quá điều thiết kế đo được.
- *Devil's Advocate:* Phản biện mạnh nhất là một hệ số tương tác "có ý nghĩa" có thể chỉ phản ánh việc thanh khoản của mã nhỏ, giá thấp và biến động mạnh tăng chung trong năm 2027, cộng với sai số chuẩn quá nhỏ. Mô phỏng ở MJ3 xác nhận rủi ro này. Tôi không xếp mức CRITICAL vì các tương tác nằm ngoài Holm và không quyết định H3.
- *Tín hiệu tổng hợp:* sửa vừa. Không có lỗi nào làm hỏng kiểm định xác nhận H3. MJ1 là lỗi duy nhất chạm tới δ, và cách sửa đơn giản.

**2. mhe-identification (Critic).**
- Câu hỏi viết lại theo kết quả tiềm năng: với các mã niêm yết tại HNX, log Amihud khi giao dịch trên HOSE trừ log Amihud nếu vẫn ở HNX, trong 24 tháng. Phần mở rộng hỏi hiệu số này thay đổi thế nào theo Eₛ,ᵢ và theo trụ sở.
- Nguồn biến thiên: một quy định cho cả sàn; với các tương tác, thêm biến thiên chéo giữa các mã theo đặc điểm đo trước xử lý.
- Đạt: mức chịu cú sốc, quy mô và trụ sở đều đo tại 30/6/2025, nên không phải kiểm soát xấu (trừ biến FTSE, MJ4).
- Chưa đạt: (i) đo lường. Quy tắc loại ngày phụ thuộc vào xử lý (MJ1). (ii) Nhận dạng của tương tác. Cần xu hướng song song theo từng mức chịu cú sốc, có E×τ (MJ2). (iii) Suy luận. Phân cụm theo doanh nghiệp không hợp lệ khi biến thiên quyết định nằm ở cấp thời gian (MJ3).
- Kết luận: δ đo được tác động gộp của sàn. Các tương tác hiện mới là mô tả dị biệt; sau khi sửa MJ2 và MJ3, chúng thành bằng chứng có điều kiện về kênh tác động, nhưng không tách riêng được từng quy tắc. Đề cương đã nói đúng điều này.

**3. aer-identification.**
- Thiết kế 2×2, một ngày xử lý, không có xử lý so le: TWFE chấp nhận được.
- Phương án dự phòng dùng Callaway và Sant'Anna khi chuyển theo nhiều đợt: đúng.
- Với tương tác theo biến liên tục, mức tác động so sánh giữa các mức E cần giả định song song mạnh hơn, nên cần xử lý MJ2. Văn liệu về khác biệt kép với xử lý liên tục nên được đọc (mục 5).
- Rambachan–Roth: mô tả cần sửa, và nên báo cáo giá trị M̄ làm kết luận đổi (m4).

**4. review-methodology.**
- Ngôn ngữ nhân quả: H1 là liên hệ, H3 là tác động gộp. Hai chỗ còn nói quá: "Hà Nội mất gì" và "phần thanh khoản mà thị trường vốn Hà Nội mất" (MJ5), cùng "tác động theo từng kênh" (m1).
- Dữ liệu thiếu: rời mẫu khác nhau theo mức chịu cú sốc biên độ (MJ2).
- Điểm mạnh: mọi biến dị biệt đều đo trước sự kiện; đề cương tự nêu giới hạn "không đo riêng tác động của từng quy tắc".

**5. liquidity-measures.**

| Chỉ báo | Chiều | Định nghĩa đã đủ? | Bẫy ở mục 4 | Thiếu gì |
|---|---|---|---|---|
| Amihud (H3) | tác động giá | gần đủ: ngưỡng chung, chỉ khớp lệnh, số ngày tối thiểu, winsorize | 4.1 (ngày liền sau), 4.2 | quy tắc ngày liền sau độc lập với sàn (MJ1) |
| Tỷ lệ ngày lợi suất bằng 0 | chi phí | đủ, theo nhóm giá | 4.3 | đọc kênh bước giá trên chỉ báo này (m3) |
| Corwin–Schultz | chi phí | đủ ở mức đề cương | 4.1, 4.3 | cách xử lý ước lượng âm: để tệp đăng ký |
| Vòng quay | hoạt động | ghi là đối chiếu | không | nói rõ dùng số cổ phiếu lưu hành hay tự do chuyển nhượng (tệp đăng ký) |

Mô tả văn liệu ở idx 125 và 231 (Amihud 2002, LOT 1999, Corwin–Schultz 2012, Bekaert và cộng sự 2007, Fong và cộng sự 2017) khớp với nội dung chung của các bài. Tôi không thấy câu nào nói "tốt nhất" mà không có căn cứ.

**6. statistical-power.**
- MDE của δ ở idx 345 khớp với bảng vòng 8: 0,64σ, 1,24σ, 1,76σ; hệ số 1,3 lần khi cửa sổ trước còn 24 tháng; ví dụ 0,25 log điểm, tức khoảng 22%. Mức ý nghĩa một phía 0,05/3 khớp với thủ tục Holm, nhưng idx 346 cần nói p một phía (m6).
- Các hệ số tương tác chưa có MDE và chưa có thủ tục kiểm định đúng kích thước (MJ3). Cận dưới minh họa, khi không có cú sốc chung tác động khác nhau theo E (đều là giả định):
  - Trụ sở, một nửa mẫu tại Hà Nội: MDE 0,10, 0,16 và 0,23 log điểm khi độ lệch chuẩn của thay đổi ở cấp mã là 0,3, 0,5 và 0,7.
  - Mỗi độ lệch chuẩn của E, khi E tương quan với các biến khác ở mức R² = 0,5: MDE 0,07, 0,12 và 0,16.
- Theo pitfall 7 của skill (chỉ tính công suất cho kết quả chính), cần ghi MDE của tương tác vào tệp đăng ký. Câu thay thế ở MJ3 đã gồm điều này.

**7. scientific-critical-thinking.**
- Cần phân biệt "không bác bỏ" với "bằng 0" ở phân tích trụ sở (MJ5).
- Không nhầm cú sốc trùng thời gian (FTSE) với cơ chế của xử lý (MJ4).
- Điểm mạnh: đề cương tự nêu giới hạn "các mức chịu cú sốc có thể tương quan với nhau và với quy mô".

**8. review-pap** (áp checklist 6 agent trong một ngữ cảnh; không có công cụ Agent, không tạo file `reviews/`).
- *Agent 1 (đặc tả):* phương trình mở rộng chưa viết ra; cách chuẩn hóa E chưa nói. Sửa ở MJ2.
- *Agent 2 (nhất quán):* idx 322, 333 và 335 kể khác nhau về "ba quy tắc" (MJ4); idx 221 và 323 khác nhau về quy mô (m2); "suy diễn hoán vị" ở idx 323 khác "suy luận hoán vị" ở idx 268 (câu thay ở MJ3 thống nhất lại).
- *Agent 3 (nhận dạng):* MJ2, MJ4, MJ5.
- *Agent 4 (thống kê):* MJ3 và m6. Tương tác đã đứng ngoài Holm, đúng. Tương tác theo trụ sở chưa được nói rõ (đã bổ sung ở MJ3).
- *Agent 5 (dữ liệu):* biến trụ sở lấy theo "địa chỉ đăng ký tại ngày 30/6/2025", cần nói nguồn. Đây là chi tiết cho tệp đăng ký, tôi không nêu thành phát hiện.
- *Agent 6 (khuyến nghị):* "Competitive". Đăng ký sau khi sửa MJ1–MJ5. Không cần thiết kế lại.

**9. econ-write.**
- Văn phong rõ, câu có chủ ngữ, không có từ quảng cáo.
- Theo quy tắc phân tích dị biệt, cần nêu số tương tác được kiểm định và đánh dấu đó là phân tích phụ (m2, MJ3).
- Theo quy tắc phương trình, phương trình mở rộng phải được giới thiệu bằng lời và định nghĩa biến (MJ2).
- Câu chủ đề "Một sự kiện duy nhất không có nghĩa là mọi cổ phiếu chịu cùng một cú sốc" mở đoạn tốt.

**10. sciwrite** (5 pass, áp cho tiếng Việt học thuật).
- *Pass 1 (từ thừa):* ít. Có thể bỏ "một cách cơ học" ở lần lặp thứ hai trong idx 224, nhưng không bắt buộc.
- *Pass 2 (chủ động):* câu bị động kiểu "được báo cáo", "được ước lượng" phù hợp với phần phương pháp; không có câu bị động che chủ thể.
- *Pass 3 (cấu trúc câu):* idx 316 là một câu khoảng 200 âm tiết, nối bằng dấu chấm phẩy; vị ngữ của phần điểm gãy bị chôn sâu (m7).
- *Pass 4 (thuật ngữ):* có ba lệch: "kênh" và "mức chịu cú sốc" (m1); "suy diễn hoán vị" và "suy luận hoán vị" (MJ3); "ngày chạm biên độ" mang hai nghĩa sau khi có ngưỡng chung (MJ1).
- *Pass 5 (số và trích dẫn):* kiểm tra 299 mã, 20 và 8 cửa sổ, 18 tháng chuyển tiếp, 193 tháng, các hệ số MDE và mốc FTSE; tất cả khớp. Coval và Moskowitz cần sửa (m5).

---

## (5) Tài liệu cần tìm mới

| # | Tài liệu | Vì sao | idx | Nơi tìm và từ khóa | Ưu tiên |
|---|---|---|---|---|---|
| 1 | Coval, J. D., & Moskowitz, T. J. (1999), toàn văn | MJ5, m5: đối chiếu đối tượng (nhà quản lý quỹ) và khẳng định | 324 | Wiley/JSTOR; "Home bias at home local equity preference" | Cao |
| 2 | Loughran, T., & Schultz, P. (2005), toàn văn | MJ5: thanh khoản theo vị trí trụ sở; định nghĩa urban và rural | 324 | ScienceDirect; "Liquidity: Urban versus rural firms" | Cao |
| 3 | Quy tắc đủ điều kiện của FTSE GEIS với cổ phiếu niêm yết tại HNX, và kết quả kỳ rà soát tháng 3/2027 | MJ4: xác nhận mã chuyển sàn có thể được thêm vào chỉ số FTSE sau khi lên HOSE hay không | 322, 333 | lseg.com/ftse-russell; "FTSE GEIS ground rules Vietnam eligible exchange", "Vietnam HNX FTSE eligibility" | Cao |
| 4 | Biểu bước giá của HOSE và HNX theo từng thời kỳ (đã có trong danh sách vòng 8, chưa có trong hồ sơ) | m3, MJ2 | 223, 322 | Quy chế giao dịch của HOSE và HNX; "đơn vị yết giá HOSE", "bước giá HNX 100 đồng" | Cao |
| 5 | Bài về khác biệt kép với xử lý liên tục, nhóm tác giả Callaway, Goodman-Bacon và Sant'Anna [CẦN XÁC MINH năm, nơi đăng] | MJ2: giả định cần để so sánh tác động giữa các mức E | 323 | NBER/arXiv; "Difference-in-differences with a continuous treatment" | Trung bình |
| 6 | Quy tắc chỉ số VN-Index và VNAllshare với mã chuyển sàn (QĐ 737, 738/QĐ-SGDHCM, bản PDF gốc) | MJ4: kênh chỉ số thực của việc chuyển sàn | 322, 333 | stream.vnx.vn; "Quy tắc chỉ số VNINDEX phiên bản 1.0", "cổ phiếu niêm yết mới" | Trung bình |
| 7 | Nguồn địa chỉ trụ sở doanh nghiệp tại ngày 30/6/2025 (báo cáo thường niên, Cổng thông tin quốc gia về đăng ký doanh nghiệp, nhà cung cấp dữ liệu) | MJ5, review-pap Agent 5 | 324 | Cổng đăng ký doanh nghiệp quốc gia; FiinPro | Thấp |

Script mô phỏng: `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r10/sim/interact_size.py`, `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r10/sim/mde_interact.py`, `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r10/sim/series_size.py`.
