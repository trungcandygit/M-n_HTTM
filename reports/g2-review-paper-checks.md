Xác nhận: luồng chính gọi được công cụ Skill (review-paper-checks), phản hồi "Launching skill: review-paper-checks". Theo V7, skill chạy ở LUỒNG CHÍNH vì nó cần công cụ Agent để khởi chạy 3 agent con, mà subagent không có công cụ này (phiên trước đã xác nhận).

Số file skill đã đọc: 1/1 (.claude/skills/review-paper-checks/SKILL.md; thư mục skill chỉ có file này cùng SKILL.md.bak của bản gốc).
Đầu vào: bản LaTeX tạm (pandoc từ ho-so/de-cuong-goc.docx), chỉ lưu cục bộ trong scratchpad. Báo cáo của skill sau lần chạy lại Phase 3: scratchpad/paper/reviews/PAPER_CHECK_2026-10-14.md. Phần từ "# Paper Check" trở xuống trong file này là nguyên văn của báo cáo đó. Bản ngày 2026-10-13 vẫn được giữ trong reviews/ để đối chiếu, nhưng đã bị thay thế.

## Bằng chứng tuân thủ (theo thứ tự SKILL.md)

| # | Bước | Làm? | Bằng chứng / trích đề cương |
|---|---|---|---|
| 1 | Phase 1.0 — nhận đường dẫn file chính từ đối số | Làm | Đối số là đường dẫn main.tex, nên bỏ qua auto-detect (bước 1–2 không cần) |
| 2 | Phase 1.3 — dựng include-graph | Làm | grep \input/\include/\subfile: không có; một file duy nhất |
| 3 | Phase 1.4 — đọc các file thành phần; danh sách giao agent đúng bằng include-graph | Làm | Chỉ giao main.tex |
| 4 | Phase 1.5 — tìm file bảng | Làm | Không có file bảng riêng; 9 longtable inline. Đã ghi cảnh báo bắt buộc của skill |
| 5 | Phase 1.6 — tìm bibliography | Làm | Không có .bib; tham khảo gõ tay ở mục 11 ("11. Danh mục tài liệu tham khảo") |
| 6 | Phase 1 — ghi tên đề tài, tác giả, tóm tắt | Làm | "RỦI RO LỰA CHỌN MÔ HÌNH TRONG QUẢN TRỊ DANH MỤC ĐẦU TƯ THEO CHẾ ĐỘ THỊ TRƯỜNG…"; tác giả NGUYỄN VĂN TRUNG; không có tóm tắt |
| 7 | Phase 2 — khởi chạy 3 agent A/B/C trong MỘT tin nhắn, general-purpose | Làm | 3 lời gọi Agent trong cùng một tin nhắn |
| 8 | Scope guard chép nguyên văn vào cả 3 prompt | Làm | Khối "Review ONLY the files listed…" ở đầu mỗi prompt |
| 9 | Precision guard chép nguyên văn vào cả 3 prompt | Làm | Khối "Every issue you report must be anchored…" |
| 10 | Agent A — 7 mục kiểm tra + format | Làm | Ví dụ A-1: "Đại học Kinh tế Quốc Dân" ↔ "Trường Đại học Kinh tế Quốc dân". Mục 3 (US/UK) và quy tắc số < 10 được agent ghi "không áp dụng cho văn xuôi tiếng Việt" |
| 11 | Agent B — 10 mục kiểm tra + format | Làm | Ví dụ B-2: "loại cơ chế (ii) và (iii) khỏi M" ↔ "\|M\| = 7" |
| 12 | Agent C — 7 mục kiểm tra + format | Làm | Ví dụ C causal-1: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình" |
| 13 | Phase 3 — kiểm tra agent lỗi hoặc thiếu đầu ra | Làm (lần chạy lại kiểm lại) | Cả 3 file agent-out/checks-A, B, C đầy đủ, mang ngày 2026-10-13 và không bị sửa; không cần chèn placeholder |
| 14 | Phase 3 — khử trùng lặp | Làm lại | Có 8 nhóm (a)–(h) ghi ở Summary. Sáu nhóm (b)–(f) và (h) gộp thành một dòng, giữ thẻ cao hơn, nên 77 thẻ còn 71 dòng. Hai nhóm (a) và (g) chỉ ghi chéo góc nhìn. Nhóm (h) (chú thích "Bảng ." mất số: A style-12 ↔ B drafting-3) mới được nhận ra ở lần chạy lại |
| 15 | Lưu vào reviews/PAPER_CHECK_[ngày].md, kiểm tra -v2 | Làm lại | Lần đầu lưu PAPER_CHECK_2026-10-13.md. Lần chạy lại mang ngày 2026-10-14; chưa có file nào trùng tên nên không cần hậu tố -v2, và báo cáo được lưu thành PAPER_CHECK_2026-10-14.md |
| 16 | Cấu trúc báo cáo (Summary, Counts, 1-2-3, Fix List) | Làm lại phần Summary, Counts, Fix List | Thứ tự: Unsupported → Consistency → Spelling → Fix List. Phần 1–3 vẫn là đầu ra agent chép nguyên văn, không đổi chữ nào. Fix List mới có 71 dòng, mỗi lỗi một dòng, ghi đủ vị trí, vấn đề, cách sửa và mã nguồn agent kèm thẻ gốc. Xếp theo thẻ: CRITICAL rồi MAJOR rồi MINOR; trong mỗi mức, nhân quả đứng trước, rồi mâu thuẫn số liệu, lời khẳng định, thuật ngữ, cuối cùng là chính tả. Counts 2/33/36 khớp với số dòng của Fix List |
| 17 | Báo người dùng 4 mục (đường dẫn, số đếm, top 5, kiểm tra không chạy được) | Làm lại | Xem mục "Báo cáo cho người dùng" ngay dưới bảng này. Top 5 là Fix List dòng 1–5 |
| 18 | Đề nghị (không tự làm) sửa lỗi máy móc | Làm (chỉ đề nghị) | Không sửa file nào; việc sửa thuộc vòng lặp L1 sau khi qua Bước 4 |

Sai lệch có chủ đích: (i) mỗi prompt có thêm ghi chú bối cảnh của điều phối viên (văn bản tiếng Việt; lỗi chuyển đổi do pandoc), đặt SAU hai khối guard chép nguyên văn; (ii) đầu ra viết bằng tiếng Việt nhưng giữ nguyên tiêu đề và thẻ. Không bỏ bước nào.

Quy đổi mức độ cho tong-hop-van-de: CRITICAL → NGHIÊM TRỌNG; MAJOR → ĐÁNG SỬA; MINOR → CHỈNH NHẸ. Không nâng hạng mục nào. Lần đầu, mục "tác động lên" (C causal-1) bị nâng từ MAJOR lên CRITICAL. Việc này đã được bỏ ở lần chạy lại, vì skill chỉ yêu cầu xếp thứ tự ("rank"), không yêu cầu đổi thẻ, và vì nó làm Counts lệch với Fix List. Mục này giờ đứng đầu nhóm MAJOR (dòng 3).

## Chạy lại lần 1 sau kiểm toán Cổng 3 (2026-10-14)

Căn cứ: audit/cong3-A.md, mục 3 (review-paper-checks), kết luận KHÔNG ĐẠT ở các dòng P3.e, P3.f, P3.g và S2. Lần chạy lại xác nhận đã gọi được công cụ Skill (`review-paper-checks`, có phản hồi "Launching skill: review-paper-checks") và chỉ làm lại Phase 3. Phase 1–2 và ba agent không chạy lại. Đầu vào là agent-out/checks-A.md, checks-B.md, checks-C.md (ngày 2026-10-13, không đổi).

| # | Lỗi kiểm toán | Đã sửa | Kiểm chứng |
|---|---|---|---|
| R1 | P3.e/S2: Fix List gom khoảng 40 mục vào vài dòng (cũ: dòng 23–26), thiếu vị trí và cách sửa | Viết lại Fix List: 71 dòng, mỗi lỗi một dòng, có vị trí, vấn đề, cách sửa và mã nguồn agent kèm thẻ gốc. Chỉ 6 dòng là dòng gộp, ứng với các cặp trùng (b)–(f) và (h) | Đếm: C 19 MAJOR + 11 MINOR, B 9 + 13, A 2 CRITICAL + 7 + 16, tổng 77 thẻ. Trừ 6 thẻ đã gộp còn 71 dòng (`grep -c '^[0-9]*\. \*\*'` cho 71) |
| R2 | P3.f: Counts ghi 2 CRITICAL nhưng Fix List có 3, do một mục bị nâng hạng | Bỏ nâng hạng, giữ thẻ gốc. Counts 2/33/36 bằng đúng số dòng CRITICAL (1–2), MAJOR (3–35), MINOR (36–71). Thẻ thô 2/35/40 ghi riêng, có giải thích phần chênh | Summary, dòng "Counts" |
| R3 | P3.g: top 5 cho người dùng không có trong file | Thêm mục "Báo cáo cho người dùng" ngay dưới đây | Mục bên dưới |

## Báo cáo cho người dùng (Phase 3, sau khi lưu)

1. **Đường dẫn**: scratchpad/paper/reviews/PAPER_CHECK_2026-10-14.md. Bản sao có phần bằng chứng nằm ở reports/g2-review-paper-checks.md.
2. **Số đếm** (sau khử trùng lặp, theo thẻ gốc): 2 CRITICAL, 33 MAJOR, 36 MINOR. Theo nhóm: Unsupported claims 0/19/10; Consistency 0/7/10; Spelling–style 2/7/16. Trước khử trùng lặp là 2/35/40.
3. **Top 5 của Fix List**:
   1. (CRITICAL) Trang bìa ghi "Đại học Kinh tế Quốc Dân" → sửa thành "Trường Đại học Kinh tế Quốc dân" như ở Mục 8.2 và 10 [A-1; B drafting-2].
   2. (CRITICAL) Mục 10 có dấu nháy kép thẳng `"…"` → đổi thành ``` ``…'' ```; cần kiểm tra trên .docx [A-2].
   3. (MAJOR) 4.3.2: ba lần "tác động lên" mang nghĩa nhân quả, trái với cam kết "liên hệ có điều kiện" ở 4.3.7 → viết lại thành ngôn ngữ kiểm định liên hệ cho H1–H4 [C causal-1; B term-2].
   4. (MAJOR) Bảng 2, H2: "thanh khoản cạn làm…", "tương quan cao làm…" → "dự kiến dương/âm, vì … có thể …" [C causal-2].
   5. (MAJOR) Câu hỏi 2 và 4.3.7: "phần chênh lệch … do các biến kênh giải thích bằng hiệu β0 − β1" → "mức thay đổi của hệ số chế độ khi đưa biến kênh vào", và thêm câu nói rõ đây là phân rã thống kê, không phải phân tích trung gian [C causal-3].
4. **Các kiểm tra không chạy được**: không có file bảng .tex riêng (bảng inline nên vẫn đối chiếu được); không có .bib (đối chiếu với danh mục gõ tay ở mục 11); Hình 1–3 không có ảnh, nên số liệu trong hình không kiểm được; chú thích "Bảng ."/"Hình ." mất số do pandoc, cần kiểm tra trên .docx.

Đề nghị (chưa làm): có thể áp ngay các sửa lỗi máy móc rõ ràng, gồm chính tả, dấu nháy, tên trường, en-dash, title case và ký hiệu toán (Fix List dòng 1, 2, 33, 62, 66, 70). Mọi mục ở mức lời khẳng định và thiết kế để tác giả quyết định. Theo quy trình, việc sửa thuộc vòng lặp L1 sau khi qua Bước 4.

---

# Paper Check

**Paper**: Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường: Bằng chứng từ thị trường chứng khoán Việt Nam (đề cương nghiên cứu sinh)
**Authors**: Nguyễn Văn Trung
**Date**: 2026-10-14 (Phase 3 tổng hợp lại; ba agent chạy ngày 2026-10-13, đầu ra giữ nguyên)
**Scope**: Mechanical check — spelling and grammar, internal consistency, unsupported claims. No assessment of contribution or identification.

Ghi chú Phase 1: file chính là bản LaTeX tạm dựng từ ho-so/de-cuong-goc.docx bằng pandoc (một file, không include). Không có file bảng riêng ("No table .tex files were found in standard locations. Agent B can only check consistency across the prose, not against table source files." — các bảng nằm inline trong main.tex nên Agent B vẫn đối chiếu được). Không có .bib; tài liệu tham khảo gõ trực tiếp ở mục 11. Đề cương không có tóm tắt (abstract).

---

## Summary

Agent C (lời khẳng định vượt bằng chứng) gắn 30 thẻ, Agent B (nhất quán nội bộ) 22 thẻ, Agent A (chính tả–văn phong) 25 thẻ, tổng cộng 77 thẻ. Sau khi khử trùng lặp còn 71 lỗi khác nhau, gồm 29 lỗi lời khẳng định, 17 lỗi nhất quán và 25 lỗi chính tả–văn phong. Hai mục CRITICAL (theo thẻ gốc) đều là lỗi trình bày: tên trường viết hoa không nhất quán và một dấu nháy thẳng. Lỗi có hệ quả lớn nhất là ngôn ngữ nhân quả "tác động lên" ở mục 4.3.2 (Fix List dòng 3, thẻ gốc MAJOR). Nó mâu thuẫn với cam kết của chính mục 4.3.7 rằng kết quả chỉ được gọi là "liên hệ có điều kiện".

