# Rà soát hình thức slide, vòng 1, người rà soát A

Đối tượng: `latex/slides/slides.tex` (md5 `77a85cc5…`) và `latex/slides/presentation.sty` (md5 `89ee2119…`). Đây là bản đang có trong cây làm việc lúc 03:24 UTC ngày 18/10/2026: main đã chuyển sang Source Sans Pro (`fonts/`) và đã viết hoa tiêu đề bằng `\capsfont\MakeUppercase`. Báo cáo không đề xuất lại hai thay đổi này.

Skill đã nạp: `beamer` (gồm audit, tikz, validate, rubric 100, Hard Rules), `beamer-check` (chỉ dùng phần phân tích log, vì script gọi pdflatex), `slide-design-principles` (đọc cả hai tệp trong references/), `latex-econ-model`.

Cách làm, theo quy tắc không render ảnh:
- Biên dịch bản sao `/tmp/sA` bằng `xelatex` hai lần.
- Đọc log bằng các regex của `beamer_check.py`.
- Đo tọa độ chữ bằng `pdftotext -bbox` (trang 453,54 × 255,12 pt; lề chữ 14,17–439,37 pt; `\textheight` = 252,07 pt). Từ đó tính số dòng tiêu đề, mép dưới của nội dung, chữ vượt lề phải và chữ chồng nhau.
- Đọc chữ bằng `pdftotext -layout`.
- Đối chiếu với bản gốc của template: `presentation.tex`, `wide.tex`, `presentation.sty`, `README.md`. Hai tệp `presentation.pdf` và `figures.pdf` chỉ đọc được phần chữ vì không được render ảnh.

**Đã kiểm chứng các cặp sửa.** Tôi áp toàn bộ cặp CŨ/MỚI trong báo cáo (trừ S3, vì S3 và S7 là hai cách sửa cùng một dòng) vào bản sao `/tmp/sF`, rồi biên dịch XeLaTeX hai lần:
- Mã thoát 0; không có Overfull, Underfull hay lỗi nào.
- Mọi tiêu đề nằm trên 1 dòng và không vượt x = 432 pt.
- Mép dưới cao nhất là 240,2 pt (slide tài liệu); trang tiêu đề còn 231,9 pt.
- Trục thời gian ở slide 2 hiện đủ "30/9/2026", "VNX công bố lịch" và "TT 139: lùi đến 31/12/2026".
- Mỗi chuỗi CŨ đều xuất hiện đúng 1 lần trong tệp gốc (đã đếm bằng script), nên các cặp áp được theo thứ tự bất kỳ.

## Validate (skill beamer, mục 2.10)

| Kiểm tra | Kết quả | Trạng thái |
|---|---|---|
| Số trang | 32 trang. Phần chính có 25 trang (gồm 19 slide nội dung, 4 slide mục, trang tiêu đề, slide cảm ơn), thêm `\lastslide` và 6 trang phụ lục. Với 30 phút là khoảng 1,6 phút một slide nội dung, khớp mức 1,5–2 phút của skill (khoảng 17–22 slide nếu nội suy giữa mốc 20 và 45 phút) | OK |
| Tỷ lệ khung | 453,54 × 255,12 pt (16:9) | OK |
| Dung lượng tệp | 67,9 KB | OK |
| Overfull/Underfull hbox, vbox | 0 / 0 | OK |
| Lệnh chưa định nghĩa, trích dẫn chưa định nghĩa, nhãn trùng | 0 | OK |
| Cảnh báo khác | 1: hyperref "Token not allowed … `\translate`" ở dòng 491, sinh ra từ `\appendix`. Không ảnh hưởng hiển thị | OK |
| Lệnh overlay (`\pause`, `\only`, `\onslide`, `\uncover`) | 0 | OK |
| Slide có hơn 2 khung màu | 0 (deck chưa có khung nào) | OK |
| `\tiny` | 0 | OK |
| Slide tài liệu tham khảo | Có (slide 24, đứng ngay trước slide cảm ơn) | OK |
| Bảng tô nền xám | 0 | OK |
| Slide chỉ có chữ (không công thức, bảng hay hình) | 1/19 trong phần chính (slide 23, "Ba điều cần nhớ") | OK |
| Log sạch nhưng lỗi vẫn hiện trên slide | Có: trục thời gian slide 2 bị cắt nhãn (A1) | **FAIL** |

Kết luận validate: **FAIL**. Deck biên dịch sạch, nhưng có một lỗi hiển thị mà log không báo.

## Số đo bố cục (bản hiện tại)

