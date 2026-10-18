# Rà soát vòng 2 (B): nội dung bộ slide bảo vệ đề cương

Đối tượng: `latex/slides/slides.tex` (588 dòng; PDF hiện tại 37 trang, đọc bằng `pdftotext -layout` và `-bbox-layout`). Nguồn đối chiếu: `outputs/round-14/v14-text-round-14.txt` (trích theo `[n]`), `latex/ban-dai/chapters/*.tex`, `ban-giao-slide/GHI-CHU.md`, văn bản trong `ban-giao-slide/2-tai-lieu-nguon/`, template gốc `pmichaillat/latex-presentation` (bản sao chỉ đọc trong thư mục tạm). Ngày rà: 18/10/2026. Không sửa tệp nào trong repo ngoài báo cáo này; không render ảnh; không gửi câu chữ đề cương ra ngoài.

Quy ước: "Slide n" là số trang trong PDF hiện tại; "dòng" là dòng trong `slides.tex`. Mỗi chuỗi CŨ đã kiểm bằng script: xuất hiện đúng 1 lần trong tệp đích. Toàn bộ cặp CŨ/MỚI (trừ m13) đã áp cùng lúc lên một bản sao trong thư mục tạm và biên dịch `xelatex` hai lượt: 0 lỗi, 0 Overfull, 38 trang; mọi tiêu đề nằm trên 1 dòng (đo bằng `pdftotext -bbox-layout`: đúng một dòng chữ ở y < 35 pt mỗi trang); không dòng nào thấp hơn y = 245 pt (trang cao 255 pt). Cặp m13 (chỉ dùng nếu không nhận B1) được thử riêng trên một bản sao khác: 0 lỗi, 0 Overfull.

## Skill đã nạp và dùng vào việc gì

Đã đọc SKILL.md của từng skill. Tệp references đọc chọn lọc theo phần liên quan; các phần về tra cứu mạng (citation-management), kiểm định nhóm và Bayes (statistical-analysis), viết bài báo (econ-write) chỉ lướt. Không chạy script nào của skill.

| Skill | Dùng vào việc |
|---|---|
| beamer | Hard Rules (cấm overlay, ≤ 2 khung, ≤ 7 ý, ý ≤ 2 dòng), pedagogy (động cơ trước công thức), devils-advocate, validate, rubric 100 |
| beamer-check | Đọc log: 0 lỗi, 0 Overfull ở bản hiện tại và bản đã áp cặp |
| beamer-presentation | Tiêu đề nêu kết luận, phân bổ thời gian, phần dự phòng |
| slide-design-principles | Một ý mỗi slide; hình chỉ khi cần (B1, m8) |
| latex-econ-model | Ký hiệu (1)–(7): chỉ số dưới liền, tham số Hy Lạp, tên biến chữ đứng; khớp |
| mhe-identification (critic) | Nguồn biến thiên, xu hướng song song, kiểm soát xấu, suy luận khi chỉ có một sự kiện (B7, m5, bảng câu hỏi) |
| aer-identification | Chuẩn 2×2 một mốc (TWFE hợp lệ vì mọi mã chuyển cùng ngày, đối chứng HOSE không bị xử lý), pre-trend kèm Rambachan–Roth, tách cơ chế khỏi nhận dạng (B1) |
| mostly-harmless-guide, panel-data-guide | Đọc lại (5) và (7) với hiệu ứng cố định hai chiều; β ở (7) chỉ xác định từ biến thiên trong quốc gia (slide 22 đã nêu) |
| review-methodology | Soát ngôn ngữ nhân quả (B5, m9) |
| statistical-power | Tính lại MDE bằng `hinh/taodulieu.py`: 0,64σ; 1,24σ; 1,76σ; tỷ số 24/193 tháng = 1,33; z(1 − 0,05/3) = 2,128; điểm vẽ cứng trong `mde.tex` (m8) |
| statistical-analysis | Holm với giá trị p một phía (B4); cách gọi "chưa đủ cơ sở kết luận" (m9) |
| liquidity-measures | Amihud với ngưỡng chung và loại ngày liền sau; bẫy biên độ, bước giá, ngày lợi suất 0, Corwin–Schultz (B1, m4, m13) |
| review-pap | Đăng ký trước: khai dữ liệu đã thấy, phân tích giữa kỳ, MDE có ý nghĩa chính sách không (m10, m11, bảng câu hỏi) |
| fact-checker, consistency-checker | Đối chiếu từng số, ngày, trích dẫn với v14 (bảng đối chiếu) |
| credible-claims | Không nâng ngôn ngữ quá bằng chứng: số minh họa không làm tiêu đề (B5); không dùng số của hộp ví dụ (B4) |
| scientific-critical-thinking | Lập luận thay thế cho từng giả thuyết; các mối đe dọa trong bảng câu hỏi |
| vn-legal-verify | Đối chiếu mốc pháp lý ở slide 2, 37 với v14 [73], [122], [131] và văn bản trong `2-tai-lieu-nguon` |
| citation-management | Kiểm APA cục bộ: 9 mục "Tài liệu chính" khớp v14 [290]–[351]; "&" trong ngoặc, "và" ngoài ngoặc |
| econ-write | Mạch bài nói, bottom line, lời văn phần định tính |
| vina-me, vietnamese-human-writing, sciwrite | Lời văn mọi chuỗi MỚI; bỏ gạch vừa dùng làm dấu trừ (m3) |
| Shapiro, How to Give an Applied Micro Talk | Đọc toàn văn; đối chiếu ở mục riêng |

