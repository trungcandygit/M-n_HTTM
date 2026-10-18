# Rà soát hình thức slide, vòng 1, người rà soát A

**Bản được rà soát:** `latex/slides/slides.tex` (md5 `77a85cc5…`) và `latex/slides/presentation.sty` (md5 `9cbceb58…`, commit `ea6eef5`).
- Ở bản này, presentation.sty đã về sát bản gốc template. Chỉ có ba chỗ đánh dấu [VN]: bỏ T1, tắt ghép chữ f bằng fontspec, nạp fontspec trước sourcesanspro. Tiêu đề dùng `\scshape\MakeLowercase` như template, với chữ hoa nhỏ thật của Source Sans Pro.
- Trong lúc tôi rà, sty đổi hai lần (Inter, rồi Source Sans Pro với chữ hoa giãn cách, rồi bản hiện tại). Mọi số đo và cặp sửa dưới đây đều làm lại trên bản hiện tại.
- Báo cáo không đề xuất lại việc chọn phông Source Sans Pro và cách viết hoa tiêu đề.

**Skill đã nạp:** `beamer` (gồm audit, tikz, validate, rubric 100, Hard Rules), `beamer-check` (chỉ dùng phần phân tích log, vì script gọi pdflatex), `slide-design-principles` (đọc cả hai tệp trong references/), `latex-econ-model`.

**Cách làm** (tuân thủ quy tắc không render ảnh):
- Biên dịch bản sao bằng `xelatex` hai lần.
- Đọc log bằng các regex của `beamer_check.py`.
- Đo tọa độ chữ bằng `pdftotext -bbox`. Trang 453,54 × 255,12 pt; lề chữ 14,17–439,37 pt; `\textheight` = 252,07 pt. Từ đó tính số dòng tiêu đề, mép dưới nội dung, chữ vượt lề và chữ chồng nhau.
- Dùng `pdffonts` theo từng trang để biết phông thật được nhúng, và fontTools để kiểm bảng chữ hoa nhỏ (smcp) của Source Sans Pro.
- Đối chiếu với `presentation.tex`, `wide.tex`, `presentation.sty`, `README.md` của template gốc. Hai tệp `presentation.pdf` và `figures.pdf` chỉ đọc phần chữ.

**Các cặp sửa đã được kiểm chứng.** Tôi áp toàn bộ cặp CŨ/MỚI trong báo cáo vào bản sao `/tmp/sG`, rồi biên dịch XeLaTeX hai lần:
- Mã thoát 0; không còn Overfull, Underfull hay cảnh báo phông.
- Mọi tiêu đề nằm trên 1 dòng và không vượt x = 430 pt.
- Không trang nào còn dùng LMRoman.
- Mép dưới cao nhất là 240,2 pt (slide tài liệu); trang tiêu đề kết thúc ở 229,7 pt.
- Trục thời gian ở slide 2 hiện đủ nhãn.
- Mỗi chuỗi CŨ xuất hiện đúng 1 lần trong tệp hiện tại (đã đếm bằng script), nên các cặp áp được theo thứ tự bất kỳ.
- Bản thử còn có thêm hai cặp rút gọn tiêu đề slide 3 và slide 15. Ở bản hiện tại hai tiêu đề này đã vừa 1 dòng (x ≤ 428,5 pt) nên tôi không đưa thành phát hiện.

## Validate (skill beamer, mục 2.10)

