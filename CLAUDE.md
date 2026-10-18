# Quy tắc làm việc (do người dùng đặt, áp dụng cho mọi phiên)

## Phạm vi và git
- Chỉ làm trên repo `trungcandygit/M-n_HTTM`, nhánh `claude/quirky-ritchie-evnzw5`. Commit và push sau mỗi bước; không tạo PR khi chưa được yêu cầu.
- Không can thiệp bất kỳ repo nào khác. Repo skill bên ngoài chỉ đọc, sao về thư mục tạm.
- Quét secret trước mỗi lần push.

## An toàn và trung thực
- Không gửi câu chữ của đề cương ra dịch vụ ngoài; khi tìm kiếm chỉ dùng từ khóa chung.
- Không bịa trích dẫn, số liệu, DOI. Số minh họa phải ghi rõ "minh họa". Không đưa các số minh họa trong `ban-giao-slide/GHI-CHU.md` (δ = −0,25; Ḡ = 4,66; MQI = 0,3) lên slide như kết quả.
- Không chạy script nào của skill khi chưa đọc hết nó.
- Cổng 0 trước khi cài skill mới: đọc toàn bộ tệp; quét lời gọi mạng, exec, secret; ghi kết quả vào `reports/cong0-skill-moi.md`.
- Không render ảnh (không chuyển PDF thành ảnh để xem) khi người dùng chưa cho phép; kiểm bố cục bằng pdftotext -bbox, pdffonts, log.

## Văn phong và định dạng
- Văn học thuật tiếng Việt, tự nhiên (vina-me, vietnamese-human-writing).
- APA 7: "&" trong ngoặc, "và" ngoài ngoặc.
- Bảng kiểu mặc định, không tô nền xám. Bảng viết tắt 3 cột.
- H₁–H₄, M₁–M₇, K₁–K₄ viết chỉ số dưới.
- Công thức kiểu kinh tế lượng cổ điển: chỉ số dưới không dấu phẩy, không dấu nhân, tham số chữ Hy Lạp, tên biến nhiều chữ viết đứng.
- Tên đề tài giữ nguyên.

## Slide (latex/slides)
- Beamer, XeLaTeX, template pmichaillat/latex-presentation (MIT). Giống template mẫu 100%: phông, cỡ chữ, màu chữ, khoảng cách, cách đặt hình và chú thích (figure/table + \caption xám), khung định lý nền xám, \heading, \lastslide, mức tối giản. Bản gốc template ở repo GitHub pmichaillat/latex-presentation; sty chỉ sửa tối thiểu, đánh dấu [VN].
- Khoảng 30 phút, không ghi chú người nói. Tiêu đề nêu kết luận, nằm trên 1 dòng.
- Ưu tiên thêm phần định tính (cơ chế, trực giác, hàm ý) có nguồn trong đề cương. Chỉ vẽ hình khi thật sự cần; hình vẽ theo kiểu figures.pdf của template (Dark2: #7570b3, #d95f02, #e7298a; nhãn trên đường, không chú giải).
- Chuẩn nội dung: đề cương v14, Shapiro "How to Give an Applied Micro Talk" (`ho-so/tham-khao/`).

## Quy trình rà soát theo vòng
- Tối đa 2 agent chạy cùng lúc, nhưng mỗi agent phải nạp ĐỦ bộ skill mạnh nhất (cả hình thức lẫn nội dung):
  beamer, beamer-check (chỉ phần phân tích log), beamer-presentation, slide-design-principles, latex-econ-model,
  mhe-identification, aer-identification, mostly-harmless-guide, panel-data-guide, review-methodology,
  statistical-power, statistical-analysis, liquidity-measures, review-pap,
  fact-checker, consistency-checker, credible-claims, scientific-critical-thinking,
  vn-legal-verify, citation-management (chỉ kiểm cục bộ), econ-write, vina-me, vietnamese-human-writing, sciwrite.
- Phát hiện chia CRITICAL / MAJOR / MINOR, kèm cặp CŨ/MỚI (MỚI chỉ chứa văn bản thay thế). Agent không sửa repo; main sửa một lần sau khi cả 2 agent xong.
- Chạy các vòng đến khi hết CRITICAL và MAJOR (điểm rubric ≥ 90). Sau mỗi vòng gửi file PDF cho người dùng kiểm tra rồi mới chạy tiếp.
- Cần tài liệu, ảnh hay thứ gì phải cài thì báo người dùng.