## Đánh giá chung

Các sửa của vòng 1 đã vào đủ: trục thời gian đúng ngày, giả định nhận dạng viết tường minh, có slide điểm yếu, có MDE, danh mục tài liệu khớp v14. Mọi số, ngày và văn bản pháp lý trên slide khớp v14 (bảng đối chiếu). Không còn lỗi CRITICAL.

Phần còn lại chủ yếu thuộc ba yêu cầu mới của người dùng. Phần định tính còn mỏng: chưa slide nào nói vì sao đổi sàn có thể làm thanh khoản đổi, hay vì sao chất lượng thị trường quan trọng với vị thế Hà Nội. Hai hình bước giá và lợi suất trần không cần thiết, lại dùng overlay và một giả định làm tròn giá của HNX không có nguồn. Bảng Holm dùng đúng các giá trị p của hộp ví dụ trong bản dài, loại số GHI-CHU.md cấm đưa lên slide. Ngoài ra deck thiếu slide năng lực thí sinh, và tiêu đề kết luận đưa con số 22% minh họa lên làm thông điệp.

## Phát hiện

### B1. [MAJOR] Slide 10–11, dòng 187–192. Hai hình không cần thiết, dùng overlay, và đường HNX dựa trên giả định không có nguồn

Thứ nhất, người dùng yêu cầu chỉ vẽ hình khi thật cần, mà cả hai thông điệp của hình đều nói được bằng chữ có nguồn: bước giá giảm mười lần dưới 10.000 đồng và giảm một nửa đến 49.950 đồng [122]; giá 1.140 đồng chỉ tăng được 6,14% đã có ở slide 12 [125]. Thứ hai, `\only<1>`, `\only<2>` vi phạm Hard Rule 1 của skill beamer. Thứ ba, đường HNX trong `hinh/tran.tex` làm tròn giá trần xuống theo bước 100 đồng; v14 [125] chỉ nêu quy tắc làm tròn của HOSE, còn bản trích QĐ 529/QĐ-SGDHN (Điều 25) ghi "Quy chế không quy định chiều làm tròn giá trần, giá sàn".

Đổi slide thành bảng cơ chế, đáp đúng yêu cầu định tính: vì sao từng thay đổi có thể làm thanh khoản đổi và mã nào chịu mạnh nhất. Nguồn: [111] (quy tắc giao dịch, mức tập trung lệnh), [122]–[124], [177] (ba mức chịu cú sốc), [183] (kênh sự chú ý gắn với nơi đặt sàn), [77] và [100] (bằng chứng trái chiều theo quy mô). Bảng theo đúng kiểu template (table kèm \caption xám). Ý "δ đo tác động gộp" vẫn ở chú thích slide 15, nên bảng không ngụ ý tách riêng từng kênh. Sau khi nhận B1, `hinh/buocgia.tex`, `hinh/tran.tex` và các tệp `.dat` của chúng không còn được dùng.

