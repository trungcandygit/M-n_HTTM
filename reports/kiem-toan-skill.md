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

# Cổng 3 — Kiểm toán tuân thủ, lượt 1 (2026-10-14)
Hai subagent kiểm toán mới, chưa thấy quá trình tạo báo cáo, mở lại từng SKILL.md và đối chiếu từng bước.
| Skill | Kết quả | Bước thiếu |
|---|---|---|
| sciwrite | ĐẠT | — |
| review-paper | KHÔNG ĐẠT | Phase 3: nén 68 MAJOR thành 12 dòng và 139 MINOR thành 5 dòng; Overall Assessment 5 câu; thiếu top 5 |
| review-paper-checks | KHÔNG ĐẠT | Phase 3: Fix List gom khoảng 40 mục; số đếm CRITICAL lệch (2 so với 3); thiếu top 5 |
| review-pap | ĐẠT (lưu ý: Overall Assessment khoảng 6 câu) | — |
| academic-paper-reviewer | KHÔNG ĐẠT | Chưa phát hành revision-roadmap/1.0; lý do "thiếu block manifest" không đứng được |
| paper-writing-skill (red-team) | KHÔNG ĐẠT | Thiếu output grep nguyên văn theo red_team_protocol.md |
| peer-review | ĐẠT | — |
| research-grants | ĐẠT | — |
Đang chạy lại lần 1 cho bốn skill không đạt (tối đa 2 lần).

## Biên bản nhóm A (nguyên văn)
# Cổng 3 — Kiểm toán tuân thủ độc lập (nhóm A)

Người kiểm toán: subagent độc lập, chưa xem quá trình tạo báo cáo. Chỉ dựa trên file.
Ngày: 2026-10-14. Không sửa báo cáo nào.

## Phương pháp
- Đọc trọn SKILL.md của: sciwrite (247 dòng), review-paper (662), review-paper-checks (274), review-pap (514). Ba skill review-* không trỏ tới file references/ hay agents/ nào. Thư mục chỉ có SKILL.md và SKILL.md.bak. sciwrite có thêm HOW-TO-USE/README/LICENSE nhưng SKILL.md không bắt buộc đọc các file này.
- Đối chiếu trích dẫn: dùng script `audit/qcheck.py` để so các chuỗi trong ngoặc kép với `paper/de-cuong-goc.md`, sau khi chuẩn hóa khoảng trắng và `*`. Những chuỗi không khớp được kiểm tay bằng grep. Toàn bộ đều là: (a) chữ trong bảng pandoc bị ngắt cột, (b) LaTeX `$R_{t}$` so với `R~t~`, (c) chữ của hình, có trong `paper/hinh-van-ban.txt`, (d) cụm từ "đã tìm, không thấy", hoặc (e) câu sửa đề xuất, vốn không phải trích dẫn. **Không phát hiện trích dẫn đề cương bịa đặt nào.**
- Đầu ra agent: mọi dòng có nội dung (>20 ký tự) của `agent-out/rp-1..8`, `checks-A..C`, `pap-1..6` đều có mặt nguyên văn trong báo cáo tương ứng (0 dòng thiếu). Bản trong `reports/` trùng khớp với bản gốc trong `paper/reviews/` (diff rỗng).
- Gọi Skill: transcript phiên `ab114070-….jsonl` có các lời gọi Skill `"skill":"sciwrite"` (qua subagent), `review-paper`, `review-paper-checks`, `review-pap` (và `review-paper-light`), cùng phản hồi "Launching skill: …". Dòng xác nhận trong báo cáo là thật.
- Song song và guard: transcript cho thấy 3, 6 và 8 lời gọi Agent `general-purpose`, mỗi nhóm nằm trong **một** tin nhắn (msg_011CfzQchw…, msg_011CfzQhDE…, msg_011CfzQoUH…). Cả 17 prompt mở đầu bằng scope guard nguyên văn. 3 prompt checks có thêm precision guard. Agent 6–8 của review-paper mở đầu bằng "The target journal is top-field." và giữ nguyên `TARGET_JOURNAL` trong thân prompt. Agent 6 của review-pap đã thay thành `OSF`.

---

## 1. sciwrite → g2-sciwrite.md (yêu cầu: đủ 5 pass)

