# R15 – Vòng 1 – Phản biện A: bản dài LaTeX (latex/ban-dai/)

Đối chiếu với: `outputs/round-14/v14-text-round-14.txt` (văn bản v14), công thức lấy từ `outputs/round-14/de-cuong-v14-round-14.docx` (OMML), `ho-so/QD-1193-QD-UBND-2026-bai-toan-lon-dot-1.pdf` (bài toán số 19).
Skill đã nạp: consistency-checker, fact-checker, review-methodology, mhe-identification, panel-data-guide, statistical-power, liquidity-measures, latex-econ-model, credible-claims.

## 0. Những gì đã kiểm và thấy ĐÚNG (không cần sửa)

- **Sự kiện, số liệu, mốc của v14:** khi đối chiếu từng đoạn, không thấy số, ngày, tên văn bản, ngưỡng, số cửa sổ (20/8), số mã (299), giai đoạn (6/2009–6/2025; 7/2025–12/2026; 1/2027–12/2028) hay định nghĩa biến nào bị đổi. Bốn câu hỏi con và năm sản phẩm của bài toán số 19 (ch04-1-lydo.tex:20) khớp nguyên văn QĐ 1193.
- **7 công thức** (4.1)–(4.7) khớp OMML của v14, kể cả Σ_k ở (6) và λW_it ở (7). Theo `main.aux`, số công thức (4.1)–(4.7) khớp với (1)–(7) của v14 đúng như Phụ lục A nói.
- **Tham chiếu chéo:** mọi `\ref`/`\eqref` đều có nhãn, `main.log` không báo tham chiếu treo; 4.3.1–4.3.10, "mục 7.3" (sec:nckh = 7.3) và "mục 9" (chương 9) trỏ đúng.
- **Danh mục tài liệu:** đúng 80 mục (16 tiếng Việt + 64 tiếng Anh). So tự động sau khi bỏ markup: 0 khác biệt so với v14. APA: không có "\&" ngoài ngoặc (chỉ có tên nhà xuất bản "Taylor \& Francis") và không có "và" giữa hai tác giả trong ngoặc trích dẫn.
- **Ký hiệu:** không có chỉ số dưới dùng dấu phẩy, không có `\cdot`/`\times`. MQI, Post, SMD, TK, HQ, MB viết đứng qua `\vn{}`; tham số là chữ Hy Lạp.
- **Ví dụ số, đã tính lại và đều đúng:**
  - Holm: 0,004 < 0,0167; 0,020 < 0,025; 0,030 < 0,05. Ở biến thể có p = 0,028 thì thủ tục dừng ở bước 2.
  - Bước giá: 1,25%; 0,125%; 0,33%; 0,17%; 0,17%.
  - Giá trần: 1.140 → 1.210 (+6,14%); 10.020 → 10.700 (+6,79%); 50.000 → 53.500 (+7,00%).
  - MQI: −0,2 và 0,3.
  - U và G: U_1(H) = 2,0%; U_1(CS) = −3,4%; G_1 = 5,4; Ḡ = 32,6/7 = 4,66; mức thu hẹp ≈ 2,2.
  - Sharpe: −0,5 và −0,2; tỷ lệ độ lệch chuẩn 2,5 lần.
  - Khác biệt kép: −0,25; e^−0,25 − 1 = −22,1%; e^−0,40 − 1 = −33,0%.
  - Bootstrap: p = 120/9.999 ≈ 0,012 (có hiệu chỉnh +1 thì 0,0121).
  - Hệ số tương tác: −0,28 và −0,12. Hai hướng lan tỏa: −0,25 và −0,15.
  - MDE, tính lại bằng ma trận hiệp phương sai AR(1) với 193 + 18 + 24 tháng và z(1 − 0,05/3) + z(0,8) = 2,970: 0,643σ / 1,239σ / 1,760σ. Tỷ số khi cửa sổ trước còn 24 tháng là 1,33 / 1,33 / 1,32 (v14 viết "khoảng 1,3").
  - 1 − e^−x: 12,0% / 22,0% / 29,7%.
- **Giải thích phương pháp đúng:**
  - Amihud nhân với tỷ số MC_t/MC_6/2025 đúng hướng.
  - Winsorize theo mẫu gộp; tỷ số phương sai (>1 là phản ứng chậm, <1 là đảo chiều); độ trễ giá Hou–Moskowitz.
  - Bootstrap khối dừng; lấy mẫu đồng thời hai rổ (bỏ hiệp phương sai dương thì khoảng tin cậy rộng ra).
  - Hồi quy về trung bình khi ghép theo Amihud kéo δ về phía 0; giải thích Callaway–Sant'Anna; e^δ − 1.
  - Hiệu ứng cố định theo trung tâm làm mất biến thiên của SMD.