```text
CŨ: \frametitle{Thách thức: biên độ và bước giá đổi cùng lúc với sàn}
\begin{figure}
\only<1>{\input{hinh/buocgia.tex}}%
\only<2>{\input{hinh/tran.tex}}%
\caption{\only<1>{Bước giá chia cho giá. HNX: 100 đồng mọi mức giá; HOSE: 10, 50 hoặc 100 đồng tùy giá. Nguồn: quy chế giao dịch HNX (2016) và HOSE (2025).}\only<2>{Lợi suất tăng tối đa trong một phiên, sau khi làm tròn giá trần xuống theo bước giá.}}
\end{figure}
MỚI: \frametitle{Thách thức: đổi sàn kéo theo bốn thay đổi cùng lúc}
\begin{table}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.25\textwidth} L L@{}}
\toprule
Thay đổi & Vì sao thanh khoản có thể đổi & Mã chịu mạnh nhất\\
\midrule
Bước giá: 100 đồng $\rightarrow$ 10, 50 hoặc 100 đồng & Chi phí giao dịch đổi; tỷ lệ ngày lợi suất 0 và Corwin--Schultz phản ánh một phần bước giá & Mã giá dưới 10.000 đồng: bước giá giảm mười lần\\
Biên độ: $\pm$10\% $\rightarrow$ $\pm$7\% & Lợi suất bị cắt ở ngày chạm biên độ \so Amihud có thể giảm cơ học & Mã hay tăng giảm 7--10\%\\
Vào VN-Index và chỉ số HOSE & Áp lực cầu lớn hơn & Mã vốn hóa lớn so với giá trị giao dịch\\
Nơi đặt sàn & Sự chú ý và thông tin gắn với nơi đặt sàn & Nếu kênh này có thật: mã có trụ sở Hà Nội được lợi ít hơn\\
\bottomrule
\end{tabularx}
\caption{Quy tắc giao dịch và mức tập trung lệnh của sàn ảnh hưởng chi phí giao dịch và tốc độ giá phản ánh thông tin (Amihud, 2002; Huang \& Stoll, 1996). Bằng chứng quốc tế trái chiều theo quy mô doanh nghiệp (Hisada, 2018; Nielsson, 2009).}
\end{table}
```

### B2. [MAJOR] Sau slide 3, dòng 88–89. Chưa có slide nói vì sao chất lượng thị trường quan trọng với vị thế tài chính của Hà Nội

Slide 3 nêu bài toán 19 và bảng GFCI nhưng chưa nói cơ chế: vì sao mất sàn cổ phiếu niêm yết lại đặt ra câu hỏi chuyên môn hóa. v14 [75] có sẵn lập luận (tích tụ, phân vai, Bắc Kinh, Luxembourg), [71] nêu các thị trường HNX còn vận hành. Bản dài (ch04-1-lydo) có câu chốt: đề tài không giả định Hà Nội đi hướng nào, đề tài đo những gì cần đo để lựa chọn có căn cứ; câu này hợp với khung `remark` như slide 22 đang dùng. Đây là phần Motivation của Shapiro: vì sao hội đồng nên quan tâm. Gehrig, Kindleberger, Lai, Yao đều có trong danh mục v14 và được dòng "Các nguồn khác: xem danh mục" bao.

```text
CŨ: \begin{frame}
\frametitle{Bốn giả thuyết; trọng tâm là tác động của việc chuyển sàn}
MỚI: \begin{frame}
\frametitle{Sau hợp nhất, Hà Nội cần chọn thị trường để chuyên môn hóa}
\begin{itemize}
\item Hoạt động tài chính dồn về nơi có quy mô giao dịch và thông tin (Gehrig, 2000; Kindleberger, 1974)
\item Các trung tâm trong một nước phân vai (Lai, 2012); Bắc Kinh là trung tâm tài chính lớn dù phần lớn thời gian không có sở giao dịch tầm quốc gia (Naeem, 2023)
\item Trung tâm nhỏ vẫn cạnh tranh được nếu chọn đúng mảng: Luxembourg với ngành quỹ (Yao, 2012)
\item Sau hợp nhất, HNX còn vận hành trái phiếu, phái sinh và UPCoM
\end{itemize}
\begin{remark}[Vai trò của đề tài]
Đề tài không chọn hướng thay cho Hà Nội. Đề tài đo chất lượng thị trường để việc chọn mảng chuyên môn hóa có căn cứ.
\end{remark}
\end{frame}

\begin{frame}
\frametitle{Bốn giả thuyết; trọng tâm là tác động của việc chuyển sàn}
```

### B3. [MAJOR] Trước phần kết, dòng 423. Thiếu slide năng lực và sự chuẩn bị của thí sinh

GHI-CHU.md mục 2.12 đưa năng lực thí sinh vào dàn ý; v14 mục 8 [249]–[262] dành riêng cho việc này, và hội đồng xét tuyển NCS thường hỏi thí sinh đã có gì để làm được đề tài. Hai bản thảo số 4 và số 6 dùng đúng công cụ của H₃ [262]. Nội dung chỉ lấy từ [249]–[262]; không nêu tên tạp chí, mã bài.