**Counts**: 2 CRITICAL, 33 MAJOR, 36 MINOR (71 dòng Fix List, sau khử trùng lặp; dùng thẻ gốc của agent, không nâng hạng mục nào).
- Theo nhóm, sau khử trùng lặp (mỗi lỗi tính ở nhóm chứa dòng của nó): Unsupported claims 0/19/10; Consistency 0/7/10; Spelling–style 2/7/16.
- Thẻ thô trước khử trùng lặp: 2/35/40 (C 0/19/11; B 0/9/13; A 2/7/16). Chênh lệch là 6 thẻ, đến từ 6 lần gộp dòng: (b), (c), (d), (e), (f), (h). Mỗi dòng gộp giữ thẻ cao hơn.

Trùng lặp đã gộp (báo một lần ở agent mô tả chính xác nhất, ghi góc nhìn còn lại):
- (a) Người hướng dẫn ở trang bìa ↔ mục 10: B-1. A cũng ghi lỗi này nhưng xếp vào phần "ngoài phạm vi", không gắn thẻ, nên không bớt thẻ.
- (b) Tên "Đại học Kinh tế Quốc Dân/Quốc dân": A-1 CRITICAL, gộp với B drafting-2 MINOR.
- (c) "Hệ số của tương quan đuôi âm" mơ hồ: A-3 MAJOR, gộp với B term-3 MINOR.
- (d) "Tác động lên" ở 4.3.2: C causal-1 MAJOR, gộp với B term-2 MAJOR.
- (e) Chiều của độ phân tán chéo ở H4: C mech-2 MAJOR, gộp với B-7 MAJOR.
- (f) Biến động là biến kiểm soát hay biến kênh: B-4 MAJOR, gộp với C significance-2 MINOR.
- (g) β0 − β1 không phải phân tích trung gian: C causal-3. Chỉ ghi chéo góc của B-4, không gộp dòng, vì B-4 đã ở (f) và hai lỗi cần cách sửa khác nhau.
- (h) Chú thích "Bảng ."/"Hình ." mất số do pandoc: A style-12 MINOR, gộp với B drafting-3 MINOR. Cặp này được nhận ra ở lần chạy lại.

---

## 1. Unsupported Claims

## Agent C: Unsupported Claims

Phạm vi: tôi chỉ đọc phần chữ đang có hiệu lực của `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/main.tex`, không sửa file nào. Đây là đề cương, chưa có kết quả, nên nhận xét chỉ xét cách đề cương trình bày động cơ nghiên cứu, tổng quan, giả thuyết, đóng góp và hàm ý.

Nhìn chung, đề cương đã tự hạn chế lời lẽ khá tốt. Mục 4.3.7 viết "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả". Có quy tắc "không kết luận" khi dưới 10 cửa sổ căng thẳng, và có lời thừa nhận phạm vi tìm kiếm tài liệu. Các lỗi còn lại chủ yếu là những chỗ phần khung, phần tổng quan và phần hàm ý viết mạnh hơn những ràng buộc đó.

### Causal Overclaiming

1. [MAJOR] main.tex, 4.3.2 (đoạn ngay sau Hình 1) | "Theo Hình 1, chế độ thị trường tác động lên rủi ro lựa chọn mô hình (giả thuyết H1). Các biến kênh tác động lên chính quan hệ đó, tức giải thích một phần chênh lệch giữa hai chế độ (H2 và H4). Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục (H3)."
   - Vì sao vượt mức: chữ "tác động" xuất hiện ba lần, mỗi lần đều mang nghĩa nhân quả. Trong khi đó phương trình (5) là hồi quy chuỗi thời gian của Y_t theo S_t và X_t. Chính mục 4.3.7 lại cam kết chỉ gọi kết quả là "liên hệ có điều kiện". Như vậy khung lý thuyết mâu thuẫn với quy tắc diễn giải của chính đề cương.
   - Thêm một điểm: "tác động lên chính quan hệ đó" là ngôn ngữ của biến điều tiết, còn "giải thích một phần chênh lệch" là ngôn ngữ của biến trung gian. Hai cách nói này không thống nhất với nhau.
   - Sửa: "Theo Hình 1, H1 kiểm định rủi ro lựa chọn mô hình có khác nhau giữa chế độ căng thẳng và chế độ bình thường hay không. H2 và H4 kiểm định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình hay không, và hệ số chế độ thay đổi bao nhiêu khi đưa chúng vào. H3 so sánh kết quả danh mục của các cơ chế giảm thiểu với việc chọn một mô hình." Mũi tên trong Hình 1 cũng nên ghi chú là "liên hệ được kiểm định", không phải "tác động".

2. [MAJOR] main.tex, Bảng 2, dòng H2 | "(thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau)" và "(tương quan cao làm các danh mục chỉ mua hội tụ)"
   - Vì sao vượt mức: chữ "làm" khẳng định quan hệ nhân quả ngay trong lời giả thuyết. Thước đo của H2 chỉ là "Dấu và khoảng tin cậy của hai hệ số", tức một liên hệ có điều kiện.
   - Sửa: "(dự kiến dương, vì khi thanh khoản cạn, chi phí giao dịch có thể khuếch đại chênh lệch giữa các mô hình có vòng quay khác nhau)" và "(dự kiến âm, vì khi tương quan cao, các danh mục chỉ mua có thể hội tụ)".

3. [MAJOR] main.tex, 4.1 (Câu hỏi 2) và 4.3.7 (đoạn về β0 − β1) | "chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?"; "Đề tài ước lượng phần chênh lệch giữa hai chế độ do các biến kênh giải thích bằng hiệu β0 − β1"
   - Vì sao vượt mức: β0 − β1 chỉ là mức thay đổi của hệ số khi thêm biến (một phép phân rã kế toán, giống công thức thiên lệch do bỏ sót biến). Nó không đo phần chênh lệch đi "qua" kênh, nên không phải phân tích trung gian. Kết quả còn phụ thuộc vào đặc tả, và đề cương đã thừa nhận S_t và X_t cùng phụ thuộc biến động. Đọc "do các biến kênh giải thích" theo nghĩa thông thường thì đó là một khẳng định trung gian nhân quả.
   - Sửa: đổi thành "mức thay đổi của hệ số chế độ khi đưa các biến kênh vào", và thêm câu: "Hiệu β0 − β1 là phép phân rã thống kê. Nó không đo phần tác động của chế độ truyền qua các kênh."

4. [MINOR] main.tex, 4.1, đoạn thứ ba | "Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách."
   - Vì sao vượt mức: câu này coi H1 (rủi ro lựa chọn cao hơn khi căng thẳng) là sự thật đã biết. Các bằng chứng dẫn ngay sau đó (Reinhart và Rogoff; Laeven và Valencia) chỉ cho thấy khủng hoảng xảy ra thường xuyên.
   - Sửa: "Khủng hoảng lặp lại thường xuyên, nên câu hỏi liệu thứ hạng mô hình có đổi khi thị trường căng thẳng hay không có ý nghĩa thực tiễn."

5. [MINOR] main.tex, 4.4 (Đóng góp dự kiến) và Bảng 4 (Chương 5) | "cung cấp bằng chứng cho thị trường Việt Nam về mức độ, thời điểm và các kênh của rủi ro lựa chọn mô hình"; "Các biến kênh của rủi ro lựa chọn mô hình"
   - Vì sao vượt mức: "kênh của" ngụ ý các biến này là nguồn gốc nhân quả, nhưng thiết kế chỉ cho ra các liên hệ có điều kiện.
   - Sửa: "... và các biến có liên hệ thống kê với rủi ro lựa chọn mô hình".

### Mechanisms Stated as Facts

1. [MAJOR] main.tex, 4.3.1 | "nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng, tổn thất do chọn sai mô hình cũng tăng theo."
   - Vì sao vượt mức: câu viết như một hệ quả tất yếu, nhưng chính đề cương nêu một cơ chế ngược chiều. Bảng 2 (H2) viết "tương quan cao làm các danh mục chỉ mua hội tụ", nghĩa là khi căng thẳng, các mô hình có thể cho kết quả gần nhau hơn và mức hối tiếc có thể giảm.
   - Sửa: "... tổn thất do chọn sai mô hình có thể tăng. Tuy nhiên, tương quan cao ở chế độ căng thẳng có thể làm các danh mục hội tụ và kéo tổn thất theo chiều ngược lại. Chiều tác động ròng là câu hỏi thực nghiệm mà H1 kiểm định."

2. [MAJOR] main.tex, 4.2 (5) và 4.4 (Phạm vi nội dung) | "Bầy đàn, ... là một kênh hành vi có thể làm các mô hình cho kết quả khác nhau." và "độ phân tán chéo của lợi suất, một thước đo bầy đàn ở cấp thị trường"
   - Vì sao vượt mức: câu thứ nhất không có trích dẫn hay lập luận nào đi kèm. Câu thứ hai coi độ phân tán chéo thô là thước đo bầy đàn. Trong khi đó, H4 (Bảng 2) giả thuyết rằng "độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao". Theo cách đọc của Christie và Huang (1995) mà đề cương trích dẫn, độ phân tán thấp mới là dấu hiệu bầy đàn. Vì vậy H4 thực chất gắn rủi ro cao với mức bầy đàn thấp, ngược với hướng gợi ý trong mục 4.2 (5).
   - Sửa: "H4 kiểm định liên hệ giữa độ phân tán chéo của lợi suất và rủi ro lựa chọn mô hình. Độ phân tán thấp chỉ là một dấu hiệu gián tiếp của bầy đàn. Kết quả của H4 không xác lập hành vi bầy đàn." Nên nêu rõ chiều dự kiến và cách diễn giải nó theo bầy đàn.

3. [MINOR] main.tex, 4.3.6 | "khi lợi suất vượt trội trung bình âm (đúng tình huống của chế độ căng thẳng)"
   - Vì sao vượt mức: mục 4.3.4 chỉ định nghĩa chế độ căng thẳng là chế độ có "lợi suất kỳ vọng thấp hơn chế độ bình thường", không bắt buộc lợi suất phải âm.
   - Sửa: "(thường xảy ra ở chế độ căng thẳng)".

4. [MINOR] main.tex, 4.2 (1) | "Mọi mô hình phân bổ đều mang sai số ở đầu vào."
   - Vì sao vượt mức: quy tắc 1/N (M1) không ước lượng tham số nào.
   - Sửa: "Mọi mô hình phân bổ dựa trên tham số ước lượng đều mang sai số ở đầu vào."

### Generalization Beyond the Sample

1. [MAJOR] main.tex, 4.1 (đoạn đầu) | "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê."
   - Vì sao vượt mức: câu khẳng định chung cho mọi tổ chức. Cũng trong mục 4.1, đề cương nói rằng thí sinh "sẽ xác định ... mức độ họ dùng mô hình định lượng để phân bổ danh mục". Tức là mức độ sử dụng mô hình ở Việt Nam còn chưa được xác lập.
   - Sửa: "Nhiều tổ chức đầu tư dùng mô hình thống kê để hỗ trợ phân bổ vốn; mức độ sử dụng ở các công ty quản lý quỹ Việt Nam sẽ được xác định ở năm thứ nhất."

2. [MAJOR] main.tex, 4.4, "Giới hạn khác" (cùng tên đề tài và mục tiêu tổng quát) | "kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam."
   - Vì sao vượt mức: mẫu thực tế hẹp hơn nhiều. Đó là 30 mã HOSE lớn nhất về giá trị giao dịch và vốn hóa tự do chuyển nhượng, danh mục chỉ mua, tập 7 mô hình cố định, và một quy tắc chọn mô hình theo CER của 36 tháng trước. Mẫu không gồm HNX, UPCoM và các cổ phiếu kém thanh khoản.
   - Sửa: "Kết luận chỉ áp dụng cho danh mục chỉ mua gồm các cổ phiếu thanh khoản cao trên HOSE, với tập bảy mô hình và quy tắc chọn mô hình đã đăng ký trước."

3. [MAJOR] main.tex, 4.4 (Đóng góp dự kiến, ý "Về thực tiễn") | "đề tài đề xuất một thủ tục giám sát mô hình gồm ba bước: ... đo độ phân tán và tập tin cậy mô hình định kỳ, và kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng. Thủ tục này suy ra từ H3"
   - Vì sao vượt mức: H3 chỉ so sánh kết hợp mô hình với chọn một mô hình trong chế độ căng thẳng. H3 không kiểm định quy tắc "kích hoạt" chuyển qua lại theo chế độ. Thêm vào đó, mục 4.1 tự nói độ phân tán và tập tin cậy "chỉ báo hiệu mức bất định, không đo rủi ro", còn mục 4.3.6 coi kích thước tập tin cậy là "thước đo mô tả". Vậy thủ tục đề xuất dùng các chỉ báo mà đề cương không coi là thước đo rủi ro, và quy tắc kích hoạt chưa được kiểm định ngoài mẫu.
   - Sửa: thêm câu "Quy tắc kích hoạt theo chế độ chưa được kiểm định trực tiếp trong H3; luận án sẽ kiểm định ngoài mẫu quy tắc này trước khi đề xuất." Hoặc bổ sung quy tắc này vào các cơ chế được đánh giá.