- Tiêu đề xuống 2 dòng ở 6 slide: 4, 5, 6, 9, 18, 19. Ba slide 3, 15, 19 có tiêu đề kéo đến x ≥ 436 pt, sát lề phải 439,4 pt.
- Mép dưới của nội dung: slide 1 ở 246,1 pt, slide 24 ở 240,3, slide 9 ở 240,3, slide 4 ở 239,4. Không slide nào vượt `\textheight`. Không có chữ nào chồng nhau, kể cả nhãn TikZ ở slide 2, 6, 8 và 14.
- TikZ slide 6: nhãn "khác biệt kép" và "bối cảnh" nằm gọn trong khe giữa hai hộp, cách viền hộp 2–3 pt. Không chồng, nhưng sát.
- Cỡ chữ nhỏ nhất ngoài chỉ số dưới là \footnotesize (9 pt), dùng cho dòng nguồn ở slide 3, 5, 6, 14 và nhãn TikZ ở slide 2, 6, 8. Hard Rule 13 đặt mức tối thiểu cho chú thích là \small, nhưng template để caption ở footnotesize. Vì người dùng yêu cầu bám sát template, các phát hiện nhóm B chuyển những dòng này thành caption kiểu template (footnotesize, màu xám) thay vì tăng lên \small.

## 1. Lỗi hiển thị và tràn

### A1. [CRITICAL] Slide 2, dòng slides.tex 42

Nhãn trục thời gian bị cắt. `\foreach \x/\a/\b` tách theo dấu "/", nên mốc thứ tư hiện "30" ở trên và "9" ở dưới (mất "/9/2026" và "VNX công bố lịch"); nhãn TT 139 chỉ còn "TT 139: lùi đến 31" (mất "/12/2026"). Kiểm bằng `pdftotext -bbox`: tại x≈277–290 pt chỉ có từ "30", tại x≈280 pt chỉ có "9". Log biên dịch không báo gì. Sửa: bọc trường có "/" trong ngoặc nhọn.

```text
FILE: latex/slides/slides.tex
CŨ: \foreach \x/\a/\b in {0.4/2021/TT 57: hạn năm 2023, 3.2/2023/TT 69: lùi đến hết 2025, 6.0/2025/TT 139: lùi đến 31/12/2026, 8.8/30/9/2026/VNX công bố lịch}
MỚI: \foreach \x/\a/\b in {0.4/2021/{TT 57: hạn năm 2023}, 3.2/2023/{TT 69: lùi đến hết 2025}, 6.0/2025/{TT 139: lùi đến 31/12/2026}, 8.8/{30/9/2026}/{VNX công bố lịch}}
```

### A2. [MAJOR] Slide 1, dòng slides.tex 29

Trang tiêu đề kín từ trên xuống dưới: tên đề tài viết hoa ở \LARGE xuống 4 dòng, dòng 1 lẻ "TRƯỜNG:", dòng 4 lẻ "CHÍNH HÀ NỘI"; chữ bắt đầu ở y=12,7 pt, dòng ngày kết thúc ở y=246,1 pt (cách mép dưới 9 pt). Sửa: tự ngắt thành 4 dòng cân nhau (chữ giữ nguyên, chỉ thêm `\\`) và giảm cỡ tiêu đề (cặp S7 bên dưới). Có cả hai cặp thì trang chiếm y=16,4–231,9 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \title{Hợp nhất sàn chứng khoán và chất lượng thị trường:\\ Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội}
MỚI: \title{Hợp nhất sàn chứng khoán\\ và chất lượng thị trường:\\ Bằng chứng thực nghiệm từ HNX\\ và vị thế tài chính Hà Nội}
```

### S7. [MAJOR] Slide 1, dòng sty 52

Thay cho S3, đi cùng A2: bỏ semibold và giảm xuống \Large để trang tiêu đề có lề dưới khoảng 23 pt. Đây là lệch khỏi \huge của template, nhưng với tên đề tài viết hoa dài 4 dòng thì \huge (hoặc \LARGE) đẩy dòng ngày sát mép dưới.

```text
FILE: latex/slides/presentation.sty
CŨ: \setbeamerfont{title}{size=\LARGE, series=\sbseries}
MỚI: \setbeamerfont{title}{size=\Large}
```


## 2. Tiêu đề quá dài (xuống 2 dòng hoặc sát lề phải)

### A3. [MINOR] Slide 3, dòng slides.tex 58

Tiêu đề viết hoa dài đến x=436,1 pt, sát lề phải (439,4 pt). Bỏ "cần biết" thì vẫn giữ được kết luận.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Hà Nội cần biết mất gì, được gì khi không còn sàn cổ phiếu niêm yết}
MỚI: \frametitle{Hà Nội mất gì, được gì khi không còn sàn cổ phiếu niêm yết}
```

### A4. [MINOR] Slide 4, dòng slides.tex 85

Tiêu đề xuống 2 dòng nên bảng bị đẩy xuống, chân bảng tới y=239,4 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Ba câu hỏi, bốn giả thuyết; trọng tâm là tác động của việc chuyển sàn}
MỚI: \frametitle{Bốn giả thuyết; trọng tâm là tác động của việc chuyển sàn}
```

### A5. [MINOR] Slide 5, dòng slides.tex 104

Tiêu đề xuống 2 dòng (81 ký tự).

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Đóng góp: đo vai trò của sàn ở một thị trường mới nổi, bằng một sự kiện ngoại sinh}
MỚI: \frametitle{Đóng góp: đo vai trò của sàn ở thị trường mới nổi}
```

### A6. [MINOR] Slide 6, dòng slides.tex 121