```text
CŨ: %=================================================================== KẾT
MỚI: \begin{frame}
\frametitle{Chuẩn bị: các công trình đã có dùng công cụ của đề tài}
\begin{table}
\small
\begin{tabularx}{\textwidth}{@{}L L@{}}
\toprule
Công trình & Kinh nghiệm dùng cho đề tài\\
\midrule
Bản thảo về điểm gãy cấu trúc của thanh khoản & Amihud và Bai--Perron: chọn cửa sổ trước cho \HH{3}\\
Bản thảo về thanh khoản quanh đợt nâng hạng FTSE Russell & Nghiên cứu sự kiện trên thanh khoản, công cụ trực tiếp của \HH{3}\\
Nguyễn và Nguyễn (2026a) & Nền của mô hình \MM{5}\\
Bài về Black--Litterman ngược trên cổ phiếu ngân hàng & So sánh nhiều mô hình danh mục trên cùng dữ liệu\\
\bottomrule
\end{tabularx}
\caption{Thí sinh có 4 công trình đã công bố hoặc được chấp nhận đăng và 8 bản thảo đang phản biện hoặc xét duyệt; trạng thái tính đến 30/9/2026, một bài cập nhật đến 9/10/2026.}
\end{table}
\end{frame}

%=================================================================== KẾT
```

### B4. [MAJOR] Slide 36, dòng 554–563. Bảng Holm dùng giá trị p của hộp ví dụ trong bản dài

Các số 0,004; 0,020; 0,030 lấy từ khung `vidu` ở `latex/ban-dai/chapters/ch04-3a-khung.tex` dòng 79. GHI-CHU.md và CLAUDE.md không cho đưa số của hộp ví dụ lên slide; ba dòng "đạt" cạnh H₁–H₃ dễ bị đọc như kết quả dù có chữ "minh họa". Thay bằng thứ tự ký hiệu và nêu loại giá trị p một phía theo v14 [208].

```text
CŨ: \begin{tabular}{@{}lccl@{}}
\toprule
 & p & Ngưỡng & Kết quả\\
\midrule
\HH{2} & 0,004 & 0,0167 & đạt\\
\HH{3} & 0,020 & 0,025 & đạt\\
\HH{1} & 0,030 & 0,050 & đạt\\
\bottomrule
\end{tabular}
\caption{Giá trị p minh họa.}
MỚI: \begin{tabular}{@{}lll@{}}
\toprule
Thứ tự & Ngưỡng & Dừng: số ủng hộ\\
\midrule
$p_{(1)}$ & 0,05/3 & 0\\
$p_{(2)}$ & 0,05/2 & 1\\
$p_{(3)}$ & 0,05 & 2\\
\bottomrule
\end{tabular}
\caption{Giá trị p một phía: phân cụm theo quốc gia (\HH{1}), bootstrap khối dừng (\HH{2}), bootstrap tự hồi quy (\HH{3}).}
```

### B5. [MAJOR] Slide 26, dòng 425. Tiêu đề kết luận biến con số minh họa thành thông điệp

v14 [207] ghi rõ σ = 0,2 và φ = 0,6 là "giả định minh họa". Tiêu đề là thứ khán giả nhớ nhất (bottom line của Shapiro), nên phải mang nhãn minh họa (credible-claims: "illustrated ≠ validated"). Ý 3 trong thân slide đã đúng; chỉ sửa tiêu đề.

```text
CŨ: \frametitle{Một sự kiện đo được; phát hiện được tác động từ khoảng 22\%}
MỚI: \frametitle{Một sự kiện đo được; ngưỡng phát hiện minh họa khoảng 22\%}
```

### B6. [MAJOR] Slide 26, dòng 430. Thiếu hàm ý chính sách; ý 4 gộp báo cáo định hướng vào nhóm "có được dù kết quả ra sao"

v14 [86] chỉ xếp hai chỉ số và tệp đăng ký trước vào nhóm này. Cũng ở [86], chỉ số chất lượng là một cấu phần của "Hệ thống dữ liệu tài chính đô thị"; báo cáo định hướng dành cho các thị trường HNX tiếp tục vận hành [93], [198]. Tách thành hai ý để bài kết bằng hàm ý cho Hà Nội.

```text
CŨ: \item \textsb{Sản phẩm có được dù kết quả ra sao:} hai chỉ số và tệp đăng ký trước, kèm báo cáo định hướng cho Hà Nội
MỚI: \item \textsb{Sản phẩm có được dù kết quả ra sao:} hai chỉ số và tệp đăng ký trước
\item \textsb{Hàm ý cho Hà Nội:} chỉ số chất lượng là một cấu phần của hệ thống dữ liệu tài chính đô thị; định hướng chuyên môn hóa cho các thị trường HNX tiếp tục vận hành
```

### B7. [MAJOR] Slide 14, dòng 223. Phương trình khác biệt kép chưa có lời giải thích trực giác