4. [MINOR] main.tex, 4.1 (đoạn "Tài liệu hiện có để ngỏ hai vấn đề") | "Thị trường Việt Nam có thanh khoản hạn chế và chịu nhiều cú sốc trong một lịch sử giao dịch ngắn, nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển."
   - Vì sao vượt mức: tiền đề "thanh khoản hạn chế" không có trích dẫn. Phép so sánh với thị trường phát triển cũng không được kiểm định, vì mẫu chỉ có Việt Nam. Ngoài ra, câu thiếu chữ "so với" nên nghĩa đen bị đảo thành "lớn hơn ở thị trường phát triển".
   - Sửa: "..., nên chênh lệch giữa các mô hình có thể lớn hơn so với ở thị trường phát triển. Đề tài không kiểm định trực tiếp phép so sánh này." Đồng thời thêm trích dẫn cho đặc điểm thanh khoản.

5. [MINOR] main.tex, Bảng 4 (mục 6.6) và 4.4 | "Hàm ý cho tổ chức đầu tư và cơ quan giám sát"; "tư liệu tham khảo cho tổ chức đầu tư và cơ quan giám sát"
   - Vì sao vượt mức: mục 4.1 viết "Đề tài không đánh giá mức đầy đủ của khung quy định", và khung TT 83/2025 áp dụng cho ngân hàng, không áp dụng cho công ty quản lý quỹ. Hàm ý cho cơ quan giám sát vì vậy không có căn cứ trong thiết kế.
   - Sửa: chỉ nêu hàm ý cho tổ chức đầu tư, hoặc ghi "chỉ ở mức gợi ý, ngoài phạm vi kiểm định".

6. [MINOR] main.tex, mục 6 | "công ty quản lý quỹ cần một thủ tục giám sát mô hình có căn cứ thực nghiệm"
   - Vì sao vượt mức: câu mặc định nhu cầu này đã có, trong khi mức dùng mô hình định lượng của các công ty này chưa được xác định (mục 4.1).
   - Sửa: "công ty quản lý quỹ có dùng mô hình định lượng và có thể cần một thủ tục giám sát mô hình".

### Missing Caveats

1. [MAJOR] Mức hối tiếc phụ thuộc vào tập M và vào quy tắc chọn.
   - Chỗ cần bổ sung: mục 4.3.6, sau phương trình (4), và phần Đóng góp dự kiến. Bằng chứng trong văn bản: "U_{o,t} là giá trị cao nhất trong M" và "nhà đầu tư chọn trước mô hình c có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước".
   - R_t đo tổn thất của một quy tắc chọn cụ thể so với giá trị cao nhất của một tập 7 mô hình cụ thể. Thêm hoặc bớt mô hình sẽ làm R_t thay đổi một cách cơ học. Mục tiêu "đo lường ... rủi ro lựa chọn mô hình trong quản trị danh mục" vì vậy rộng hơn những gì thước đo này đo được.
   - Câu đề xuất: "Mức hối tiếc được định nghĩa tương đối với tập M và với quy tắc chọn theo CER của 36 tháng trước. Kết luận về rủi ro lựa chọn mô hình chỉ có hiệu lực trong phạm vi tập và quy tắc này. Luận án báo cáo độ nhạy theo thành phần tập M và theo độ dài cửa sổ chọn."

2. [MAJOR] Các cửa sổ "độc lập" thực ra không độc lập.
   - Chỗ cần bổ sung: mục 4.3.6 ("khoảng 28 cửa sổ đánh giá độc lập") và mục 4.3.10 ("số cửa sổ độc lập").
   - Cửa sổ 6 tháng không chồng lấn không có nghĩa là độc lập. Chế độ thị trường và biến động có tính bền, và quy tắc chọn dùng 36 tháng trước, tức chồng lấn qua khoảng 6 cửa sổ liên tiếp. Do đó R_t tự tương quan và số quan sát hiệu dụng nhỏ hơn 28. Ngưỡng "dưới 10" cửa sổ căng thẳng đang được tính trên một con số đếm bị thổi phồng.
   - Câu đề xuất: "Các cửa sổ đánh giá không chồng lấn nhưng không độc lập, do chế độ có tính bền và cửa sổ chọn 36 tháng chồng lấn nhau. Luận án báo cáo số quan sát hiệu dụng, và áp dụng quy tắc không kết luận theo số giai đoạn căng thẳng độc lập."

3. [MAJOR] Chuẩn hóa mức hối tiếc không loại được thiên lệch cơ học.
   - Chỗ cần bổ sung: mục 4.3.6 ("Để loại tác động cơ học này, phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap") và mục 4.3.7 ("Để tách rủi ro lựa chọn mô hình khỏi nhiễu ước lượng và biến động").
   - Chia cho sai số chuẩn giúp chuẩn hóa thang đo, nhưng kỳ vọng của giá trị lớn nhất của các nhiễu đã chuẩn hóa vẫn dương. Phân phối rỗng chỉ dùng để hiệu chuẩn kiểm định, không "tách" được hai thành phần.
   - Câu đề xuất: "Phép chuẩn hóa làm giảm, nhưng không loại hết, phần tăng cơ học của R_t khi nhiễu tăng; phân phối rỗng dùng để hiệu chuẩn kiểm định β theo phần tăng cơ học đó."

4. [MAJOR] Kết luận từ việc không bác bỏ được H0 khi công suất thấp.
   - Chỗ cần bổ sung: mục 4.3.10 | "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam."
   - Câu này mâu thuẫn với câu mở đầu của chính đoạn đó: "các kiểm định có công suất thấp". Nó cũng mâu thuẫn với quy tắc gọi kết quả là "không kết luận". Không bác bỏ được giả thuyết không chứng minh được "không đổi theo chế độ". Còn việc "1/N đủ dùng" thì không có kiểm định nào trong thiết kế trả lời trực tiếp.
   - Câu đề xuất: "Nếu dữ liệu không ủng hộ giả thuyết, đề tài báo cáo kích thước hiệu ứng và khoảng tin cậy để cho thấy mức chênh lệch nào có thể loại trừ được. Đề tài không diễn giải việc không bác bỏ là bằng chứng cho thấy rủi ro không đổi hay 1/N là đủ."

5. [MINOR] Mức "loại" thiên lệch nhìn trước bị nói quá.
   - Chỗ cần bổ sung: mục 4.3.4 | "cách làm này loại thiên lệch nhìn trước".
   - Xác suất lọc trên cửa sổ mở rộng loại được thiên lệch nhìn trước trong ước lượng tham số. Tuy nhiên, độ dài cửa sổ "sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất" trên dữ liệu 2019–2025, là giai đoạn thí sinh đã dùng và đã thấy kết quả (mục 4.3.5).
   - Câu đề xuất: "Cách làm này loại thiên lệch nhìn trước trong ước lượng tham số chế độ. Các lựa chọn thiết kế được xác định sau khi ước lượng thử trên 2019–2025 vẫn có thể mang thiên lệch này và được khai trong tệp đăng ký trước."

### Unverified Priority Assertions

Ghi chú: câu khẳng định ở cuối mục 4.2 ("Theo hiểu biết của thí sinh, chưa có nghiên cứu nào ... trên thị trường chứng khoán Việt Nam") đã được giới hạn đúng cách, có nêu cơ sở dữ liệu và ngày tìm kiếm. Các câu dưới đây thì không có giới hạn tương tự. Phần lớn có phạm vi toàn cầu, rộng hơn câu đã được giới hạn, trong khi đề cương thừa nhận "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn".

1. [MAJOR] main.tex, 4.2 (2) | "Các nghiên cứu đã đo rủi ro mô hình cho dự báo và định giá, nhưng chưa đo cho quyết định phân bổ."
   - Cần xác minh: câu này nằm cạnh các nguồn do chính đề cương trích về bất định mô hình trong chọn danh mục, gồm Garlappi và cộng sự (2007), tên bài "Portfolio selection with parameter and model uncertainty", và Pflug và cộng sự (2012) về 1/N "under high model ambiguity". Tác giả phải đối chiếu và thu hẹp câu này, ví dụ "chưa đo dưới dạng tổn thất của việc chọn mô hình".

2. [MAJOR] main.tex, 4.2 (2), câu cuối | "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục."
   - Cần xác minh: khẳng định "chưa thước đo nào" có phạm vi toàn cầu, nên phải kiểm tra với tài liệu về chọn mô hình và mức hối tiếc trong phân bổ danh mục, rồi thêm "theo hiểu biết của thí sinh".

3. [MAJOR] main.tex, 4.2 (3), câu cuối | "Các công cụ này có sẵn, song chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường."
   - Cần xác minh: đây là khẳng định toàn cầu. Phải xác nhận lại sau khi mở rộng tìm kiếm (Scopus, Web of Science), vì đề cương đã thừa nhận chưa tìm trên hai nguồn này.

4. [MAJOR] main.tex, 4.2 (4), câu cuối | "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không."
   - Cần xác minh: câu này đứng ngay sau các nguồn được trích là đã so sánh chiến lược danh mục theo chế độ: Kritzman và cộng sự (2012) ("chiến lược động của họ vượt chiến lược tĩnh") và Tu (2010) (tổn thất CER khi bỏ qua chuyển chế độ). Tác giả phải giải thích các nghiên cứu này khác thế nào với "thứ hạng theo chế độ" của đề tài.

5. [MAJOR] main.tex, 4.2, đoạn sau Bảng 1 | "chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường."
   - Cần xác minh: câu này có phạm vi toàn cầu và không có giới hạn, trong khi câu được giới hạn ngay sau nó chỉ nói về Việt Nam. Nên gộp hai câu, hoặc thêm cùng giới hạn về phạm vi tìm kiếm.

6. [MAJOR] main.tex, 4.1 (đoạn "Tài liệu hiện có để ngỏ hai vấn đề") và 4.2 (1) | "chưa xét thứ hạng thay đổi ra sao khi thị trường chuyển chế độ"; "nhóm tài liệu này chưa trả lời nhà đầu tư nên chọn mô hình nào và chịu tổn thất bao nhiêu khi chọn sai."
   - Cần xác minh: đây là các khẳng định về khoảng trống chung của cả nhóm tài liệu. Tác giả phải xác nhận, hoặc giới hạn câu vào đúng các công trình được trích.

7. [MINOR] main.tex, 4.1 (đoạn khung giám sát) | "Thông tư 83/2025/TT-NHNN ... lần đầu thiết lập khuôn khổ quản lý rủi ro mô hình cho các ngân hàng"
   - Cần xác minh: chữ "lần đầu" là một khẳng định ưu tiên về văn bản pháp quy. Tác giả phải đối chiếu với Thông tư 13/2018/TT-NHNN mà Thông tư 83 thay thế, rồi trích điều khoản cụ thể.

### Significance and Hedging

1. [MAJOR] main.tex, 4.3.7 (tiêu chí H1) và 4.3.8 (tiêu chí H3) | "Đề tài coi H1 được ủng hộ khi thỏa đồng thời ba điều kiện: β của R_t dương và vượt phân vị 95% của phân phối rỗng; khoảng tin cậy bootstrap khối của β loại trừ 0; và β của D_t cùng dấu." và "H3 được ủng hộ khi ... với khoảng tin cậy bootstrap khối loại trừ 0."
   - Vì sao có vấn đề: tiêu chí hoàn toàn là thống kê, không có ngưỡng kinh tế đăng ký trước. Phân tích chính lại dùng R_t đã chia cho sai số chuẩn, tức một con số không đơn vị, nên không đọc được độ lớn kinh tế. Một β "ủng hộ H1" vì thế có thể chỉ tương ứng với vài điểm cơ bản CER mỗi năm. Đề cương đã có sẵn một chuẩn so sánh mà không dùng: Tu (2010), "thường trên 2% mỗi năm".
   - Sửa: thêm "Luận án báo cáo song song mức hối tiếc chưa chuẩn hóa, tính bằng điểm phần trăm CER năm hóa, và đăng ký trước một ngưỡng chênh lệch có ý nghĩa kinh tế, ví dụ so với mức tổn thất do bỏ qua chuyển chế độ trong Tu (2010) và so với chi phí giao dịch khứ hồi. Một kết quả chỉ có ý nghĩa thống kê mà dưới ngưỡng này được mô tả là nhỏ về kinh tế."

2. [MINOR] main.tex, 4.1 (Mục tiêu cụ thể iii) | "xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm biến động, thanh khoản, tương quan cực trị và bầy đàn"
   - Vì sao có vấn đề: ở đây biến động được liệt kê như một biến kênh, nhưng Câu hỏi 2, H2, H4 và phương trình (5) đều coi biến động thực hiện là biến kiểm soát ("Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát").
   - Sửa: bỏ "biến động" khỏi danh sách biến kênh, hoặc nêu rõ vai trò của nó là biến kiểm soát.

3. [MINOR] main.tex, 4.3.5 | "Tập này bao phủ các hướng chính của tài liệu"
   - Vì sao có vấn đề: đây là khẳng định về độ bao phủ mà không có căn cứ. Vì mức hối tiếc phụ thuộc vào M (xem Missing Caveats, mục 1), nên cần lý giải cách chọn tập.
   - Sửa: "Tập này đại diện cho sáu hướng tiếp cận được trích ở mục 4.2; đây không phải danh sách đầy đủ."


---

## 2. Internal Consistency & Cross-References

## Agent B: Internal Consistency & Cross-References

Phạm vi: chỉ đọc `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/main.tex`, không sửa file nào. Tôi đã kiểm tra bằng máy để có các kết quả sau. Tệp không có `\ref`, `\eqref` hay `\cite` nào. Không có `\label` hay `\hypertarget` nào bị trùng. Mọi `\hyperlink` trong mục lục, danh mục bảng và danh mục hình đều trỏ tới một `\hypertarget` có thật.