| Kiểm tra | Kết quả | Trạng thái |
|---|---|---|
| Số trang | 32 trang. Phần chính có 25 trang (19 slide nội dung, 4 slide mục, trang tiêu đề, slide cảm ơn), thêm `\lastslide` và 6 trang phụ lục. Với 30 phút là khoảng 1,6 phút một slide nội dung, khớp mức 1,5–2 phút của skill | OK |
| Tỷ lệ khung | 453,54 × 255,12 pt (16:9) | OK |
| Dung lượng tệp | 73,7 KB | OK |
| Overfull hbox / vbox | 0 / **1** (trang tiêu đề, 4,65 pt, dòng 34) | **CRITICAL** |
| Lệnh chưa định nghĩa, trích dẫn chưa định nghĩa, nhãn trùng | 0 | OK |
| Cảnh báo phông | **30** (thiếu semibold, LaTeX tự thay bằng bold) | **FAIL** |
| Cảnh báo khác | 1: hyperref `\translate` ở dòng 491, sinh ra từ `\appendix`. Không ảnh hưởng hiển thị | OK |
| Lệnh overlay | 0 | OK |
| Slide có hơn 2 khung màu | 0 (deck chưa có khung nào) | OK |
| `\tiny` | 0 | OK |
| Slide tài liệu tham khảo | Có (slide 24) | OK |
| Bảng tô nền xám | 0 | OK |
| Slide chỉ có chữ | 1/19 trong phần chính (slide 23) | OK |
| Log sạch nhưng lỗi vẫn hiện trên slide | Có: trục thời gian slide 2 bị cắt nhãn (A1) | **FAIL** |

Kết luận validate: **FAIL**.

## Số đo bố cục (bản hiện tại)

- **Trang tiêu đề:** chữ chiếm từ y = 10,0 đến 258,1 pt, tức vượt mép dưới trang 3 pt (N3).
- **Tiêu đề slide:** ở cỡ \Large chữ hoa nhỏ, có 6 slide xuống 2 dòng: 4, 5, 6, 9, 18, 19. Hai dòng cách nhau 17 pt, khung chữ cao 20,4 pt vì có dấu thanh chồng. Script báo hai dòng chồng 3,5 pt theo khung chữ. Chữ hoa nhỏ không có phần chân chữ, nên trên thực tế dấu ở dòng dưới chỉ còn cách dòng trên khoảng 2–3 pt: chưa đè nhưng rất sát.
- **Mép dưới nội dung:** slide 24 ở 240,2 pt, slide 9 ở 240,0, slide 4 ở 238,9. Không slide nội dung nào vượt `\textheight`. Không có chữ hay nhãn TikZ nào chồng nhau (đã kiểm slide 2, 6, 8, 14).
- **Chữ hoa nhỏ:** `pdftotext` xuất "THị", "NGHiỆM", tức chữ "i" ra chữ thường. Kiểm bằng fontTools: bảng `smcp` của Source Sans Pro có ánh xạ đủ i, í, ì, ỉ, ĩ, ị (i → I.s, ị → uni1ECA.s). Đây chỉ là lỗi khi trích chữ, không phải lỗi hiển thị.
- **Cỡ chữ:** nhỏ nhất ngoài chỉ số dưới là \footnotesize (dòng nguồn ở slide 3, 5, 6, 14; nhãn TikZ ở slide 2, 6, 8). Template để caption ở cỡ footnotesize, màu DarkGray. Vì yêu cầu là bám sát template, nhóm B chuyển các dòng nguồn này sang kiểu caption của template thay vì nâng lên \small như Hard Rule 13.

## 1. Lỗi hiển thị, tràn và phông

### A1. [CRITICAL] Slide 2, dòng slides.tex 42

Nhãn trục thời gian bị cắt. `\foreach \x/\a/\b` tách theo dấu "/", nên mốc thứ tư hiện "30" ở trên và "9" ở dưới (mất "/9/2026" và "VNX công bố lịch"); nhãn TT 139 chỉ còn "TT 139: lùi đến 31" (mất "/12/2026"). Kiểm bằng `pdftotext -bbox`: tại x≈277–290 pt chỉ có từ "30", tại x≈280 pt chỉ có "9". Log biên dịch không báo gì. Sửa: bọc trường có "/" trong ngoặc nhọn.

```text
FILE: latex/slides/slides.tex
CŨ: \foreach \x/\a/\b in {0.4/2021/TT 57: hạn năm 2023, 3.2/2023/TT 69: lùi đến hết 2025, 6.0/2025/TT 139: lùi đến 31/12/2026, 8.8/30/9/2026/VNX công bố lịch}
MỚI: \foreach \x/\a/\b in {0.4/2021/{TT 57: hạn năm 2023}, 3.2/2023/{TT 69: lùi đến hết 2025}, 6.0/2025/{TT 139: lùi đến 31/12/2026}, 8.8/{30/9/2026}/{VNX công bố lịch}}
```