| # | Bước SKILL.md | Kết luận | Bằng chứng |
|---|---|---|---|
| 1 | Chọn mode (full-review mặc định) | ĐẠT | Hàng 1 bảng tuân thủ: "full-review (theo args; cũng là chế độ mặc định)" |
| 2 | Pass 1 Clutter (bảng cụm thừa, cụm mở đầu, redundancy) | ĐẠT | "### Pass 1: Clutter — 8 issues found". Ví dụ 1.1, câu gốc "(quy tắc 1/N) một cách nhất quán", có trong đề cương. Các cụm mở đầu đã tìm và không thấy: grep đề cương cho 0 kết quả, khớp với báo cáo |
| 3 | Pass 2 Voice/Verbs (bị động, danh hóa, bị động chấp nhận được) | ĐẠT | "### Pass 2: Voice and Verbs — 4 issues found". Câu gốc 2.1 "Sự chuẩn bị cho đề tài đến từ các công việc nghiên cứu đã làm." có trong đề cương |
| 4 | Pass 3 Sentence architecture (vị ngữ bị chôn, dấu câu, độ dài câu) | ĐẠT | "### Pass 3 … — 11 issues found". 3.1 "do mô hình chuyển chế độ ước lượng" có trong đề cương |
| 5 | Pass 4 Terminology (Banana, keyword audit 3 bước, acronym) | ĐẠT | "### Pass 4: Terminology — 16 issues found". Hàng 11–15 bảng tuân thủ |
| 6 | Pass 5 Numbers & Citations (N, %, chữ số có nghĩa, Hình↔Bảng, Telephone Game) | ĐẠT (có phần không áp dụng, đã khai) | "### Pass 5 … — 7 issues found". "N ở Tóm tắt" được khai không áp dụng vì đề cương không có tóm tắt. Hình 3 khai CHƯA LÀM được, vì khung #6 rỗng; đã xác minh `hinh-van-ban.txt` không có chữ của Hình 3 |
| 7 | Output format (Summary, Pass 1–5 kèm số lượng, Top 5) | ĐẠT | "### Summary", "### Top 5 Priority Revisions" |
| 8 | Severity CRITICAL/MAJOR/MINOR | ĐẠT | Mỗi mục có thẻ, ví dụ "MAJOR / ĐÁNG SỬA" |
| 9 | Constraints (không đổi nội dung, quy ước ngành, giữ giọng, cụ thể) | ĐẠT | Vấn đề nội dung được tách sang "Vấn đề thiết kế cốt lõi — chờ tác giả duyệt". Việc không hỏi tạp chí đích được khai lý do |
| S3 | Mục "Bằng chứng tuân thủ" đánh số theo bước, có trạng thái, lý do và trích dẫn | ĐẠT | 26 hàng, mỗi hàng có trích dẫn đề cương. Trích dẫn đã spot-check: 83/94 câu "Gốc:" khớp trực tiếp, 11 câu còn lại khớp sau khi kiểm tay (bảng hoặc hình bị ngắt) |
| S2 | Không bỏ, gộp hay rút gọn bước nào mà không khai | ĐẠT | Có mục "Không áp dụng được cho tiếng Việt" gồm 10 điểm, kèm lý do |
| Nguồn | Không bịa nguồn | ĐẠT | Các số chưa đối chiếu được ghi "cần đối chiếu" |
| Skill | Gọi qua công cụ Skill | ĐẠT | Transcript có `"skill":"sciwrite"`; báo cáo có dòng "Launching skill: sciwrite" |

**Kết luận: ĐẠT.**

---

## 2. review-paper → g2-review-paper.md (khai không cần review-paper-light)

| # | Bước SKILL.md | Kết luận | Bằng chứng |
|---|---|---|---|
| P1.a | Phân tích đối số → TARGET_JOURNAL = top-field | ĐẠT | Hàng 1; header "Review Standard: Leading Field Journal" |
| P1.b | Bước 1–7: auto-detect, include-graph, glob hình/bảng, lọc file | ĐẠT | Hàng 2–6. Hai cảnh báo bắt buộc được chép nguyên văn trong "Ghi chú Phase 1" |
| P1.c | Ghi tên đề tài, tác giả, tóm tắt | ĐẠT | Hàng 7, "Không có tóm tắt" |
| P2.a | 8 agent general-purpose trong MỘT tin nhắn | ĐẠT | Transcript msg_011CfzQoUH… có 8 lời gọi Agent |
| P2.b | Scope guard nguyên văn; dòng target journal ở Agent 6–8; giữ logic điều kiện | ĐẠT | Transcript: scope=True ×8; "The target journal is top-field." ở 6/7/8; TARGET_JOURNAL vẫn còn trong thân prompt (5/2/2 lần) |
| A1–A8 | Từng agent chạy đủ mục và đúng format | ĐẠT | rp-1..8 có đủ tiêu đề format. Trích dẫn kiểm được: "có thể lớn hơn ở thị trường phát triển" (dòng 225–226), "không đo rủi ro", "tác động lên rủi ro lựa chọn mô hình" đều có trong đề cương |
| P3.a | Kiểm tra agent lỗi hoặc placeholder | ĐẠT | Hàng 19; cả 8 file agent-out đều đầy đủ |
| P3.b | Lưu reviews/PRE_SUBMISSION_REVIEW_[ngày].md, kiểm tra -v2 | ĐẠT | File tồn tại và trùng nội dung báo cáo |
| P3.c | Overall Assessment: 3–4 câu; câu (3) = mục CRITICAL đứng đầu Priority list | KHÔNG ĐẠT (nhẹ) | Đoạn này có 5 câu. Câu "Vấn đề nghiêm trọng nhất là công suất…" ứng với Priority #2 (A6-Required 1), trong khi Priority #1 là "[Khoảng trống đóng góp]". Không khai sai lệch |
| P3.d | Contribution Rating; Recommendation chép nguyên văn A6 Part 4 | ĐẠT | "Revise before sending to referees" khớp rp-6 dòng 131. Hạng "Incremental"/"Insufficient…" khớp rp-7 và rp-8 |
| P3.e | Phần 1–7 chép nguyên văn đầu ra agent | ĐẠT | 0 dòng thiếu |
| P3.f | Synthesis (chỗ đồng ý, điểm tranh chấp, không lấy trung bình, câu caveat) | ĐẠT | Có câu "Novelty relative to literature not cited in the paper has not been verified." |
| P3.g | Priority Action Items: "Collect all tagged items … and rank them" | **KHÔNG ĐẠT** | CRITICAL có đủ 11 mục (A1 3, A2 3, A6 5, cộng mục khoảng trống đóng góp); "[A1-C3; A2-C1]" là gộp trùng hợp lệ. Nhưng 68 mục MAJOR (A1 13, A2 11, A3 19, A4 11, A5 9, A6 5) bị nén thành 12 dòng (12–23), và 139 mục MINOR thành 5 dòng (24–28), mỗi dòng gom cả một agent, ví dụ "19. [A2] Tiêu chí H3 …; H4 …; K=3 chế độ; …". Bảng tuân thủ (hàng 24) ghi "Làm" mà không khai việc rút gọn |
| P3.h | Báo người dùng 5 mục | KHÔNG KIỂM CHỨNG ĐƯỢC từ file | Hàng 25 ghi "tóm tắt ở tin nhắn cuối phiên". Báo cáo có đường dẫn, khuyến nghị, số đếm và ghi chú file bị loại, nhưng không có danh sách "top 5" riêng |
| S3 | Bằng chứng tuân thủ đánh số theo bước | ĐẠT (lưu ý) | 25 hàng. Các hàng thủ tục (1–10, 19–25) không có trích dẫn đề cương; điều này chấp nhận được vì đó là bước kỹ thuật |
| S2 | Không bỏ, gộp hay rút gọn mà không khai | **KHÔNG ĐẠT** | Xem P3.g và P3.c |
| Nguồn | Không bịa nguồn | ĐẠT | Nguồn ngoài đề cương có nhãn `[UNVERIFIED …]` (rp-6, rp-8) |
| Skill | Gọi qua công cụ Skill | ĐẠT | Transcript `"skill":"review-paper"`. Có gọi review-paper-light nhưng báo cáo khai không cần dùng fallback |

