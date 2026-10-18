# Nguồn
- Repo: aspi6246/Claude-Code-Skills-for-Academics, commit 8a8f112, thư mục `beamer-check/`.
- Giấy phép: repo KHÔNG có tệp giấy phép (mặc định tác giả giữ mọi quyền). Cài theo quyết định của người dùng ngày 18/10/2026, chỉ để dùng cá nhân. Nếu repo này chuyển sang công khai, gỡ thư mục `beamer-check/` ra trước.

# Cổng 0
- Đã đọc toàn bộ SKILL.md và scripts/beamer_check.py.
- Script chỉ gọi lệnh cục bộ qua subprocess: pdflatex, pdfinfo, pdftk, pdftoppm, convert (ImageMagick). Không gọi mạng, không đọc khóa API, không xóa file.

# Ghi chú áp dụng
- Script biên dịch bằng pdflatex; bộ slide của dự án dùng XeLaTeX (tiếng Việt). Với bộ slide này, biên dịch bằng xelatex trước rồi chỉ dùng phần phân tích log và kết xuất ảnh, hoặc sửa lệnh trong script thành xelatex trước khi chạy.