Một số số liệu đã được đối chiếu và khớp nhau:
- 9 bản thảo trong Bảng 7, trong đó 3 bản thảo đánh "Có" (số 1, 5, 6).
- Chỉ số bản thảo ở mục 8.2 khớp với Bảng 7.
- Bảng 3 có 7 mô hình và |M| = 7.
- Bảng 1 có 4 nhóm, khớp với 4 khoảng trống.
- Bảng 4 có 6 chương.
- Hình 3 mô tả đúng 5 bước.
- Mốc thời gian SR 11-7 và SR 26-2 khớp với danh mục tham khảo.
- Mọi trích dẫn tác giả–năm trong bài đều có mục tương ứng trong mục 11, và mọi mục trong mục 11 đều được trích dẫn.
- Phép tính "khoảng 28 cửa sổ" khớp: 104 tuần + 36 tháng thì mức hối tiếc bắt đầu từ năm thứ 5 (2012), và 2012–2026 cho khoảng 28 cửa sổ 6 tháng.

Các lỗi do chuyển đổi bằng pandoc (chỉ ghi một lần, không tính là lỗi của tác giả): chú thích bị rỗng "Bảng ." / "Hình .", Hình 1–3 không có ảnh, các nhãn `\label{ux...}` tự sinh và số trang trong mục lục. Đây là lỗi chuyển đổi, cần kiểm tra lại trong file .docx.

### Numerical and Factual Contradictions

1. [MAJOR] Trang bìa ("Người hướng dẫn khoa học (dự kiến): … PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân") ↔ Mục 10 ("Người hướng dẫn chính (dự kiến): GS.TS. Nguyễn Đức Khương" và "Người hướng dẫn thứ hai (dự kiến): PGS.TS. Hà Hồng Hạnh"). | Trang bìa chỉ ghi người hướng dẫn thứ hai và bỏ sót người hướng dẫn chính. | Mục 10 có vẻ đúng. Cần bổ sung GS.TS. Nguyễn Đức Khương vào trang bìa.

2. [MAJOR] Mục 4.3.8 ("Khi kiểm định H3, đề tài loại cơ chế (ii) và (iii) khỏi *M*, nên mức hối tiếc của hai cơ chế này có thể âm") ↔ Bảng 3 ("M6 & Danh mục vững chắc với nhiều niềm tin tiên nghiệm & Garlappi và cộng sự (2007)"; "M7 & Giảm tỷ trọng rủi ro theo xác suất chế độ căng thẳng & Kritzman và cộng sự (2012)") và mục 4.3.6 ("|M| = 7").
   - Cơ chế (ii) (Garlappi, 2007) và (iii) (Kritzman, 2012) chính là M6 và M7, vốn thuộc *M*. Câu "loại khỏi *M*" vì vậy mâu thuẫn với định nghĩa |M| = 7 dùng trong các phương trình (2)–(4).
   - Cơ chế (i) (kết hợp mô hình) cũng không thuộc *M*, nhưng bài lại chỉ nói (ii) và (iii) có thể có hối tiếc âm.
   - Kết luận: không xác định được bên nào đúng, tác giả phải làm rõ *M* dùng khi kiểm định H3.

3. [MAJOR] Bảng 2, dòng H3 ("kết hợp mô hình và danh mục vững chắc cho mức hối tiếc và độ sụt giảm tối đa thấp hơn") ↔ Mục 4.3.8 ("mức hối tiếc thấp hơn và độ sụt giảm tối đa không cao hơn so với chọn một mô hình").
   - Quy tắc quyết định cho độ sụt giảm tối đa khác nhau: một chỗ là "thấp hơn", chỗ kia là "không cao hơn".
   - Bảng 2 chỉ nêu hai cơ chế, trong khi 4.3.8 nói "Đề tài đánh giá ba cơ chế", gồm cả "(iii) quy tắc chuyển chế độ".
   - Kết luận: không xác định được bên nào đúng. Cần thống nhất tiêu chí và tập cơ chế của H3.

4. [MAJOR] Câu hỏi 2 ("Sau khi kiểm soát biến động thực hiện, các biến kênh … giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?") ↔ Mục 4.3.7 ("Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát" và "hiệu β0 − β1, trong đó β0 và β1 là hệ số β của phương trình (5) khi không có và khi có X_t").
   - Vì biến động thực hiện nằm trong X_t, hiệu β0 − β1 gộp cả phần do biến động giải thích vào "phần do các biến kênh giải thích". Như vậy phép phân rã không kiểm soát biến động như Câu hỏi 2 đặt ra.
   - Mục tiêu (iii) lại xếp biến động là biến kênh: "các biến kênh … gồm biến động, thanh khoản, tương quan cực trị và bầy đàn".
   - Kết luận: không xác định được, tác giả cần chọn biến động là biến kiểm soát hay là biến kênh.

5. [MAJOR] Mục 4.3.7, điều kiện cho H1 ("H1 được ủng hộ khi … β của R_t dương và vượt phân vị 95% của phân phối rỗng") ↔ cùng mục (phương trình (5) có "γ'X_t", và định nghĩa "β0 … khi không có và β1 … khi có X_t").
   - Bài không nói H1 dùng β0 hay β1.
   - Câu hỏi 1 hỏi rủi ro "thay đổi thế nào giữa chế độ bình thường và chế độ căng thẳng", không có điều kiện theo biến kênh. Trong khi đó phương trình (5) như đang viết cho ra β1.
   - Kết luận: không xác định được, tác giả phải nêu rõ.

6. [MAJOR] Ngưỡng ý nghĩa không thống nhất:
   - Mục 4.3.10: "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết".
   - Mục 4.3.7: H1 dùng "phân vị 95% của phân phối rỗng" và các "khoảng tin cậy bootstrap khối … loại trừ 0", nhưng không nêu mức tin cậy của các khoảng này.
   - Mục 4.3.7 cũng ghi "Đề tài chỉ báo cáo H4 như kết quả thăm dò", vậy mà H4 vẫn nằm trong họ bốn giả thuyết được hiệu chỉnh Holm.
   - Ngưỡng 5% cố định cho H1 không khớp với hiệu chỉnh Holm 10% trên bốn giả thuyết. Tác giả cần kiểm tra lại.

7. [MAJOR] Hướng tác động của bầy đàn ở H4:
   - Mục 4.2(5) viết: "Bầy đàn … là một kênh hành vi có thể làm các mô hình cho kết quả khác nhau", và "Christie và Huang (1995) đo bầy đàn bằng độ phân tán chéo của lợi suất".
   - Bảng 2, H4 viết: "độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao".
   - Bài không nói độ phân tán cao tương ứng với bầy đàn mạnh hay yếu. Nếu theo cách đo của Christie–Huang, độ phân tán cao nghĩa là bầy đàn yếu. Khi đó H4 lại ngụ ý bầy đàn yếu đi cùng rủi ro cao, ngược với lập luận ở 4.2(5).
   - Kết luận: không xác định được, tác giả cần nêu rõ chiều của thước đo.

8. [MINOR] Mục 4.3.2 ("Các biến kênh tác động lên chính quan hệ đó, tức giải thích một phần chênh lệch giữa hai chế độ (H2 và H4)") ↔ Bảng 2, H4 ("độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao").
   - H4 được phát biểu như một liên hệ trực tiếp, không phải như phần giải thích chênh lệch giữa hai chế độ.
   - Phương trình (5) đưa X_t vào dạng cộng ("+ γ'X_t"), không có biến tương tác, nên không mô hình hóa việc biến kênh "tác động lên quan hệ".
   - Cần thống nhất cách mô tả vai trò của biến kênh.

9. [MINOR] Câu hỏi 3 ("Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?") ↔ H3 ("Ở chế độ căng thẳng, sau chi phí giao dịch, …"). | H3 chỉ xét chế độ căng thẳng, còn câu hỏi 3 không giới hạn theo chế độ. | Cần sửa cho khớp phạm vi.

10. [MINOR] Mục 4.3.5 ("Đề tài chọn siêu tham số của M2, M4, M5, M6 và M7 từ một lưới") ↔ cùng mục ("Tệp đăng ký cố định … siêu tham số của bảy mô hình"). | M1 (1/N) và M3 không có siêu tham số. | Nên sửa thành "năm mô hình", hoặc ghi rõ các mô hình có siêu tham số.

11. [MINOR] Mục 7.2 ("(iii) thước đo rủi ro lựa chọn mô hình và thiết kế kiểm định có đăng ký trước") ↔ Bảng 5 (Năm 1, "Quý 4: đăng ký trước kế hoạch phân tích"; Năm 2, sản phẩm "chuyên đề 2 và 3"). | Chuyên đề về thiết kế đăng ký trước lại được nộp sau thời điểm đăng ký trước. | Tác giả cần kiểm tra lại trình tự.

### Broken Cross-References and Citations

1. [MINOR] main.tex, Bảng 6 và mục 11 | "(Nguyễn và Nguyễn, 2026b)" (tên có dấu, nằm trong "Tài liệu tiếng Việt") và "(Nguyen và Nguyen, 2026a)" (tên không dấu, nằm trong "Tài liệu tiếng Anh") | Cùng hai tác giả nhưng viết tên hai kiểu khác nhau, và hậu tố a/b được gán chéo giữa hai danh mục. Khi tra cứu sẽ không rõ đây là cùng một nhóm tác giả. Nên thống nhất cách viết tên và thứ tự a/b.

2. Ngoài lỗi trên, không có tham chiếu chéo nào bị treo, không có nhãn trùng, không có trích dẫn thiếu mục tham khảo và không có mục tham khảo nào không được trích dẫn.

### Terminology and Sample Drift

1. [MAJOR] Cặp "rủi ro" và "bất định".
   - Mục 4.1 cam kết "giữ nguyên nghĩa của chúng trong toàn văn bản" và viết: "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro."
   - Tuy vậy, mục 4.3.7 viết: "đề tài hồi quy các thước đo rủi ro mô hình theo biến chế độ … Với Y_t là D_t hoặc R_t". Ở đây D_t bị gọi là thước đo rủi ro, và thuật ngữ cũng chuyển từ "rủi ro lựa chọn mô hình" sang "rủi ro mô hình", vốn được định nghĩa khác (theo Fed, 2011).
   - Mục 4.3.6 có tên "Thước đo rủi ro lựa chọn mô hình" nhưng lại gọi kích thước tập tin cậy là "Thước đo thứ ba".
   - Mục 4.4 mô tả đóng góp là "đề tài đo mức bất định khi chọn mô hình".
   - Đề nghị: chỉ gọi R_t là thước đo rủi ro lựa chọn mô hình. D_t và kích thước tập tin cậy nên gọi là "chỉ báo bất định", và sửa "thước đo rủi ro mô hình" ở mục 4.3.7.

2. [MAJOR] Ngôn ngữ nhân quả và ngôn ngữ liên hệ.
   - Mục 4.3.2 viết: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình", "Các biến kênh tác động lên chính quan hệ đó", "Cơ chế giảm thiểu tác động lên quan hệ…".
   - Mục 4.3.7 lại viết: "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả". Câu hỏi 2 và Mục tiêu (iii) cũng dùng "liên hệ thống kê".
   - Đề nghị: thay "tác động lên" ở mục 4.3.2 bằng "liên hệ với" hoặc "đi cùng".

3. [MINOR] Tên biến tương quan không thống nhất.
   - Câu hỏi 2, Mục tiêu (iii) và Bảng 4 (mục 5.2) dùng "tương quan cực trị".
   - Bảng 2 và mục 4.3.7 dùng "hệ số của tương quan đuôi âm" và "tương quan đuôi".
   - Định nghĩa X_t ở mục 4.3.7 có hai biến: "tương quan đuôi và tương quan hiệu chỉnh theo biến động". Tiêu chí H2 chỉ nói tới "tương quan đuôi", không nói biến hiệu chỉnh theo biến động được dùng thế nào.
   - Cụm "hệ số của tương quan đuôi âm" ở Bảng 2 có hai cách đọc: hệ số mang dấu âm, hoặc hệ số của biến tương quan ở đuôi âm.
   - Đề nghị: dùng một tên biến duy nhất và viết rõ "hệ số … mang dấu âm".

4. [MINOR] Độ phân tán chéo và bầy đàn.
   - Mục 4.4 viết: "độ phân tán chéo của lợi suất, một thước đo bầy đàn ở cấp thị trường", tức coi hai khái niệm là một.
   - Bảng 2, cột thước đo của H4, viết: "Độ phân tán chéo của lợi suất; thước đo bầy đàn", tức liệt kê như hai thước đo riêng.
   - Đề nghị: nêu rõ có một hay hai biến.

5. [MINOR] Đơn vị "chế độ căng thẳng" của từng cửa sổ.
   - Mục 4.3.7 định nghĩa "S_t là tỷ lệ số ngày trong cửa sổ có xác suất lọc … vượt ngưỡng", tức một biến liên tục.
   - Mục 4.3.10 lại dùng "số cửa sổ độc lập ở chế độ căng thẳng dưới 10" và H3 dùng "Ở chế độ căng thẳng". Hai chỗ này cần một quy tắc phân loại cửa sổ chưa được nêu.
   - Mục 4.3.4 cho phép "Số chế độ (hai hoặc ba)", trong khi H1 và β so sánh với "chế độ bình thường". Bài chưa định nghĩa "chế độ bình thường" khi có ba chế độ.
   - Đề nghị: thêm quy tắc phân loại cửa sổ và định nghĩa nhóm đối chứng.

