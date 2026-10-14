Xác nhận: luồng chính gọi được công cụ Skill (academic-paper-reviewer), phản hồi "Launching skill: academic-paper-reviewer". Skill cần công cụ Agent nên chạy ở luồng chính theo V7. Mỗi ghế phản biện là một subagent riêng, mở trong ngữ cảnh mới.

# Cổng 2 — academic-paper-reviewer (Imbad0202, v3.6.2 sprint contract): ĐẠT

Ngày 2026-10-14. Chế độ `full` (hợp đồng `reviewer/reviewer_full/v2`, sha256 e9712090…). Báo cáo thất bại ngày 2026-10-13 (thiếu shared/ và scripts/) đã được khắc phục: theo lựa chọn của người dùng, đã chép shared/ và scripts/ từ commit d1e51716 vào `.claude/ars/`; các script có chạy đều đã được đọc trước.

## Kết quả
- **Quyết định biên tập:** `editorial_decision=major_revision` (sửa lớn)
- `dimension_verdicts: [D1=block, D2=warn, D3=block, D4=warn, D5=warn, D6=warn]`
- `fired_conditions: [F2, F3, F5]`. F2 (90) quyết định: hai chiều bắt buộc bị chấm block, đều thuộc loại sửa được, không có block fatal.
- `da_critical_adjudications: []`: bảng CRITICAL của DA trống. 9 phát hiện MAJOR (M1–M9) đã đưa vào lộ trình.
- **Vấn đề chặn:**
  - R2: H1 dễ "không kết luận" vì chỉ có khoảng 28 cửa sổ, so với ngưỡng 10 cửa sổ căng thẳng.
  - R7: mẫu số chuẩn hóa chưa được định nghĩa.
  - R10: đăng ký trước diễn ra sau khi đã ước lượng thử trên 2019–2025.
- **Lộ trình sửa đổi:** 49 mục (21 must_fix, 22 should_fix, 6 consider) và 12 câu hỏi. Ma trận R&R đầy đủ ở Phụ lục B.
- Nhiều mục must_fix chạm vào thiết kế cốt lõi (R2, R6–R16, R18, R21): định nghĩa cửa sổ căng thẳng, phân phối rỗng, Holm/α, tập M, quy tắc chọn mô hình. Theo nguyên tắc 2, các mục này chuyển vào danh sách **chờ người dùng duyệt** và không tự sửa. Các mục chỉ là văn bản (R1, R3, R4, R5, R17, R19, R20) có thể đưa vào Vòng 1.

## Nguồn gốc hội đồng (provenance, 6 trục)
role_separated = true; fresh_context = true; blind (không thấy báo cáo ghế khác) = true; model_family_distinct = false; provider_distinct = false; human_distinct = false. Công bố bắt buộc: cả 5 ghế cùng một họ mô hình, nên lỗi của chúng có thể tương quan; tách vai trò KHÔNG có nghĩa là các đánh giá độc lập. Artifact: panel-provenance.json (validate PASS, validate-carrier PASS).

## Bằng chứng tuân thủ (theo SKILL.md "Orchestration Workflow" và "Checkpoint Rules")
| Bước | Trạng thái | Bằng chứng |
|---|---|---|
| Sprint Contract Hard Gate: nạp `shared/contracts/reviewer/full.json`, chạy check_sprint_contract | LÀM | contract.json; các script kiểm tra exit 0 |
| Phase 0: field_analyst_agent đọc trọn bài → 4 thẻ cấu hình phản biện | LÀM | phase0_field_analysis.md |
| Checkpoint 1: trình thẻ cấu hình cho người dùng | LÀM (tự xác nhận) | Người dùng dặn "làm đi chuẩn theo các skill, không hỏi lại", nên thẻ được giữ nguyên, không chỉnh |
| Phase 1: 5 ghế (EIC, R1 phương pháp, R2 lĩnh vực, R3 góc nhìn, DA) không xem bài, chạy song song | LÀM | phase1_*.md; `check_phase_conformance --phase1-only` exit 0 cho cả 5 |
| Phase 2 (paper-visible) cho từng ghế | LÀM | phase2_*.md; `check_phase_conformance --phase2` exit 0 cho cả 5 (ghế phương pháp có cảnh báo [RECEIPT-ATTESTATION]: khai `no_recomputable_statistics`, vì đề cương chưa có số liệu kết quả) |
| Iron Rule 2: ghi provenance | LÀM | review_panel_provenance build/validate/build-carrier/validate-carrier đều PASS |
| check_panel_synthesis --layer1-only | LÀM | PASS |
| editorial_synthesizer_agent, giao thức 3 bước | LÀM | synthesis.md; `check_panel_synthesis --synthesis` → `PANEL-SYNTHESIS: PASS`, exit 0 (luồng chính chạy lại để kiểm chứng) |
| Iron Rule 3: không bịa nhận xét | LÀM | Mỗi mục lộ trình dẫn về ghế và W-id/M-id |
| Iron Rule 4: phân xử DA CRITICAL | LÀM | Không có CRITICAL; danh sách rỗng được ghi rõ |
| Iron Rule 6: không sửa bản thảo | LÀM | manuscript.md không đổi |
| #684 ràng buộc tiêu chí | LÀM | `criteria_binding_unavailable`; không có nhận định nào về venue-fit |
| #849 gắn kết quả kiểm tra từ viết tắt | LÀM | Gắn nguyên văn ở cuối thư quyết định. Hạn chế: script chỉ hỗ trợ en/zh-TW, nên các tiêu đề tiếng Việt viết hoa (QU, NG, TR…) bị báo nhầm là từ viết tắt; nhiều mục là tên tạp chí hay tổ chức. Mục này chỉ để tham khảo, không sinh mục sửa đổi nào |
| #518 kiểm tra mô hình chéo | KHÔNG ÁP DỤNG | ARS_CROSS_MODEL không được đặt |
| Artifact máy revision-roadmap/1.0 | CHƯA LÀM | Thiếu block manifest và base_draft_sha256; các mục được định vị bằng mục/bảng/phương trình ([BLOCK-MANIFEST-UNAVAILABLE]) |
| Phase 2.5 Revision Coaching (Socratic) | CHƯA LÀM | Bước này phải hỏi đáp với tác giả. Người dùng yêu cầu không hỏi lại, tương đương lựa chọn "just fix it" để bỏ qua. Cột phản hồi tác giả trong ma trận R&R ghi "[chờ tác giả]" |

Câu trích làm bằng chứng (từ đề cương): §4.3.10 "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận"; Bảng 5 "ước lượng thử bảy mô hình trên giai đoạn 2019--2025"; §8.2 "Thí sinh đang theo học ngành Kế toán hệ vừa làm vừa học tại Đại học Kinh tế Quốc dân (năm thứ ba)".

---
# Phụ lục A — Gói quyết định biên tập (nguyên văn)
# Editorial Decision Package

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Ranh giới hiện tại: gói này không được nâng hạng từ một hồ sơ ứng viên hay hồ sơ đặt tên bằng văn xuôi. `PROFILE_MEASURED` chưa khả dụng cho đến khi có một artifact hồ sơ đóng và trình kiểm tra replay gắn đúng các trường mục tiêu với `execution_topology_sha256` của hội đồng đã hoàn tất. Cả năm thẻ phản biện cũng tự khai `NOT_CALIBRATED`.

## Ràng buộc tiêu chí

criteria_binding_unavailable

Lượt chạy này được khai báo rõ là không ràng buộc tiêu chí. Không có Review Target Context #683 hay marker #684 nào được cung cấp. Cả năm thẻ (EIC, R1, R2, R3, DA) đều ghi `criteria_binding_unavailable`, nên điều kiện của lượt không ràng buộc đã thỏa. Gói này **không** đưa ra nhận định nào về mức phù hợp với venue, với tiêu chí xét tuyển NCS của Trường Quốc tế – ĐHQGHN hay với bất kỳ hồ sơ hỗ trợ nào. Chiều D6 (venue_fit_and_contribution) chỉ được dùng như điểm số hợp đồng của ghế EIC. Ghế EIC tự giới hạn nhận định D6 vào việc đối chiếu nội tại các lời tự mô tả trong văn bản.

## Mechanical Audit (v3.6.2 Sprint Contract Synthesizer Protocol)

Hợp đồng: `reviewer/reviewer_full/v2` (contract_sha256 `e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`). Hội đồng gồm 5/5 báo cáo dùng được, vai trò theo thứ tự dispatch: eic, methodology, domain, perspective, da. Không có `[PANEL-SHRUNK]`.

### Bước 1 — Ma trận điểm theo vai trò đủ điều kiện

| Dim | Priority | eligible_roles | Điểm đã chấm của ghế đủ điều kiện | Verdict (xấu nhất) |
|---|---|---|---|---|
| D1 methodology_rigor | mandatory | methodology | R1 = block (block_class: repairable) | block |
| D2 domain_accuracy | mandatory | domain | R2 = warn | warn |
| D3 argumentative_coherence | mandatory | da, methodology | DA = block (repairable); R1 = warn | block |
| D4 cross_disciplinary_relevance | high | perspective | R3 = warn | warn |
| D5 writing_and_structure | normal | eic | EIC = warn | warn |
| D6 venue_fit_and_contribution | mandatory | eic | EIC = warn | warn |

Giá trị `not_assessed` của các ghế không đủ điều kiện bị loại khỏi cả tử số lẫn mẫu số. Không ghế nào khai `block_class: fatal`. Không có `[DIMENSION-UNASSESSED]`.

### Bước 2 — Đánh giá failure_conditions

| ID | Severity | Quantifier | Expression (mẫu §9) | Đánh giá | fired |
|---|---|---|---|---|---|
| F1 | 95 | any | `any mandatory dimension has a fatal block` (mẫu 6) | D1, D2, D3, D6: không có ghế nào khai fatal | false |
| F2 | 90 | any | `any mandatory dimension scores 'block'` (mẫu 1) | D1: R1 = block → true (≥1); D3: DA = block → true | **true** |
| F3 | 70 | majority | `two or more mandatory dimensions score 'warn' or worse` (mẫu 2) | D1 (n=1, chính ghế chủ): block ≥ warn → true; D2 (n=1): warn → true; D3 (n=2, cần cả hai): DA block, R1 warn → true; D6 (n=1): warn → true; 4 ≥ 2 | **true** |
| F4 | 60 | any | `any high-priority dimension scores 'block'` (mẫu 1) | D4: R3 = warn ≠ block | false |
| F5 | 40 | any | `any dimension scores 'warn' or worse` (mẫu 7) | D1–D6 đều ≥ warn | **true** |
| F0 | 10 | all | `every dimension scores 'pass'` (mẫu 9) | Không chiều nào pass | false |

Mọi expression đều thuộc bộ từ vựng §9 được công nhận. Không có `[EXPRESSION-UNRECOGNISED]`.

### Bước 3 — Thứ tự ưu tiên, quyết định và các dòng kiểm toán

Các điều kiện đã kích hoạt là F2 (90), F3 (70) và F5 (40). F2 có severity cao nhất, action `major_revision`. Action này không bị làm mềm vì lý do hậu nghiệm nào.

DA CRITICAL: bảng `#### CRITICAL` trong báo cáo DA không có dòng nào. DA còn ghi rõ: "Không có phát hiện nào riêng lẻ đạt mức Critical". Vì vậy không có ID C<n> nào cần phân xử, và dòng adjudication là danh sách rỗng. Chín phát hiện MAJOR của DA (M1–M9) được đưa vào Lộ trình sửa đổi dưới dạng nguồn trực tiếp (REV-48) hoặc nguồn chứng thực, theo mục Phân tích đồng thuận. Quyết định không phải accept, nên không cần marker `DA-CRITICAL-VS-ACCEPT`.

dimension_verdicts: [D1=block, D2=warn, D3=block, D4=warn, D5=warn, D6=warn]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