---

## 1. Phát hiện

### MAJOR

**MAJOR-1. Câu hỏi 1 bị diễn đạt sai thành "sàn giao dịch".** Ở v14, câu hỏi 1 và \HH{1} nói về *mức phát triển thị trường cổ phiếu* cấp quốc gia (SMD = vòng quay, vốn hóa/GDP), kết luận chỉ là liên hệ có điều kiện. Bản dài viết thành "sàn giao dịch liên hệ/quan trọng với vị thế trung tâm", tức đổi đối tượng của câu hỏi nghiên cứu.

- `chapters/ch04-1-lydo.tex:13`
  - CŨ: `Đề tài đo ba thứ: sàn giao dịch liên hệ thế nào với vị thế trung tâm tài chính (câu hỏi~1)`
  - MỚI: `Đề tài đo ba thứ: mức phát triển thị trường cổ phiếu liên hệ thế nào với điểm GFCI của trung tâm tài chính (câu hỏi~1)`
- `frontmatter/huongdandoc.tex:19`
  - CŨ: `\item Câu hỏi đầu tiên là sàn giao dịch có quan trọng với vị thế của một trung tâm tài chính hay không; đề tài trả lời bằng dữ liệu GFCI của các trung tâm trên thế giới (\HH{1}).`
  - MỚI: `\item Câu hỏi đầu tiên là trung tâm tài chính ở quốc gia có thị trường cổ phiếu phát triển hơn có điểm GFCI cao hơn hay không, sau khi kiểm soát thể chế và thu nhập; đề tài trả lời bằng dữ liệu bảng GFCI của các trung tâm trên thế giới (\HH{1}), và kết quả chỉ là liên hệ có điều kiện.`

**MAJOR-2. Hộp tóm tắt 4.3.1 nói "kiểm định hai mắt xích đầu", mâu thuẫn với v14.** \HH{4} (mắt xích chất lượng thị trường → khả năng đầu tư) là "ước lượng, không kiểm định xác nhận". Còn mắt xích đầu chỉ được kiểm định dưới dạng tác động gộp của việc đổi sàn lên Amihud (\HH{3}).

- `chapters/ch04-3a-khung.tex:13`
  - CŨ: `Đề tài kiểm định hai mắt xích đầu; mắt xích cuối chỉ được tổng hợp định tính.`
  - MỚI: `Đề tài kiểm định mắt xích đầu qua \HH{3} (tác động gộp của việc đổi sàn lên thanh khoản), chỉ ước lượng mắt xích thứ hai qua \HH{4} (không kiểm định xác nhận), và không kiểm định quan hệ nhân quả ở mắt xích cuối; mắt xích này chỉ được tổng hợp định tính.`

**MAJOR-3. Lập luận "so sánh giữa các mô hình cho biết kênh nào đang hoạt động" là khẳng định phương pháp mới, không có trong v14, và sai về kinh tế.**

- Chi phí giao dịch giảm thì mô hình có vòng quay cao (M3) được lợi nhiều hơn M1. Vì vậy câu "mọi mô hình được lợi gần như nhau" là sai.
- Bản dài tự nói (ch04-3b:175) rằng cửa sổ ước lượng sau sự kiện phần lớn nằm trước 28/12/2026, nên kênh "dữ liệu sạch hơn" khó hiện trong 8 cửa sổ sau.
- Phụ lục D nhắc lại khẳng định này.

- `chapters/ch04-3b-chiso.tex:81`
  - CŨ: `Ý nghĩa của thứ tự này với đề tài: nếu chuyển sàn làm dữ liệu giá sạch hơn, thì các mô hình phải ước lượng nhiều (\MM{3}, \MM{4}, \MM{5}) sẽ được lợi nhiều hơn \MM{1}. Ngược lại, nếu chỉ chi phí giao dịch giảm, thì mọi mô hình được lợi gần như nhau. So sánh khoảng cách giữa các mô hình vì vậy cho biết kênh nào đang hoạt động.`
  - MỚI: `Thứ tự này giúp đọc độ phân tán của $G_m$ giữa các mô hình, nhưng không đủ để tách kênh tác động. Khi chi phí giao dịch giảm, mô hình có vòng quay danh mục cao (thường là \MM{3}) được lợi nhiều hơn \MM{1}, nên chênh lệch giữa các mô hình không chỉ phản ánh kênh ước lượng. Ngoài ra, cửa sổ ước lượng của các cửa sổ đánh giá sau sự kiện phần lớn còn nằm trước ngày chuyển sàn. Vì vậy đề tài chỉ báo cáo độ phân tán của $G_m$ và số mô hình có cùng dấu, cùng khoảng cách riêng của \MM{1}, không dùng so sánh giữa các mô hình để kết luận về kênh tác động.`
