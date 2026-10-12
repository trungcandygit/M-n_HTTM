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