Tiêu đề xuống 2 dòng, dòng 2 chỉ có "HÀ NỘI"; slide có hình TikZ nên càng chật.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Khung phân tích: từ chất lượng trước hợp nhất đến hàm ý cho Hà Nội}
MỚI: \frametitle{Khung phân tích: từ đo chất lượng đến hàm ý cho Hà Nội}
```

### A7. [MINOR] Slide 9, dòng slides.tex 164

Tiêu đề xuống 2 dòng; slide có công thức, bảng và 2 ý nên chân tới y=240,3 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Chỉ số chất lượng thị trường vốn: ba chiều, sáu chỉ báo, trọng số bằng nhau}
MỚI: \frametitle{Chỉ số chất lượng: ba chiều, sáu chỉ báo, trọng số bằng nhau}
```

### A8. [MINOR] Slide 15, dòng slides.tex 300

Tiêu đề dài đến x=438,8 pt, chỉ còn 0,6 pt là tới lề.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Lực kiểm định phụ thuộc vào số tháng, không phụ thuộc vào số mã}
MỚI: \frametitle{Lực kiểm định phụ thuộc số tháng, không phụ thuộc số mã}
```

### A9. [MINOR] Slide 18, dòng slides.tex 353

Tiêu đề xuống 2 dòng; slide đã có 3 công thức.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Khả năng đầu tư: nhà đầu tư thiệt bao nhiêu với rổ cổ phiếu chuyển sàn}
MỚI: \frametitle{Khả năng đầu tư: rổ chuyển sàn kém rổ HOSE bao nhiêu}
```

### A10. [MINOR] Slide 19, dòng slides.tex 374

Tiêu đề xuống 2 dòng (77 ký tự).

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Bằng chứng quốc tế: thị trường cổ phiếu và điểm GFCI là liên hệ có điều kiện}
MỚI: \frametitle{Thị trường cổ phiếu và điểm GFCI: liên hệ có điều kiện}
```


## 3. Mật độ, ký hiệu công thức, nhất quán nội dung–tiêu đề

### D1. [MAJOR] Slide 18, dòng slides.tex 357–362

Slide có 3 công thức trưng bày trong `align*`, vượt giới hạn ≤2 của skill. Ngoài ra $\bar G$ viết bằng phép cộng dàn trải `G_1+\dots+G_7` thay vì dùng tổng Σ như kinh tế lượng cổ điển. Cặp này chuyển $U$ vào dòng định nghĩa và viết $\bar G=\frac17\sum_m G_m$.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{align*}
U &= \mu - \frac{\rho}{2}\sigma^2\\
G_m &= U_m(\vn{H}) - U_m(\vn{CS})\\
\bar{G} &= \frac{G_1 + G_2 + \dots + G_7}{7}
\end{align*}
{\small $U$: lợi suất tương đương chắc chắn sau chi phí;
MỚI: \begin{align*}
G_m &= U_m(\vn{H}) - U_m(\vn{CS})\\
\bar{G} &= \frac{1}{7}\sum_{m=1}^{7} G_m
\end{align*}
{\small $U = \mu - \rho\sigma^2/2$: lợi suất tương đương chắc chắn sau chi phí;
```

### D2. [MAJOR] Slide 15, dòng slides.tex 305

Ký hiệu không nhất quán: σ ở slide 15 là độ lệch chuẩn của $d_t$, còn σ² ở slide 18 là phương sai lợi suất danh mục. Đổi σ ở slide 15 thành $\sigma_d$ (gồm các cặp D2, D3, D4). Đề cương v15 cũng dùng σ cho cả hai nghĩa, nên nếu muốn khớp đề cương thì có thể giữ nguyên, nhưng trên slide hai nghĩa chỉ cách nhau 3 slide.

```text
FILE: latex/slides/slides.tex
CŨ: $\sigma = 0{,}2$ minh họa
MỚI: $\sigma_d = 0{,}2$ minh họa
```

### D3. [MAJOR] Slide 15, dòng slides.tex 309

Tiếp theo D2.

```text
FILE: latex/slides/slides.tex
CŨ: Theo $\sigma$
MỚI: Theo $\sigma_d$
```

### D4. [MAJOR] Slide 15, dòng slides.tex 321

Tiếp theo D2.

```text
FILE: latex/slides/slides.tex
CŨ: \item $\sigma$, $\phi$ thật
MỚI: \item $\sigma_d$, $\phi$ thật
```

### D5. [MINOR] Slide 22, dòng slides.tex 444–450

Tiêu đề nói "sáu chỉ tiêu" nhưng cột phải chỉ có 4 gạch đầu dòng (gộp hai chỉ số làm một và thiếu chỉ tiêu (3) của v14: ước lượng tác động). Đổi thành danh sách đánh số đúng 6 chỉ tiêu theo mục [87]–[93] của v14, mỗi mục 1 dòng.