- `backmatter/phuluc.tex:185`
  - CŨ: `, và so sánh mô hình ước lượng nhiều với \MM{1} cho biết kênh ước lượng hay kênh chi phí đang hoạt động (mục~\ref{sec:mohinh}).`
  - MỚI: `; khoảng cách của \MM{1}, mô hình không cần ước lượng tham số, được báo cáo riêng như phép so sánh sạch nhất (mục~\ref{sec:mohinh}, \ref{sec:khanangdautu}).`

**MAJOR-4. Mô tả bootstrap tự hồi quy sai thủ tục.**

- (a) Bước 3 mô tả việc "mỗi tháng cộng thêm một phần dư", tức một bước ngẫu nhiên (random walk), không phải chuỗi tự hồi quy. Phân phối dưới giả thuyết gốc sinh ra như vậy sẽ sai.
- (b) Bước 2 ước lượng trên "cửa sổ trước", trong khi v14 ghi "mô hình tự hồi quy ước lượng trên giai đoạn tham chiếu".
- (c) Chưa nói rằng chuỗi giả phải trải qua cả 18 tháng chuyển tiếp để giữ đúng cấu trúc tự tương quan giữa cửa sổ trước và cửa sổ sau.

- `chapters/ch04-3c-kiemdinh.tex:70`
  - CŨ: `\item Trên cửa sổ trước, ước lượng $d_t = c + \phi d_{t-1} + u_t$; giả sử được $\phi = 0{,}6$ sau khi hiệu chỉnh độ chệch, và giữ lại các phần dư $u_t$.`
  - MỚI: `\item Trên giai đoạn tham chiếu, ước lượng mô hình tự hồi quy, ở đây minh họa bằng bậc một: $d_t = c + \phi d_{t-1} + u_t$; giả sử được $\phi = 0{,}6$ sau khi hiệu chỉnh độ chệch, và giữ lại các phần dư $u_t$ đã trừ trung bình.`
- `chapters/ch04-3c-kiemdinh.tex:71`
  - CŨ: `\item Tạo một chuỗi giả dài bằng chuỗi thật bằng cách bắt đầu từ một giá trị ban đầu và mỗi tháng cộng thêm một phần dư rút ngẫu nhiên có hoàn lại; chuỗi giả này \enquote{không có sự kiện}.`
  - MỚI: `\item Tạo một chuỗi giả theo đúng mô hình đã ước lượng, $d^*_t = c + \phi d^*_{t-1} + u^*_t$, với $u^*_t$ rút ngẫu nhiên có hoàn lại từ các phần dư, bắt đầu từ một giá trị ban đầu và bỏ một đoạn khởi động. Chuỗi giả trải liên tục qua cửa sổ trước, 18 tháng chuyển tiếp và cửa sổ sau; các tháng chuyển tiếp không vào thống kê nhưng được giữ để tự tương quan giữa hai cửa sổ được tính đúng. Chuỗi giả này \enquote{không có sự kiện}.`

**MAJOR-5. Giải thích sai nguồn nhiễu của chuỗi d_t và lý do không phân cụm theo cổ phiếu.** d_t là chênh lệch giữa nhóm chuyển sàn và nhóm đối chứng, nên cú sốc chung tác động như nhau lên mọi mã bị triệt tiêu khi lấy chênh lệch (và bị τ_t hấp thụ trong phương trình (4.5)). Nguồn nhiễu không giảm khi thêm cổ phiếu là các cú sốc theo tháng tác động *khác nhau* lên hai nhóm. v14 (đoạn [182]) cũng diễn đạt theo hướng này.

- `chapters/ch04-3d-tincay.tex:14`
  - CŨ: `Thêm cổ phiếu làm mỗi điểm của chuỗi bớt nhiễu riêng lẻ, nhưng không làm giảm các cú sốc chung của tháng, vốn chiếm phần lớn biến động của chuỗi.`
  - MỚI: `Thêm cổ phiếu làm mỗi điểm của chuỗi bớt nhiễu riêng lẻ của từng mã, nhưng không làm giảm các cú sốc theo tháng tác động khác nhau lên nhóm chuyển sàn và nhóm đối chứng; cú sốc tác động như nhau lên mọi mã thì đã triệt tiêu khi lấy chênh lệch. Nếu loại cú sốc thứ nhất chiếm phần lớn phương sai của chuỗi, thêm cổ phiếu gần như không làm giảm hiệu ứng nhỏ nhất phát hiện được.`
