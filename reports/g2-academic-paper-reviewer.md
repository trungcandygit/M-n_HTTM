Xác nhận: luồng chính gọi được công cụ Skill (academic-paper-reviewer), phản hồi "Launching skill: academic-paper-reviewer". Skill cần công cụ Agent nên chạy ở luồng chính theo V7.

# Cổng 2 — academic-paper-reviewer (Imbad0202): KHÔNG QUA (S4), DỪNG

Ngày 2026-10-13. Chế độ: `full` (reviewer_full, 5 ghế + synthesizer).

## Lỗi nguyên văn
SKILL.md, mục "v3.6.2 Sprint Contract Hard Gate", quy định: "All reviewer modes that ship with contracts (`reviewer_full`, `reviewer_methodology_focus`) now run two-call Phase 1 (paper-content-blind) + Phase 2 (paper-visible) orchestration… Templates: `shared/contracts/reviewer/full.json`". Bước 1 của references/sprint_contract_protocol.md §2 yêu cầu: "Load template from `shared/contracts/<domain>/<mode>.json`… Run `check_sprint_contract.py` on the in-memory object; abort on error."

Kết quả chạy bước 1 (nguyên văn):
```
cat: shared/contracts/reviewer/full.json: No such file or directory
cat: ../shared/contracts/reviewer/full.json: No such file or directory
cat: scripts/check_sprint_contract.py: No such file or directory
cat: scripts/check_phase_conformance.py: No such file or directory
cat: scripts/check_panel_synthesis.py: No such file or directory
cat: scripts/review_panel_provenance.py: No such file or directory
cat: scripts/check_acronyms.py: No such file or directory
cat: ../shared/sprint_contract.schema.json: No such file or directory
```
Lệnh `find /` trên toàn máy cũng không thấy các file `full.json` (contracts), `check_phase_conformance.py`, `check_panel_synthesis.py`, `sprint_contract.schema.json` hay `review_panel_provenance.py`.

## Nguyên nhân
Ở Cổng 0, bộ skill của Imbad0202/academic-research-skills (commit d1e51716e53fc371727ea6164dd709fc8ea28c97) chỉ được chép phần thư mục skill: SKILL.md, agents/, references/, templates/, examples/. Thư mục `shared/` (hợp đồng chấm điểm, schema) và `scripts/` (bộ kiểm tra) ở gốc repo không được chép. Theo §11 của protocol, hợp đồng thiếu hoặc không hợp lệ là lỗi loại `[CONTRACT-INVALID]` / exit 2, và phải hủy phiên đánh giá ("abort the editorial round"), không được thử lại.

## Không làm thay
- Không tự soạn hợp đồng: §3 yêu cầu dùng mẫu đã đóng băng; tự soạn là mô phỏng skill, vi phạm S1.
- Không chạy chế độ không có hợp đồng thay cho `full`: SKILL.md coi hợp đồng là "hard gate" của `full`; bỏ qua là rút gọn quy trình, vi phạm S2.
- Không tải `shared/`, `scripts/` từ GitHub: đó là sửa bản cài ngoài phạm vi người dùng đã cho phép, và là tải mã chưa đọc (S5).

## Bằng chứng tuân thủ
| # | Bước (theo SKILL.md / sprint_contract_protocol.md) | Làm? | Ghi chú |
|---|---|---|---|
| 1 | Routing core (Step 0–3) | Làm | Ý định rõ ("full review"), chuyển thẳng tới chế độ full |
| 2 | Chọn chế độ `full` | Làm | Theo yêu cầu người dùng: "đủ các reviewer kể cả Devil's Advocate, và ma trận R&R" |
| 3 | Đọc references/sprint_contract_protocol.md | Làm | Đọc trọn 301 dòng |
| 4 | Protocol §2 bước 1: nạp mẫu hợp đồng + check_sprint_contract.py | THẤT BẠI | Lỗi nguyên văn ở trên |
| 5 | Phase 0 field_analyst → Phase 1 (5 ghế × 2 lượt gọi) → Phase 2 synthesizer → ma trận R&R | CHƯA LÀM | Dừng theo §2/§11 của protocol và theo S4 |

Số file skill đã đọc: SKILL.md, references/sprint_contract_protocol.md, agents/eic_agent.md (một phần, qua grep). Chưa đọc trọn 28 file vì skill dừng ở bước 1.

## Phương án chờ người dùng quyết (không tự làm)
1. (Khuyến nghị) Cho phép chép `shared/` và `scripts/` từ đúng commit đã ghim d1e51716… vào `.claude/` của dự án; đọc từng script trước khi chạy (S5), rồi chạy lại skill.
2. Chạy chế độ khác không cần hợp đồng (`guided` hoặc `quick`). Lưu ý: hai chế độ này không có đủ 5 ghế và ma trận R&R như yêu cầu.
3. Cài lại toàn bộ repo ARS dạng plugin.
