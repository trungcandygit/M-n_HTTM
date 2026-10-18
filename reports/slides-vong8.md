# Slide vòng 8: dựng lại bố cục theo presentation.tex

Tệp đã sửa: `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/v8l/slides.tex` (PDF ở cùng thư mục). Repo chưa bị sửa.
Máy: xelatex 2 lượt, 0 lỗi, 0 overfull/underfull, 43 trang; mọi tiêu đề 1 dòng (pdftotext -bbox); \al ≤ 1/slide; không còn columns, tabularx, \nguon, \appendix; \HH chỉ ở slide giả thuyết. Chưa render ảnh vì CLAUDE.md cấm khi người dùng chưa cho phép; cần người dùng đồng ý thì mới chạy -r 40.

| Frame (tiêu đề rút gọn) | Kiểu slide của template |
|---|---|
| Bìa | \frame{\titlepage} |
| 28/12/2026 toàn bộ HNX sang HOSE | Nested numbered lists + nút (Slide with buttons) |
| Hà Nội chưa có hạng GFCI | Basic table with note |
| Bài toán số 19 | Corollary (khung xám + 3 ý) |
| Hai kênh nối sàn với Hà Nội | Nested lists • – □ |
| Ba câu hỏi, bốn giả thuyết | Nested numbered lists + 2 nút |
| Đóng góp | Nested lists • – □ |
| 4 slide \heading | Generic section |
| Ba giai đoạn | Nested numbered lists + nút (bỏ columns) |
| Chỉ số chất lượng thị trường | Corollary (định nghĩa + 3 ý) |
| Thách thức; Xử lý Amihud | Nested lists |
| Khác biệt kép | Corollary (giả định + 3 ý) |
| Tác động là khoảng cách | Basic figure with note (hinh/did.tex) |
| Mỗi cú sốc trùng thời gian | Nested numbered lists + 2 nút |
| Một sự kiện, bootstrap | Slide with buttons (enumerate + 2 nút; bỏ columns) |
| Lực kiểm định | Basic table with note |
| Điểm yếu lớn nhất | Nested numbered lists + nút |
| Khả năng đầu tư; mô hình GFCI | Corollary (định nghĩa + 3 ý) |
| Kế hoạch khóa trước | Nested lists |
| Mỗi sản phẩm cho Hà Nội | Basic table with note |
| Mỗi kiểu kết quả | Nested numbered lists |
| Bốn công trình đã công bố/chấp nhận | Slide with buttons (Bảng 6, [250]–[252]) |
| Hà Nội có thước đo dùng được | Nested numbered lists |
| Tài liệu chính | Long reference list (allowframebreaks) |
| Dự phòng: mốc pháp lý, Holm, bảy mô hình, theo mức chịu cú sốc | Basic table (with note) + nút quay lại |
| Dự phòng: dữ liệu, sự kiện (math trong item), sai lệch, không phân cụm, khả năng đầu tư | Generic / nested / Slide with math + nút quay lại |
| Dự phòng: ba bước bootstrap, tám bản thảo, công trình dùng cho đề tài | Backup enumerate + "Quay lại slide chính" |

Chuyển xuống slide dự phòng (nối bằng \beamergotobutton, có nút quay lại):
- Bảng tabularx 4 công trình và 8 bản thảo (Bảng 7, [254]–[256]) thành enumerate; bảng "Chuẩn bị" thành dự phòng "bốn công trình cho thí sinh công cụ" (theo [262]).
- Số hiệu TT 57/2021, 69/2023, 139/2025 (slide mở đầu) sang "Mốc pháp lý".
- Cột dữ liệu (ba sàn, GFCI, Čihák, Kaufmann) sang "Dữ liệu ngày và GFCI".
- Ba bước bootstrap sang dự phòng riêng; "theo mức chịu cú sốc là phân tích phụ" chỉ còn ở dự phòng.
- Holm: thay H₁–H₃ bằng tên kiểm định (GFCI, chỉ số chất lượng, Amihud).
- Gộp ý trùng: bỏ "Đối chứng UPCoM là một cận khác" ở dự phòng sai lệch; gộp Sharpe và ngày sự kiện giả vào ý liền trước.
Còn lại: LiberationSans có trong hình did (giống bản cũ); slide "Hai kênh" và "bảy mô hình" sát đáy nhưng không tràn.
