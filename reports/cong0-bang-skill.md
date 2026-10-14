# Cổng 0 — Bảng skill đã cài (ghim commit)

| Skill (name trong frontmatter) | Repo | Commit | Số file trong thư mục skill | Cài được | Đã đọc toàn bộ chưa |
|---|---|---|---|---|---|
| manuscript-writing-review (sciwrite) | labarba/sciwrite | 64b128b88fdaadfd1eb312f42c2ae1475f91b512 | 4 | Có (git clone) | CÓ — 4/4 file (subagent sciwrite, Cổng 2) |
| review-paper | claesbackman/AI-research-feedback | d12975697b8603ec4dd6f0e922fcc1251d5355d1 | 1 | Có | CÓ — 1/1 (luồng chính) |
| review-paper-light | (cùng repo) | (cùng commit) | 1 | Có | CÓ — 1/1 (nạp ở Cổng 1; Cổng 2 không cần vì review-paper đã chạy đủ) |
| review-paper-checks | (cùng repo) | (cùng commit) | 1 | Có | CÓ — 1/1 (luồng chính) |
| review-pap | (cùng repo) | (cùng commit) | 1 | Có | CÓ — 1/1 (luồng chính) |
| peer-review | K-Dense-AI/claude-scientific-writer | 529b9f73ab4b48925027145800d7b49e96ccfd3c | 24 | Có | CÓ — 24/24 (subagent peer-review, kể cả script) |
| research-grants | (cùng repo) | (cùng commit) | 16 | Có | CÓ — 16/16 (subagent research-grants) |
| scientific-writing | (cùng repo) | (cùng commit) | 31 | Có | CHƯA |
| citation-management | (cùng repo) | (cùng commit) | 21 | Có | CHƯA |
| paper-writing (paper-writing-skill) | SNL-UCSB/paper-writing-skill | 676f8520bba54208eb4fe1d41620e365d9af6a24 | 34 | Có | CÓ — 27 file nội dung (subagent red-team; không chạy `setup`; `examples/project_context.md` mà SKILL.md trỏ tới không tồn tại) |
| academic-paper-reviewer | Imbad0202/academic-research-skills | d1e51716e53fc371727ea6164dd709fc8ea28c97 | 28 | Có | ĐÃ ĐỌC (SKILL.md, agents, references, templates dùng cho full) — dừng ở bước 1 (thiếu shared/ và scripts/); đã đọc SKILL.md + sprint_contract_protocol.md |
| academic-paper | (cùng repo) | (cùng commit) | 63 | Có | CHƯA |
| deep-research | (cùng repo) | (cùng commit) | 53 | Có | CHƯA |
| academic-pipeline | (cùng repo) | (cùng commit) | 30 | Có | CHƯA |

Xác nhận repo sciwrite: github.com/labarba/sciwrite (README nêu "Agent Skill for AI-assisted manuscript writing review", 5 pass; tác giả commit "Lorena A. Barba"); trang sourcepulse.org/projects/27915676 là trang tổng hợp trỏ về cùng repo.

Quét an toàn (S5): không thấy chỉ dẫn gửi dữ liệu ra ngoài. Các skill peer-review và scientific-writing còn cấm gửi bản thảo ra dịch vụ ngoài. Có script Python trong citation-management (tra OpenAlex/PubMed/Google Scholar), chưa đọc và chưa chạy.

Cập nhật 2026-10-14 từ số file mà từng subagent/luồng chính báo ở Cổng 2. Các skill không được giao ở Cổng 2 (scientific-writing, citation-management, academic-paper, deep-research, academic-pipeline) vẫn ghi CHƯA.
