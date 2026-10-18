# Rà soát vòng 1 (B): nội dung bộ slide bảo vệ đề cương

Đối tượng: `latex/slides/slides.tex` (581 dòng, 32 trang PDF ở `outputs/slides/slides-vong0.pdf`, đọc bằng `pdftotext -layout`).
Nguồn đối chiếu: `outputs/round-14/v14-text-round-14.txt` (v14 đã duyệt, trích theo số đoạn `[n]`) và `latex/ban-dai/chapters/*.tex`.
Ngày rà: 18/10/2026. Người rà: Claude (phiên rà soát nội dung B). Không sửa tệp nào ngoài báo cáo này, không render ảnh.

Skill đã nạp và áp dụng: beamer (pedagogy, review, devils-advocate, mở/kết bài, mật độ), beamer-presentation (tiêu đề nêu kết luận, nhận dạng, backup, kết bằng takeaway), econ-write, mhe-identification (chế độ critic), consistency-checker, fact-checker, vina-me, vietnamese-human-writing. Bổ sung theo yêu cầu điều phối: Shapiro, *How to Give an Applied Micro Talk* (`ho-so/tham-khao/Shapiro-How-to-Give-an-Applied-Micro-Talk.txt`), các phát hiện liên quan ghi ở mục E.

Quy ước: "Slide n" là số trang trong PDF; "dòng" là dòng trong `slides.tex`. Mỗi chuỗi **CŨ** chép nguyên văn và đã được kiểm bằng script: xuất hiện đúng một lần trong `slides.tex`. **MỚI** là đúng mã LaTeX thay vào. Với slide mới, CŨ là chuỗi đứng ngay trước chỗ chèn và MỚI gồm chuỗi đó cộng frame mới. Mọi nội dung đề xuất lấy từ v14 hoặc bản dài; không thêm sự kiện hay số liệu mới.

## Đánh giá chung

Bộ slide đi đúng mạch: mở bằng sự kiện có ngày cụ thể, câu hỏi và đóng góp xuất hiện ở slide 4 và 5, có phần nhận dạng riêng, kết bằng ba ý. Phần lớn con số khớp v14: 299 mã, 23/12, 24–25/12, 28/12/2026, GFCI 40 (67, 71, 117), ±7%/±10%, bước giá, 1.140 đồng và 6,14%, hiệu ứng nhỏ nhất phát hiện được (0,64σ; 1,24σ; 1,76σ; 22%; 1,3 lần), 20 và 8 cửa sổ, bảy mô hình, các công thức (1)–(7). Các số suy ra (0,13; 12%; 0,35; 30%; −22% ở ví dụ khác biệt kép; 28 cửa sổ; ngưỡng Holm) tính lại đều đúng và có ghi "minh họa".

Vấn đề còn lại thuộc bốn loại:

1. Một lỗi hiển thị làm sai ngày trên slide mở đầu (dấu "/" trong `\foreach`), và danh mục tài liệu lệch v14.
2. Một số tiêu đề và câu kết nói mạnh hơn v14: "không do doanh nghiệp chọn", "sự kiện ngoại sinh", "không phụ thuộc vào số mã", "tách theo ba kênh", "Hà Nội mất gì, được gì".
3. Phần nhận dạng thiếu giả định nhận dạng viết tường minh, thiếu quy tắc chọn cửa sổ trước, thiếu điều kiện để bootstrap tự hồi quy đáng tin, và chưa có backup cho câu hỏi lan tỏa sang nhóm đối chứng.
4. Chưa có "bottom line" định lượng và chưa có chỗ dừng để nói điểm yếu lớn nhất (theo Shapiro).

---

## A. Đối chiếu số liệu, ngày, văn bản, trích dẫn với v14

### 1. CRITICAL: Slide 2, dòng 42. Trục thời gian in sai ngày: "30", "9" và "lùi đến 31"

`\foreach \x/\a/\b` tách mỗi phần tử theo dấu "/". Phần tử `6.0/2025/TT 139: lùi đến 31/12/2026` bị cắt thành `\b = TT 139: lùi đến 31`, còn `8.8/30/9/2026/VNX công bố lịch` thành `\a = 30`, `\b = 9`. PDF trang 2 xác nhận: trên trục in "30" ở vị trí của mốc VNX, dưới trục in "9", và nhãn TT 139 dừng ở "lùi đến 31". Ba mốc này sai so với v14 [73] (hạn 31/12/2026; VNX công bố ngày 30/9/2026). Bọc phần chứa "/" trong ngoặc nhọn để `\foreach` không tách.

```text
CŨ: \foreach \x/\a/\b in {0.4/2021/TT 57: hạn năm 2023, 3.2/2023/TT 69: lùi đến hết 2025, 6.0/2025/TT 139: lùi đến 31/12/2026, 8.8/30/9/2026/VNX công bố lịch}
MỚI: \foreach \x/\a/\b in {0.4/2021/{TT 57: hạn năm 2023}, 3.2/2023/{TT 69: lùi đến hết 2025}, 6.0/2025/{TT 139: lùi đến 31/12/2026}, 8.8/{30/9/2026}/{VNX công bố lịch}}
```

### 2. CRITICAL: Slide 24, dòng 471–476. Bốn mục tài liệu lệch với danh mục v14

So với v14 (danh mục tài liệu, các đoạn [290], [302], [339], [346]): tên bài Amihud thiếu phụ đề; tên tạp chí của Conley và Taber, Rambachan và Roth thiếu "The"; tên và loại luận án của Naeem bị rút gọn.

```text
CŨ: \item Amihud, Y. (2002). Illiquidity and stock returns. \emph{Journal of Financial Markets, 5}(1), 31--56.
MỚI: \item Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects. \emph{Journal of Financial Markets, 5}(1), 31--56.
```