- `chapters/ch04-3c-kiemdinh.tex:62`
  - CŨ: `Nhưng ở đây, mọi cổ phiếu chuyển sàn cùng chịu một sự kiện vào cùng một ngày, và mọi cú sốc của tháng (một đợt bán tháo, một tin chính sách) tác động lên tất cả cùng lúc.`
  - MỚI: `Nhưng ở đây, mọi cổ phiếu chuyển sàn cùng chịu một sự kiện vào cùng một ngày. Cú sốc tác động như nhau lên mọi cổ phiếu đã được hiệu ứng cố định theo tháng $\tau_t$ hấp thụ; vấn đề là những cú sốc theo tháng tác động lên cả nhóm chuyển sàn khác với nhóm đối chứng (một tin chỉ liên quan đến các mã HNX, một đợt bán tháo dồn vào mã nhỏ), làm sai số của các mã chuyển sàn tương quan với nhau trong cùng tháng.`

**MAJOR-6. Hàm ý chính sách từ phân tích theo trụ sở vượt quá v14.** Câu trong bản dài coi "không được lợi ít hơn" (không bác bỏ) là bằng chứng "vị trí sàn không còn quan trọng" và "mất sàn không phải mất mát lớn". Điều này trái với v14 ở hai chỗ: chênh lệch theo trụ sở "không đo lượng thanh khoản mà thị trường vốn Hà Nội mất", và chỉ "khoảng tin cậy hẹp quanh 0" mới "không ủng hộ vai trò của vị trí sàn".

- `chapters/ch04-3c-kiemdinh.tex:135`
  - CŨ: `Nếu doanh nghiệp Hà Nội không được lợi ít hơn, thì vị trí địa lý của sàn cổ phiếu không còn quan trọng với thanh khoản, và việc Hà Nội mất sàn cổ phiếu niêm yết không phải là mất mát lớn về mặt này.`
  - MỚI: `Nếu khoảng tin cậy của chênh lệch theo trụ sở hẹp quanh 0, kết quả không ủng hộ vai trò của vị trí sàn đối với thanh khoản của các mã chuyển sàn; nếu khoảng tin cậy rộng, kết quả chưa đủ cơ sở kết luận. Trong cả hai trường hợp, chênh lệch này không đo lượng thanh khoản mà thị trường vốn Hà Nội mất.`

**MAJOR-7. "Bốn tình huống" có hai suy luận sai.**

- (a) Coi kết quả "chưa đủ cơ sở kết luận" là bằng chứng rằng khác biệt do doanh nghiệp. Điều này trái với nguyên tắc v14 [210]: chưa đủ cơ sở kết luận "không phải bằng chứng về việc không có tác động".
- (b) SMD đo ở cấp quốc gia, giống nhau cho Hà Nội và Thành phố Hồ Chí Minh, nên \HH{1} không thể cho biết việc cổ phiếu tập trung ở Thành phố Hồ Chí Minh là "bất lợi" của Hà Nội.
- (c) δ chỉ là tác động lên các mã chuyển sàn, nên không nói được "hợp nhất có lợi cho nhà đầu tư" nói chung.

- `chapters/ch04-3c-kiemdinh.tex:207`
  - CŨ: `thì hợp nhất có lợi cho nhà đầu tư, và thế mạnh`
  - MỚI: `thì việc chuyển sàn có lợi cho nhà đầu tư vào các mã chuyển sàn, và thế mạnh`
  - CŨ: `Nếu tác động nhỏ hoặc chưa đủ cơ sở kết luận, thì khác biệt giữa hai sàn chủ yếu do doanh nghiệp chứ không do sàn, và câu hỏi chuyên môn hóa ít phụ thuộc vào việc mất sàn cổ phiếu.`
  - MỚI: `Nếu khoảng tin cậy hẹp quanh 0, khác biệt giữa hai sàn ở \HH{2} nhiều khả năng đến từ đặc điểm doanh nghiệp hơn là từ sàn; nếu kết quả chưa đủ cơ sở kết luận, đề tài không rút ra hàm ý nào về vai trò của sàn.`
  - CŨ: `Nếu \HH{1} được ủng hộ, thì vị thế trung tâm tài chính đi cùng thị trường cổ phiếu phát triển, và việc thị trường cổ phiếu tập trung ở Thành phố Hồ Chí Minh là một bất lợi cần được bù bằng chuyên môn hóa ở mảng khác.`
  - MỚI: `Nếu \HH{1} được ủng hộ, thì ở cấp quốc gia, điểm GFCI đi cùng mức phát triển thị trường cổ phiếu (liên hệ có điều kiện). Vì $\SMD$ đo ở cấp quốc gia và như nhau với mọi thành phố của Việt Nam, kết quả này không cho biết việc giao dịch cổ phiếu tập trung ở Thành phố Hồ Chí Minh có bất lợi cho Hà Nội hay không; nó chỉ là bối cảnh cho phần so sánh định tính.`

