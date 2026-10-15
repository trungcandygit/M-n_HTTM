# Cổng 0 — Kiểm tra skill mới trước khi dùng

Ngày 2026-10-15. Người dùng duyệt dùng các skill này ("kéo hết về, sửa theo").

| Skill | Nguồn (commit) | Giấy phép | Kiểm tra an toàn | Quyết định |
|---|---|---|---|---|
| statistical-power | K-Dense-AI/claude-scientific-skills @ a1043ef5 | MIT (LICENSE.md) | SKILL.md và references đã đối chiếu với nguồn; scripts/power.py, simulate_power.py chưa đọc hết nên KHÔNG chạy | Dùng ở chế độ hướng dẫn |
| fact-checker | franklee16/academic-research-skills @ 9a4b2db2 | Kho không có file LICENSE; frontmatter ghi MIT | Chỉ có SKILL.md; không có mã | Dùng cục bộ, không commit |
| consistency-checker | franklee16 @ 9a4b2db2 | Kho không có file LICENSE | scripts/ xử lý file LaTeX cục bộ (crossref_validator.py import subprocess); đề cương là .docx nên KHÔNG chạy scripts | Dùng checklist, không commit |
| mhe-identification | franklee16 @ 9a4b2db2 | Kho không có file LICENSE | Chỉ cài SKILL.md và references/research; không cài references/sources (trích nguyên văn sách có bản quyền) | Dùng ở chế độ Critic, không commit |

Đối chiếu: nội dung đã cài khớp với mã nguồn gốc; chỗ khác duy nhất là dòng chú thích nguồn gốc mà agent trước thêm vào. Quét mẫu nguy hiểm (curl, wget, requests, subprocess, os.system, eval, exec, rm -rf, token, api key, câu lệnh chèn): chỉ có `import subprocess` trong crossref_validator.py, và script này không được chạy.

Ràng buộc S5 vẫn áp dụng: không gửi nội dung đề cương ra dịch vụ ngoài; không chạy script chưa đọc. Các skill vẫn nằm trong `.git/info/exclude`, không commit lên repo public.