### N3. [CRITICAL] Slide 1, dòng slides.tex 30–31

Trang tiêu đề tràn khỏi trang: dòng "Hà Nội, 2026" nằm ở y=241,1–258,1 pt, mà trang chỉ cao 255,12 pt. Log báo `Overfull \vbox (4.64793pt too high) detected at line 34`. Nguyên nhân: tên đề tài ở \huge xuống 4 dòng, cộng với khối tác giả 2 dòng và dòng ngày. Sửa trong slides.tex, không đụng sty: đưa "Hà Nội, 2026" lên dòng tên theo mẫu "Location -- Date" của template và để `\date` trống. Đã thử: không còn Overfull, trang kết thúc ở y=229,7 pt, không mất chữ nào.

```text
FILE: latex/slides/slides.tex
CŨ: \author{Nguyễn Văn Trung\\[1mm]{\normalsize Đề cương nghiên cứu sinh, ngành Kinh tế và Quản lý, Trường Quốc tế, ĐHQGHN}}
\date{Hà Nội, 2026}
MỚI: \author{Nguyễn Văn Trung -- Hà Nội, 2026\\[1mm]{\normalsize Đề cương nghiên cứu sinh, ngành Kinh tế và Quản lý, Trường Quốc tế, ĐHQGHN}}
\date{}
```

### N1. [MAJOR] Slide mọi slide có `\textsb`, tiêu đề khung, nút TikZ `\sbseries`, dòng sty 10–11

Dưới XeLaTeX, gói `sourcesanspro` không khai báo kiểu chữ semibold: log có 30 cảnh báo `Font shape TU/SourceSansPro(0)/sb/n undefined, using b/n instead`, và pdffonts chỉ thấy SourceSansPro-Bold, không có Semibold. Vì vậy mọi `\textsb{...}` (đầu cột ở slide 3, 10, 12–15, 18, 19, 21–23), tiêu đề khung và nhãn TikZ đều in đậm hẳn (Bold), không phải Semibold như template. Cặp này khai báo lại phông với `FontFace={sb}`. Đã thử: hết cảnh báo, PDF có SourceSansPro-Semibold, chữ hoa nhỏ ở tiêu đề vẫn giữ.

```text
FILE: latex/slides/presentation.sty
CŨ: \usepackage{sourcesanspro}
MỚI: \usepackage{sourcesanspro}
\setsansfont{SourceSansPro}[Extension=.otf, UprightFont=*-Regular, ItalicFont=*-RegularIt, BoldFont=*-Bold, BoldItalicFont=*-BoldIt, FontFace={sb}{n}{*-Semibold}, FontFace={sb}{it}{*-SemiboldIt}]
```

### N2. [MAJOR] Slide 9, 12, 16, 18, 19, dòng slides.tex 17

Tên biến nhiều chữ viết đứng ($\MQI$, TK, HQ, MB, $\Post$, $\SMD$, H, CS) dùng `\mathrm`, mà mathastext không đổi `\mathrm`, nên các chữ này in bằng Latin Modern có chân (pdffonts thấy LMRoman10 ở đúng các slide 9, 12, 16, 18, 19), lạc giữa chữ không chân Source Sans Pro. Template lấy chữ trong công thức theo phông văn bản. Đã thử: hết LMRoman, chỉ số dưới vẫn co đúng cỡ.

```text
FILE: latex/slides/slides.tex
CŨ: \newcommand{\vn}[1]{\mathrm{#1}}
MỚI: \newcommand{\vn}[1]{\text{\normalfont #1}}
```

### A2. [MINOR] Slide 1, dòng slides.tex 29

Tên đề tài ở \huge, chữ hoa nhỏ, xuống 4 dòng; dòng 2 chỉ có "TRƯỜNG:", dòng 4 là "CHÍNH HÀ NỘI". Ngắt tay thành 4 dòng cân nhau (giữ nguyên từng chữ, chỉ thêm `\\`). Lỗi tràn trang tiêu đề là N3; cặp này chỉ để bố cục đẹp hơn.