Shapiro ("lay out explicit economic assumptions that justify your econometric assumptions") và mhe-identification đều đòi nói rõ thiết kế loại bỏ được gì. Bản dài (ch04-3c-kiemdinh, khung "Vì sao dùng khác biệt kép") có câu trả lời: so trước với sau thì lẫn thay đổi chung của thị trường; so với HOSE sau sự kiện thì lẫn khác biệt sẵn có; αᵢ và τₜ trừ cả hai. Thêm một ý, slide còn 3 ý và vẫn vừa trang.

```text
CŨ: \item $A_{it}$: log Amihud; $D_i = 1$: mã chuyển sàn; $\Post_t = 1$ từ 1/2027; \HH{3}: $\delta < 0$
MỚI: \item $A_{it}$: log Amihud; $D_i = 1$: mã chuyển sàn; $\Post_t = 1$ từ 1/2027; \HH{3}: $\delta < 0$
\item $\alpha_i$ loại khác biệt sẵn có giữa hai nhóm; $\tau_t$ loại thay đổi chung của thị trường (lãi suất, dòng vốn ngoại, nâng hạng)
```

### m1. [MINOR] Slide 2, dòng 55. Chưa nói vì sao "không do doanh nghiệp chọn" lại quan trọng

Bản dài (ch04-1-lydo, mục "Vì sao đây là một cơ hội đo hiếm có"): mã tự chuyển sang sàn lớn thường là doanh nghiệp đang tăng trưởng. Thêm vế so sánh này, không khẳng định thêm về tính ngoại sinh.

```text
CŨ: \item Thời điểm chuyển không do từng doanh nghiệp chọn
MỚI: \item Thời điểm chuyển không do từng doanh nghiệp chọn, khác trường hợp mã tự chuyển sàn khi đang tăng trưởng
```

### m2. [MINOR] Slide 3, dòng 70. "Chưa có nghiên cứu" thiếu phạm vi tìm kiếm

v14 [85] và [108] luôn kèm "trong phạm vi tìm kiếm". Slide 5 đã có; slide 3 chưa.

```text
CŨ: \item Chưa có nghiên cứu so sánh chất lượng thị trường HNX với HOSE
MỚI: \item Trong phạm vi tìm kiếm, chưa có nghiên cứu so sánh chất lượng thị trường HNX với HOSE
```

### m3. [MINOR] Slide 9, dòng 182. Gạch vừa dùng làm dấu trừ

"HOSE -- HNX" in ra gạch vừa, dễ đọc thành một khoảng. v14 [141] viết "chênh lệch chỉ số theo tháng giữa HOSE và sàn niêm yết HNX".

```text
CŨ: chênh lệch HOSE -- HNX theo tháng
MỚI: chênh lệch HOSE trừ HNX theo tháng
```

### m4. [MINOR] Slide 12, dòng 198. Ý đầu lặp slide trước và thiếu lý do không chỉ bỏ ngày chạm biên độ

Sau B1, cơ chế "Amihud có thể giảm cơ học" đã nằm ở slide trước. Hội đồng hay hỏi "sao không bỏ ngày chạm trần là xong"; v14 [124] trả lời đúng câu này.

```text
CŨ: \item Biên độ hẹp \so lợi suất bị cắt \so Amihud \al{có thể giảm cơ học}
MỚI: \item Chỉ bỏ ngày chạm biên độ chưa đủ: sau chuyển sàn, mọi ngày lẽ ra tăng giảm 7--10\% đều thành ngày chạm biên độ
```

### m5. [MINOR] Slide 14, dòng 217. Giả định nói chênh lệch "không đổi", đúng ra là không đổi về bình quân

Với sai số εᵢₜ, chênh lệch từng tháng vẫn dao động; điều được giả định là kỳ vọng của nó.

```text
CŨ: Nếu không chuyển sàn, chênh lệch log Amihud giữa hai nhóm không đổi theo thời gian:
MỚI: Nếu không chuyển sàn, chênh lệch log Amihud bình quân giữa hai nhóm không đổi theo thời gian:
```

### m6. [MINOR] Slide 15, dòng 232. Hình khác biệt kép vẽ giai đoạn trước sát ngày sự kiện

`hinh/did.tex` vẽ đường trước nối liền tới 1/2027, trong khi thiết kế bỏ 18 tháng chuyển tiếp [131], [170]. Nên giữ hình vì nó cho hội đồng ngoài chuyên ngành thấy ngay δ là gì; chỉ cần ghi rõ ở chú thích.

```text
CŨ: \caption{Hình minh họa thiết kế, không phải dữ liệu. $\delta$ đo tác động gộp
MỚI: \caption{Hình minh họa thiết kế, không phải dữ liệu; lược bỏ 18 tháng chuyển tiếp trước 1/2027. $\delta$ đo tác động gộp
```

### m7. [MINOR] Slide 16, dòng 255. Cách xử lý cú sốc VN-Index chưa đúng v14