**Kết luận: KHÔNG ĐẠT** (lỗi khu trú ở Phase 3, không cần chạy lại agent).
Bước phải làm lại:
1. Phase 3 — **Priority Action Items**: liệt kê riêng và xếp hạng từng mục [MAJOR] và [MINOR] của Agent 1–6 theo triage hierarchy, lấy từ `agent-out/rp-1..6`. Nếu vẫn gộp thì phải khai lý do gộp trong bảng tuân thủ.
2. Phase 3 — **Overall Assessment**: viết lại trong 3–4 câu, câu (3) lấy đúng mục CRITICAL đứng đầu Priority list. Nếu giữ cách hiện tại thì phải khai sai lệch.
3. Bổ sung "top 5 priority items" vào phần báo người dùng (hàng 25), hoặc dẫn tới chỗ có thể kiểm chứng.

---

## 3. review-paper-checks → g2-review-paper-checks.md

| # | Bước SKILL.md | Kết luận | Bằng chứng |
|---|---|---|---|
| P1.1–6 | Đường dẫn, include-graph, file thành phần, bảng, bib, tên/tác giả/tóm tắt | ĐẠT | Hàng 1–6. Cảnh báo "No table .tex files…" chép nguyên văn. "11. Danh mục tài liệu tham khảo" có trong đề cương (dòng 1161) |
| P2.a | 3 agent general-purpose trong MỘT tin nhắn | ĐẠT | Transcript msg_011CfzQchw… có 3 lời gọi |
| P2.b | Scope guard và precision guard nguyên văn ở cả 3 prompt | ĐẠT | Transcript: scope=True, prec=True ×3 |
| A/B/C | Mục kiểm tra và format | ĐẠT | checks-A/B/C đủ tiêu đề. Trích dẫn "Đại học Kinh tế Quốc Dân", "loại cơ chế (ii) và (iii) khỏi", "thanh khoản cạn làm" (Bảng 2, dòng 460) đều có trong đề cương. Các mục US/UK và số < 10 khai không áp dụng |
| P3.a | Kiểm tra agent lỗi | ĐẠT | Hàng 13 |
| P3.b | Khử trùng lặp, báo một lần và ghi góc nhìn còn lại | ĐẠT | Summary liệt kê 7 nhóm (a)–(g) |
| P3.c | Lưu reviews/PAPER_CHECK_[ngày].md | ĐẠT | File tồn tại và trùng nội dung |
| P3.d | Cấu trúc (Summary, Counts, 1-2-3) | ĐẠT | Các phần 1–3 chép nguyên văn; 0 dòng thiếu |
| P3.e | Fix List: "Collect every tagged item … Each line must be actionable on its own — location, the problem, and the fix" | **KHÔNG ĐẠT** | Dòng 23 gom A-3…7 cùng A style-1. Dòng 24–26 gom toàn bộ khoảng 40 mục MINOR thành 3 dòng, ví dụ "24. Các mục MINOR của A (style 2–12, recurring 2–6): …". Các dòng này thiếu vị trí và cách sửa cho từng mục. Không khai lý do rút gọn |
| P3.f | Xếp hạng CRITICAL | ĐẠT có lưu ý | Mục 1 do Agent C gắn MAJOR nhưng được nâng lên CRITICAL. Việc này đã khai, nhưng skill chỉ yêu cầu xếp thứ tự, không yêu cầu đổi thẻ. Hệ quả là Counts ghi "2 CRITICAL" còn Fix List có 3 CRITICAL, không nhất quán |
| P3.g | Báo người dùng 4 mục; đề nghị sửa nhưng không tự sửa | ĐẠT một phần, KHÔNG KIỂM CHỨNG ĐƯỢC top 5 | Có mục "Không chạy được hoặc giới hạn" và số đếm theo nhóm. Top 5 nằm ở tin nhắn cuối phiên, không có trong file |
| S3 | Bằng chứng tuân thủ | ĐẠT | 18 hàng, có trích dẫn đề cương ở các hàng nội dung |
| S2 | Không gộp hay rút gọn mà không khai | **KHÔNG ĐẠT** | Xem P3.e |
| Nguồn | Không bịa nguồn | ĐẠT | — |
| Skill | Gọi qua công cụ Skill | ĐẠT | Transcript `"skill":"review-paper-checks"` |