```text
CŨ: with a small number of policy changes. \emph{Review of Economics and Statistics, 93}(1), 113--125.
MỚI: with a small number of policy changes. \emph{The Review of Economics and Statistics, 93}(1), 113--125.
```

```text
CŨ: \item Naeem, M. M. F. (2023). What makes an International Financial Centre (IFC) competitive? [Luận án tiến sĩ, Durham University].
MỚI: \item Naeem, M. M. F. (2023). \emph{What makes an International Financial Centre (IFC) competitive? An empirical study of the determinants responsible for the competitiveness of an IFC} [Luận án Tiến sĩ Quản trị kinh doanh (DBA), Durham University]. Durham E-Theses.
```

```text
CŨ: A more credible approach to parallel trends. \emph{Review of Economic Studies, 90}(5), 2555--2591.
MỚI: A more credible approach to parallel trends. \emph{The Review of Economic Studies, 90}(5), 2555--2591.
```

### 3. MAJOR: Slide 24, dòng 476. Hai nguồn được trích trong phần chính nhưng không có trong "Tài liệu chính"

Wardle và Mainelli (2026) (slide 3) và Callaway và Sant'Anna (2021) (slide 21) được trích ở phần chính mà không có trong danh mục. Phụ lục còn trích DeMiguel, Ledoit và Wolf, Markowitz, Black và Litterman, Garlappi, Kritzman, Nguyễn và Nguyễn; nếu không đưa hết vào slide thì ghi một dòng trỏ về danh mục đầy đủ của đề cương. Mục nhập lấy nguyên từ v14 [297], [351].

```text
CŨ: \item Rambachan, A., \& Roth, J. (2023).
MỚI: \item Callaway, B., \& Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. \emph{Journal of Econometrics, 225}(2), 200--230.
\item Rambachan, A., \& Roth, J. (2023).
```

```text
CŨ: 2555--2591.
\end{itemize}}
MỚI: 2555--2591.
\item Wardle, M., \& Mainelli, M. (2026, September). \emph{The Global Financial Centres Index 40}. Z/Yen Group \& China Development Institute.
\end{itemize}
Nguồn trong phụ lục: xem danh mục tài liệu tham khảo của đề cương.}
```

(Cặp thứ hai áp sau cặp số 2; chuỗi CŨ "2555--2591.\n\end{itemize}}" vẫn duy nhất sau khi sửa.)

### 4. MAJOR: Slide 2, dòng 51. Thiếu mốc tính 299 mã; "doanh nghiệp không tự chọn" nói quá

v14 [76] ghi "299 mã tính đến phiên 30/9/2026"; slide bỏ mốc này, nên con số dễ bị hiểu là số chốt ngày chuyển. Về nhận dạng (mhe-identification), bản dài (ch04-1-lydo.tex, dòng 104) chỉ khẳng định *thời điểm* chuyển không do từng doanh nghiệp chọn, và nói rõ "nhóm chuyển sàn vẫn là các doanh nghiệp đã chọn niêm yết ở HNX từ trước". Những doanh nghiệp đã tự chuyển sang HOSE trước 2026 (v14 [211]) không còn trong nhóm xử lý, nên thành phần nhóm có chọn lọc. Câu "doanh nghiệp không tự chọn" để hội đồng hiểu là phân nhóm như ngẫu nhiên.

```text
CŨ: \item \al{299 mã}, chuyển \al{cùng một ngày}, theo quyết định hành chính (doanh nghiệp không tự chọn)
MỚI: \item \al{299 mã} (tính đến phiên 30/9/2026), chuyển \al{cùng một ngày} theo lịch của VNX; thời điểm không do từng doanh nghiệp chọn
```

---

## B. Khẳng định quá mức và vấn đề phương pháp (mhe-identification, chế độ critic)

**Câu hỏi viết lại theo kết cục tiềm năng.** H3 hỏi $E[A_{it}(1) - A_{it}(0) \mid D_i = 1, t \geq 1/2027]$, tức ATT của việc đổi sàn trên các mã đang niêm yết tại HNX. **Nguồn biến thiên** là lịch hành chính đặt cùng một ngày cho mọi mã. Thiết kế diệt được thiên lệch chọn *thời điểm*, nhưng không diệt khác biệt *xu hướng* giữa nhóm đã ở lại HNX và nhóm HOSE; việc đó thuộc về giả định xu hướng song song. **Kết luận theo MHE**: thiết kế đứng được nếu slide trình bày nó đúng như v14, tức là một sự kiện, tác động gộp, suy luận dựa trên số tháng. Những câu "ngoại sinh", "không do doanh nghiệp chọn", "tách theo kênh", "không phụ thuộc số mã" làm thiết kế có vẻ mạnh hơn mức v14 cam kết. Trước hội đồng, đây chính là chỗ dễ bị hỏi vặn nhất.

### 5. MAJOR: Slide 23, dòng 456–461. Ba ý chính lặp lại khẳng định quá mức, tự khen thiết kế, và lệch danh sách sản phẩm

- Ý 1 lặp "không do doanh nghiệp chọn" (xem mục 4).
- Ý 2 dùng "Thiết kế chặt": econ-write không cho tự gắn tính từ khen công trình của mình. "bootstrap cho một sự kiện" cũng không đúng tên phương pháp.
- Ý 3: v14 [86] nói "Hai chỉ số … cùng tệp đăng ký trước là sản phẩm có được dù kết quả kiểm định ra sao". Báo cáo định hướng không thuộc nhóm này.
- Tiêu đề "Ba điều cần nhớ" nêu chủ đề, không nêu kết luận (beamer-presentation). Theo Shapiro thì cũng thiếu một "bottom line" định lượng; xem mục 27.

```text
CŨ: \frametitle{Ba điều cần nhớ}
MỚI: \frametitle{Đợt chuyển sàn đo được; tác động từ khoảng 22\% trở lên sẽ phát hiện được}
```

