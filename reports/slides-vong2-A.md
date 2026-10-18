# Rà soát slide vòng 2, người rà soát A (hình thức và mức khớp template)

**Bản được rà soát:** `latex/slides/slides.tex` (md5 `80daae8f…`), `presentation.sty` (`ec9f24af…`), `hinh/did.tex` (`b075ec63…`), `hinh/kieu.tex` (`24e48323…`), commit `d3d7858`. Bản này 37 trang: 26 trang chính (20 khung nội dung, trang tiêu đề, 4 slide mục, 2 trang tài liệu), `\lastslide`, 8 trang phụ lục.

**Cách làm (không render ảnh).** Biên dịch bản sao bằng `xelatex` hai lần. Đọc log bằng các regex của `beamer_check.py` (không chạy script vì nó gọi pdfLaTeX và render ảnh). Đo chữ bằng `pdftotext -bbox`; xác định phông theo từng trang bằng `pdffonts`; giải nén luồng nội dung PDF bằng pypdf để lấy cỡ chữ (Tf × CTM), màu, độ dày nét, alpha và tọa độ đường vẽ. Nhãn biểu đồ được kiểm bằng cách giao hộp chữ với các đoạn thẳng đã vẽ. Làm cùng việc đó với `wide.pdf`, `presentation.pdf` và `figures.pdf` của template để có số đối chiếu.

**Kiểm chứng các cặp sửa.** Cả 17 cặp CŨ/MỚI dưới đây được áp bằng script lên bản sao `scratchpad/v2A/new/` (mỗi chuỗi CŨ đã được đếm, xuất hiện đúng 1 lần trong tệp hiện tại của repo, các cặp không chồng nhau nên áp theo thứ tự nào cũng được). Biên dịch hai lần: mã thoát 0; 36 trang; 0 Overfull, 0 Underfull, 0 cảnh báo phông; 0 lệnh overlay; mọi tiêu đề 1 dòng, x tối đa 418,2 pt (lề phải 439,4); chân nội dung thấp nhất 239,7 pt (slide 13 mới); không còn nhãn nào chạm đường vẽ. Còn đúng một cảnh báo hyperref `\translate` sinh từ `\appendix` (đã chấp nhận).

## Skill đã nạp và đã dùng vào việc gì

| Skill | Đã đọc | Dùng vào |
|---|---|---|
| beamer | SKILL.md, create-workflow, review-actions, tikz-standards | Hard Rules (overlay, tối đa 2 khung, cỡ chữ TikZ, ý ≤ 2 dòng), validate, audit, kiểm nhãn TikZ, rubric 100 điểm |
| beamer-check | SKILL.md và toàn bộ `beamer_check.py` | Chỉ dùng regex phân tích log (Overfull/Underfull/lỗi); không chạy script |
| beamer-presentation | SKILL.md, reference.md, danh sách examples | Tiêu đề nêu kết luận, ngân sách thời gian 30 phút, phụ lục sau `\appendix` |
| slide-design-principles | SKILL.md, hai tệp references | Một ý mỗi slide, tối giản, chỉ giữ hình khi cần, màu an toàn |
| latex-econ-model | SKILL.md | Quy ước công thức: tham số Hy Lạp, chỉ số dưới không dấu phẩy, tên biến nhiều chữ viết đứng |
| econ-write | SKILL.md, specialized-tasks (presentations), identification-strategies, review-checklist, latex-tips | Định nghĩa ký hiệu ngay sau phương trình (F6), tiêu đề nêu kết luận, giải thích trực giác của DiD |
| mhe-identification | SKILL.md và 6 tệp references/research | Kiểm nguồn biến thiên ngoại sinh (F2), suy luận với một sự kiện và cú sốc chung theo tháng (F13) |
| aer-identification | SKILL.md, estimator-playbook | DiD 2×2 một ngày: TWFE hợp lệ; suy luận khi có một nhóm xử lý; không có red flag |
| mostly-harmless-guide | SKILL.md | Đối chiếu giả định xu hướng song song, phân cụm |
| panel-data-guide | SKILL.md | Kiểm hiệu ứng cố định α_i, τ_t trong (5)–(7) |
| review-methodology | SKILL.md | Rà ngôn ngữ nhân quả: H₁ "liên hệ có điều kiện", δ "tác động gộp" |
| review-pap | SKILL.md | Rà các slide đăng ký trước, phương án dự phòng (F16) |
| credible-claims | SKILL.md | Không nâng số minh họa thành kết quả (F17) |
| consistency-checker | SKILL.md, checklist | Đối chiếu tiêu đề với nội dung (F13), bảng với v14 (F16), trích dẫn trong slide với danh mục |
| fact-checker | SKILL.md | Đối chiếu mọi con số mới thêm với v14 (ghi số đoạn trong từng phát hiện) |
| scientific-critical-thinking | SKILL.md, danh mục references | Tách điều đã chứng minh với điều minh họa |
| statistical-power | SKILL.md, danh mục references | Báo cáo MDE theo dải φ (độ nhạy) thay vì một số; không dùng "observed power" |
| statistical-analysis | SKILL.md, danh mục references | Đọc giá trị p minh họa ở slide Holm |
| liquidity-measures | SKILL.md | Bẫy biên độ và bước giá cho Amihud, Corwin–Schultz, tỷ lệ ngày lợi suất 0 (F5) |
| vn-legal-verify | SKILL.md | Mốc Thông tư 57/2021, 69/2023, 139/2025 và thông báo VNX 30/9/2026 ở F2 khớp v14 [73] |
| citation-management | SKILL.md, bibtex_formatting | Chỉ kiểm cục bộ: APA "&" trong ngoặc, "và" ngoài ngoặc ở mọi trích dẫn trên slide; không tra cứu ngoài |
| vina-me | SKILL.md | Viết lại các ý mới cho thuận miệng; giọng trang trọng; không thêm dữ kiện ngoài v14 |
| vietnamese-human-writing | SKILL.md, mục II–IV bộ quy tắc | Tránh sáo ngữ, không bịa, không phóng đại trong câu mới |
| sciwrite | SKILL.md (5 lượt rà) | Cắt chữ thừa, động từ trực tiếp trong các câu mới |