```text
FILE: latex/slides/slides.tex
CŨ: \textsb{Sản phẩm}
\begin{itemize}
\item Tệp đăng ký trước có dấu thời gian
\item Chỉ số chất lượng thị trường và chỉ số khả năng đầu tư, mã nguồn mở
\item Ba bài báo, ít nhất một bài WoS Q1/Q2
\item Báo cáo cho Sở KH\&CN Hà Nội, ưu tiên HNX dùng
\end{itemize}
MỚI: \textsb{Sáu chỉ tiêu}
\begin{enumerate}
\item Tệp đăng ký trước (OSF)
\item Chỉ số chất lượng, mã nguồn mở
\item Ước lượng tác động (\HH{3})
\item Chỉ số khả năng đầu tư
\item Ba bài báo, $\geq 1$ bài WoS Q1/Q2
\item Báo cáo cho Sở KH\&CN Hà Nội
\end{enumerate}
```

### D6. [MINOR] Slide 30, dòng slides.tex 534

Ý dài 3 dòng (28 từ), vượt giới hạn ≤2 dòng của Hard Rule 8. Tách thành 2 ý; sau khi tách slide có 6 ý (≤7).

```text
FILE: latex/slides/slides.tex
CŨ: \item Kiểm tra bổ sung: ngày sự kiện giả trong giai đoạn tham chiếu (Conley \& Taber, 2011); chỉ khoảng sáu cửa sổ độc lập nên không dùng làm suy luận chính
MỚI: \item Kiểm tra bổ sung: ngày sự kiện giả (Conley \& Taber, 2011)
\item Chỉ khoảng sáu cửa sổ độc lập \so không dùng làm suy luận chính
```

### C2. [MINOR] Slide 14, dòng slides.tex 279

Trích dẫn để \footnotesize trên dòng riêng (dưới mức \small tối thiểu của Hard Rule 13), cột trái còn 8 dòng. Gộp trích dẫn vào cùng dòng và dùng `\so` của template.

```text
FILE: latex/slides/slides.tex
CŨ: \item Coi mã là độc lập $\Rightarrow$ sai số chuẩn quá nhỏ\\{\footnotesize (Conley \& Taber, 2011)}
MỚI: \item Coi mã là độc lập \so sai số chuẩn quá nhỏ (Conley \& Taber, 2011)
```

### C3. [MINOR] Slide 14, dòng slides.tex 278

Ý xuống 2 dòng chỉ để chứa chữ "sàn". Rút gọn lại.

```text
FILE: latex/slides/slides.tex
CŨ: \item 299 mã nhưng chỉ \al{một lần} chuyển sàn
MỚI: \item 299 mã, chỉ \al{một lần} chuyển sàn
```

### C4. [MINOR] Slide 14, dòng slides.tex 284

Ý xuống 2 dòng, dòng 2 chỉ có "trước". Viết bằng ký hiệu (chỉ số dưới nhiều chữ để đứng).

```text
FILE: latex/slides/slides.tex
CŨ: \item Thống kê: trung bình $d_t$ sau trừ trước
MỚI: \item Thống kê: $\bar{d}_\text{sau} - \bar{d}_\text{trước}$
```

### C5. [MINOR] Slide 16, dòng slides.tex 331

Cột đầu `p{0.22\textwidth}` hẹp nên có dòng lẻ "sàn" và "±7%". Đã thử 0.25: mỗi hàng còn 1 dòng.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.22\textwidth} L L@{}}
MỚI: \begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.25\textwidth} L L@{}}
```

### C6. [MINOR] Slide 16, dòng slides.tex 342

Ý xuống 2 dòng, dòng 2 chỉ có "Holm"; công thức có dấu cách thừa trước `E_{si}`.

```text
FILE: latex/slides/slides.tex
CŨ: \item Tương tác $D_i\Post_t E_{si}$; suy luận cùng cách với $\delta$; là phân tích phụ, ngoài thủ tục Holm
MỚI: \item Tương tác $D_i\Post_tE_{si}$: phân tích phụ, suy luận như $\delta$, ngoài Holm
```

### C1. [MINOR] Slide 6, dòng slides.tex 128

Hai hộp hàng dưới lệch nhau: hộp e đặt `below=of c`, hộp d đặt `below=of b`, mà hộp b cao hơn hộp c, nên đỉnh hai hộp hàng dưới lệch khoảng 9 pt. Đặt e ở `(c |- d)` để hai hộp cùng hàng.

```text
FILE: latex/slides/slides.tex
CŨ: \node[box, text width=3.3cm, below=of c] (e)
MỚI: \node[box, text width=3.3cm] (e) at (c |- d)
```


## 4. Đối chiếu với template Michaillat (bổ sung theo yêu cầu vòng 1)

### B1. [MINOR] Slide 4, dòng slides.tex 86–88

Template không ghi chú bằng một dòng `{\small ...}` màu đen mà dùng `table`/`figure` kèm `\caption` (chữ footnotesize, màu DarkGray, căn giữa; xem slide "Basic table with note"). Cặp B1 và B2 đổi `center` thành `table` và đưa ghi chú vào `\caption`.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{center}
{\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.33\textwidth} L l@{}}
MỚI: \begin{table}
{\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.33\textwidth} L l@{}}
```

### B2. [MINOR] Slide 4, dòng slides.tex 97–100

Tiếp theo B1.