```text
FILE: latex/slides/slides.tex
CŨ: \title{Hợp nhất sàn chứng khoán và chất lượng thị trường:\\ Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội}
MỚI: \title{Hợp nhất sàn chứng khoán\\ và chất lượng thị trường:\\ Bằng chứng thực nghiệm từ HNX\\ và vị thế tài chính Hà Nội}
```


## 2. Tiêu đề quá dài (xuống 2 dòng hoặc sát lề phải)

### A4. [MINOR] Slide 4, dòng slides.tex 85

Tiêu đề xuống 2 dòng nên bảng bị đẩy xuống, chân bảng tới y=238,9 pt.

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

Tiêu đề xuống 2 dòng; slide có công thức, bảng và 2 ý nên chân tới y=240,0 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Chỉ số chất lượng thị trường vốn: ba chiều, sáu chỉ báo, trọng số bằng nhau}
MỚI: \frametitle{Chỉ số chất lượng: ba chiều, sáu chỉ báo, trọng số bằng nhau}
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

### S2. [MINOR] Slide toàn bộ, dòng sty 217–219

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

## Mức khớp template sau commit `ea6eef5`

presentation.sty đã khớp bản gốc, chỉ trừ ba chỗ [VN] và hai lỗi XeLaTeX ở trên (N1 thiếu semibold, N2 `\mathrm` in phông Latin Modern). Phần còn lệch nằm trong slides.tex:

| Mặt | Template | Deck hiện tại | Phát hiện |
|---|---|---|---|
| Chú thích hình, bảng | `figure`/`table` + `\caption`, chữ footnotesize màu DarkGray, căn giữa | Dòng `{\small ...}` hoặc `{\footnotesize ...}` màu đen, căn trái | B1–B11 |
| Khung theorem nền LightGray | Có ở slide theorem, lemma, proposition, corollary | Không slide nào dùng | G1, S2 |
| Ký hiệu `\so`, `\then` | Dùng cho quan hệ suy ra | Gõ tay `$\Rightarrow$` | E1–E5, C2 |
| Cỡ chữ bảng | Cỡ thường | `\small` ở mọi bảng | F1–F4 (bảng dài vẫn giữ `\small`) |
| Slide cuối | `\lastslide`, rồi slide dự phòng ngay sau | Slide "Xin cảm ơn", `\lastslide`, rồi trang "Slide phụ lục" kiểu riêng | H1, H2 |
| Màu | Chỉ RubineRed qua `\al` | Có thêm `cbBlue`, `cbOrange` không dùng | H3 |
| Slide mục `\heading` | 4 slide, kiểu chuẩn | Khớp | — |
| Khoảng cách, lề, màu chữ, gạch đầu dòng | Theo sty | Khớp (sty là bản gốc) | — |

## Đề xuất hình pgfplots (Dark2: tím #7570b3, cam #d95f02, hồng #e7298a; nhãn trên đường, không chú giải)

Thư mục `latex/slides/hinh/` đã có `mde.tex`, `tran.tex`, `buocgia.tex` (kiểu `mau` trong `kieu.tex`), nhưng slides.tex chưa `\input` tệp nào. Gợi ý cách gắn hình và những slide nên đổi sang hình, theo thứ tự ưu tiên:

1. **Slide 15:** thay bảng 3 dòng bằng `hinh/mde.tex`, đặt trong `figure` với `\caption{Lực 80\%, mức một phía 0,05/3; $\sigma_d = 0{,}2$ minh họa.}`. Bỏ dòng `{\small (lực 80\%...)}` vì caption đã thay nó.
2. **Slide 10:** thay bảng biên độ và bước giá bằng `hinh/tran.tex` (lợi suất trần theo giá, HNX so với HOSE). Có thể thêm `hinh/buocgia.tex`, nhưng mỗi slide chỉ nên có một hình như `figures.pdf`; hình bước giá nên sang slide phụ lục.
3. **Slide 12 (khác biệt kép):** thay bảng "Ví dụ minh họa" bằng hình DiD. Trục hoành là tháng, có vạch ở 28/12/2026. Đường tím là mã chuyển sàn, đường cam là mã đối chứng, đường tím nét đứt là phản thực. Mũi tên ghi $\delta$ đặt giữa đường thật và phản thực. Caption: "Số liệu minh họa". Xem thêm lưu ý về −0,25 ở mục dưới.
4. **Slide 14:** đặt cạnh lưu đồ một histogram thống kê trên chuỗi giả (tím). Vạch cam là giá trị quan sát. Đuôi tô hồng là giá trị p.
5. **Slide 2 và 8:** giữ trục thời gian TikZ (tối giản, không khung), chỉ cần sửa A1.