```text
CŨ: \item \textsb{Cơ hội đo hiếm có:} 299 mã đổi sàn cùng ngày, không do doanh nghiệp chọn
\item \textsb{Thiết kế chặt:} khác biệt kép, ngưỡng lợi suất chung, bootstrap cho một sự kiện, đăng ký trước
\item \textsb{Sản phẩm dùng được dù kết quả ra sao:} hai chỉ số và báo cáo định hướng cho thị trường vốn Hà Nội
MỚI: \item \textsb{Một sự kiện đo được:} 299 mã đổi sàn cùng ngày; thời điểm không do từng doanh nghiệp chọn
\item \textsb{Thiết kế:} khác biệt kép, ngưỡng lợi suất chung, bootstrap tự hồi quy trên chuỗi theo tháng, đăng ký trước; với $\sigma = 0{,}2$, $\phi = 0{,}6$ (minh họa), phát hiện được Amihud giảm từ khoảng 22\%
\item \textsb{Sản phẩm có được dù kết quả ra sao:} hai chỉ số và tệp đăng ký trước; kèm báo cáo định hướng cho thị trường vốn Hà Nội
```

### 6. MAJOR: Slide 5, dòng 104. "bằng một sự kiện ngoại sinh" không có trong v14

v14 không gọi sự kiện là ngoại sinh. Ngoại sinh là một giả định cần bảo vệ, không phải dữ kiện: lịch đã được biết trước (v14 [131]), trùng với ba cú sốc khác (v14 [193]), và nhóm xử lý có chọn lọc (mục 4). Đặt chữ này lên tiêu đề là mời hội đồng phản bác ngay.

```text
CŨ: \frametitle{Đóng góp: đo vai trò của sàn ở một thị trường mới nổi, bằng một sự kiện ngoại sinh}
MỚI: \frametitle{Đóng góp: đo vai trò của sàn ở một thị trường mới nổi, qua đợt chuyển sàn cùng một ngày}
```

### 7. MAJOR: Slide 15, dòng 300 và 305. "không phụ thuộc vào số mã" trái với v14; bảng thiếu tiền đề

v14 [205]: lực kiểm định "phụ thuộc chủ yếu vào số tháng … và chỉ phụ thuộc yếu vào số cổ phiếu". Ba giá trị 0,64σ, 1,24σ, 1,76σ của v14 [206] tính với cửa sổ trước 193 tháng, 18 tháng chuyển tiếp bị loại và 24 tháng sau; slide không nêu điều kiện này, trong khi ước lượng chính lại dùng cửa sổ trước ngắn hơn (mục 9).

```text
CŨ: \frametitle{Lực kiểm định phụ thuộc vào số tháng, không phụ thuộc vào số mã}
MỚI: \frametitle{Lực kiểm định phụ thuộc chủ yếu vào số tháng, chỉ phụ thuộc yếu vào số mã}
```

```text
CŨ: {\small (lực 80\%, mức một phía 0,05/3; $\sigma = 0{,}2$ minh họa)}\\[2mm]
MỚI: {\small (lực 80\%, mức một phía 0,05/3; trước 193 tháng, sau 24 tháng; $\sigma = 0{,}2$ minh họa)}\\[2mm]
```

### 8. MAJOR: Slide 16, dòng 327 và 343. "Tác động được tách theo ba kênh" trái với v14

v14 [181]: "hệ số tương tác không đo riêng tác động của từng quy tắc"; v14 [197]: "δ đo tác động gộp của sàn, không đo riêng từng quy tắc". Về trụ sở, v14 [185] nói chênh lệch "không phải tác động nhân quả của vị trí trụ sở, và không đo lượng thanh khoản mà thị trường vốn Hà Nội mất". Ở slide, ý này chưa xuất hiện.

```text
CŨ: \frametitle{Tác động được tách theo ba kênh và theo trụ sở doanh nghiệp}
MỚI: \frametitle{Tác động khác nhau theo mức chịu ba cú sốc và theo trụ sở, nhưng không tách riêng từng quy tắc}
```

```text
CŨ: \item Trụ sở tại Hà Nội: kiểm tra kênh chú ý và thông tin gắn với nơi đặt sàn
MỚI: \item Trụ sở tại Hà Nội: kiểm tra kênh chú ý và thông tin gắn với nơi đặt sàn; không phải tác động nhân quả của trụ sở
\item $\delta$ là tác động gộp của sàn; hệ số tương tác không đo riêng từng quy tắc
```

### 9. MAJOR: Slide 12, dòng 227. Thiếu quy tắc chọn cửa sổ trước của ước lượng chính

v14 [170]: cửa sổ trước của ước lượng chính "bắt đầu sau điểm gãy cấu trúc cuối cùng của chuỗi chênh lệch theo tháng (Bai & Perron, 1998)", kèm ước lượng với cửa sổ trước 24 tháng (7/2023–6/2025). Trong phần chính, chỉ slide 15 nhắc "rút còn 24 tháng" mà không giải thích vì sao. Hội đồng sẽ hỏi "so 16 năm trước với 2 năm sau à?", và slide chưa trả lời được.

```text
CŨ: \item \HH{3}: $\delta < 0$
MỚI: \item \HH{3}: $\delta < 0$
\item Cửa sổ trước: sau điểm gãy cấu trúc cuối (Bai \& Perron, 1998); báo cáo kèm 7/2023--6/2025
```

### 10. MAJOR: Slide 14, dòng 284, 289 và 292. Bootstrap tự hồi quy thiếu hai điều kiện v14 cam kết, và giá trị p không ghi một phía

Bootstrap tự hồi quy chỉ đáng tin khi mô hình AR đúng và kích thước kiểm định đúng. v14 [172] cam kết hai việc: "hệ số được hiệu chỉnh độ chệch" và "kích thước kiểm định được kiểm tra bằng mô phỏng trước ngày đăng ký". Slide bỏ cả hai. v14 [208] quy định giá trị p một phía, còn "cực đoan hơn" gợi ý kiểm định hai phía.

