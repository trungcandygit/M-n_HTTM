# Trạng thái phiên (V6) — đọc file này đầu tiên khi mở phiên mới

Nhánh: claude/quirky-ritchie-evnzw5 | Repo: PUBLIC (V5: không push ho-so/, outputs/; nội dung trích từ đề cương cũng giữ cục bộ)
Bản vá hiệu lực: V1 (trần 3 vòng, không đếm mục chờ duyệt), V2 (Bước 4 xong trước docx vòng 1), V3, V4, V5, V6, V7.

| Cổng/vòng/bước | Trạng thái | Ghi chú |
|---|---|---|
| Cổng 0 | XONG (phiên trước) | bảng ở cong0-bang-skill.md; cột "đã đọc toàn bộ" chờ số liệu Cổng 2 |
| Cổng 1 | XONG | 14/14 skill gọi được, nạp SKILL.md, không chạy quy trình (V3 đạt). 4 skill Bäckman không còn lỗi disable-model-invocation |
| Cổng 2 | ĐANG CHẠY | Subagent KHÔNG có công cụ Agent -> 4 skill cần agent con (review-paper, review-paper-checks, review-pap, academic-paper-reviewer) dừng đúng S4 trong subagent (báo cáo g2-*.md ghi 'KHÔNG CHẠY ĐƯỢC'). Theo V7 chạy chúng ở LUỒNG CHÍNH (agent con do luồng chính khởi chạy). 4 skill còn lại (sciwrite, paper-writing red-team, peer-review, research-grants) chạy bằng subagent, chờ kết quả |
| Cổng 3 | CHƯA | kiểm toán bằng subagent khác |
| Bước 4 | CHẶN TRƯỚC | 4a: ho-so/ KHÔNG có Quyết định 1193 (chỉ có "2. NQPQ-57-2026.pdf", bản scan, không có text layer, không có tesseract) -> sẽ DỪNG và báo sau Cổng 3 |
| Vòng 1-3 | CHƯA | phụ thuộc Bước 4 (V2) |

## Việc tiếp theo
Chờ 8 subagent Cổng 2 -> cập nhật bảng Cổng 0 -> Cổng 3 -> dừng ở Bước 4a báo người dùng.

## Lỗi / lưu ý
- Repo public: ho-so/de-cuong-goc.docx và NQ 57 đã nằm sẵn trên nhánh từ commit trước (6167125, 32b865a). Cần người dùng quyết định (xóa khỏi lịch sử hoặc chuyển repo private).
- Container ephemeral: file chỉ lưu cục bộ có thể mất khi phiên kết thúc.