6. [MINOR] Tên phương pháp bootstrap.
   - Mục 4.3.7 viết: "bootstrap khối dừng (Politis và Romano, 1994) cho các hệ số hồi quy", nhưng tiêu chí H1, H2, H3 lại dùng "khoảng tin cậy bootstrap khối".
   - Cùng đoạn đó còn nêu "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" cho cùng hệ số.
   - Đề nghị: nêu rõ suy diễn cho β dùng phương pháp nào.

7. [MINOR] Có chuẩn hóa hay không.
   - Mục 4.3.6 viết: "phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap".
   - Phương trình (5) và Bảng 2 dùng R_t và D_t chưa chuẩn hóa: "mức hối tiếc (chênh lệch lợi suất tương đương chắc chắn …)".
   - Đề nghị: dùng ký hiệu riêng cho các đại lượng đã chuẩn hóa.

8. Mẫu nghiên cứu ("2007 đến 2026", HOSE, rổ 30 mã) thống nhất giữa các mục 4.3.3, 4.3.6 và 4.4. Không phát hiện sai lệch.

### Drafting Artifacts

1. [MINOR] main.tex, trang bìa và mục 3 | "Cơ quan công tác:" và "3. \textbf{Đơn vị công tác:}" | Hai trường này để trống. Cần điền, hoặc ghi "Không" nếu không có đơn vị công tác.

2. [MINOR] main.tex, trang bìa | "Đại học Kinh tế Quốc Dân" ↔ mục 10 "Trường Đại học Kinh tế Quốc dân" | Tên trường viết hoa và viết đầy đủ không thống nhất. Nên thống nhất thành "Trường Đại học Kinh tế Quốc dân".

3. [MINOR] main.tex, các chú thích bảng và hình cùng mục lục | "Bảng . Các nhóm nghiên cứu…", "Hình . Khung phân tích…", Hình 1–3 không có ảnh, các nhãn `ux...` | Đây là lỗi chuyển đổi, cần kiểm tra lại trong file .docx. Không tính là lỗi của tác giả.

---

## 3. Spelling, Grammar & Style

## Agent A: Chính tả, ngữ pháp và văn phong

Tệp đã rà: `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/main.tex`. Tôi không sửa tệp nào.

Phần chính tả tiếng Việt khá sạch. Tôi không thấy lỗi dấu, và cách bỏ dấu kiểu cũ ("hóa", "khóa", "hủy") được dùng nhất quán. Văn bản không có các từ đệm kiểu "đáng chú ý là", "rõ ràng", "quan trọng là", "rất", "đáng kể", cũng không có câu bị động "bị/được … bởi". Các vấn đề còn lại chủ yếu là câu tối nghĩa và thiếu nhất quán về chủ ngữ, thuật ngữ và cách ghi số.

### Lỗi (phải sửa trước khi nộp)

1. [CRITICAL] main.tex, trang bìa và Mục 10 | Trang bìa ghi "Đại học Kinh tế Quốc Dân", còn Mục 8.2 và Mục 10 ghi "Đại học Kinh tế Quốc dân" / "Trường Đại học Kinh tế Quốc dân" → thống nhất "Trường Đại học Kinh tế Quốc dân" | Tên riêng của cơ sở bị viết hoa không nhất quán.
2. [CRITICAL] main.tex, Mục 10 | `hướng nghiên cứu "chính sách tài khóa, …, quản trị ngân hàng"` → ``` ``chính sách tài khóa, …, quản trị ngân hàng'' ``` | Đây là dấu nháy kép thẳng `"` duy nhất trong tệp. LaTeX sẽ in nó thành hai dấu nháy đóng, trong khi mọi chỗ khác đều dùng ``` `` '' ```.
3. [MAJOR] main.tex, Bảng 2 (H₂) và Mục 4.3.7 | "hệ số của độ phi thanh khoản dương … và hệ số của tương quan đuôi âm" và "hệ số của tương quan đuôi âm và khoảng tin cậy…" → "hệ số của tương quan đuôi mang dấu âm" | "Tương quan đuôi âm" dễ bị hiểu là tương quan ở đuôi âm (lower-tail correlation), chứ không phải hệ số mang dấu âm. Câu đang có hai cách hiểu.
4. [MAJOR] main.tex, Mục 4.1, đoạn 2 | "một trạng thái thống kê có biến động cao và lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng" → "…lợi suất thị trường thấp, được xác định bằng mô hình chuyển chế độ" | Chữ "do" có thể đọc là "vì", tức biến động cao là do mô hình gây ra. Câu cuối đoạn 3 có cùng vấn đề: "chế độ căng thẳng do mô hình ước lượng".
5. [MAJOR] main.tex, Mục 4.2 (3) | "giữ lại những mô hình chưa thể bị loại là kém hơn ở một mức tin cậy cho trước, nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ" → "giữ lại những mô hình chưa bị bác bỏ là kém hơn ở mức tin cậy cho trước; vì vậy dữ liệu ít thông tin cho ra tập lớn, dữ liệu nhiều thông tin cho ra tập nhỏ" | Phải đọc lại mới hiểu, và vế sau thiếu động từ rõ ràng.
6. [MAJOR] main.tex, Mục 7.4, đoạn sau Bảng 5 | "thí sinh áp dụng quy tắc gọi kết quả là không kết luận đã đăng ký" → "thí sinh áp dụng quy tắc đã đăng ký trước để xếp kết quả vào loại chưa đủ cơ sở kết luận" | Cụm "đã đăng ký" đứng cuối nên có thể hiểu nó bổ nghĩa cho "kết quả" thay vì cho "quy tắc".
7. [MAJOR] main.tex, Bảng 7, dòng 4 | "Corporate Brownwashing and Firm Valuation in ASEAN-5 Disclosure Regimes" → "Corporate brownwashing and firm valuation in ASEAN-5 disclosure regimes" | Đây là tên duy nhất viết hoa kiểu title case. Tám tên còn lại trong Bảng 7, Bảng 6 và danh mục tài liệu tham khảo đều viết hoa kiểu câu (sentence case).

### Văn phong và trình bày chữ

1. [MAJOR] main.tex, Mục 4.3.5, đoạn cuối | "trên nền tảng OSF Registries vào quý 4 năm thứ nhất, ở chế độ khóa có dấu thời gian" → "ở dạng khóa có dấu thời gian" | Từ "chế độ" đã được dành riêng cho "chế độ thị trường" (regime) trong toàn đề cương. Dùng nó với nghĩa "mode" ở đây gây nhầm thuật ngữ.
2. [MINOR] main.tex, Mục 4.2 (4) | "Tu (2010) ước tính nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất lợi suất tương đương chắc chắn thường trên 2\% mỗi năm, có thể tới 10\%" → "Tu (2010) ước tính rằng nhà đầu tư bỏ qua chuyển chế độ thường mất trên 2% lợi suất tương đương chắc chắn mỗi năm, có khi tới 10%" | Chuỗi danh từ quá dài.
3. [MINOR] main.tex, Mục 4.3.6, đoạn 1 | "danh mục biến động hơn lại có tỷ số Sharpe ít âm hơn" → "danh mục biến động mạnh hơn…" | "Biến động hơn" thiếu trạng từ.
4. [MINOR] main.tex, Mục 4.3.8 | "Cơ chế (i) kết hợp các mô hình theo trọng số Bayes … Cơ chế (ii) là danh mục vững chắc… Cơ chế (iii) là quy tắc chuyển chế độ" → "Cơ chế (i) là kết hợp các mô hình…" | Ba vế không song song: (ii) và (iii) có "là", (i) thì không.
5. [MINOR] main.tex, Mục 4.3.5, đoạn cuối | "nên không thể khẳng định chưa từng thấy kết quả ở chế độ căng thẳng" → "nên thí sinh không thể khẳng định mình chưa từng thấy kết quả ở chế độ căng thẳng" | Vế sau thiếu chủ ngữ.
6. [MINOR] main.tex, Mục 4.1, đoạn 4 | "Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này, cùng mức độ họ dùng mô hình định lượng để phân bổ danh mục, từ báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ." → "Dựa trên báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ, thí sinh sẽ xác định (a) khung quy định áp dụng cho nhóm tổ chức này và (b) mức độ họ dùng mô hình định lượng để phân bổ danh mục." | Cụm chỉ nguồn bị đẩy xuống cuối câu, tách xa động từ.
7. [MINOR] main.tex, Mục 4.4, "Đóng góp dự kiến" | "Dựa trên phần tóm tắt của các công trình gần nhất, đề tài khác chúng ở bốn điểm." → "So với các công trình gần nhất (theo phần tóm tắt của chúng), đề tài khác ở bốn điểm." | Chủ ngữ "đề tài" không phải là bên "dựa trên" nguồn, nên đây là trạng ngữ treo.
8. [MINOR] main.tex, Mục 4.3.7 | "\textbar{}\emph{M}\textbar{} = 7", trong khi phương trình (2)–(3) viết `|M|` ở chế độ toán. Các chỉ số khác cũng lẫn kiểu: "\emph{t}", "\emph{m}", "\emph{c}" ở dạng chữ nghiêng văn bản, còn \(U_{m,t}\) ở dạng toán → đặt mọi ký hiệu vào `\( \)`, ví dụ `\(|M| = 7\)`, `\(t\)` | Ký hiệu toán trình bày không thống nhất.
9. [MINOR] main.tex, Mục 4.4 | "+ Phạm vi không gian: …", "+ Phạm vi thời gian: …", "+ Phạm vi nội dung: …", "+ Giới hạn khác: …" → dùng `itemize` hoặc viết thành một đoạn văn | Đây là danh sách bằng dấu "+" gõ tay trong thân bài. Nếu mẫu đề cương của trường yêu cầu liệt kê thì nên dùng môi trường danh sách thật.
10. [MINOR] main.tex, Mục 4.3.7 | "hiệu chuẩn \(\beta\) bằng một phân phối rỗng" → "phân phối dưới giả thuyết không (H₀)" | "Phân phối rỗng" là cách dịch sát chữ "null distribution" và ít gặp trong tiếng Việt học thuật. Nếu giữ thì nên chú thích tiếng Anh ở lần dùng đầu.
11. [MINOR] main.tex, Mục 4.2 (1) và Mục 4.3.6 | "nhà đầu tư né tránh mơ hồ" và "nhà đầu tư ngại rủi ro" → thống nhất "ngại mơ hồ" / "ngại rủi ro" | Hai khái niệm song song (ambiguity aversion / risk aversion) nhưng được dịch bằng hai động từ khác nhau.
12. [MINOR] Bảng 1, Bảng 2, Bảng 3, Bảng 5, Hình 1, Hình 2, Hình 3 | "Bảng . Các nhóm nghiên cứu…", "Hình . Khung phân tích…" | Thiếu số thứ tự trong chú thích. Đây gần như chắc chắn là lỗi chuyển đổi của pandoc (trường SEQ của Word bị mất), không phải lỗi tác giả. Tuy vậy cần kiểm tra trên bản PDF hoặc .docx cuối cùng, vì nếu bản nộp sinh ra từ .tex thì người đọc sẽ thấy lỗi này.

### Các lỗi lặp lại cần sửa trong toàn văn bản