```text
CŨ: \item Thống kê: trung bình $d_t$ sau trừ trước
MỚI: \item Thống kê: trung bình $d_t$ sau trừ trước
\item Kích thước kiểm định kiểm tra bằng mô phỏng trước ngày đăng ký
```

```text
CŨ: \node[box, text width=5cm] (s1) {Ước lượng AR trên giai đoạn tham chiếu};
MỚI: \node[box, text width=5cm] (s1) {Ước lượng AR trên giai đoạn tham chiếu, hiệu chỉnh độ chệch};
```

```text
CŨ: (s4) {Giá trị p = tỷ lệ chuỗi giả cực đoan hơn};
MỚI: (s4) {Giá trị p một phía = tỷ lệ chuỗi giả có thống kê nhỏ hơn hoặc bằng giá trị thật};
```

### 11. MAJOR: Slide 6, dòng 134. Chú giải nói nét liền là "kiểm định hoặc ước lượng", nhưng mũi tên Trước hợp nhất → Sự kiện chỉ là trình tự thời gian

Ghi chú Hình 1 ở v14 [117]: "mũi tên từ ô Trước hợp nhất sang ô Sự kiện chỉ trình tự thời gian". Với chú giải hiện tại, hội đồng sẽ đọc là có kiểm định quan hệ H2 → H3, điều đề cương không làm.

```text
CŨ: {\footnotesize Nét liền: kiểm định hoặc ước lượng. Nét đứt: tổng hợp định tính.}
MỚI: {\footnotesize Mũi tên ngang đầu: trình tự thời gian. Mũi tên khác biệt kép: ước lượng \HH{3}, \HH{4}. Nét đứt: tổng hợp định tính.}
```

### 12. MAJOR: Phụ lục, sau dòng 524. Thiếu backup về ba giả định của khác biệt kép, lan tỏa sang nhóm đối chứng và rời mẫu

Câu hội đồng dễ hỏi nhất: "dòng tiền chảy từ mã HOSE sang mã chuyển sàn thì đối chứng còn sạch không?" Phần chính và phụ lục đều chưa trả lời. v14 [192]–[197] đã có đủ nội dung, gồm hướng sai lệch theo từng trường hợp, rời mẫu, và rủi ro hồi quy về trung bình khi ghép theo Amihud (v14 [171]). Đề xuất thêm một slide phụ lục.

```text
CŨ: \item 18 tháng chuyển tiếp giữa tháng gốc và giai đoạn sau $\Rightarrow$ khoảng tin cậy có thể rộng
\end{itemize}
\end{frame}
MỚI: \item 18 tháng chuyển tiếp giữa tháng gốc và giai đoạn sau $\Rightarrow$ khoảng tin cậy có thể rộng
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Phụ lục: ba giả định của khác biệt kép và hướng sai lệch nếu vi phạm}
{\small
\begin{itemize}
\item Xu hướng song song: hệ số trước sự kiện, độ nhạy theo Rambachan và Roth (2023)
\item Nhóm chuyển sàn đã chọn HNX từ trước: $\alpha_i$ hấp thụ khác biệt cố định, không hấp thụ khác biệt xu hướng
\item Đối chứng HOSE mất thanh khoản vì dòng lệnh chuyển sang mã chuyển sàn $\Rightarrow$ $\delta$ phóng đại; đối chứng UPCoM là một cận khác
\item Lan tỏa dương sang HOSE (Amihud và cộng sự, 1997; Hisada, 2018) $\Rightarrow$ $\delta$ đánh giá thấp
\item Rời mẫu: báo cáo tỷ lệ hủy niêm yết từng nhóm, ước lượng lại trên bảng cân bằng
\item Ghép theo Amihud có thể tạo hồi quy về trung bình: báo cáo thêm khi chỉ ghép theo vốn hóa và ngành (Daw \& Hatfield, 2018)
\end{itemize}}
\end{frame}
```

(Nếu dùng slide này, thêm Amihud và cộng sự (1997) và Daw và Hatfield (2018) vào danh mục, hoặc dựa vào dòng "xem danh mục của đề cương" ở mục 3.)

---

## C. Mạch trình bày 30 phút, slide thừa hoặc thiếu, backup

**Cân đối.** Phần chính có 20 slide nội dung, 4 slide chia mục, tài liệu và cảm ơn, tức khoảng 1,5 phút một slide. Mức này hợp với 30 phút theo bảng thời lượng của skill beamer, nên không phải cắt nhiều. Phân bổ: động cơ 2, câu hỏi và đóng góp 2, khung 1, dữ liệu và đo lường 3, nhận dạng 5, H4 và H1 2, kế hoạch 2, kết 1. Phần nhận dạng chiếm tỉ trọng lớn nhất, đúng với vai trò trọng tâm của H3.

**Lặp.** Trục thời gian xuất hiện ba lần (slide 2, slide 8, phụ lục slide 32). Mức này chấp nhận được, vì mỗi lần một mục đích.

**Phần còn thiếu, xếp theo mức hội đồng có thể hỏi:**

- Lan tỏa và tính sạch của đối chứng: mục 12.
- Giả định nhận dạng viết tường minh: mục 25.
- Điểm yếu lớn nhất: mục 26.
- Chi tiết suy luận H4: mục 23.
- Không có liên kết từ slide chính sang slide phụ lục (`\hyperlink`). Đây là việc kỹ thuật, không lập cặp sửa.

### 13. MINOR: Slide 8, dòng 158. Lý do loại giai đoạn chuyển tiếp nên theo đúng căn cứ của v14

