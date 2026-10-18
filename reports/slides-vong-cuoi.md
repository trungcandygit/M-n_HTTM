# Vòng cuối: rà toàn bộ slides.tex (43 trang): 82/100 trước sửa, ước ≥ 95 sau sửa

Đã xem đủ 43 trang (pdftoppm -r 45) đối chiếu wide.pdf; v14 grep đúng đoạn; GHI-CHU.md. Không có CRITICAL: số, mốc, pháp lý, trích dẫn khớp v14; không số minh họa thành kết quả.
Nút: 11 \hyperlink đều có nhãn; 13/14 slide dự phòng có nút quay lại, thiếu tr. 41. \al ≤ 1 mỗi slide. Bảng chính: 4.
Cặp sửa: ⏎ là xuống dòng. Bản máy đọc được (danh sách Python P): /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/vc/pairs.py

## MAJOR
1. Tr. 36 suKien: công thức trưng bày để trần giữa danh sách; đưa vào khung dinhnghia (kiểu Corollary + ≤3 gạch). Rambachan–Roth vẫn giữ.
```text
CŨ: \begin{itemize} ⏎ \item Đặc tả: ⏎ \begin{equation*} ⏎ A_{it} = \alpha_i + \tau_t + \sum_k \delta_k D_i T_{kt} + \varepsilon_{it} ⏎ \end{equation*} ⏎ \item $T_{kt} = 1$ nếu tháng $t$ là $k$; $k$ từ 1/2024 đến 12/2028; gốc 6/2025; trước 1/2024 gộp ⏎ \item Kiểm định
MỚI: \begin{dinhnghia}[Đặc tả nghiên cứu sự kiện] ⏎ $T_{kt} = 1$ nếu tháng $t$ là tháng $k$, với $k$ từ 1/2024 đến 12/2028; gốc 6/2025; trước 1/2024 gộp: ⏎ \[ ⏎ A_{it} = \alpha_i + \tau_t + \sum_k \delta_k D_i T_{kt} + \varepsilon_{it} ⏎ \] ⏎ \end{dinhnghia} ⏎ \begin{itemize} ⏎ \item Kiểm định
```
2. Tr. 17 suyLuan: thống kê kiểm định (công thức chính của suy luận) nằm inline trong danh sách; đóng khung, còn 2 gạch + 2 nút.
```text
CŨ: \begin{enumerate} ⏎ \item 299 mã chỉ chịu \al{một lần} chuyển sàn: coi mã độc lập thì sai số chuẩn quá nhỏ (Conley \& Taber, 2011) ⏎ \item Chuỗi chuyển sàn trừ đối chứng: $d_t$ là chênh lệch log Amihud theo tháng ⏎ \item Thống kê kiểm định: $\bar{d}_\text{sau} - \bar{d}_\text{trước}$ ⏎ \item Giá trị p một phía: so với thống kê trên các chuỗi giả không có sự kiện ⏎ \end{enumerate}
MỚI: \begin{dinhnghia}[Thống kê kiểm định] ⏎ Với $d_t$ là chênh lệch log Amihud theo tháng giữa mã chuyển sàn và mã đối chứng: ⏎ \[ ⏎ \bar{d}_{\vn{sau}} - \bar{d}_{\vn{trước}} ⏎ \] ⏎ \end{dinhnghia} ⏎ \begin{itemize} ⏎ \item 299 mã chỉ chịu \al{một lần} chuyển sàn: coi mã độc lập thì sai số chuẩn quá nhỏ (Conley \& Taber, 2011) ⏎ \item Giá trị p một phía: so với thống kê trên các chuỗi giả không có sự kiện ⏎ \end{itemize}
```
3. Tr. 21/41: slide dự phòng tr. 41 mồ côi: không nhãn, không nút đi từ tr. 21, không nút quay lại. Bốn cặp:
```text
CŨ: \begin{frame} ⏎ \frametitle{Khả năng đầu tư: rổ chuyển sàn kém rổ HOSE bao nhiêu}
MỚI: \begin{frame}[label=khaNang] ⏎ \frametitle{Khả năng đầu tư: rổ chuyển sàn kém rổ HOSE bao nhiêu}
CŨ: \al{chỉ ước lượng} ⏎ \end{itemize}
MỚI: \al{chỉ ước lượng} ⏎ \end{itemize} ⏎ \hyperlink{uocLuongG}{\beamergotobutton{Cách ước lượng}}
CŨ: \begin{frame} ⏎ \frametitle{Phụ lục: khả năng đầu tư chỉ ước lượng, kèm khoảng tin cậy}
MỚI: \begin{frame}[label=uocLuongG] ⏎ \frametitle{Phụ lục: khả năng đầu tư chỉ ước lượng, kèm khoảng tin cậy}
CŨ: (Ledoit \& Wolf, 2008) ⏎ \end{itemize}
MỚI: (Ledoit \& Wolf, 2008) ⏎ \end{itemize} ⏎ \hyperlink{khaNang}{\beamergotobutton{Quay lại slide chính}}
```
7. Tr. 33 Holm: ô tiêu đề dài (quy tắc ô ngắn); caption 2 dòng (quy tắc 1 dòng); '28 cửa sổ' không nguyên văn v14. Hai cặp:
```text
CŨ: Giá trị p (sắp tăng dần) & Ngưỡng & Dừng ở đây: số giả thuyết được ủng hộ\\
MỚI: Giá trị p tăng dần & Ngưỡng & Nếu dừng: số được ủng hộ\\
CŨ: \caption{Giá trị p một phía: GFCI phân cụm theo quốc gia; chỉ số chất lượng thị trường bootstrap khối dừng; Amihud bootstrap tự hồi quy. Khả năng đầu tư ngoài họ: chỉ 28 cửa sổ.}
MỚI: \caption{Giá trị p một phía của \HH{1}--\HH{3}; \HH{4} chỉ ước lượng, ngoài Holm.}
```
9. Tr. 40 mucChiu: tiêu đề nói 'theo trụ sở' nhưng bảng không có trụ sở; 'cú sốc' lẫn với 'thay đổi' ở tr. 11.
```text
CŨ: \frametitle{Phụ lục: tác động theo mức chịu ba cú sốc và theo trụ sở}
MỚI: \frametitle{Phụ lục: tác động theo mức chịu ba thay đổi quy tắc}
```
11. Tr. 40: caption 2 dòng; ý trụ sở đã có ở tr. 26 (mục 4).
```text
CŨ: \caption{Tương tác $D_i\Post_tE_{si}$, đo đến 30/6/2025: phân tích phụ, ngoài Holm, không tách riêng từng quy tắc. Chênh lệch theo trụ sở Hà Nội không phải tác động nhân quả.}
MỚI: \caption{Tương tác $D_i \Post_t E_{si}$, $E_{si}$ đo đến 30/6/2025: phân tích phụ, ngoài Holm.}
```
## MINOR
10. Tr. 40: ô bảng dài 2 vế chữ; viết bằng bất đẳng thức gọn.
```text
CŨ: Tỷ lệ ngày $|r|$ từ 7\% đến dưới 10\%\\
MỚI: Tỷ lệ ngày 7\% $\leq |r| <$ 10\%\\
```
12. Tr. 43: 'cho thí sinh công cụ dùng trong' khó đọc.
```text
CŨ: \frametitle{Phụ lục: bốn công trình cho thí sinh công cụ dùng trong đề tài}
MỚI: \frametitle{Phụ lục: bốn công trình chuẩn bị công cụ cho đề tài}
```
13. Tr. 11: 'so với giao dịch' không rõ đo gì; v14 [mục 4.3.8]: 'vốn hóa lớn so với giá trị giao dịch'.
```text
CŨ: \item Vào VN-Index: cầu tăng nhiều ở mã vốn hóa lớn so với giao dịch
MỚI: \item Vào VN-Index: cầu tăng nhiều ở mã có vốn hóa lớn so với giá trị giao dịch
```
14. Tr. 14: kỳ vọng viết E thường, template dùng \mathbb{E}.
```text
CŨ: E[\varepsilon_{it} \mid D_i, \Post_t, \alpha_i, \tau_t] = 0
MỚI: \mathbb{E}[\varepsilon_{it} \mid D_i, \Post_t, \alpha_i, \tau_t] = 0
```
15. Tr. 21: gạch đầu không nói Ḡ đo gì; viết lại đúng định nghĩa trong khung.
```text
CŨ: \item Đo nhà đầu tư đa dạng hóa thu được bao nhiêu sau chi phí giao dịch, có tính rủi ro
MỚI: \item $\bar{G}$: lợi suất tương đương chắc chắn mất đi khi giữ rổ CS thay vì rổ H, sau chi phí
```
## Không đề xuất sửa (đã cân nhắc)
- Trang bìa chỉ ghi PGS.TS. Hà Hồng Hạnh: người dùng chủ ý (commit c94b1db), v14 mục 10 có GS.TS. Nguyễn Đức Khương; giữ.
- Tài liệu chính dùng allowframebreaks (template =0.8): thử =0.8 sinh trang thứ ba chỉ 2 dòng, nên giữ.
- Tr. 42 có 8 mục (> 7): slide dự phòng, danh mục; giữ.
## Kết quả thử
Áp 15 cặp lên bản sao (scratchpad/vc/t), script xác nhận mỗi CŨ xuất hiện đúng 1 lần. xelatex 2 lượt: 0 lỗi, 0 Overfull, 0 undefined, 43 trang; mọi \hyperlink có nhãn; mọi slide phụ lục có nút quay lại; tiêu đề 1 dòng (pdftotext); caption tr. 33, 40 còn 1 dòng. Phông thêm Fourier-Math-BlackBoard do \mathbb (như template).
