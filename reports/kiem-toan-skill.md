# Kiểm toán skill — ghi chép chỉnh sửa bản cài

## Gỡ cờ disable-model-invocation (Bäckman)
Lý do: lệnh trực tiếp của người dùng ("Chọn cách 2..."), sau khi công cụ Skill báo lỗi: `Skill review-pap cannot be used with Skill tool due to disable-model-invocation...`. Chỉ sửa bản cài trong dự án, không sửa repo gốc, không sửa gì khác.

- review-paper/SKILL.md : dòng 6 `disable-model-invocation: true` đã xoá; bản gốc lưu ở review-paper/SKILL.md.bak
- review-paper-light/SKILL.md : dòng 6 `disable-model-invocation: true` đã xoá; bản gốc lưu ở review-paper-light/SKILL.md.bak
- review-paper-checks/SKILL.md : dòng 6 `disable-model-invocation: true` đã xoá; bản gốc lưu ở review-paper-checks/SKILL.md.bak
- review-pap/SKILL.md : dòng 6 `disable-model-invocation: true` đã xoá; bản gốc lưu ở review-pap/SKILL.md.bak

## Kết quả thử lại sau khi gỡ cờ (Cổng 1)
Gọi `Skill review-pap` ngay sau khi sửa file, lỗi nguyên văn:
`Skill review-pap cannot be used with Skill tool due to disable-model-invocation. Ask the user to run /review-pap themselves — it cannot be invoked via the Skill tool. Do not replicate this skill's workflow by other means — it is reserved for explicit user invocation.`
Nhận định: phiên vẫn dùng bản skill nạp lúc khởi động (cờ còn nguyên trong bộ nhớ phiên); cần khởi động lại để nhận thay đổi. Đã dừng theo lệnh người dùng, không mô phỏng.

## Cổng 1 — kiểm tra lại (phiên 2026-10-13, nhánh khởi động claude/quirky-ritchie-evnzw5)
Gọi bằng công cụ Skill ở luồng chính, đối số "CỔNG 1 — CHỈ XÁC NHẬN NẠP ĐƯỢC. KHÔNG thực thi quy trình." Cả 14 skill trả về "Launching skill: <tên>" và nạp nội dung SKILL.md. Không skill nào tự chạy quy trình (không glob, không đọc file, không khởi chạy agent, không chạy script) — V3 đạt.

| Skill gọi | Kết quả | Ghi chú S5 |
|---|---|---|
| review-paper-light | nạp được | — |
| review-paper | nạp được | — |
| review-paper-checks | nạp được | — |
| review-pap | nạp được | — |
| sciwrite (manuscript-writing-review) | nạp được | — |
| peer-review | nạp được | Mục "Citing Scientific Agent Skills" đòi chèn trích dẫn skill vào bản thảo: không phục vụ đề cương → không làm |
| research-grants | nạp được | Bước vẽ hình tuỳ chọn gửi prompt tới OpenRouter (dịch vụ ngoài) → không dùng; mục "Citing" → không làm |
| scientific-writing | nạp được | mục "Citing" → không làm |
| citation-management | nạp được | Script tra OpenAlex/PubMed/Scholar: chưa đọc, không chạy; mục "Citing" → không làm |
| paper-writing-skill (paper-writing) | nạp được | — |
| academic-paper-reviewer | nạp được | Theo dõi cross-model (gửi bản thảo ra nhà cung cấp ngoài) → không bật |
| academic-paper | nạp được | — |
| deep-research | nạp được | — |
| academic-pipeline | nạp được | ARS_AUDIT_ARTIFACT_GATE (gửi ra model ngoài) → không bật |

Kết luận Cổng 1: ĐẠT 14/14.

## Bổ sung shared/ và scripts/ cho academic-paper-reviewer (2026-10-14, người dùng chọn phương án 1)
- Nguồn: github.com/Imbad0202/academic-research-skills, commit d1e51716e53fc371727ea6164dd709fc8ea28c97 (cùng commit đã ghim ở Cổng 0). Chép nguyên vẹn `shared/` (155 file) và `scripts/` (632 file) vào `.claude/ars/`, giữ hai thư mục ngang cấp vì các script tìm `shared/` theo `scripts/../shared`.
- SHA-256 của shared/contracts/reviewer/full.json = e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af, khớp giá trị ghim trong review_panel_provenance.py. `check_sprint_contract.py full.json` → OK (Schema 13.2), có 3 cảnh báo SC-12 chỉ để thông tin.
- S5: chỉ chạy 6 script (check_sprint_contract, check_phase_conformance, check_panel_synthesis, recompute_receipts, review_panel_provenance, check_acronyms). Một subagent đã đọc trọn từng dòng cả 6 script: không truy cập mạng, không gọi subprocess, không đọc biến môi trường, không có eval/exec; chỉ ghi ra đường dẫn do người chạy truyền vào. Kết luận SAFE. Đã kiểm tra: schema không có $ref trỏ ra URL ngoài; trong scripts/ không có file trùng tên module chuẩn. Mọi script đều chạy bằng `python3 -I`. Các script còn lại không chạy.