v14 [131] dựa vào sự kiện "HNX ngừng tiếp nhận hồ sơ đăng ký niêm yết cổ phiếu mới từ ngày 01/7/2025". Câu "thị trường đã biết trước sự kiện từ 1/7/2025" có trong hộp ví dụ của bản dài (ch04-3a-khung.tex, dòng 168), nhưng nói chưa chính xác: hạn chuyển sàn đã được biết từ Thông tư 57/2021, còn ngày chuyển cụ thể chỉ được biết từ 30/9/2026.

```text
CŨ: \item Chuyển tiếp bị loại khỏi kiểm định chính: thị trường đã biết trước sự kiện từ 1/7/2025
MỚI: \item Chuyển tiếp bị loại khỏi kiểm định chính: từ 1/7/2025 HNX ngừng nhận niêm yết mới, giá có thể phản ứng trước
```

### 14. MINOR: Slide 22, dòng 429 và 446–449. Tiêu đề nói "sáu chỉ tiêu" nhưng chỉ có bốn sản phẩm; "ít nhất một bài" thiếu chữ "mục tiêu"

Chỉ tiêu (3) của v14 [90] (ước lượng H3 với 24 tháng, kèm hiệu ứng nhỏ nhất phát hiện được và khoảng tin cậy) không có trên slide. v14 [92] viết "với mục tiêu ít nhất một bài, do thí sinh là tác giả chính". Cụm "ưu tiên HNX dùng" tối nghĩa; v14 [93] là văn bản xác nhận hoặc cam kết sử dụng, ưu tiên HNX.

```text
CŨ: \item Tệp đăng ký trước có dấu thời gian
\item Chỉ số chất lượng thị trường và chỉ số khả năng đầu tư, mã nguồn mở
\item Ba bài báo, ít nhất một bài WoS Q1/Q2
\item Báo cáo cho Sở KH\&CN Hà Nội, ưu tiên HNX dùng
MỚI: \item Tệp đăng ký trước có dấu thời gian
\item Chỉ số chất lượng thị trường vốn theo tháng từ 6/2009, mã nguồn mở
\item Ước lượng \HH{3} với 24 tháng sau sự kiện, kèm khoảng tin cậy
\item Chỉ số khả năng đầu tư: 20 cửa sổ trước, 8 cửa sổ sau
\item Ba bài báo; mục tiêu ít nhất một bài WoS Q1/Q2, thí sinh là tác giả chính
\item Báo cáo gửi Sở KH\&CN Hà Nội, kèm cam kết sử dụng của ít nhất một đơn vị (ưu tiên HNX)
```

### 15. MINOR: Slide 21, dòng 421. "Đối chứng tổng hợp" dễ bị hiểu là phương pháp đối chứng tổng hợp (synthetic control)

v14 [213] mô tả một nhóm đối chứng gộp từ mã HOSE ngoài danh sách FTSE Russell và mã UPCoM, không phải synthetic control. Câu hội đồng dễ hỏi: nếu cả hai nhóm đều không song song thì gộp lại có song song không? Câu trả lời cần chuẩn bị bằng lời nói.

```text
CŨ: Không song song & Đối chứng tổng hợp\\
MỚI: Không song song & Đối chứng gộp: HOSE ngoài FTSE và UPCoM\\
```

### 16. MINOR: Phụ lục, sau dòng 511. Thiếu backup cho suy luận H4

Hội đồng có thể hỏi ρ bằng bao nhiêu, chi phí giao dịch tính thế nào, khoảng tin cậy của H4 lấy từ đâu. v14 [152], [153], [161], [186] đã trả lời đủ.

```text
CŨ: {\small Danh mục chỉ mua; ước lượng lại hằng tháng trên cửa sổ 104 tuần; báo cáo cả khi bỏ \MM{5}.}
\end{frame}
MỚI: {\small Danh mục chỉ mua; ước lượng lại hằng tháng trên cửa sổ 104 tuần; báo cáo cả khi bỏ \MM{5}.}
\end{frame}

\begin{frame}
\frametitle{Phụ lục: \HH{4} chỉ được ước lượng, kèm khoảng tin cậy bootstrap khối dừng}
{\small
\begin{itemize}
\item $\mu$, $\sigma^2$: lợi suất vượt trội tuần sau chi phí, nhân 52; $\rho = 5$, độ nhạy ở 3 và 10
\item Chi phí A: tỷ lệ cố định nhân vòng quay; chi phí B: phí, thuế và một nửa chênh lệch mua-bán theo mã, theo tháng
\item $\bar{G} > 0$: rổ CS cho lợi suất tương đương chắc chắn thấp hơn rổ H (điểm phần trăm mỗi năm)
\item Báo cáo: $\bar{G}$ sau trừ trước; khoảng tin cậy bootstrap khối dừng trên lợi suất tuần của hai rổ, lấy mẫu đồng thời; số mô hình cùng dấu
\item Cửa sổ ước lượng sau sự kiện còn chứa dữ liệu trước $\Rightarrow$ \MM{1} là phép so sánh sạch nhất
\item Tỷ số Sharpe là thước đo phụ, kiểm định theo Ledoit và Wolf (2008)
\end{itemize}}
\end{frame}
```

---

## D. Tiếng Việt, tiêu đề, thuật ngữ, APA

### 17. MAJOR: Slide 3, dòng 58 và 67. Tiêu đề hứa đo "Hà Nội mất gì, được gì"; câu "Chưa có số đo" là khẳng định mới

v14 [185] nói rõ thiết kế "không đo lượng thanh khoản mà thị trường vốn Hà Nội mất". Hà Nội cũng vẫn còn trái phiếu, phái sinh và UPCoM (v14 [71]). Câu "Chưa có số đo về chất lượng thị trường của Hà Nội" rộng hơn khoảng trống K4 của v14 ("Chưa so sánh HNX với HOSE").