1. [MAJOR] Chủ thể hành động không nhất quán (tương đương lỗi "we/the paper" trong tiếng Anh). Cùng một loại hành động được gán cho bốn chủ ngữ khác nhau: "Đề cương dùng ba khái niệm…", "Đề tài ước lượng mô hình chuyển chế độ Markov…", "Thí sinh đăng ký trước kế hoạch phân tích…", "Luận án sẽ ghi kèm nguồn…". "Đề tài" làm chủ ngữ khoảng 60 lần, "thí sinh" khoảng 55 lần. Riêng "Đề tài" thường là chủ ngữ của những động từ mà chỉ người mới làm được (ước lượng, báo cáo, gọi, coi). Một số đoạn lặp liên tục, ví dụ Mục 4.3.7, đoạn cuối: "đề tài báo cáo hệ số phóng đại… đề tài báo cáo hai phương trình… Đề tài chỉ báo cáo H₄… Đề tài gọi các kết quả này…". Cách sửa: chọn một quy ước, ví dụ "thí sinh/nghiên cứu sinh" cho hành động và "đề tài/luận án" cho nội dung. Ở những câu liền nhau, lược hoặc đổi chủ ngữ để không lặp.
2. [MINOR] "Kết quả không kết luận", dịch sát chữ "inconclusive", xuất hiện 4 lần. Ví dụ Mục 4.3.10: "đề tài gọi kết quả là không kết luận". Cách sửa: thay thống nhất bằng "chưa đủ cơ sở kết luận" hoặc "không đi đến kết luận", hoặc định nghĩa thuật ngữ ở lần dùng đầu.
3. [MINOR] Từ "robust" được dịch không nhất quán. Có "danh mục vững chắc" và "lý thuyết kiểm soát vững chắc" (khoảng 7 lần), "sai số chuẩn bền vững" (1 lần), "kiểm tra độ bền" (khoảng 7 lần, nghĩa robustness check). Cách sửa: giữ "kiểm tra độ bền" cho robustness check. Với tính từ "robust", chọn một trong hai từ "vững" hoặc "bền vững" và dùng cho cả danh mục lẫn sai số chuẩn.
4. [MINOR] Dấu chấm phẩy nối hai mệnh đề độc lập, khoảng 10 lần. Ví dụ: "Các thước đo trong nhóm này gắn với dự báo rủi ro và định giá; chưa thước đo nào đo hậu quả…" và "Hành vi thị trường đổi theo chế độ; chưa nghiên cứu nào kiểm định…" (Mục 4.2). Tương tự ở phần Đóng góp dự kiến. Cách sửa: tách thành hai câu, hoặc nối bằng "nhưng" / "song".
5. [MINOR] Gạch nối trong thuật ngữ ghép từ hai danh từ ngang hàng, khoảng 7 lần. Ví dụ "khung trung bình-phương sai", "Trung bình-phương sai với ước lượng mẫu". Cách sửa: dùng gạch ngang en-dash ("trung bình–phương sai", `--` trong LaTeX). Khoảng năm như "1970--2017" đã dùng en-dash đúng.
6. [MINOR] Cách ghi số không nhất quán. Cùng loại đại lượng lúc viết bằng chữ, lúc bằng số: "chín bản thảo" (Mục 8.1) và "cả 9 bản thảo" (ghi chú Bảng 7); "bình quân ba tháng" (Mục 4.3.3) và "cửa sổ 6 tháng" (Mục 4.3.6); "đến 3 chữ số" (tiêu đề 4.5) và "(đến ba chữ số)" (Bảng 4). Ký hiệu quý cũng lẫn kiểu: "quý IV/2022" (2 lần) so với "quý 4 năm thứ nhất" và "Quý 1--2" (khoảng 15 lần). Cách sửa: chọn một quy tắc (ví dụ số nhỏ hơn 10 viết bằng chữ, trừ khi đi kèm đơn vị đo) và một kiểu ký hiệu quý, rồi áp dụng cho toàn bài. Quy tắc "viết bằng chữ các số dưới 10" của tiếng Anh không áp dụng nguyên văn cho văn xuôi tiếng Việt; ở đây chỉ yêu cầu nhất quán.

**Các kiểm tra không áp dụng hoặc không phát hiện lỗi:**
- Quy ước chính tả Mỹ/Anh: không áp dụng cho văn xuôi tiếng Việt. Các tên tài liệu tiếng Anh giữ cách viết gốc của bài ("behavioral", "Modelling", "naïve"/"naive"), nên không tính là lẫn quy ước.
- Định dạng số thập phân và phần trăm: nhất quán theo chuẩn tiếng Việt ("0,5", "3,41/4", "1.000", "95\%"). Không thiếu dấu `\%` nào.
- Tên tác giả và tên công trình tiếng Anh trong danh mục tham khảo: không thấy lỗi chính tả (Danielsson, López de Prado, Kouontchou, von Mettenheim, Rigobon, v.v.).

**Ngoài phạm vi chính tả, ghi lại để điều phối viên chuyển tiếp:**
- Trang bìa chỉ ghi "PGS.TS. Hà Hồng Hạnh" là người hướng dẫn, trong khi Mục 10 ghi người hướng dẫn chính là "GS.TS. Nguyễn Đức Khương" và PGS.TS. Hà Hồng Hạnh là người hướng dẫn thứ hai. Hai chỗ mâu thuẫn nhau.
---

## Fix List

Quy ước: mỗi dòng ứng với đúng một lỗi, ghi theo dạng **Vị trí** | vấn đề | cách sửa | [mã nguồn agent, thẻ gốc]. Thẻ của mỗi dòng là thẻ gốc của agent; không có mục nào bị nâng hạng. Khi gộp hai thẻ trùng nhau, dòng đó lấy thẻ cao hơn. Chỉ có 6 dòng là dòng gộp, ứng với các cặp trùng (b)–(f) và (h) đã khai ở Summary. Cặp (a) và (g) chỉ ghi chéo góc nhìn, không gộp thẻ. Trong mỗi mức, thứ tự là: ngôn ngữ nhân quả trước, rồi mâu thuẫn số liệu và dữ kiện, các lời khẳng định khác, thuật ngữ, cuối cùng là chính tả và văn phong.

**CRITICAL** (a reader or referee will notice these):
1. **Trang bìa** ("Đại học Kinh tế Quốc Dân") ↔ **Mục 8.2, Mục 10** ("Trường Đại học Kinh tế Quốc dân") | Tên cơ sở viết hoa và viết đầy đủ không nhất quán | Sửa trang bìa thành "Trường Đại học Kinh tế Quốc dân" | [A-1 CRITICAL; trùng B drafting-2 MINOR]
2. **Mục 10**, hướng nghiên cứu "chính sách tài khóa, …, quản trị ngân hàng" | Đây là dấu nháy kép thẳng `"` duy nhất trong tệp; LaTeX sẽ in nó thành hai dấu nháy đóng | Đổi thành ``` ``…'' ``` như các chỗ khác. Trên .docx gốc cần kiểm tra lại vì có thể chỉ là lỗi chuyển đổi | [A-2 CRITICAL]