v14 [193]: ngày vào chỉ số thực tế của từng mã được ghi lại và đưa vào ước lượng; đo mức chịu cú sốc chỉ số [178] là phần thứ hai.

```text
CŨ: VN-Index nhận mã mới & Đo mức chịu cú sốc chỉ số\\
MỚI: VN-Index nhận mã chuyển sàn & Ghi ngày vào chỉ số từng mã; đo mức chịu cú sốc\\
```

### m8. [MINOR] Slide 18, dòng 293–296. Hình MDE không cần thiết; tiêu đề nói điều hình không cho thấy

Hình vẽ MDE theo φ, còn tiêu đề nói về số tháng và số mã; hình không cho thấy vế "ít vào số mã". Ba điểm trong `hinh/mde.tex` ghi tọa độ cứng (rubric beamer trừ 8 điểm). Số đã tính lại khớp v14 [206]: 0,129; 0,248; 0,352 khi σ = 0,2; tỷ số 24/193 tháng là 1,33. Thay bằng bảng ba giá trị và lời giải thích của bản dài (ch04-3d-tincay) về vì sao thêm mã ít tác dụng. Nếu buổi nói vượt 30 phút, có thể chuyển hẳn slide này vào phụ lục vì con số 22% đã có ở slide 4 (giả thuyết) và slide kết.

```text
CŨ: \begin{figure}
\input{hinh/mde.tex}
\caption{Hiệu ứng nhỏ nhất phát hiện được của $\delta$: lực 80\%, mức một phía 0,05/3; $\sigma_d = 0{,}2$ minh họa; chuyển tiếp 18 tháng bị loại, sau 24 tháng. Bằng $0{,}64\sigma_d$, $1{,}24\sigma_d$, $1{,}76\sigma_d$ khi $\phi = 0$; 0,6; 0,8.}
\end{figure}
MỚI: \begin{itemize}
\item Thêm mã làm mỗi tháng bớt nhiễu riêng của từng mã, nhưng không làm giảm cú sốc theo tháng tác động khác nhau lên hai nhóm
\item Thêm tháng mới có tác dụng thật; cửa sổ trước còn 24 tháng \so hiệu ứng nhỏ nhất tăng khoảng 1,3 lần
\end{itemize}
\begin{table}
\begin{tabular*}{\textwidth}{@{\extracolsep\fill}lccc}
\toprule
Tự tương quan $\phi$ của chuỗi $d_t$ & 0 & 0,6 & 0,8\\
\midrule
Hiệu ứng nhỏ nhất phát hiện được của $\delta$ & $0{,}64\sigma_d$ & $1{,}24\sigma_d$ & $1{,}76\sigma_d$\\
\bottomrule
\end{tabular*}
\caption{Lực 80\%, mức một phía 0,05/3; cửa sổ trước 193 tháng, chuyển tiếp 18 tháng bị loại, sau 24 tháng. Minh họa: $\sigma_d = 0{,}2$ và $\phi = 0{,}6$ \so phát hiện được Amihud giảm từ khoảng 22\%.}
\end{table}
```

### m9. [MINOR] Slide 19, dòng 310. "Không bác bỏ được gọi là chưa đủ cơ sở kết luận" rộng hơn v14

v14 [210] đặt điều kiện: chỉ khi khoảng tin cậy chứa cả 0 lẫn tác động lớn hơn MDE. Khoảng tin cậy hẹp quanh 0 lại là bằng chứng không có tác động lớn ([185] dùng đúng lập luận này cho trụ sở).

```text
CŨ: Dữ liệu sau sự kiện chỉ 24 tháng & Không bác bỏ được gọi là chưa đủ cơ sở kết luận, không phải không có tác động\\
MỚI: Dữ liệu sau sự kiện chỉ 24 tháng & Khoảng tin cậy chứa cả 0 lẫn tác động lớn hơn hiệu ứng nhỏ nhất: gọi là chưa đủ cơ sở kết luận, không phải không có tác động\\
```

### m10. [MINOR] Slide 24, dòng 387. Bảng dự phòng có 4 dòng, v14 nêu 5 phương án

Thiếu phương án khi dữ liệu sau sự kiện dưới 24 tháng hoặc rổ CS dưới 30 mã [213]. Bảng 5 dòng vẫn vừa trang.

```text
CŨ: Không dùng được GFCI & \HH{1} ở dạng mô tả\\
MỚI: Không dùng được GFCI & \HH{1} ở dạng mô tả\\
Sau sự kiện dưới 24 tháng; rổ CS dưới 30 mã & Dùng mọi tháng có sẵn; rổ 20 mã\\
```

