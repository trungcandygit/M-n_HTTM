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

## Cập nhật Cổng 2
- research-grants: XONG (g2-research-grants.md, local-only vì trích đề cương; repo public). 2 NGHIÊM TRỌNG, 9 ĐÁNG SỬA, 3 CHỈNH NHẸ + 3 lỗi thiết kế chờ duyệt. Đã đọc 16 file skill.
- Chạy ở luồng chính (V7): review-paper-checks (agent A,B,C), review-pap (agent 1-6), review-paper (agent 1-8) đang chạy; cần Phase 3 hợp nhất. academic-paper-reviewer chưa bắt đầu.
- Chờ: sciwrite, paper-writing red-team, peer-review.
- Các báo cáo có trích đề cương được loại khỏi git cục bộ (.git/info/exclude), KHÔNG push (V5).

## Phiên 2026-10-13 — DỪNG theo S4 (Cổng 1 kiểm tra lại không qua)
- Phiên mới khởi động trên nhánh claude/upbeat-hopper-eqlt83 (không có .claude/skills/); đã checkout claude/quirky-ritchie-evnzw5 sau khi phiên bắt đầu, nên 14 skill trong repo KHÔNG được đăng ký với công cụ Skill.
- Luồng chính, lỗi nguyên văn: `Unknown skill: review-paper-light`; `Unknown skill: peer-review`; `Unknown skill: manuscript-writing-review`; `Unknown skill: academic-paper-reviewer`.
- Subagent (V7): cùng lỗi `Unknown skill: ...` cho review-paper-light, peer-review, manuscript-writing-review. Không đọc SKILL.md để làm thay.
- Báo cáo local-only của phiên trước (g2-research-grants.md, 4 skill còn lại) KHÔNG còn: container cũ đã bị thu hồi.
- Bước 4a vẫn chặn: ho-so/ chưa có Quyết định 1193; NQ 57 là bản scan không có lớp chữ.
- Việc tiếp theo: mở phiên mới với nhánh khởi động là claude/quirky-ritchie-evnzw5 -> kiểm tra lại Cổng 1 -> chạy lại toàn bộ Cổng 2.