**MAJOR** (fix before submission):
3. **4.3.2**, đoạn ngay sau Hình 1: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình… Các biến kênh tác động lên chính quan hệ đó… Cơ chế giảm thiểu tác động lên quan hệ…" | Ba lần "tác động" mang nghĩa nhân quả, trộn ngôn ngữ điều tiết với trung gian, và trái với cam kết "liên hệ có điều kiện, không gọi là quan hệ nhân quả" ở 4.3.7 | Viết lại: "Theo Hình 1, H1 kiểm định rủi ro lựa chọn mô hình có khác nhau giữa chế độ căng thẳng và chế độ bình thường hay không. H2 và H4 kiểm định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình hay không, và hệ số chế độ thay đổi bao nhiêu khi đưa chúng vào. H3 so sánh kết quả danh mục của các cơ chế giảm thiểu với việc chọn một mô hình." Ghi chú mũi tên Hình 1 là "liên hệ được kiểm định" | [C causal-1 MAJOR; trùng B term-2 MAJOR: mâu thuẫn thuật ngữ với 4.3.7, Câu hỏi 2, Mục tiêu (iii)]
4. **Bảng 2, dòng H2**: "(thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau)", "(tương quan cao làm các danh mục chỉ mua hội tụ)" | Chữ "làm" khẳng định nhân quả, trong khi thước đo của H2 chỉ là dấu và khoảng tin cậy của hệ số | Đổi thành "(dự kiến dương, vì khi thanh khoản cạn, chi phí giao dịch có thể khuếch đại chênh lệch giữa các mô hình có vòng quay khác nhau)" và "(dự kiến âm, vì khi tương quan cao, các danh mục chỉ mua có thể hội tụ)" | [C causal-2 MAJOR]
5. **4.1 (Câu hỏi 2)** "chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?" và **4.3.7** "phần chênh lệch giữa hai chế độ do các biến kênh giải thích bằng hiệu β0 − β1" | β0 − β1 là mức thay đổi của hệ số khi thêm biến (phân rã thống kê), không phải phân tích trung gian | Đổi thành "mức thay đổi của hệ số chế độ khi đưa các biến kênh vào". Thêm câu: "Hiệu β0 − β1 là phép phân rã thống kê. Nó không đo phần tác động của chế độ truyền qua các kênh." | [C causal-3 MAJOR; góc của B-4: hiệu này còn gộp cả phần của biến động, xem dòng 8]
6. **4.3.8** "Khi kiểm định H3, đề tài loại cơ chế (ii) và (iii) khỏi *M*" ↔ **Bảng 3** (M6 Garlappi 2007, M7 Kritzman 2012) và **4.3.6** "|M| = 7" | Cơ chế (ii) và (iii) chính là M6 và M7 thuộc *M*. Cơ chế (i) cũng không thuộc *M* nhưng câu không nhắc tới | Nêu rõ tập dùng khi kiểm định H3, ví dụ "*M* \ {M6, M7}", và sửa câu cho khớp với phương trình (2)–(4). Tác giả phải xác định | [B-2 MAJOR]
7. **Bảng 2, dòng H3** ("mức hối tiếc và độ sụt giảm tối đa thấp hơn", hai cơ chế) ↔ **4.3.8** ("độ sụt giảm tối đa không cao hơn", ba cơ chế gồm "(iii) quy tắc chuyển chế độ") | Tiêu chí quyết định và tập cơ chế của H3 khác nhau giữa hai chỗ | Chọn một tiêu chí ("thấp hơn" hoặc "không cao hơn") và một tập cơ chế, rồi sửa cả Bảng 2 lẫn 4.3.8 | [B-3 MAJOR]
8. **Vai trò của biến động thực hiện**: Mục tiêu (iii) ("các biến kênh … gồm biến động, thanh khoản…") ↔ 4.3.7 ("Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát") ↔ Câu hỏi 2 ("Sau khi kiểm soát biến động thực hiện") | Vì biến động nằm trong X_t, hiệu β0 − β1 gộp cả phần của biến động; Mục tiêu (iii) lại xếp biến động là biến kênh | Chọn một vai trò. Nếu là biến kiểm soát: đưa vào cả hai hồi quy cho β0 và β1, và bỏ khỏi danh sách kênh ở Mục tiêu (iii). Nếu là biến kênh: sửa Câu hỏi 2 và 4.3.7. Vì đây là định nghĩa biến trong thiết kế, việc chọn thuộc DANH SÁCH CHỜ DUYỆT | [B-4 MAJOR; trùng C sig-2 MINOR]
9. **4.3.7**, tiêu chí H1 "β của R_t dương và vượt phân vị 95% của phân phối rỗng" ↔ phương trình (5) có "γ'X_t" và định nghĩa β0/β1 | Không nói H1 dùng β0 hay β1; Câu hỏi 1 không điều kiện theo biến kênh, còn phương trình (5) như đang viết cho ra β1 | Ghi rõ "β trong tiêu chí H1 là β0 (hồi quy không có X_t)", hoặc β1, cho khớp với Câu hỏi 1 | [B-5 MAJOR]
10. **Ngưỡng ý nghĩa**: 4.3.10 ("hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết") ↔ 4.3.7 ("phân vị 95%"; các "khoảng tin cậy bootstrap khối … loại trừ 0" không ghi mức; "chỉ báo cáo H4 như kết quả thăm dò") | Ngưỡng 5% cố định cho H1 không khớp Holm 10%; mức của các khoảng tin cậy chưa nêu; H4 thăm dò vẫn nằm trong họ Holm | Ghi mức tin cậy của mọi khoảng tin cậy, nêu ngưỡng H1 sau hiệu chỉnh Holm, và quyết định H4 có thuộc họ hiệu chỉnh hay không | [B-6 MAJOR]
11. **H4**: 4.2 (5) ("Bầy đàn, … là một kênh hành vi có thể làm các mô hình cho kết quả khác nhau"; Christie và Huang (1995) đo bầy đàn bằng độ phân tán chéo) ↔ Bảng 2 H4 ("độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao") ↔ 4.4 ("một thước đo bầy đàn ở cấp thị trường") | Theo cách đo của Christie–Huang, độ phân tán thấp mới là dấu hiệu bầy đàn, nên H4 ngụ ý bầy đàn yếu đi cùng rủi ro cao, ngược với 4.2 (5). Câu cơ chế ở 4.2 (5) không có trích dẫn | Nêu rõ chiều dự kiến của thước đo và cách diễn giải. Thêm: "H4 kiểm định liên hệ giữa độ phân tán chéo của lợi suất và rủi ro lựa chọn mô hình. Độ phân tán thấp chỉ là một dấu hiệu gián tiếp của bầy đàn. Kết quả của H4 không xác lập hành vi bầy đàn." | [C mech-2 MAJOR; trùng B-7 MAJOR: mâu thuẫn chiều giữa 4.2 (5) và Bảng 2]
12. **Trang bìa** ("Người hướng dẫn khoa học (dự kiến): … PGS.TS. Hà Hồng Hạnh") ↔ **Mục 10** ("Người hướng dẫn chính (dự kiến): GS.TS. Nguyễn Đức Khương"; "Người hướng dẫn thứ hai (dự kiến): PGS.TS. Hà Hồng Hạnh") | Trang bìa bỏ sót người hướng dẫn chính | Bổ sung GS.TS. Nguyễn Đức Khương vào trang bìa theo đúng thứ tự ở Mục 10 | [B-1 MAJOR; A ghi cùng lỗi ở phần "ngoài phạm vi", không gắn thẻ]
13. **4.3.7** "hồi quy các thước đo rủi ro mô hình … Với Y_t là D_t hoặc R_t"; **4.3.6** gọi kích thước tập tin cậy là "Thước đo thứ ba"; **4.4** "đo mức bất định" ↔ **4.1** "chỉ báo hiệu mức bất định, không đo rủi ro" | D_t và kích thước tập tin cậy bị gọi là thước đo rủi ro; "rủi ro mô hình" (định nghĩa theo Fed 2011) bị dùng thay "rủi ro lựa chọn mô hình" | Chỉ gọi R_t là thước đo rủi ro lựa chọn mô hình; gọi D_t và kích thước tập tin cậy là "chỉ báo bất định"; sửa "thước đo rủi ro mô hình" ở 4.3.7 | [B term-1 MAJOR]
14. **4.3.1** "nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng, tổn thất do chọn sai mô hình cũng tăng theo." | Viết như hệ quả tất yếu, trong khi Bảng 2 (H2) nêu cơ chế ngược chiều (tương quan cao làm danh mục hội tụ) | "... tổn thất do chọn sai mô hình có thể tăng. Tuy nhiên, tương quan cao ở chế độ căng thẳng có thể làm các danh mục hội tụ và kéo tổn thất theo chiều ngược lại. Chiều tác động ròng là câu hỏi thực nghiệm mà H1 kiểm định." | [C mech-1 MAJOR]
15. **4.1**, đoạn đầu: "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê." | Khẳng định chung cho mọi tổ chức, trong khi cùng mục nói mức độ dùng mô hình ở Việt Nam sẽ còn phải xác định | "Nhiều tổ chức đầu tư dùng mô hình thống kê để hỗ trợ phân bổ vốn; mức độ sử dụng ở các công ty quản lý quỹ Việt Nam sẽ được xác định ở năm thứ nhất." | [C gen-1 MAJOR]
16. **4.4, "Giới hạn khác"**: "kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam." | Mẫu thực tế hẹp hơn nhiều: 30 mã HOSE, danh mục chỉ mua, tập 7 mô hình cố định, một quy tắc chọn | "Kết luận chỉ áp dụng cho danh mục chỉ mua gồm các cổ phiếu thanh khoản cao trên HOSE, với tập bảy mô hình và quy tắc chọn mô hình đã đăng ký trước." | [C gen-2 MAJOR]
17. **4.4, Đóng góp dự kiến, "Về thực tiễn"**: "kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng. Thủ tục này suy ra từ H3" | H3 không kiểm định quy tắc kích hoạt theo chế độ; thủ tục còn dựa vào các chỉ báo mà 4.1 nói "không đo rủi ro" | Thêm: "Quy tắc kích hoạt theo chế độ chưa được kiểm định trực tiếp trong H3; luận án sẽ kiểm định ngoài mẫu quy tắc này trước khi đề xuất." Hoặc đưa quy tắc này vào các cơ chế được đánh giá | [C gen-3 MAJOR]
18. **4.3.6** (sau phương trình (4)) và **4.4, Đóng góp dự kiến** | Thiếu cảnh báo: R_t được định nghĩa tương đối với tập *M* ("U_{o,t} là giá trị cao nhất trong M") và với quy tắc chọn theo CER 36 tháng; thêm hay bớt mô hình làm R_t đổi một cách cơ học | Thêm: "Mức hối tiếc được định nghĩa tương đối với tập M và với quy tắc chọn theo CER của 36 tháng trước. Kết luận về rủi ro lựa chọn mô hình chỉ có hiệu lực trong phạm vi tập và quy tắc này. Luận án báo cáo độ nhạy theo thành phần tập M và theo độ dài cửa sổ chọn." | [C caveat-1 MAJOR]
19. **4.3.6** "khoảng 28 cửa sổ đánh giá độc lập" và **4.3.10** "số cửa sổ độc lập" | Cửa sổ không chồng lấn nhưng không độc lập (chế độ có tính bền; cửa sổ chọn 36 tháng chồng lấn qua khoảng 6 cửa sổ), nên số quan sát hiệu dụng nhỏ hơn 28 | Đổi "độc lập" thành "không chồng lấn" và thêm: "Các cửa sổ đánh giá không chồng lấn nhưng không độc lập, do chế độ có tính bền và cửa sổ chọn 36 tháng chồng lấn nhau. Luận án báo cáo số quan sát hiệu dụng, và áp dụng quy tắc không kết luận theo số giai đoạn căng thẳng độc lập." | [C caveat-2 MAJOR]
20. **4.3.6** "Để loại tác động cơ học này, phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap" và **4.3.7** "Để tách rủi ro lựa chọn mô hình khỏi nhiễu ước lượng và biến động" | Chuẩn hóa không loại hết phần tăng cơ học (kỳ vọng của giá trị lớn nhất của các nhiễu đã chuẩn hóa vẫn dương); phân phối rỗng chỉ hiệu chuẩn kiểm định | Đổi "loại"/"tách" thành "giảm"/"hiệu chuẩn" và thêm: "Phép chuẩn hóa làm giảm, nhưng không loại hết, phần tăng cơ học của R_t khi nhiễu tăng; phân phối rỗng dùng để hiệu chuẩn kiểm định β theo phần tăng cơ học đó." | [C caveat-3 MAJOR]
21. **4.3.10** "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam." | Coi việc không bác bỏ được là bằng chứng, mâu thuẫn với câu "các kiểm định có công suất thấp" và quy tắc "không kết luận" của cùng đoạn; "1/N đủ dùng" không có kiểm định nào trả lời | Thay bằng: "Nếu dữ liệu không ủng hộ giả thuyết, đề tài báo cáo kích thước hiệu ứng và khoảng tin cậy để cho thấy mức chênh lệch nào có thể loại trừ được. Đề tài không diễn giải việc không bác bỏ là bằng chứng cho thấy rủi ro không đổi hay 1/N là đủ." | [C caveat-4 MAJOR]
22. **4.2 (2)** "Các nghiên cứu đã đo rủi ro mô hình cho dự báo và định giá, nhưng chưa đo cho quyết định phân bổ." | Khẳng định ưu tiên chưa kiểm chứng, đứng cạnh chính các nguồn về bất định mô hình trong chọn danh mục (Garlappi và cộng sự 2007; Pflug và cộng sự 2012) | Tác giả đối chiếu với các nguồn này rồi thu hẹp, ví dụ "chưa đo dưới dạng tổn thất của việc chọn mô hình", kèm "theo hiểu biết của thí sinh" | [C priority-1 MAJOR]
23. **4.2 (2)**, câu cuối: "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục." | Khẳng định "chưa thước đo nào" phạm vi toàn cầu, chưa kiểm chứng | Kiểm tra tài liệu về chọn mô hình và mức hối tiếc trong phân bổ danh mục, rồi thêm "theo hiểu biết của thí sinh, trong phạm vi tìm kiếm…" | [C priority-2 MAJOR]
24. **4.2 (3)**, câu cuối: "Các công cụ này có sẵn, song chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường." | Khẳng định toàn cầu, trong khi đề cương thừa nhận chưa tìm trên Scopus và Web of Science | Xác nhận lại sau khi mở rộng tìm kiếm trên hai cơ sở này; trong lúc chờ, thêm giới hạn phạm vi tìm kiếm | [C priority-3 MAJOR]
25. **4.2 (4)**, câu cuối: "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không." | Đứng ngay sau Kritzman và cộng sự (2012) và Tu (2010), là các nguồn đã so sánh chiến lược danh mục theo chế độ | Giải thích các nghiên cứu này khác "thứ hạng theo chế độ" của đề tài ở điểm nào, và thêm giới hạn phạm vi | [C priority-4 MAJOR]
26. **4.2, đoạn sau Bảng 1**: "chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường." | Phạm vi toàn cầu, không giới hạn, trong khi câu đã giới hạn ngay sau nó chỉ nói về Việt Nam | Gộp với câu đã giới hạn (có cơ sở dữ liệu và ngày tìm kiếm), hoặc thêm cùng giới hạn phạm vi | [C priority-5 MAJOR]
27. **4.1** (đoạn "Tài liệu hiện có để ngỏ hai vấn đề") "chưa xét thứ hạng thay đổi ra sao khi thị trường chuyển chế độ" và **4.2 (1)** "nhóm tài liệu này chưa trả lời nhà đầu tư nên chọn mô hình nào và chịu tổn thất bao nhiêu khi chọn sai." | Khẳng định khoảng trống chung của cả nhóm tài liệu, chưa kiểm chứng | Xác nhận, hoặc giới hạn câu vào đúng các công trình được trích | [C priority-6 MAJOR]
28. **4.3.7** (tiêu chí H1) và **4.3.8** (tiêu chí H3) | Tiêu chí chỉ có ngưỡng thống kê; R_t chia cho sai số chuẩn nên không đọc được độ lớn kinh tế; chuẩn so sánh có sẵn (Tu 2010, "thường trên 2% mỗi năm") chưa được dùng | Thêm: "Luận án báo cáo song song mức hối tiếc chưa chuẩn hóa, tính bằng điểm phần trăm CER năm hóa, và đăng ký trước một ngưỡng chênh lệch có ý nghĩa kinh tế… Một kết quả chỉ có ý nghĩa thống kê mà dưới ngưỡng này được mô tả là nhỏ về kinh tế." Vì liên quan thiết kế nên thuộc DANH SÁCH CHỜ DUYỆT | [C sig-1 MAJOR]
29. **Bảng 2 (H2)** và **4.3.7**: "hệ số của tương quan đuôi âm" | Có hai cách đọc (hệ số mang dấu âm, hoặc hệ số của tương quan ở đuôi âm). Tên biến cũng trôi: "tương quan cực trị" ở Câu hỏi 2, Mục tiêu (iii), Bảng 4, còn "tương quan đuôi" ở Bảng 2, 4.3.7; X_t có hai biến tương quan nhưng tiêu chí H2 chỉ nhắc một | Viết "hệ số của tương quan đuôi mang dấu âm"; chọn một tên biến cho toàn văn bản; nói rõ vai trò của biến "tương quan hiệu chỉnh theo biến động" trong H2 | [A-3 MAJOR; trùng B term-3 MINOR]
30. **4.1**, đoạn 2: "lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng"; cuối đoạn 3: "chế độ căng thẳng do mô hình ước lượng" | Chữ "do" đọc được là "vì", tức mô hình gây ra trạng thái | "…lợi suất thị trường thấp, được xác định bằng mô hình chuyển chế độ" (sửa tương tự ở đoạn 3) | [A-4 MAJOR]
31. **4.2 (3)**: "giữ lại những mô hình chưa thể bị loại là kém hơn ở một mức tin cậy cho trước, nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ" | Câu phải đọc lại; vế sau thiếu động từ rõ ràng | "giữ lại những mô hình chưa bị bác bỏ là kém hơn ở mức tin cậy cho trước; vì vậy dữ liệu ít thông tin cho ra tập lớn, dữ liệu nhiều thông tin cho ra tập nhỏ" | [A-5 MAJOR]
32. **7.4**, đoạn sau Bảng 5: "thí sinh áp dụng quy tắc gọi kết quả là không kết luận đã đăng ký" | "đã đăng ký" đứng cuối nên có thể hiểu là bổ nghĩa cho "kết quả" | "thí sinh áp dụng quy tắc đã đăng ký trước để xếp kết quả vào loại chưa đủ cơ sở kết luận" | [A-6 MAJOR]
33. **Bảng 7, dòng 4**: "Corporate Brownwashing and Firm Valuation in ASEAN-5 Disclosure Regimes" | Tên duy nhất viết hoa kiểu title case, các tên khác viết kiểu câu | "Corporate brownwashing and firm valuation in ASEAN-5 disclosure regimes" | [A-7 MAJOR]
34. **4.3.5**, đoạn cuối: "ở chế độ khóa có dấu thời gian" | "Chế độ" đã dành cho nghĩa regime trong toàn đề cương | "ở dạng khóa có dấu thời gian" | [A style-1 MAJOR]
35. **Toàn văn** (ví dụ 4.3.7, đoạn cuối: "đề tài báo cáo hệ số phóng đại… đề tài báo cáo hai phương trình… Đề tài chỉ báo cáo H₄… Đề tài gọi các kết quả này…") | Chủ thể hành động không nhất quán: "đề tài" (~60 lần), "thí sinh" (~55 lần), "đề cương", "luận án"; "đề tài" làm chủ ngữ cho động từ chỉ người làm được | Quy ước "thí sinh/nghiên cứu sinh" cho hành động, "đề tài/luận án" cho nội dung. Ở các câu liền nhau, lược hoặc đổi chủ ngữ để không lặp | [A recurring-1 MAJOR]