```text
FILE: latex/slides/slides.tex
CŨ: \end{tabularx}}
\end{center}
\vspace{1mm}
{\small \HH{1}--\HH{3}: kiểm định xác nhận, hiệu chỉnh Holm 5\%. \HH{4}: chỉ ước lượng (ít cửa sổ).}
MỚI: \end{tabularx}}
\caption{\HH{1}--\HH{3}: kiểm định xác nhận, hiệu chỉnh Holm 5\%. \HH{4}: chỉ ước lượng (ít cửa sổ).}
\end{table}
```

### B3. [MINOR] Slide 5, dòng slides.tex 105–107

Ghi chú phạm vi tìm kiếm đang để \footnotesize màu đen, ngắt bằng `\\[1mm]` trong `center`, khác cách chú thích của template. Cặp B3 và B4 chuyển sang `table` và `\caption`.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{center}
{\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.27\textwidth} L L@{}}
MỚI: \begin{table}
{\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.27\textwidth} L L@{}}
```

### B4. [MINOR] Slide 5, dòng slides.tex 115–117

Tiếp theo B3.

```text
FILE: latex/slides/slides.tex
CŨ: \end{tabularx}}\\[1mm]
{\footnotesize Trong phạm vi tìm kiếm đến 30/9/2026.}
\end{center}
MỚI: \end{tabularx}}
\caption{Trong phạm vi tìm kiếm đến 30/9/2026.}
\end{table}
```

### B5. [MINOR] Slide 5, dòng slides.tex 112

Hai tài liệu Nielsson (2009) và Hisada (2018) có trong slide "Tài liệu chính" nhưng không được dẫn ở slide nào; slide 5 nhắc Euronext và Tokyo–Osaka mà không ghi nguồn. Đã thử biên dịch: hàng này dài thêm 1 dòng, slide vẫn còn chỗ (chân ở y=220,9 pt).

```text
FILE: latex/slides/slides.tex
CŨ: Euronext, Tokyo--Osaka: thị trường phát triển, chỉ đo thanh khoản
MỚI: Euronext (Nielsson, 2009), Tokyo--Osaka (Hisada, 2018): thị trường phát triển, chỉ đo thanh khoản
```

### B6. [MINOR] Slide 6, dòng slides.tex 122

Hình TikZ để trong `center`, còn chú giải nét liền/nét đứt để dưới dạng `{\footnotesize ...}` màu đen, căn trái. Template đặt hình trong `figure` và chú giải bằng `\caption` (xám, căn giữa). Cặp B6 và B7 sửa chỗ này.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{center}
\begin{tikzpicture}[node distance=5mm and 10mm
MỚI: \begin{figure}
\begin{tikzpicture}[node distance=5mm and 10mm
```

### B7. [MINOR] Slide 6, dòng slides.tex 132–134

Tiếp theo B6.

```text
FILE: latex/slides/slides.tex
CŨ: \end{tikzpicture}
\end{center}
{\footnotesize Nét liền: kiểm định hoặc ước lượng. Nét đứt: tổng hợp định tính.}
MỚI: \end{tikzpicture}
\caption{Nét liền: kiểm định hoặc ước lượng. Nét đứt: tổng hợp định tính.}
\end{figure}
```

### B8. [MINOR] Slide 3, dòng slides.tex 63

Dòng nguồn "QĐ 1193" để \footnotesize màu đen. Trong cột không đặt được `\caption` nên dùng đúng font và màu caption của template.

```text
FILE: latex/slides/slides.tex
CŨ: {\footnotesize QĐ 1193/QĐ-UBND, 2026}
MỚI: {\usebeamerfont{caption}\usebeamercolor[fg]{caption}QĐ 1193/QĐ-UBND, 2026}
```

### B9. [MINOR] Slide 3, dòng slides.tex 80

Nguồn của bảng GFCI cũng vậy; đổi sang font/màu caption và thêm chữ "Nguồn:".

```text
FILE: latex/slides/slides.tex
CŨ: {\footnotesize Wardle \& Mainelli (2026)}
MỚI: {\usebeamerfont{caption}\usebeamercolor[fg]{caption}Nguồn: Wardle \& Mainelli (2026).}
```

### B10. [MINOR] Slide 28, dòng slides.tex 510–511

Ghi chú dưới bảng M1–M7 là `{\small ...}` màu đen, cách bảng bằng `\\[2mm]`. Cặp B10 và B11 chuyển sang `table` và `\caption`.

```text
FILE: latex/slides/slides.tex
CŨ: \end{tabularx}}\\[2mm]
{\small Danh mục chỉ mua; ước lượng lại hằng tháng trên cửa sổ 104 tuần; báo cáo cả khi bỏ \MM{5}.}
MỚI: \end{tabularx}}
\caption{Danh mục chỉ mua; ước lượng lại hằng tháng trên cửa sổ 104 tuần; báo cáo cả khi bỏ \MM{5}.}
\end{table}
```

### B11. [MINOR] Slide 28, dòng slides.tex 496–497