### m11. [MINOR] Slide 24, dòng 375. Chưa nói lý do cốt lõi của đăng ký trước: thí sinh đã dùng dữ liệu HOSE

v14 [148]: thí sinh đã dùng dữ liệu HOSE trong các bài trước nên khai rõ phạm vi đã tính. review-pap coi đây là điểm hội đồng sẽ hỏi.

```text
CŨ: \item Mọi thay đổi sau đó ghi là lệch kế hoạch
MỚI: \item Khai rõ sàn, giai đoạn, chỉ báo đã dùng trong các bài trước
\item Mọi thay đổi sau đó ghi là lệch kế hoạch
```

### m12. [MINOR] Slide 25, dòng 418. Chỉ tiêu (6) thiếu phần kiểm chứng được

v14 [93]: báo cáo đi "kèm văn bản xác nhận hoặc cam kết sử dụng kết quả của ít nhất một đơn vị".

```text
CŨ: \item Báo cáo gửi Sở KH\&CN Hà Nội
MỚI: \item Báo cáo gửi Sở KH\&CN Hà Nội, kèm cam kết sử dụng
```

### m13. [MINOR] `hinh/tran.tex`, dòng 6. Chỉ áp dụng nếu không nhận B1: đường HNX giả định làm tròn giá trần xuống

Như đã nêu ở B1, QĐ 529/QĐ-SGDHN không quy định chiều làm tròn. Đường phẳng ở 10% là biên độ danh nghĩa, không cần giả định. Phần còn lại của hai biểu đồ khớp quy tắc: bước giá HOSE 10/50/100 đồng với ngưỡng 10.000 và 50.000 đồng, HNX 100 đồng mọi mức giá [122]; đường HOSE làm tròn giá trần xuống theo bước giá [125]; điểm 1.140 đồng cho 6,14% [125]. Dữ liệu `.dat` tạo lại từ `taodulieu.py` trùng từng byte với tệp trong repo.

Tệp: `latex/slides/hinh/tran.tex` (chuỗi CŨ duy nhất trong tệp này).

```text
CŨ: \addplot[Cam, no markers, line width=0.8pt] table[x=gia, y=hnx]{hinh/tran_hnx.dat};
MỚI: \addplot[Cam, no markers, line width=0.8pt, domain=1:20, samples=2] {10};
```

## Đối chiếu số liệu, ngày, pháp lý, trích dẫn với v14

| Nội dung trên slide | Nguồn | Trạng thái |
|---|---|---|
| 299 mã tính đến phiên 30/9/2026; phiên cuối HNX 23/12; tạm ngừng 24 và 25/12; phiên đầu HOSE 28/12/2026 | [73], [76]; thông báo VNX trong `TaiLieu_Vong12` | KHỚP |
| TT 57/2021 hạn năm 2023; TT 69/2023 hết 2025; TT 139/2025 (ký 30/12/2025) hết 31/12/2026 | [73]; `TONG_HOP_TAI_LIEU_HNX_HOSE.txt` | KHỚP |
| HNX ngừng nhận niêm yết mới từ 1/7/2025 | [131] | KHỚP |
| UPCoM không thuộc đợt này | [74], [212] | KHỚP |
| NQ 222/2025/QH15; QĐ 1193/QĐ-UBND, bài toán 19 | [68], [72], [288] | KHỚP |
| GFCI 40: TP.HCM 67/117, Đà Nẵng 71, Hà Nội không có | [72] | KHỚP |
| Bước giá HNX 100 đồng (QĐ 529, Điều 23); HOSE 10/50/100 đồng (QĐ 341, 2016; quy chế 2025) | [122], [280], [281]; bản trích QĐ 529 | KHỚP |
| 1.140 đồng, trần 1.210 đồng, 6,14% | [125]; tính lại | KHỚP |
| FTSE Russell bốn đợt 9/2026–9/2027 | [193] | KHỚP |
| Ba giai đoạn 6/2009–6/2025, 7/2025–12/2026, 1/2027–12/2028 | [131] | KHỚP |
| MDE 0,64σ; 1,24σ; 1,76σ; khoảng 1,3 lần; 0,25 log, khoảng 22% | [206], [207]; tính lại | KHỚP |
| ρ = 5 (độ nhạy 3 và 10); 20 và 8 cửa sổ; 104 tuần; rổ CS tối đa 30 mã | [152], [160], [161] | KHỚP |
| M₁–M₇ và nguồn | Bảng 3 [145] | KHỚP |
| Công thức (1)–(7) | [138]–[189]; GHI-CHU mục 4 | KHỚP |
| Giá trị p 0,004; 0,020; 0,030 (slide 36) | Hộp ví dụ của bản dài, không có trong v14 | LỆCH quy tắc GHI-CHU (B4) |
| 9 mục "Tài liệu chính" | [290]–[351] | KHỚP |