Kiểm tra mô hình chéo (#518): `ARS_CROSS_MODEL` không được đặt trong phiên này, nên không chạy và hành vi không đổi.

---

## Part 1: Editorial Decision Letter

# Editorial Decision

## Manuscript Information
- **Title**: Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường: Bằng chứng từ thị trường chứng khoán Việt Nam (đề cương nghiên cứu sinh)
- **Manuscript ID**: NOT PROVIDED
- **Submission Date**: NOT PROVIDED
- **Decision Date**: 2026-10-14
- **Review Round**: Round 1 (panel_id `de-cuong-cong2-round-1`)

Kính gửi tác giả,

Cảm ơn tác giả đã gửi đề cương. Đề cương được đánh giá qua năm ghế phản biện tách vai trò, trong đó có một ghế Journal-Fit Reviewer (EIC). Nguồn gốc thực thi của các ghế được báo cáo chi tiết dưới đây theo sáu trục riêng biệt. Gói này **không** quy các trục đó về một tuyên bố nhị phân về tính độc lập. Không có tạp chí hay venue nào được ràng buộc (`criteria_binding_unavailable`), nên thư này không nhận định mức phù hợp với venue.

## Review Panel Provenance (#540/#740)

- **Typed artifact**: `artifacts/panel-provenance.json` (carrier `panel-carrier.json`, `status: valid`, schema `review-panel-provenance-carrier/1.0`)
- **Artifact SHA-256**: `f1e0e6778312faba4503b7e91ed3850ddc1c56719b40475779138e916ee673d0` (đã đối chiếu lại với byte thô của artifact trong phiên này; khớp carrier)
- **Panel ID**: `de-cuong-cong2-round-1`
- **Normalized manifest SHA-256**: `5b2952413125799a7963e31b18cacd0cd0da49bc5a470babe75b578bffa9d292`
- **Execution topology SHA-256**: `ba4de2cf08761c7f478a4d22252e1c234f07e2b96cfc887197ff296a1c11b059`
- **Fresh-context scope**: `within_panel_attempt_only` (không so sánh với các lần thử lại hay các vòng trước)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | subagent-aac588dbadb97dd25 | false | claude | anthropic | null |
| R1 | methodology | model | subagent-a94b9163e8fdb1b99 | false | claude | anthropic | null |
| R2 | domain | model | subagent-ae0c73c7d7fbbd6c6 | false | claude | anthropic | null |
| R3 | perspective | model | subagent-aee65b8f2b13956a7 | false | claude | anthropic | null |
| DA | da | model | subagent-aeacba7cafab3ceca | false | claude | anthropic | null |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | true |
| Blind to peer outputs | true |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

- **Binary independence claim**: Không tính (`independence_claim: not_computed_from_personas`). Sự đa dạng persona hay vai trò chỉ chứng minh `role_separated`. Hội đồng này không được gọi là độc lập.
- **Correlated-error disclosure**: All model-executed review seats used one model family; role separation does not remove correlated-error risk.
- `fresh_context: true` chỉ có nghĩa trong phạm vi một lần chạy hội đồng. Nó không chứng minh rằng các context ID là mới so với các lần thử lại hay các vòng trước.

---

## Decision *

### Major Revision

---

## Blocking Issues * (0–3, immutable source order)

Danh sách đầy đủ các mục bắt buộc ở R1–R21 bên dưới. Ba vấn đề dưới đây là những mục mà cả ghế phương pháp (chấm D1 = block) và ghế DA (chấm D3 = block) cùng nêu là trực tiếp chặn phép kiểm định H1.

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R2 | Kết quả chủ đạo H1 có nguy cơ cao rơi vào "không kết luận" (khoảng 28 cửa sổ so với ngưỡng 10 cửa sổ căng thẳng), nhưng chưa có ước tính trước số cửa sổ căng thẳng hay phân tích công suất | EIC (W2), R1 (W1), DA (M4) | `text: §4.3.10 "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10"` | REV-02 |
| R7 | Phép chuẩn hóa thước đo chính (chia R_t, D_t cho sai số chuẩn bootstrap) chưa được định nghĩa | R1 (W2), DA (M9) | `text: §4.3.6 "cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình trong cùng cửa sổ"` | REV-12 |
| R10 | Đăng ký trước diễn ra sau khi đã ước lượng thử cả bảy mô hình trên 2019–2025, giai đoạn chứa hai đợt căng thẳng; độ dài cửa sổ được biện minh sau lần thử đó | R1 (W4), DA (M3) | `table: Bảng 5, hàng Năm 1, cột Nội dung — "ước lượng thử bảy mô hình trên giai đoạn 2019--2025"` | REV-15 |

---

## Reviewer Summary

| Reviewer | Role | Recommendation | Confidence |
|---|---|---|---|
| Journal-Fit Reviewer (EIC) | Biên tập viên cấp cao field-general, tạp chí tài chính thực nghiệm (Thẻ #1) | Major (tín hiệu sơ bộ của ghế: "cần sửa đổi lớn ở phần định vị đóng góp"); D5 = warn, D6 = warn | 4 (toàn thẻ) |
| Reviewer 1 | Nhà kinh tế lượng tài chính: đánh giá ngoài mẫu, MCS, Markov-switching (Thẻ #2) | Không nêu khuyến nghị tổng thể tường minh; D1 = block (repairable), D3 = warn | Theo từng phát hiện (3–5); không có điểm toàn thẻ |
| Reviewer 2 | Nhà nghiên cứu lựa chọn danh mục dưới bất định mô hình (Thẻ #3) | Major Revision (phạm vi miền chuyên môn); D2 = warn | 4 |
| Reviewer 3 | Chuyên gia quản trị rủi ro mô hình (MRM) và khoa học quản lý (Thẻ #4) | Không nêu khuyến nghị tổng thể tường minh; D4 = warn | 3 |
| Devil's Advocate | Ghế đối nghịch cố định | N/A — chỉ phát hiện (D3 = block, repairable; 0 CRITICAL, 9 MAJOR) | N/A — theo từng phát hiện |

Mức tin cậy chỉ là công bố phạm vi do ghế tự khai. Nó không được dùng để cộng, lấy trung bình, bỏ phiếu hay phân xử.

### Step 1a — Ma trận tóm tắt báo cáo

| Dimension | EIC | R1 (Methodology) | R2 (Domain) | R3 (Perspective) |
|---|---|---|---|---|
| Overall Recommendation | Major (sơ bộ) | Không tường minh (D1 block) | Major Revision | Không tường minh (D4 warn) |
| Confidence / scope disclosure | 4; không đánh giá kinh tế lượng | 3–5 theo phát hiện; không đánh giá văn liệu và độ phù hợp chương trình | 4; không xác minh được SR 26-2 và Thông tư 83/2025 | 3; không đánh giá kinh tế lượng và văn liệu |
| Key Strengths | S1–S4 | S1–S8 | S1–S5 | S1–S4 |
| Key Weaknesses | → Step 1b (W1–W2 Major, W3–W9 Minor) | → Step 1b (W1–W9 Major, W10–W18 Minor) | → Step 1b (W1–W3 Major, W4–W8 Minor) | → Step 1b (W1, W2, W6 Major; W3–W5, W7–W8 Minor) |
| # of Questions | 0 | 4 | 4 | 4 |
| # of Minor Issues (danh sách riêng) | 0 | 0 | 4 | 0 |

### Step 1b — Bảng phân rã tiểu luận điểm (chỉ ghi các vị trí khác `not-mentioned`)

Severity được chuyển nguyên từ thẻ (Major/Minor → major/minor). DA không tham gia đếm đồng thuận, nhưng vị trí chứng thực của DA được ghi lại để truy vết.

| sub_claim_id | parent_weakness | reviewer_id | position | evidence_pointer | severity | confidence |
|---|---|---|---|---|---|---|
| SC-1 | Khoảng trống viết tuyệt đối | EIC | raised | EIC W1 — text: §4.2(2), §4.2(4) | major | 4 |
| SC-1 | | R2 | corroborated | R2 W1 — text: §4.2(2), §4.2(4) | major | 4 |
| SC-1 | | DA | (chứng thực, ngoài đếm) | DA M8 | major | 4 |
| SC-2 | Nguy cơ H1 "không kết luận" | EIC | raised | EIC W2 (a) — text: §4.3.6, §4.3.10 | major | 3 |
| SC-2 | | R1 | corroborated | R1 W1 (a) — text: §4.3.10 | major | 4 |
| SC-2 | | DA | (chứng thực, ngoài đếm) | DA M4 | major | 3 |
| SC-3 | Chưa có đóng góp dự phòng khi "không kết luận" | EIC | raised | EIC W2 (b) | major | 3 |
| SC-4 | Đóng góp "lý thuyết" bị nói rộng | EIC | raised | EIC W3 — text: §4.4 | minor | 4 |
| SC-4 | | R2 | corroborated | R2 Nhận xét chi tiết, "Đóng góp cho lĩnh vực" ("nên được viết khiêm tốn hơn") | minor [SEVERITY-SOURCE: letter-fallback] | 4 [CONFIDENCE-SOURCE: report-level] |
| SC-5 | Tuyên bố liên ngành / phù hợp chương trình (§5) | EIC | raised | EIC W4 — text: §5 đoạn 1 | minor | 3 |
| SC-5 | | R3 | disputed (severity) | R3 W2 (a) — text: §5, §4.4 | major | 3 |
| SC-6 | Tách luận án khỏi bản thảo 1, 5, 6 (Bảng 7) | EIC | raised | EIC W5 — table: Bảng 7 | minor | 4 |
| SC-6 | | R3 | disputed (severity) | R3 W6 (b) — text: §8.2 | major | 3 |
| SC-7 | Người hướng dẫn ghi không thống nhất | EIC | raised | EIC W6 | minor | 5 |
| SC-8 | Trường thông tin để trống | EIC | raised | EIC W7 | minor | 5 |
| SC-9 | Hình 3 trống, chú thích mất số | EIC | raised | EIC W8 — figure: Hình 3 | minor | 2 |
| SC-10 | Tiêu đề rộng hơn phạm vi HOSE | EIC | raised | EIC W9 | minor | 4 |
| SC-11 | "Cửa sổ căng thẳng" chưa định nghĩa | R1 | raised | R1 W1 (b) | major | 4 |
| SC-11 | | DA | (chứng thực, ngoài đếm) | DA M4 ("S_t là tỷ lệ ngày liên tục") | major | 3 |
| SC-12 | Mẫu số chuẩn hóa chưa định nghĩa | R1 | raised | R1 W2 (a) — text: §4.3.6 | major | 4 |
| SC-13 | Chuẩn hóa có thể loại tín hiệu cần đo | R1 | raised | R1 W2 (b) | major | 4 |
| SC-13 | | DA | (chứng thực, ngoài đếm) | DA M9 | major | 4 |
| SC-14 | Phân phối rỗng không trung tính theo CE | R1 | raised | R1 W3 — text: §4.3.7 | major | 4 |
| SC-15 | Đăng ký trước sau ước lượng thử | R1 | raised | R1 W4 — table: Bảng 5 | major | 4 |
| SC-15 | | DA | (chứng thực, ngoài đếm) | DA M3 | major | 4 |
| SC-16 | Suy luận mẫu nhỏ (~28 quan sát) | R1 | raised | R1 W5 | major | 4 |
| SC-17 | Phân rã β0 − β1 | R1 | raised | R1 W6 — equation: Eq. (5) | major | 4 |
| SC-17 | | DA | (chứng thực, ngoài đếm) | DA M2 | major | 4 |
| SC-18 | Quy tắc VIF và tiêu chí H2 | R1 | raised | R1 W7 | major | 4 |
| SC-19 | Cơ chế (ii), (iii) trùng M6, M7 | R1 | raised | R1 W8 — text: §4.3.8 | major | 4 |
| SC-19 | | DA | (chứng thực, ngoài đếm) | DA M7 | major | 4 |
| SC-20 | Mức α và Holm với tiêu chí ghép | R1 | raised | R1 W9 | major | 3 |
| SC-21 | S_t là biến tạo sinh | R1 | raised | R1 W10 | minor | 4 |
| SC-22 | "Trọng số Bayes" chưa định nghĩa | R1 | raised | R1 W11 | minor | 4 |
| SC-23 | Regret gắn với một quy tắc chọn duy nhất | R1 | raised | R1 W12 — text: §4.3.6 | minor | 4 |
| SC-23 | | DA | (chứng thực, ngoài đếm) | DA M6 | major | 4 |
| SC-24 | Ngưỡng N/T của M3 | R1 | raised | R1 W13 | minor | 5 |
| SC-25 | Tần suất lợi suất, năm hóa, chi phí | R1 | raised | R1 W14 — absence | minor | 4 |
| SC-26 | Xây dựng biến kênh cấp cửa sổ | R1 | raised | R1 W15 — absence | minor | 4 |
| SC-26 | | R2 | corroborated | R2 Vấn đề nhỏ 1 (thuật ngữ tương quan dùng xen kẽ) | minor [SEVERITY-SOURCE: letter-fallback] | 4 [CONFIDENCE-SOURCE: report-level] |
| SC-27 | Nhãn chế độ khi ước lượng lại | R1 | raised | R1 W16 | minor | 4 |
| SC-28 | Diễn giải kết quả không bác bỏ | R1 | raised | R1 W17 — text: §4.3.10 | minor | 4 |
| SC-28 | | DA | (chứng thực, ngoài đếm) | DA Minor (i) | minor | — |
| SC-29 | Dấu kênh tương quan đuôi (H2) ngược cơ chế H1 | R1 | raised | R1 W18 — table: Bảng 2 H2 | minor | 3 |
| SC-29 | | R2 | corroborated | R2 W4 — text: Bảng 2 H2 | minor | 4 |
| SC-29 | | DA | (chứng thực, ngoài đếm) | DA M5 | major | 3 |
| SC-30 | Regret gán sai cơ sở lý thuyết (maxmin/robust control) | R2 | raised | R2 W2 — text: §4.3.1 | major | 4 |
| SC-30 | | R3 | disputed (severity) | R3 W5 (a) | minor | 4 |
| SC-31 | Tập 7 mô hình; ràng buộc chỉ mua là co rút ngầm | R2 | raised | R2 W3 — text: §4.3.5, §4.4 | major | 4 |
| SC-32 | Độ phân tán chéo gọi là "thước đo bầy đàn" | R2 | raised | R2 W5 — text: §4.4 | minor | 4 |
| SC-33 | Mô tả Kerkhof và cộng sự (2010) | R2 | raised | R2 W6 | minor | 3 |
| SC-34 | Ledoit–Wolf (2008) mở rộng sang CE | R2 | raised | R2 W7 | minor | 4 |
| SC-35 | Vi cấu trúc HOSE (biên độ giá) | R2 | raised | R2 W8 — absence [FIELD-NORM UNVERIFIED] | minor | 3 |
| SC-36 | Hiệu chỉnh Forbes–Rigobon dùng như chuỗi thời gian | R2 | raised | R2 Vấn đề nhỏ 2 | minor [SEVERITY-SOURCE: letter-fallback] | 4 [CONFIDENCE-SOURCE: report-level] |
| SC-37 | Kritzman (2012) "dự báo" chế độ | R2 | raised | R2 Vấn đề nhỏ 3 | minor [SEVERITY-SOURCE: letter-fallback] | 4 [CONFIDENCE-SOURCE: report-level] |
| SC-38 | Cập nhật "Dựa trên phần tóm tắt" | R2 | raised | R2 Vấn đề nhỏ 4 | minor [SEVERITY-SOURCE: letter-fallback] | 4 [CONFIDENCE-SOURCE: report-level] |
| SC-39 | Tiền đề người dùng (công ty quản lý quỹ) chưa xác lập | R3 | raised | R3 W1 — text: §4.1 đoạn 4 | major | 4 |
| SC-39 | | DA | (chứng thực, ngoài đếm) | DA "Tiền đề chưa được kiểm tra" (Minor) | minor | — |
| SC-40 | Quy tắc 36 tháng là giả định hành vi chưa biện minh | R3 | raised | R3 W2 (b); Assumption Audit (ii) | major | 3 |
| SC-41 | Thủ tục giám sát thiếu yếu tố MRM | R3 | raised | R3 W3 | minor | 4 |
| SC-42 | Regret chuẩn hóa khó đọc với người dùng | R3 | raised | R3 W4 — equation: Eq. (4), §4.3.6 | minor | 3 |
| SC-42 | | DA | (chứng thực, ngoài đếm) | DA M9 | major | 4 |
| SC-43 | Nghĩa hành vi của "regret" | R3 | raised | R3 W5 (b) | minor | 4 |
| SC-44 | Khả thi thời gian so với cam kết song song | R3 | raised | R3 W6 (a) — text: §8.2 | major | 3 |
| SC-45 | Giấy phép dữ liệu thương mại | R3 | raised | R3 W7 | minor | 3 |
| SC-46 | Bên liên quan chưa nêu | R3 | raised | R3 W8 | minor | 3 |
| SC-47 | Rủi ro hành vi đồng loạt khi nhiều tổ chức cùng kích hoạt quy tắc | R3 | raised | R3 Broader Implications, "Tác động xã hội" | minor [SEVERITY-SOURCE: letter-fallback] | 3 [CONFIDENCE-SOURCE: report-level] |

Hai phát hiện chỉ do DA nêu (DA M1 và DA Minor (ii)) không có `sub_claim_id`. Chúng được đưa vào lộ trình với Sub-Claim = `—` (REV-48, REV-49).

Kiểm tra cân bằng hình thức (Step 1c): không phát hiện nào bị hạ hay nâng mức vì cách diễn đạt. Các nhận định dựa trên trí nhớ hoặc chưa xác minh (R2 W6, R2 W8 `[FIELD-NORM UNVERIFIED]`, các gợi ý `[UNVERIFIED]`) được giữ nguyên nhãn và chuyển thành yêu cầu tác giả tự đối chiếu. Chúng không được coi là sai cũng không được coi là đã xác nhận.

---

## Consensus Analysis *

### Points of Agreement (Consensus)

**[CONSENSUS-4]**: Không có. Không tiểu luận điểm nào được cả bốn ghế không phải DA cùng nêu.

**[CONSENSUS-3]**: Không có. Mức đồng thuận cao nhất là 2/4.

Theo quy tắc đếm, im lặng không được tính là đồng ý. Vì vậy các mục dưới đây là **phát hiện được chứng thực (2/4, không xung đột)**, không phải đồng thuận:

1. **SC-1 — Tuyên bố khoảng trống tuyệt đối ở §4.2 mâu thuẫn với chính văn liệu được trích** (EIC W1 + R2 W1; DA M8 chứng thực; R1, R3 im lặng). Cả hai ghế cùng chỉ ra rằng Tu (2010) và Avramov (2002), cả hai đều được đề cương trích, đã đo tổn thất kinh tế của việc chọn hoặc bỏ qua mô hình. R2 bổ sung Kan và Zhou (2007). Hai ghế đề xuất cùng một hành động: viết lại ở dạng hẹp và phân biệt rõ với các công trình đó.
2. **SC-2 — Nguy cơ cao H1 rơi vào "không kết luận"** (EIC W2 + R1 W1; DA M4 chứng thực; R2, R3 im lặng). R1 tự ước tính: để đạt 10 trên khoảng 28 cửa sổ, khoảng 36% số cửa sổ phải là cửa sổ căng thẳng. Đây là ước tính định hướng của người phản biện, không phải kết quả.
3. **SC-4 — Đóng góp "lý thuyết" bị khẳng định rộng hơn phạm vi kiểm chứng** (EIC W3 + R2 Nhận xét chi tiết; R1, R3 im lặng).
4. **SC-29 — Dấu kỳ vọng âm của tương quan đuôi trong H2 ngược chiều cơ chế H1** (R1 W18 + R2 W4, cả hai mức Minor; DA M5 nêu ở mức Major; EIC, R3 im lặng).
5. **SC-26 — Biến kênh tương quan chưa được định nghĩa và đặt tên thống nhất** (R1 W15 + R2 Vấn đề nhỏ 1; EIC, R3 im lặng).

Mọi tiểu luận điểm còn lại trong Step 1b là **phát hiện của một ghế (1/4, không xung đột)**. Chúng được đánh giá theo tiêu chí và bằng chứng neo của chính chúng. Đáng chú ý, chín phát hiện Major của R1 (W1–W9) là cơ sở của điểm D1 = block. Mỗi phát hiện chỉ do một ghế không phải DA nêu, nhưng năm trong số đó được DA chứng thực độc lập về nội dung (M2, M3, M4, M7, M9). Theo trục `model_family_distinct: false`, sự chứng thực này **không** loại trừ được sai số tương quan.

### Points of Disagreement

**Disagreement 1 (SC-5): Tuyên bố "giao điểm liên ngành" và phù hợp chương trình ở §5**
- **EIC view (W4, Minor, conf 3)**: Lời tự mô tả ở §5 ("tập trung vào kinh tế hành vi và quản lý") vênh với tỷ trọng thực tế, vì H4 chỉ là thăm dò và thủ tục giám sát chưa kiểm nghiệm. EIC đề nghị viết lại §5 cho khớp §4.4.
- **R3 view (W2, Major, conf 3)**: Cùng hiện tượng, nhưng R3 đánh giá khẳng định liên ngành chưa được chứng minh và nặng hơn. R3 đưa phương án (a) viết lại cho đúng tầm, và phương án (b) thêm một cấu phần định tính nhỏ.
- **Disagreement type**: Severity disagreement (cùng tồn tại, khác mức).
- **Editor's Resolution**: Hành động tối thiểu không bị tranh chấp và là **bắt buộc**: viết lại §5 và §4.4 cho khớp tỷ trọng thực của thiết kế. Bất đồng về mức độ (Minor hay Major) **không giải quyết được** bằng bằng chứng. Cả hai ghế neo vào cùng đoạn văn và cùng thừa nhận giới hạn phạm vi đối với tiêu chí chương trình (không có ràng buộc tiêu chí). Vì vậy bất đồng được ghi lại là bất đồng chưa giải quyết, và cả hai mức severity được chuyển nguyên vào REV-05. Phương án (b) thuộc quyền tự quyết của tác giả và người hướng dẫn, vì nó thay đổi nguyên tắc "không dùng khảo sát hay phương pháp định tính" ở §4.3.3. Chính R3 cũng nêu điều này.
- **Resolution Rationale**: Áp dụng nguyên tắc bất đồng chưa giải quyết (#574 B1) và nguyên tắc quyền tự quyết của tác giả. Không ghế nào được ưu tiên dựa trên mức tin cậy.

**Disagreement 2 (SC-6): Tách luận án khỏi các bản thảo đang phản biện (Bảng 7, hàng 1, 5, 6)**
- **EIC view (W5, Minor, conf 4)**: Thiếu một câu nêu phần nào của bản thảo 1, 5, 6 được dùng lại và phần nào là mới. Đây là rủi ro liêm chính công bố.
- **R3 view (W6 (b), Major, conf 3)**: Cùng yêu cầu xử lý chín bản thảo đang xét, nhất là ba bản liên quan, nhưng nằm trong một gói Major về khả thi thời gian.
- **Disagreement type**: Severity disagreement.
- **Editor's Resolution**: Hai cách sửa tương thích và trùng nhau: một tuyên bố tách bạch ở §4.4 hoặc §7.3, kèm cam kết trích dẫn chéo. Mục này là **bắt buộc** (REV-06) vì đây là vấn đề liêm chính công bố và chi phí sửa thấp. Severity được chuyển nguyên cả hai giá trị. Mức Major của R3 gắn với gói khả thi thời gian (SC-44), và phần đó được giữ thành mục riêng REV-44.
- **Resolution Rationale**: Ưu tiên chuyên môn. Chính sách công bố trùng lặp thuộc phạm vi biên tập của ghế EIC. Tuy vậy, mức Major của R3 không bị loại bỏ mà vẫn được hiển thị.

**Disagreement 3 (SC-30): Cơ sở lý thuyết của thước đo regret**
- **R2 view (W2, Major, conf 4)**: §4.3.1 gán regret cho Gilboa–Schmeidler (maxmin) và Hansen–Sargent (robust control). Regret thực ra thuộc tiêu chí minimax regret (Savage) hoặc regret theory, nên nền lý thuyết của biến phụ thuộc chính bị trình bày sai.
- **R3 view (W5 (a), Minor, conf 4)**: Cùng nhận định rằng regret gần minimax regret của Savage hơn, nhưng R3 xếp ở mức Minor dưới góc khả năng tiếp cận thuật ngữ.
- **Disagreement type**: Severity disagreement.
- **Editor's Resolution**: Giữ mức **Major, bắt buộc** (REV-30).
- **Resolution Rationale**: Ưu tiên chuyên môn. Đây là vấn đề miền chuyên môn (khung lý thuyết của biến phụ thuộc chính) nên ưu tiên R2. R3 tự giới hạn góc nhìn của mình vào khả năng tiếp cận của người đọc ngành lân cận. Cả hai ghế đồng ý về sự tồn tại và hướng sửa.

**Ghi chú về các khác biệt không phải SPLIT**: DA chấm các vấn đề SC-23 (một quy tắc chọn duy nhất), SC-29 (dấu kênh tương quan) và SC-42 (đơn vị của regret chuẩn hóa) ở mức Major, còn ghế không phải DA chấm Minor. DA không thuộc bộ đếm đồng thuận, nên đây không phải SPLIT. Severity của ghế gốc được chuyển nguyên, và mức của DA được ghi kèm trong lộ trình để hiển thị.

### DA-CRITICAL

Không có. Bảng CRITICAL của DA trống, và DA tự khẳng định không phát hiện nào đạt mức Critical. Vì vậy không cần phân xử VALIDATED/REJECTED/UNRESOLVED. Lập luận đối nghịch mạnh nhất của DA ("đề cương đo thất bại của một quy tắc đuổi theo thành tích quá khứ tại điểm chuyển chế độ, không đo rủi ro lựa chọn mô hình như một thuộc tính thị trường") được giữ hiển thị qua REV-23 và REV-48. Tác giả phải phản hồi cả hai mục này.

---

## Decision Rationale *

Quyết định Major Revision được xác định cơ học theo hợp đồng `reviewer/reviewer_full/v2`. F2 kích hoạt vì hai chiều bắt buộc bị chấm `block`: D1 (R1) và D3 (DA). Cả hai đều thuộc loại `repairable`, không ghế nào khai `fatal`, nên F1 (reject) không kích hoạt. F3 và F5 cũng kích hoạt nhưng có severity thấp hơn F2.

Quyết định này nhất quán với nội dung các báo cáo. R1 chấm D1 = block "do tác động chung của các phát hiện Major lên quy trình kiểm định chính". Ở dạng hiện tại, quy trình kiểm định H1 chưa tách được rủi ro lựa chọn tăng thật khỏi nhiễu ước lượng tăng ở chế độ căng thẳng (R1 W1–W4). DA chấm D3 = block vì hai mắt xích lõi tự mâu thuẫn: phép kiểm định H1 kiểm soát chính biến động định nghĩa chế độ (M1), và đăng ký trước đến sau ước lượng thử (M3). R2 khuyến nghị Major Revision cho phần tổng quan và khung lý thuyết. EIC đưa tín hiệu cần sửa lớn ở phần định vị đóng góp. R3 chấm D4 = warn.

Quyết định không nhẹ hơn (Minor Revision) vì các sửa đổi bắt buộc chạm tới thiết kế kiểm định chính: định nghĩa thước đo, phân phối rỗng, quy tắc ra quyết định và trình tự đăng ký trước. Đây không chỉ là việc làm rõ câu chữ. Quyết định cũng không nặng hơn (Reject) vì mọi ghế đều nói lõi đề tài vẫn đứng được: EIC nói "cốt lõi đề tài vẫn đứng được", R1 nói "không khuyết điểm nào là tử huyệt", R2 nói khoảng trống ở dạng hẹp "có khả năng đứng vững", và DA nói luận đề đo lường "vẫn còn đứng được nếu sửa". Phần lớn sửa đổi làm được trước khi đăng ký trước mà không cần dữ liệu mới.

Ba bất đồng về mức độ (SC-5, SC-6, SC-30) đã được phân xử ở trên. Bất đồng ở SC-5 được ghi nhận là chưa giải quyết, nhưng hành động bắt buộc không bị tranh chấp. Không có DA CRITICAL nào. Mọi ghế đều chạy trên cùng một họ mô hình, nên khả năng sai số tương quan giữa các ghế không loại trừ được (xem phần Provenance).

---

## Required Revisions * (Must Fix)

Không có block manifest hoặc `base_draft_sha256` nào được cung cấp cho lượt này, nên mọi mục ghi `proposed_targets: [BLOCK-MANIFEST-UNAVAILABLE]`. Vị trí được nêu bằng locator mục/bảng/phương trình của đề cương. Artifact máy `revision-roadmap/1.0` **không** được phát hành trong lượt này vì thiếu hai giá trị băm bắt buộc. Bảng dưới đây là lõi lộ trình ở dạng người đọc.

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| R1 (REV-01) | Viết lại tuyên bố khoảng trống ở §4.2(1)–(4) ở dạng hẹp; phân biệt với Tu (2010), Avramov (2002), Kan và Zhou (2007) | SC-1 | major | `text: §4.2(2) "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục"` | 4 — EIC; 4 — R2 | EIC W1; R2 W1; DA M8 | must_fix | section: §4.2(1)–(4), §4.4 | claim_scope_unsupported → claim: tuyên bố khoảng trống §4.2 |
| R2 (REV-02) | Ước tính trước số cửa sổ căng thẳng (chỉ dùng HMM) và mô phỏng công suất trước khi đăng ký trước | SC-2 | major | `text: §4.3.10 "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10"` | 3 — EIC; 4 — R1 | EIC W2; R1 W1; DA M4 | must_fix | re_analysis: §4.3.6, §4.3.10 (HMM-only + mô phỏng) | evidence_gap_remains → claim: H1 / Câu hỏi 1 |
| R3 (REV-03) | Nêu đóng góp còn lại trong kịch bản "không kết luận" | SC-3 | major | `text: §4.3.6 "dự kiến có khoảng 28 cửa sổ đánh giá độc lập"` | 3 — EIC | EIC W2 | must_fix | section: §4.4, §4.3.10 | claim_scope_unsupported → section: §4.4 Đóng góp dự kiến |
| R4 (REV-05) | Viết lại §5 và §4.4 cho khớp tỷ trọng thực của chiều hành vi và quản lý | SC-5 (SPLIT) | minor (EIC W4) / major (R3 W2) — bất đồng chưa giải quyết | `text: §5, đoạn 1 "tập trung vào kinh tế hành vi và quản lý trong lĩnh vực kinh tế"` | 3 — EIC; 3 — R3 | EIC W4; R3 W2 | must_fix | section: §5, §4.4 | claim_scope_unsupported → claim: giao điểm liên ngành §5 |
| R5 (REV-06) | Tuyên bố tách bạch luận án với bản thảo 1, 5, 6 và cam kết trích dẫn chéo | SC-6 (SPLIT) | minor (EIC W5) / major (R3 W6) | `table: Bảng 7, hàng 1, 5 và 6, cột "Liên quan đến đề tài" = "Có"` | 4 — EIC; 3 — R3 | EIC W5; R3 W6 | must_fix | sentence: §4.4 hoặc §7.3 | reporting_requirement_unmet → table: Bảng 7 |
| R6 (REV-11) | Định nghĩa "cửa sổ căng thẳng" (ngưỡng S_t) và đăng ký trước | SC-11 | major | `text: §4.3.10 "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận"` | 4 — R1 | R1 W1; DA M4 | must_fix | sentence: §4.3.10 | method_reproducibility_unresolved → section: §4.3.10 |
| R7 (REV-12) | Định nghĩa chính xác mẫu số chuẩn hóa (cặp, tần suất, độ dài khối, số lần lặp) | SC-12 | major | `text: §4.3.6 "cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình trong cùng cửa sổ"` | 4 — R1 | R1 W2 | must_fix | section: §4.3.6 | method_reproducibility_unresolved → section: §4.3.6 |
| R8 (REV-13) | Báo cáo song song regret thô và chuẩn hóa; nêu trước biến kết quả chính và cách đọc khi hai thước đo bất đồng | SC-13 | major | `text: §4.3.6 "phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap"` (DA M9) | 4 — R1 | R1 W2; DA M9 | must_fix | section: §4.3.6, §4.1 | interpretive_ambiguity_remains → claim: H1 (đơn vị thước đo) |
| R9 (REV-14) | Định nghĩa lại phân phối rỗng theo CE (cả trung bình và phương sai); nêu rõ thủ tục tái lấy mẫu; kiểm tra size bằng mô phỏng | SC-14 | major | `text: §4.3.7 "loại chênh lệch trung bình giữa các mô hình trong từng chế độ nhưng giữ nguyên tương quan chéo và biến động"` | 4 — R1 | R1 W3; DA (giải thích thay thế 2) | must_fix | re_analysis: §4.3.7 | evidence_gap_remains → claim: điều kiện 1 ủng hộ H1 |
| R10 (REV-15) | Tách bước thử khỏi mẫu xác nhận (HMM/dữ liệu mô phỏng hoặc trước 2012); khai các tham số chọn sau khi xem kết quả | SC-15 | major | `table: Bảng 5, hàng Năm 1 — "ước lượng thử bảy mô hình trên giai đoạn 2019--2025"` | 4 — R1 | R1 W4; DA M3 | must_fix | section: Bảng 5, §4.3.5, §4.3.6 | claim_scope_unsupported → claim: "phân tích xác nhận có đăng ký trước" |
| R11 (REV-16) | Giới hạn số biến mỗi phương trình; HAC hiệu chỉnh mẫu nhỏ; quy tắc độ dài khối ấn định trước | SC-16 | major | `text: §4.3.6 "đề tài dự kiến có khoảng 28 cửa sổ đánh giá độc lập"` | 4 — R1 | R1 W5 | must_fix | section: §4.3.7 | evidence_gap_remains → claim: H2, H4 (khoảng tin cậy) |
| R12 (REV-17) | Tách đóng góp của biến động khỏi các kênh (ví dụ Gelbach); đổi ngôn ngữ "phần được giải thích" | SC-17 | major | `equation: Eq. (5) và hiệu β0 − β1 ở mục 4.3.7` | 4 — R1 | R1 W6; DA M2 | must_fix | section: §4.3.7, §4.1 (Câu hỏi 2) | claim_scope_unsupported → claim: Câu hỏi 2 |
| R13 (REV-18) | Nêu trước "hai phương trình tách riêng" và tiêu chí H2 trong nhánh VIF cao | SC-18 | major | `text: §4.3.7 "Khi hệ số này vượt ngưỡng, đề tài báo cáo hai phương trình tách riêng và không diễn giải riêng từng hệ số"` | 4 — R1 | R1 W7; DA M1 (một phần) | must_fix | section: §4.3.7 | acceptance_criterion_unmet → claim: tiêu chí ủng hộ H2 |
| R14 (REV-19) | Giữ tập M cố định giữa H1 và H3 hoặc nêu rõ M thu gọn; định nghĩa chuẩn đối chứng "chọn một mô hình" | SC-19 | major | `text: §4.3.8 "nên mức hối tiếc của hai cơ chế này có thể âm"` | 4 — R1 | R1 W8; DA M7 | must_fix | section: §4.3.8 | interpretive_ambiguity_remains → claim: H3 |
| R15 (REV-20) | Mỗi giả thuyết xác nhận có một thống kê và p-value; Holm cho H1–H3; thống nhất α | SC-20 | major | `text: §4.3.10 "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết"` | 3 — R1 | R1 W9 | must_fix | section: §4.3.10 | acceptance_criterion_unmet → section: §4.3.10 quy tắc kết luận |
| R16 (REV-23) | Thêm ít nhất một quy tắc chọn thay thế hoặc thước đo không phụ thuộc quy tắc (U_o − Ū_t), hoặc thu hẹp tuyên bố | SC-23 | minor (R1 W12); DA M6 = major | `text: §4.3.6 "chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước"` | 4 — R1; 4 — DA | R1 W12; DA M6 | must_fix | re_analysis: §4.3.6, §4.3.2, §4.3.10 | claim_scope_unsupported → claim: H1 khái quát hóa "rủi ro lựa chọn mô hình" |
| R17 (REV-30) | Tách cơ sở lý thuyết: maxmin/robust control cho cơ chế (ii); minimax regret/regret theory cho thước đo regret | SC-30 (SPLIT) | major (R2 W2) / minor (R3 W5) — phân xử: major | `text: §4.3.1 "cung cấp cách đo tổn thất của một lựa chọn so với lựa chọn tốt nhất nhìn lại sau thực tế"` | 4 — R2; 4 — R3 | R2 W2; R3 W5 | must_fix | section: §4.3.1 | claim_scope_unsupported → section: §4.3.1 khung lý thuyết |
| R18 (REV-31) | Lý giải tính đại diện của tập M; thêm phương sai nhỏ nhất mẫu và một chiến lược định thời biến động (vào M hoặc kiểm tra độ bền); thảo luận ràng buộc chỉ mua như co rút ngầm | SC-31 | major | `text: §4.3.5 và §4.4 "Tập này bao phủ các hướng chính của tài liệu"` | 4 — R2 | R2 W3 | must_fix | re_analysis: §4.3.5, §4.4, Bảng 3 | claim_scope_unsupported → claim: "bao phủ các hướng chính" |
| R19 (REV-39) | Xác lập tiền đề về mức dùng mô hình định lượng của công ty quản lý quỹ (phân tích tài liệu công bố) hoặc định vị lại người dùng | SC-39 | major | `text: §4.1, đoạn 4 "Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này"` | 4 — R3 | R3 W1; DA (Tiền đề chưa kiểm tra) | must_fix | section: §4.1, §4.4, §6 | claim_scope_unsupported → claim: hàm ý quản trị |
| R20 (REV-44) | Nêu thời điểm hoàn thành hoặc tạm dừng các chương trình học song song so với mốc năm 1 | SC-44 | major | `text: §8.2, đoạn 1 "Thí sinh đang theo học ngành Kế toán hệ vừa làm vừa học tại Đại học Kinh tế Quốc dân (năm thứ ba)"` | 3 — R3 | R3 W6 | must_fix | section: §7.4 | reporting_requirement_unmet → section: §7.4 kế hoạch |
| R21 (REV-48) | Nêu rõ β nào (β0 hay β1) là phép kiểm định H1 trong tệp đăng ký trước; xử lý việc kiểm soát biến động thực hiện khi chế độ được định nghĩa bằng phương sai | — | major | `text: §4.3.4 "Chế độ căng thẳng là chế độ có phương sai điều kiện cao nhất"; §4.3.7 "Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát"` | 4 — DA | DA M1 | must_fix | section: §4.3.7, Bảng 2 (H1) | acceptance_criterion_unmet → claim: H1 |

### Required Item Details

**R1: Thu hẹp tuyên bố khoảng trống**
- **Problem**: Các câu kết ở §4.2(1)–(4) ("chưa thước đo nào", "chưa công trình nào") mâu thuẫn với Tu (2010) và Avramov (2002), cả hai được mô tả ngay trong §4.2.
- **Source**: EIC W1; R2 W1 (bổ sung Kan và Zhou, 2007); DA M8.
- **Requirement**: Viết lại các câu kết theo mức giới hạn của câu cuối §4.2. Thêm đoạn phân biệt đề tài với các công trình đó (tập cạnh tranh nhiều mô hình, theo chế độ, thị trường cận biên).
- **Acceptance criteria**: Không còn khẳng định khoảng trống tuyệt đối không giới hạn ở §4.2; có đoạn đối chiếu nêu tên Tu (2010), Avramov (2002), Kan và Zhou (2007) và điểm khác biệt cụ thể.

**R2: Ước tính số cửa sổ căng thẳng và công suất**
- **Problem**: Khoảng 28 cửa sổ so với ngưỡng 10 cửa sổ căng thẳng khiến kịch bản "không kết luận" cho H1 có xác suất đáng kể. Chưa có phân tích công suất.
- **Source**: EIC W2; R1 W1 (kèm phép tính định hướng); DA M4.
- **Requirement**: Trước đăng ký trước, chỉ chạy HMM để đếm số cửa sổ căng thẳng khả dĩ. Mô phỏng công suất với cùng số cửa sổ và cấu trúc tự tương quan. Nếu công suất quá thấp, cân nhắc cửa sổ 3 tháng hoặc cửa sổ trượt.
- **Acceptance criteria**: Đề cương báo cáo số cửa sổ căng thẳng kỳ vọng và hiệu ứng nhỏ nhất phát hiện được, cùng phương án định trước khi dưới ngưỡng.

**R3: Đóng góp trong kịch bản "không kết luận"**
- **Problem**: Đề cương chưa nói luận án và Bài báo 1 còn đóng góp gì nếu H1 không kết luận.
- **Source**: EIC W2.
- **Requirement**: Nêu rõ đóng góp còn lại (thước đo, bộ dữ liệu, ước lượng khoảng). Tùy tác giả chọn: thêm một thị trường so sánh hoặc một nghiên cứu mô phỏng có chế độ đã biết.
- **Acceptance criteria**: §4.4 có một đoạn mô tả đóng góp dự kiến riêng cho kịch bản "không kết luận".

**R4: Viết lại tuyên bố liên ngành ở §5**
- **Problem**: §5 nêu chương trình "tập trung vào kinh tế hành vi và quản lý", nhưng chiều hành vi chỉ là H4 thăm dò và chiều quản lý là thủ tục chưa kiểm nghiệm.
- **Source**: EIC W4 (Minor); R3 W2 (Major). Mức độ là bất đồng chưa giải quyết.
- **Requirement**: Viết lại §5 và §4.4 cho đúng tầm. Việc thêm cấu phần định tính (phương án b của R3) do tác giả và người hướng dẫn quyết định.
- **Acceptance criteria**: §5 và §4.4 mô tả nhất quán tỷ trọng các chiều hành vi và quản lý so với thiết kế ở §4.3.

**R5: Tách bạch với các bản thảo đang phản biện**
- **Problem**: Bảng 7 ghi bản thảo 1, 5, 6 liên quan trực tiếp, trong đó bản 5 và 6 trùng biến kênh H2, nhưng cam kết ở §4.4 chỉ nói về Nguyen và Nguyen (2026a).
- **Source**: EIC W5; R3 W6.
- **Requirement**: Nêu phần nào được dùng lại làm công cụ, phần nào là kết quả mới, và cam kết trích dẫn chéo.
- **Acceptance criteria**: §4.4 hoặc §7.3 có tuyên bố nêu tên bản thảo 1, 5, 6 và phân định phạm vi dùng lại.

**R6: Định nghĩa "cửa sổ căng thẳng"**
- **Problem**: S_t là tỷ lệ liên tục, nhưng quy tắc lại đếm cửa sổ căng thẳng như phân loại nhị phân.
- **Source**: R1 W1; DA M4.
- **Requirement**: Nêu ngưỡng (ví dụ S_t ≥ 0,5) và đăng ký trước.
- **Acceptance criteria**: §4.3.10 chứa ngưỡng phân loại cửa sổ căng thẳng được ấn định trước.

**R7: Định nghĩa mẫu số chuẩn hóa**
- **Problem**: Có 21 cặp chênh lệch, nhưng đề cương không nói dùng cặp nào, tần suất nào, độ dài khối và số lần lặp ra sao.
- **Source**: R1 W2.
- **Requirement**: Nêu công thức, cặp, tần suất, độ dài khối, số lần lặp và đăng ký trước.
- **Acceptance criteria**: §4.3.6 có công thức mẫu số đủ để người khác tái lập.

**R8: Báo cáo song song regret thô và chuẩn hóa**
- **Problem**: Chia cho sai số chuẩn (vốn tăng theo biến động) có thể loại chính tín hiệu cần đo, và làm thước đo mất đơn vị tổn thất mà định nghĩa ở §4.1 yêu cầu.
- **Source**: R1 W2; DA M9 (R3 W4 nêu cùng hướng sửa dưới góc người dùng, xem S23).
- **Requirement**: Báo cáo cả hai dạng, nêu biến kết quả chính và cách diễn giải định trước khi hai dạng bất đồng.
- **Acceptance criteria**: §4.3.6 nêu rõ biến kết quả chính và quy tắc đọc khi regret thô và regret chuẩn hóa cho kết luận khác nhau.

**R9: Phân phối rỗng trung tính theo CE**
- **Problem**: Phân phối rỗng chỉ loại chênh lệch trung bình, nhưng CE còn chứa số hạng ρ/2·σ², nên dưới H0 các mô hình vẫn khác nhau. Thủ tục tái lấy mẫu chưa rõ, và có nguy cơ vòng lặp với S_t.
- **Source**: R1 W3; DA (giải thích thay thế 2, khuếch đại cơ học qua ρ/2·σ²).
- **Requirement**: Định nghĩa H0 sao cho CE kỳ vọng bằng nhau. Nêu thủ tục khối (theo chế độ hay toàn chuỗi, có tái ước lượng S_t hay không). Kiểm tra size bằng mô phỏng.
- **Acceptance criteria**: §4.3.7 mô tả H0 theo CE, thủ tục tái lấy mẫu và kết quả kiểm tra size dự kiến.

**R10: Trình tự đăng ký trước**
- **Problem**: Ước lượng thử bảy mô hình trên 2019–2025 ở quý 2 diễn ra trước đăng ký ở quý 4, và độ dài cửa sổ được biện minh sau lần thử. Mẫu kiểm tra sau đăng ký quá ngắn.
- **Source**: R1 W4; DA M3.
- **Requirement**: Trước đăng ký, chỉ chạy HMM hoặc dữ liệu mô phỏng hoặc dữ liệu không dùng để kiểm định. Nếu vẫn thử trên 2019–2025, khai rõ các tham số chọn sau khi xem kết quả và gắn nhãn thăm dò.
- **Acceptance criteria**: Bảng 5 và §4.3.5 không còn ước lượng CE/regret trên mẫu xác nhận trước đăng ký, hoặc có danh mục khai báo tham số hậu nghiệm.

**R11: Suy luận mẫu nhỏ**
- **Problem**: Khoảng 7 tham số trên khoảng 28 quan sát; HAC thiên lệch xuống; bootstrap khối có rất ít khối.
- **Source**: R1 W5.
- **Requirement**: Giới hạn biến mỗi phương trình. Dùng HAC hiệu chỉnh mẫu nhỏ. Ấn định quy tắc độ dài khối. Cân nhắc dữ liệu tháng cho hồi quy kênh.
- **Acceptance criteria**: §4.3.7 nêu đặc tả phương trình, thủ tục sai số chuẩn và quy tắc độ dài khối đã ấn định.

**R12: Phân rã β0 − β1**
- **Problem**: X_t luôn chứa biến động thực hiện, nên β0 − β1 gán phần biến động hấp thụ cho "biến kênh". Đây là vấn đề bad control.
- **Source**: R1 W6; DA M2.
- **Requirement**: Tách đóng góp của biến động (ví dụ phân rã Gelbach). Diễn đạt là "mức thay đổi của β khi thêm X".
- **Acceptance criteria**: Câu hỏi 2 và §4.3.7 không còn dùng "phần chênh lệch được giải thích" mà không có phân rã theo từng khối biến.

**R13: Quy tắc VIF và tiêu chí H2**
- **Problem**: Khi VIF > 5, đề cương không diễn giải từng hệ số, trong khi tiêu chí H2 cần đọc từng hệ số.
- **Source**: R1 W7; DA M1 (hệ quả tương tự cho H1).
- **Requirement**: Nêu trước nội dung hai phương trình tách riêng và tiêu chí H2 trong nhánh VIF cao. Cân nhắc bỏ S_t khỏi phương trình H2 hoặc trực giao hóa.
- **Acceptance criteria**: §4.3.7 có tiêu chí ủng hộ H2 cho cả hai nhánh VIF.

**R14: Tập so sánh của H3**
- **Problem**: Cơ chế (ii) và (iii) chính là M6 và M7. Loại chúng khỏi M làm thay đổi tập so sánh, và H3 trở thành một cuộc đua mô hình.
- **Source**: R1 W8; DA M7.
- **Requirement**: Giữ M cố định hoặc nêu rõ M thu gọn. Định nghĩa chuẩn đối chứng bằng quy tắc c. Nêu cách chọn cơ chế ex ante.
- **Acceptance criteria**: §4.3.8 định nghĩa rõ tập M của H3 và chuẩn đối chứng.

**R15: Mức ý nghĩa và Holm**
- **Problem**: Holm cần p-value cho từng giả thuyết, nhưng tiêu chí ủng hộ là ghép nhiều điều kiện. Mức 5% của phân vị không khớp mức 10% của Holm. H4 thăm dò vẫn nằm trong họ giả thuyết.
- **Source**: R1 W9.
- **Requirement**: Mỗi giả thuyết xác nhận có một thống kê và p-value. Áp Holm cho H1–H3. Thống nhất α.
- **Acceptance criteria**: §4.3.10 định nghĩa một p-value duy nhất cho mỗi giả thuyết H1–H3, cùng một mức α thống nhất.

**R16: Quy tắc chọn duy nhất**
- **Problem**: R_t gắn với quy tắc "người thắng 36 tháng trước". Giải thích đối thủ ("quy tắc đuổi theo thành tích thất bại tại điểm chuyển") chưa được loại trừ.
- **Source**: R1 W12 (Minor); DA M6 (Major, "Core Thesis Challenge").
- **Requirement**: Thêm ít nhất một quy tắc chọn không nhìn lùi theo thành tích, hoặc báo cáo U_o − Ū_t. Kiểm tra độ nhạy với cửa sổ chọn 12, 24, 60 tháng. Nếu không, thu hẹp tuyên bố.
- **Acceptance criteria**: §4.3.2 nêu giải thích đối thủ, và §4.3.10 có ít nhất một quy tắc chọn thay thế trong kiểm tra độ bền, hoặc tuyên bố H1 được giới hạn vào quy tắc 36 tháng.

**R17: Cơ sở lý thuyết của regret**
- **Problem**: §4.3.1 gán regret cho maxmin và robust control.
- **Source**: R2 W2; R3 W5 (đã phân xử ở mức Major).
- **Requirement**: Tách maxmin/robust control (cơ sở của cơ chế ii) khỏi minimax regret/regret theory (cơ sở của thước đo). Nói rõ đây là regret ex post trên tập M.
- **Acceptance criteria**: §4.3.1 dẫn nguồn minimax regret cho thước đo regret (tác giả tự xác minh nguồn), và không còn gán regret cho Gilboa–Schmeidler hay Hansen–Sargent.

**R18: Tính đại diện của tập M**
- **Problem**: Tuyên bố "bao phủ các hướng chính" chưa đứng vững. Ràng buộc chỉ mua có thể nén khác biệt giữa M2, M3 và M6.
- **Source**: R2 W3.
- **Requirement**: Đổi tuyên bố thành "đại diện cho các hướng X, Y, Z". Thêm phương sai nhỏ nhất mẫu và một chiến lược định thời biến động. Thảo luận ràng buộc như co rút ngầm. Nêu rằng rủi ro lựa chọn mô hình là đại lượng tương đối theo M.
- **Acceptance criteria**: §4.3.5 và §4.4 có lý do chọn tập M và kế hoạch kiểm tra khi nới ràng buộc chỉ mua.

**R19: Tiền đề về người dùng**
- **Problem**: Hàm ý quản trị giả định công ty quản lý quỹ dùng mô hình định lượng, trong khi đề cương thừa nhận chưa biết điều này.
- **Source**: R3 W1; DA (tiền đề chưa kiểm tra).
- **Requirement**: Biến bước xác lập tiền đề thành cấu phần có sản phẩm (ví dụ phân tích bản cáo bạch và báo cáo quỹ mở), hoặc định vị lại người dùng, hoặc nói rõ hàm ý chỉ có tính chuẩn tắc.
- **Acceptance criteria**: §4.1, §4.4 hoặc §6 có kế hoạch xác lập tiền đề kèm phương án định vị lại khi tiền đề không đúng.

**R20: Khả thi thời gian**
- **Problem**: Thí sinh có nhiều chương trình học song song và chín bản thảo đang xét, nhưng kế hoạch năm 1 dày.
- **Source**: R3 W6.
- **Requirement**: Thêm đoạn ở §7.4 nêu thời điểm hoàn thành hoặc tạm dừng các cam kết song song.
- **Acceptance criteria**: §7.4 có mốc thời gian cho từng cam kết song song đối chiếu với Bảng 5.

**R21: Xác định hệ số kiểm định H1**
- **Problem**: Chế độ căng thẳng được định nghĩa bằng phương sai cao nhất, trong khi phương trình (5) luôn kiểm soát biến động thực hiện. Vì vậy β chỉ đo phần vượt ngoài biến động, khác với H1 ở Bảng 2.
- **Source**: DA M1.
- **Requirement**: Nêu rõ β0 hay β1 là phép kiểm định H1 trong tệp đăng ký trước, và lập luận về việc kiểm soát biến động thực hiện.
- **Acceptance criteria**: Bảng 2 và §4.3.7 nêu một hệ số duy nhất dùng để kiểm định H1, cùng lý do đặc tả.

---

## Suggested Revisions (Should Fix / Consider)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| S1 (REV-04) | Gọi tên đóng góp chính xác hơn ("phương pháp đo lường áp dụng") | SC-4 | minor | `text: §4.4 "Về lý thuyết, đề tài đưa ra khung khái niệm và thước đo rủi ro lựa chọn mô hình theo chế độ"` | 4 — EIC | EIC W3; R2 (Nhận xét chi tiết) | should_fix | sentence: §4.4 | claim_scope_unsupported → claim: đóng góp lý thuyết |
| S2 (REV-07) | Thống nhất người hướng dẫn giữa trang bìa và §10 | SC-7 | minor | `text: trang bìa "PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân"` | 5 — EIC | EIC W6 | should_fix | sentence: trang bìa, §10 | editorial_conformance_unmet → manuscript: trang bìa |
| S3 (REV-08) | Điền "Cơ quan công tác" và "Đơn vị công tác" | SC-8 | minor | `text: trang bìa "Cơ quan công tác:"` | 5 — EIC | EIC W7 | should_fix | sentence: trang bìa, mục 3 | editorial_conformance_unmet → manuscript: trang bìa |
| S4 (REV-09) | Kiểm tra Hình 3 và số chú thích hình, bảng trong bản nộp gốc | SC-9 | minor | `figure: Hình 3 (Quy trình nghiên cứu, §4.3.9)` | 2 — EIC | EIC W8 | should_fix | other (surface_id: figure_rendering): Hình 3, chú thích | reader_traceability_reduced → figure: Hình 3 |
| S5 (REV-10) | Thêm "(HOSE)" vào phụ đề hoặc nêu lý do giới hạn | SC-10 | minor | `text: §4.4 "Phạm vi không gian: cổ phiếu niêm yết trên HOSE."` | 4 — EIC | EIC W9 | should_fix | sentence: tiêu đề, §4.4 | claim_scope_unsupported → claim: tiêu đề |
| S6 (REV-21) | Đưa HMM vào vòng bootstrap (kiểm tra độ bền) hoặc báo cáo độ nhạy theo ngưỡng | SC-21 | minor | `text: §4.3.7 "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng đăng ký trước"` | 4 — R1 | R1 W10 | should_fix | re_analysis: §4.3.7 | evidence_gap_remains → claim: khoảng tin cậy của β |
| S7 (REV-22) | Định nghĩa "trọng số Bayes" cho cơ chế (i) | SC-22 | minor | `text: §4.3.8 "kết hợp các mô hình theo trọng số Bayes"` | 4 — R1 | R1 W11 | should_fix | sentence: §4.3.8 | method_reproducibility_unresolved → section: §4.3.8 |
| S8 (REV-24) | Nêu độ dài cửa sổ và quy tắc N/T cho dữ liệu tháng | SC-24 | minor | `text: §4.3.5 "tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5"` | 5 — R1 | R1 W13 | should_fix | sentence: §4.3.5 | method_reproducibility_unresolved → section: §4.3.5 |
| S9 (REV-25) | Nêu tần suất lợi suất, quy ước năm hóa, mức chi phí giao dịch cơ sở | SC-25 | minor | `absence: §4.3.6 và §4.3.8` (checked §4.3.3, 4.3.6, 4.3.7, 4.3.8, 4.3.10, Bảng 3) | 4 — R1 | R1 W14 | should_fix | sentence: §4.3.6, §4.3.8 | method_reproducibility_unresolved → section: §4.3.6 |
| S10 (REV-26) | Định nghĩa thao tác và đặt một tên thống nhất cho các biến kênh ở cấp cửa sổ | SC-26 | minor | `absence: §4.3.7` (checked §4.3.1, 4.3.3, 4.3.7, Bảng 2, Hình 1) | 4 — R1; 4 — R2 [CONFIDENCE-SOURCE: report-level] | R1 W15; R2 Vấn đề nhỏ 1 | should_fix | section: §4.3.7, Bảng 2 | method_reproducibility_unresolved → section: §4.3.7 |
| S11 (REV-27) | Quy tắc gán nhãn chế độ qua các lần ước lượng lại | SC-27 | minor | `text: §4.3.4 "Chế độ căng thẳng là chế độ có phương sai điều kiện cao nhất và lợi suất kỳ vọng thấp hơn chế độ bình thường"` | 4 — R1 | R1 W16 | should_fix | sentence: §4.3.4 | method_reproducibility_unresolved → section: §4.3.4 |
| S12 (REV-28) | Sửa diễn giải kết quả không bác bỏ (dùng hiệu ứng nhỏ nhất phát hiện được hoặc TOST) | SC-28 | minor | `text: §4.3.10 "khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam"` | 4 — R1 | R1 W17; DA Minor (i) | should_fix | sentence: §4.3.10 | claim_scope_unsupported → claim: diễn giải khi bác bỏ |
| S13 (REV-29) | Lập luận lại cơ chế và dấu của kênh tương quan đuôi; nêu cách diễn giải khi các kênh bù trừ | SC-29 | minor (R1, R2); DA M5 = major | `table: Bảng 2, hàng H2 — "hệ số của tương quan đuôi âm (tương quan cao làm các danh mục chỉ mua hội tụ)"` | 3 — R1; 4 — R2 | R1 W18; R2 W4; DA M5 | should_fix | section: §4.3.1, Bảng 2, Hình 1 | interpretive_ambiguity_remains → claim: H2 |
| S14 (REV-32) | Đổi biến H4 sang hệ số bầy đàn CSAD hoặc bỏ cách diễn giải bầy đàn | SC-32 | minor | `text: §4.4 "độ phân tán chéo của lợi suất, một thước đo bầy đàn ở cấp thị trường"` | 4 — R2 | R2 W5 | should_fix | section: §4.4, Bảng 2 (H4) | claim_scope_unsupported → claim: H4 |
| S15 (REV-33) | Đối chiếu toàn văn Kerkhof và cộng sự (2010) (ba thành phần?) | SC-33 | minor | `text: §4.2(2) "tách rủi ro mô hình thành rủi ro ước lượng và rủi ro đặc tả sai"` | 3 — R2 | R2 W6 | should_fix | sentence: §4.2(2) | evidence_gap_remains → claim: mô tả Kerkhof (2010) |
| S16 (REV-34) | Ghi rõ áp dụng Ledoit–Wolf (2008) là mở rộng cho CE | SC-34 | minor | `text: §4.3.7 "so sánh lợi suất tương đương chắc chắn và tỷ số Sharpe giữa các mô hình bằng khoảng tin cậy bootstrap chuỗi thời gian"` | 4 — R2 | R2 W7 | should_fix | sentence: §4.3.7 | reader_traceability_reduced → section: §4.3.7 |
| S17 (REV-35) | Thảo luận vi cấu trúc HOSE (biên độ giá) và kiểm tra độ bền trên lợi suất tuần | SC-35 | minor [FIELD-NORM UNVERIFIED] | `absence: §4.3.3, §4.3.4, §4.3.10` (checked §4.1, 4.3.3, 4.3.4, 4.3.7, 4.3.10, 4.4) | 3 — R2 | R2 W8 | consider | section: §4.3.4 | evidence_gap_remains → section: §4.3.4 |
| S18 (REV-36) | Nói rõ cách dùng hiệu chỉnh Forbes–Rigobon như chuỗi thời gian một thị trường | SC-36 | minor [SEVERITY-SOURCE: letter-fallback] | R2 Vấn đề nhỏ 2 (§4.3.7) | 4 [CONFIDENCE-SOURCE: report-level] — R2 | R2 Vấn đề nhỏ 2 | consider | sentence: §4.3.7 | method_reproducibility_unresolved → section: §4.3.7 |
| S19 (REV-37) | Dùng từ "nhận diện" thay "dự báo" cho Kritzman và cộng sự (2012) | SC-37 | minor [SEVERITY-SOURCE: letter-fallback] | R2 Vấn đề nhỏ 3 | 4 [CONFIDENCE-SOURCE: report-level] — R2 | R2 Vấn đề nhỏ 3 | consider | sentence: §4.2 | reader_traceability_reduced → claim: mô tả Kritzman (2012) |
| S20 (REV-38) | Cập nhật câu "Dựa trên phần tóm tắt" sau khi đọc toàn văn | SC-38 | minor [SEVERITY-SOURCE: letter-fallback] | R2 Vấn đề nhỏ 4 (§4.4) | 4 [CONFIDENCE-SOURCE: report-level] — R2 | R2 Vấn đề nhỏ 4 | consider | sentence: §4.4 | evidence_gap_remains → section: §4.4 |
| S21 (REV-40) | Biện minh quy tắc chọn 36 tháng như một giả định hành vi hoặc quy tắc chuẩn tắc | SC-40 | major | `text: §5 và §4.4 "Đề tài không quan sát hành vi chọn mô hình của từng tổ chức đầu tư."` | 3 — R3 | R3 W2; Assumption Audit (ii) | should_fix | section: §4.3.6, §4.4 | claim_scope_unsupported → claim: quy tắc chọn trước |
| S22 (REV-41) | Ánh xạ thủ tục giám sát vào khung MRM (ngưỡng, tần suất, chủ thể, thẩm định độc lập, chi phí tín hiệu sai) | SC-41 | minor | `text: §4.4 "kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng"` | 4 — R3 | R3 W3 | should_fix | section: §4.4 (kế hoạch chương 6.5) | claim_scope_unsupported → claim: thủ tục giám sát |
| S23 (REV-42) | Báo cáo regret thô (điểm % năm hóa) cho phần hàm ý quản trị | SC-42 | minor; DA M9 = major | `equation: Eq. (4) và §4.3.6, đoạn 4` | 3 — R3 | R3 W4; DA M9 | should_fix | section: §4.3.6 | interpretive_ambiguity_remains → claim: hàm ý quản trị |
| S24 (REV-43) | Phân biệt nghĩa thống kê của "mức hối tiếc" với regret theory hành vi | SC-43 | minor | `text: §4.1, đoạn 2 "chênh lệch giữa kết quả của mô hình tốt nhất nhìn lại sau thực tế và kết quả của mô hình đã chọn"` | 4 — R3 | R3 W5 | should_fix | sentence: §4.1 | reader_traceability_reduced → section: §4.1 |
| S25 (REV-45) | Nêu tên nhà cung cấp dữ liệu, điều khoản chia sẻ, hoặc phiên bản trên dữ liệu công khai | SC-45 | minor | `text: §4.3.3, đoạn 1 "Nguồn dữ liệu là HOSE và một nhà cung cấp dữ liệu thương mại."` | 3 — R3 | R3 W7 | should_fix | sentence: §4.3.3 | method_reproducibility_unresolved → dataset: dữ liệu thương mại |
| S26 (REV-46) | Nêu cơ quan quản lý cụ thể và góc nhìn người nắm chứng chỉ quỹ | SC-46 | minor | `text: §4.4 "chỉ là tư liệu tham khảo cho tổ chức đầu tư và cơ quan giám sát"` | 3 — R3 | R3 W8 | consider | sentence: §4.4 (kế hoạch chương 6.6) | reader_traceability_reduced → section: §4.4 |
| S27 (REV-47) | Bàn ngắn rủi ro hành vi đồng loạt khi nhiều tổ chức cùng kích hoạt quy tắc theo chế độ | SC-47 | minor [SEVERITY-SOURCE: letter-fallback] | R3 Broader Implications ("Tác động xã hội") | 3 [CONFIDENCE-SOURCE: report-level] — R3 | R3 Detailed Comments | consider | sentence: kế hoạch chương 6.6 | interpretive_ambiguity_remains → section: hàm ý chính sách |
| S28 (REV-49) | Thống nhất vai trò của độ phân tán và tập tin cậy mô hình (chỉ báo bất định hay đầu vào giám sát và điều kiện H1) | — | minor | DA Minor (ii): §4.1 "chỉ báo hiệu mức bất định, không đo rủi ro" và §4.4 "đo độ phân tán và tập tin cậy mô hình định kỳ" | không công bố trong thẻ DA [CONFIDENCE-SOURCE: unavailable] | DA Minor (ii) | should_fix | sentence: §4.1, §4.4, Bảng 2 | interpretive_ambiguity_remains → claim: vai trò D_t và MCS |

Câu hỏi cho tác giả (kênh `question`; tác giả phải trả lời, chi tiết trong ma trận R&R): R1 Q1–Q4, R2 Q1–Q4, R3 Q1–Q4. EIC và DA không đặt câu hỏi.

---

## Revision Roadmap *

### Source-traceability checklist

Danh sách theo thứ tự nguồn bất biến (EIC → R1 → R2 → R3 → DA, sau đó theo số W). Thứ tự này không phải thứ tự làm việc. Tác giả sẽ chọn `will_address`, `wont_address` hoặc `not_on_point` ở bước phân xử của tác giả sau đó, trong sidecar riêng.

- [ ] R1 (REV-01) — obligation `must_fix`: Thu hẹp tuyên bố khoảng trống §4.2
- [ ] R2 (REV-02) — obligation `must_fix`: Ước tính số cửa sổ căng thẳng và công suất
- [ ] R3 (REV-03) — obligation `must_fix`: Đóng góp trong kịch bản "không kết luận"
- [ ] S1 (REV-04) — obligation `should_fix`: Gọi tên đóng góp chính xác
- [ ] R4 (REV-05) — obligation `must_fix`: Viết lại tuyên bố liên ngành §5 và §4.4
- [ ] R5 (REV-06) — obligation `must_fix`: Tách bạch với bản thảo 1, 5, 6
- [ ] S2 (REV-07) — obligation `should_fix`: Thống nhất người hướng dẫn
- [ ] S3 (REV-08) — obligation `should_fix`: Điền trường để trống
- [ ] S4 (REV-09) — obligation `should_fix`: Kiểm tra Hình 3 và số chú thích
- [ ] S5 (REV-10) — obligation `should_fix`: Tiêu đề và phạm vi HOSE
- [ ] R6 (REV-11) — obligation `must_fix`: Định nghĩa cửa sổ căng thẳng
- [ ] R7 (REV-12) — obligation `must_fix`: Định nghĩa mẫu số chuẩn hóa
- [ ] R8 (REV-13) — obligation `must_fix`: Regret thô và chuẩn hóa song song
- [ ] R9 (REV-14) — obligation `must_fix`: Phân phối rỗng theo CE
- [ ] R10 (REV-15) — obligation `must_fix`: Trình tự đăng ký trước
- [ ] R11 (REV-16) — obligation `must_fix`: Suy luận mẫu nhỏ
- [ ] R12 (REV-17) — obligation `must_fix`: Phân rã β0 − β1
- [ ] R13 (REV-18) — obligation `must_fix`: Quy tắc VIF và tiêu chí H2
- [ ] R14 (REV-19) — obligation `must_fix`: Tập so sánh H3
- [ ] R15 (REV-20) — obligation `must_fix`: α và Holm
- [ ] S6 (REV-21) — obligation `should_fix`: Bất định của S_t
- [ ] S7 (REV-22) — obligation `should_fix`: Trọng số Bayes
- [ ] R16 (REV-23) — obligation `must_fix`: Quy tắc chọn thay thế
- [ ] S8 (REV-24) — obligation `should_fix`: N/T cho dữ liệu tháng
- [ ] S9 (REV-25) — obligation `should_fix`: Tần suất, năm hóa, chi phí
- [ ] S10 (REV-26) — obligation `should_fix`: Định nghĩa biến kênh
- [ ] S11 (REV-27) — obligation `should_fix`: Gán nhãn chế độ
- [ ] S12 (REV-28) — obligation `should_fix`: Diễn giải kết quả không bác bỏ
- [ ] S13 (REV-29) — obligation `should_fix`: Dấu kênh tương quan đuôi
- [ ] R17 (REV-30) — obligation `must_fix`: Cơ sở lý thuyết của regret
- [ ] R18 (REV-31) — obligation `must_fix`: Tính đại diện của tập M
- [ ] S14 (REV-32) — obligation `should_fix`: Thước đo bầy đàn H4
- [ ] S15 (REV-33) — obligation `should_fix`: Kerkhof (2010)
- [ ] S16 (REV-34) — obligation `should_fix`: Ledoit–Wolf cho CE
- [ ] S17 (REV-35) — obligation `consider`: Vi cấu trúc HOSE
- [ ] S18 (REV-36) — obligation `consider`: Forbes–Rigobon chuỗi thời gian
- [ ] S19 (REV-37) — obligation `consider`: Kritzman "nhận diện"
- [ ] S20 (REV-38) — obligation `consider`: Cập nhật sau đọc toàn văn
- [ ] R19 (REV-39) — obligation `must_fix`: Tiền đề về người dùng
- [ ] S21 (REV-40) — obligation `should_fix`: Biện minh quy tắc 36 tháng
- [ ] S22 (REV-41) — obligation `should_fix`: Thủ tục giám sát theo khung MRM
- [ ] S23 (REV-42) — obligation `should_fix`: Regret thô cho hàm ý quản trị
- [ ] S24 (REV-43) — obligation `should_fix`: Nghĩa hành vi của regret
- [ ] R20 (REV-44) — obligation `must_fix`: Khả thi thời gian
- [ ] S25 (REV-45) — obligation `should_fix`: Giấy phép dữ liệu
- [ ] S26 (REV-46) — obligation `consider`: Bên liên quan
- [ ] S27 (REV-47) — obligation `consider`: Rủi ro hành vi đồng loạt
- [ ] R21 (REV-48) — obligation `must_fix`: Hệ số kiểm định H1
- [ ] S28 (REV-49) — obligation `should_fix`: Vai trò D_t và MCS

Tổng: 49 mục (must_fix 21, should_fix 22, consider 6). Thông tin cho artifact máy (chưa phát hành): `consensus_summary` = "Không có CONSENSUS-3/4; 5 phát hiện chứng thực 2/4 (SC-1, SC-2, SC-4, SC-26, SC-29); 3 SPLIT về mức độ (SC-5, SC-6, SC-30)"; `dissenting_opinions` = [SC-5 bất đồng mức độ EIC Minor và R3 Major, chưa giải quyết].

---

## Journal-Supplied Deadline (Optional Transport)

- **Exact deadline from source letter**: `NOT PROVIDED`
- Không suy ra hạn chót, thời lượng hay ước tính khối lượng công việc.

---

## Response Letter Instructions

Vui lòng dùng định dạng của `templates/revision_response_template.md` để phản hồi từng mục. Ma trận R&R đi kèm (`rr_matrix.md`) đã dựng sẵn một dòng cho mỗi mục lộ trình.

**Phải bao gồm**:
1. Phản hồi và mô tả sửa đổi cho từng Required Revision (R1–R21)
2. Phản hồi cho từng Suggested Revision (S1–S28), dù có áp dụng hay không, kèm lý do nếu không áp dụng
3. Đánh dấu thay đổi trong bản sửa (track changes hoặc tô màu)
4. Bảng đối chiếu vị trí mới theo mục, bảng hoặc trang
5. Trả lời 12 câu hỏi của R1, R2, R3

---

## Closing

Chúng tôi khuyến khích tác giả cân nhắc kỹ các nhận xét và nộp một bản đề cương được sửa đổi đáng kể. Bản sửa sẽ được đưa qua một vòng phản biện lại. Hội đồng ghi nhận những điểm mạnh thực sự mà nhiều ghế cùng nêu: kỷ luật khái niệm (EIC S1, R2 S1, R3 S1), rổ cổ phiếu theo thời gian thực và xác suất lọc không nhìn trước (R1 S1, S2), lập luận chọn CE thay Sharpe (R1 S3, R2 S3), và mức tự khai minh bạch về tiếp xúc dữ liệu cũng như xung đột lợi ích (EIC S3, R1 S6, R3 S3). Phần lớn các sửa đổi bắt buộc làm được trước khi đăng ký trước mà không cần dữ liệu mới.

---

## Part 3: Reviewer Report Summary (Appendix)

### Journal-Fit Review Report Summary
- Recommendation: Major (tín hiệu sơ bộ) | Confidence: 4
- Key Point: Đề tài có cốt lõi đứng được, nhưng định vị đóng góp bị phóng đại (W1, W3) và chưa được bảo vệ trước kịch bản "không kết luận" (W2). Ngoài ra có các lỗi trình bày dễ sửa (W6–W9).

### Reviewer 1 (Methodology) Summary
- Recommendation: Không tường minh (D1 = block, repairable; D3 = warn) | Confidence: theo từng phát hiện, 3–5
- Key Point: Quy trình kiểm định H1 chưa tách được rủi ro lựa chọn tăng thật khỏi nhiễu ước lượng tăng ở chế độ căng thẳng (W1–W4). Mọi khuyết điểm đều sửa được trước đăng ký trước.

### Reviewer 2 (Domain) Summary
- Recommendation: Major Revision | Confidence: 4
- Key Point: Phần lớn công trình nền được mô tả đúng. Tuy vậy, tuyên bố khoảng trống dạng rộng mâu thuẫn với nguồn được trích (W1), regret được gán sai cơ sở lý thuyết (W2), và tập M chưa đại diện (W3).

### Reviewer 3 (Perspective) Summary
- Recommendation: Không tường minh (D4 = warn) | Confidence: 3
- Key Point: Cầu nối sang người dùng và các ngành lân cận còn yếu: tiền đề về người dùng chưa xác lập (W1), khẳng định liên ngành mạnh hơn thiết kế (W2), và khả thi thời gian chưa được đối chiếu (W6).

### Devil's Advocate Summary
- Recommendation: N/A — findings only
- Key Challenge: No unresolved Critical challenge. Phản luận mạnh nhất của DA (cấp Major) là: kết quả H1 có thể chỉ phản ánh thất bại của quy tắc đuổi theo thành tích 36 tháng tại điểm chuyển chế độ, cộng với việc chế độ trùng với biến động (M1, M6). Lập luận này được giữ hiển thị qua R16 và R21.

## Appendix: Full Reviewer Reports

Năm báo cáo đầy đủ nằm tại `phase2_eic.md`, `phase2_methodology.md`, `phase2_domain.md`, `phase2_perspective.md`, `phase2_da.md` (cùng thư mục với gói này).

## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body (partial)
Not in this input: English abstract, Chinese abstract.
Not checked:
- Body, line 346: HOSE (the initials before its parentheses do not spell it)
- Body, line 1112: VSTEP (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 1 | Not defined | GIA | 1 |
| Body | 1 | Not defined | QU | 3 |
| Body | 3 | Not defined | NG | 9 |
| Body | 3 | Not defined | TR | 4 |
| Body | 10 | Not defined | CH | 4 |
| Body | 10 | Not defined | DANH | 3 |
| Body | 10 | Not defined | NH | 2 |
| Body | 10 | Not defined | RO | 1 |
| Body | 10 | Not defined | TH | 2 |
| Body | 10 | Not defined | THEO | 1 |
| Body | 10 | Not defined | TRONG | 1 |
| Body | 11 | Not defined | KHO | 1 |
| Body | 11 | Not defined | NAM | 1 |
| Body | 13 | Not defined | NGHI | 1 |
| Body | 19 | Not defined | NGUY | 1 |
| Body | 19 | Not defined | TRUNG | 1 |
| Body | 25 | Not defined | PGS | 2 |
| Body | 25 | Not defined | TS | 3 |
| Body | 192 | Not defined | COVID | 3 |
| Body | 194 | Not defined | IV | 3 |
| Body | 202 | Not defined | SR | 4 |
| Body | 207 | Not defined | NHNN | 4 |
| Body | 207 | Not defined | TT | 6 |
| Body | 354 | Not defined | VN | 4 |
| Body | 399 | Not defined | IDEAS | 1 |
| Body | 399 | Not defined | RePEc | 1 |
| Body | 399 | Not defined | SSRN | 2 |
| Body | 400 | Not defined | MDPI | 1 |
| Body | 580 | Not defined | OSF | 1 |
| Body | 1010 | Not defined | CAPM | 2 |
| Body | 1011 | Not defined | ABC | 2 |
| Body | 1011 | Not defined | MCMC | 2 |
| Body | 1055 | Not defined | JEBS | 1 |
| Body | 1062 | Not defined | ASEAN | 1 |
| Body | 1067 | Not defined | AJEB | 1 |
| Body | 1075 | Not defined | FEJM | 1 |
| Body | 1080 | Not defined | FINR | 1 |
| Body | 1081 | Not defined | FTSE | 1 |
| Body | 1087 | Not defined | ESG | 1 |
| Body | 1087 | Not defined | LSEG | 1 |
| Body | 1087 | Not defined | SFR | 1 |
| Body | 1151 | Not defined | GS | 1 |
| Body | 1209 | Not defined | DC | 3 |
| Body | 1259 | Not defined | MCDA | 1 |
| Body | 1290 | Not defined | IMF | 2 |
| Body | 1375 | Not defined | VNU | 1 |
| Body | 1380 | Not defined | TUY | 1 |

---
# Phụ lục B — Ma trận R&R

# Ma trận R&R — Response to Reviewer Comments (khung chờ tác giả)

Ma trận được dựng theo `templates/revision_response_template.md` (định dạng R→A→C) từ Lộ trình sửa đổi bất biến trong `synthesis.md`. Mỗi mục lộ trình có một dòng, xếp theo thứ tự nguồn (EIC → R1 → R2 → R3 → DA). Thứ tự này không phải thứ tự làm việc. Chưa có phân xử nào của tác giả, nên mọi cột phản hồi của tác giả để ở trạng thái `[chờ tác giả]`. Ma trận không suy đoán hay điền sẵn phản hồi.

## Manuscript Information
- **Title**: Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường: Bằng chứng từ thị trường chứng khoán Việt Nam
- **Manuscript ID**: NOT PROVIDED
- **Original Submission Date**: NOT PROVIDED
- **Revision Submission Date**: [chờ tác giả]
- **Review Round**: Round 1 → bản sửa vòng 1
- **Editorial decision**: Major Revision (F2 kích hoạt; D1 = block, D3 = block, cả hai loại repairable)
- **Criteria binding**: `criteria_binding_unavailable` (không nhận định mức phù hợp với venue)

## Summary of Changes
[chờ tác giả]

---

## 1. Ma trận các mục lộ trình

Cột "Vị trí trong đề cương" là locator gốc lấy từ evidence anchor của người phản biện. Cột "Vị trí sau sửa" do tác giả điền.

| ID | Ref | Nguồn (ghế / W-id) | Obligation | Severity (chuyển nguyên) | Vấn đề | Hành động yêu cầu | Vị trí trong đề cương | Phản hồi tác giả | Trạng thái | Thay đổi đã làm | Vị trí sau sửa |
|---|---|---|---|---|---|---|---|---|---|---|---|
| REV-01 | R1 | EIC W1; R2 W1; DA M8 | must_fix | major | Tuyên bố khoảng trống tuyệt đối mâu thuẫn với Tu (2010) và Avramov (2002), cả hai đều được đề cương trích | Viết lại ở dạng hẹp; phân biệt với Tu (2010), Avramov (2002), Kan và Zhou (2007) | §4.2(1)–(4), §4.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-02 | R2 | EIC W2; R1 W1; DA M4 | must_fix | major | H1 có nguy cơ cao "không kết luận" (khoảng 28 cửa sổ so với ngưỡng 10) | Đếm cửa sổ căng thẳng chỉ bằng HMM; mô phỏng công suất trước đăng ký trước | §4.3.6, §4.3.10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-03 | R3 | EIC W2 | must_fix | major | Chưa nêu đóng góp còn lại khi kết quả không kết luận | Thêm đoạn đóng góp riêng cho kịch bản không kết luận | §4.4, §4.3.10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-04 | S1 | EIC W3; R2 (Nhận xét chi tiết) | should_fix | minor | "Đóng góp lý thuyết" được nói rộng hơn phạm vi kiểm chứng | Gọi đúng tên ("phương pháp đo lường áp dụng") hoặc nêu tính chất mới có thể kiểm chứng | §4.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-05 | R4 | EIC W4; R3 W2 (SPLIT) | must_fix | minor / major (chưa giải quyết) | Tuyên bố liên ngành ở §5 mạnh hơn thiết kế thực có | Viết lại §5 và §4.4 cho đúng tầm; việc thêm cấu phần định tính do tác giả quyết định | §5 đoạn 1, §4.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-06 | R5 | EIC W5; R3 W6 (SPLIT) | must_fix | minor / major | Chưa tách luận án khỏi bản thảo 1, 5, 6 | Tuyên bố phần dùng lại và phần mới; cam kết trích dẫn chéo | Bảng 7; §4.4 hoặc §7.3 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-07 | S2 | EIC W6 | should_fix | minor | Người hướng dẫn ghi không thống nhất | Thống nhất trang bìa với §10 | Trang bìa, §10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-08 | S3 | EIC W7 | should_fix | minor | Trường thông tin để trống | Điền hoặc ghi rõ "Không" | Trang bìa, mục 3 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-09 | S4 | EIC W8 | should_fix | minor | Hình 3 trống; chú thích hình, bảng mất số | Kiểm tra bản nộp gốc; nhúng Hình 3 dưới dạng ảnh; chuyển số tự động thành văn bản tĩnh | Hình 3 (§4.3.9), các chú thích | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-10 | S5 | EIC W9 | should_fix | minor | Tiêu đề rộng hơn phạm vi HOSE | Thêm "(HOSE)" vào phụ đề hoặc nêu lý do giới hạn | Tiêu đề, §4.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-11 | R6 | R1 W1; DA M4 | must_fix | major | "Cửa sổ căng thẳng" chưa được định nghĩa (S_t là biến liên tục) | Ấn định ngưỡng S_t và đăng ký trước | §4.3.10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-12 | R7 | R1 W2 | must_fix | major | Mẫu số chuẩn hóa chưa được định nghĩa | Nêu cặp mô hình, tần suất, độ dài khối, số lần lặp | §4.3.6 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-13 | R8 | R1 W2; DA M9 | must_fix | major | Chuẩn hóa có thể loại tín hiệu và làm mất đơn vị tổn thất | Báo cáo song song regret thô và chuẩn hóa; nêu biến kết quả chính và quy tắc đọc khi hai dạng bất đồng | §4.3.6, §4.1 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-14 | R9 | R1 W3; DA (giải thích thay thế 2) | must_fix | major | Phân phối rỗng không trung tính theo CE | Đặt H0 theo CE; nêu thủ tục tái lấy mẫu; kiểm tra size bằng mô phỏng | §4.3.7 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-15 | R10 | R1 W4; DA M3 | must_fix | major | Đăng ký trước diễn ra sau ước lượng thử trên 2019–2025 | Tách bước thử khỏi mẫu xác nhận, hoặc khai báo các tham số chọn hậu nghiệm | Bảng 5 (Năm 1), §4.3.5, §4.3.6 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-16 | R11 | R1 W5 | must_fix | major | Suy luận trên khoảng 28 quan sát với khoảng 7 tham số | Giới hạn số biến; dùng HAC hiệu chỉnh mẫu nhỏ; ấn định quy tắc độ dài khối | §4.3.7 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-17 | R12 | R1 W6; DA M2 | must_fix | major | β0 − β1 gán phần biến động hấp thụ cho các kênh | Phân rã theo từng khối biến (ví dụ Gelbach); đổi ngôn ngữ diễn giải | Eq. (5), §4.3.7, Câu hỏi 2 (§4.1) | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-18 | R13 | R1 W7; DA M1 (một phần) | must_fix | major | Quy tắc VIF mâu thuẫn với tiêu chí H2 | Nêu tiêu chí H2 cho nhánh VIF cao | §4.3.7 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-19 | R14 | R1 W8; DA M7 | must_fix | major | Cơ chế (ii), (iii) trùng M6, M7 | Giữ M cố định hoặc nêu rõ M thu gọn; định nghĩa chuẩn đối chứng | §4.3.8 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-20 | R15 | R1 W9 | must_fix | major | α và Holm không khớp với tiêu chí ủng hộ ghép | Mỗi giả thuyết một p-value; Holm cho H1–H3; thống nhất α | §4.3.10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-21 | S6 | R1 W10 | should_fix | minor | S_t là biến tạo sinh | Đưa HMM vào vòng bootstrap hoặc báo cáo độ nhạy | §4.3.7 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-22 | S7 | R1 W11 | should_fix | minor | "Trọng số Bayes" chưa được định nghĩa | Nêu cách tính trọng số và đăng ký trước | §4.3.8 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-23 | R16 | R1 W12; DA M6 | must_fix | minor (R1); DA major | Regret gắn với một quy tắc chọn duy nhất (36 tháng) | Thêm quy tắc chọn thay thế hoặc U_o − Ū_t; kiểm tra độ nhạy; hoặc thu hẹp tuyên bố | §4.3.6, §4.3.2, §4.3.10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-24 | S8 | R1 W13 | should_fix | minor | Ngưỡng N/T của M3 gần như không bao giờ có hiệu lực | Nêu độ dài cửa sổ và quy tắc cho dữ liệu tháng | §4.3.5 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-25 | S9 | R1 W14 | should_fix | minor | Thiếu tần suất lợi suất, quy ước năm hóa, mức chi phí cơ sở | Nêu trong tệp đăng ký trước | §4.3.6, §4.3.8 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-26 | S10 | R1 W15; R2 Vấn đề nhỏ 1 | should_fix | minor | Biến kênh cấp cửa sổ chưa được định nghĩa; tên tương quan dùng xen kẽ | Định nghĩa thao tác; dùng một tên thống nhất | §4.3.7, Bảng 2 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-27 | S11 | R1 W16 | should_fix | minor | Nhãn chế độ có thể hoán đổi giữa các lần ước lượng lại | Dùng một tiêu chí gán nhãn; nêu quy tắc qua các lần ước lượng | §4.3.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-28 | S12 | R1 W17; DA Minor (i) | should_fix | minor | Diễn giải kết quả không bác bỏ vượt quá điều kiểm định cho phép | Dùng hiệu ứng nhỏ nhất phát hiện được hoặc TOST | §4.3.10 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-29 | S13 | R1 W18; R2 W4; DA M5 | should_fix | minor (DA major) | Dấu âm của kênh tương quan đuôi ngược chiều cơ chế H1 | Lập luận lại cơ chế và dấu; nêu cách diễn giải khi các kênh bù trừ | §4.3.1, Bảng 2 (H2), Hình 1 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-30 | R17 | R2 W2; R3 W5 (SPLIT → major) | must_fix | major | Regret bị gán cho maxmin và robust control | Tách cơ sở lý thuyết; dẫn nguồn minimax regret (tác giả tự xác minh) | §4.3.1 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-31 | R18 | R2 W3 | must_fix | major | Tập M "bao phủ các hướng chính" chưa đứng vững; ràng buộc chỉ mua là co rút ngầm | Lý giải tính đại diện; thêm mô hình hoặc kiểm tra độ bền; báo cáo khi nới ràng buộc | §4.3.5, §4.4, Bảng 3 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-32 | S14 | R2 W5 | should_fix | minor | Độ phân tán chéo bị gọi là "thước đo bầy đàn" | Dùng hệ số CSAD hoặc bỏ cách diễn giải bầy đàn | §4.4, Bảng 2 (H4) | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-33 | S15 | R2 W6 | should_fix | minor | Mô tả Kerkhof và cộng sự (2010) có thể thiếu thành phần thứ ba | Đối chiếu toàn văn | §4.2(2) | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-34 | S16 | R2 W7 | should_fix | minor | Ledoit–Wolf (2008) được mở rộng sang CE mà không nêu | Ghi rõ đây là mở rộng; mô tả thống kê được studentize | §4.3.7 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-35 | S17 | R2 W8 [FIELD-NORM UNVERIFIED] | consider | minor | Chưa thảo luận vi cấu trúc HOSE (biên độ giá) | Thêm đoạn thảo luận; kiểm tra độ bền trên lợi suất tuần | §4.3.3, §4.3.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-36 | S18 | R2 Vấn đề nhỏ 2 | consider | minor (letter-fallback) | Hiệu chỉnh Forbes–Rigobon được dùng như chuỗi thời gian một thị trường | Nói rõ cách điều chỉnh | §4.3.7 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-37 | S19 | R2 Vấn đề nhỏ 3 | consider | minor (letter-fallback) | Kritzman (2012) được mô tả là "dự báo" chế độ | Dùng từ "nhận diện" | §4.2 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-38 | S20 | R2 Vấn đề nhỏ 4 | consider | minor (letter-fallback) | Câu "Dựa trên phần tóm tắt" cần cập nhật | Cập nhật sau khi đọc toàn văn | §4.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-39 | R19 | R3 W1; DA (tiền đề chưa kiểm tra) | must_fix | major | Tiền đề về người dùng (công ty quản lý quỹ) chưa được xác lập | Thêm cấu phần xác lập tiền đề hoặc định vị lại người dùng | §4.1 đoạn 4, §4.4, §6 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-40 | S21 | R3 W2 (b) | should_fix | major | Quy tắc 36 tháng là giả định hành vi chưa được biện minh | Biện minh như quy tắc chuẩn tắc hoặc dựa trên thực tiễn | §4.3.6, §4.4 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-41 | S22 | R3 W3 | should_fix | minor | Thủ tục giám sát thiếu các yếu tố của khung MRM | Ánh xạ vào khung MRM: ngưỡng, tần suất, chủ thể, thẩm định độc lập, chi phí tín hiệu sai | §4.4 (kế hoạch chương 6.5) | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-42 | S23 | R3 W4; DA M9 | should_fix | minor (DA major) | Regret chuẩn hóa khó đọc với người dùng | Báo cáo regret thô (điểm % năm hóa) cho phần hàm ý quản trị; xem cùng REV-13 | Eq. (4), §4.3.6 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-43 | S24 | R3 W5 (b) | should_fix | minor | Nghĩa hành vi của "regret" chưa được phân biệt | Thêm câu phân biệt với regret theory | §4.1 đoạn 2 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-44 | R20 | R3 W6 (a) | must_fix | major | Khả thi thời gian chưa được đối chiếu với các cam kết song song | Nêu mốc hoàn thành hoặc tạm dừng các chương trình song song | §8.2, §7.4, Bảng 5 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-45 | S25 | R3 W7 | should_fix | minor | Rủi ro giấy phép dữ liệu thương mại | Nêu tên nhà cung cấp và điều khoản, hoặc phiên bản trên dữ liệu công khai | §4.3.3 đoạn 1 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-46 | S26 | R3 W8 | consider | minor | Các bên liên quan chưa được nêu | Nêu cơ quan quản lý cụ thể và góc nhìn người nắm chứng chỉ quỹ | §4.4 (kế hoạch chương 6.6) | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-47 | S27 | R3 Detailed Comments (Tác động xã hội) | consider | minor (letter-fallback) | Rủi ro hành vi đồng loạt khi nhiều tổ chức cùng kích hoạt quy tắc | Bàn ngắn trong kế hoạch chương 6.6 | Kế hoạch chương 6.6 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-48 | R21 | DA M1 | must_fix | major | Phép kiểm định H1 kiểm soát chính biến động định nghĩa chế độ | Nêu β nào kiểm định H1; lập luận về việc kiểm soát biến động thực hiện | §4.3.4, §4.3.7, Bảng 2 (H1) | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |
| REV-49 | S28 | DA Minor (ii) | should_fix | minor | Vai trò của độ phân tán và MCS không thống nhất | Thống nhất vai trò ở §4.1, §4.4 và Bảng 2 | §4.1, §4.4, Bảng 2 | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |

Tổng: 49 dòng (must_fix 21, should_fix 22, consider 6). Giá trị "Trạng thái" do tác giả chọn: `will_address`, `wont_address` hoặc `not_on_point`. Với `wont_address`, tác giả bắt buộc nêu lý do.

---

## 2. Câu hỏi của người phản biện

| ID | Nguồn | Câu hỏi (tóm lược) | Phản hồi tác giả | Vị trí thay đổi (nếu có) |
|---|---|---|---|---|
| R1-Q1 | R1 | Cửa sổ 6 tháng được tính là căng thẳng khi S_t đạt mức nào? Có thể đếm số cửa sổ chỉ bằng HMM trước đăng ký trước không? | [chờ tác giả] | [chờ tác giả] |
| R1-Q2 | R1 | Phân phối rỗng: khối lấy trong từng chế độ hay toàn chuỗi; S_t có được tính lại không; chênh lệch phương sai được xử lý thế nào? | [chờ tác giả] | [chờ tác giả] |
| R1-Q3 | R1 | Mẫu số của regret chuẩn hóa dùng cặp mô hình nào và tần suất nào? | [chờ tác giả] | [chờ tác giả] |
| R1-Q4 | R1 | Tham số nào sẽ được chọn sau bước ước lượng thử quý 2 năm 1, và được khai báo thế nào? | [chờ tác giả] | [chờ tác giả] |
| R2-Q1 | R2 | Ngoài yếu tố "theo chế độ", regret trên M khác gì tổn thất CE trong Tu (2010) và Avramov (2002)? | [chờ tác giả] | [chờ tác giả] |
| R2-Q2 | R2 | Tập M đại diện cho thực tiễn quỹ Việt Nam hay cho các hướng học thuật? | [chờ tác giả] | [chờ tác giả] |
| R2-Q3 | R2 | Với danh mục chỉ mua, khác biệt giữa M2, M3 và M6 còn lại bao nhiêu? Có kế hoạch nới ràng buộc không? | [chờ tác giả] | [chờ tác giả] |
| R2-Q4 | R2 | Có văn bản gốc hoặc số hiệu chính thức của SR 26-2 và Thông tư 83/2025/TT-NHNN không? | [chờ tác giả] | [chờ tác giả] |
| R3-Q1 | R3 | Có bằng chứng sơ bộ nào rằng công ty quản lý quỹ Việt Nam phân bổ danh mục bằng mô hình như M1–M7 không? | [chờ tác giả] | [chờ tác giả] |
| R3-Q2 | R3 | Quy tắc 36 tháng mô tả cách tổ chức thực sự chọn mô hình, hay là một quy tắc chuẩn tắc? | [chờ tác giả] | [chờ tác giả] |
| R3-Q3 | R3 | Ai sở hữu quyết định "kích hoạt kết hợp mô hình", và ai thẩm định độc lập quyết định đó? | [chờ tác giả] | [chờ tác giả] |
| R3-Q4 | R3 | Các chương trình học song song kết thúc hoặc tạm dừng khi nào so với mốc năm 1? | [chờ tác giả] | [chờ tác giả] |

---

## 3. Change Log
| Vị trí (bản gốc) | Vị trí (bản sửa) | Mục | Mô tả thay đổi |
|---|---|---|---|
| [chờ tác giả] | [chờ tác giả] | [chờ tác giả] | [chờ tác giả] |

### Word Count Change
- **Original**: 13461 từ (theo metadata)
- **Revised**: [chờ tác giả]

## Closing Statement
[chờ tác giả]
