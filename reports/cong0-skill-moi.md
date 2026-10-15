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

## Đợt 2 (2026-10-15): tìm skill nhiều sao theo yêu cầu người dùng

Nguồn danh mục: O0000-code/awesome-academic-skills @ 9142287 (CC0, có ghi giấy phép, số sao và việc gọi mạng của từng skill). Người dùng cho phép cài ("ok kéo đủ… Không cần thì thôi").

| Skill | Nguồn (commit) | Sao | Giấy phép | Quyết định | Lý do |
|---|---|---|---|---|---|
| econ-write | hanlulong/econ-writing-skill @ f2bf7a2 | 569 | MIT | **Cài** | Đã đọc SKILL.md; chỉ có file hướng dẫn, không có script; viết kinh tế học theo Cochrane, McCloskey, Shapiro |
| credible-claims | pedrohcgs/claude-code-my-workflow @ ae72617 | 1.5k | MIT | **Cài** | Đã đọc toàn văn; chống nói quá, tách liên hệ và nhân quả |
| grant-proposal | pedrohcgs @ ae72617 | 1.5k | MIT | Không cài | Chỉ chạy khi người dùng gọi tay; phụ thuộc các skill riêng của kho (interview-me, quality_reports); phần kiểm tra độ khớp đã có ở consistency-checker và research-grants |
| challenge | pedrohcgs @ ae72617 | 1.5k | MIT | Không cài | Cần chạy lưới đặc tả trên dữ liệu; đề cương chưa có dữ liệu |
| econ-audit | eabeam/econ-skills @ 1b0238d | – | CC-BY 4.0 | Không cài | Rà mã Stata/R/Python; đề cương chưa có mã |
| avoid-ai-writing | conorbronsdon/avoid-ai-writing @ 2eec2d4 | 3.5k | MIT | Không cài | Tự ghi chỉ hiệu chỉnh cho tiếng Anh; đề cương viết tiếng Việt |
| stop-slop | hardikpandya/stop-slop | 16.5k | MIT | Không cài | Viết cho văn blog tiếng Anh |
| literature-review (K-Dense writer) | K-Dense-AI/claude-scientific-writer @ 529b9f7 | 2.3k | MIT | Không cài | Gọi OpenRouter/parallel-web, trái S5 |
| humanizer, nature-skills, paperspine | – | 38k/37k/5k | MIT | Không cài | Gọi mạng, trái S5 |

Không bổ sung skill sửa Word: anthropic-skills:docx (anthropics/skills, 172k sao) đã có và là lựa chọn tốt nhất trong danh mục.
Hai skill đã cài nằm trong `.git/info/exclude`, không commit.