```text
CŨ: \frametitle{Hà Nội cần biết mất gì, được gì khi không còn sàn cổ phiếu niêm yết}
MỚI: \frametitle{Hà Nội cần thước đo chất lượng thị trường để định hướng chuyên môn hóa sau hợp nhất}
```

```text
CŨ: \item Chưa có số đo về chất lượng thị trường của Hà Nội
MỚI: \item Chưa có nghiên cứu so sánh chất lượng thị trường HNX với HOSE
```

### 18. MINOR: Slide 9, dòng 164. "sáu chỉ báo, trọng số bằng nhau" dễ hiểu thành sáu chỉ báo nặng như nhau

Theo v14 [140], ba *chiều* có trọng số bằng nhau. Mỗi chỉ báo thanh khoản vì vậy chỉ nặng 1/9, còn chỉ báo minh bạch nặng 1/3.

```text
CŨ: \frametitle{Chỉ số chất lượng thị trường vốn: ba chiều, sáu chỉ báo, trọng số bằng nhau}
MỚI: \frametitle{Chỉ số chất lượng thị trường vốn: sáu chỉ báo, ba chiều có trọng số bằng nhau}
```

### 19. MINOR: Slide 10, dòng 200. Khẳng định chắc hơn v14

v14 [124]: Amihud "có thể giảm một cách cơ học".

```text
CŨ: {\small Biên độ hẹp $\Rightarrow$ lợi suất bị cắt $\Rightarrow$ Amihud \al{giảm cơ học}}
MỚI: {\small Biên độ hẹp $\Rightarrow$ lợi suất bị cắt $\Rightarrow$ Amihud \al{có thể giảm cơ học}}
```

### 20. MINOR: Slide 4, dòng 94. H3 viết chung là "độ phi thanh khoản", trong khi v14 định nghĩa hẹp

v14 Bảng 2: H3 là độ phi thanh khoản Amihud tính trên các ngày dưới ngưỡng chung.

```text
CŨ: & \HH{3}: độ phi thanh khoản giảm so với đối chứng & \al{trọng tâm}\\
MỚI: & \HH{3}: độ phi thanh khoản Amihud (ngày dưới ngưỡng chung) giảm so với đối chứng & \al{trọng tâm}\\
```

### 21. MINOR: Slide 18, dòng 362, 365 và 366. Phạm vi bảy mô hình mô tả sai; "không phụ thuộc" nói quá; thiếu ρ

Mô hình cuối trong Bảng 3 là M7 (Kritzman và cộng sự), không phải Black-Litterman chuyển chế độ (M5). v14 [143] viết "ít phụ thuộc vào sai số ước lượng của một mô hình". Giá trị cơ sở ρ = 5 (v14 [152]) nên có trên slide, vì công thức U dùng nó.

```text
CŨ: \item \al{7 mô hình phân bổ} \MM{1}--\MM{7}: từ 1/N đến Black-Litterman chuyển chế độ
\item Bình quân để không phụ thuộc một mô hình
MỚI: \item \al{7 mô hình phân bổ} \MM{1}--\MM{7}: từ 1/N đến các mô hình có trạng thái thị trường
\item Bình quân để ít phụ thuộc vào sai số ước lượng của một mô hình
```

```text
CŨ: {\small $U$: lợi suất tương đương chắc chắn sau chi phí;
MỚI: {\small $U$: lợi suất tương đương chắc chắn sau chi phí ($\rho = 5$);
```

### 22. MINOR: Slide 19, dòng 390. Thiếu ý quan hệ nhân quả ngược mà v14 nêu

v14 [190]: "trung tâm mạnh có thể kéo theo giao dịch cổ phiếu, nên β được gọi là liên hệ có điều kiện".

```text
CŨ: \item $\SMD$ ít đổi theo thời gian
MỚI: \item $\SMD$ ít đổi theo thời gian
\item Trung tâm mạnh có thể kéo theo giao dịch cổ phiếu
```

### 23. MINOR: Dòng 80, 254, 419, 503, 504, 506, 522. APA: "&" đứng ngoài ngoặc

Theo APA 7, "&" chỉ dùng trong trích dẫn trong ngoặc; trích dẫn kể tên dùng "và", đúng như Bảng 3 của v14 ("Ledoit và Wolf (2004)").

```text
CŨ: {\footnotesize Wardle \& Mainelli (2026)}
MỚI: {\footnotesize Nguồn: Wardle và Mainelli (2026)}
```

```text
CŨ: độ nhạy theo Rambachan \& Roth (2023)
MỚI: độ nhạy theo Rambachan và Roth (2023)
```

```text
CŨ: Chuyển sàn lùi, nhiều đợt & Callaway \& Sant'Anna (2021)\\
MỚI: Chuyển sàn lùi, nhiều đợt & Callaway và Sant'Anna (2021)\\
```

```text
CŨ: & Ledoit \& Wolf (2004)\\
MỚI: & Ledoit và Wolf (2004)\\
```

```text
CŨ: & Black \& Litterman (1992)\\
MỚI: & Black và Litterman (1992)\\
```

```text
CŨ: \item Độ nhạy trước vi phạm xu hướng song song: Rambachan \& Roth (2023)
MỚI: \item Độ nhạy trước vi phạm xu hướng song song: Rambachan và Roth (2023)
```

### 24. MINOR: Slide 28, dòng 506. M5 thiếu "Mở rộng từ"

v14 Bảng 3: "Mở rộng từ Nguyễn và Nguyễn (2026a)". Bỏ chữ "Mở rộng từ" thì người nghe hiểu M5 chính là mô hình đã công bố. Cặp này gộp luôn phần sửa APA của dòng 506.

```text
CŨ: & Nguyễn \& Nguyễn (2026a)\\
MỚI: & Mở rộng từ Nguyễn và Nguyễn (2026a)\\
```

### 25. MINOR: Các chỗ văn nói, văn tắt hoặc tiêu đề nêu chủ đề