**MAJOR-8. Khẳng định sai về điểm z GFCI.** Điểm z theo từng kỳ *vẫn* phụ thuộc vào thành phần của bảng: khi trung tâm vào hoặc ra, trung bình và độ lệch chuẩn của kỳ thay đổi. Vì vậy câu "không bị ảnh hưởng bởi số trung tâm trong bảng" là sai. v14 có sẵn phép kiểm tra độ vững trên mẫu cân bằng cho đúng vấn đề này.

- `chapters/ch04-3c-kiemdinh.tex:154`
  - CŨ: `Điểm z theo từng kỳ giữ được khoảng cách và không bị ảnh hưởng bởi số trung tâm trong bảng.`
  - MỚI: `Điểm z theo từng kỳ giữ được khoảng cách và đưa các kỳ về cùng thang đo, nhưng vẫn phụ thuộc vào thành phần của bảng: khi có trung tâm vào hoặc ra, trung bình và độ lệch chuẩn của kỳ thay đổi theo. Vì vậy đề tài kiểm tra độ vững trên mẫu các trung tâm có ít nhất năm kỳ và trên mẫu cân bằng (mục~\ref{sec:tincay}).`

### MINOR

**MINOR-1. Giá tham chiếu 10.020 đồng không nằm trên lưới giá.** Với giá từ 10.000 đồng trở lên, giá ở HOSE là bội số của 50 (và ở HNX là bội số của 100), nên ví dụ dùng một giá không có thật. Đổi sang 10.050: 10.050 × 1,07 = 10.753,5 → 10.750; 700/10.050 = 6,97%.

- `chapters/ch04-3a-khung.tex:112`
  - CŨ: `\item giá 10.020 đồng: 10.020 nhân 1,07 bằng 10.721,4; làm tròn xuống theo bước 50 đồng được 10.700 đồng; mức tăng tối đa là 6,79\%;`
  - MỚI: `\item giá 10.050 đồng: 10.050 nhân 1,07 bằng 10.753,5; làm tròn xuống theo bước 50 đồng được 10.750 đồng; mức tăng tối đa là 6,97\%;`

**MINOR-2. Diễn giải sai đơn vị của MQI.** MQI là trung bình của các trung bình điểm z, nên không có độ lệch chuẩn bằng 1. Mốc 0 cũng là bình quân của *mẫu gộp các sàn*, không phải bình quân của giai đoạn tham chiếu nói chung.

- `chapters/ch04-3b-chiso.tex:34`
  - CŨ: `Chênh lệch giữa HOSE và HNX trong tháng này là $0{,}5$ độ lệch chuẩn.`
  - MỚI: `Chênh lệch giữa HOSE và HNX trong tháng này là $0{,}5$ đơn vị điểm z (trung bình của các điểm z, không đúng bằng một độ lệch chuẩn của chỉ số).`
- `chapters/ch04-3b-chiso.tex:26`
  - CŨ: `Chỉ số bằng 0 nghĩa là sàn ở đúng mức bình quân của giai đoạn tham chiếu;`
  - MỚI: `Chỉ số bằng 0 nghĩa là sàn ở mức bình quân của mẫu gộp các sàn trong giai đoạn tham chiếu;`

**MINOR-3. Mô tả sai tần suất ước lượng lại.** Theo v14 (ghi chú Bảng 3), trọng số được ước lượng lại *hằng tháng* trên cửa sổ trượt 104 tuần, không phải trượt ba tháng mỗi lần.

- `chapters/ch04-3b-chiso.tex:172`
  - CŨ: `Hình~\ref{fig:cuaso} cho thấy cửa sổ ước lượng trượt về phía trước ba tháng mỗi lần, và các cửa sổ đánh giá nối tiếp nhau không chồng lên nhau.`
  - MỚI: `Hình~\ref{fig:cuaso} vẽ giản lược mỗi cửa sổ đánh giá với một cửa sổ ước lượng; trên thực tế, trong mỗi cửa sổ đánh giá, trọng số vẫn được ước lượng lại hằng tháng trên cửa sổ trượt 104 tuần (Bảng~\ref{tab:baymohinh}). Các cửa sổ đánh giá nối tiếp nhau không chồng lên nhau.`