**Kết luận: KHÔNG ĐẠT** (lỗi khu trú ở Phase 3).
Bước phải làm lại:
1. Phase 3 — **Fix List**: liệt kê riêng từng mục được gắn thẻ (A 2/7/16, B 0/9/13, C 0/19/11), mỗi dòng có vị trí, vấn đề và cách sửa. Phần gộp chỉ dành cho các cặp trùng (a)–(g) đã khai.
2. Làm cho Counts khớp với Fix List: giữ thẻ gốc của agent, hoặc ghi rõ "2 CRITICAL gốc + 1 nâng hạng" ở cả hai chỗ.
3. Đưa top 5 vào phần báo người dùng, ở chỗ có thể kiểm chứng.

---

## 4. review-pap → g2-review-pap.md (áp cho kế hoạch đăng ký trước và phương pháp)

| # | Bước SKILL.md | Kết luận | Bằng chứng |
|---|---|---|---|
| P1.a | Phân tích đối số → TARGET_REGISTRY = OSF | ĐẠT | "đăng ký trước kế hoạch phân tích trên nền tảng OSF Registries" có trong đề cương |
| P1.b | Kiểm tra đường dẫn là PAP chính (fallback nếu không phải) | ĐẠT | Hàng 2 |
| P1.4–6 | Tài liệu hỗ trợ, tìm theo mẫu tên, kiểm kê, ghi danh mục thiếu | ĐẠT | Mục File Inventory nêu thiếu năm nhóm, có ghi "không áp dụng" khi phù hợp |
| P2.a | 6 agent general-purpose trong MỘT tin nhắn | ĐẠT | Transcript msg_011CfzQhDE… có 6 lời gọi |
| P2.b | Scope guard nguyên văn; thay TARGET_REGISTRY ở Agent 6 | ĐẠT | Transcript: scope=True ×6; Agent 6 có "appropriate to `OSF`", không còn chuỗi TARGET_REGISTRY |
| A1–A6 | Mục kiểm tra, thẻ và format | ĐẠT | pap-1..6 đủ tiêu đề. Trích dẫn "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10", "khoảng 28 cửa sổ đánh giá độc lập", "một nhà cung cấp dữ liệu thương mại", "biện minh chúng sau khi ước lượng thử", "Quý 2: ước lượng thử bảy mô hình … 2019--2025" (Bảng 5, dòng 951–952) đều có trong đề cương. Agent 6 Part 1 ghi "Borderline — cần sửa đổi đáng kể" |
| P3.a | Lưu reviews/PAP_REVIEW_[ngày].md | ĐẠT | File tồn tại và trùng nội dung |
| P3.b | Cấu trúc và thứ tự (Inventory, Overall, Recommendation, Priority, A6, A2, A3, A4, A5, A1) | ĐẠT | Thứ tự tiêu đề khớp; agent chép nguyên văn, 0 dòng thiếu |
| P3.c | Overall Assessment 3–4 câu | KHÔNG ĐẠT (rất nhẹ) | Đoạn này có khoảng 6 câu. Nội dung đủ ba ý bắt buộc |
| P3.d | Recommendation ánh xạ từ hạng A6 (Borderline → Substantial revision required) | ĐẠT | "Substantial revision required" |
| P3.e | Priority theo triage (3/6 > 4 > 2 > 5 > 1; trong mỗi agent C > M > m) | ĐẠT | Cả 23 mục CRITICAL của agent đều có mặt, kèm mã nguồn. Có khai việc gộp trùng ("Các mục trùng … được gộp và ghi nguồn"). Skill không bắt liệt kê mọi mục |
| P3.f | Báo người dùng 4 mục | KHÔNG KIỂM CHỨNG ĐƯỢC top 5 từ file | Hàng 19; số đếm có ghi |
| S3 | Bằng chứng tuân thủ | ĐẠT | 19 hàng, có trích dẫn đề cương ở các hàng nội dung |
| S2 | Không gộp hay bỏ mà không khai | ĐẠT | Việc gộp đã khai |
| Nguồn | Không bịa nguồn | ĐẠT | — |
| Skill | Gọi qua công cụ Skill | ĐẠT | Transcript `"skill":"review-pap"` |

**Kết luận: ĐẠT** (lưu ý nhỏ: Overall Assessment dài hơn 3–4 câu; nên rút gọn hoặc khai sai lệch, không cần chạy lại).

---