Tiếp theo B10: mở `table`.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Phụ lục: bảy mô hình phân bổ}
{\small
MỚI: \frametitle{Phụ lục: bảy mô hình phân bổ}
\begin{table}
{\small
```

### G1. [MINOR] Slide 19, dòng slides.tex 387–392

Template có khung theorem nền xám LightGray (`\setbeamertemplate{blocks}[rounded]`, nền LightGray), nhưng deck không dùng khung nào. Phần "Giới hạn nêu thẳng" hợp để đặt vào `block` (chỉ một khung, theo đúng Rule 10: không quá 2–3 ý). Đã thử: chân slide ở y=220,1 pt, không tràn.

```text
FILE: latex/slides/slides.tex
CŨ: \textsb{Giới hạn nêu thẳng}
\begin{itemize}
\item GFCI đã chứa dữ liệu giao dịch cổ phiếu
\item $\SMD$ ít đổi theo thời gian
\item $\Rightarrow$ không gọi là tác động nhân quả
\end{itemize}
MỚI: \begin{block}{Giới hạn nêu thẳng}
\begin{itemize}
\item GFCI đã chứa dữ liệu giao dịch cổ phiếu
\item $\SMD$ ít đổi theo thời gian
\item[\so] không gọi là tác động nhân quả
\end{itemize}
\end{block}
```

### E1. [MINOR] Slide 10, dòng slides.tex 200

Template có sẵn ký hiệu `\so` (⇒ kèm khoảng cách mảnh) nhưng deck gõ tay `$\Rightarrow$`. Thay ở mọi chỗ (E1, E2, E4, E5; slide 19 nằm trong G1; slide 14 nằm trong C2). Riêng ý mở đầu bằng mũi tên thì dùng `\item[\so]` như slide "pictograms" của template.

```text
FILE: latex/slides/slides.tex
CŨ: {\small Biên độ hẹp $\Rightarrow$ lợi suất bị cắt $\Rightarrow$ Amihud \al{giảm cơ học}}
MỚI: {\small Biên độ hẹp \so lợi suất bị cắt \so Amihud \al{giảm cơ học}}
```

### E2. [MINOR] Slide 15, dòng slides.tex 319

Như E1.

```text
FILE: latex/slides/slides.tex
CŨ: \item Cửa sổ trước rút còn 24 tháng $\Rightarrow$ ngưỡng tăng khoảng 1,3 lần
MỚI: \item Cửa sổ trước rút còn 24 tháng \so ngưỡng tăng khoảng 1,3 lần
```

### E4. [MINOR] Slide 29, dòng slides.tex 523

Như E1.

```text
FILE: latex/slides/slides.tex
CŨ: giai đoạn sau $\Rightarrow$ khoảng tin cậy có thể rộng
MỚI: giai đoạn sau \so khoảng tin cậy có thể rộng
```

### E5. [MINOR] Slide 30, dòng slides.tex 533

Như E1.

```text
FILE: latex/slides/slides.tex
CŨ: loại cú sốc này $\Rightarrow$ thông tin nằm ở số tháng
MỚI: loại cú sốc này \so thông tin nằm ở số tháng
```

### F1. [MINOR] Slide 10, dòng slides.tex 191

Template không dùng `\small` cho bảng (slide "Basic table" để cỡ thường). Bảng nhỏ ở slide 10 còn thừa chỗ nên bỏ `\small` (vẫn giữ nhóm `{...}` để ngoặc khớp). Cặp F1–F4 đã thử, không gây tràn. Bảng `tabularx` nhiều chữ ở slide 4, 5, 9, 13, 16, 21, 22, 28, 32 vẫn cần `\small`, nên chấp nhận lệch template ở các slide này.

```text
FILE: latex/slides/slides.tex
CŨ: {\small
\begin{tabular}{@{}lcc@{}}
MỚI: {
\begin{tabular}{@{}lcc@{}}
```

### F2. [MINOR] Slide 12, dòng slides.tex 231

Như F1.

```text
FILE: latex/slides/slides.tex
CŨ: {\small
\begin{tabular}{@{}lccc@{}}
MỚI: {
\begin{tabular}{@{}lccc@{}}
```

### F3. [MINOR] Slide 15, dòng slides.tex 306

Như F1.

```text
FILE: latex/slides/slides.tex
CŨ: {\small
\begin{tabular}{@{}cccc@{}}
MỚI: {
\begin{tabular}{@{}cccc@{}}
```

### F4. [MINOR] Slide 31, dòng slides.tex 550

Như F1.

```text
FILE: latex/slides/slides.tex
CŨ: {\small
\begin{tabular}{@{}lccl@{}}
MỚI: {
\begin{tabular}{@{}lccl@{}}
```

### H1. [MINOR] Slide 25, dòng slides.tex 480–485

Template kết thúc bằng `\lastslide` (trang xám trống), không có slide "Xin cảm ơn". Bỏ slide này để giống template.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{frame}
\begin{center}
{\LARGE\sbseries Xin cảm ơn}\\[4mm]
Nguyễn Văn Trung
\end{center}
\end{frame}


MỚI: 
```

### H2. [MINOR] Slide 27, dòng slides.tex 491–493

Template để các slide dự phòng ngay sau `\lastslide`, không có trang ngăn. Trang "Slide phụ lục" lại dùng kiểu riêng (`\Large\sbseries` căn giữa), khác `\heading`. Bỏ trang này; tiêu đề "Phụ lục: ..." của từng slide đã đủ để nhận ra.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{frame}
\begin{center}{\Large\sbseries Slide phụ lục}\end{center}
\end{frame}


MỚI: 
```

### H3. [MINOR] Slide —, dòng slides.tex 22–23

Định nghĩa `cbBlue` và `cbOrange` nhưng không dùng ở đâu; template chỉ dùng một màu nhấn qua `\al{}`. Xóa (MỚI để trống).

```text
FILE: latex/slides/slides.tex
CŨ: \definecolor{cbBlue}{HTML}{0173B2}
\definecolor{cbOrange}{HTML}{DE8F05}

MỚI: 
```

### S1. [MINOR] Slide toàn bộ, dòng sty 20

Template có `\MTsetmathskips{y}` và `{j}` để chỉnh khoảng cách chữ nghiêng; bản dự án bỏ mất, mà deck dùng $j$ trong $\MQI_{jt}$. Thêm lại. Lưu ý thêm: tùy chọn `eulergreek` của template không dùng được ở máy này (thiếu phông `zeur`, đã thử) nên chữ Hy Lạp vẫn lấy từ Computer Modern; nếu máy chính có eulervm thì nên thêm `eulergreek`.

```text
FILE: latex/slides/presentation.sty
CŨ: \usepackage[italic, nolessnomore, noparenthesis, noplusnominus, noequal, nohbar]{mathastext}
MỚI: \usepackage[italic, nolessnomore, noparenthesis, noplusnominus, noequal, nohbar]{mathastext}
\MTsetmathskips{y}{2mu}{0mu}
\MTsetmathskips{j}{2mu}{0mu}
```

### S2. [MINOR] Slide toàn bộ, dòng sty 193–195

Tên môi trường theorem do template định nghĩa vẫn bằng tiếng Anh, nếu dùng sẽ in "Proposition", "Assumption" trên slide tiếng Việt.

```text
FILE: latex/slides/presentation.sty
CŨ: \newtheorem{proposition}{Proposition}
\newtheorem{assumption}{Assumption}
\newtheorem{remark}{Remark}
MỚI: \newtheorem{proposition}{Mệnh đề}
\newtheorem{assumption}{Giả định}
\newtheorem{remark}{Nhận xét}
```

### S3. [MINOR] Slide 1, dòng sty 52

Template để tên deck ở cỡ \huge, nét thường (`shape=\scshape`, không semibold). Bản dự án dùng `series=\sbseries`. Cặp S3 chỉ bỏ semibold. Nếu áp S7 thì không áp S3 (hai cặp sửa cùng một dòng).

```text
FILE: latex/slides/presentation.sty
CŨ: \setbeamerfont{title}{size=\LARGE, series=\sbseries}
MỚI: \setbeamerfont{title}{size=\LARGE}
```

### S4. [MINOR] Slide tất cả slide có tiêu đề, dòng sty 61

Template: tiêu đề slide nét thường (`shape=\scshape`, không có series). Bản dự án thêm `series=\sbseries`. Bỏ semibold cho giống template; chữ hoa giãn cách vẫn giữ nguyên. Đã thử: mọi tiêu đề vẫn nằm trên 1 dòng.

```text
FILE: latex/slides/presentation.sty
CŨ: \setbeamerfont{frametitle}{size=\large, series=\sbseries}
MỚI: \setbeamerfont{frametitle}{size=\large}
```

### S5. [MINOR] Slide 7, 11, 17, 20, dòng sty 199

Template: `\heading` dùng `\LARGE\scshape`, nét thường. Bản dự án thêm `\sbseries`.

```text
FILE: latex/slides/presentation.sty
CŨ: \newcommand*{\heading}[1]{\LARGE\sbseries\color{BlackGray}\singlespacing\capsfont\MakeUppercase{#1}}
MỚI: \newcommand*{\heading}[1]{\LARGE\color{BlackGray}\singlespacing\capsfont\MakeUppercase{#1}}
```

### S6. [MINOR] Slide toàn bộ, dòng sty 7

Template bỏ chữ ghép f (`\DisableLigatures[f]`, chỉ chạy với pdfTeX). Với fontspec thì làm tương đương bằng `Ligatures=NoCommon`.

```text
FILE: latex/slides/presentation.sty
CŨ: \defaultfontfeatures{Ligatures=TeX}
MỚI: \defaultfontfeatures{Ligatures={TeX, NoCommon}}
```

## Đề xuất hình pgfplots (bảng Dark2: tím #7570b3, cam #d95f02, hồng #e7298a; nhãn đặt trên đường, không dùng chú giải)

Theo `figures.pdf`, mỗi hình của template chiếm gần trọn slide (`scale=0.25` trong `wide.tex`) và có `\caption` xám bên dưới. Những slide nên đổi bảng hoặc chữ sang hình, xếp theo thứ tự ưu tiên:

1. **Slide 12 (khác biệt kép).** Thay bảng "Ví dụ minh họa" bằng hình kinh điển của DiD. Trục hoành là tháng, có vạch đứng ở 28/12/2026. Đường tím là mã chuyển sàn, đường cam là mã đối chứng, đường tím nét đứt là phản thực. Mũi tên giữa đường thật và đường phản thực ghi $\delta$. Caption: "Số liệu minh họa, không phải ước lượng". Lưu ý thêm ở mục dưới về con số −0,25.
2. **Slide 15 (lực kiểm định).** Thay bảng 3 dòng bằng hình hiệu ứng nhỏ nhất phát hiện được (theo log Amihud) tại $\phi$ = 0; 0,6; 0,8, vẽ 3 điểm nối liền màu tím. Nhãn "12%", "22%", "30%" đặt ngay trên từng điểm. Thêm một điểm cam cho trường hợp cửa sổ trước rút còn 24 tháng (×1,3).
3. **Slide 10 (biên độ cắt lợi suất).** Vẽ một phân phối lợi suất ngày. Phần đuôi vượt ±7% tô hồng là "bị cắt". Vạch đứng tím ở ngưỡng chung, nhãn ghi ngay trên vạch. Cách này cho thấy vì sao Amihud "giảm cơ học" mà không cần thêm chữ.
4. **Slide 14 (bootstrap tự hồi quy).** Đặt cạnh lưu đồ 4 bước một histogram của thống kê trên chuỗi giả (tím). Vạch cam là giá trị quan sát. Phần đuôi tô hồng là giá trị p.
5. **Slide 2 và 8 (trục thời gian):** giữ TikZ, vì hình hiện tại đúng kiểu template (tối giản, không khung). Chỉ cần sửa A1.

Không nên thay: bảng GFCI ở slide 3 (chỉ có 2 con số), bảng giả thuyết ở slide 4 và bảng rủi ro ở slide 21 (nội dung là chữ).

## Ngoài phạm vi hình thức (ghi lại để main cân nhắc, không tính điểm)

- Slide 12 dùng $\delta = -0{,}25$ (và $-22\%$) trong bảng "Ví dụ minh họa". `ban-giao-slide/GHI-CHU.md` mục 1 ghi rõ "Ví dụ không được dùng: … δ = −0,25". Slide có ghi chữ "minh họa", nhưng con số này lại trùng với hiệu ứng nhỏ nhất phát hiện được 0,25/22% ở slide 15, nên dễ bị hiểu là kết quả. Nên đổi sang số khác hoặc dùng hình ở đề xuất 1 mà không ghi số.
- Màu nhấn RubineRed (dvipsnames) trên nền trắng có độ tương phản khoảng 4,3:1, thấp hơn một chút so với mức WCAG AA 4,5:1. Đây là màu của template nên giữ nguyên, nhưng không nên dùng \al{} cho chữ \small hay chữ nhỏ hơn.
- Slide 31: cảnh báo hyperref về `\translate` đến từ `\appendix`. Nếu áp H2 và bỏ luôn `\appendix` thì cảnh báo mất, nhưng skill beamer (Hard Rule 14) lại khuyên giữ `\appendix`. Tôi không đề xuất cặp sửa cho điểm này.

## Chấm điểm theo rubric 100 của skill beamer (bản hiện tại)

| Mục trừ | Áp vào | Điểm |
|---|---|---|
| Lỗi hiển thị nghiêm trọng mà log không báo. Rubric không có mục riêng; ánh xạ vào mức Critical −15, ngang "undefined" | A1, slide 2 | −15 |
| Trang tiêu đề kín đến mép dưới (Major, ánh xạ như nội dung sát tràn) | A2/S7, slide 1 | −5 |
| Ký hiệu không nhất quán (σ hai nghĩa) | D2–D4 | −3 |
| Vượt ≤2 công thức trưng bày (Major, ánh xạ như vi phạm mật độ) | D1, slide 18 | −3 |
| Giảm cỡ chữ (\footnotesize cho chữ thường), −1 mỗi slide | slide 3, 5, 6, 14 | −4 |
| Tiêu đề xuống 2 dòng làm chật slide (Minor, ánh xạ), −1 mỗi slide | slide 4, 5, 6, 9, 18, 19 | −6 |
| Các điểm lệch template còn lại (nhóm 4 trừ B, C2) | không có mục tương ứng trong rubric | 0 |
| **Tổng** | | **64/100** |

Ngưỡng của skill: dưới 80 là "Must fix". Nếu áp đủ các cặp ở trên (đã kiểm chứng trên `/tmp/sF`), các mục trừ đều hết; phần còn lại chỉ là `\small` ở các bảng `tabularx` dài, ước tính **≥ 95/100**.

## Bảng đếm

| Mức | Số phát hiện | Mã |
|---|---|---|
| CRITICAL | 1 | A1 |
| MAJOR | 4 | A2, S7 (hai cặp cho cùng lỗi trang tiêu đề; áp S7 thì bỏ S3), D1, D2 (gồm D3, D4) |
| MINOR | 35 | A3–A10; B1/B2, B3/B4, B5, B6/B7, B8, B9, B10/B11; C1–C6; D5, D6; E1 (gồm E2, E4, E5); F1 (gồm F2–F4); G1; H1–H3; S1–S6 |
| **Tổng** | **40** | (các cặp ghi "Tiếp theo"/"Như" không tính thành phát hiện riêng) |