- Slide 15, dòng 309 và 318: tiêu đề cột "Theo $\sigma$" khó hiểu; "chuỗi càng 'dính'" là văn nói.
- Slide 16, dòng 333: "Mã chịu mạnh nhất" thiếu bổ ngữ.
- Slide 12, dòng 217: "so cổ phiếu" là văn nói.
- Slide 13, dòng 247: "được xử lý riêng" không nêu kết luận.
- Tiêu đề phụ lục ở dòng 528 nêu chủ đề, chưa nêu kết luận.

```text
CŨ: $\phi$ & Theo $\sigma$ & Log Amihud & Amihud giảm\\
MỚI: $\phi$ & Bội số $\sigma$ & Log Amihud & Amihud giảm\\
```

```text
CŨ: chuỗi càng ``dính'', cần tác động càng lớn
MỚI: tự tương quan càng cao, tác động phải càng lớn mới phát hiện được
```

```text
CŨ: Thay đổi khi chuyển sàn & Mã chịu mạnh nhất &
MỚI: Thay đổi khi chuyển sàn & Mã chịu tác động mạnh nhất &
```

```text
CŨ: \frametitle{Khác biệt kép: so cổ phiếu chuyển sàn với cổ phiếu HOSE đối sánh}
MỚI: \frametitle{Khác biệt kép: so sánh cổ phiếu chuyển sàn với cổ phiếu HOSE đối sánh}
```

```text
CŨ: \frametitle{Nhóm đối chứng và các cú sốc trùng thời gian được xử lý riêng}
MỚI: \frametitle{Đối chứng là mã HOSE ghép cặp; mỗi cú sốc trùng thời gian có cách xử lý riêng}
```

```text
CŨ: \frametitle{Phụ lục: vì sao không dùng sai số chuẩn phân cụm theo mã}
MỚI: \frametitle{Phụ lục: thêm mã không thêm thông tin, nên không phân cụm theo mã}
```

### 26. MINOR: Slide 5, dòng 112. Không nêu tên nguồn của bằng chứng Euronext và Tokyo–Osaka

Hai nguồn này đã có trong "Tài liệu chính", nhưng ô bảng chỉ ghi tên sự kiện, không ghi nguồn.

```text
CŨ: Hợp nhất sàn & Euronext, Tokyo--Osaka: thị trường phát triển, chỉ đo thanh khoản &
MỚI: Hợp nhất sàn & Euronext (Nielsson, 2009), Tokyo--Osaka (Hisada, 2018): thị trường phát triển, chỉ đo thanh khoản &
```

---

## E. Đối chiếu với Shapiro, *How to Give an Applied Micro Talk*

Đạt:

- Động cơ gói trong hai slide (slide 2 và 3), mở bằng một sự kiện có ngày cụ thể.
- Câu hỏi nghiên cứu xuất phát từ kinh tế học (đổi sàn làm thanh khoản thay đổi bao nhiêu), không xuất phát từ khoảng trống tài liệu.
- Slide 5 đóng vai "This paper", nêu cái mới so với từng nhóm tài liệu.
- Số slide hợp với 30 phút. Phần chính không cố nhồi chi tiết của bản dài.

Chưa đạt: bốn điểm dưới đây.

### 27. MAJOR: Chưa có preview kết quả và "bottom line" định lượng ở đầu bài

Shapiro: "Assume the audience is about to leave", và cần "a single … (ideally) quantitative take-away". Đề cương chưa có kết quả. Thứ định lượng tương đương mà v14 đã có là ngưỡng phát hiện (v14 [207]: với σ = 0,2 và φ = 0,6, chỉ phát hiện được Amihud giảm từ khoảng 22%). Con số này hiện chỉ nằm ở slide 15. Đề xuất đưa nó vào slide câu hỏi; mục 5 cũng đưa nó vào slide kết.

```text
CŨ: {\small \HH{1}--\HH{3}: kiểm định xác nhận, hiệu chỉnh Holm 5\%. \HH{4}: chỉ ước lượng (ít cửa sổ).}
MỚI: {\small \HH{1}--\HH{3}: kiểm định xác nhận, hiệu chỉnh Holm 5\%. \HH{4}: chỉ ước lượng (ít cửa sổ).}\\[1mm]
{\small \textsb{Kết quả đề tài sẽ cho:} khoảng cách HNX--HOSE theo tháng từ 6/2009; tác động của việc chuyển sàn, phát hiện được nếu Amihud giảm từ khoảng 22\% (giả định minh họa, slide 15).}
```

### 28. MAJOR: Slide 12, dòng 218–220. Mô hình chưa viết tường minh giả định nhận dạng

Shapiro ("Be even more explicit") yêu cầu viết ra giả định dạng $E(\varepsilon_{it} \mid x_{it}, \alpha_i, \delta_t) = 0$ và diễn giải nó. Slide 12 có phương trình nhưng không có giả định; xu hướng song song chỉ xuất hiện như một phép kiểm tra ở slide 13. Cách viết dưới đây chỉ là dạng ký hiệu của giả định xu hướng song song ở v14 [192], không thêm nội dung mới.

```text
CŨ: A_{it} = \alpha_i + \tau_t + \delta D_i\Post_t + \varepsilon_{it}
\]
\begin{columns}[T]
\column{0.50\textwidth}
MỚI: A_{it} = \alpha_i + \tau_t + \delta D_i\Post_t + \varepsilon_{it}, \qquad E[\varepsilon_{it} \mid D_i, \Post_t, \alpha_i, \tau_t] = 0
\]
{\small Giả định nhận dạng: nếu không chuyển sàn, chênh lệch log Amihud giữa hai nhóm không đổi theo thời gian (xu hướng song song).}
\begin{columns}[T]
\column{0.50\textwidth}
```

### 29. MAJOR: Chưa có chỗ dừng để nói điểm yếu lớn nhất của cách tiếp cận