Không nên đổi sang hình: bảng GFCI ở slide 3 (chỉ có 2 số), bảng giả thuyết ở slide 4, bảng rủi ro ở slide 21.

## Ngoài phạm vi hình thức (để main cân nhắc, không tính điểm)

- Slide 12 dùng $\delta = -0{,}25$ và $-22\%$ trong bảng minh họa. `ban-giao-slide/GHI-CHU.md` mục 1 ghi "Ví dụ không được dùng: … δ = −0,25". Con số này lại trùng với hiệu ứng nhỏ nhất 0,25/22% ở slide 15, nên dễ bị đọc thành kết quả.
- RubineRed trên nền trắng có độ tương phản khoảng 4,3:1, thấp hơn mức WCAG AA 4,5:1. Đây là màu của template nên giữ nguyên, nhưng tránh dùng `\al{}` cho chữ nhỏ.
- Cảnh báo hyperref `\translate` đến từ `\appendix`. Template không có `\appendix`, nhưng Hard Rule 14 của skill khuyên giữ, nên tôi không đề xuất sửa.
- Tùy chọn `eulergreek` và `mathalpha` trong sty đã chạy được ở máy này (pdffonts thấy EURM10, MnSymbol10). Phần này không cần sửa.

## Chấm điểm theo rubric 100 của skill beamer (bản hiện tại)

| Mục trừ | Áp vào | Điểm |
|---|---|---|
| Nội dung tràn khỏi trang. Ánh xạ vào mức Critical "Overfull > 10pt" vì chữ bị cắt ở mép trang dù chỉ thừa 4,65 pt | N3, slide 1 | −10 |
| Lỗi hiển thị mà log không báo. Ánh xạ vào mức Critical −15 | A1, slide 2 | −15 |
| Ký hiệu không nhất quán: σ mang hai nghĩa | D2–D4 | −3 |
| Công thức in sai phông (Latin Modern lẫn trong Source Sans), tính như không nhất quán ký hiệu | N2 | −3 |
| Thiếu semibold, LaTeX thay bằng bold (Major, ánh xạ) | N1 | −3 |
| Hơn 2 công thức trưng bày trên một slide (Major, ánh xạ) | D1, slide 18 | −3 |
| Giảm cỡ chữ (\footnotesize cho chữ thường), −1 mỗi slide | slide 3, 5, 6, 14 | −4 |
| Tiêu đề xuống 2 dòng làm chật slide (Minor, ánh xạ), −1 mỗi slide | slide 4, 5, 6, 9, 18, 19 | −6 |
| Các điểm lệch template khác (nhóm 4) | rubric không có mục tương ứng | 0 |
| **Tổng** | | **53/100** |

Ngưỡng của skill: dưới 80 là "Must fix". Nếu áp đủ các cặp (đã kiểm chứng trên `/tmp/sG`), mọi mục trừ đều hết; phần còn lại chỉ là `\small` ở các bảng `tabularx` dài, ước tính **≥ 95/100**.

## Bảng đếm

| Mức | Số phát hiện | Mã |
|---|---|---|
| CRITICAL | 2 | A1, N3 |
| MAJOR | 4 | N1, N2, D1, D2 (gồm D3, D4) |
| MINOR | 29 | A2, A4–A7, A9, A10; B1/B2, B3/B4, B5, B6/B7, B8, B9, B10/B11; C1–C6; D5, D6; E1 (gồm E2, E4, E5); F1 (gồm F2–F4); G1; H1–H3; S2 |
| **Tổng** | **35** | (các cặp ghi "Tiếp theo"/"Như" không tính thành phát hiện riêng) |