**MINOR** (polish):
36. **4.1**, đoạn thứ ba: "Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách." | Coi H1 như sự thật đã biết; các nguồn dẫn sau chỉ cho thấy khủng hoảng xảy ra thường xuyên | "Khủng hoảng lặp lại thường xuyên, nên câu hỏi liệu thứ hạng mô hình có đổi khi thị trường căng thẳng hay không có ý nghĩa thực tiễn." | [C causal-4 MINOR]
37. **4.4, Đóng góp dự kiến** "các kênh của rủi ro lựa chọn mô hình" và **Bảng 4, Chương 5** "Các biến kênh của rủi ro lựa chọn mô hình" | "Kênh của" ngụ ý nguồn gốc nhân quả | "… và các biến có liên hệ thống kê với rủi ro lựa chọn mô hình" | [C causal-5 MINOR]
38. **4.3.6**: "khi lợi suất vượt trội trung bình âm (đúng tình huống của chế độ căng thẳng)" | 4.3.4 chỉ định nghĩa chế độ căng thẳng là có lợi suất kỳ vọng thấp hơn, không bắt buộc âm | "(thường xảy ra ở chế độ căng thẳng)" | [C mech-3 MINOR]
39. **4.2 (1)**: "Mọi mô hình phân bổ đều mang sai số ở đầu vào." | Quy tắc 1/N (M1) không ước lượng tham số nào | "Mọi mô hình phân bổ dựa trên tham số ước lượng đều mang sai số ở đầu vào." | [C mech-4 MINOR]
40. **4.1** (đoạn "Tài liệu hiện có để ngỏ hai vấn đề"): "…nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển." | Thiếu "so với" nên nghĩa đen bị đảo; tiền đề "thanh khoản hạn chế" không có trích dẫn; phép so sánh không được kiểm định | "…có thể lớn hơn so với ở thị trường phát triển. Đề tài không kiểm định trực tiếp phép so sánh này." Thêm trích dẫn cho đặc điểm thanh khoản | [C gen-4 MINOR]
41. **Bảng 4 (mục 6.6)** "Hàm ý cho tổ chức đầu tư và cơ quan giám sát" và **4.4** "tư liệu tham khảo cho tổ chức đầu tư và cơ quan giám sát" | 4.1 nói đề tài không đánh giá khung quy định, và TT 83/2025 áp dụng cho ngân hàng chứ không cho công ty quản lý quỹ | Chỉ nêu hàm ý cho tổ chức đầu tư, hoặc ghi "chỉ ở mức gợi ý, ngoài phạm vi kiểm định" | [C gen-5 MINOR]
42. **Mục 6**: "công ty quản lý quỹ cần một thủ tục giám sát mô hình có căn cứ thực nghiệm" | Mặc định nhu cầu đã có, trong khi mức dùng mô hình chưa xác định | "công ty quản lý quỹ có dùng mô hình định lượng và có thể cần một thủ tục giám sát mô hình" | [C gen-6 MINOR]
43. **4.3.4**: "cách làm này loại thiên lệch nhìn trước" | Chỉ loại thiên lệch trong ước lượng tham số; các lựa chọn thiết kế được xác định sau khi ước lượng thử trên 2019–2025 (4.3.5) | "Cách làm này loại thiên lệch nhìn trước trong ước lượng tham số chế độ. Các lựa chọn thiết kế được xác định sau khi ước lượng thử trên 2019–2025 vẫn có thể mang thiên lệch này và được khai trong tệp đăng ký trước." | [C caveat-5 MINOR]
44. **4.1** (đoạn khung giám sát): "Thông tư 83/2025/TT-NHNN ... lần đầu thiết lập khuôn khổ quản lý rủi ro mô hình cho các ngân hàng" | "Lần đầu" là khẳng định ưu tiên chưa kiểm chứng | Đối chiếu với Thông tư 13/2018/TT-NHNN mà TT 83 thay thế, rồi trích điều khoản cụ thể; bỏ "lần đầu" nếu không xác nhận được | [C priority-7 MINOR]
45. **4.3.5**: "Tập này bao phủ các hướng chính của tài liệu" | Khẳng định độ bao phủ không có căn cứ, trong khi R_t phụ thuộc vào *M* | "Tập này đại diện cho sáu hướng tiếp cận được trích ở mục 4.2; đây không phải danh sách đầy đủ." | [C sig-3 MINOR]
46. **4.3.2** ("Các biến kênh tác động lên chính quan hệ đó, tức giải thích một phần chênh lệch… (H2 và H4)") ↔ **Bảng 2, H4** và phương trình (5) ("+ γ'X_t", không có tương tác) | H4 là liên hệ trực tiếp; phương trình (5) không mô hình hóa việc biến kênh "tác động lên quan hệ" | Thống nhất cách mô tả vai trò biến kênh (liên hệ cộng thêm, không phải điều tiết); sửa cùng lúc với dòng 3 | [B-8 MINOR]
47. **Câu hỏi 3** ("Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?") ↔ **H3** ("Ở chế độ căng thẳng, sau chi phí giao dịch, …") | Phạm vi chế độ khác nhau | Thêm "ở chế độ căng thẳng" vào Câu hỏi 3, hoặc mở rộng H3 | [B-9 MINOR]
48. **4.3.5**: "siêu tham số của bảy mô hình" ↔ cùng mục "siêu tham số của M2, M4, M5, M6 và M7" | M1 và M3 không có siêu tham số | Sửa thành "năm mô hình" hoặc liệt kê các mô hình có siêu tham số | [B-10 MINOR]
49. **7.2** ("(iii) thước đo rủi ro lựa chọn mô hình và thiết kế kiểm định có đăng ký trước") ↔ **Bảng 5** (Năm 1, "Quý 4: đăng ký trước kế hoạch phân tích"; Năm 2 nộp "chuyên đề 2 và 3") | Chuyên đề về thiết kế đăng ký trước được nộp sau thời điểm đăng ký | Tác giả kiểm tra lại trình tự, dời chuyên đề hoặc ghi rõ chuyên đề hoàn thiện thiết kế đã đăng ký | [B-11 MINOR]
50. **Bảng 6 và mục 11**: "(Nguyễn và Nguyễn, 2026b)" (tiếng Việt) ↔ "(Nguyen và Nguyen, 2026a)" (tiếng Anh) | Cùng nhóm tác giả viết tên hai kiểu; hậu tố a/b gán chéo giữa hai danh mục | Thống nhất cách viết tên và thứ tự a/b | [B ref-1 MINOR]
51. **4.4** ("độ phân tán chéo của lợi suất, một thước đo bầy đàn ở cấp thị trường") ↔ **Bảng 2, H4, cột thước đo** ("Độ phân tán chéo của lợi suất; thước đo bầy đàn") | Không rõ là một biến hay hai | Nêu rõ có một hay hai biến và sửa cả hai chỗ | [B term-4 MINOR]
52. **4.3.7** ("S_t là tỷ lệ số ngày trong cửa sổ có xác suất lọc … vượt ngưỡng") ↔ **4.3.10** ("số cửa sổ độc lập ở chế độ căng thẳng dưới 10"), **H3** ("Ở chế độ căng thẳng"), **4.3.4** ("Số chế độ (hai hoặc ba)") | S_t liên tục nhưng có chỗ đếm cửa sổ "ở chế độ căng thẳng"; chưa định nghĩa "chế độ bình thường" khi có ba chế độ | Thêm quy tắc phân loại cửa sổ và định nghĩa nhóm đối chứng | [B term-5 MINOR]
53. **4.3.7**: "bootstrap khối dừng (Politis và Romano, 1994)" ↔ tiêu chí H1–H3 "khoảng tin cậy bootstrap khối" ↔ "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" | Không rõ suy diễn cho β dùng phương pháp nào | Nêu một phương pháp chính cho β và dùng cùng một tên ở mọi chỗ | [B term-6 MINOR]
54. **4.3.6** ("phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap") ↔ phương trình (5) và Bảng 2 (R_t, D_t chưa chuẩn hóa) | Cùng ký hiệu cho đại lượng đã và chưa chuẩn hóa | Dùng ký hiệu riêng cho đại lượng đã chuẩn hóa (ví dụ R̃_t, D̃_t) | [B term-7 MINOR]
55. **Trang bìa** "Cơ quan công tác:" và **mục 3** "Đơn vị công tác:" | Hai trường để trống | Điền, hoặc ghi "Không" | [B drafting-1 MINOR]
56. **4.2 (4)**: "Tu (2010) ước tính nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất lợi suất tương đương chắc chắn thường trên 2\% mỗi năm, có thể tới 10\%" | Chuỗi danh từ quá dài | "Tu (2010) ước tính rằng nhà đầu tư bỏ qua chuyển chế độ thường mất trên 2% lợi suất tương đương chắc chắn mỗi năm, có khi tới 10%" | [A style-2 MINOR]
57. **4.3.6**, đoạn 1: "danh mục biến động hơn" | Thiếu trạng từ | "danh mục biến động mạnh hơn" | [A style-3 MINOR]
58. **4.3.8**: "Cơ chế (i) kết hợp các mô hình theo trọng số Bayes … Cơ chế (ii) là … Cơ chế (iii) là …" | Ba vế không song song | "Cơ chế (i) là kết hợp các mô hình…" | [A style-4 MINOR]
59. **4.3.5**, đoạn cuối: "nên không thể khẳng định chưa từng thấy kết quả ở chế độ căng thẳng" | Vế sau thiếu chủ ngữ | "nên thí sinh không thể khẳng định mình chưa từng thấy kết quả ở chế độ căng thẳng" | [A style-5 MINOR]
60. **4.1**, đoạn 4: "Thí sinh sẽ xác định khung quy định … từ báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ." | Cụm chỉ nguồn bị đẩy xuống cuối, xa động từ | "Dựa trên báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ, thí sinh sẽ xác định (a) khung quy định áp dụng cho nhóm tổ chức này và (b) mức độ họ dùng mô hình định lượng để phân bổ danh mục." | [A style-6 MINOR]
61. **4.4, Đóng góp dự kiến**: "Dựa trên phần tóm tắt của các công trình gần nhất, đề tài khác chúng ở bốn điểm." | Trạng ngữ treo: "đề tài" không phải bên "dựa trên" | "So với các công trình gần nhất (theo phần tóm tắt của chúng), đề tài khác ở bốn điểm." | [A style-7 MINOR]
62. **4.3.7**: "\textbar{}\emph{M}\textbar{} = 7" và các chỉ số "\emph{t}", "\emph{m}", "\emph{c}" | Ký hiệu toán lúc ở chế độ văn bản nghiêng, lúc ở chế độ toán | Đặt mọi ký hiệu vào `\( \)`, ví dụ `\(|M| = 7\)`, `\(t\)` | [A style-8 MINOR]
63. **4.4**: "+ Phạm vi không gian: …", "+ Phạm vi thời gian: …", "+ Phạm vi nội dung: …", "+ Giới hạn khác: …" | Danh sách gõ tay bằng dấu "+" trong thân bài | Dùng `itemize`, hoặc viết thành một đoạn văn | [A style-9 MINOR]
64. **4.3.7**: "hiệu chuẩn \(\beta\) bằng một phân phối rỗng" | Dịch sát "null distribution", ít gặp trong tiếng Việt học thuật | "phân phối dưới giả thuyết không (H₀)", hoặc giữ nhưng chú thích tiếng Anh ở lần dùng đầu | [A style-10 MINOR]
65. **4.2 (1)** "nhà đầu tư né tránh mơ hồ" ↔ **4.3.6** "nhà đầu tư ngại rủi ro" | Hai khái niệm song song dịch bằng hai động từ khác nhau | Thống nhất "ngại mơ hồ" / "ngại rủi ro" | [A style-11 MINOR]
66. **Chú thích Bảng 1, 2, 3, 5 và Hình 1, 2, 3; mục lục**: "Bảng . Các nhóm nghiên cứu…", "Hình . Khung phân tích…"; Hình 1–3 không có ảnh; nhãn `ux...` | Chú thích mất số thứ tự, gần như chắc chắn do pandoc làm mất trường SEQ của Word | Kiểm tra trên .docx/PDF cuối cùng; nếu bản nộp sinh từ .tex thì thêm số bảng/hình | [A style-12 MINOR; trùng B drafting-3 MINOR]
67. **Toàn văn**, 4 lần "kết quả không kết luận" (ví dụ 4.3.10: "đề tài gọi kết quả là không kết luận") | Dịch sát "inconclusive" | Thay thống nhất bằng "chưa đủ cơ sở kết luận", hoặc định nghĩa ở lần dùng đầu | [A recurring-2 MINOR]
68. **Toàn văn**: "danh mục vững chắc", "lý thuyết kiểm soát vững chắc" (~7 lần) ↔ "sai số chuẩn bền vững" (1 lần) ↔ "kiểm tra độ bền" (~7 lần) | "Robust" dịch không nhất quán | Giữ "kiểm tra độ bền" cho robustness check; với tính từ "robust", chọn "vững" hoặc "bền vững" cho cả danh mục lẫn sai số chuẩn | [A recurring-3 MINOR]
69. **Toàn văn, ~10 lần**, ví dụ 4.2: "Các thước đo trong nhóm này gắn với dự báo rủi ro và định giá; chưa thước đo nào…", "Hành vi thị trường đổi theo chế độ; chưa nghiên cứu nào…", và phần Đóng góp dự kiến | Dấu chấm phẩy nối hai mệnh đề độc lập | Tách thành hai câu, hoặc nối bằng "nhưng"/"song" | [A recurring-4 MINOR]
70. **Toàn văn, ~7 lần**, ví dụ "khung trung bình-phương sai", "Trung bình-phương sai với ước lượng mẫu" | Gạch nối thay cho en-dash giữa hai danh từ ngang hàng | Dùng "trung bình–phương sai" (`--` trong LaTeX) | [A recurring-5 MINOR]
71. **Toàn văn**: "chín bản thảo" (8.1) ↔ "cả 9 bản thảo" (ghi chú Bảng 7); "bình quân ba tháng" (4.3.3) ↔ "cửa sổ 6 tháng" (4.3.6); "đến 3 chữ số" (tiêu đề 4.5) ↔ "(đến ba chữ số)" (Bảng 4); "quý IV/2022" (2 lần) ↔ "quý 4 năm thứ nhất", "Quý 1--2" (~15 lần) | Cách ghi số và ký hiệu quý không nhất quán | Chọn một quy tắc ghi số (ví dụ số nhỏ hơn 10 viết bằng chữ, trừ khi kèm đơn vị đo) và một kiểu ký hiệu quý, áp dụng cho toàn bài | [A recurring-6 MINOR]

Không chạy được hoặc giới hạn: không có file bảng .tex riêng (các bảng nằm inline nên vẫn kiểm được). Không có .bib (đối chiếu với danh mục gõ tay ở mục 11). Hình 1–3 là hình vẽ Word nên không có ảnh; chỉ kiểm được chữ trích ra. Chú thích "Bảng ."/"Hình ." mất số là lỗi chuyển đổi pandoc, cần kiểm tra trên .docx.