**MINOR-4. Diễn giải β trong ví dụ (4.7) bỏ qua hiệu ứng cố định theo trung tâm.** Khi có α_i, β là liên hệ *trong cùng trung tâm theo thời gian*, không phải so sánh với "các trung tâm cùng kỳ".

- `chapters/ch04-3c-kiemdinh.tex:158`
  - CŨ: `Khi đó, một trung tâm ở quốc gia có mức phát triển thị trường cổ phiếu tăng thêm một độ lệch chuẩn có điểm GFCI cao hơn trung bình 0,3 độ lệch chuẩn so với các trung tâm cùng kỳ, khi thu nhập và thể chế không đổi.`
  - MỚI: `Khi đó, ở đặc tả có hiệu ứng cố định theo trung tâm, khi $\SMD$ của quốc gia chứa một trung tâm cao hơn mức thường lệ của chính quốc gia ấy một độ lệch chuẩn, điểm z GFCI của trung tâm ấy cao hơn mức thường lệ của nó khoảng 0,3, khi thu nhập và thể chế không đổi; chỉ ở đặc tả không có hiệu ứng cố định theo trung tâm, hệ số mới được đọc như so sánh giữa các trung tâm cùng kỳ.`

**MINOR-5. Nói quá về thiết kế "gần thí nghiệm" và thêm khái quát không có nguồn.** Nhóm chuyển sàn là các doanh nghiệp đã tự chọn niêm yết ở HNX, và sự kiện trùng với nhiều cú sốc khác (mục 4.3.8).

- `chapters/ch04-1-lydo.tex:60`
  - CŨ: `Doanh nghiệp chuyển sang sàn lớn thường là doanh nghiệp đang tăng trưởng, nên`
  - MỚI: `Doanh nghiệp tự chuyển sang sàn lớn có thể là doanh nghiệp đang tăng trưởng, nên`
  - CŨ: `Đây là điều kiện gần với thí nghiệm nhất mà nghiên cứu về sàn giao dịch có thể có.`
  - MỚI: `Thời điểm chuyển sàn vì vậy không do từng doanh nghiệp chọn. Tuy nhiên, nhóm chuyển sàn vẫn là các doanh nghiệp đã chọn niêm yết ở HNX từ trước, và việc chuyển sàn trùng với nhiều thay đổi khác, nên đề tài vẫn cần nhóm đối chứng và các kiểm tra ở mục~\ref{sec:did}.`

**MINOR-6. Khẳng định "chưa ai…" thiếu phạm vi tìm kiếm** (trái với chính hộp "Chỗ dễ hiểu nhầm" ở ch04-2:85).

- `chapters/ch04-1-lydo.tex:13`
  - CŨ: `Lúc này chưa ai đo được Hà Nội mất hay được gì từ việc đó.`
  - MỚI: `Trong phạm vi tìm kiếm của thí sinh đến ngày 30/9/2026, chưa có nghiên cứu nào đo Hà Nội mất hay được gì từ việc đó.`
- `chapters/ch04-2-tongquan.tex:7`
  - CŨ: `và cả bốn cùng chỉ về một chỗ: chưa ai đo vai trò của sàn đối với chất lượng thị trường và khả năng đầu tư ở Việt Nam.`
  - MỚI: `và cả bốn cùng chỉ về một chỗ: trong phạm vi tìm kiếm đến ngày 30/9/2026, vai trò của sàn đối với chất lượng thị trường và khả năng đầu tư chưa được đo cho Việt Nam.`

**MINOR-7. Ba khẳng định thực tế mới, không có trong v14 hay ho-so.**

- `chapters/ch04-1-lydo.tex:54`: v14 chỉ nói Bắc Kinh là trung tâm chính trị và quản lý (Lai, 2012); "trụ sở ngân hàng" là thông tin mới.
  - CŨ: `nhờ cơ quan quản lý, trụ sở ngân hàng và thông tin chính sách.`
  - MỚI: `nhờ vai trò trung tâm chính trị và quản lý (Lai, 2012) và lợi thế thông tin (Wang và cộng sự, 2007).`
- `chapters/ch04-2-tongquan.tex:38`: v14 nói lợi ích dồn vào doanh nghiệp lớn và doanh nghiệp có doanh thu nước ngoài, không nói "được biết đến rộng rãi".
  - CŨ: `lợi ích dồn vào doanh nghiệp vốn đã được nhà đầu tư rộng rãi biết đến.`
  - MỚI: `lợi ích dồn vào doanh nghiệp lớn và doanh nghiệp có doanh thu nước ngoài.`