## Tổng hợp
| Skill | Kết luận | Bước phải làm lại |
|---|---|---|
| sciwrite | ĐẠT | — |
| review-paper | KHÔNG ĐẠT | Phase 3: Priority Action Items (liệt kê riêng từng MAJOR/MINOR hoặc khai lý do gộp); Overall Assessment (3–4 câu, câu 3 = CRITICAL #1); top 5 cho người dùng |
| review-paper-checks | KHÔNG ĐẠT | Phase 3: Fix List (mỗi mục một dòng có vị trí, vấn đề, cách sửa); làm Counts khớp với việc nâng hạng; top 5 cho người dùng |
| review-pap | ĐẠT | (khuyến nghị) rút Overall Assessment về 3–4 câu hoặc khai sai lệch |

## Biên bản nhóm B (nguyên văn)
# Cổng 3 — Kiểm toán tuân thủ độc lập (nhóm B)

Ngày 2026-10-14. Người kiểm toán chưa thấy quá trình tạo báo cáo và chỉ xét trên file. Không báo cáo nào bị sửa.

Phương pháp:
- Đọc trọn SKILL.md của từng skill, cùng các file mà SKILL.md nói là bắt buộc cho chế độ đang chạy: `agents/editorial_synthesizer_agent.md` (Step 5) của APR, `red_team_protocol.md` và `gate_mechanical.md` Part C của paper-writing.
- Đối chiếu từng bước với báo cáo.
- Chạy lại các checker ở chế độ chỉ đọc.
- Kiểm tra câu trích từ đề cương bằng cách so khớp với `scratchpad/paper/de-cuong-goc.md` sau khi gộp dòng (đặt ở `scratchpad/norm.txt`; chỉ là bản sao để so khớp).

Tổng số câu trích đã kiểm: 52.
- 50 câu khớp nguyên văn.
- 2 câu chỉ khác định dạng markdown, chấp nhận được: `**NGUYỄN VĂN TRUNG**`, `M~5~`.
- 1 câu trích bị lược chữ mà không đánh dấu (APR, xem dưới).

Không phát hiện nguồn bịa. Mọi trích dẫn tác giả–năm trong 4 báo cáo đều có trong đề cương. Riêng "Ledoit–Wolf (2008)" là cách viết khác của "Ledoit và Wolf (2008)", và nguồn này có trong đề cương.

---

## 1. academic-paper-reviewer (chế độ `full`) → `reports/g2-academic-paper-reviewer.md`

Xác nhận gọi skill: dòng 1, "Launching skill: academic-paper-reviewer". ĐẠT.

### Kiểm chứng lại bằng checker (chỉ đọc, chạy từ `.claude/ars`)
| Lệnh | Kết quả |
|---|---|
| `check_sprint_contract.py apr/contract.json` | OK, Schema 13.2 (2 cảnh báo SC-12: D2 và D6 mỗi chiều chỉ có một ghế chấm) |
| `check_phase_conformance.py --phase2` × 5 vai (eic, methodology, domain, perspective, da) | exit 0 cả 5, `PHASE-CONFORMANCE: PASS`. Riêng methodology có `[RECEIPT-ATTESTATION: declaration-only]` |
| `check_panel_synthesis.py --synthesis apr/synthesis.md` (5 báo cáo, roles theo thứ tự) | `PANEL-SYNTHESIS: PASS`, exit 0 |
| sha256 `artifacts/panel-provenance.json` | `f1e0e677…73d0`, khớp carrier và thư quyết định |

### Bảng bước
| # | Bước (SKILL.md / file bắt buộc) | Kết luận | Bằng chứng |
|---|---|---|---|
| 1 | Routing: "review" → `full` | ĐẠT | Dòng 5: "Chế độ `full` (hợp đồng `reviewer/reviewer_full/v2`…)" |
| 2 | Sprint Contract Hard Gate: nạp `full.json`, chạy `check_sprint_contract` | ĐẠT | Đã chạy lại, kết quả OK |
| 3 | Phase 0: field_analyst đọc trọn bài, lập 4 thẻ, DA là ghế thứ 5 cố định | ĐẠT | `apr/phase0_field_analysis.md` (đọc dòng 1–1385); có mục Target Journal ghi `criteria_binding_unavailable` |
| 4 | Checkpoint 1: trình thẻ cấu hình cho người dùng | ĐẠT (có khai lý do) | Dòng 27: "Người dùng dặn 'làm đi chuẩn theo các skill, không hỏi lại'" |
| 5 | Phase 1: 5 ghế làm paper-blind, song song | ĐẠT | `phase1_*.md` × 5. Dòng 28: `--phase1-only` exit 0 |
| 6 | Phase 2: paper-visible cho từng ghế | ĐẠT | Đã chạy lại `--phase2`, 5/5 PASS |
| 7 | Iron Rule 2: provenance 6 trục, công bố lỗi tương quan, không tuyên bố "độc lập" | ĐẠT | Dòng 129–148 có bảng seat/context ID/model family, và câu "Correlated-error disclosure: All model-executed review seats used one model family" |
| 8 | Định dạng riêng của DA (Strongest Counter-Argument, CRITICAL/MAJOR/MINOR, giải thích thay thế, bên liên quan) | ĐẠT | `phase2_da.md` dòng 38 "Phản luận mạnh nhất", dòng 40, 42, 48–52 |
| 9 | Synthesizer: giao thức 3 bước, audit lines | ĐẠT | Dòng 64–99. Checker đã chạy lại: PASS |
| 10 | Iron Rule 3: không bịa nhận xét, mỗi mục dẫn về ghế | ĐẠT | Step 1b (dòng 197–265); mỗi REV có cột Source |
| 11 | Iron Rule 4: phân xử DA CRITICAL | ĐẠT | Dòng 316–318. Bảng CRITICAL của DA trống (đã kiểm `phase2_da.md` dòng 48–50) |
| 12 | Iron Rule 6: không sửa bản thảo | ĐẠT | Dòng 35 |
| 13 | #684 ràng buộc tiêu chí: `criteria_binding_unavailable` cho cả 5 ghế | ĐẠT | Dòng 54–58 |
| 14 | #518 cross-model | KHÔNG ÁP DỤNG | `ARS_CROSS_MODEL` không được đặt (dòng 101) |
| 15 | #849 kiểm tra từ viết tắt, đặt cuối thư quyết định | ĐẠT | Dòng 641 trở đi. Hạn chế ngôn ngữ (vi) đã được khai |
| 16 | **Step 5 (`editorial_synthesizer_agent.md`): phát hành `revision-roadmap/1.0` theo `revision_roadmap.schema.json`, mỗi mục có `proposed_targets[]` lấy block id từ block manifest** | **KHÔNG ĐẠT** | Dòng 39: "CHƯA LÀM — Thiếu block manifest và base_draft_sha256". Có khai lý do, nhưng lý do không đứng được. (a) `base_draft_sha256` tính được trực tiếp từ `manuscript.md`. (b) Block manifest tạo được bằng `scripts/ars_anchorize_draft.py --manifest-out …` chạy trên **bản sao** của manuscript, nên vẫn giữ Iron Rule 6. (c) Token `[BLOCK-MANIFEST-UNAVAILABLE]` không có trong skill, `shared/` hay `scripts/`, tức không phải nhánh dự phòng được skill cho phép |
| 17 | Lộ trình sửa đổi (bản người đọc) + ma trận R&R | ĐẠT | 49 dòng REV trong Phụ lục B (đã đếm); 12 câu hỏi |
| 18 | Phase 2.5 Revision Coaching | ĐẠT (bỏ qua hợp lệ) | SKILL.md cho phép: "User can say 'just fix it' to skip guidance". Dòng 40 đã khai lý do |
| 19 | Quy tắc người dùng S3: mục "Bằng chứng tuân thủ" có đánh số bước và câu trích | ĐẠT một phần | Có bảng (dòng 22–40) và 3 câu trích (dòng 42), nhưng các dòng **không đánh số**. Câu trích "ước lượng thử bảy mô hình trên giai đoạn 2019--2025" (dòng 42, 166, 349) **lược mất "chuyên đề 1"** mà không có dấu "…". Nguyên văn đề cương: "ước lượng thử bảy mô hình trên chuyên đề 1 giai đoạn 2019--2025" |
| 20 | S2: không bỏ, gộp hay rút gọn bước mà không khai | ĐẠT | Các bước CHƯA LÀM hay KHÔNG ÁP DỤNG đều có lý do |

**Kết luận: KHÔNG ĐẠT.**

Các bước phải chạy lại:
1. Chép `apr/manuscript.md` sang một bản sao, rồi chạy `ars_anchorize_draft.py <bản sao> --manifest-out apr/block-manifest.json`. Không chạy trên `manuscript.md` gốc.
2. Tính `base_draft_sha256` và `block_manifest_sha256`. Phát hành `apr/revision-roadmap.json` (`schema_version: revision-roadmap/1.0`) gồm 49 mục theo thứ tự nguồn, mỗi mục có `proposed_targets[]` là block id và operation được phép.
3. Chạy `python3 -I -B scripts/revision_roadmap.py validate-roadmap --base <bản sao> --block-manifest apr/block-manifest.json apr/revision-roadmap.json` và dán output vào báo cáo.
4. Thay `[BLOCK-MANIFEST-UNAVAILABLE]` trong Required/Suggested Revisions bằng block id thật. Chạy lại `check_panel_synthesis.py --synthesis` (phải PASS). Gắn lại kết quả kiểm tra từ viết tắt #849 làm phần ghi cuối cùng.
5. Sửa câu trích Bảng 5 thành nguyên văn, có "chuyên đề 1". Đánh số các dòng của bảng "Bằng chứng tuân thủ".

---

## 2. paper-writing-skill (red-team) → `reports/g2-paper-writing-redteam.md`

Xác nhận gọi skill: dòng 1, "Launching skill: paper-writing-skill". ĐẠT.

### Bảng bước (`red_team_protocol.md` + các mục MUST của SKILL.md)
| # | Bước | Kết luận | Bằng chứng |
|---|---|---|---|
| 1 | When: chạy sau gate của tác giả, trước khi trình | ĐẠT | §6.1 dòng 1 |
| 2 | Gate 1 WRITE (tác giả) | KHÔNG ÁP DỤNG | Văn bản đã có sẵn |
| 3 | Gate 2 MECHANICAL phía tác giả | KHÔNG ÁP DỤNG (khai đúng) | Reviewer không được xem self-assessment của tác giả |
| 4 | Gate 3: reviewer tự chạy lại grep `gate_mechanical.md` (M1–M18) | ĐẠT | §1, bảng M1–M18 có số đếm. Script ở `scratchpad/g2rt/` (`g.sh`, `gate.py`, `rules.py`) |
| 5 | **Evidence rule / Gate 2: "PASTE the raw output (hit counts + lines)… 'Audited' without pasted output is INVALID"** | **KHÔNG ĐẠT** | §1 chỉ có bảng tóm tắt: số đếm kèm 1–3 dòng ví dụ cho mỗi mã. Ví dụ M11 có "26 (25 câu)" nhưng chỉ dẫn 3 dòng, M12 có "40 (37 câu)" nhưng chỉ dẫn 2 dòng, M2 có 15 câu nhưng chỉ dẫn 3. Output thô của grep (toàn bộ các dòng trúng) không được dán. `g.sh` có in đủ danh sách nhưng báo cáo không chép lại |
| 6 | Áp `gate_semantic.md` S1–S31 với lăng kính người đọc mới | ĐẠT | §2 đủ 31 mục |
| 7 | Nhất quán từ vựng và phân rã, không trùng lặp, định vị trung thực, nói thẳng danh từ | ĐẠT | S8, S9, S10, S12, S21 |
| 8 | Săn 4 lớp lỗi (giọng máy, khó tiếp cận, thiếu mạch lạc, phi logic) | ĐẠT | Mục "Bốn lớp lỗi phải săn" |
| 9 | Danh sách phát hiện có mã quy tắc, dòng, cách sửa; không trả yes/no | ĐẠT | §3: 4 C, 21 J, 25 m. Ví dụ "C1. [S21, S18] … Vị trí: L275–276"; câu trích đã kiểm là có thật |
| 10 | Reviewer tách biệt, không xem self-assessment | ĐẠT (theo lời khai) | Dòng 7 |
| 11 | Vòng sửa và closure (S31) đến khi clean | CHƯA LÀM (có khai) | §4 "CHƯA CLEAN"; lý do: cấm sửa đề cương. Báo cáo không tuyên bố clean, nên đúng với evidence rule |
| 12 | SKILL.md MUST 1–7 (đọc author_profile, project_context, brainstorming, artifact anh em) | ĐẠT (các bước không làm đều có khai lý do) | §6.2. Đã kiểm: `examples/project_context.md` đúng là không tồn tại |
| 13 | Review mode: intervention_types theo thứ tự, mức độ + số nguyên tắc | ĐẠT | §6.2 |
| 14 | Section checklists / rhetorical moves | ĐẠT | §6.2, quy đổi mục |
| 15 | S3: "Bằng chứng tuân thủ" đánh số, có câu trích | ĐẠT | §6.1 đánh số 1–11; câu trích khớp đề cương (11/11 câu đã kiểm) |
| 16 | S2: không bỏ hay gộp mà không khai | ĐẠT | Loop mode, figure spec, compression: đều có lý do |

**Kết luận: KHÔNG ĐẠT.** Chỉ thiếu bước 5 (evidence rule).

Các bước phải chạy lại:
1. Chạy lại `scratchpad/g2rt/g.sh`, `gate.py` và `rules.py` trên dòng 155–1160, cho từng mã M1–M18 và cho độ dài câu.
2. Dán **nguyên văn output thô** (mọi dòng trúng, có số dòng) vào một phụ lục của báo cáo. Ghi rõ dòng nào là dương tính giả, ví dụ "được" mang nghĩa khả năng, hay "cộng sự".
3. Đối chiếu lại số đếm trong bảng §1 với output thô.

---

## 3. peer-review → `reports/g2-peer-review.md`

Xác nhận gọi skill: dòng 1, "Launching skill: peer-review". ĐẠT.

### Kiểm chứng lại bằng script (chỉ đọc, chạy từ thư mục skill)
| Lệnh | Kết quả |
|---|---|
| `validate_review_intake.py W/completed-intake.json` | exit 0, errors [] |
| `validate_claim_evidence.py W/local-claim-matrix.csv` | exit 0 |
| `audit_statistics_reproducibility.py …json` | errors [] |
| `lint_review.py reports/g2-peer-review.md` | exit 0, channel_separation author_before_editor true |

(`W/` = `scratchpad/peer-review/`; đủ các file intake, claim, stats, citation, lint đã nêu.)

### Bảng bước
| # | Bước SKILL.md | Kết luận | Bằng chứng |
|---|---|---|---|
| S1–S4 | Safety boundary: ủy quyền, chính sách venue, xung đột và năng lực, xử lý cục bộ | ĐẠT (S2 một phần, có khai) | Bảng tuân thủ S1–S4. Chưa đọc được quy định AI của trường vì không dùng mạng |
| S5 | Danh sách "Never" | ĐẠT | Không gọi skill khác; lint 0 lỗi EDITORIAL_DECISION |
| S6 | Đọc `ethical_review_practice.md` trước khi xử lý | ĐẠT (theo lời khai) | Danh sách 24 file |
| S7/C8 | Xóa hoặc lưu giữ bản phái sinh | CHƯA LÀM (có khai) | Đợi tác giả xác nhận; đã ghi trong intake |
| H1/H2 | Nhãn bản nháp; trách nhiệm của con người | ĐẠT / CHƯA LÀM (thuộc tác giả) | Dòng 3 "BẢN NHÁP LÀM VIỆC" |
| G | Intake gate → READY_FOR_LOCAL_REVIEW | ĐẠT | Đã chạy lại, exit 0 |
| 1 | Phạm vi và bằng chứng có sẵn | ĐẠT | Câu trích khớp |
| 2 | Tóm tắt trung lập, không ra quyết định | ĐẠT | "Tóm tắt trung lập" |
| 3 | Chọn hướng dẫn báo cáo | ĐẠT; 3b KHÔNG ÁP DỤNG (có khai) | `NO_BUNDLED_GUIDELINE_MATCH` |
| 4 | Ma trận tuyên bố–bằng chứng | ĐẠT | Đã chạy lại, exit 0 |
| 5 | Phương pháp và thống kê theo 9 mục | ĐẠT | Script chạy lại, errors [] |
| 6 | Tái lập và minh bạch | ĐẠT (mức kế hoạch) | Không tuyên bố đã tái lập |
| 7 | Đạo đức và liêm chính | ĐẠT | |
| 8a | Hình và bảng | ĐẠT một phần (có khai) | Hình 3 không trích được chữ |
| 8b | `audit_citations.py` | ĐẠT | Có bản phái sinh khóa cục bộ; 56/56 nguồn |
| 9 | Scaffold; mỗi góp ý có đủ 5 trường | ĐẠT | 18 major + 12 minor; lint báo 0 ACTIONABILITY_FIELD_EMPTY |
| 10 | Tách kênh | ĐẠT | Lint: author_before_editor true |
| 11 | Lint và hoàn thiện; checklist trước bàn giao C1–C7 | ĐẠT | Phụ lục A, nguyên văn A1–A4 |
| X | Mục "Citing Scientific Agent Skills" | Bỏ qua có khai | Theo chỉ thị |
| — | S3: "Bằng chứng tuân thủ" đánh số, có câu trích | ĐẠT | Đánh số S1…C8; 12/12 câu trích đã kiểm là có thật (2 câu chỉ khác định dạng markdown) |

**Kết luận: ĐẠT.** Không có bước nào phải chạy lại. Lưu ý không chặn: các bước quy trình (S6, H1, 9–11) ghi "n/a" ở cột câu trích, điều này hợp lý vì chúng không gắn với nội dung đề cương.

---

## 4. research-grants → `reports/g2-research-grants.md`

Xác nhận gọi skill: dòng 1, "Launching skill: research-grants". ĐẠT.

### Bảng bước
| # | Mục SKILL.md | Kết luận | Bằng chứng |
|---|---|---|---|
| 1 | Overview / When to Use | ĐẠT | Mục H |
| 2 | Visual Enhancement (tùy chọn) | KHÔNG ÁP DỤNG (có khai) | Gửi dữ liệu ra OpenRouter, vi phạm S5 |
| 3 | Agency-Specific Overview (NSF, NIH, DOE, DARPA, NSTC) | ĐẠT | Mục E: từng cơ quan, ghi rõ "không áp dụng trực tiếp" |
| 4 | Core Components (core_components.md: aims, significance, innovation, approach, preliminary, timeline, budget, biosketch, facilities, DMP, broader impacts, summary) | ĐẠT | B1–B12, C1–C5 |
| 5 | Review Criteria | ĐẠT | Mục E |
| 6 | Writing Principles, Proposal Types and Resubmission | ĐẠT | Mục H |
| 7 | Common Mistakes (5 nhóm × 5 mục) | ĐẠT | Mục F, đủ 25 mục |
| 8 | Workflow Phase 1–5 | ĐẠT | Mục G |
| 9 | Integration with Other Skills | CHƯA LÀM (có khai) | Phạm vi Cổng 2 chỉ cho một skill |
| 10 | Resources (7 references) + Templates (3 mẫu) | ĐẠT | Đã đọc 16 file; mẫu dùng cho C1, B1, B3; không chép số liệu mẫu |
| 11 | Không bịa ngân sách hay tiêu chí cơ quan tài trợ | ĐẠT | Ghi [CẦN TÁC GIẢ CUNG CẤP] cho NQ 57/2026 và QĐ 1193 |
| 12 | Citing Scientific Agent Skills | Bỏ qua có khai | |
| 13 | S3: "Bằng chứng tuân thủ" theo thứ tự SKILL.md, có câu trích | ĐẠT (lưu ý nhỏ) | Mục H theo đúng thứ tự SKILL.md; 17/17 câu trích đã kiểm là có thật. Các dòng gọi theo tên mục (Phase 1–5, Common Mistakes 1–5), **không có cột số thứ tự** |
| 14 | S2 | ĐẠT | Mọi mục CHƯA LÀM hay không áp dụng đều có lý do |

**Kết luận: ĐẠT.** Không có bước nào phải chạy lại. Lưu ý không chặn: nên thêm cột số thứ tự cho mục H để khớp hẳn yêu cầu "đánh số" của S3.

---

## Tổng hợp
| Skill | Kết luận | Bước phải chạy lại |
|---|---|---|
| academic-paper-reviewer | KHÔNG ĐẠT | Step 5: anchorize bản sao → block manifest + sha → phát hành `revision-roadmap/1.0` → `revision_roadmap.py validate-roadmap` → thay `[BLOCK-MANIFEST-UNAVAILABLE]`, chạy lại `check_panel_synthesis`, gắn lại #849. Sửa câu trích Bảng 5 ("chuyên đề 1"); đánh số bảng tuân thủ |
| paper-writing-skill (red-team) | KHÔNG ĐẠT | Evidence rule: dán nguyên văn output thô của grep M1–M18 (mọi dòng trúng) và đối chiếu số đếm |
| peer-review | ĐẠT | — |
| research-grants | ĐẠT | — (khuyến nghị đánh số mục H) |