Chuẩn nội dung đã đối chiếu: `outputs/round-14/v14-text-round-14.txt` (đọc các đoạn [66]–[246] và danh mục tài liệu), `ban-giao-slide/GHI-CHU.md`, `ho-so/tham-khao/Shapiro-How-to-Give-an-Applied-Micro-Talk.txt`. Quy tắc chung theo `CLAUDE.md`.

## Số đo template (để đối chiếu)

- `wide.pdf`: trang 453,54 × 255,12 pt; tên đề tài 20,66 pt; tiêu đề slide 14,35 pt; chữ thường 10,91 pt màu xám 0,15 (BlackGray); caption 8,97 pt màu 0,675 (DarkGray). Phông: Source Sans Pro, MnSymbol cho dấu = + ( ), EURM10 cho chữ Hy Lạp; **không có CMR**.
- `figures.pdf` (đặt trên slide ở scale 0,25): chữ trục 10,06 pt, nhãn trên đường 8,75 pt; đường dữ liệu 1,37 pt (Dark2 tím #7570b3, cam #d95f02, hồng #e7298a); trục và vạch chia màu đen 0,46 pt, vạch chia hướng ra ngoài, **không có mũi tên ở trục**; lưới **chỉ nằm ngang**, đen, độ mờ 0,149; vùng tô cùng màu đường, độ mờ 0,2; không chú giải.
- Deck: tên đề tài 20,66 pt, tiêu đề slide 14,35 pt, chữ thường 10,91 pt, caption 8,97 pt, màu 0,15 và 0,675: **khớp**. Lệch: chữ số trong công thức là CMR10 (F1); trục biểu đồ có mũi tên, màu black!70, lưới cả hai chiều (F10, F11); 5 hình TikZ kiểu sơ đồ mà template không có (F2–F5, F12).

## Validate (skill beamer, mục 2.10), bản hiện tại → bản sau sửa

| Kiểm tra | Hiện tại | Sau sửa |
|---|---|---|
| Số trang / thời lượng | 37 trang, 20 khung nội dung (≈ 1,5 phút/khung) | 36 trang, 20 khung nội dung: OK |
| Tỷ lệ khung | 453,54 × 255,12 pt (16:9) | OK |
| Overfull / Underfull | 0 / 0 | 0 / 0 |
| Cảnh báo phông | 0 | 0 |
| Phông lạ trong công thức | CMR10, CMR9, CMR8 ở 11 trang (chữ số, = + ( )) | Chỉ còn CMR10 cho dấu gạch ngang của `\bar` (3 trang, xem Ghi chú 1) |
| Lệnh overlay | 2 (`\only<1>`, `\only<2>`, slide 10–11): VIOLATION | 0 |
| Slide hơn 2 khung | 0 | 0 |
| `\tiny` | 0 | 0 |
| Tiêu đề 1 dòng | Mọi khung (x tối đa 420,2 pt) | Mọi khung (x tối đa 418,2 pt) |
| Nhãn đè nhau hoặc đè đường | 3 chỗ ở slide 15, 1 chỗ ở slide 18 | 0 |
| Slide tài liệu tham khảo | Có | Có |

## Đánh giá từng hình (yêu cầu 3 của người dùng)

| Hình | Cần thật không | Đề xuất |
|---|---|---|
| Trục thời gian (slide 2) | Không. Ba thông tư và hai ngày đọc ngay được từ bảng; template không có sơ đồ TikZ | Thay bằng bảng 4 dòng (F2) |
| Khung phân tích 5 hộp (slide 6) | Không. Trùng bảng giả thuyết slide 4, cần chú thích dài để đọc mũi tên | Thay bằng chuỗi lập luận đánh số (F3) |
| Ba giai đoạn (slide 8) | Không. Ba khoảng thời gian | Thay bằng bảng 3 dòng có cột "Dùng để" (F4) |
| Bước giá/giá và lợi suất trần (slide 10–11) | Không. Người nghe cần biết quy tắc nào đổi và chỉ báo nào méo, không cần đường cong | Thay bằng bảng 2 dòng và 2 ý định tính, bỏ overlay (F5) |
| Khác biệt kép (slide 15) | **Có.** Đây là trực giác cốt lõi: tác động là khoảng cách so với đường phản thực | Giữ; sửa 3 nhãn chồng (F7–F9) và kiểu trục cho giống figures.pdf (F10, F11) |
| Lưu đồ bootstrap (slide 17) | Không. Bốn bước là một danh sách đánh số | Thay bằng enumerate, thêm câu "Ý tưởng" (F12) |
| Hiệu ứng nhỏ nhất theo φ (slide 18) | Không, và hình không chứng minh tiêu đề ("ít vào số mã") | Thay bằng 2 ý định tính và bảng 3 cột với đúng số v14 (F13) |

Sau sửa, deck còn 1 hình (khác biệt kép). Các tệp `hinh/buocgia.tex`, `tran.tex`, `mde.tex` và `.dat` không còn được gọi; main có thể giữ trong repo làm tư liệu hoặc xóa.

## Phần định tính được thêm (yêu cầu 1), mỗi câu có nguồn v14

- Slide 2: vì sao sự kiện này đo được tác động (ngày do cơ quan quản lý ấn định, không do doanh nghiệp chọn) [76].
- Slide 6: ba mắt xích sàn → chất lượng → khả năng đầu tư → vị thế trung tâm, mắt xích cuối không kiểm định nhân quả [111]–[112]; tiền lệ Bắc Kinh [75]; các thị trường HNX còn vận hành [71].
- Slide 8: vì sao giai đoạn chuyển tiếp bị loại [131], [176].
- Slide 10: bước giá giảm mười lần hay một nửa tùy mức giá [122]; vì sao phải xử lý (thay đổi do quy tắc, không do chất lượng) [121], [124].
- Slide 14: α_i, τ_t hấp thụ gì [169].
- Slide 17: ý tưởng của bootstrap [172].
- Slide 18: vì sao số tháng quan trọng hơn số mã, vì sao tự tương quan làm giảm lực [205], [182].
- Slide 21: lợi suất tương đương chắc chắn nghĩa là gì, dấu của Ḡ đọc thế nào [151], [159].

## Phát hiện

### F1. [MAJOR] Slide mọi slide có công thức (9, 14, 17, 18, 21, 22, 25, 31, 32) và mọi biểu đồ, dòng 10 (presentation.sty)

Chữ số, dấu =, + và ngoặc trong công thức in bằng Computer Modern có chân (CMR10, CMR9, CMR8 trong pdffonts), lạc giữa Source Sans Pro. Nguyên nhân: fontspec nạp với chế độ toán mặc định nên ở \begin{document} nó khai báo lại chữ số và dấu = + ( ) sang phông legacymaths OT1/cmr, đè lên thiết lập của mathastext (Umathcode của chữ số 0 trỏ vào họ 13 = cmr10). Template gốc (pdfLaTeX) in các ký tự này bằng Source Sans và MnSymbol, không có CMR nào trong presentation.pdf. Tùy chọn no-math của fontspec trả lại đúng hành vi template; đã thử: pdffonts không còn CMR, chữ số trục pgfplots cũng chuyển sang Source Sans. Đây là một chỗ sửa [VN] tối thiểu, thay cho \PassOptionsToPackage{}{fontspec} đang để trống.

```text
FILE: latex/slides/presentation.sty
CŨ: \PassOptionsToPackage{}{fontspec}\RequirePackage{fontspec}\defaultfontfeatures{Ligatures={NoCommon, TeX}} % [VN] tắt ghép chữ f như bản gốc
MỚI: \PassOptionsToPackage{no-math}{fontspec}\RequirePackage{fontspec}\defaultfontfeatures{Ligatures={NoCommon, TeX}} % [VN] tắt ghép chữ f như bản gốc; no-math để mathastext giữ chữ số và dấu toán như bản gốc
```

### F2. [MAJOR] Slide 2, dòng 43–57 (slides.tex)

Trục thời gian TikZ không cần thiết: thông tin (ba thông tư, ngày VNX công bố, ngày chuyển) đọc được ngay từ một bảng kiểu "Basic table" của template, còn template không có sơ đồ TikZ nào. Hình hiện tại cũng lệch template ở hai điểm đo được: nhãn năm ở ba độ cao khác nhau (y = 63,0; 65,9; 67,4 pt) và nhãn dưới ở bốn độ cao (96,2 đến 99,7 pt). Đề xuất thay bằng bảng 4 dòng và thêm một ý định tính có nguồn v14 [76]: vì mọi mã đổi sàn cùng một ngày do cơ quan quản lý ấn định, có thể so sánh chính các cổ phiếu ấy trước và sau với một nhóm đối chứng (vấn đề tự chọn sàn không xuất hiện). Đã thử: tiêu đề 1 dòng, chân slide ở y ≈ 224 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{figure}
\begin{tikzpicture}[x=0.96cm]
\draw[arr] (0,0) -- (12.6,0) node[right, font=\small]{thời gian};
\foreach \x/\a/\b in {0.4/2021/{TT 57: hạn năm 2023}, 3.2/2023/{TT 69: lùi đến hết 2025}, 6.0/2025/{TT 139: lùi đến 31/12/2026}, 8.8/{30/9/2026}/{VNX công bố lịch}}
  {\draw[thick] (\x,0.12) -- (\x,-0.12); \node[above=4pt, font=\small\sbseries] at (\x,0.1){\a}; \node[below=4pt, font=\footnotesize, text width=2.2cm, align=center] at (\x,-0.1){\b};}
\draw[very thick, RubineRed] (11.3,0.25) -- (11.3,-0.25);
\node[above=4pt, font=\small\sbseries, RubineRed] at (11.3,0.2){28/12/2026};
\node[below=4pt, font=\footnotesize, text width=2.4cm, align=center, RubineRed] at (11.3,-0.2){phiên đầu tại HOSE};
\end{tikzpicture}
\end{figure}
\begin{itemize}
\item \al{299 mã} (tính đến phiên 30/9/2026), chuyển \al{cùng một ngày} theo lịch của VNX
\item Thời điểm chuyển không do từng doanh nghiệp chọn
\item Phiên cuối ở HNX 23/12; tạm ngừng 24--25/12/2026; lộ trình đã \al{lùi hai lần}; UPCoM không thuộc đợt này
\end{itemize}
MỚI: \begin{itemize}
\item \al{299 mã} (tính đến phiên 30/9/2026) chuyển \al{cùng một ngày}; UPCoM không thuộc đợt này
\item Ngày chuyển do cơ quan quản lý ấn định, không do từng doanh nghiệp chọn \so so sánh được chính các cổ phiếu ấy trước và sau, với một nhóm đối chứng
\end{itemize}
\begin{table}
\begin{tabular*}{\textwidth}{@{\extracolsep\fill}ll}
\toprule
Mốc & Nội dung\\
\midrule
2021 & Thông tư 57: hạn chuyển sàn năm 2023\\
2023 & Thông tư 69: \al{lùi} đến hết năm 2025\\
2025 & Thông tư 139: \al{lùi} đến 31/12/2026\\
30/9/2026 & VNX công bố lịch: phiên cuối ở HNX 23/12, phiên đầu ở HOSE 28/12/2026\\
\bottomrule
\end{tabular*}
\end{table}
```

### F3. [MAJOR] Slide 6, dòng 125–137 (slides.tex)

Khung phân tích vẽ bằng 5 hộp TikZ có viền và mũi tên ba kiểu, phải có một chú thích dài để giải nghĩa mũi tên; template không có kiểu hình này và mức tối giản của template là danh sách đánh số. Nội dung hình trùng với bảng giả thuyết ở slide 4. Đề xuất thay bằng chuỗi lập luận định tính theo v14 [111]–[112] (sàn \then chất lượng \then khả năng đầu tư; mắt xích cuối không kiểm định nhân quả) và [71], [75] (thị trường HNX còn vận hành; tiền lệ Bắc Kinh), dùng ký hiệu \then của template. Đây cũng là chỗ thêm phần "vì sao" mà người dùng yêu cầu. Đã thử: mỗi mục tối đa 2 dòng, chân slide y ≈ 212 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{figure}
\begin{tikzpicture}[node distance=5mm and 10mm, every node/.append style={inner sep=4pt}]
\node[box, text width=3.3cm] (a) {\textsb{Trước hợp nhất}\\HNX so với HOSE (\HH{2})\\6/2009--6/2025};
\node[box, text width=3.3cm, right=of a, draw=RubineRed, very thick] (b) {\textsb{Sự kiện 28/12/2026}\\Thanh khoản (\HH{3})\\Khả năng đầu tư (\HH{4})};
\node[box, text width=3.3cm, right=of b] (c) {\textsb{Hàm ý cho Hà Nội}\\Chuyên môn hóa thị trường\\Hạ tầng dữ liệu};
\node[box, text width=3.3cm, below=of b] (d) {\textsb{Nhóm đối chứng}\\Cổ phiếu HOSE đối sánh\\Cổ phiếu UPCoM};
\node[box, text width=3.3cm] (e) at (c |- d) {\textsb{Bằng chứng quốc tế}\\Điểm GFCI (\HH{1})\\Thể chế, thu nhập};
\draw[arr] (a) -- (b); \draw[darr] (b) -- (c);
\draw[arr] (d) -- node[right, font=\footnotesize]{khác biệt kép} (b);
\draw[darr] (e) -- node[right, font=\footnotesize]{bối cảnh} (c);
\end{tikzpicture}
\caption{Mũi tên từ ô Trước hợp nhất: trình tự thời gian. Mũi tên khác biệt kép: ước lượng \HH{3}, \HH{4}. Nét đứt: tổng hợp định tính.}
\end{figure}
MỚI: \begin{enumerate}
\item \textsb{Sàn \then chất lượng thị trường:} quy tắc giao dịch và mức tập trung lệnh của sàn quyết định chi phí giao dịch và tốc độ giá phản ánh thông tin (\HH{2}, \HH{3})
\item \textsb{Chất lượng \then khả năng đầu tư:} giao dịch đắt và kém thanh khoản làm nhà đầu tư đa dạng hóa nhận lợi suất tương đương chắc chắn thấp hơn (\HH{4})
\item \textsb{Thị trường cổ phiếu \then vị thế trung tâm tài chính:} chỉ là liên hệ có điều kiện, không kiểm định nhân quả (\HH{1})
\item \textsb{Hàm ý:} Bắc Kinh lớn mạnh dù không có sàn cổ phiếu tầm quốc gia (Naeem, 2023) \so Hà Nội chọn chuyên môn hóa: trái phiếu, phái sinh, UPCoM, dữ liệu
\end{enumerate}
```

### F4. [MAJOR] Slide 8, dòng 147–162 (slides.tex)

Hình ba giai đoạn (TikZ) chỉ chở ba khoảng thời gian; một bảng ba dòng theo kiểu template nói đủ, lại có chỗ ghi mỗi giai đoạn dùng để làm gì. Hình hiện tại đẩy chân slide xuống y = 242,3 pt, sát mép dưới nhất trong deck. Thay bằng bảng; ý "chuyển tiếp bị loại" chuyển vào bảng kèm lý do (v14 [131], [176]). Đã thử: chân slide y ≈ 214 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{figure}
\begin{tikzpicture}[x=0.62cm, y=0.9cm]
\draw[arr] (0,0) -- (21,0) node[right, font=\small]{năm};
\foreach \y/\l in {0/2009,4/2013,8/2017,12/2021,16/2025,20/2029}{\draw (\y,0.1)--(\y,-0.1) node[below, font=\footnotesize]{\l};}
\draw[thick, fill=LightGray] (0.5,0.45) rectangle (16.5,1.25); \node[font=\small] at (8.5,0.85){Tham chiếu 6/2009--6/2025};
\draw[thick, dashed] (16.5,0.45) rectangle (18,1.25);
\draw[thick, fill=RubineRed!15] (18,0.45) rectangle (20,1.25);
\draw[very thick] (18,-0.15) -- (18,1.6);
\node[anchor=south east, font=\footnotesize, align=right] at (17.2,1.7){chuyển tiếp\\7/2025--12/2026};
\node[anchor=south west, font=\footnotesize, align=left] at (18.8,1.7){sau sự kiện\\1/2027--12/2028};
\end{tikzpicture}
\end{figure}
\begin{itemize}
\item Dữ liệu ngày HNX, UPCoM, HOSE (sở giao dịch, nhà cung cấp thương mại), \al{kể cả mã đã hủy niêm yết}
\item Chuyển tiếp bị loại: từ 1/7/2025 HNX ngừng nhận niêm yết mới, giá có thể phản ứng trước
\item
MỚI: \begin{table}
\begin{tabularx}{\textwidth}{@{}l l L@{}}
\toprule
Giai đoạn & Thời gian & Dùng để\\
\midrule
Tham chiếu & 6/2009--6/2025 & \HH{2}; cửa sổ trước của \HH{3}, \HH{4}\\
Chuyển tiếp & 7/2025--12/2026 & \al{bị loại}: HNX ngừng niêm yết mới, giá có thể phản ứng sớm\\
Sau sự kiện & 1/2027--12/2028 & cửa sổ sau 24 tháng của \HH{3}, \HH{4}\\
\bottomrule
\end{tabularx}
\end{table}
\begin{itemize}
\item Dữ liệu ngày HNX, UPCoM, HOSE (sở giao dịch, nhà cung cấp thương mại), \al{kể cả mã đã hủy niêm yết}
\item
```

### F5. [MAJOR] Slide 10–11, dòng 188–192 (slides.tex)

Hai biểu đồ pgfplots (bước giá/giá, lợi suất trần theo giá) hiện bằng \only<1>/\only<2> trên cùng một khung, vi phạm Hard Rule 1 của skill beamer (không overlay) và tốn hai trang cho một ý. Người nghe chỉ cần biết hai quy tắc đổi thế nào và chỉ báo nào bị méo cơ học (skill liquidity-measures mục 4.1, 4.3); một bảng hai dòng nói đủ, theo kiểu "Basic table with note". Con số 6,14% ở giá 1.140 đồng đã có ở slide sau. Đề xuất bỏ hai hình (hinh/buocgia.tex, hinh/tran.tex không còn được gọi), thay bằng bảng và một ý định tính về hệ quả, nguồn v14 [121]–[124]. Đã thử: 1 trang, chân slide y ≈ 222 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{figure}
\only<1>{\input{hinh/buocgia.tex}}%
\only<2>{\input{hinh/tran.tex}}%
\caption{\only<1>{Bước giá chia cho giá. HNX: 100 đồng mọi mức giá; HOSE: 10, 50 hoặc 100 đồng tùy giá. Nguồn: quy chế giao dịch HNX (2016) và HOSE (2025).}\only<2>{Lợi suất tăng tối đa trong một phiên, sau khi làm tròn giá trần xuống theo bước giá.}}
\end{figure}
MỚI: \begin{table}
\small
\begin{tabularx}{\textwidth}{@{}l l l L@{}}
\toprule
Quy tắc & HNX & HOSE & Chỉ báo bị méo cơ học\\
\midrule
Biên độ & $\pm$10\% & $\pm$7\% & Amihud, Corwin--Schultz: lợi suất ngày lớn bị cắt ở giá trần, giá sàn\\
Bước giá & 100 đồng & 10, 50, 100 đồng & tỷ lệ ngày lợi suất 0, Corwin--Schultz: phản ánh một phần bước giá, nhất là ở mã giá thấp\\
\bottomrule
\end{tabularx}
\caption{HOSE: 10 đồng khi giá dưới 10.000 đồng, 50 đồng đến 49.950 đồng, 100 đồng từ 50.000 đồng. Nguồn: quy chế giao dịch HNX (2016) và HOSE (2025).}
\end{table}
\begin{itemize}
\item Khi chuyển sàn, bước giá giảm mười lần ở mã giá dưới 10.000 đồng, giảm một nửa ở mã 10.000--49.950 đồng
\item Nếu không xử lý, một phần thay đổi đo được đến từ quy tắc, không từ chất lượng giao dịch
\end{itemize}
```

### F7. [MAJOR] Slide 15 (hinh/did.tex dòng 17), dòng 17 (did.tex)

Nhãn "trước sự kiện" (y = 60,5–74,7 pt, x = 151–205) đè lên nhãn "Cổ phiếu chuyển sàn" (y = 67,2–81,4, x = 130–216), chồng 7,4 pt theo chiều dọc (đo bằng pdftotext -bbox). Chuyển nhãn xuống đáy vùng tô xám, nơi không có đường nào (đường cam ở x = −6 có y = 0,598).

```text
FILE: latex/slides/hinh/did.tex
CŨ: \node[black!60, anchor=north, font=\small] at (axis cs:-6,1.48) {trước sự kiện};
MỚI: \node[black!60, anchor=south, font=\small] at (axis cs:-6,0.04) {trước sự kiện};
```

### F8. [MAJOR] Slide 15 (hinh/did.tex dòng 15), dòng 15 (did.tex)

Nhãn "nếu không chuyển sàn" (anchor south tại x = 4) trải từ x ≈ −0,9 đến 8,9 theo trục, nên cắt vạch dọc 1/2027 tại x = 0 (giao tại (234,8; 88,8) pt) và mép trái chạm đường tím liền trước sự kiện. Đặt nhãn bắt đầu sau vạch, cao hơn đường nét đứt: tại x = 0,6 đường nét đứt ở y = 1,045 < 1,07.

```text
FILE: latex/slides/hinh/did.tex
CŨ: \node[Tim, anchor=south, font=\small] at (axis cs:4,1.03) {nếu không chuyển sàn};
MỚI: \node[Tim, anchor=south west, font=\small] at (axis cs:0.6,1.07) {nếu không chuyển sàn};
```

### F9. [MAJOR] Slide 15 (hinh/did.tex dòng 16), dòng 16 (did.tex)

Nhãn "Cổ phiếu HOSE đối sánh" (anchor north west tại y = 0,6) có mép trên cao hơn đường cam ở nửa phải: đường cam y = 0,55 − 0,008x, tại mép phải nhãn (x ≈ −1,0) là 0,558 < 0,6, nên đường cam đi xuyên phần trên của nhãn (y ≈ 127,5–129,4 pt). Hạ nhãn xuống 0,52: khe hở nhỏ nhất ≈ 2,9 pt ở mép phải.

```text
FILE: latex/slides/hinh/did.tex
CŨ: \node[Cam, anchor=north west, font=\small] at (axis cs:-11.5,0.6) {Cổ phiếu HOSE đối sánh};
MỚI: \node[Cam, anchor=north west, font=\small] at (axis cs:-11.5,0.52) {Cổ phiếu HOSE đối sánh};
```

### F12. [MAJOR] Slide 17, dòng 279–287 (slides.tex)

Lưu đồ TikZ 4 hộp cho bootstrap: template không có kiểu hình này; danh sách đánh số của template ("Slide with numbered list") chở đúng bốn bước. Đề xuất thay bằng enumerate và đặt trước nó một câu nêu ý tưởng (so giá trị thật với các chuỗi giả không có sự kiện), nguồn v14 [172]. Đã thử: chân slide y ≈ 225 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{figure}
\begin{tikzpicture}[node distance=3mm, every node/.append style={font=\footnotesize, inner sep=3pt}]
\node[box, text width=5cm] (s1) {Ước lượng AR trên giai đoạn tham chiếu, hiệu chỉnh độ chệch};
\node[box, text width=5cm, below=of s1] (s2) {Tạo chuỗi giả theo mô hình AR, rút phần dư có hoàn lại};
\node[box, text width=5cm, below=of s2] (s3) {Tính thống kê trên mỗi chuỗi giả};
\node[box, text width=5cm, below=of s3, draw=RubineRed, very thick] (s4) {Giá trị p một phía = tỷ lệ chuỗi giả có thống kê nhỏ hơn hoặc bằng giá trị thật};
\draw[arr] (s1)--(s2); \draw[arr] (s2)--(s3); \draw[arr] (s3)--(s4);
\end{tikzpicture}
\end{figure}
MỚI: \textsb{Ý tưởng:} giá trị thật có hiếm không, so với các chuỗi giả không có sự kiện
\begin{enumerate}
\item Ước lượng mô hình AR của $d_t$ trên giai đoạn tham chiếu, hiệu chỉnh độ chệch
\item Tạo chuỗi giả theo mô hình AR, rút phần dư có hoàn lại
\item Tính thống kê trên mỗi chuỗi giả
\item Giá trị p một phía: tỷ lệ chuỗi giả có thống kê nhỏ hơn hoặc bằng giá trị thật
\end{enumerate}
```

### F13. [MAJOR] Slide 18, dòng 293–296 (slides.tex)

Biểu đồ hiệu ứng nhỏ nhất phát hiện được không chứng minh tiêu đề: tiêu đề nói lực kiểm định "ít phụ thuộc vào số mã", nhưng hình chỉ vẽ theo φ và độ dài cửa sổ, không có trục số mã. Ngoài ra nhãn "cửa sổ trước 193 tháng" (x = 258,6–352,4; y = 142,7–156,9 pt) bị đường gióng hồng nét đứt tại φ = 0,6 cắt ngang (giao tại (283,0; 154,5) pt), và chú thích phải đọc 4 dòng số. Ba con số v14 [206] đọc rõ hơn trong một bảng kiểu template; lý do "ít phụ thuộc số mã" cần nói bằng lời (v14 [205], [182]: cú sốc chung theo tháng). Giữ đúng các số trong v14: 0,64σ; 1,24σ; 1,76σ; khoảng 1,3 lần khi cửa sổ trước 24 tháng; 0,25 log ≈ 22% là minh họa. Đã thử: chân slide y ≈ 224 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \begin{figure}
\input{hinh/mde.tex}
\caption{Hiệu ứng nhỏ nhất phát hiện được của $\delta$: lực 80\%, mức một phía 0,05/3; $\sigma_d = 0{,}2$ minh họa; chuyển tiếp 18 tháng bị loại, sau 24 tháng. Bằng $0{,}64\sigma_d$, $1{,}24\sigma_d$, $1{,}76\sigma_d$ khi $\phi = 0$; 0,6; 0,8.}
\end{figure}
MỚI: \begin{itemize}
\item Mọi mã chịu chung một cú sốc mỗi tháng \so thêm mã không làm nhiễu chung nhỏ đi, thêm tháng thì có
\item Chuỗi chênh lệch càng tự tương quan, mỗi tháng mới càng ít thông tin \so hiệu ứng nhỏ nhất phát hiện được tăng
\end{itemize}
\begin{table}
\begin{tabular*}{\textwidth}{@{\extracolsep\fill}lccc}
\toprule
Tự tương quan $\phi$ của $d_t$ & 0 & 0,6 & 0,8\\
\midrule
Hiệu ứng nhỏ nhất phát hiện được & $0{,}64\sigma_d$ & $1{,}24\sigma_d$ & $1{,}76\sigma_d$\\
Với $\sigma_d = 0{,}2$ (log Amihud) & 0,13 & \al{0,25} & 0,35\\
\bottomrule
\end{tabular*}
\caption{Lực 80\%, mức một phía 0,05/3; cửa sổ trước 193 tháng, 18 tháng chuyển tiếp bị loại, sau 24 tháng. $\sigma_d = 0{,}2$ là giả định minh họa; 0,25 log tương ứng Amihud giảm khoảng 22\%. Nếu cửa sổ trước chỉ còn 24 tháng, các mức trên tăng khoảng 1,3 lần.}
\end{table}
```

### F6. [MINOR] Slide 14, dòng 223 (slides.tex)

Phương trình có $\alpha_i$, $\tau_t$ nhưng slide không nói hai số hạng này làm gì; đây là trực giác cốt lõi của khác biệt kép (econ-write: định nghĩa mọi ký hiệu ngay sau phương trình; mhe-identification: nói rõ thiết kế loại bỏ thành phần nào). Thêm một ý, nguồn v14 [169]. Đã thử: chân slide y ≈ 236 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \item $A_{it}$: log Amihud; $D_i = 1$: mã chuyển sàn; $\Post_t = 1$ từ 1/2027; \HH{3}: $\delta < 0$
MỚI: \item $A_{it}$: log Amihud; $D_i = 1$: mã chuyển sàn; $\Post_t = 1$ từ 1/2027; \HH{3}: $\delta < 0$
\item $\alpha_i$ hấp thụ khác biệt cố định giữa các mã, $\tau_t$ hấp thụ cú sốc chung của cả thị trường từng tháng
```

### F10. [MINOR] Slide 15 (hinh/kieu.tex dòng 10–12), dòng 10–12 (kieu.tex)

Kiểu trục lệch figures.pdf: (a) `axis lines=left` vẽ đầu mũi tên ở cuối hai trục, figures.pdf không có mũi tên; (b) trục và vạch chia màu black!70, figures.pdf màu đen đặc; (c) `grid=major` vẽ cả lưới dọc, figures.pdf trang 1–3, 5 chỉ có lưới ngang, màu đen độ mờ 0,149 (≈ black!15). Đo bằng cách giải nén luồng nội dung: figures.pdf có các nét S màu 0 alpha 0,149 chỉ nằm ngang.

```text
FILE: latex/slides/hinh/kieu.tex
CŨ:   axis lines=left, axis line style={black!70, thin}, tick style={black!70},
  tick align=outside, major tick length=2pt,
  grid=major, grid style={black!12, thin},
MỚI:   axis lines*=left, axis line style={black, thin}, tick style={black},
  tick align=outside, major tick length=2pt,
  ymajorgrids, grid style={black!15, thin},
```

### F11. [MINOR] Slide 15 (hinh/kieu.tex dòng 13), dòng 13 (kieu.tex)

Chữ số và nhãn trục trong figures.pdf màu đen (sc 0), deck dùng black!85. Đổi về đen cho khớp.

```text
FILE: latex/slides/hinh/kieu.tex
CŨ: ticklabel style={font=\small, color=black!85}, label style={font=\small, color=black!85},
MỚI: ticklabel style={font=\small, color=black}, label style={font=\small, color=black},
```

### F14. [MINOR] Slide 21, dòng 330 (slides.tex)

Dòng định nghĩa $U$ chỉ gọi tên "lợi suất tương đương chắc chắn" mà không nói nó nghĩa là gì, và không nói dấu của $\bar{G}$ đọc thế nào (ý này hiện chỉ có ở phụ lục). Thêm trực giác theo v14 [151], [159].

```text
FILE: latex/slides/slides.tex
CŨ: {\small $U = \mu - \rho\sigma^2/2$: lợi suất tương đương chắc chắn sau chi phí ($\rho = 5$); rổ CS: tối đa 30 mã chuyển sàn; rổ H: mã HOSE ghép cặp}
MỚI: {\small $U = \mu - \rho\sigma^2/2$: lợi suất chắc chắn mà nhà đầu tư ngại rủi ro coi là ngang giá với danh mục, sau chi phí ($\rho = 5$); rổ CS: tối đa 30 mã chuyển sàn; rổ H: mã HOSE ghép cặp; $\bar{G} > 0$: rổ CS thiệt hơn rổ H}
```

### F15. [MINOR] Slide — (preamble, dòng 26–28), dòng 26–29 (slides.tex)

Sau F2, F3, F4, F12 không còn hình nào dùng kiểu box, arr, darr; bỏ để preamble tối giản như template.

```text
FILE: latex/slides/slides.tex
CŨ: \tikzset{box/.style={draw=black!70, rounded corners=2pt, align=center, font=\small, inner sep=5pt},
         arr/.style={-{Stealth[length=2.2mm]}, thick, black!70},
         darr/.style={-{Stealth[length=2.2mm]}, thick, dashed, black!70}}

MỚI: 
```

### F16. [MINOR] Slide 24, dòng 387 (slides.tex)

Bảng rủi ro có 4 dòng, trong khi v14 [211]–[213] nêu năm phương án dự phòng; thiếu phương án khi dữ liệu sau sự kiện ngắn hơn 24 tháng hoặc rổ CS ít hơn 30 mã. Thêm một dòng (consistency-checker, mục 5). Đã thử: chân slide y ≈ 211 pt.

```text
FILE: latex/slides/slides.tex
CŨ: Không dùng được GFCI & \HH{1} ở dạng mô tả\\
MỚI: Không dùng được GFCI & \HH{1} ở dạng mô tả\\
Dữ liệu sau ngắn, rổ CS ít mã & Dùng mọi tháng có sẵn; rổ 20 mã\\
```

### F17. [MINOR] Slide 26, dòng 425 (slides.tex)

Tiêu đề kết luận nêu "phát hiện được tác động từ khoảng 22%" như một kết quả, trong khi con số dựa trên giả định minh họa σ = 0,2, φ = 0,6 (v14 [207]); thân slide có ghi "với giả định minh họa" nhưng tiêu đề thì không (credible-claims: không nâng "minh họa" thành "đã kiểm chứng"; GHI-CHU mục 1). Đã thử: 1 dòng, x tối đa ≈ 400 pt.

```text
FILE: latex/slides/slides.tex
CŨ: \frametitle{Một sự kiện đo được; phát hiện được tác động từ khoảng 22\%}
MỚI: \frametitle{Một sự kiện đo được; ngưỡng phát hiện khoảng 22\% là minh họa}
```

## Ghi chú không kèm cặp sửa

1. **`\bar` vẫn lấy dấu gạch từ CMR10** (slide 17, 21, phụ lục H₄). Đây là dấu gạch ngang trên chữ, hình dạng như nhau ở mọi phông, nên không thấy khác trên slide. Muốn sạch hẳn thì thêm tùy chọn `mathaccents` cho mathastext, nhưng template gốc không dùng tùy chọn này nên tôi không đề xuất.
2. **Tên đề tài xuống 3 dòng** ở cỡ \huge chữ hoa nhỏ (template mẫu chỉ 1 dòng). Tên đề tài phải giữ nguyên nên chấp nhận; trang tiêu đề kết thúc ở y = 220 pt, không tràn.
3. **Biểu đồ khác biệt kép còn lệch nhỏ so với figures.pdf**: nhãn trên đường cỡ \small (10 pt) so với 8,75 pt; đường 1,25 pt so với 1,37 pt; vùng tô black!6 đặc so với đen độ mờ 0,149; có nhãn trục hoành ("Tháng") trong khi figures.pdf không có. Các lệch này không ảnh hưởng đọc hiểu; nếu main muốn khớp tuyệt đối thì đổi `font=\small` của 5 nhãn thành `\footnotesize` và `line width=1.25pt` thành `1.4pt` trong `kieu.tex`, rồi kiểm lại khe hở nhãn.
4. Slide 6 mới: dòng 2 của mục 4 bắt đầu bằng "Nội" (tên "Hà Nội" bị ngắt dòng). Nếu muốn, thêm `~` giữa "Hà" và "Nội" trong cặp F3.
5. Cảnh báo hyperref `\translate` từ `\appendix` và bảng `tabularx` cỡ \small: đã được chấp nhận, không đề xuất lại.

## Điểm rubric 100 (skill beamer, mục 5c)

| Mục trừ (bản hiện tại) | Áp vào | Điểm |
|---|---|---|
| Nhãn TikZ đè nhau hoặc đè đường (Major, −5 mỗi hình) | slide 15 (F7–F9), slide 18 (F13) | −10 |
| Phông lạ trong công thức, tính như không nhất quán ký hiệu (Major) | F1 | −3 |
| Overlay trái Hard Rule 1 (Major, ánh xạ) | slide 10–11 (F5) | −3 |
| Tiêu đề không khớp nội dung hình (Major, ánh xạ không nhất quán) | slide 18 (F13) | −3 |
| Giảm cỡ chữ \footnotesize cho nội dung (Minor, −1 mỗi slide) | nhãn TikZ slide 2, 6, 8, 17 | −4 |
| **Tổng hiện tại** | | **77/100** |

Sau khi áp đủ 17 cặp (đã biên dịch kiểm chứng): còn −1 cho đoạn chữ \small ở slide 21 (ngoài bảng); dấu `\bar` CMR không thấy được nên không trừ. **Ước tính sau sửa: 99/100.**

## Bảng đếm

| Mức | Số phát hiện | Mã |
|---|---|---|
| CRITICAL | 0 | |
| MAJOR | 10 | F1, F2, F3, F4, F5, F7, F8, F9, F12, F13 |
| MINOR | 7 | F6, F10, F11, F14, F15, F16, F17 |
| **Tổng** | **17** | |

## Mức khớp template theo từng mặt

| Mặt | Template | Hiện tại | Sau sửa |
|---|---|---|---|
| Phông chữ thường, tiêu đề, chữ hoa nhỏ | Source Sans Pro, Semibold, \scshape | Khớp | Khớp |
| Phông trong công thức | Source Sans (chữ, số), MnSymbol (= + ( )), Euler (Hy Lạp) | Lệch: chữ số và dấu là CMR (≈ 85%) | Khớp (≈ 99%, chỉ còn dấu `\bar`) |
| Cỡ chữ (20,66 / 14,35 / 10,91 / 8,97 pt) | | Khớp | Khớp |
| Màu chữ (0,15; caption 0,675; nhấn RubineRed) | | Khớp | Khớp |
| Lề, giãn dòng, khoảng cách | sty gốc | Khớp | Khớp |
| Đặt hình và chú thích (figure/table + \caption xám) | | Khớp | Khớp |
| Khung định lý nền xám | assumption, remark | Khớp (2 khung, mỗi slide ≤ 1) | Khớp |
| `\heading`, `\lastslide`, phụ lục sau `\lastslide` | | Khớp | Khớp |
| Overlay | Template có dùng `<n>` cho hình | Dùng `\only` (skill cấm) | Không dùng |
| Mức tối giản (không sơ đồ TikZ) | Chỉ chữ, bảng, biểu đồ | Lệch: 5 sơ đồ/hình phụ (≈ 70%) | Khớp (1 biểu đồ cần thiết) |
| Kiểu biểu đồ (Dark2, nhãn trên đường, không chú giải, trục không mũi tên, lưới ngang) | figures.pdf | Lệch: mũi tên trục, lưới hai chiều, màu trục xám, nhãn chồng (≈ 75%) | Gần khớp (≈ 95%, xem Ghi chú 3) |
| **Tổng thể** | | **≈ 85%** | **≈ 98%** |