- `chapters/ch04-2-tongquan.tex:26`: khẳng định về độ đầy đủ của dữ liệu trong ngày giai đoạn đầu không có nguồn.
  - CŨ: `kể cả khi dữ liệu trong ngày cho giai đoạn đầu không đầy đủ.`
  - MỚI: `mà không cần dữ liệu trong ngày.`

**MINOR-8. "Tác động 10% rất có thể không được phát hiện" chưa nêu giả định.** Tính lại với σ = 0,2: lực kiểm định để phát hiện mức giảm 10% (log 0,105) là 62% khi φ = 0, 19% khi φ = 0,6 và 11% khi φ = 0,8. Khi φ = 0 thì câu "rất có thể không" không còn đúng.

- `chapters/ch04-3d-tincay.tex:37`
  - CŨ: `Với lực kiểm định như trên, một tác động thật bằng 10\% rất có thể không được phát hiện.`
  - MỚI: `Với giả định minh họa $\sigma = 0{,}2$ và $\phi = 0{,}6$, một tác động thật làm độ phi thanh khoản giảm 10\% chỉ được phát hiện với xác suất khoảng một phần năm.`

**MINOR-9. Nói quá về nhóm đối chứng tổng hợp.** Khớp tốt ở giai đoạn trước không bảo đảm có xu hướng song song ở giai đoạn sau, và phương pháp không phải lúc nào cũng tạo được tổ hợp khớp tốt. Thêm nữa, v14 chỉ ghi "nhóm đối chứng tổng hợp từ các mã HOSE … và mã UPCoM". Việc bản dài hiểu cụm này là synthetic control có trọng số tối ưu là một bổ sung phương pháp, cần ghi đúng như vậy trong tệp đăng ký.

- `chapters/ch04-3d-tincay.tex:60`
  - CŨ: `Nếu không có nhóm có sẵn nào đi song song, phương pháp này tạo ra một nhóm như vậy từ dữ liệu.`
  - MỚI: `Phương pháp này chỉ dùng được khi tổ hợp bám sát nhóm chuyển sàn trong giai đoạn trước; bám sát ở giai đoạn trước không bảo đảm xu hướng song song ở giai đoạn sau, nên độ khớp trước sự kiện được báo cáo kèm, và cách lập nhóm cụ thể được ghi trong tệp đăng ký.`

**MINOR-10. "30 mã thanh khoản nhất" lệch v14.** v14 ghi "tối đa 30", tiêu chí là giá trị giao dịch, và có phương án dự phòng 20 mã.

- `chapters/ch04-4-5-phamvi.tex:20`
  - CŨ: `\HH{4} chỉ đo trên 30 mã thanh khoản nhất,`
  - MỚI: `\HH{4} chỉ đo trên rổ CS (tối đa 30 mã, hoặc 20 mã theo phương án dự phòng, có giá trị giao dịch bình quân lớn nhất),`

**MINOR-11. Bảng cú sốc trùng thời gian và Phụ lục C lệch v14.** v14 chỉ *báo cáo thêm* ước lượng với cửa sổ sau cắt tại ngày áp dụng, chứ không cắt cửa sổ của ước lượng chính. Kênh chỉ số trong v14 là "vốn hóa lớn *so với giá trị giao dịch*".

- `chapters/ch04-3c-kiemdinh.tex:190`
  - CŨ: `Ghi ngày áp dụng, cắt cửa sổ sau tại ngày đó\\`
  - MỚI: `Ghi ngày áp dụng; báo cáo thêm ước lượng với cửa sổ sau cắt tại ngày đó\\`
- `chapters/ch04-3c-kiemdinh.tex:189`
  - CŨ: `Áp lực cầu lên mã chuyển sàn, nhất là mã vốn hóa lớn &`
  - MỚI: `Áp lực cầu lên mã chuyển sàn, nhất là mã có vốn hóa lớn so với giá trị giao dịch &`
- `backmatter/phuluc.tex:155`
  - CŨ: `Cắt cửa sổ sau tại ngày áp dụng & \ref{sec:did}`
  - MỚI: `Báo cáo thêm ước lượng với cửa sổ sau cắt tại ngày áp dụng & \ref{sec:did}`

**MINOR-12. Phụ lục B, dòng 30/9/2026.** Ngày 30/9/2026 là ngày công bố, không phải "ngày sự kiện" (ngày sự kiện là 28/12/2026). Con số 299 mã lấy từ Tuổi Trẻ Online (2026b), không phải từ thông báo của VNX.