## Đối chiếu với Shapiro (sau khi áp các cặp)

| Nguyên tắc | Hiện trạng |
|---|---|
| Motivation trong 1–2 slide | Slide 2–3 đạt; B2 thêm lý do vì sao hội đồng nên quan tâm |
| Câu hỏi nghiên cứu xuất phát từ kinh tế, không từ văn liệu | Slide 4–5 đạt |
| Preview, bottom line | Chưa có kết quả; bottom line là MDE minh họa, hai chỉ số và hàm ý cho Hà Nội (B5, B6) |
| Data: nguồn từng biến | Slide 9 đạt |
| Model: viết tường minh, giả định nhận dạng có lý do kinh tế | Slide 14 đạt; B7 thêm lời trực giác |
| Dừng lại nói điểm yếu lớn nhất | Slide 19 đạt; m9 sửa câu về kết quả không bác bỏ |
| Hình kể chuyện; không đưa lên slide điều không nói | B1, m8 bỏ hai hình thừa; giữ trục thời gian, khung phân tích, hình khác biệt kép |
| Scaling cho 30 phút | Xem mục thời lượng |

## Thời lượng

Sau khi áp các cặp, có 29 trang trước \lastslide: trang bìa, 4 slide mục, 2 trang tài liệu và 22 slide nội dung, tức khoảng 1,3 phút mỗi slide. Mức này vừa 30 phút nhưng không dư. Nếu tập nói vượt giờ, chuyển slide "Lực kiểm định" (m8) vào phụ lục trước.

## Câu hỏi hội đồng dự kiến và chỗ trả lời

| Câu hỏi | Chỗ trả lời |
|---|---|
| Giao dịch đã điện tử toàn quốc, sao đổi sàn lại làm thanh khoản đổi? | Slide cơ chế mới (B1); [185]: khoảng tin cậy hẹp quanh 0 sẽ không ủng hộ vai trò của vị trí sàn |
| Sao không chỉ bỏ ngày chạm trần, sàn? | Slide "Xử lý" (m4) |
| Mã chuyển sàn đã tự chọn HNX từ trước? | Phụ lục hướng sai lệch |
| Dòng lệnh từ HOSE chảy sang mã chuyển sàn thì đối chứng còn sạch? | Phụ lục hướng sai lệch |
| Kết quả giữa kỳ H₃ ở năm 2 có làm tăng sai lầm loại I? | Chưa có slide. Đáp theo v14 [245]: kết quả giữa kỳ chỉ báo cáo theo tệp đăng ký; kiểm định chính dùng đủ 24 tháng |
| Bài báo 1 (H₂) ra trước khi có H₃ thì Holm áp thế nào? | v14 chưa nói; nên chuẩn bị lời đáp miệng, không đưa lên slide |
| Mức giảm 22% có ý nghĩa chính sách không? | v14 chưa nói; đáp theo [207]: σ, φ thật được ước lượng lại và ghi vào tệp đăng ký |
| Thí sinh đã thấy dữ liệu HOSE? | Slide đăng ký trước (m11) |
| Thí sinh đủ sức làm? | Slide năng lực (B3) |
| Vì sao không phân cụm theo mã? | Phụ lục phân cụm |

## Ngoài phạm vi nội dung, để agent A cân nhắc

- Template dùng `tabular*{\textwidth}{@{\extracolsep\fill}...}` và không thu nhỏ chữ trong bảng; deck dùng `tabularx` kèm `\small` ở 10 bảng và một đoạn ở slide 21. Cặp m8 đã theo đúng kiểu template.
- Template có nút `\hyperlink` và `\beamergotobutton` nối slide chính với slide dự phòng; deck chưa dùng.
- Slide 7 (khung phân tích) có nút TikZ chạm x = 441 pt trên trang rộng 453,5 pt.

## Điểm rubric beamer (ước tính)

Bản hiện tại: 100 − 8 (điểm vẽ cứng trên đường MDE) − 11 (`\small` ở 11 slide) = 81; thêm overlay vi phạm Hard Rule 1 (rubric không có mức trừ riêng). Sau khi áp các cặp: không overlay, không điểm vẽ cứng, `\small` ở 12 slide: 88. Bỏ `\small` ở những bảng vừa trang không cần thu nhỏ sẽ đưa điểm lên trên 90.

## Bảng đếm

| Mức | Số | Mục |
|---|---|---|
| CRITICAL | 0 | |
| MAJOR | 7 | B1, B2, B3, B4, B5, B6, B7 |
| MINOR | 13 | m1–m13 |
| **Tổng** | **20** | |