Shapiro: "Pause to discuss the most important vulnerabilities … what you will do to assess plausibility". Các điểm yếu hiện nằm rải rác ở slide 13, 14, 16 và trong phụ lục. v14 [220] và phần Kết luận của Bảng 4 đã nêu gọn: một sự kiện duy nhất, độ dài dữ liệu sau sự kiện, các cú sốc trùng thời gian, H1 là liên hệ có điều kiện. Đề xuất một slide ngay sau slide lực kiểm định. Nếu cần giữ thời gian, chuyển slide 16 (tương tác, phân tích phụ) xuống phụ lục; theo Shapiro, đó là loại "fine points" không cần nói trong 30 phút.

```text
CŨ: \item $\sigma$, $\phi$ thật ước lượng lại, ghi vào tệp đăng ký
\end{itemize}
\end{columns}
\end{frame}
MỚI: \item $\sigma$, $\phi$ thật ước lượng lại, ghi vào tệp đăng ký
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Điểm yếu lớn nhất: một sự kiện, đo tác động gộp của sàn}
\begin{center}
{\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.34\textwidth} L@{}}
\toprule
Điểm yếu & Cách đánh giá\\
\midrule
Một sự kiện duy nhất & Bootstrap tự hồi quy trên chuỗi theo tháng; báo cáo hiệu ứng nhỏ nhất phát hiện được và khoảng tin cậy\\
Biên độ, bước giá, hệ thống giao dịch, chỉ số đổi cùng lúc & $\delta$ là tác động gộp của sàn; tương tác theo mức chịu cú sốc là phân tích phụ\\
Cú sốc trùng thời gian ở đối chứng HOSE & Loại mã FTSE Russell; biến giả nhóm bảng; đối chứng UPCoM là một cận khác\\
Dữ liệu sau sự kiện chỉ 24 tháng & Kết quả không bác bỏ được gọi là chưa đủ cơ sở kết luận\\
\bottomrule
\end{tabularx}}
\end{center}
\end{frame}
```

### 30. MINOR: Slide 8, dòng 157 và 159. Dữ liệu chưa nói rõ nguồn của từng biến

Shapiro: "State clearly the source of each variable". v14 [129]–[130] có đủ: dữ liệu giao dịch từ HNX, HOSE và một nhà cung cấp dữ liệu thương mại; GFCI của Z/Yen; chỉ báo thị trường cổ phiếu theo Čihák và cộng sự (2012); quản trị nhà nước theo Kaufmann và cộng sự (2011). Ngược lại, slide 9 và 10 nói khá nhiều về cách xử lý dữ liệu (điểm z, bỏ ngày liền sau, loại mã giá thấp). Ở slide 10 điều đó hợp lý, vì đây là mối đe dọa đo lường chính. Ở slide 9 có thể nói bằng lời thay vì ghi lên slide.

```text
CŨ: \item Dữ liệu ngày của sàn niêm yết HNX, UPCoM, HOSE, \al{kể cả mã đã hủy niêm yết} (tránh thiên lệch sống sót)
MỚI: \item Dữ liệu ngày của sàn niêm yết HNX, UPCoM, HOSE (nguồn: HNX, HOSE, nhà cung cấp thương mại), \al{kể cả mã đã hủy niêm yết}
```

```text
CŨ: \item Quốc tế: điểm GFCI kỳ 1--40, chỉ báo thị trường cổ phiếu, quản trị nhà nước
MỚI: \item Quốc tế: điểm GFCI kỳ 1--40 (Z/Yen), chỉ báo thị trường cổ phiếu (Čihák và cộng sự, 2012), quản trị nhà nước (Kaufmann và cộng sự, 2011)
```

---

## F. Câu hỏi phản biện dự kiến (devils-advocate) và backup tương ứng

| Câu hỏi hội đồng dễ hỏi | Hiện có backup? | Đề xuất |
|---|---|---|
| Mã chuyển sàn đã tự chọn HNX, vậy nhóm xử lý có chọn lọc không? | Không | Mục 4, 12 |
| Dòng tiền chuyển từ HOSE sang mã chuyển sàn thì đối chứng còn sạch không? | Không | Mục 12 |
| Vì sao không dùng sai số phân cụm theo mã? | Có (slide 30) | Đủ |
| Bootstrap tự hồi quy có đúng kích thước không? | Không | Mục 10 |
| Cửa sổ trước dài bao nhiêu, chọn thế nào? | Không | Mục 9 |
| Không bác bỏ thì kết luận gì? | Có (slide 15) | Đủ |
| H4 tính chi phí và khoảng tin cậy thế nào? | Không | Mục 16 |
| M5 do thí sinh phát triển, có thiên vị không? | Có (slide 28) | Đủ |
| Không được dùng GFCI thì sao? | Có (slide 21) | Đủ |

## Ngoài phạm vi rà nội dung

`pdftotext` không lấy ra được dấu ngoặc đơn, dấu hai chấm và "±" ở nhiều slide (ví dụ "Naeem 2023 17 yếu tố", "Biên độ 10% →"). Log không báo `Missing character`, nên nhiều khả năng đây chỉ là lỗi lớp ánh xạ ký tự của font Inter Light, không phải glyph bị mất. Người rà hình ảnh nên nhìn trực tiếp slide 2, 5, 10 và 16 để chắc chắn.

## Bảng đếm

| Mức | Số phát hiện | Mục |
|---|---|---|
| CRITICAL | 2 | 1, 2 |
| MAJOR | 14 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 27, 28, 29 |
| MINOR | 14 | 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 30 |
| **Tổng** | **30** | |

Theo nhóm: A (đối chiếu v14) 4; B (phương pháp, nhận dạng) 8; C (mạch, backup) 4; D (tiếng Việt, APA) 10; E (Shapiro) 4.