- `backmatter/phuluc.tex:112`
  - CŨ: `30/9/2026 & Thông báo của VNX về lịch chuyển sàn; 299 mã niêm yết tại HNX & Ngày sự kiện\\`
  - MỚI: `30/9/2026 & Thông báo của VNX về lịch chuyển sàn; phiên 30/9/2026 có 299 mã niêm yết tại HNX (Tuổi Trẻ Online, 2026b) & Ngày công bố lịch chuyển sàn\\`

**MINOR-13. Phụ lục A (bảng ký hiệu) chưa khớp hẳn văn bản.**

- φ xuất hiện lần đầu ở ví dụ bootstrap (mục 4.3.7), không phải 4.3.10.
- Định nghĩa A_it thiếu điều kiện "không liền sau…".
- λW_it là tích của hai véc-tơ; theo lối cổ điển cần nói rõ đó là tích vô hướng. Công thức của v14 được giữ nguyên, chỉ thêm chú giải.

- `backmatter/phuluc.tex:55`
  - CŨ: `$\phi$ & Hệ số tự hồi quy bậc một của chuỗi $d_t$ & mục~\ref{sec:tincay}\\`
  - MỚI: `$\phi$ & Hệ số tự hồi quy bậc một của chuỗi $d_t$ (giả định minh họa) & mục~\ref{sec:kiemdinh}, \ref{sec:tincay}\\`
- `backmatter/phuluc.tex:44`
  - CŨ: `$A_{it}$ & Logarit độ phi thanh khoản Amihud, tính trên ngày dưới ngưỡng chung & \eqref{eq:did}\\`
  - MỚI: `$A_{it}$ & Logarit độ phi thanh khoản Amihud, tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày có lợi suất tuyệt đối từ ngưỡng trở lên & \eqref{eq:did}\\`
- `backmatter/phuluc.tex:63`
  - CŨ: `$\lambda$ & Véc-tơ hệ số của $W_{it}$ & \eqref{eq:gfci}\\`
  - MỚI: `$\lambda$ & Véc-tơ hệ số của $W_{it}$; $\lambda W_{it}$ hiểu là tích vô hướng của hai véc-tơ & \eqref{eq:gfci}\\`

**MINOR-14. Phụ lục D gán sai nguồn.** Nghị quyết 222 không nói gì về GFCI 40 hay việc mất sàn.

- `backmatter/phuluc.tex:173`
  - CŨ: `Theo Nghị quyết số 222/2025/QH15, Hà Nội không có trung tâm tài chính quốc tế, không có trong GFCI 40 và sắp không còn sàn cổ phiếu niêm yết.`
  - MỚI: `Theo Nghị quyết số 222/2025/QH15, trung tâm tài chính quốc tế đặt tại Thành phố Hồ Chí Minh và Đà Nẵng; Hà Nội không có trong GFCI 40 (Wardle \& Mainelli, 2026) và sắp không còn sàn cổ phiếu niêm yết.`

**MINOR-15. "Đảm bảo" quá mức.** Ngày điểm gãy Bai–Perron là một ước lượng, có sai số.

- `chapters/ch04-3c-kiemdinh.tex:45`
  - CŨ: `Bắt đầu từ sau điểm gãy cuối cùng đảm bảo cửa sổ trước chỉ gồm giai đoạn có cùng chế độ với thời điểm ngay trước sự kiện.`
  - MỚI: `Bắt đầu từ sau điểm gãy cuối cùng giúp cửa sổ trước chủ yếu gồm giai đoạn có cùng chế độ với thời điểm ngay trước sự kiện; vì ngày gãy được ước lượng có sai số, ước lượng với cửa sổ trước 24 tháng được báo cáo kèm.`

**MINOR-16. Dấu nháy mở sai trong mục Michaud.** Trong LaTeX, `'` in ra dấu ’, nên nháy mở bị in thành ’optimized’.

- `chapters/ch11-tailieu.tex:71`
  - CŨ: `Is 'optimized' optimal?`
  - MỚI: ``Is `optimized' optimal?``

---

## 2. Bảng tổng hợp

| Mức | Số lượng | Mã |
|---|---|---|
| CRITICAL | 0 | — |
| MAJOR | 8 | MAJOR-1 đến MAJOR-8 |
| MINOR | 16 | MINOR-1 đến MINOR-16 |
| **Tổng** | **24** | |

Ghi chú: không có số liệu, ngày tháng, trích dẫn hay công thức nào của v14 bị sửa sai. Các lỗi tập trung ở phần giải thích mới thêm: diễn đạt lại câu hỏi 1, mô tả thủ tục bootstrap, nguồn nhiễu của d_t, và các suy luận chính sách vượt quá thiết kế.
