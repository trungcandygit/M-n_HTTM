Xác nhận: luồng chính gọi được công cụ Skill (review-paper), phản hồi "Launching skill: review-paper". Skill chạy ở luồng chính vì cần công cụ Agent (V7).

Số file skill đã đọc: 1/1 (.claude/skills/review-paper/SKILL.md).
Đầu vào: bản LaTeX tạm (pandoc từ ho-so/de-cuong-goc.docx). Lý do dựng bản LaTeX: skill đòi file .tex. Không cần lùi về review-paper-light, vì review-paper đã chạy đủ.
Báo cáo gốc của skill: scratchpad/paper/reviews/PRE_SUBMISSION_REVIEW_2026-10-13.md (bên dưới là nguyên văn).

## Bằng chứng tuân thủ (theo thứ tự SKILL.md)

| # | Bước | Làm? | Bằng chứng / trích đề cương |
|---|---|---|---|
| 1 | Phase 1 — đối số không khớp tên tạp chí nào → TARGET_JOURNAL = top-field, đối số là đường dẫn | Làm | Đối số là đường dẫn main.tex |
| 2 | Bước 1–2 auto-detect | Không cần | Đường dẫn đã có sẵn |
| 3 | Bước 3–4 include-graph và đọc file thành phần | Làm | Không có \input/\include; một file |
| 4 | Bước 5 glob figure files | Làm | Không có (Hình 1–3 là hình vẽ Word). Đã ghi cảnh báo bắt buộc |
| 5 | Bước 6 glob table files | Làm | Không có; bảng nằm inline. Đã ghi cảnh báo bắt buộc |
| 6 | Bước 7 lọc file không được tham chiếu | Làm | Không có file nào bị loại |
| 7 | Ghi tên đề tài, tác giả, tóm tắt | Làm | Không có tóm tắt |
| 8 | Phase 2 — 8 agent trong MỘT tin nhắn | Làm | 8 lời gọi Agent trong cùng một tin nhắn |
| 9 | Scope guard chép nguyên văn vào cả 8 prompt | Làm | Khối "Review ONLY the files listed…" |
| 10 | Dòng "The target journal is top-field." ở đầu prompt Agent 6, 7, 8; giữ nguyên logic điều kiện | Làm | Đúng ba prompt |
| 11 | Agent 1 — 6 mục | Làm | A1-C1: "…có thể lớn hơn ở thị trường phát triển" |
| 12 | Agent 2 — 8 mục | Làm | A2-C2: "chỉ báo hiệu mức bất định, không đo rủi ro" |
| 13 | Agent 3 — 7 mục | Làm | A3: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình" |
| 14 | Agent 4 — 8 mục | Làm | A4: "\(\beta\) đo chênh lệch của \(Y_{t}\) giữa chế độ căng thẳng và chế độ bình thường" |
| 15 | Agent 5 — bảng, hình, tham chiếu chéo | Làm | A5: Bảng 2 "thấp hơn" ↔ 4.3.8 "không cao hơn" |
| 16 | Agent 6 — 5 phần | Làm | "Revise before sending to referees" |
| 17 | Agent 7 — 4 phần | Làm | "Incremental (Gia tăng)" |
| 18 | Agent 8 — 4 phần | Làm | "Insufficient for target journal." |
| 19 | Phase 3 — kiểm tra agent lỗi | Làm | Cả 8 agent trả đủ đầu ra; không cần placeholder |
| 20 | Lưu vào reviews/PRE_SUBMISSION_REVIEW_[ngày].md, kiểm tra -v2 | Làm | Chưa có file cũ |
| 21 | Cấu trúc báo cáo (Overall, Rating, Recommendation, phần 1–7, Priority); Overall Assessment 3–4 câu theo thứ tự (1) Agent 7 Part 1, (2) Contribution Synthesis, (3) mục CRITICAL đứng đầu Priority list | Làm (sửa ở lần chạy lại 1) | Đúng thứ tự. Overall Assessment nay có đúng 3 câu; câu 3 nêu mục CRITICAL #1 của Priority list (khoảng trống đóng góp). Bản trước có 5 câu và câu "nghiêm trọng nhất" lại ứng với Priority #2 |
| 22 | Synthesis chỉ dựa trên Agent 7/8; nêu chỗ đồng ý, điểm tranh chấp, không lấy trung bình hạng; câu caveat chuẩn | Làm | "Novelty relative to literature not cited in the paper has not been verified." |
| 23 | Recommendation chép nguyên văn từ Agent 6 Part 4 | Làm | "Revise before sending to referees" (không cộng ghi chú vì chỉ Agent 8 xếp Insufficient) |
| 24 | Priority: "Collect all tagged items across those agents and rank them"; CRITICAL thêm ở đầu vì hạng là Incremental/Insufficient; thứ tự triage A3 → A6P1 → A6P2 → các CRITICAL còn lại → MAJOR → MINOR | Làm (sửa ở lần chạy lại 1) | Mỗi mục gắn thẻ của Agent 1–6 nay là một dòng riêng, chép nguyên văn vị trí, vấn đề và cách sửa, kèm nhãn nguồn. Khử trùng chỉ với mục trùng nguyên văn: 217 trước, 0 trùng, 217 sau. Cộng mục khoảng trống đóng góp: 218 dòng (CRITICAL 12, MAJOR 67, MINOR 139). Mục 1 là khoảng trống đóng góp; A3/A6P1 không có thẻ CRITICAL; A6P2 là mục 2–6; A1 là 7–9; A2 là 10–12. Bản trước nén 67 MAJOR thành 12 dòng và 139 MINOR thành 5 dòng mà không khai |
| 25 | Báo người dùng 5 mục (đường dẫn; khuyến nghị và hạng đóng góp; top 5 priority; số đếm theo nhóm; file bị loại) | Làm (sửa ở lần chạy lại 1) | Cả 5 mục nay nằm trong mục "Báo cáo cho người dùng" ngay dưới đây, để kiểm chứng được từ file |

Sai lệch có chủ đích: prompt của mỗi agent có thêm ghi chú bối cảnh (đề cương tiếng Việt, chưa có kết quả), đặt sau scope guard; đầu ra bằng tiếng Việt. Giữa Phase 2 và Phase 3, phiên bị gián đoạn vì giới hạn API (cả 8 agent đã xong trước đó); việc hợp nhất làm ngày 2026-10-14.

## Chạy lại lần 1 sau kiểm toán Cổng 3 (2026-10-14)

Căn cứ: audit/cong3-A.md, mục 2 (review-paper), các dòng P3.c, P3.g, P3.h, S2. Chỉ làm lại Phase 3 (hợp nhất). Không chạy lại agent nào. Đầu vào là 8 file đầu ra gốc agent-out/rp-1.md … rp-8.md (không đổi).

- Priority Action Items: dựng lại bằng script đọc rp-1..6. Script lấy mọi dòng bắt đầu bằng thẻ `[CRITICAL]`, `[MAJOR]`, `[MINOR]` (có hoặc không có số thứ tự, có hoặc không có `**`), cùng các dòng thụt lề đi kèm. Đã đối chiếu: không dòng nội dung nào của agent bị bỏ khỏi một mục. Số mục theo agent (C/M/m): A1 3/12/61; A2 3/11/17; A3 0/19/16; A4 0/11/17; A5 0/9/28; A6 5/5/0; tổng 217. Quy tắc khử trùng: chỉ gộp mục trùng nguyên văn; 0 mục trùng, nên còn 217. Cộng mục khoảng trống đóng góp: 218 dòng.
- Overall Assessment: viết lại còn 3 câu; câu 3 là mục CRITICAL #1.
- Báo cáo cho người dùng: thêm vào file, có top 5 (bên dưới).
- Các phần 1–7 (đầu ra agent) và phần Synthesis giữ nguyên văn, không sửa chữ nào. Contribution Rating và Preliminary Recommendation cũng giữ nguyên.
- Sai lệch có chủ đích: (i) bên trong hai tầng MAJOR và MINOR, skill không quy định thứ tự, nên coordinator dùng cùng thứ tự agent như tầng CRITICAL (A3 → A6 → A1 → A2 → A4 → A5). (ii) Bản trong scratchpad/paper/reviews/PRE_SUBMISSION_REVIEW_2026-10-13.md được ghi đè bằng bản đã sửa, không tạo -v2, vì đây là bản sửa của chính lần chạy đó chứ không phải một lần review mới. (iii) Sửa số đếm A1 MAJOR từ 13 thành 12; dòng thứ 13 là câu chú thích của agent, không phải một mục.

## Báo cáo cho người dùng (Phase 3, bước cuối)

1. Đường dẫn báo cáo: scratchpad/paper/reviews/PRE_SUBMISSION_REVIEW_2026-10-13.md (bản sao kèm phần tuân thủ: reports/g2-review-paper.md).
2. Khuyến nghị sơ bộ (Agent 6): Revise before sending to referees. Hạng đóng góp tổng hợp: Incremental (advocate) / Insufficient for target journal (skeptic). Hai bên bất đồng ở chỗ thước đo hối tiếc theo chế độ có phải một đại lượng mới so với Tu (2010) và Danielsson và cộng sự (2016) hay không.
3. Top 5 priority action items:
   1. [CRITICAL] Khoảng trống đóng góp: xây chuẩn mô phỏng hoặc lý thuyết cho mức hối tiếc dưới giả thuyết không, để tách nhiễu khỏi đảo hạng thực, và phân biệt rõ với Tu (2010), Danielsson và cộng sự (2016), DeMiguel và cộng sự (2009).
   2. [CRITICAL] A6 Required #1: phân tích công suất và mô phỏng thiết kế trước khi đăng ký; định nghĩa cách đếm "cửa sổ căng thẳng" khi S_t liên tục.
   3. [CRITICAL] A6 Required #2: phân phối rỗng cân bằng CE và tách thành phần cơ học do phương sai; báo cáo R_t ở cả dạng chưa chuẩn hóa và đã chuẩn hóa.
   4. [CRITICAL] A6 Required #3: thêm mốc chuẩn chọn ngẫu nhiên và kiểm tra độ bền theo quy tắc chọn (Sharpe, MCS, lịch sử 12/24/60 tháng).
   5. [CRITICAL] A6 Required #4: kiểm định giả cho định nghĩa chế độ và cho các biến kênh.
4. Số đếm (sau khử trùng, gồm mục khoảng trống đóng góp): CRITICAL 12, MAJOR 67, MINOR 139; tổng 218. Theo agent (C/M/m): A1 3/12/61; A2 3/11/17; A3 0/19/16; A4 0/11/17; A5 0/9/28; A6 5/5/0.
5. File bảng hoặc hình bị loại vì không được tham chiếu: 0. Không có file nào bị bỏ qua khi review.


---

# Pre-Submission Referee Report

**Paper**: Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường: Bằng chứng từ thị trường chứng khoán Việt Nam (đề cương nghiên cứu sinh)
**Authors**: Nguyễn Văn Trung
**Date**: 2026-10-13 (hợp nhất ngày 2026-10-14, sau khi phiên bị gián đoạn vì giới hạn API)
**Review Standard**: Leading Field Journal

Ghi chú Phase 1: file chính là bản LaTeX tạm (pandoc), không có include-graph. "No figure files were found in standard locations. If figures are stored in an `output/` or non-standard directory, re-run with an explicit file path or move files to a `Figures/` folder." Hình 1–3 là hình vẽ Word; chữ của Hình 1–2 đã được trích ra hinh-van-ban.txt. "No table .tex files were found in standard locations. Tables may be stored in an `output/` or non-standard directory. Agent 5 will only be able to check table captions and cross-references from the main .tex files." Các bảng nằm inline nên vẫn đọc được. Không có file hình hoặc bảng nào bị loại vì không được tham chiếu.

---

## Overall Assessment

Đề cương đề xuất đo "rủi ro lựa chọn mô hình", tức mức hối tiếc theo lợi suất tương đương chắc chắn sau chi phí khi phải chọn trước một trong bảy mô hình danh mục cho rổ 30 cổ phiếu HOSE, rồi kiểm định xem mức này có cao hơn ở chế độ căng thẳng hay không (Agent 7, Part 1). Về đóng góp, advocate xếp Incremental còn skeptic xếp Insufficient for target journal, và cả hai cùng thấy giá trị nằm ở khung đo lường và quy trình hơn là ở một phát hiện thực nghiệm đủ công suất (Synthesis, mục 1). Vấn đề nghiêm trọng nhất, tức mục CRITICAL #1 trong Priority Action Items, là khoảng trống đóng góp: đề cương cần một chuẩn mô phỏng hoặc lý thuyết cho mức hối tiếc dưới giả thuyết không để tách phần do nhiễu khỏi phần do đảo hạng thực, và dùng nó để phân biệt đại lượng của mình với Tu (2010), Danielsson và cộng sự (2016) và DeMiguel và cộng sự (2009) (Agent 8, Part 3).

**Contribution Rating**: Incremental (advocate) / Insufficient for target journal (skeptic). Hai bên khác nhau ở một điểm: phần mới so với Danielsson và cộng sự (2016), Tu (2010) và DeMiguel và cộng sự (2009) là một khung đo mới, hay chỉ là đổi biến kết quả và đổi bối cảnh.

**Preliminary Recommendation**: Revise before sending to referees

---

## 1. Central Contribution

### Advocate's Case

## Agent 7: Contribution Advocate

### Part 1 — Đóng góp được tuyên bố

**Đóng góp theo cách tác giả trình bày (một câu).** Đề cương nói rằng đây là nghiên cứu đầu tiên đo *rủi ro lựa chọn mô hình*, tức "tổn thất kỳ vọng phát sinh khi nhà đầu tư phải chọn một mô hình trước lúc biết mô hình nào tốt nhất", đo bằng "mức hối tiếc (regret)". Thước đo này được áp dụng cho quyết định phân bổ danh mục, tính riêng theo chế độ thị trường, trên thị trường chứng khoán Việt Nam. Nguyên văn: "chưa có nghiên cứu nào đo rủi ro lựa chọn mô hình theo chế độ thị trường cho quyết định phân bổ danh mục trên thị trường chứng khoán Việt Nam".

**Loại đóng góp:**
- **Câu hỏi mới (chính):** đề cương chuyển từ câu hỏi "mô hình nào tốt nhất trung bình" sang câu hỏi "chọn sai mô hình tốn bao nhiêu, và chi phí đó có tăng ở chế độ căng thẳng không". Tác giả nêu khoảng trống như sau: "Các nghiên cứu so sánh danh mục (DeMiguel và cộng sự, 2009; Garlappi và cộng sự, 2007) xếp hạng mô hình theo bình quân toàn mẫu, chưa xét thứ hạng thay đổi ra sao khi thị trường chuyển chế độ."
- **Thước đo/phương pháp mới (phụ):** gồm ba phần.
  - Mức hối tiếc $R_t = U_{o,t} - U_{c,t}$, tính trên lợi suất tương đương chắc chắn sau chi phí.
  - Mức hối tiếc được chuẩn hóa bằng sai số chuẩn bootstrap, nhằm loại "tác động cơ học" của giá trị lớn nhất trên các đại lượng có nhiễu.
  - $\beta$ được hiệu chuẩn bằng một phân phối rỗng: đề cương "loại chênh lệch trung bình giữa các mô hình trong từng chế độ nhưng giữ nguyên tương quan chéo và biến động".
- **Bối cảnh mới:** thị trường cận biên có "thanh khoản hạn chế và chịu nhiều cú sốc trong một lịch sử giao dịch ngắn".
- **Câu trả lời mới cho câu hỏi cũ (một phần):** H3 kiểm định lại câu hỏi "kết hợp mô hình hay chọn một mô hình", nhưng có điều kiện theo chế độ căng thẳng và tính sau chi phí giao dịch.

**Điều biên tập viên bận rộn sẽ nhớ (một dòng):** "Ở Việt Nam, cái giá của việc chọn sai mô hình danh mục có tăng khi thị trường vào chế độ căng thẳng không? Nếu có, kết hợp mô hình có giảm được cái giá đó sau chi phí giao dịch không?"

### Part 2 — Phần vượt trội so với các nghiên cứu gần nhất

Lưu ý: chưa có kết quả nào. Phần "đóng góp thêm" dưới đây chỉ ghi những gì thiết kế đã đăng ký *có thể* tạo ra, không ghi những gì phần đặt vấn đề hứa hẹn.

1. **Danielsson và cộng sự (2016); Boucher và cộng sự (2014)**
   - *Nghiên cứu đó cho thấy gì (theo đề cương):* các nghiên cứu này "đo rủi ro mô hình của các mô hình dự báo rủi ro thị trường và rủi ro hệ thống". Rủi ro mô hình "tăng theo mức bất định và nhỏ khi thị trường yên ắng". Tuy vậy, chúng chỉ "đo chênh lệch giữa các dự báo rủi ro, chưa đo hậu quả của việc chọn sai mô hình lên trọng số và kết quả danh mục".
   - *Đề cương thêm gì:* thiết kế chuyển đơn vị đo từ *độ phân tán dự báo* sang *tổn thất phúc lợi của quyết định*. Đó là mức hối tiếc tính bằng lợi suất tương đương chắc chắn sau chi phí, với quy tắc chọn trước khả thi trong thực tế: chọn mô hình có lợi suất tương đương chắc chắn ngoài mẫu cao nhất "trong 36 tháng liền trước". Đề cương cũng tách rõ "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro".
   - *Ý nghĩa nếu H1 được ủng hộ:* kết quả sẽ chuyển phát hiện "rủi ro mô hình tăng theo bất định" của Danielsson và cộng sự từ dự báo rủi ro sang quyết định phân bổ. Đây là phần mở rộng có ý nghĩa thực chất, không chỉ đổi tên khái niệm.

2. **DeMiguel và cộng sự (2009), cùng Garlappi và cộng sự (2007) và Pflug và cộng sự (2012)**
   - *Nghiên cứu đó cho thấy gì (theo đề cương):* DeMiguel và cộng sự so sánh "14 mô hình trên bảy bộ dữ liệu và không tìm thấy mô hình nào vượt quy tắc chia đều vốn cho N tài sản (quy tắc 1/N) một cách nhất quán". Pflug và cộng sự chứng minh 1/N "xấp xỉ tối ưu theo nghĩa vững chắc khi mức mơ hồ về mô hình đủ cao". Theo đề cương, các nghiên cứu này xếp hạng mô hình "theo bình quân toàn mẫu".
   - *Đề cương thêm gì:* đề cương dùng chính phát hiện "không ai thắng ổn định" làm *biến phụ thuộc* thay vì làm kết luận. Thiết kế đo xem tổn thất do chọn sai có phụ thuộc trạng thái thị trường không, thông qua hệ số $\beta$ trong phương trình (5).
   - Đề cương cũng nêu sẵn giả thuyết đối lập: "một quy tắc đơn giản như 1/N có thể thắng ổn định". Như vậy kết quả âm tính vẫn có thông tin: "quy tắc 1/N đủ dùng ở Việt Nam".
   - Kiểm định trên "tập chỉ gồm các mô hình tĩnh M1, M2, M3, M4 và M6" giúp tránh kết luận ngược vòng, vì M5 và M7 đổi hành vi theo chế độ một cách cơ học.

3. **Goutte và cộng sự (2025); Nguyen và Nguyen (2026a), là bài của chính thí sinh**
   - *Nghiên cứu đó cho thấy gì (theo đề cương):* Goutte và cộng sự "so sánh năm phương pháp ra quyết định đa tiêu chí với bốn cách gán trọng số trên rổ VN100 giai đoạn 01/2015--11/2023". Nguyen và Nguyen (2026a) "áp dụng mô hình Black-Litterman với mô hình định giá tài sản vốn có chuyển chế độ ... giai đoạn 2019--2025 và chỉ đánh giá một mô hình". Đề cương xếp cả hai vào nhóm "Đánh giá từng mô hình hoặc từng phương pháp".
   - *Đề cương thêm gì:* thiết kế đặt bảy mô hình vào "một tập cạnh tranh" với "cùng một quy tắc và cùng ngân sách tinh chỉnh". Rổ cổ phiếu được xác định theo từng thời điểm, "kể cả những mã đã hủy niêm yết". Đề cương còn có đăng ký trước trên OSF và tự công khai rằng thí sinh đã xem kết quả 2019–2025.
   - So với các nghiên cứu Việt Nam trong danh mục tham khảo, đây là bước nâng rõ rệt về tính nghiêm ngặt. Tuy vậy, đối với một tạp chí hàng đầu chuyên ngành, phần vượt trội này chủ yếu thuộc về bối cảnh và quy trình, không phải về ý tưởng.

(Tu (2010) cũng gần về khái niệm: "nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất lợi suất tương đương chắc chắn thường trên 2% mỗi năm". Đề cương khác ở chỗ đo tổn thất do *chọn giữa nhiều mô hình*, không phải do bỏ qua chế độ.)

### Part 3 — Lập luận mạnh nhất

**Vì sao biên tập viên có thể thấy hấp dẫn.**
- Đề cương nối hai nhánh lớn nhưng tách rời trong tài liệu chính của nó: tranh luận về sai số ước lượng và 1/N (DeMiguel và cộng sự, 2009; Kan và Zhou, 2007), và tài liệu về chế độ thị trường (Ang và Bekaert, 2002; Guidolin và Timmermann, 2007).
- Câu hỏi được đặt sắc: *thứ hạng* của các mô hình danh mục có đổi theo chế độ không, và *chi phí của sự không ổn định đó* lớn đến đâu. Đề cương tự nêu: "Hành vi thị trường đổi theo chế độ; chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không."
- Nếu được trả lời đáng tin cậy, câu hỏi này cho nhà nghiên cứu và nhà quản lý quỹ một đại lượng *có đơn vị kinh tế* (điểm phần trăm lợi suất tương đương chắc chắn) cho rủi ro mô hình ở cấp quyết định. Đề cương liên hệ trực tiếp đại lượng này với khung giám sát SR 11-7 / SR 26-2 và Thông tư 83/2025/TT-NHNN.

**Điểm mạnh thiết kế thực sự giúp đề cương nổi bật.**
- *Nhận diện được cái bẫy cơ học của thước đo:* "Kỳ vọng của $R_t$ vẫn dương khi các mô hình ngang chất lượng, vì giá trị lớn nhất của các đại lượng có nhiễu tăng theo phương sai của nhiễu". Đây là đúng cái bẫy khiến "regret cao hơn ở chế độ căng thẳng" có thể chỉ là hệ quả của biến động cao hơn.
- *Hai lớp phòng vệ trước cái bẫy đó:* chuẩn hóa bằng sai số chuẩn bootstrap, và phân phối rỗng giữ nguyên tương quan chéo và biến động.
- *Tiêu chí ủng hộ ba điều kiện cho H1 được ấn định trước.*
- *Quy tắc "không kết luận" khi số cửa sổ căng thẳng dưới 10*, kèm hiệu chỉnh Holm.
- *Chọn lợi suất tương đương chắc chắn thay tỷ số Sharpe, có lý do rõ:* "khi lợi suất vượt trội trung bình âm ... danh mục biến động hơn lại có tỷ số Sharpe ít âm hơn".

Với một đề cương, mức trung thực về phương pháp này hiếm gặp và là điểm cộng thật.

**Kết quả gánh đóng góp.** Đóng góp đứng hay đổ chủ yếu ở hệ số $\beta$ của mức hối tiếc chuẩn hóa $R_t$ theo $S_t$ trong phương trình (5), tức H1, vượt phân vị 95% của phân phối rỗng.

**Kết quả đó mạnh đến đâu nếu xét riêng.** Ở mức thận trọng.
- Thiết kế dự kiến chỉ có "khoảng 28 cửa sổ đánh giá độc lập", và "khủng hoảng tài chính toàn cầu chủ yếu phục vụ ước lượng chế độ". Số cửa sổ thực sự rơi vào chế độ căng thẳng có thể chỉ vài cái (COVID-19 2020, quý IV/2022), và có thể dưới ngưỡng 10. Khi đó, theo đúng quy tắc đã đăng ký, kết quả chính sẽ là "không kết luận".
- $S_t$ được xác định từ biến động và lợi suất, nên phần lớn sức nặng nhận diện dồn vào phân phối rỗng.
- H2 và H4 được tác giả tự gọi là "liên hệ có điều kiện, không gọi là quan hệ nhân quả".
- Thủ tục giám sát ba bước "chưa qua kiểm nghiệm với người dùng".

Vì vậy, lập luận mạnh nhất hiện nằm ở *khung khái niệm và thước đo*, không nằm ở một phát hiện thực nghiệm đủ công suất. Hai điều sẽ làm đóng góp vững hơn rõ rệt: chuyển thước đo sang dữ liệu có nhiều giai đoạn căng thẳng hơn, ví dụ các bộ dữ liệu của DeMiguel và cộng sự (2009), và đặt Việt Nam làm phép thử ngoài mẫu. Đây là gợi ý mở rộng, không có trong đề cương.

### Part 4 — Xếp hạng tạm thời

**Incremental (Gia tăng)**

Lập luận ủng hộ có thật. Câu hỏi "chi phí của việc chọn sai mô hình danh mục có phụ thuộc chế độ không" được đặt sắc. Thước đo mức hối tiếc có đơn vị phúc lợi, có hiệu chỉnh tường minh cho thiên lệch cơ học của toán tử max. Thiết kế đăng ký trước có kỷ luật hiếm thấy.

Tuy vậy, so với chuẩn của một tạp chí hàng đầu chuyên ngành, kết quả gánh đóng góp (H1) dựa trên khoảng 28 cửa sổ sáu tháng ở một thị trường cận biên với rất ít giai đoạn căng thẳng độc lập. Các kênh giải thích chỉ là tương quan có điều kiện. Phần lớn phần vượt trội so với Danielsson và cộng sự (2016) và DeMiguel và cộng sự (2009) là thay đổi đơn vị đo và bối cảnh, chưa phải một cơ chế hay phương pháp tổng quát mới.

Đề cương có thể tiến tới mức "Significant" nếu thước đo chứng minh được tính tổng quát trên nhiều thị trường và có H1 đủ công suất. Với phạm vi chỉ Việt Nam như hiện tại, mức xếp hạng mạnh nhất có thể bảo vệ là Incremental, phù hợp hơn với tạp chí chuyên ngành tầm trung hoặc tạp chí về thị trường mới nổi.

### Skeptic's Case

## Agent 8: Contribution Skeptic

*(Tôi đã đọc toàn bộ live text của `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/main.tex`. Đây là đề cương, chưa có kết quả. Vì vậy "delivery" bên dưới là những gì thiết kế đã đăng ký có thể tạo ra, không phải kết quả thực. Tôi không sửa file nào.)*

### Part 1 — The Contribution Under Attack

**Đóng góp tuyên bố, tóm trong một câu.** Đề tài nói mình là nghiên cứu đầu tiên đo "rủi ro lựa chọn mô hình" theo chế độ thị trường cho quyết định phân bổ danh mục ở Việt Nam. Thước đo là mức hối tiếc CE: lấy CE của mô hình tốt nhất nhìn lại sau thực tế trừ CE của mô hình đã chọn trước, trong tập 7 mô hình, trên rổ 30 cổ phiếu HOSE. Đề tài muốn chứng minh rủi ro này cao hơn ở chế độ căng thẳng (H1), gắn với thanh khoản, tương quan đuôi và phân tán chéo (H2, H4), và giảm được nhờ kết hợp mô hình hoặc danh mục vững chắc (H3).

**Lập luận mạnh nhất để bác bỏ, chỉ dựa trên thư mục của chính đề cương:**

1. **H1 là kết quả đã biết, chỉ chuyển sang một biến kết quả khác.** Chính đề cương tóm tắt Danielsson và cộng sự (2016) như sau: "rủi ro mô hình của các mô hình rủi ro thị trường và rủi ro hệ thống tăng theo mức bất định và nhỏ khi thị trường yên ắng". Ang và Bekaert (2002) thì được tóm là "tương quan và biến động cùng tăng ở chế độ xấu". Như vậy H1 ("Rủi ro lựa chọn mô hình ở chế độ căng thẳng cao hơn ở chế độ bình thường") là phát hiện của Danielsson và cộng sự (2016), đổi từ dự báo VaR sang CE của danh mục. Phần chênh lệch mới chỉ là đổi biến kết quả, không phải một cơ chế mới. Bảng 2 còn ghi Danielsson và cộng sự (2016) là "Cơ sở" của H1, tức chính tác giả thừa nhận giả thuyết này được suy ra từ kết quả đã có.

2. **Khoảng trống "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục" bị chính thư mục bác bỏ.**
   - Đề cương viết Tu (2010) "ước tính nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất lợi suất tương đương chắc chắn thường trên 2% mỗi năm, có thể tới 10%". Đó chính là tổn thất CE do chọn sai mô hình (mô hình một chế độ thay vì mô hình chuyển chế độ), đo bằng đúng thước đo mà đề tài dùng.
   - Kan và Zhou (2007) đo tổn thất hiệu quả ngoài mẫu do sai số ước lượng.
   - DeMiguel và cộng sự (2009) so 14 mô hình theo CE.
   - Mức hối tiếc so với lựa chọn tốt nhất nhìn lại là khái niệm chuẩn mà đề cương tự gán cho Gilboa và Schmeidler (1989) và Hansen và Sargent (2008).

   Cái thực sự mới chỉ còn là ghép các mảnh này lại theo chế độ, trên một thị trường.

3. **H3 đã được chính các tài liệu được trích dẫn trả lời.** Đề cương viết Timmermann (2006) cho thấy "dự báo kết hợp thường tốt hơn dự báo riêng lẻ", Avramov (2002) cho thấy kết hợp Bayes tốt hơn chọn một mô hình, Rapach và cộng sự (2010) cho thấy "kết hợp dự báo bù được phần chất lượng dự báo mất đi do mô hình bất ổn định", và Tu và Zhou (2011) cho thấy kết hợp 1/N với trung bình-phương sai "vượt 1/N trong hầu hết kịch bản". Nếu H3 được ủng hộ ở Việt Nam, đó là xác nhận một kết quả đã biết trong bối cảnh mới.

4. **Các "biến kênh" H2 và H4 phần lớn là số học danh mục, chưa phải cơ chế kinh tế.** Phân tán CE giữa các mô hình phụ thuộc trực tiếp vào hai yếu tố: phân tán của lợi suất từng cổ phiếu và mức trọng số các mô hình khác nhau. Khi lợi suất các cổ phiếu phân tán mạnh, cùng một khác biệt trọng số sẽ tạo ra khác biệt lợi suất danh mục lớn hơn. Vì vậy H4 ("độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao") gần như đúng theo định nghĩa. Nhánh tương quan của H2 cũng vậy: chính văn bản viết "tương quan cao làm các danh mục chỉ mua hội tụ", tức là một hệ quả cơ học. Gọi đó là "kênh" hay giao thoa với tài chính hành vi ("bầy đàn") là phóng đại. Phép kiểm định cũng chỉ phân biệt được hai giả thuyết đối lập về dấu hệ số, không phân biệt được cơ chế kinh tế với hệ quả cơ học.

5. **Khoảng trống còn lại chủ yếu là "chưa ai làm ở Việt Nam".** Bảng 1 nêu khoảng trống (2)–(4) theo kiểu "Danh mục ở Việt Nam… Chưa đặt các mô hình vào một tập cạnh tranh", "Chế độ thị trường ở Việt Nam… Chưa nối chế độ với chất lượng quyết định danh mục", "Bầy đàn ở Việt Nam… Chưa gắn bầy đàn với rủi ro của việc chọn mô hình". Ba trong bốn khoảng trống được định nghĩa theo địa lý. Đây đúng là "kết quả đã biết, đặt vào bối cảnh mới".

6. **Bản thân lời khẳng định tính mới cũng yếu, theo chính lời tác giả.** Đề cương viết: "Phạm vi tìm kiếm chưa gồm Scopus, Web of Science và các tạp chí tiếng Việt trong nước… Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn". Phần đóng góp dự kiến cũng mở đầu bằng "Dựa trên phần tóm tắt của các công trình gần nhất". Ở một tạp chí top-field, khẳng định "đầu tiên" dựa trên việc đọc tóm tắt sẽ bị biên tập viên coi là chưa được chứng minh. Ngoài ra, tôi cho rằng có tài liệu về kết hợp dự báo hoặc kết hợp danh mục có điều kiện theo chế độ, và về ổn định thứ hạng chiến lược qua chu kỳ, mà đề cương chưa trích. `[UNVERIFIED — based on general knowledge; authors must confirm]`

7. **Khẳng định "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo [chế độ]" chưa được đối chiếu với nhóm tài liệu chế độ mà đề cương trích.**
   - Guidolin và Timmermann (2007) và Ang và Bekaert (2002) cho thấy danh mục tối ưu đổi theo chế độ.
   - Kritzman và cộng sự (2012) cho thấy "chiến lược động… vượt chiến lược tĩnh".

   Khi chiến lược tối ưu đổi theo chế độ, việc một quy tắc chọn tĩnh nhìn lại 36 tháng có mức hối tiếc cao hơn ở chế độ căng thẳng là hệ quả trực tiếp của các tài liệu này, chưa phải phát hiện mới.

### Part 2 — Framing vs. Delivery

**Những lời hứa mà thiết kế khó hoặc không thể thực hiện:**

1. **Lời hứa thực nghiệm chính có thể tự vô hiệu theo chính quy tắc đã đăng ký.** Đề cương hứa "cung cấp bằng chứng cho thị trường Việt Nam về mức độ, thời điểm và các kênh của rủi ro lựa chọn mô hình". Nhưng thiết kế ghi:
   - "đề tài dự kiến có khoảng 28 cửa sổ đánh giá độc lập, và khủng hoảng tài chính toàn cầu chủ yếu phục vụ ước lượng chế độ";
   - "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận".

   Mức hối tiếc chỉ tính được từ khoảng năm 2012. Giai đoạn 2012–2026 có các đợt căng thẳng chính được nêu là COVID-19 năm 2020 và căng thẳng trái phiếu từ quý IV/2022. Vì vậy số cửa sổ 6 tháng ở chế độ căng thẳng nhiều khả năng dưới 10. Đây là suy luận của tôi từ các con số trong đề cương, tác giả cần kiểm tra. Nếu đúng, H1, H2 và H3 đều có khả năng cao rơi vào nhóm "không kết luận" ngay theo thiết kế. Đề cương cũng không có phân tích công suất trước, chỉ hứa "báo cáo số giai đoạn căng thẳng rơi vào phần mẫu tính được mức hối tiếc". Mẫu kiểm tra sau ngày đăng ký (quý 4 năm thứ nhất) chỉ dài khoảng 2–3 năm, tức thêm vài cửa sổ.

2. **Lời hứa về lý thuyết không có mô hình lý thuyết đi kèm.** Đề cương viết: "Về lý thuyết, đề tài đưa ra khung khái niệm và thước đo rủi ro lựa chọn mô hình theo chế độ". Nhưng thước đo là $R_t = U_{o,t} - U_{c,t}$, một mức hối tiếc chuẩn. Không có mô hình nào cho biết mức hối tiếc *nên* phụ thuộc vào chế độ, số mô hình hay độ dài mẫu như thế nào. Khung lý thuyết ở mục 4.3.1 chỉ có một câu điều kiện: "nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng, tổn thất do chọn sai mô hình cũng tăng theo". Câu này là trực giác, chưa phải một đóng góp lý thuyết.

3. **Lời hứa về "kênh" mâu thuẫn với chính các hạn chế mà đề cương tự đặt ra.**
   - Câu hỏi 2 hỏi các biến kênh "giải thích được bao nhiêu phần chênh lệch giữa hai chế độ".
   - Nhưng đề cương lại viết "Khi hệ số này [VIF] vượt ngưỡng, đề tài báo cáo hai phương trình tách riêng và không diễn giải riêng từng hệ số" và "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả".

   Với khoảng 28 quan sát, $S_t$ và mọi biến kênh đều phụ thuộc vào biến động, và biến động thực hiện luôn có trong $X_t$. Phép phân rã $\beta_0-\beta_1$ vì thế gần như chắc chắn không định danh được. Chữ "kênh" hứa nhiều hơn mức một hồi quy với 28 quan sát có thể cho.

4. **Lời hứa so sánh quốc tế mà thiết kế không kiểm định.** Đề cương viết: "Thị trường Việt Nam có thanh khoản hạn chế… nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển". Thiết kế không có thị trường đối chứng nào ("kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam"), nên không kiểm tra được câu này. Đây cũng là lý do duy nhất đề cương đưa ra cho việc bối cảnh Việt Nam đáng quan tâm.

5. **Lời hứa về chính sách và thực tiễn đặt sai đối tượng.**
   - Phần động cơ viện dẫn SR 11-7/SR 26-2 và Thông tư 83/2025/TT-NHNN, nhưng tự thừa nhận "Khung này áp dụng cho ngân hàng, còn người dùng kết quả của đề tài là công ty quản lý quỹ".
   - Việc các quỹ có dùng mô hình định lượng hay không vẫn còn bỏ ngỏ: "Thí sinh sẽ xác định… mức độ họ dùng mô hình định lượng để phân bổ danh mục".
   - Thủ tục ba bước ("kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng") được "suy ra từ H3, chưa qua kiểm nghiệm với người dùng". Nếu H3 không kết luận, thủ tục này không còn căn cứ.

6. **Kết quả trung tâm có làm thay đổi cách nhìn của giới kinh tế không?** Có lẽ là không. Nếu H1 được ủng hộ, kết quả khớp với Danielsson và cộng sự (2016) và Tu (2010). Nếu H3 được ủng hộ, kết quả khớp với Timmermann (2006) và Tu và Zhou (2011). Nếu giả thuyết bị bác bỏ, đề cương tự kết luận "quy tắc 1/N đủ dùng ở Việt Nam", vốn là thông điệp của DeMiguel và cộng sự (2009). Mọi nhánh kết quả đều xác nhận định kiến sẵn có, và không nhánh nào tạo ra một điều bất ngờ có ý nghĩa ngoài phạm vi Việt Nam.

### Part 3 — What It Would Take

1. **Định nghĩa lại đối tượng thành "đảo hạng" và đo trực tiếp.** Thay vì chỉ đo mức hối tiếc trung bình, cần kiểm định độ bền thứ hạng giữa các chế độ: tương quan hạng Spearman giữa các cửa sổ, ma trận chuyển của "mô hình tốt nhất", và xác suất quy tắc chọn trúng mô hình tốt nhất (selection skill) ở từng chế độ. Đây mới là đại lượng phân biệt "rủi ro *lựa chọn*" với "rủi ro mô hình" kiểu Danielsson và cộng sự (2016), và với "giá trị của chuyển chế độ" kiểu Tu (2010).

2. **Xây một chuẩn lý thuyết hoặc mô phỏng cho mức hối tiếc dưới giả thuyết không.** Cần suy ra giá trị kỳ vọng của $R_t$ khi các mô hình ngang nhau, như một hàm của $|M|$, độ dài cửa sổ, biến động và tương quan chéo giữa các chiến lược. Sau đó tách mức hối tiếc thành (a) phần thuần do nhiễu (giá trị lớn nhất của các đại lượng có nhiễu) và (b) phần do đảo hạng thực. Bước chuẩn hóa bằng sai số chuẩn bootstrap và phân phối rỗng ở mục 4.3.7 mới là bản thô của việc này. Làm thành một kết quả hình thức có thể là đóng góp phương pháp thực sự.

3. **Đối chiếu trực tiếp với Tu (2010) và Kan và Zhou (2007).** Cần chỉ ra mức hối tiếc theo chế độ thêm được gì so với tổn thất CE do bỏ qua chuyển chế độ (Tu, 2010) và tổn thất do sai số ước lượng (Kan và Zhou, 2007). Nếu không tách được ba đại lượng này, phần chênh lệch so với tài liệu sẽ bằng 0.

4. **Kiểm soát phần cơ học của H2 và H4.** Với mỗi cửa sổ, tính phân tán CE mà trọng số các mô hình và ma trận hiệp phương sai ước lượng đã ngụ ý, kiểu $(w_m-w_{m'})'\hat\Sigma(w_m-w_{m'})$. Sau đó kiểm định xem thanh khoản, tương quan đuôi và phân tán chéo có giải thích được *phần dư* hay không. Chỉ khi đó mới nên gọi các biến này là "kênh". Nếu không làm được, nên bỏ H4 và bỏ khung "bầy đàn/hành vi".

5. **Giải quyết công suất kiểm định ngay từ thiết kế, không để đến lúc gọi kết quả là "không kết luận".**
   - Làm phân tích công suất trước khi đăng ký: hiệu ứng nhỏ nhất phát hiện được với khoảng 28 cửa sổ, và số cửa sổ căng thẳng dự kiến.
   - Mở rộng mẫu thành bảng dữ liệu nhiều thị trường, gồm các thị trường mới nổi và cận biên khác cùng ít nhất một thị trường phát triển. Việc này vừa tăng số đợt căng thẳng độc lập, vừa kiểm định được câu "chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển".
   - Hoặc dùng thêm HNX hay rổ VN100 để tăng chiều cắt ngang.

   Với tạp chí top-field, Việt Nam nên là một trường hợp trong bảng dữ liệu, không phải toàn bộ mẫu.

6. **Dùng quy tắc chọn mô hình thực tế và nhiều quy tắc chọn.** Quy tắc "chọn CE cao nhất 36 tháng trước" là một chuẩn yếu. Cần thêm: chọn dựa trên tập tin cậy mô hình (MCS), chọn có điều kiện theo xác suất chế độ, và chọn theo tỷ số Sharpe hiệu chỉnh. Từ đó chỉ ra rủi ro lựa chọn có bền với quy tắc chọn hay chỉ là hệ quả của một quy tắc ngây thơ.

7. **Lượng hóa ý nghĩa kinh tế cho người dùng thật.** Cần có dữ liệu, dù ở mức mô tả, về mức các công ty quản lý quỹ Việt Nam dùng mô hình định lượng, quy mô tài sản liên quan, và mức hối tiếc quy ra điểm cơ bản trên tài sản quản lý. Nếu không có những số liệu này, phần hàm ý quản trị và giám sát chưa đủ căn cứ.

8. **Hoàn tất rà soát tài liệu trước khi khẳng định tính mới.**
   - Đọc toàn văn các công trình gần nhất, mở rộng tìm kiếm sang Scopus, Web of Science và tạp chí trong nước.
   - Tìm riêng tài liệu về kết hợp danh mục hoặc dự báo có điều kiện theo chế độ, và về độ bền thứ hạng chiến lược `[UNVERIFIED — based on general knowledge; authors must confirm]`.
   - Bỏ hoặc làm mềm câu "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục", vì chính Tu (2010) và DeMiguel và cộng sự (2009) trong thư mục đã mâu thuẫn với câu này.

9. **Viết lại H3 thành câu hỏi điều kiện mà tài liệu chưa trả lời.** Hiện H3 hỏi "kết hợp có tốt hơn chọn một mô hình không", điều Timmermann (2006) và Tu và Zhou (2011) đã trả lời. Nên hỏi lợi ích của việc kết hợp có *tăng* ở chế độ căng thẳng hay không, và có còn sau chi phí giao dịch khi thanh khoản cạn hay không. Cần một kiểm định tương tác chế độ × cơ chế có chuẩn hiệu chuẩn rõ ràng.

### Part 4 — Provisional Rating

**Insufficient for target journal.**

Thiết kế cẩn thận và trung thực hơn mức thường gặp ở một đề cương: có đăng ký trước, có phân phối rỗng, có quy tắc "không kết luận". Nhưng đóng góp cốt lõi là ghép các kết quả đã có trong chính thư mục: rủi ro mô hình tăng khi bất định cao (Danielsson và cộng sự, 2016), tổn thất CE do bỏ qua chế độ (Tu, 2010), và kết hợp tốt hơn chọn (Timmermann, 2006; Tu và Zhou, 2011). Những kết quả này được áp dụng cho một thị trường đơn lẻ với 30 cổ phiếu. Thiết kế với khoảng 28 cửa sổ, trong đó nhiều khả năng dưới 10 cửa sổ căng thẳng, có thể không đủ để kết luận về chính giả thuyết trung tâm, và mọi kết quả có thể xảy ra đều xác nhận định kiến sẵn có.

So với tài liệu, mức đóng góp là Incremental, phù hợp với một luận án tiến sĩ hoặc một tạp chí chuyên ngành cấp thấp hơn. Để đạt chuẩn top-field, đề tài cần ít nhất ba thay đổi: chuẩn lý thuyết hoặc mô phỏng tách nhiễu khỏi đảo hạng (mục 2), mẫu nhiều thị trường (mục 5), và xử lý phần cơ học của các "kênh" (mục 4).
### Synthesis

Hai agent đồng ý ở bốn điểm: (i) câu hỏi được đặt sắc, chuyển trọng tâm từ "mô hình nào tốt nhất trung bình" sang "chọn sai mô hình tốn bao nhiêu theo chế độ"; (ii) thiết kế có kỷ luật hiếm thấy ở cấp đề cương (đăng ký trước, phân phối rỗng, quy tắc không kết luận, tự khai báo dữ liệu đã xem); (iii) kết quả gánh đóng góp là β của H1, và nó dễ bị quy tắc của chính đề cương xếp vào "không kết luận" vì chỉ có khoảng 28 cửa sổ; (iv) phần mới so với tài liệu chủ yếu là đổi đơn vị đo và bối cảnh, chưa phải một cơ chế tổng quát mới. Điểm khác nhau quyết định là: thước đo hối tiếc theo chế độ, có phân phối rỗng, có tạo được một đại lượng mới tách khỏi Tu (2010) và Danielsson và cộng sự (2016) hay không. Tác giả phải thắng điểm này ngay ở phần đặt vấn đề. Xếp hạng tổng hợp: Incremental (advocate) / Insufficient for target journal (skeptic), không lấy trung bình. Thay đổi có lợi nhất cho đóng góp, theo Agent 8 Part 3: xây một chuẩn mô phỏng hoặc lý thuyết cho mức hối tiếc dưới giả thuyết không, để tách phần do nhiễu khỏi phần do đảo hạng thực. Novelty relative to literature not cited in the paper has not been verified.

---

## 2. Referee Assessment (Identification, Analyses, Positioning & Fit)

## Agent 6: Referee Assessment

*(Ghi chú phạm vi: tài liệu là đề cương nghiên cứu sinh, chưa có kết quả. Tôi đánh giá thiết kế và các phân tích dự kiến theo chuẩn của một tạp chí hàng đầu chuyên ngành tài chính. Những tài liệu tôi nêu tên mà đề cương không trích đều được gắn nhãn [UNVERIFIED — based on general knowledge; authors must confirm].)*

### Part 1 — Identification and Credibility

**Nguồn biến thiên dùng để nhận diện.** Kết quả chính (H1) dựa trên biến thiên theo thời gian giữa khoảng 28 cửa sổ đánh giá 6 tháng: "Với mẫu 2007--2026, đề tài dự kiến có khoảng 28 cửa sổ đánh giá độc lập". Biến giải thích là $S_t$, "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng đăng ký trước". Biến này lấy từ mô hình Markov ước lượng trên chính lợi suất VN-Index. Biến phụ thuộc là mức hối tiếc $R_t = U_{o,t} - U_{c,t}$ hoặc độ phân tán $D_t$, cả hai tính từ lợi suất tương đương chắc chắn (CE) $U_{m,t} = \mu_{m,t} - \frac{\rho}{2}\sigma^2_{m,t}$.

**Bản chất của kết quả.** Kết quả mang tính mô tả và tương quan. Đề cương tự nhận đúng điều này: "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả." Tuy vậy, khung ở Hình 1 vẫn viết theo ngôn ngữ cơ chế: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình" và "Các biến kênh … giải thích một phần chênh lệch giữa hai chế độ". Phép phân rã $\beta_0 - \beta_1$ cũng được trình bày như một phân rã trung gian. Thiết kế hiện tại không nhận diện được trung gian. Kết quả nên được gọi là phân rã thống kê.

**Các mối đe dọa chính (điều một nhà kinh tế lượng khó tính sẽ hỏi ở hội thảo):**

1. **Công suất kiểm định: thiết kế gần như chắc chắn cho ra "không kết luận".** Có khoảng 28 cửa sổ, trong đó GFC "chủ yếu phục vụ ước lượng chế độ". Số cửa sổ căng thẳng thực sự vì vậy có lẽ chỉ vài cửa sổ: COVID-2020, quý IV/2022, có thể thêm một giai đoạn khác. Trong khi đó, quy tắc đăng ký trước ghi: "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Trừ khi mẫu có ít nhất 10 cửa sổ căng thẳng không chồng lấn, tức khoảng 5 năm căng thẳng trong 15 năm có tính được mức hối tiếc, H1 sẽ không kết luận theo chính quy tắc của đề cương. Thêm vào đó, cách đếm một cửa sổ là "ở chế độ căng thẳng" chưa được định nghĩa, vì $S_t$ là biến liên tục. Đề cương chưa có phân tích công suất hay mô phỏng trước. Đây là vấn đề lớn nhất của thiết kế.

2. **Quan hệ cơ học giữa biến động, chế độ và CE.** Chế độ căng thẳng được định nghĩa là chế độ "có phương sai điều kiện cao nhất". CE trừ đi $\frac{\rho}{2}\sigma^2$, nên khi phương sai tăng thì chênh lệch CE giữa các mô hình có tải phương sai khác nhau tăng theo một cách cơ học. Đề cương có nhận ra một phần ("giá trị lớn nhất của các đại lượng có nhiễu tăng theo phương sai của nhiễu") và chuẩn hóa bằng sai số chuẩn bootstrap. Nhưng sau chuẩn hóa, $R_t$ không còn là tổn thất kinh tế (điểm CE) nữa; nó trở thành một thống kê kiểu $t$ đo mức tách bạch của các mô hình. Hai đại lượng này có thể đi ngược chiều nhau ở chế độ căng thẳng: tổn thất kinh tế tăng nhưng độ tách bạch thống kê giảm. Định nghĩa "rủi ro lựa chọn mô hình là tổn thất kỳ vọng" ở phần 4.1 vì vậy không khớp với thước đo chính.

3. **Phân phối rỗng không đúng với khái niệm "ngang chất lượng" theo CE.** Đề cương viết: "đề tài loại chênh lệch trung bình giữa các mô hình trong từng chế độ nhưng giữ nguyên tương quan chéo và biến động". Nhưng CE phụ thuộc cả phương sai. Sau khi loại chênh lệch trung bình, các mô hình vẫn khác nhau về CE vì $\sigma^2_m$ khác nhau, và chênh lệch này phóng đại ở chế độ căng thẳng. Như vậy phân phối rỗng chưa loại được chính kênh cơ học ở điểm 2. Phân phối rỗng đúng phải cân bằng CE, không chỉ cân bằng trung bình. Ngoài ra, việc khử trung bình "trong từng chế độ" dùng phân loại chế độ, trong khi phân loại chế độ là một kết quả ước lượng có sai số.

4. **Kiểm soát biến động thực hiện gần như hấp thụ hết biến chế độ.** "Biến động thực hiện luôn có mặt trong $X_t$", trong khi $S_t$ được định nghĩa chủ yếu bằng phương sai. Vì vậy $\beta$ có điều kiện chỉ còn được nhận diện từ phần chênh lệch lợi suất trung bình giữa các chế độ, trên khoảng 28 quan sát. Thêm 4–5 biến kênh nữa (Amihud, tương quan đuôi, tương quan hiệu chỉnh, CSAD) thì số bậc tự do còn rất ít. Ngưỡng VIF = 5 chỉ giúp nhận ra đa cộng tuyến, không giải quyết được nó. Phép $\beta_0 - \beta_1$ còn phụ thuộc thứ tự đưa biến vào. Phân rã theo kiểu Gelbach (2016) [UNVERIFIED — based on general knowledge; authors must confirm] sẽ là chuẩn tối thiểu.

5. **Chiều của H4 mâu thuẫn với lý thuyết bầy đàn được trích dẫn.** Christie và Huang (1995) và Chang và cộng sự (2000) coi bầy đàn là độ phân tán chéo *thấp* bất thường. Vậy mà H4 viết: "độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao". Hơn nữa, quan hệ dương giữa phân tán chéo và chênh lệch giữa các danh mục gần như cơ học: hai danh mục khác trọng số sẽ có lợi suất cách xa nhau hơn khi các cổ phiếu phân tán hơn. H4 như đang viết không kiểm định bầy đàn.

6. **H2 về thanh khoản có thể đúng theo cấu trúc.** Nếu chi phí giao dịch được tham số hóa theo thanh khoản hay độ phi thanh khoản, hệ số Amihud dương là hệ quả của cách xây dựng biến. Đề cương mới chỉ nói "tham số hóa chi phí giao dịch" mà chưa nêu dạng hàm cụ thể.

7. **Đăng ký trước bị "nhiễm" ngay trong lịch trình.** Đề cương thừa nhận thí sinh đã thấy kết quả 2019–2025, nhưng Bảng 5 lại dự kiến: "Quý 2: ước lượng thử bảy mô hình trên giai đoạn 2019--2025 … Quý 4: đăng ký trước". Đề cương cũng viết: "Các độ dài cửa sổ là giá trị dự kiến, và thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất". Điều này mâu thuẫn với câu "Thí sinh đăng ký trước kế hoạch phân tích trước khi ước lượng chính thức tập mô hình". Thiết kế (cửa sổ, ngưỡng, siêu tham số) sẽ được chọn sau khi đã thấy các giai đoạn căng thẳng quan trọng nhất trong mẫu. Còn "mẫu kiểm tra riêng" (dữ liệu sau ngày đăng ký, khoảng cuối năm 1 đến năm 4) chỉ dài khoảng 4–6 cửa sổ 6 tháng.

8. **Quy tắc chọn mô hình và quy tắc tinh chỉnh.** Mức hối tiếc chỉ đo cho một quy tắc chọn duy nhất ("CE ngoài mẫu cao nhất trong 36 tháng liền trước"). Do đó H1 là kết luận về quy tắc này, chưa phải về "rủi ro lựa chọn mô hình" nói chung. Ngoài ra, các siêu tham số được chọn "từ một lưới cho trước, bằng cùng một quy tắc", nhưng quy tắc đó chưa được nêu. Nếu tinh chỉnh trên toàn mẫu thì xuất hiện thiên lệch nhìn trước.

9. **Ma sát đặc thù của HOSE.** Biên độ giá, T+2, giới hạn sở hữu nước ngoài và ngày chạm trần/sàn trong khủng hoảng làm giá cuối ngày không giao dịch được, đúng vào lúc căng thẳng. Đề cương chỉ nói sẽ "ghi kèm nguồn của biên độ dao động giá" mà không xử lý trong khâu đo CE.

10. **Kiểm định bội và thiên lệch chọn lọc chưa nhất quán.**
    - Holm "ở mức 10% cho bốn giả thuyết" có tính cả H4, vốn được tuyên bố là thăm dò.
    - Bản thân H1 gồm ba điều kiện, còn H3 gồm nhiều cơ chế × nhiều tiêu chí.
    - Hiệu chỉnh thiên lệch chọn lọc dùng tỷ số Sharpe hiệu chỉnh (Bailey và López de Prado, 2014), trong khi đề cương đã loại Sharpe khỏi vai trò thước đo chính.

11. **H3 so sánh trên các tập M khác nhau.** "Khi kiểm định H3, đề tài loại cơ chế (ii) và (iii) khỏi M". Nhưng cơ chế (ii) chính là M6 (Garlappi và cộng sự, 2007) và cơ chế (iii) chính là M7 (Kritzman và cộng sự, 2012). Khi bỏ chúng ra, mức hối tiếc của "chọn một mô hình" cũng thay đổi. Kết quả là phép so sánh với mức chuẩn dịch chuyển giữa các phân tích.

**Điều kiện để nhận diện đủ thuyết phục với khán giả hàng đầu:**
- Tăng số giai đoạn căng thẳng độc lập: mở rộng sang nhiều thị trường, hoặc thêm một mẫu Mỹ dài làm phòng thí nghiệm song song, với Việt Nam là trường hợp ứng dụng.
- Xây phân phối rỗng cân bằng CE, có tính đến sai số ước lượng chế độ.
- Báo cáo song song tổn thất kinh tế (chưa chuẩn hóa) và thống kê đã chuẩn hóa.
- Tách thành phần cơ học do phương sai ra khỏi thành phần thông tin.
- Đặt đăng ký trước *trước* mọi ước lượng thử.

### Part 2 — Analyses: Required and Suggested

**Required:**

1. **[CRITICAL] Phân tích công suất và mô phỏng thiết kế trước khi đăng ký.**
   - *Phân tích:* Mô phỏng DGP có chuyển chế độ, hiệu chuẩn theo VN-Index, với hiệu ứng H1 giả định, và tính xác suất đạt cả ba điều kiện của H1 với khoảng 28 cửa sổ. Cần định nghĩa rõ cách đếm "cửa sổ căng thẳng" khi $S_t$ là biến liên tục, rồi báo cáo số cửa sổ căng thẳng kỳ vọng.
   - *Vì sao thiếu là vấn đề:* Không có phân tích này, quy tắc "dưới 10 → không kết luận" có thể khiến câu hỏi trung tâm không thể trả lời được ngay từ thiết kế.
   - *Nếu kết quả tích cực:* Mô phỏng cho thấy công suất ≥ 0,8 với hiệu ứng có ý nghĩa kinh tế thì thiết kế chứng minh được tính khả thi. Nếu không đạt, đề cương phải chuyển sang mẫu đa thị trường.

2. **[CRITICAL] Phân phối rỗng cân bằng CE và tách thành phần cơ học do phương sai.**
   - *Phân tích:* Tái lấy mẫu sao cho các mô hình có CE bằng nhau trong từng chế độ, không chỉ trung bình bằng nhau. Đồng thời báo cáo $R_t$ ở dạng tổn thất kinh tế chưa chuẩn hóa và dạng đã chuẩn hóa. Thêm một biến thể với $\rho \to 0$ (chỉ trung bình) để thấy phần do số hạng phương sai.
   - *Vì sao thiếu là vấn đề:* Như đang viết, $\beta > 0$ có thể chỉ phản ánh việc phương sai cao hơn ở chế độ căng thẳng.
   - *Nếu kết quả tích cực:* H1 vẫn đứng vững dưới phân phối rỗng cân bằng CE thì kết quả thực sự nói về *lựa chọn*, không phải về biến động.

3. **[CRITICAL] Mốc chuẩn chọn ngẫu nhiên và độ bền theo quy tắc chọn.**
   - *Phân tích:* So sánh mức hối tiếc của quy tắc "tốt nhất 36 tháng" với (a) chọn ngẫu nhiên đều trong M, (b) chọn theo Sharpe, (c) chọn trong tập tin cậy mô hình, (d) các độ dài lịch sử 12/24/60 tháng.
   - *Vì sao thiếu là vấn đề:* Không có mốc chuẩn này thì không phân biệt được "khó chọn" với "quy tắc chọn tồi". Chọn ngẫu nhiên cũng là phép thử giả (placebo) tự nhiên cho thông tin chứa trong lịch sử hiệu quả.
   - *Nếu kết quả tích cực:* Chênh lệch giữa hối tiếc của quy tắc chọn và của chọn ngẫu nhiên tăng ở chế độ căng thẳng thì đó là bằng chứng rằng lịch sử hiệu quả mất giá trị thông tin khi thị trường đổi chế độ. Phát hiện này mạnh hơn nhiều so với H1 hiện tại.

4. **[CRITICAL] Kiểm định giả cho định nghĩa chế độ và cho các biến kênh.**
   - *Phân tích:*
     - (a) Gán ngẫu nhiên các khối thời gian giả làm "căng thẳng", giữ nguyên tỷ lệ và độ dài khối.
     - (b) Thay $S_t$ bằng chế độ ước lượng trên một chuỗi không liên quan, hoặc bằng chế độ dời trễ/dời sớm $k$ cửa sổ.
     - (c) Ước lượng H2 với chi phí giao dịch bằng 0, để kiểm tra hệ số Amihud dương có phải do cấu trúc hay không.
     - (d) Đo bầy đàn theo đặc tả phi tuyến của Chang và cộng sự (2000), tức CSAD theo $|R_m|$ và $R_m^2$, thay cho CSAD thô. Đồng thời sửa chiều kỳ vọng của H4.
   - *Vì sao thiếu là vấn đề:* Không có các phép thử này thì không phân biệt được kênh kinh tế với hệ quả cơ học của cách xây dựng biến.
   - *Nếu kết quả tích cực:* Các phép thử giả không có ý nghĩa thống kê còn phép thử thật thì có, nên H2 và H4 trở nên đáng tin.

5. **[CRITICAL] Sửa thứ tự đăng ký trước và kiểm soát thiên lệch dò tìm dữ liệu cho thước đo CE.**
   - *Phân tích:* Đăng ký trước *trước* đợt "ước lượng thử bảy mô hình trên giai đoạn 2019--2025", hoặc giới hạn ước lượng thử ở giai đoạn trước 2019. Cố định cửa sổ và lưới siêu tham số, kèm một quy tắc tinh chỉnh lồng nhau theo thời gian. Thay tỷ số Sharpe hiệu chỉnh bằng các kiểm định dò tìm dữ liệu áp dụng trực tiếp cho CE: Reality Check của White (2000), SPA của Hansen (2005), StepM của Romano và Wolf (2005) [UNVERIFIED — based on general knowledge; authors must confirm]. Xác định rõ họ giả thuyết cho Holm (có tính H4 hay không).
   - *Vì sao thiếu là vấn đề:* Đây là điểm mạnh được quảng bá của đề cương, nhưng lịch trình hiện tại vô hiệu hóa nó.
   - *Nếu kết quả tích cực:* Đăng ký trước đáng tin sẽ là một lợi thế thật sự so với các bài cùng chủ đề.

**Suggested:**

1. **[MAJOR] Mở rộng đa thị trường hoặc thêm mẫu tham chiếu dài.**
   - *Phân tích:* Áp dụng đúng quy trình cho các thị trường ASEAN (đề cương đã nêu đây là hướng sau tốt nghiệp) hoặc cho danh mục ngành của Mỹ có lịch sử dài [UNVERIFIED — based on general knowledge; authors must confirm]. Sau đó ước lượng H1 trên dữ liệu bảng thị trường × cửa sổ.
   - *Vì sao quan trọng:* Đây là cách duy nhất để có đủ số giai đoạn căng thẳng, đồng thời đưa đề tài ra khỏi khuôn khổ "nghiên cứu một thị trường".
   - *Tính khả thi:* Cao với dữ liệu công khai, nhưng cần điều chỉnh kế hoạch bốn năm.

2. **[MAJOR] Phân rã mức hối tiếc thành phần do sai số ước lượng và phần do sai đặc tả.**
   - *Phân tích:* Cho từng mô hình, so sánh CE với tham số "oracle" ước lượng trên toàn cửa sổ với CE từ tham số ước lượng thực. Cách tiếp cận theo tinh thần Kerkhof và cộng sự (2010) mà đề cương đã trích.
   - *Vì sao quan trọng:* Kiểm tra trực tiếp cơ chế mà khung lý thuyết nêu ("nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng").
   - *Tính khả thi:* Khả thi với dữ liệu sẵn có.

3. **[MAJOR] Đo xác suất quá khớp khi kiểm định ngược (PBO) và độ ổn định thứ hạng theo chế độ.**
   - *Phân tích:* Ma trận chuyển thứ hạng của bảy mô hình giữa các cửa sổ; tương quan hạng Spearman giữa cửa sổ $t$ và $t+1$, tách theo chế độ; PBO theo Bailey, Borwein, López de Prado và Zhu (2017) [UNVERIFIED — based on general knowledge; authors must confirm].
   - *Vì sao quan trọng:* Trả lời trực tiếp khoảng trống mà đề cương nêu ("chưa xét thứ hạng thay đổi ra sao khi thị trường chuyển chế độ"). Các thước đo này cũng ít phụ thuộc vào thang đo phương sai.
   - *Tính khả thi:* Cao.

4. **[MAJOR] Hàm hữu dụng và thước đo đuôi thay thế cho mức hối tiếc.**
   - *Phân tích:* Tính CE theo CRRA hoặc theo hữu dụng có tính độ lệch và độ nhọn. Tính mức hối tiếc theo CVaR và theo mức sụt giảm tối đa. Hiện nay các tiêu chí đuôi chỉ dùng cho H3.
   - *Vì sao quan trọng:* Trong chế độ căng thẳng, xấp xỉ trung bình–phương sai đánh giá thấp tổn thất đuôi. Kết luận H1 có thể đổi tùy hàm hữu dụng.
   - *Tính khả thi:* Cao.

5. **[MAJOR] Truyền sai số ước lượng chế độ vào kết quả.**
   - *Phân tích:* Dùng xác suất lọc làm trọng số liên tục thay cho ngưỡng. Bootstrap cả bước ước lượng Markov. So sánh 2 với 3 chế độ và các định nghĩa theo ngưỡng sụt giảm hoặc biến động thực hiện (đề cương đã nêu). Báo cáo tỷ lệ trùng khớp giữa các định nghĩa.
   - *Vì sao quan trọng:* Đề cương tự nhận "Việc nhận diện chế độ tự nó là một dạng rủi ro mô hình". Sai số này cần đi vào khoảng tin cậy của $\beta$, không chỉ vào phần kiểm tra độ bền.
   - *Tính khả thi:* Trung bình, do tải tính toán khi ước lượng lại theo cửa sổ mở rộng.

### Part 3 — Literature Positioning

**Độ bao phủ.** Các tài liệu kinh điển về sai số ước lượng, 1/N, chuyển chế độ và tập tin cậy mô hình được trích đúng và đủ. Có một số khoảng trống đáng kể (tất cả [UNVERIFIED — based on general knowledge; authors must confirm]):

- **Lý thuyết hối tiếc.** Đây là thước đo trung tâm của đề tài, nhưng đề cương không trích công trình nào về mức hối tiếc như tiêu chí ra quyết định: Savage (1951) với minimax regret; Manski (2004) về quy tắc xử lý thống kê. Phần lý thuyết hiện chỉ dựa vào Gilboa và Schmeidler (1989) và Hansen và Sargent (2008), tức maxmin/vững chắc, khác về bản chất với regret.
- **Đo rủi ro mô hình bằng khoảng cách trên một tập mô hình.** Barrieu và Scandolo (2015, "Assessing financial model risk"), Glasserman và Xu (2014), Alexander và Sarabia (2012). Các bài này định nghĩa rủi ro mô hình là khoảng cách giữa mô hình được chọn và các mô hình cực trị trong một tập, rất gần với $R_t$. Đề cương phải phân biệt rõ với các bài này, vì nhận định "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục" có thể không đứng vững.
- **Bất định mô hình trong lựa chọn danh mục.** Pástor và Stambaugh (2000), Uppal và Wang (2003), Maenhout (2004), Anderson và Cheng (2016, BMA cho danh mục), Kan, Wang và Zhou (về danh mục tối ưu có rủi ro ước lượng), Kirby và Ostdiek (2012, phản biện DeMiguel và cộng sự), DeMiguel, Garlappi, Nogales và Uppal (2009, ràng buộc chuẩn), Jagannathan và Ma (2003), Ledoit và Wolf (2017, co rút phi tuyến), Kritzman, Page và Turkington (2010).
- **Dò tìm dữ liệu.** White (2000), Hansen (2005), Romano và Wolf (2005), Harvey, Liu và Zhu (2016).
- **Câu đố kết hợp dự báo.** Smith và Wallis (2009), liên quan trực tiếp đến H3.
- **Phân bổ tài sản theo chế độ.** Guidolin và Timmermann (2008), Nystrup và cộng sự (2015, 2017).
- **Tương quan bất đối xứng.** Ang và Chen (2002), Hong, Tu và Zhou (2007).
- **Thanh khoản và chi phí ở thị trường mới nổi.** Lesmond, Ogden và Trzcinka (1999), thước đo ngày lợi suất bằng 0, phù hợp với HOSE.

**Trích dẫn thừa.** Kahneman và Tversky (1979), Barberis và Thaler (2003), Reinhart và Rogoff (2009), Laeven và Valencia (2020, khủng hoảng *ngân hàng*), Lo và Mueller (2010) và Derman (1996) có vai trò trang trí, không tham gia vào thiết kế. Các văn bản SR 11-7/SR 26-2 và Thông tư 83/2025/TT-NHNN chiếm nguyên một đoạn ở phần lý do chọn đề tài, nhưng chính đề cương thừa nhận "Khung này áp dụng cho ngân hàng, còn người dùng kết quả của đề tài là công ty quản lý quỹ".

**Phân biệt với công trình gần nhất.** Bảng 1 so sánh chủ yếu với các bài về Việt Nam ở tạp chí khu vực. Đó không phải những đối thủ mà một biên tập viên tạp chí hàng đầu sẽ dùng để đánh giá đóng góp. Đối thủ thật là các bài đo rủi ro mô hình trên một tập mô hình (Barrieu–Scandolo, Danielsson và cộng sự) và các bài đánh giá hiệu quả của chiến lược danh mục theo chế độ hoặc theo thời gian. Đề cương cũng tự thừa nhận "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn", nên các tuyên bố "chưa công trình nào" cần được làm mềm cho đến khi đọc xong toàn văn.

**Cách đặt vấn đề tốt hơn.** Thay vì "khủng hoảng + khung giám sát", nên đặt vấn đề quanh câu hỏi: *thông tin chứa trong lịch sử hiệu quả của các mô hình danh mục có mất giá trị khi thị trường chuyển chế độ không, và giá trị của việc kết hợp hay đa dạng hóa mô hình có phụ thuộc vào trạng thái không?* Cách này gắn đề tài vào hai luồng tài liệu lớn là lý thuyết hối tiếc/quyết định thống kê và kết hợp dự báo. Việt Nam khi đó là phòng thí nghiệm có lịch sử ngắn và cú sốc dày, không phải là toàn bộ đóng góp.

### Part 4 — Journal Fit and Recommendation

**Đích thực tế.** Như thiết kế hiện tại (một thị trường cận biên, khoảng 30 cổ phiếu, khoảng 28 cửa sổ), JF/JFE/RFS gần như chắc chắn từ chối ngay vòng biên tập. JFQA và Review of Finance cũng chỉ thực tế khi có mẫu đa thị trường và một đóng góp phương pháp rõ ràng. Các đích thực tế cao nhất nếu đề tài được thiết kế lại theo hướng đa thị trường kèm thước đo mới:
- *Journal of Banking & Finance*: đã đăng Boucher và cộng sự (2014) và Pflug và cộng sự (2012) mà đề cương trích.
- *Journal of Empirical Finance* và *Journal of Financial Econometrics*: phù hợp nếu trọng tâm là kiểm định và phân phối rỗng.
- *Management Science*: phù hợp nếu khung quyết định theo hối tiếc được phát triển nghiêm túc.

**Khuyến nghị sơ bộ: Revise before sending to referees.** Thiết kế có những điểm cẩn thận hiếm gặp ở cấp đề cương: đăng ký trước, phân phối rỗng, quy tắc gọi kết quả "không kết luận", phân biệt giữa bất định và rủi ro, phân tích riêng tập mô hình tĩnh. Nhưng có hai lỗi mang tính cấu trúc khiến kết quả chính chưa thể đứng vững:
- (a) Công suất kiểm định gần như chắc chắn dẫn đến "không kết luận" theo chính quy tắc của đề cương.
- (b) Thước đo chính và phân phối rỗng chưa loại được kênh cơ học do phương sai.

Nếu nộp ở dạng hiện tại cho một tạp chí hàng đầu, sản phẩm dự kiến sẽ bị từ chối ngay vòng biên tập.

**Cần làm gì để đạt chuẩn:**
1. Chuyển sang mẫu đa thị trường, hoặc có mẫu tham chiếu dài, để có ít nhất vài chục giai đoạn căng thẳng.
2. Định nghĩa lại thước đo chính và phân phối rỗng theo hướng cân bằng CE, có mốc chuẩn chọn ngẫu nhiên.
3. Phát triển khung hối tiếc về mặt lý thuyết, liên hệ với Savage/Manski, và phân biệt rõ với Barrieu–Scandolo.
4. Sửa thứ tự đăng ký trước.
5. Sửa H4 cho đúng lý thuyết bầy đàn.
6. Thay tỷ số Sharpe hiệu chỉnh bằng các kiểm định SPA/StepM cho CE.

**Phương án thay thế thực tế** nếu vẫn giữ phạm vi Việt Nam: *International Review of Financial Analysis*, *Pacific-Basin Finance Journal*, *Emerging Markets Review*, *Journal of Portfolio Management* (nếu nhấn mạnh thủ tục giám sát mô hình), *Finance Research Letters* (cho một kết quả hẹp, ví dụ H1). Đây là đánh giá chủ quan của người phản biện.

### Part 5 — Questions to the Authors

1. Với mẫu 2007–2026, cửa sổ ước lượng 104 tuần và yêu cầu 36 tháng lịch sử hiệu quả ngoài mẫu, xin cho biết cụ thể có bao nhiêu cửa sổ đánh giá 6 tháng không chồng lấn sẽ được tính là "ở chế độ căng thẳng", và tiêu chí phân loại một cửa sổ là gì khi $S_t$ là biến liên tục. Nếu con số này dưới 10, như ước tính sơ bộ cho thấy, thì theo quy tắc đăng ký trước H1 sẽ "không kết luận". Vì sao thiết kế này vẫn được coi là trả lời được Câu hỏi 1?

2. Phân phối rỗng của bạn "loại chênh lệch trung bình giữa các mô hình … nhưng giữ nguyên tương quan chéo và biến động". Vì CE trừ đi $\frac{\rho}{2}\sigma^2_m$, các mô hình vẫn khác nhau về CE dưới giả thuyết rỗng này, và khác biệt đó lớn hơn ở chế độ có phương sai cao. Làm sao bạn bảo đảm $\beta > 0$ không chỉ phản ánh quan hệ cơ học giữa phương sai và CE? Bạn có sẵn sàng dùng phân phối rỗng cân bằng CE không?

3. Sau khi chuẩn hóa bằng sai số chuẩn bootstrap, $R_t$ không còn là "tổn thất kỳ vọng" như định nghĩa ở mục 4.1. Nếu tổn thất kinh tế tăng ở chế độ căng thẳng nhưng thước đo đã chuẩn hóa thì không, bạn sẽ kết luận gì về H1, và đại lượng nào là đại lượng mà nhà quản lý quỹ quan tâm?

4. Bảng 5 dự kiến "ước lượng thử bảy mô hình trên giai đoạn 2019--2025" ở quý 2 và đăng ký trước ở quý 4, đồng thời độ dài cửa sổ sẽ được "biện minh … sau khi ước lượng thử". Với việc giai đoạn 2019–2025 chứa hai trong số ít giai đoạn căng thẳng của mẫu và bạn đã thấy kết quả trên giai đoạn này, đăng ký trước còn bảo vệ được điều gì? Vì sao không giới hạn ước lượng thử ở dữ liệu trước 2019?

5. H4 dự đoán phân tán chéo *cao* đi cùng rủi ro lựa chọn mô hình cao, trong khi Christie và Huang (1995) và Chang và cộng sự (2000) coi bầy đàn là phân tán chéo *thấp*. Hơn nữa, quan hệ dương giữa phân tán chéo và chênh lệch giữa các danh mục khác trọng số là cơ học. H4 thực sự kiểm định bầy đàn hay chỉ kiểm định một đồng nhất thức?

6. Mức hối tiếc chỉ được đo cho quy tắc "chọn mô hình có CE cao nhất trong 36 tháng". So với chọn ngẫu nhiên trong M, quy tắc này có mức hối tiếc thấp hơn không, và chênh lệch đó có thay đổi theo chế độ không? Nếu không, kết quả nói về độ khó của việc chọn, hay chỉ về một quy tắc chọn kém?

7. Thước đo $R_t$ rất gần với cách Barrieu và Scandolo (2015) và các tài liệu liên quan định nghĩa rủi ro mô hình là khoảng cách trên một tập mô hình [UNVERIFIED — based on general knowledge; authors must confirm]. Ngoài việc áp dụng cho danh mục và theo chế độ, thước đo của bạn khác các định nghĩa đó ở điểm nào về mặt khái niệm? Ở cơ chế (i) (kết hợp mô hình), hối tiếc âm sẽ được diễn giải thế nào khi tập M đối chứng thay đổi giữa H1 và H3?


---

## 3. Unsupported Claims & Identification Integrity

## Agent 3: Unsupported Claims & Identification Integrity

Ghi chú phạm vi: Tôi chỉ đọc phần chữ đang có hiệu lực của `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/main.tex`. Đây là đề cương, chưa có kết quả. Vì vậy tôi rà xem lời văn ở phần lý do chọn đề tài, tổng quan, khung phân tích, giả thuyết, đóng góp dự kiến và hàm ý thực tiễn có vượt quá những gì thiết kế này cho phép kết luận hay không. Nhìn chung, đề cương giữ kỷ luật tuyên bố khá tốt: dòng 859–860 tự cam kết gọi kết quả là "liên hệ có điều kiện", có đăng ký trước, có quy tắc "không kết luận", và tuyên bố ưu tiên cho Việt Nam được rào đón kỹ. Các vấn đề chính nằm ở năm chỗ: (i) Hình 1 dùng ngôn ngữ nhân quả, mâu thuẫn với cam kết trên; (ii) cơ chế của H2 và H4 được viết như sự thật đã biết; (iii) các tuyên bố "chưa nghiên cứu nào" ở mục 4.2 mang phạm vi toàn cầu và không được rào đón; (iv) cách diễn giải khi dữ liệu không ủng hộ giả thuyết; (v) ý nghĩa kinh tế của kết quả bị bỏ ngỏ.

### Causal Overclaiming (must address)

1. [MAJOR] [4.3.2, đoạn diễn giải Hình 1, dòng 564–568] | "Theo Hình 1, chế độ thị trường tác động lên rủi ro lựa chọn mô hình (giả thuyết H1). Các biến kênh tác động lên chính quan hệ đó, tức giải thích một phần chênh lệch giữa hai chế độ (H2 và H4). Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục (H3)." | "Tác động" xuất hiện ba lần và trình bày khung phân tích như một mô hình nhân quả. Trong khi đó, "chế độ" chỉ là một nhãn thống kê, được ước lượng từ chính biến động và lợi suất, tức những đại lượng cấu thành R_t và D_t. Không có biến thể ngoại sinh nào cả. Đoạn này cũng mâu thuẫn trực tiếp với dòng 859–860 ("Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả"). Loại lỗi: (a), dùng ngôn ngữ nhân quả cho một liên hệ. | Fix (làm yếu ngôn ngữ): "Theo Hình 1, rủi ro lựa chọn mô hình được kỳ vọng khác nhau giữa các chế độ thị trường (H1). Các biến kênh được kỳ vọng có liên hệ với rủi ro lựa chọn mô hình và tương quan với phần chênh lệch giữa hai chế độ (H2, H4). Cơ chế giảm thiểu được kỳ vọng cho mức hối tiếc thấp hơn so với chọn một mô hình (H3)." Nên vẽ lại mũi tên trong Hình 1 thành đường liên hệ, hoặc ghi chú rằng mũi tên không mang nghĩa nhân quả.

2. [MAJOR] [Bảng 2, H2, dòng 597–600] | "hệ số của độ phi thanh khoản dương (thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau) và hệ số của tương quan đuôi âm (tương quan cao làm các danh mục chỉ mua hội tụ)" | Hai cơ chế ("làm … cách xa nhau", "làm … hội tụ") được viết ở thể khẳng định, như sự thật đã được chứng minh. Thực ra chúng là giả thuyết, và hồi quy (5) không kiểm định được kênh nào. Hệ số dương của độ phi thanh khoản tương thích với nhiều giải thích khác, chẳng hạn cả hai cùng phản ánh một cú sốc chung. Loại lỗi: (b), cơ chế được viết như sự thật. | Fix: "(giả thuyết cơ chế: khi thanh khoản cạn, các mô hình có vòng quay khác nhau có thể cho kết quả sau chi phí cách xa nhau hơn)" và "(giả thuyết cơ chế: tương quan cao có thể khiến các danh mục chỉ mua hội tụ)". Nên thêm một câu nói rõ dấu của hệ số tương thích với cơ chế nhưng không xác lập cơ chế.

3. [MAJOR] [4.1 Câu hỏi 2, dòng 352–355; Bảng 2 H2 "phần chênh lệch giữa hai chế độ do biến kênh giải thích", dòng 600–601; 4.3.7, dòng 849–852] | "chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?"; "phần chênh lệch giữa hai chế độ do biến kênh giải thích"; "Đề tài ước lượng phần chênh lệch giữa hai chế độ do các biến kênh giải thích bằng hiệu β0 − β1" | Hiệu β0 − β1 chỉ là mức thay đổi của hệ số khi thêm biến, theo kiểu phân rã trung gian Baron–Kenny. Muốn đọc nó là "phần do X giải thích" thì phải giả định X là trung gian ngoại sinh và không có biến gây nhiễu chung giữa X và Y. Ở đây độ phi thanh khoản và tương quan đuôi đều là kết quả của chính chế độ căng thẳng, nên chúng là biến kiểm soát xấu (bad controls), và β0 − β1 không có nghĩa nhân quả. "Do … giải thích" ngầm khẳng định quan hệ trung gian nhân quả. Loại lỗi: (a). | Fix: đổi thành "mức suy giảm của hệ số chế độ khi đưa biến kênh vào (β0 − β1), một thống kê mô tả về phần đồng biến chung, không phải ước lượng của hiệu ứng trung gian". Câu hỏi 2 nên sửa thành "…và hệ số chênh lệch giữa hai chế độ thay đổi bao nhiêu khi đưa các biến này vào?" Tên mục 5.4 trong Bảng 4 ("Phân rã chênh lệch theo chế độ") cũng nên sửa tương ứng.

4. [MAJOR] [4.4 Đóng góp dự kiến, dòng 973–974] | "Về thực nghiệm, đề tài cung cấp bằng chứng cho thị trường Việt Nam về mức độ, thời điểm và các kênh của rủi ro lựa chọn mô hình." | "Các kênh" khẳng định đã xác lập cơ chế, trong khi thiết kế chỉ cho phép báo cáo liên hệ có điều kiện, và H4 chỉ ở mức thăm dò. Loại lỗi: (b). | Fix: "…về mức độ, thời điểm của rủi ro lựa chọn mô hình và các biến thị trường có liên hệ thống kê với nó." Tên Chương 5 nên đổi từ "Các biến kênh của rủi ro lựa chọn mô hình" thành "Các biến thị trường liên hệ với rủi ro lựa chọn mô hình".

5. [MAJOR] [4.2 (5) và 4.4 Phạm vi nội dung, dòng 453–455 và 949–951; H4 Bảng 2, dòng 609–611] | "Bầy đàn … là một kênh hành vi có thể làm các mô hình cho kết quả khác nhau"; "độ phân tán chéo của lợi suất, một thước đo bầy đàn ở cấp thị trường" | Có hai tầng vượt mức. (i) Cơ chế "bầy đàn làm các mô hình cho kết quả khác nhau" không được lập luận ở đâu cả, chỉ được nêu ra. (ii) Mức phân tán chéo không phải thước đo bầy đàn. Trong chính Christie–Huang (1995) và Chang và cộng sự (2000), bầy đàn được suy ra khi độ phân tán *giảm*, hoặc tăng chậm hơn tuyến tính, so với |lợi suất thị trường|. Theo cách hiểu đó, "phân tán chéo cao" là dấu hiệu *ít* bầy đàn. Vì vậy, nếu H4 được ủng hộ thì kết quả không nói được gì về bầy đàn, và việc gọi phép thử này là "giao thoa với kinh tế hành vi" là vượt mức. | Fix: gọi biến này là "độ phân tán chéo của lợi suất (CSAD)". Nếu muốn nói đến bầy đàn, cần dùng hệ số phi tuyến của Chang và cộng sự (2000) ước lượng theo từng cửa sổ và đặt giả thuyết theo dấu của hệ số đó. Câu ở dòng 453–455 nên viết thành giả thuyết, kèm một lập luận cụ thể vì sao bầy đàn có thể làm khác biệt giữa các mô hình tăng hoặc giảm.

6. [MAJOR] [4.3.10, dòng 914–917] | "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam." | Câu này tự tin quá mức theo chiều ngược lại. Không bác bỏ được H0 với khoảng 28 cửa sổ, trong đó chỉ một vài cửa sổ rơi vào chế độ căng thẳng, không chứng minh được rằng rủi ro "không đổi". Câu này cũng mâu thuẫn với quy tắc "không kết luận" ở dòng 907–908 của chính đề cương. Hơn nữa, H1 không được ủng hộ cũng không suy ra được "1/N đủ dùng". Đó là một kết luận khác, cần một phép thử riêng (1/N không thua mô hình nào, với khoảng tin cậy chặt). | Fix: "Nếu dữ liệu không ủng hộ giả thuyết, đề tài báo cáo kích thước hiệu ứng và khoảng tin cậy để xác định chênh lệch giữa hai chế độ có bị chặn trên bởi một mức nhỏ về mặt kinh tế hay không (kiểm định tương đương). Chỉ khi đó đề tài mới kết luận rủi ro lựa chọn mô hình không khác biệt đáng kể giữa các chế độ."

7. [MAJOR] [4.3.1 Khung lý thuyết, dòng 545–547] | "nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng, tổn thất do chọn sai mô hình cũng tăng theo." | Mệnh đề nhân quả này được trình bày như một hệ quả tất yếu, nhưng nó không tất yếu. Chính H2 dự đoán rằng tương quan cao làm các danh mục hội tụ, khi đó mức hối tiếc có thể *giảm* dù sai số ước lượng tăng. Ngoài ra, phần "tăng do sai số ước lượng" chính là thứ mà phép chuẩn hóa theo sai số chuẩn bootstrap và phân phối rỗng (dòng 782–784, 835–839) được thiết kế để loại bỏ. Như vậy cơ chế lý thuyết được nêu và đại lượng thực sự được kiểm định không khớp nhau. Loại lỗi: (b). | Fix: "…tổn thất do chọn sai mô hình có thể tăng theo; tuy nhiên tương quan tăng có thể kéo các danh mục lại gần nhau, nên chiều tác động ròng là câu hỏi thực nghiệm." Đồng thời cần nói rõ H1, sau khi chuẩn hóa, kiểm định phần rủi ro lựa chọn *vượt quá* mức do nhiễu ước lượng.

8. [MAJOR] [4.2 (2), dòng 393–394; và cuối (1), dòng 390–391] | "Các nghiên cứu đã đo rủi ro mô hình cho dự báo và định giá, nhưng chưa đo cho quyết định phân bổ."; "nhóm tài liệu này chưa trả lời nhà đầu tư nên chọn mô hình nào và chịu tổn thất bao nhiêu khi chọn sai." | Đây là cách mô tả tài liệu vượt mức, và mâu thuẫn với chính các nguồn đề cương trích. Kan và Zhou (2007) đo tổn thất lợi suất tương đương chắc chắn do sai số tham số trong quyết định phân bổ. DeMiguel và cộng sự (2009) báo cáo chênh lệch lợi suất tương đương chắc chắn của 14 mô hình so với 1/N. Tu (2010), được trích ở dòng 440–442, ước tính tổn thất lợi suất tương đương chắc chắn khi bỏ qua chuyển chế độ, tức là tổn thất của việc chọn sai mô hình trong quyết định phân bổ. Đây là tuyên bố ưu tiên chưa kiểm chứng. | Fix: thu hẹp khoảng trống cho đúng điểm mới: "Các nghiên cứu này đo tổn thất của từng mô hình so với một chuẩn, hoặc so với tham số thật; chưa nghiên cứu nào mà thí sinh tìm được đo tổn thất kỳ vọng của việc *chọn trước* một mô hình trong tập cạnh tranh và so sánh tổn thất đó giữa các chế độ." Tác giả cần xác nhận tuyên bố này trước khi nộp.

### Generalization Issues

1. [MAJOR] [Tên đề tài; 4.1 Mục tiêu, dòng 360–363; 4.4, dòng 941 và 955] | "đo lường và giải thích rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư trên thị trường chứng khoán Việt Nam"; "kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam" | Mẫu thực tế chỉ là rổ 30 mã thanh khoản và vốn hóa lớn nhất trên HOSE, danh mục chỉ mua, tái cân bằng hằng tháng, với một tập 7 mô hình. Câu "chỉ áp dụng trong phạm vi thị trường Việt Nam" vẫn rộng hơn mẫu: nó không bao phủ HNX, UPCoM, cổ phiếu vốn hóa nhỏ và thanh khoản thấp, mà theo chính H2 đây lại là nơi rủi ro lựa chọn có thể lớn nhất. | Fix: "Kết luận áp dụng cho danh mục chỉ mua gồm các cổ phiếu thanh khoản cao trên HOSE và cho tập bảy mô hình đã đăng ký; không suy rộng cho cổ phiếu thanh khoản thấp, các sàn khác hoặc tập mô hình khác."

2. [MAJOR] [4.3.6, dòng 770–775; dùng xuyên suốt từ "nhà đầu tư"] | "Tại đầu mỗi cửa sổ đánh giá, nhà đầu tư chọn trước mô hình c có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước" | Mức hối tiếc R_t, và do đó toàn bộ "rủi ro lựa chọn mô hình", chỉ được định nghĩa với một quy tắc chọn cụ thể (chọn mô hình thắng trong 36 tháng). Nhưng lời văn của đề cương ("tổn thất kỳ vọng phát sinh khi nhà đầu tư phải chọn một mô hình", dòng 290–291) khái quát cho mọi nhà đầu tư và mọi cách chọn. Đề cương cũng tự thừa nhận chưa biết các công ty quản lý quỹ Việt Nam chọn mô hình thế nào (dòng 327–330, 952). | Fix: nói rõ thước đo này có điều kiện theo quy tắc chọn đã đăng ký. Nên thêm kiểm tra độ bền với các quy tắc khác (cửa sổ 12, 24, 60 tháng; chọn trong tập tin cậy mô hình; mức hối tiếc kỳ vọng khi chọn ngẫu nhiên đều).

3. [MAJOR] [4.1, dòng 273] | "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê." | Câu mở đầu khẳng định như sự thật phổ quát, trong khi dòng 327–330 thừa nhận thí sinh *sẽ* xác định "mức độ họ dùng mô hình định lượng để phân bổ danh mục". Động cơ thực tiễn của đề tài ở Việt Nam vì vậy dựa trên một tiền đề chưa được chứng minh. | Fix: "Nhiều tổ chức đầu tư, chủ yếu ở các thị trường phát triển, phân bổ vốn có sự hỗ trợ của mô hình thống kê; mức độ áp dụng ở Việt Nam sẽ được xác định trong năm thứ nhất."

4. [MINOR] [4.1, dòng 338–341] | "Thị trường Việt Nam có thanh khoản hạn chế và chịu nhiều cú sốc trong một lịch sử giao dịch ngắn, nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển." | Đây là một tuyên bố so sánh mà thiết kế một quốc gia không kiểm định được, vì không có thị trường đối chứng. Đoạn "thanh khoản hạn chế" cũng không có nguồn trích. | Fix: thêm nguồn cho đặc điểm thanh khoản và đổi thành "có thể khác so với thị trường phát triển; đề tài không so sánh trực tiếp". Nếu muốn giữ tuyên bố so sánh thì cần thêm một chuẩn đối chiếu, ví dụ chạy cùng quy trình trên dữ liệu Mỹ.

5. [MINOR] [4.2 (1), dòng 375–376] | "Mọi mô hình phân bổ đều mang sai số ở đầu vào." | Khái quát quá mức: quy tắc 1/N (M1) không ước lượng tham số nào. | Fix: "Mọi mô hình phân bổ dựa trên tham số ước lượng đều mang sai số ở đầu vào."

6. [MINOR] [Bảng 2, cột "Cơ sở" của H1] | "Danielsson và cộng sự (2016); Hansen và cộng sự (2011)" | Danielsson và cộng sự (2016) cho thấy rủi ro mô hình tăng theo bất định đối với *mô hình dự báo rủi ro* (VaR, rủi ro hệ thống), không phải đối với quyết định phân bổ. Dùng làm cơ sở trực tiếp cho H1 là ngoại suy. | Fix: ghi rõ đây là cơ sở gián tiếp, được ngoại suy từ bối cảnh dự báo rủi ro.

7. [MINOR] [4.1, dòng 309–313] | "Quỹ Tiền tệ Quốc tế ghi nhận thị trường trái phiếu doanh nghiệp đóng băng trong quý IV/2022 … Những cú sốc này là các giai đoạn tham chiếu" | Cú sốc trên thị trường trái phiếu doanh nghiệp được dùng làm giai đoạn tham chiếu cho chế độ căng thẳng trên thị trường cổ phiếu mà không có lập luận về sự lan truyền sang cổ phiếu HOSE. | Fix: thêm một câu, có nguồn, về diễn biến VN-Index trong giai đoạn đó, hoặc nói rõ đây là giai đoạn ứng viên cần kiểm tra.

### Missing Caveats

1. [MAJOR] Ý nghĩa kinh tế so với ý nghĩa thống kê | 4.3.7 (tiêu chí H1, dòng 840–843), tiêu chí H2 (dòng 856–858), tiêu chí H3 (dòng 882–885) | Mọi tiêu chí "được ủng hộ" đều thuần túy thống kê: vượt phân vị 95% của phân phối rỗng, khoảng tin cậy loại trừ 0, đúng dấu. Không có ngưỡng ý nghĩa kinh tế tối thiểu nào được ấn định trước. Ngoài ra, việc chia R_t và D_t cho sai số chuẩn bootstrap (dòng 782–784) biến thước đo chính thành đại lượng không đơn vị, nên người đọc không biết mức hối tiếc là bao nhiêu điểm phần trăm lợi suất tương đương chắc chắn mỗi năm. Kích thước hiệu ứng hiện chỉ được báo cáo khi kết quả "không kết luận" (dòng 908–910). | Suggested text: "Song song với thước đo chuẩn hóa, đề tài luôn báo cáo mức hối tiếc thô theo điểm phần trăm lợi suất tương đương chắc chắn năm hóa, cùng khoảng tin cậy. Tệp đăng ký trước ấn định một ngưỡng ý nghĩa kinh tế tối thiểu (ví dụ X điểm cơ bản/năm, so với mức phí quản lý quỹ điển hình); một kết quả có ý nghĩa thống kê nhưng dưới ngưỡng này được báo cáo là không quan trọng về mặt kinh tế."

2. [MAJOR] Khả năng thực thi giao dịch trong chế độ căng thẳng (giới hạn biên độ giá, ngày khóa sàn) | 4.3.8 và 4.3.10 (dòng 880–881, 912–914) | Cơ chế giảm thiểu (H3) và mọi lợi suất sau chi phí giả định giao dịch được ở giá đóng cửa. Trên HOSE, trong các phiên căng thẳng nhiều mã nằm sàn và không có người mua. Chi phí giao dịch dạng tham số cố định sẽ đánh giá thấp chi phí đúng vào lúc H3 được kiểm định, nên dễ phóng đại lợi ích của các cơ chế có vòng quay khác nhau. Đề cương có nhắc đến nguồn dữ liệu về biên độ dao động giá (dòng 643–644) nhưng không coi đó là mối đe dọa đối với kết luận. | Suggested text: "Trong ngày một mã chạm giá sàn (trần), lệnh bán (mua) của danh mục được giả định không khớp và chuyển sang phiên kế tiếp. Chi phí giao dịch được mô hình hóa tăng theo độ phi thanh khoản Amihud, và kết quả H3 được báo cáo cả với chi phí cố định lẫn chi phí phụ thuộc thanh khoản."

3. [MAJOR] Kênh thanh khoản trong H2 có vận hành được trong thước đo hay không | Bảng 2 H2 và 4.3.8 (dòng 880–881) | Cơ chế của H2 ("thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau") chỉ vận hành nếu chi phí giao dịch tăng khi thanh khoản giảm. Nếu chi phí là một tham số cố định, độ phi thanh khoản chỉ có thể liên hệ với R_t qua lợi suất, và hệ số dương sẽ không phản ánh cơ chế đã nêu. | Suggested text: "Để kênh thanh khoản có thể quan sát được trong thước đo, chi phí giao dịch trong phân tích chính được mô hình hóa là hàm tăng của độ phi thanh khoản; phiên bản chi phí cố định nằm trong kiểm tra độ bền."

4. [MAJOR] Chế độ căng thẳng hay *chuyển* chế độ | 4.3.6–4.3.7 (sau phương trình 4–5) | Với quy tắc chọn "thắng trong 36 tháng trước", mức hối tiếc cao trong một cửa sổ căng thẳng có thể chỉ phản ánh việc cửa sổ đó đến *sau* một giai đoạn bình thường. Mô hình thắng trong giai đoạn yên ắng bị chọn rồi thua, tức là do thời điểm chuyển chế độ chứ không phải do bản thân trạng thái căng thẳng. Hệ số β trong (5) không tách được hai cách giải thích này. | Suggested text: "Đề tài bổ sung vào (5) biến chỉ báo cửa sổ chuyển chế độ (chế độ của cửa sổ chọn khác chế độ của cửa sổ đánh giá), để phân biệt rủi ro lựa chọn gắn với trạng thái căng thẳng với rủi ro gắn với việc chuyển chế độ."

5. [MAJOR] Biến kiểm soát xấu, quan hệ đồng thời và sai số đo của biến kênh | 4.3.7 (dòng 828–833, 852–856) | Độ phi thanh khoản, tương quan đuôi và biến động thực hiện được đo trên cùng cửa sổ với R_t, nên vừa là kết quả của chế độ vừa có thể cùng chịu một cú sốc với R_t (quan hệ đồng thời hoặc nhân quả ngược). Tương quan đuôi ước lượng trên cửa sổ 6 tháng chỉ có rất ít quan sát ở đuôi, nên sai số đo lớn và hệ số bị kéo về 0. Đề cương mới chỉ bàn về đa cộng tuyến (hệ số phóng đại phương sai). | Suggested text: "Các biến kênh được đo trên cùng cửa sổ với kết quả và có thể cùng phản ứng với một cú sốc; vì vậy hệ số γ không có nghĩa nhân quả. Đề tài báo cáo thêm phiên bản dùng biến kênh của cửa sổ trước (t−1), và báo cáo sai số chuẩn hoặc khoảng tin cậy bootstrap của bản thân tương quan đuôi để đánh giá mức sai số đo."

6. [MAJOR] Tính không đồng nhất giữa các giai đoạn căng thẳng và khả năng cao không có kết luận | 4.3.6 (dòng 792–797), 4.3.10 (dòng 905–910), đoạn "Nếu dữ liệu ủng hộ các giả thuyết" (dòng 970) | Mức hối tiếc chỉ tính được từ khoảng năm thứ năm, và khủng hoảng toàn cầu chủ yếu dùng để ước lượng chế độ. Vì vậy phần mẫu tính được hối tiếc nhiều khả năng chỉ chứa 2–4 giai đoạn căng thẳng có nguyên nhân rất khác nhau (COVID-19, trái phiếu doanh nghiệp 2022…). Kết quả "chế độ căng thẳng" có thể phản ánh đặc thù của một giai đoạn. Với ngưỡng "dưới 10 cửa sổ căng thẳng thì không kết luận", kịch bản cơ sở có thể là không kết luận, nhưng phần đóng góp dự kiến không nói ra điều này. | Suggested text: "Đề tài luôn, chứ không chỉ khi kết quả không kết luận, báo cáo kích thước hiệu ứng theo từng giai đoạn căng thẳng và kết quả khi loại lần lượt từng giai đoạn. Với khoảng 28 cửa sổ, đề tài dự kiến số cửa sổ căng thẳng có thể dưới ngưỡng 10; khi đó đóng góp chính là thước đo, quy trình đăng ký trước và ước lượng khoảng của chênh lệch, không phải một kết luận ủng hộ hay bác bỏ H1."

7. [MAJOR] Hàm ý thực tiễn: quy trình giám sát dùng chính những thước đo mà đề cương nói không đo rủi ro, và phát hiện chế độ bị trễ | 4.4, dòng 974–977 | "đo độ phân tán và tập tin cậy mô hình định kỳ, và kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng" mâu thuẫn với dòng 294–295 ("Độ phân tán … và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro"). Ngoài ra, xác suất lọc thường xác nhận chế độ căng thẳng muộn, nên việc "kích hoạt khi thị trường ở chế độ căng thẳng" có thể đến sau tổn thất. | Suggested text: "Thủ tục dùng độ phân tán và tập tin cậy mô hình như chỉ báo cảnh báo về bất định, không như thước đo rủi ro. Bước kích hoạt dựa trên xác suất lọc thời gian thực, và luận án báo cáo độ trễ nhận diện cùng lợi ích sau khi tính độ trễ đó."

8. [MAJOR] Tuyên bố ưu tiên chưa kiểm chứng (phạm vi toàn cầu, không được rào đón) | 4.2, cuối các nhóm (2), (3), (4) và đoạn sau Bảng 1 | Các câu: "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục" (dòng 409–410); "chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường" (dòng 429–430); "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không" (dòng 447–448); "chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường" (dòng 519–520). Các câu này mang phạm vi *toàn cầu*, trong khi quy trình tìm kiếm được mô tả ở dòng 520–529 chỉ đỡ cho tuyên bố về *Việt Nam*, và thí sinh tự thừa nhận "mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn". Đây đều là tuyên bố ưu tiên chưa kiểm chứng. Tác giả phải xác nhận trước khi nộp. | Suggested text: mở đầu mỗi câu bằng "Trong phạm vi tìm kiếm đã mô tả, thí sinh chưa tìm thấy công trình nào…", hoặc giới hạn rõ "trên thị trường Việt Nam". Riêng câu ở dòng 447–448 nên được kiểm tra lại với tài liệu về hiệu quả danh mục trong thị trường tăng/giảm và trong khủng hoảng.

### Minor Language Issues

1. [MINOR] [4.1, dòng 301] | "Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách." | Đây là khẳng định nhân quả không có dẫn chứng. Các nguồn theo sau (Reinhart–Rogoff; Laeven–Valencia về khủng hoảng ngân hàng) chỉ cho thấy khủng hoảng thường xảy ra, không cho thấy việc chọn mô hình quan trọng hơn trong khủng hoảng. | Fix: "Nếu thứ hạng của các mô hình thay đổi trong khủng hoảng, câu hỏi chọn mô hình càng quan trọng; khủng hoảng tài chính lại lặp lại thường xuyên (…)."

2. [MINOR] [4.1, dòng 307–308] | "Dao và cộng sự (2021) cho thấy số ca mắc COVID-19 hằng ngày tác động tiêu cực đến lợi suất cổ phiếu." | Đây là cách mô tả tài liệu bằng ngôn ngữ nhân quả cho một nghiên cứu hồi quy chuỗi thời gian. | Fix: "…cho thấy số ca mắc COVID-19 hằng ngày có liên hệ âm với lợi suất cổ phiếu."

3. [MINOR] [4.1, dòng 311–312] | "Vu và cộng sự (2024) cho thấy các đợt sụt giảm giá cổ phiếu giai đoạn 2007--2022 lan truyền giữa các ngành." | "Lan truyền" là một tuyên bố về sự lây nhiễm, trong khi chính đề cương (dòng 444–447, Forbes–Rigobon) lưu ý rằng bằng chứng lây nhiễm thường biến mất sau khi hiệu chỉnh theo biến động. | Fix: "…ghi nhận các đợt sụt giảm giá xảy ra đồng thời hoặc nối tiếp giữa các ngành."

4. [MINOR] [4.3.6, dòng 781–784] | "Để loại tác động cơ học này, phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap" | Chia cho sai số chuẩn chỉ loại được phần do thang đo. Giá trị kỳ vọng của max của các đại lượng có nhiễu còn phụ thuộc vào tương quan giữa các mô hình, mà tương quan này đổi theo chế độ. | Fix: "Để giảm tác động cơ học này…", và nói rõ phân phối rỗng ở 4.3.7 mới là công cụ chính để xử lý phần còn lại.

5. [MINOR] [4.3.7, dòng 835] | "Để tách rủi ro lựa chọn mô hình khỏi nhiễu ước lượng và biến động" | "Tách" là quá mạnh, vì phân phối rỗng chỉ loại bỏ chênh lệch trung bình theo chế độ dưới các giả định của bootstrap khối. | Fix: "Để đối chiếu β với mức kỳ vọng khi các mô hình ngang chất lượng…"

6. [MINOR] [4.3.6, dòng 794–795; 4.3.10, dòng 906–907] | "khoảng 28 cửa sổ đánh giá độc lập"; "số cửa sổ độc lập ở chế độ căng thẳng" | Cửa sổ không chồng lấn không có nghĩa là độc lập. Chế độ có tính bền, và cửa sổ chọn 36 tháng của các cửa sổ liền kề chồng lên nhau, nên các cửa sổ căng thẳng tập trung thành cụm. | Fix: dùng "không chồng lấn", và báo cáo số giai đoạn căng thẳng *riêng biệt* làm đơn vị đếm hiệu dụng.

7. [MINOR] [4.3.4, dòng 663] | "cách làm này loại thiên lệch nhìn trước" | Cửa sổ mở rộng loại được thiên lệch nhìn trước trong tham số, nhưng lựa chọn họ mô hình và định nghĩa chế độ được đưa ra sau khi thí sinh đã thấy dữ liệu 2019–2025 (dòng 728–730), và định nghĩa thay thế "theo ngưỡng sụt giảm" có thể dùng thông tin hậu nghiệm. | Fix: "giảm thiên lệch nhìn trước trong ước lượng tham số".

8. [MINOR] [4.3.1, dòng 540–541] | "giải thích vì sao các mô hình cho trọng số khác nhau ngay cả khi dùng cùng dữ liệu" | Khác biệt trọng số chủ yếu đến từ mục tiêu, cấu trúc và tiên nghiệm khác nhau của các mô hình. Sai số ước lượng chỉ là một phần nguyên nhân. | Fix: "giải thích một phần vì sao…"

9. [MINOR] [Bảng 2 H2 và 4.3.7, dòng 857] | "hệ số của tương quan đuôi âm" | Cụm này đọc được theo hai nghĩa: "hệ số âm của tương quan đuôi" hoặc "hệ số của tương quan ở đuôi âm". Hai cách đọc dẫn đến dấu dự đoán khác nhau. | Fix: "hệ số của tương quan ở đuôi âm mang dấu âm".

10. [MINOR] [4.1, dòng 324–326] | "lần đầu thiết lập khuôn khổ quản lý rủi ro mô hình cho các ngân hàng" | Đây là tuyên bố "lần đầu" về văn bản quy phạm và chưa được kiểm chứng. Nội dung và ngày tháng của SR 26-2 (dòng 317–318) cũng cần đối chiếu với văn bản gốc. | Fix: tác giả xác nhận với văn bản gốc, hoặc viết "thiết lập khuôn khổ…" mà bỏ "lần đầu".

11. [MINOR] [4.4, dòng 971–972] | "Về lý thuyết, đề tài đưa ra khung khái niệm và thước đo rủi ro lựa chọn mô hình" | Mức hối tiếc là một khái niệm chuẩn trong lý thuyết quyết định. Gọi đây là đóng góp lý thuyết là cách nói quá. | Fix: "Về khái niệm và đo lường, đề tài đề xuất cách vận dụng mức hối tiếc để đo rủi ro lựa chọn mô hình theo chế độ cho quyết định phân bổ danh mục."

12. [MINOR] [4.2 (3), dòng 418–419] | "kết hợp dự báo bù được phần chất lượng dự báo mất đi do mô hình bất ổn định" | Cơ chế được gán cho Rapach và cộng sự (2010) dưới dạng khẳng định. | Fix: "…cho thấy kết hợp dự báo cải thiện hiệu quả ngoài mẫu, điều họ lý giải bằng việc giảm tác động của bất ổn định mô hình."

Không phát hiện trường hợp rào đón quá mức nào đáng kể. Phần rào đón về tuyên bố ưu tiên cho Việt Nam (dòng 520–529) và về rủi ro do đã xem dữ liệu 2019–2025 (dòng 728–738) là phù hợp, nên giữ nguyên.

---

## 4. Internal Consistency & Cross-Reference Verification

## Agent 2: Internal Consistency & Cross-Reference Verification

Phạm vi: chỉ rà `main.tex` (phần chữ đang có hiệu lực) và `hinh-van-ban.txt`, không sửa tệp nào. Đề cương chưa có kết quả, nên tôi đối chiếu câu hỏi nghiên cứu, mục tiêu, H1–H4 (Bảng 2), M1–M7 (Bảng 3), phương trình (1)–(5), Bảng 1–7, Hình 1–2 (qua tệp văn bản), mục 4.3–4.5 và 7.4.

Lỗi do pandoc chuyển đổi, chỉ nêu một lần và không tính là lỗi tác giả: chú thích bảng/hình bị trống số ("Bảng .", "Hình ."), nhãn `\label{ux...}`, số trang trong mục lục, và hình gốc là hình vẽ Word nên không hiển thị.

Đối chiếu tài liệu tham khảo: mọi cặp tác giả–năm trích trong bài đều có mục tương ứng ở mục 11, và mọi mục ở mục 11 đều được trích. Không tìm thấy trích dẫn nào thiếu tài liệu tham khảo. Các con số kiểm tra được đều khớp nhau:
- 9 tín chỉ (mục 5 ↔ 7.1 ↔ Bảng 5);
- 9 bản thảo, trong đó 3 bản "liên quan trực tiếp" (văn bản ↔ cột "Có" của Bảng 7: bản số 1, 5, 6);
- sáu chương (văn bản ↔ Bảng 4);
- bốn khoảng trống (Bảng 1 ↔ 4.3.2);
- |M| = 7 (văn bản ↔ Bảng 3);
- 104 tuần / 6 tháng / 36 tháng (4.3.6 ↔ Hình 2);
- 468 tuần cho giai đoạn 2011–2019 (Nguyen và cộng sự, 2020);
- 299 công ty, 2005–2015 (Vo và Phan, 2017).

### Critical Inconsistencies

1. [CRITICAL] Trang bìa ↔ Mục 10 | Trang bìa chỉ ghi một người hướng dẫn: "Người hướng dẫn khoa học (dự kiến): **- PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân**". Mục 10 lại đề xuất hai người, trong đó người hướng dẫn **chính** là "GS.TS. Nguyễn Đức Khương", còn PGS.TS. Hà Hồng Hạnh là "Người hướng dẫn thứ hai (dự kiến)". Hai chỗ mâu thuẫn trực tiếp về người hướng dẫn chính. Cần ghi đủ cả hai người trên trang bìa, theo đúng thứ tự ở mục 10.

2. [CRITICAL] Mục 4.1 (định nghĩa) ↔ Bảng 2, 4.3.6, 4.3.7, Hình 1 | Mục 4.1 khẳng định: "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, **không đo rủi ro**." Thế nhưng ở các chỗ sau, chính hai đại lượng này lại được coi là thước đo rủi ro:
   - Bảng 2 xếp chúng vào cột "Thước đo chính" của H1 ("Kết quả phụ: độ phân tán mô hình, kích thước tập tin cậy mô hình").
   - Mục 4.3.6 có tiêu đề "Thước đo rủi ro lựa chọn mô hình" và gọi tập tin cậy là "Thước đo thứ ba".
   - Mục 4.3.7 viết "hồi quy các thước đo rủi ro mô hình… Với Y_t là D_t hoặc R_t", và đặt điều kiện H1 được ủng hộ là "β của D_t cùng dấu".
   - Hình 1 đặt "Độ phân tán D_t | Tập tin cậy mô hình" trong ô "Rủi ro lựa chọn mô hình".

   Như vậy, khái niệm then chốt mà tác giả cam kết "giữ nguyên nghĩa… trong toàn văn bản" lại bị dùng trái với định nghĩa của chính nó.

3. [CRITICAL] Mục tiêu (iii) ↔ Câu hỏi 2, Bảng 2, 4.3.7, Hình 1 | Biến động thực hiện lúc là biến kênh, lúc là biến kiểm soát:
   - Mục tiêu (iii) xếp nó vào nhóm biến kênh: "các biến kênh… gồm **biến động**, thanh khoản, tương quan cực trị và bầy đàn".
   - Câu hỏi 2, H2, H4 và Hình 1 ("Biến động thực hiện (kiểm soát)") lại coi nó là biến kiểm soát: "Sau khi kiểm soát biến động thực hiện, các biến kênh (thanh khoản, tương quan cực trị và… bầy đàn)".
   - Mục 4.3.7 vừa định nghĩa X_t là "véc-tơ biến kênh", vừa nói "Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát".

   Hệ quả là phép phân rã "β₀ − β₁" (β khi không có và khi có X_t), được giới thiệu là "phần chênh lệch giữa hai chế độ do các biến kênh giải thích", thực ra tính cả phần do biến động giải thích. Điều này mâu thuẫn với câu hỏi 2 ("sau khi kiểm soát biến động… giải thích được bao nhiêu phần chênh lệch").

4. [MAJOR] Bảng 2 (H3) ↔ 4.3.8 ↔ Hình 1 | Tiêu chí và phạm vi của H3 khác nhau giữa ba chỗ:
   - Về độ sụt giảm tối đa: Bảng 2 yêu cầu "mức hối tiếc và độ sụt giảm tối đa **thấp hơn**", còn tiêu chí ủng hộ ở 4.3.8 chỉ yêu cầu "độ sụt giảm tối đa **không cao hơn**".
   - Về số cơ chế: Bảng 2 chỉ nêu hai cơ chế ("kết hợp mô hình và danh mục vững chắc"), trong khi 4.3.8 đánh giá ba cơ chế (thêm cơ chế (iii) "quy tắc chuyển chế độ") và Hình 1 đặt "Quy tắc theo chế độ" trong ô cơ chế giảm thiểu gắn với H3.
   - Về thước đo: Bảng 2 liệt kê thêm "giá trị thiệt hại kỳ vọng mức 95%; vòng quay", nhưng tiêu chí ủng hộ ở 4.3.8 không dùng hai thước đo này.

5. [MAJOR] H4 (Bảng 2) ↔ 4.2(5), 4.4 | Hướng tác động của H4 ngược với ý nghĩa bầy đàn mà đề tài nêu:
   - Mục 4.4 gọi độ phân tán chéo là "một thước đo bầy đàn ở cấp thị trường". Theo Christie và Huang (1995), được trích ở 4.2, bầy đàn biểu hiện bằng độ phân tán chéo **thấp**.
   - H4 lại phát biểu "độ phân tán chéo của lợi suất **cao** đi cùng rủi ro lựa chọn mô hình cao", tức là ít bầy đàn đi cùng rủi ro cao.
   - Điều đó trái với lập luận ở 4.2(5): bầy đàn là "một kênh hành vi có thể làm các mô hình cho kết quả khác nhau".

   Thêm vào đó, cột thước đo của H4 có hai đại lượng ("Độ phân tán chéo của lợi suất; thước đo bầy đàn"), nhưng 4.3.7 chỉ đưa độ phân tán chéo vào X_t.

6. [MAJOR] Hình 1 / 4.3.2 ↔ Bảng 2 (H2) ↔ 4.2(4) | Văn bản nói các biến kênh "giải thích một phần chênh lệch giữa hai chế độ (H₂ và H₄)". Tuy vậy:
   - H2 dự đoán hệ số của tương quan đuôi là âm.
   - Chính 4.2(4) dẫn Ang và Bekaert (2002): "tương quan và biến động cùng tăng ở chế độ xấu".

   Ghép hai điều này lại thì kênh tương quan sẽ **thu hẹp** chênh lệch giữa hai chế độ chứ không giải thích nó. Phép đo β₀ − β₁ gộp hai kênh có dấu ngược nhau, nên con số "bao nhiêu phần" mà câu hỏi 2 hứa trả lời không diễn giải được.

7. [MAJOR] 4.3.10 (Holm) ↔ 4.3.7 ↔ Bảng 2 | Có hai điểm không thống nhất về kiểm định bội và mức ý nghĩa:
   - "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho **bốn** giả thuyết". Trong khi đó, H4 được ghi là "(thăm dò)" và "Đề tài chỉ báo cáo H₄ như kết quả thăm dò", nên đưa H4 vào họ kiểm định khẳng định là mâu thuẫn.
   - Ngưỡng của H1 là "phân vị 95%" của phân phối rỗng, tức mức 5% một phía và chưa hiệu chỉnh. Ngưỡng này không khớp với ngưỡng Holm mức 10% đã đăng ký.

8. [MAJOR] 4.3.4 (số chế độ) ↔ 4.1, Hình 1, phương trình (5) | Văn bản để mở khả năng ba chế độ: "Số chế độ (hai hoặc ba) do tiêu chí thông tin quyết định". Nhưng toàn bộ khung phân tích là hai chế độ: Hình 1 chỉ có "Chế độ bình thường | Chế độ căng thẳng", và β "đo chênh lệch… giữa chế độ căng thẳng và chế độ bình thường". Nếu có ba chế độ thì không rõ "chế độ bình thường" là chế độ nào.

9. [MAJOR] Phương trình (5): định nghĩa S_t ↔ 4.3.4 ↔ 4.3.10 | Có hai vấn đề:
   - S_t là "tỷ lệ số ngày trong cửa sổ có xác suất lọc… vượt ngưỡng", tức cần xác suất lọc theo **ngày**. Nhưng 4.3.4 chỉ mô tả việc tính "Tại mỗi ngày tái cân bằng" (hằng tháng): "ước lượng lại tham số… và từ đó tính xác suất lọc tại ngày t".
   - S_t là biến liên tục, nhưng quy tắc "Khi số cửa sổ độc lập **ở chế độ căng thẳng** dưới 10, đề tài gọi kết quả là không kết luận" cần cách phân loại nhị phân một cửa sổ là "ở chế độ căng thẳng", và cách phân loại này chưa được định nghĩa.

10. [MAJOR] 4.3.6 (≈28 cửa sổ) + 4.3.5 + 4.3.10 ↔ Bảng 4 / 7.3 | Nhiều chi tiết do chính đề cương nêu khiến quy tắc "không kết luận" gần như chắc chắn được kích hoạt với H1:
   - chỉ có "khoảng 28 cửa sổ đánh giá độc lập";
   - khủng hoảng tài chính toàn cầu "chủ yếu phục vụ ước lượng chế độ", tức nằm ngoài phần mẫu tính được mức hối tiếc;
   - dữ liệu 2019–2025 chỉ "gồm hai giai đoạn căng thẳng";
   - ngưỡng tối thiểu là 10 cửa sổ căng thẳng.

    Trong khi đó, Bảng 4 (Chương 4: "Kiểm định H₁") và 7.3 (bài báo 1 "kiểm định H₁") được viết như thể sẽ có kết quả kiểm định. Đề cương nên nêu rõ tình huống "không kết luận" sẽ được trình bày thế nào trong cấu trúc chương và kế hoạch bài báo.

11. [MAJOR] 4.3.2 / Hình 1 ↔ 4.3.7 | Ngôn ngữ nhân quả và điều tiết không khớp với thiết kế liên hệ cộng tính:
    - "chế độ thị trường **tác động lên** rủi ro lựa chọn mô hình"; "Các biến kênh **tác động lên chính quan hệ đó**", tức là vai trò điều tiết.
    - Phương trình (5) là mô hình cộng tính không có số hạng tương tác, và phép đo β₀ − β₁ mang tính trung gian.
    - Mục 4.3.7 lại cam kết "gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả".

    Tương tự, câu "Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục (H₃)" không khớp với H3, vốn chỉ so sánh cơ chế giảm thiểu với chọn một mô hình.

### Terminology Drift

1. [MAJOR] "Rủi ro lựa chọn mô hình" / "rủi ro mô hình" / "bất định mô hình" | Mục 4.1 phân biệt ba khái niệm này, nhưng sau đó chúng bị dùng lẫn:
   - 4.3.7 viết "hồi quy các **thước đo rủi ro mô hình**" khi đang nói về R_t và D_t;
   - phần đóng góp ở 4.4 viết "đề tài **đo mức bất định** khi chọn mô hình theo từng chế độ", trong khi đối tượng đo là rủi ro lựa chọn.

   Đề xuất: dùng nhất quán "rủi ro lựa chọn mô hình" cho R_t, và gọi D_t cùng kích thước tập tin cậy là "chỉ báo bất định mô hình".

2. [MAJOR] "Tương quan cực trị" / "tương quan đuôi" / "tương quan hiệu chỉnh theo biến động" | Ba cách gọi xuất hiện ở các chỗ khác nhau:
   - câu hỏi 2, mục tiêu (iii), 4.3.1 và Bảng 4 (mục 5.2) dùng "tương quan cực trị";
   - H2 và Hình 1 dùng "tương quan đuôi";
   - 4.3.7 đưa vào X_t cả "tương quan đuôi **và** tương quan hiệu chỉnh theo biến động", nhưng H2 chỉ có một hệ số tương quan.

   Đề xuất: chọn một tên gọi, định nghĩa biến cụ thể, và nói rõ biến tương quan thứ hai đóng vai trò gì đối với H2.

3. [MAJOR] "Biến kênh" | Thuật ngữ này lúc bao gồm biến động thực hiện (mục tiêu (iii), định nghĩa X_t ở 4.3.7), lúc không (câu hỏi 2, Hình 1). Đề xuất: tách ký hiệu thành X_t (biến kênh) và V_t (biến động thực hiện, biến kiểm soát).

4. [MINOR] "Độ phân tán" | Cùng một từ chỉ hai đại lượng khác nhau: D_t, tức "độ phân tán mô hình" ở phương trình (3), và "độ phân tán chéo của lợi suất" ở H4. Đề xuất: luôn gọi đầy đủ "độ phân tán mô hình" và "độ phân tán chéo lợi suất", hoặc dùng ký hiệu riêng cho đại lượng thứ hai.

5. [MINOR] Ký hiệu *M* | |M| = 7 ở 4.3.6, nhưng tập này bị đổi ở hai chỗ khác mà không có ký hiệu mới:
   - tập mô hình tĩnh ở 4.3.7 (M₁, M₂, M₃, M₄, M₆);
   - ở 4.3.8, "đề tài loại cơ chế (ii) và (iii) khỏi *M*", tức bỏ M₆ và M₇.

   Đề xuất: đặt ký hiệu riêng, ví dụ M^tĩnh và M^H3.

6. [MINOR] "Bầy đàn" vs "phân tán chéo" | Bảng 4 (mục 5.3) và Hình 1 ("Phân tán chéo (thăm dò)") dùng hai tên cho cùng một kênh. Phần này gắn với vấn đề hướng tác động nêu ở mục Critical 5.

7. [MINOR] Tên tác giả trong cặp trích dẫn 2026a/2026b viết không thống nhất:
   - Bảng 6 hàng 1 và tài liệu tiếng Việt: "Nguyễn và Nguyễn, 2026b" / "Nguyễn Thanh Bình, Nguyễn Văn Trung (2026b)";
   - các chỗ khác: "Nguyen và Nguyen (2026a)" / "Nguyen, T. B., Nguyen, V. T. (2026a)".

   Hậu tố a/b chỉ có nghĩa khi tên tác giả viết giống hệt nhau, nên cần thống nhất một cách viết.

### Minor Inconsistencies

1. [MINOR] 4.3.6, "mức hối tiếc chỉ tính được từ khoảng **năm thứ năm** của mẫu" ↔ chính các số liệu đi kèm | Cửa sổ ước lượng 104 tuần (2 năm) cộng 36 tháng kết quả ngoài mẫu (3 năm) bằng 5 năm đã trôi qua, nên mức hối tiếc chỉ bắt đầu từ năm thứ **sáu** (khoảng 2012 nếu mẫu bắt đầu năm 2007). Con số "khoảng 28 cửa sổ" khớp với mốc 2012 đến khoảng giữa năm 2026, không khớp với mốc "năm thứ năm" (sẽ cho khoảng 30–32 cửa sổ).

2. [MINOR] Bảng 2 (H1, "Kết quả phụ: … kích thước tập tin cậy mô hình") ↔ 4.3.6 ↔ 4.3.7 | Mục 4.3.6 nói chỉ "báo cáo kích thước tập như một thước đo mô tả", và tiêu chí ủng hộ H1 ở 4.3.7 không dùng đại lượng này. Vì vậy không nên xếp nó vào cột thước đo của H1.

3. [MINOR] 4.3.7 (VIF > 5 thì "báo cáo hai phương trình tách riêng và **không diễn giải riêng từng hệ số**") ↔ tiêu chí H2 | H2 được ủng hộ dựa trên dấu và khoảng tin cậy của **từng** hệ số, nên khi VIF vượt ngưỡng thì không rõ H2 được đánh giá thế nào.

4. [MINOR] 4.3.6 ↔ 4.3.7 | Tỷ số Sharpe được nói chỉ là "thước đo phụ, ở các cửa sổ có lợi suất vượt trội trung bình dương", tức loại phần lớn các cửa sổ căng thẳng. Nhưng thiên lệch chọn lọc lại được hiệu chỉnh "bằng tỷ số Sharpe hiệu chỉnh", trong khi việc chọn mô hình dựa trên lợi suất tương đương chắc chắn.

5. [MINOR] 4.3.8 ("loại cơ chế (ii) và (iii) khỏi *M*, nên mức hối tiếc của hai cơ chế này có thể âm") ↔ cơ chế (i) | Danh mục kết hợp ở cơ chế (i) cũng không thuộc *M*, nên mức hối tiếc của nó cũng có thể âm, nhưng văn bản không nói.

6. [MINOR] Câu hỏi 3 ("Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?") ↔ H3 ("**Ở chế độ căng thẳng**, sau chi phí giao dịch…") | Câu hỏi không giới hạn theo chế độ, còn giả thuyết thì có.

7. [MINOR] 4.3.4/4.3.6 ↔ 4.3.3 | Ngưỡng của M3 ("tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5") không bao giờ có hiệu lực ở cấu hình cơ sở, vì 30/104 ≈ 0,29. Ngưỡng này chỉ có tác dụng trong kiểm tra độ bền "dùng dữ liệu tháng", nhưng ở đó tỷ lệ được định nghĩa theo "quan sát tuần" nên không áp dụng trực tiếp được.

8. [MINOR] Bảng 1 (4 khoảng trống, gồm "(4)… bầy đàn") ↔ "Đóng góp dự kiến" ở 4.4 ("khác chúng ở bốn điểm") | Bốn điểm đóng góp không trùng với bốn khoảng trống: đóng góp có bài báo của chính thí sinh nhưng không có khoảng trống về bầy đàn.

9. [MINOR] Mục 5 ("đề tài nằm ở giao điểm của tài chính định lượng, quản lý và **tài chính hành vi**") ↔ 4.4 ("giao thoa với kinh tế hành vi ở **một phép thử giới hạn**") ↔ H4 "(thăm dò)" | Mục 5 nói thành phần hành vi mạnh hơn mức mà phần thiết kế thể hiện.

10. [MINOR] Mục 4.5 ("Ngoài phần mở đầu, kết luận…, luận án dự kiến gồm sáu chương") ↔ Bảng 4 | Chương 1 "Giới thiệu nghiên cứu" trùng chức năng với "phần mở đầu".

11. [MINOR] Viết hoa không thống nhất: trang bìa "Đại học Kinh tế Quốc **D**ân" ↔ mục 8.2 và mục 10 "Kinh tế Quốc **d**ân".

12. [MINOR] Cách diễn giải tài liệu được trích:
    - Kerkhof và cộng sự (2010) được tóm tắt là chỉ tách thành "rủi ro ước lượng và rủi ro đặc tả sai". Bài gốc có thêm thành phần thứ ba (rủi ro nhận dạng), nên cách tóm tắt chưa đầy đủ.
    - Khẳng định Thông tư 83/2025/TT-NHNN "**lần đầu** thiết lập khuôn khổ quản lý rủi ro mô hình" là một nhận định mạnh. Tài liệu tham khảo chỉ cho thấy đây là thông tư về "hệ thống kiểm soát nội bộ", nên chi tiết này cần được đối chiếu.

13. [MINOR] Mục 5 dẫn "Thông báo tuyển sinh năm 2026" và "Phụ lục 1 của Thông báo" làm căn cứ, nhưng văn bản này không có trong danh mục tài liệu tham khảo.

---

## 5. Mathematics, Equations & Notation

## Agent 4: Mathematics, Equations & Notation

Tôi đã đọc toàn bộ phần chữ đang hiệu lực của main.tex, tập trung vào mục 4.3.4–4.3.8 (phương trình (1)–(5)) và các định nghĩa bằng lời ở phần mở đầu (dòng ~285–300) cùng Bảng 2–3. Tôi không xét việc số phương trình nằm ở dạng chữ "(1)"… và việc dùng `\(...\)` thay cho môi trường display như là lỗi, vì đây là hệ quả của chuyển đổi pandoc.

### Mathematical Errors

1. [MAJOR] Phương trình (5), dòng 826 | Chữ trong bài ghi "\(\beta\) đo chênh lệch của \(Y_{t}\) giữa chế độ căng thẳng và chế độ bình thường", nhưng \(S_{t}\) là "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng", tức một biến liên tục trong [0,1] chứ không phải biến giả. Vì vậy \(\beta\) là chênh lệch dự báo tuyến tính giữa một cửa sổ có toàn bộ số ngày ở chế độ căng thẳng (S=1) và một cửa sổ có toàn bộ số ngày ở chế độ bình thường (S=0). Với 6 tháng một cửa sổ, hai điểm này có thể ít hoặc không hề xuất hiện trong mẫu, nên đây là một phép ngoại suy. Ngoài ra, \(\beta\) còn được ước lượng *có điều kiện theo* \(X_{t}\) (trong đó luôn có biến động thực hiện). | Sửa thành: "\(\beta\) đo mức thay đổi của \(Y_{t}\) khi tỷ lệ ngày căng thẳng trong cửa sổ tăng từ 0 lên 1, với \(X_{t}\) giữ cố định". Một cách khác là định nghĩa \(S_{t}\) thành biến giả (chẳng hạn \(S_{t}=1\) khi tỷ lệ này vượt 0,5) nếu muốn giữ cách diễn giải "chênh lệch giữa hai chế độ".

2. [MAJOR] Phân rã \(\beta_{0}-\beta_{1}\), dòng 832–833 và 850–852 | Dòng 832–833 ghi "Biến động thực hiện luôn có mặt trong \(X_{t}\) với vai trò biến kiểm soát", trong khi \(\beta_{0}\) là hệ số "khi không có … \(X_{t}\)". Như vậy \(\beta_{0}\) không kiểm soát biến động thực hiện, và \(\beta_{0}-\beta_{1}\) gộp chung phần do biến động giải thích với phần do các biến kênh giải thích. Điều này mâu thuẫn với Câu hỏi 2 và H\textsubscript{2}, vốn đặt câu hỏi "sau khi kiểm soát biến động thực hiện". | Tách \(X_{t}=(RV_{t}, Z_{t}')'\) và định nghĩa \(\beta_{0}\) là hệ số khi chỉ có \(RV_{t}\), \(\beta_{1}\) là hệ số khi có cả \(RV_{t}\) và \(Z_{t}\). Phần do kênh giải thích khi đó là \(\beta_{0}-\beta_{1}\). Nếu muốn chia phần giải thích cho từng kênh thì nên dùng phân rã Gelbach (2016).

3. [MAJOR] Phương trình (4) và mục 4.3.8, dòng 874–875 | Bài viết suy ra \(R_{t}\ge 0\) vì "mô hình chọn trước thuộc \emph{M}". Sau đó, khi kiểm định H\textsubscript{3}, "đề tài loại cơ chế (ii) và (iii) khỏi \emph{M}, nên mức hối tiếc của hai cơ chế này có thể âm". Có ba vấn đề: (a) Cơ chế (ii) (danh mục vững chắc theo Garlappi và cộng sự, 2007) và cơ chế (iii) (theo Kritzman và cộng sự, 2012) chính là M\textsubscript{6} và M\textsubscript{7} trong Bảng 3. Loại chúng ra làm \(|M|\) giảm từ 7 xuống 5, nên \(D_{t}\), \(U_{o,t}\) và mức chuẩn hóa thay đổi theo. Bài không nói khi đó các thước đo này được tính lại hay không. (b) Cơ chế (i), kết hợp mô hình, cũng không phải là phần tử của \emph{M}, nên mức hối tiếc của nó cũng có thể âm, nhưng câu văn chỉ nhắc đến (ii) và (iii). (c) Bài chưa định nghĩa hình thức mức hối tiếc của một cơ chế, tức \(U_{o,t}-U_{k,t}\) với \(k\notin M\). | Định nghĩa rõ \(R^{(k)}_{t}=\max_{m\in M}U_{m,t}-U_{k,t}\) cho mọi cơ chế \(k\). Nêu rõ \emph{M} dùng trong H\textsubscript{3} là tập nào, và nói rõ rằng \(R^{(k)}_{t}\) có thể âm với cả ba cơ chế.

4. [MAJOR] Chuẩn hóa \(D_{t}\) và \(R_{t}\), dòng 782–784 | Câu "chia \(D_{t}\) và \(R_{t}\) cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình" không xác định được một đại lượng duy nhất: với 7 mô hình có 21 cặp chênh lệch. Bài cũng không cho ký hiệu riêng cho đại lượng đã chuẩn hóa, nên không rõ \(Y_{t}\) trong (5) là \(D_{t}\) và \(R_{t}\) thô hay đã chuẩn hóa. | Định nghĩa một ký hiệu, ví dụ \(\tilde{R}_{t}=R_{t}/\widehat{se}_{t}\) với \(\widehat{se}_{t}\) được nêu rõ (trung bình các cặp, hoặc sai số chuẩn của \(U_{c,t}-U_{o,t}\)). Ghi rõ "Với \(Y_{t}\) là \(\tilde{D}_{t}\) hoặc \(\tilde{R}_{t}\)".

5. [MAJOR] Phương trình (1), dòng 754–760 | Tần suất của \(\mu_{m,t}\) và \(\sigma^{2}_{m,t}\) (ngày, tuần hay tháng) và việc có quy đổi về năm hay không đều chưa được nêu. Với cửa sổ đánh giá 6 tháng và tái cân bằng hằng tháng, nếu dùng lợi suất tháng thì phương sai chỉ tính trên 6 quan sát. Bài cũng không nói \(\mu\) là lợi suất thô hay lợi suất vượt trội. Câu "mức lợi suất phi rủi ro mà nhà đầu tư … coi là ngang giá" chỉ đúng khi \(\mu\) là lợi suất thô (không trừ lãi suất phi rủi ro). Thêm nữa, công thức \(\mu-\frac{\rho}{2}\sigma^{2}\) chỉ đúng chính xác với hữu dụng bậc hai hoặc với CARA kết hợp phân phối chuẩn; với trường hợp khác nó là xấp xỉ. | Ghi rõ: "\(\mu_{m,t}\), \(\sigma^{2}_{m,t}\) tính từ lợi suất [ngày] sau chi phí, quy đổi năm", và thêm "(xấp xỉ bậc hai của lợi suất tương đương chắc chắn)".

6. [MINOR] Đếm số cửa sổ, dòng 792–795 | Ước lượng cần 104 tuần (2 năm) và việc chọn mô hình cần 36 tháng (3 năm), tổng cộng 5 năm. Mức hối tiếc vì thế tính được *từ đầu năm thứ sáu*, không phải "từ khoảng năm thứ năm". Con số "khoảng 28 cửa sổ" thì khớp (2012–2026 xấp xỉ 14–14,5 năm, tức 28–29 cửa sổ 6 tháng). | Sửa thành "sau năm thứ năm" hoặc "từ năm thứ sáu".

7. [MINOR] Điều kiện cho M\textsubscript{3}, dòng 723–726 | Với rổ cố định N = 30 và cửa sổ T = 104 tuần, tỷ lệ là 30/104 ≈ 0,29, luôn nhỏ hơn 0,5, nên ở cấu hình cơ sở điều kiện này không bao giờ xảy ra. Ngoài ra, khi 0,5 < N/T < 1 thì ma trận hiệp phương sai mẫu vẫn khả nghịch. Nghịch đảo giả Moore-Penrose chỉ thực sự cần khi N ≥ T, nên nó không xử lý vấn đề "ước lượng kém" ở ngưỡng 0,5. | Nói rõ ngưỡng này chỉ có tác dụng trong kiểm tra độ bền dùng dữ liệu tháng (24 tháng cho 30 mã, N/T > 1). Nếu ý đồ là xử lý điều kiện kém thì nên dùng ngưỡng N/T ≥ 1 cho nghịch đảo giả, hoặc dùng co rút.

8. [MINOR] Định nghĩa chế độ căng thẳng, dòng 665–666 | "Chế độ căng thẳng là chế độ có phương sai điều kiện cao nhất và lợi suất kỳ vọng thấp hơn chế độ bình thường." Định nghĩa này bỏ ngỏ trường hợp chế độ có phương sai cao nhất lại không có lợi suất thấp hơn. Khi có ba chế độ, "chế độ bình thường" cũng không xác định (là một chế độ hay gộp hai chế độ còn lại). | Đặt quy tắc ưu tiên (chọn theo phương sai) và nói rõ "bình thường" là phần bù của chế độ căng thẳng.

### Notation Inconsistencies

1. [MAJOR] \(t\) | Ở dòng 662, \(t\) là ngày ("xác suất lọc tại ngày \emph{t}"). Ở dòng 753–754, (1)–(5), \(t\) là cửa sổ đánh giá 6 tháng ("cửa sổ đánh giá kết thúc tại thời điểm \emph{t}"). Ngay trong định nghĩa \(S_{t}\) (dòng 824–826), hai nghĩa này chồng lên nhau, vì \(S_{t}\) tổng hợp xác suất theo ngày trong cửa sổ \(t\). | Dùng \(d\) cho ngày (\(\xi_{d}\) là xác suất lọc) và \(t\) cho cửa sổ, chẳng hạn \(S_{t}=\frac{1}{|W_t|}\sum_{d\in W_t}\mathbf{1}\{\xi_{d}>\kappa\}\).

2. [MINOR] \(M\) / M\textsubscript{k} | \emph{M} là tập mô hình (dòng 752), còn M\textsubscript{1}…M\textsubscript{7} là từng mô hình (Bảng 3). Chữ chỉ số mô hình trong các phương trình là \(m\). Cùng một chữ cái vừa chỉ tập hợp, vừa chỉ phần tử. | Dùng \(\mathcal{M}\) cho tập hợp, hoặc đổi nhãn mô hình thành \(m=1,\dots,7\).

3. [MINOR] \(c\) và \(o\) trong (4) | \(c\) là một mô hình nhưng phụ thuộc vào thời điểm chọn, vì mỗi cửa sổ chọn lại. \(o\) không phải một chỉ số mô hình cố định, mà "giá trị cao nhất trong \emph{M}". | Viết \(R_{t}=\max_{m\in M}U_{m,t}-U_{c_t,t}\), với \(c_t=\arg\max_{m}\widehat{CE}^{36}_{m,t}\).

4. [MINOR] \(\beta\), \(\beta_{0}\), \(\beta_{1}\) | \(\beta_{0}\) thường được hiểu là hệ số chặn. Ở đây hệ số chặn là \(\alpha\), còn \(\beta_{0}\) và \(\beta_{1}\) là \(\beta\) của hai đặc tả khác nhau. Ký hiệu này dễ gây nhầm. | Dùng \(\beta^{\text{(không kênh)}}\) và \(\beta^{\text{(có kênh)}}\), hoặc \(\beta^{R}\) và \(\beta^{F}\).

5. [MINOR] Cách viết \(|M|\) | Trong văn bản là \texttt{\textbackslash textbar\{\}\textbackslash emph\{M\}\textbackslash textbar\{\}} (dòng 753), còn trong phương trình là \(|M|\). | Thống nhất dùng `\(|M|=7\)`.

6. [MINOR] Vai trò của \(D_{t}\) | Dòng 293–295 ghi: "Độ phân tán giữa các mô hình … chỉ báo hiệu mức bất định, không đo rủi ro". Nhưng dòng 815–818 lại hồi quy "các thước đo rủi ro mô hình", trong đó \(Y_{t}\) có thể là \(D_{t}\), và H\textsubscript{1} yêu cầu "\(\beta\) của \(D_{t}\) cùng dấu". | Gọi \(D_{t}\) là "thước đo bất định" một cách nhất quán, kể cả trong câu mô tả hồi quy.

### Undefined Notation

1. [MAJOR] Các thành phần của \(\gamma\) | H\textsubscript{2} được phát biểu theo "hệ số của độ phi thanh khoản" và "hệ số của tương quan đuôi" (dòng 856–858), nhưng (5) chỉ có véc-tơ \(\gamma\). Bài không gán ký hiệu cho các phần tử của \(X_{t}\) (Amihud, tương quan đuôi, tương quan hiệu chỉnh, độ phân tán chéo, biến động thực hiện) hay cho các hệ số tương ứng. | Viết tường minh \(\gamma'X_{t}=\gamma_{1}ILLIQ_{t}+\gamma_{2}TC_{t}+\gamma_{3}AC_{t}+\gamma_{4}CSAD_{t}+\gamma_{5}RV_{t}\) ngay sau (5), và phát biểu H\textsubscript{2} thành \(\gamma_{1}>0,\ \gamma_{2}<0\) và H\textsubscript{4} thành \(\gamma_{4}>0\).

2. [MINOR] Ngưỡng xác suất lọc và xác suất lọc | Bài nói "ngưỡng đăng ký trước" (dòng 825–826) và "xác suất lọc" (dòng 662) nhưng không có ký hiệu cho cả hai. | Thêm \(\xi_{d}=\Pr(s_{d}=\text{căng thẳng}\mid\mathcal{F}_{d})\) và ngưỡng \(\kappa\) ở mục 4.3.4.

3. [MINOR] Đại lượng dùng để chọn \(c\) | "lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước" (dòng 770–772) là một đại lượng khác \(U_{m,t}\), vì cửa sổ là 36 tháng chứ không phải 6 tháng, nhưng không có ký hiệu. | Định nghĩa \(\widehat{CE}^{36}_{m,t}\) theo cùng công thức (1) trên 36 tháng trước \(t\).

4. [MINOR] Chuỗi tham chiếu của "\emph{t}" và "cửa sổ" trong \(S_{t}\) | Câu "tỷ lệ số ngày trong cửa sổ" không nói rõ đó là cửa sổ đánh giá 6 tháng hay cửa sổ ước lượng 104 tuần. | Ghi rõ "cửa sổ đánh giá \(t\)".

### Regression Specification Issues

1. [MAJOR] Phương trình (5) so với Bảng 2 (H\textsubscript{1}) | Bảng 2 ghi biến kết quả cho H\textsubscript{1} là "Kết quả phụ: độ phân tán mô hình, kích thước tập tin cậy mô hình" (dòng 595). Nhưng (5) chỉ cho phép "\(Y_{t}\) là \(D_{t}\) hoặc \(R_{t}\)" (dòng 818), và dòng 786–788 nói kích thước tập tin cậy chỉ là "thước đo mô tả". | Bỏ kích thước tập tin cậy khỏi cột "Thước đo chính" cho H\textsubscript{1}, hoặc thêm nó làm \(Y_{t}\) trong (5).

2. [MAJOR] Phương trình (5) so với Bảng 2 (H\textsubscript{4}) | Bảng 2 liệt kê "Độ phân tán chéo của lợi suất; thước đo bầy đàn" (dòng 610–611). Trong khi đó \(X_{t}\) (dòng 828–832) chỉ có độ phân tán chéo, không có thước đo bầy đàn riêng (chẳng hạn hệ số phi tuyến của Chang và cộng sự, 2000). | Hoặc thêm biến bầy đàn vào \(X_{t}\), hoặc xóa "thước đo bầy đàn" khỏi Bảng 2 và ghi rõ rằng CSAD chính là thước đo bầy đàn (như dòng 949–950).

3. [MAJOR] Số bậc tự do và suy diễn | Khoảng 28 quan sát (dòng 794–795) được dùng để ước lượng 7 tham số: \(\alpha\), \(\beta\) và 5 biến trong \(X_{t}\). Hai biến tương quan (tương quan đuôi và tương quan hiệu chỉnh theo biến động) gần như chắc chắn đa cộng tuyến với nhau và với \(RV_{t}\). Bài lại đồng thời dùng hai cách suy diễn: "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" (dòng 817–818) và "bootstrap khối dừng … cho các hệ số hồi quy" (dòng 812–813). Bài không nói cách nào quyết định kết luận, và cũng không nêu độ dài khối hay bandwidth HAC trên 28 cửa sổ không chồng lấn. | Nêu rõ tiêu chí suy diễn chính (các điều kiện của H\textsubscript{1} và H\textsubscript{2} đang dùng khoảng tin cậy bootstrap). Giới hạn \(X_{t}\) theo từng giả thuyết, hoặc báo cáo từng kênh riêng cộng với \(RV_{t}\). Thảo luận công suất kiểm định với n ≈ 28.

4. [MAJOR] Quy tắc khi hệ số phóng đại phương sai (VIF) > 5, dòng 855–856 | Câu "báo cáo hai phương trình tách riêng" không nói đó là hai phương trình nào (tách \(S_{t}\) khỏi \(X_{t}\)? hay tách hai nhóm kênh?). Vì vậy quy tắc ra quyết định của H\textsubscript{2} không xác định được khi VIF vượt ngưỡng. | Viết rõ hai đặc tả, ví dụ (5a) \(Y_{t}=\alpha+\beta S_{t}+\delta RV_{t}+\varepsilon_{t}\) và (5b) \(Y_{t}=\alpha+\gamma'X_{t}+\varepsilon_{t}\), và nói rõ H\textsubscript{2} được đánh giá trên đặc tả nào.

5. [MINOR] Biến kiểm soát vĩ mô | Mục 4.3.3 (dòng 652–653) bổ sung "chỉ số giá tiêu dùng, tỷ giá … và lãi suất điều hành làm biến kiểm soát" trong kiểm tra độ bền, nhưng không nói chúng vào (5) ở vị trí nào. | Thêm câu: "Trong kiểm tra độ bền, \(X_{t}\) được mở rộng thêm …".

### LaTeX Math Formatting

1. [MINOR] Dòng 765 và 767 | `\sum_{m \in M}^{}` có chỉ số trên rỗng (tàn dư của pandoc). | Bỏ `^{}`.
2. [MINOR] Dòng 760–768, 777, 821 | Các phương trình được đặt inline bằng `\(...\)`, nên sẽ hiển thị cỡ chữ nhỏ (đặc biệt \(\frac{\rho}{2}\) và căn bậc hai trong (3)). | Nếu biên tập lại thì dùng `\begin{equation}…\label{eq:…}\end{equation}` và `\eqref`.
3. [MINOR] Dòng 821 | `\gamma'X_{t}` dùng dấu phẩy trên (prime) cho chuyển vị và không phân biệt véc-tơ với vô hướng. | Dùng `\boldsymbol{\gamma}^{\top}\mathbf{X}_{t}`. Trong (5) cũng không cần `\cdot` giữa \(\beta\) và \(S_{t}\).
4. [MINOR] Dòng 752–753 | Câu `\textbar{}\emph{M}\textbar{} = 7` được viết ở chế độ văn bản. | Viết thành `\(|M| = 7\)`.
5. [MINOR] Tham chiếu phương trình | Chỉ có (5) được nhắc đến bằng số (dòng 824, 851). Các phương trình (1)–(4) được đánh số nhưng không bao giờ được tham chiếu. | Thêm tham chiếu, chẳng hạn "\(U_{m,t}\) theo (1)" và "mức hối tiếc (4)" tại dòng 782 và 841, hoặc bỏ đánh số các phương trình không được dùng.

---

## 6. Tables, Figures & Documentation

## Agent 5: Tables, Figures & Documentation

Phạm vi rà soát: tôi chỉ đọc main.tex (phần chữ đang hiển thị) và hinh-van-ban.txt. Trong tệp chữ của hình, khung #2 và #3 là Hình 1, khung #4 và #5 là Hình 2. Mỗi hình bị lặp lại do Word lưu hai bản. Khung #1 và #6 rỗng, nên tôi không đọc được chữ của Hình 3. Tôi không tính chú thích dạng "Bảng . …" / "Hình . …" là lỗi, vì mất số là do chuyển đổi. Cả 7 bảng đều là bảng mô tả (tổng quan, giả thuyết, tập mô hình, bố cục, kế hoạch, công trình), không bảng nào báo cáo ước lượng. Vì vậy các mục về sai số chuẩn, số quan sát N, hiệu ứng cố định và dấu sao mức ý nghĩa là **không áp dụng (đề cương, chưa có ước lượng)** cho cả 7 bảng. Với 3 hình, các mục về nhãn trục, khoảng tin cậy, binscatter và đồ thị hệ số cũng không áp dụng, vì đây là sơ đồ khái niệm và quy trình, không phải đồ thị dữ liệu.

### Tables with Missing or Incomplete Notes

**Bảng 1. Các nhóm nghiên cứu gần nhất và khoảng trống nghiên cứu**
[MINOR] Bảng 1 | Ghi chú chỉ có "Nguồn: Thí sinh tổng hợp". Bảng không nêu tiêu chí chọn bốn nhóm, trong khi phần tổng quan có sáu nhóm (1)–(6). Tên các dòng cũng không khớp với tên các nhóm trong tổng quan, ví dụ "Danh mục ở Việt Nam" và "Chế độ thị trường ở Việt Nam" không phải tiêu đề nhóm nào ở mục 4.2. | Thêm ghi chú: "Bốn nhóm được chọn vì gần đề tài nhất; nhóm 'Rủi ro mô hình' tương ứng mục (2), ba nhóm còn lại thuộc mục (6) Nghiên cứu về Việt Nam".
[MINOR] Bảng 1 | Phạm vi tra cứu làm căn cứ cho cột "Khoảng trống" chỉ nằm ở đoạn văn sau bảng ("SSRN, RePEc/IDEAS, ScienceDirect… thực hiện đến ngày 30/09/2026"; "chưa gồm Scopus, Web of Science và các tạp chí tiếng Việt"). Người đọc chỉ xem bảng sẽ không biết các khoảng trống này có giới hạn gì. | Thêm vào ghi chú: "Khoảng trống xác định theo tra cứu trên [cơ sở dữ liệu] đến 30/09/2026; chưa gồm Scopus, Web of Science và tạp chí tiếng Việt."
[MINOR] Bảng 1 | Hai dòng "Chế độ thị trường ở Việt Nam (Hoang và Luu, 2024)" và "Bầy đàn ở Việt Nam (Vo và Phan, 2017)" mỗi dòng chỉ dựa trên một công trình. Riêng Hoang và Luu (2024) được thân bài gọi là "một bản thảo công bố trực tuyến", nhưng bảng không ghi điều này. | Ghi rõ trong ghi chú rằng hai dòng này mỗi dòng có một nguồn và Hoang và Luu (2024) là bản thảo chưa qua phản biện.

**Bảng 2. Giả thuyết, thước đo và cơ sở lý thuyết**
[MAJOR] Bảng 2 | Tiêu chí ủng hộ H\textsubscript{3} trong bảng mâu thuẫn với mục 4.3.8. Bảng ghi "cho mức hối tiếc và độ sụt giảm tối đa thấp hơn", tức đòi hỏi giảm thật sự. Mục 4.3.8 ghi "độ sụt giảm tối đa không cao hơn", tức chỉ cần không tăng. | Thống nhất một tiêu chí, ví dụ sửa bảng thành "độ sụt giảm tối đa không cao hơn", và thêm ghi chú "Quy tắc quyết định: xem mục 4.3.7–4.3.8".
[MAJOR] Bảng 2 | Kỳ vọng về dấu ở dòng H\textsubscript{2} có thể đọc theo hai nghĩa: "hệ số của tương quan đuôi âm (tương quan cao làm các danh mục chỉ mua hội tụ)". Có thể hiểu là "hệ số của [tương quan đuôi] mang dấu âm", hoặc là "hệ số của [tương quan ở đuôi âm]" (khái niệm đuôi âm theo Longin–Solnik). Thân bài (dòng 857–858) lặp lại đúng cụm từ này. | Viết lại thành "hệ số của tương quan đuôi mang dấu âm (β < 0)" và định nghĩa tương quan đuôi (ngưỡng đuôi, tần suất) trong ghi chú.
[MAJOR] Bảng 2 | Ghi chú chỉ có "Nguồn: Thí sinh đề xuất". Bảng thiếu ba thông tin cần để tự đứng được: (a) định nghĩa chế độ căng thẳng / S\textsubscript{t}; (b) đơn vị và tần suất của lợi suất tương đương chắc chắn và mức hối tiếc (theo năm hay theo tháng, %); (c) thủ tục suy luận: phân phối rỗng 1.000 lần bootstrap, khoảng tin cậy bootstrap khối, hiệu chỉnh Holm ở mức 10%, quy tắc "không kết luận" khi có dưới 10 cửa sổ căng thẳng độc lập. | Thêm ghi chú: "S\textsubscript{t}: tỷ lệ ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng đăng ký trước. CEQ, R\textsubscript{t}: % [theo năm], sau chi phí, ρ = 5. R\textsubscript{t} và D\textsubscript{t} trong phân tích chính được chia cho sai số chuẩn bootstrap. Suy luận: bootstrap khối; Holm 10% cho bốn giả thuyết; kết quả gọi là không kết luận khi có dưới 10 cửa sổ căng thẳng độc lập."
[MINOR] Bảng 2 | Vai trò của các thước đo ở dòng H\textsubscript{1} không khớp thân bài. Bảng gộp "độ phân tán mô hình, kích thước tập tin cậy mô hình" chung là "Kết quả phụ". Nhưng ở mục 4.3.7, D\textsubscript{t} là một trong ba điều kiện để ủng hộ H\textsubscript{1} ("β của D\textsubscript{t} cùng dấu"). Ở mục 4.3.6, kích thước tập tin cậy mô hình chỉ là "một thước đo mô tả". Bảng cũng không nói rằng R\textsubscript{t} được chuẩn hóa. | Tách thành: "Kết quả chính: R\textsubscript{t} (chuẩn hóa); điều kiện phụ: dấu của β với D\textsubscript{t}; mô tả: kích thước tập tin cậy mô hình".
[MINOR] Bảng 2 | Tiêu đề bảng nói "cơ sở lý thuyết", nhưng cột "Cơ sở" chủ yếu liệt kê nguồn phương pháp hoặc thực nghiệm (Danielsson và cộng sự, 2016; Hansen và cộng sự, 2011). Các nguồn lý thuyết nêu ở mục 4.3.1 (Kan và Zhou, 2007; Gilboa và Schmeidler, 1989; Hansen và Sargent, 2008; Hamilton, 1989) không xuất hiện. | Đổi tiêu đề hoặc tên cột thành "Cơ sở lý thuyết và phương pháp", hoặc thêm các nguồn lý thuyết vào cột.
[MINOR] Bảng 2 | Ở dòng H\textsubscript{4}, "thước đo bầy đàn" không được định nghĩa. Christie và Huang (1995) dùng CSSD, còn Chang và cộng sự (2000) dùng CSAD, và phương trình (5) chỉ có "độ phân tán chéo của lợi suất". | Ghi rõ thước đo (CSSD hay CSAD) và tần suất tính.
[MINOR] Bảng 2 | Bảng không có cột liên kết mỗi giả thuyết với câu hỏi nghiên cứu và khoảng trống (1)–(4) ở Bảng 1. Liên kết này hiện chỉ có trong văn bản ("H\textsubscript{1} trả lời câu hỏi 1…"). | Thêm cột "Câu hỏi / Khoảng trống".

**Bảng 3. Tập mô hình danh mục cạnh tranh**
[MAJOR] Bảng 3 | Bảng định nghĩa tập *M* (|*M*| = 7) dùng cho các phương trình (2)–(4), nhưng không có ghi chú nào cho biết: (a) M\textsubscript{6} (Garlappi và cộng sự, 2007) trùng với cơ chế giảm thiểu (ii) và M\textsubscript{7} (Kritzman và cộng sự, 2012) trùng với cơ chế (iii); (b) "Khi kiểm định H\textsubscript{3}, đề tài loại cơ chế (ii) và (iii) khỏi *M*"; (c) phép kiểm định trên tập mô hình tĩnh {M\textsubscript{1}, M\textsubscript{2}, M\textsubscript{3}, M\textsubscript{4}, M\textsubscript{6}}; (d) kết quả được báo cáo cả khi có lẫn khi không có M\textsubscript{5}. | Thêm cột "Tĩnh / theo chế độ" và ghi chú: "M\textsubscript{6}, M\textsubscript{7} đồng thời là cơ chế (ii), (iii) và bị loại khỏi *M* khi kiểm định H\textsubscript{3}; kết quả báo cáo cả khi có lẫn khi không có M\textsubscript{5}."
[MINOR] Bảng 3 | Bảng thiếu thông số chung cho mọi mô hình: chỉ mua (không bán khống), cửa sổ ước lượng 104 tuần dữ liệu tuần, tái cân bằng hằng tháng, siêu tham số chọn từ lưới với cùng ngân sách tinh chỉnh. Bảng cũng không nêu các trường hợp riêng: M\textsubscript{3} dùng nghịch đảo giả Moore–Penrose khi tỷ lệ số cổ phiếu trên số quan sát tuần vượt 0,5; quan điểm của M\textsubscript{4} lấy từ "một mô hình dự báo đơn giản" chưa được nêu tên. | Thêm ghi chú về các thông số chung và cột "Siêu tham số / đầu vào".

**Bảng 4. Dự kiến bố cục các chương và tiểu mục của luận án**
[MINOR] Bảng 4 | Văn bản ghi "Ngoài phần mở đầu, kết luận…, luận án dự kiến gồm sáu chương". Tuy vậy bảng có dòng "Kết luận" với ô "Tên chương" bỏ trống. Bảng cũng không cho biết "phần mở đầu" có trùng với "Chương 1: Giới thiệu nghiên cứu" hay không. | Điền tên ô (ví dụ "Kết luận và kiến nghị") và ghi chú rằng phần mở đầu là Chương 1, hoặc là một phần riêng.

**Bảng 5. Kế hoạch thực hiện luận án theo bốn năm và sản phẩm dự kiến**
[MINOR] Bảng 5 | Hai cam kết trong văn bản không có trong bảng. Mục 4.2 ghi "việc đọc toàn văn và mở rộng phạm vi tìm kiếm nằm trong kế hoạch năm thứ nhất", nhưng bảng chỉ ghi "đọc toàn văn các nguồn tổng quan" và không nhắc việc mở rộng sang Scopus, WoS và tạp chí trong nước. Bảng cũng thiếu mốc báo cáo số giai đoạn căng thẳng trong phần mẫu tính được mức hối tiếc (mục 4.3.6). | Bổ sung hai mục này vào Năm 1.
[MINOR] Bảng 5 | Thứ tự công việc khó theo dõi. Ước lượng thử ở Quý 2 diễn ra trước "làm sạch dữ liệu" ở Quý 3. Chuyên đề 3 ("thiết kế kiểm định có đăng ký trước", mục 7.2) là sản phẩm Năm 2, trong khi việc đăng ký trước đã xong ở Quý 4 Năm 1. | Thêm ghi chú giải thích thứ tự, hoặc chuyển chuyên đề 3 sang Năm 1.

**Bảng 6. Công trình đã công bố hoặc đã được chấp nhận đăng**
[MINOR] Bảng 6 | Bảng không có dòng "Nguồn" và không ghi ngày chốt trong tiêu đề. Ngày chốt chỉ có ở ô của dòng 3 ("chưa xuất bản tại ngày 30/09/2026"), trong khi tiêu đề Bảng 7 có ngày chốt. Ở dòng 2, Nguyễn Văn Trung không có dấu (*), nhưng ghi chú không giải thích dòng này khác gì. | Thêm "tính đến 30/09/2026" vào tiêu đề. Ghi rõ tác giả liên hệ của dòng 2.

**Bảng 7. Bản thảo đã gửi tạp chí, chưa công bố tại ngày 30/09/2026**
[MINOR] Bảng 7 | Có hai điểm chưa rõ. Cột "Số tác giả" không cho biết thí sinh là tác giả thứ mấy. Trạng thái "Đã sửa xong vòng 2 (mã 19322)" không cho biết bản sửa đã nộp lại và đang chờ quyết định hay chưa. | Thêm vị trí tác giả, hoặc ghi danh sách tác giả như Bảng 6. Viết lại trạng thái thành "Đã nộp bản sửa vòng 2, chờ quyết định".

**Bảng hồi quy (chưa có)**
[MINOR] Toàn đề cương | Không áp dụng cho bảng hiện có. Tuy nhiên mục 4.3.7 nêu hai cách suy luận cho phương trình (5): "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" và "bootstrap khối dừng… cho các hệ số hồi quy". Mục 4.3.10 hứa "Cạnh mỗi hệ số… báo cáo số cửa sổ độc lập và số giai đoạn căng thẳng độc lập". Đề cương không có bảng mẫu nào ghi rõ sẽ báo cáo loại sai số hay khoảng tin cậy nào. | Có thể thêm một bảng mẫu (bảng rỗng) cho phương trình (5) với các cột R\textsubscript{t}/D\textsubscript{t}, có hoặc không có X\textsubscript{t}, và các dòng: sai số chuẩn HAC hoặc khoảng tin cậy bootstrap khối, số cửa sổ, số giai đoạn căng thẳng độc lập, VIF, phân vị 95% của phân phối rỗng.

### Figures with Missing or Incomplete Notes

**Hình 1. Khung phân tích rủi ro lựa chọn mô hình theo chế độ thị trường**
[MINOR] Hình 1 | Ghi chú chỉ có "Nguồn: Thí sinh đề xuất". Hình không có chú giải cho mũi tên liền và mũi tên nét đứt. Phần giải thích chỉ nằm trong thân bài: "Mũi tên nét đứt từ rủi ro lựa chọn mô hình sang kết quả danh mục không mang giả thuyết riêng". Ký hiệu R\textsubscript{t}, D\textsubscript{t}, S\textsubscript{t} và H\textsubscript{1}–H\textsubscript{4} cũng không được định nghĩa ở dưới hình. | Thêm ghi chú: "Mũi tên liền: quan hệ có giả thuyết; mũi tên nét đứt: quan hệ theo định nghĩa, không kiểm định. R\textsubscript{t}: mức hối tiếc; D\textsubscript{t}: độ phân tán; S\textsubscript{t}: tỷ lệ ngày căng thẳng trong cửa sổ."
[MINOR] Hình 1 | Hộp "Chế độ thị trường | Chế độ bình thường | Chế độ căng thẳng | (biến S\textsubscript{t})" cho người đọc cảm giác S\textsubscript{t} là biến nhị phân. Thực ra phương trình (5) định nghĩa S\textsubscript{t} là "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng". | Ghi "S\textsubscript{t}: tỷ lệ ngày căng thẳng (0–1)" trong hình hoặc trong ghi chú.
[MINOR] Hình 1 | Tôi không kiểm tra được hướng mũi tên và việc H\textsubscript{2}/H\textsubscript{4} trỏ vào quan hệ (tác động điều tiết) hay trỏ vào biến, vì tệp chữ chỉ có nhãn. Thân bài khẳng định "Các biến kênh tác động lên chính quan hệ đó". | Đề nghị tác giả kiểm tra lại hình gốc.

**Hình 2. Cửa sổ ước lượng, cửa sổ đánh giá và thời điểm chọn mô hình**
[MAJOR] Hình 2 | Hình và văn bản cùng để ngỏ một chi tiết thiết kế then chốt. Hình vẽ mỗi cửa sổ thành một khối "Ước lượng: 104 tuần | Đánh giá: 6 tháng", nên người đọc hiểu là ước lượng một lần cho mỗi cửa sổ 6 tháng. Văn bản lại ghi "mô hình được chọn sau đó tái cân bằng hằng tháng trong suốt cửa sổ". Cả hai không cho biết mỗi tháng có ước lượng lại trên cửa sổ trượt 104 tuần hay không. Hình cũng không vẽ khoảng 36 tháng kết quả ngoài mẫu dùng để chọn mô hình *c*. Thời kỳ khởi động (mục 4.3.6 viết "mức hối tiếc chỉ tính được từ khoảng năm thứ năm của mẫu") cũng không có trên hình. | Vẽ thêm đoạn "36 tháng chọn mô hình" trước mỗi cửa sổ đánh giá, các mốc tái cân bằng hằng tháng, và ghi rõ có ước lượng lại hằng tháng hay không. Thêm ghi chú: "Cửa sổ đánh giá 6 tháng không chồng lấn; khoảng 28 cửa sổ cho giai đoạn 2007–2026; cửa sổ trượt hằng tháng chỉ dùng cho phân tích phụ."
[MINOR] Hình 2 | Trục ngang chỉ ghi "thời gian", không có mốc năm hay thang đo. Hình trộn đơn vị tuần và tháng ("104 tuần", "6 tháng", "36 tháng"). | Ghi mốc ví dụ (ví dụ năm 2007 → khoảng 2012 → …) hoặc quy đổi sang một đơn vị thống nhất (104 tuần ≈ 24 tháng).

**Hình 3. Quy trình nghiên cứu**
[MAJOR] Hình 3 | Tôi không đọc được chữ của hình (khung #6 rỗng), và ghi chú chỉ có "Nguồn: Thí sinh đề xuất". Vì vậy không kiểm chứng được nhận định "Hình 3 tóm tắt năm bước của quy trình…" và "đăng ký trước kế hoạch phân tích trước khi ước lượng chính thức tập mô hình ở bước 3". | Thêm ghi chú liệt kê năm bước, đánh dấu mốc đăng ký trước (Quý 4 Năm 1), và ghi rằng bước ước lượng thử (Quý 2 Năm 1, giai đoạn 2019–2025) diễn ra trước mốc này. Đề nghị tác giả kiểm tra lại hình gốc.

### Cross-Reference Issues

Cả 7 bảng và 3 hình đều được nhắc đến ít nhất một lần trong văn bản: Bảng 1 (dòng 479, 556), Bảng 2 (557), Bảng 3 (676, 752, 921), Bảng 4 (986), Bảng 5 (1122), Bảng 6 (1186), Bảng 7 (1234, 1322), Hình 1 (556, 564), Hình 2 (791), Hình 3 (891). Không có bảng hay hình nào được định nghĩa mà không được dẫn. Những tham chiếu tôi đã kiểm và thấy đúng:
- "chín bản thảo… trong đó ba bản thảo liên quan trực tiếp": Bảng 7 có 9 dòng, trong đó dòng 1, 5, 6 ghi "Có".
- "bản thảo số 5 ở Bảng 7": đúng là bản thảo về điểm gãy cấu trúc của thanh khoản theo Amihud/Bai-Perron. "Bản thảo số 6" đúng là bản thảo về tương quan. "Bản thảo số 1" đúng là bản thảo Black-Litterman nghịch đảo kết hợp phân cụm.
- "bảy mô hình… (Bảng 3)": Bảng 3 có M\textsubscript{1}–M\textsubscript{7}.
- "sáu chương (Bảng 4)": Bảng 4 có Chương 1–6.
- "bốn khoảng trống ở Bảng 1": Bảng 1 có khoảng trống (1)–(4).

[MAJOR] Hình 1 và Mục tiêu (iii) | Hình 1 và thân bài mâu thuẫn về vai trò của biến động. Hình 1 đặt biến động là biến kiểm soát ("Biến kênh | Biến động thực hiện (kiểm soát)"), và Câu hỏi 2 cùng H\textsubscript{2} cũng vậy ("Sau khi kiểm soát biến động thực hiện"; "Biến động thực hiện luôn có mặt trong X\textsubscript{t} với vai trò biến kiểm soát"). Nhưng mục tiêu (iii) lại xếp biến động vào nhóm biến kênh: "xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm biến động, thanh khoản, tương quan cực trị và bầy đàn". | Bỏ "biến động" khỏi danh sách biến kênh ở mục tiêu (iii), hoặc nói rõ đây là biến kiểm soát.
[MAJOR] Bảng 2 và mục 4.3.8 | Tiêu chí ủng hộ H\textsubscript{3} về độ sụt giảm tối đa không thống nhất: bảng ghi "thấp hơn", thân bài ghi "không cao hơn". Chi tiết ở phần Bảng 2 bên trên.
[MAJOR] Bảng 3 và mục 4.3.8 | Bảng 3 không đánh dấu rằng M\textsubscript{6} và M\textsubscript{7} trùng với cơ chế (ii) và (iii). Văn bản lại ghi "đề tài loại cơ chế (ii) và (iii) khỏi *M*", trong khi *M* được định nghĩa là "tập bảy mô hình ở Bảng 3". Người đọc sẽ không biết H\textsubscript{3} được kiểm định trên tập *M* nào (5 hay 7 mô hình).
[MINOR] Bảng 1 và mục 4.2 | Cùng một chữ "nhóm" được dùng cho hai cách chia khác nhau. Mục 4.2 chia tài liệu thành sáu nhóm có đánh số (1)–(6). Bảng 1 có "bốn nhóm công trình", và các khoảng trống của bảng cũng đánh số (1)–(4). Hai dãy số trùng nhau nên dễ nhầm. | Đánh số khoảng trống là K1–K4 (hoặc G1–G4).
[MINOR] Mục 4.3.10 và Bảng 7 | Câu "dùng phương pháp Bai-Perron trong một bản thảo đang gửi tạp chí" không dẫn đến dòng cụ thể. | Thêm "(bản thảo số 5, Bảng 7)".

### Formatting Inconsistencies

[MINOR] Nhãn ghi chú dưới bảng không thống nhất | Bảng 1–5 dùng "Nguồn: …", còn Bảng 6–7 dùng "Ghi chú: …" và không có dòng Nguồn. | Dùng chung một khuôn cho mọi bảng: "Nguồn: …" rồi đến "Ghi chú: …" khi cần.
[MINOR] Tên cột trích dẫn không thống nhất | Bảng 2 đặt tên cột là "Cơ sở", Bảng 3 là "Nguồn". Riêng ở Bảng 3, tên cột "Nguồn" trùng với dòng ghi chú "Nguồn: Thí sinh tổng hợp" ngay dưới bảng. | Đổi cột của Bảng 3 thành "Tài liệu gốc" hoặc "Cơ sở".
[MINOR] Cách ghi tác giả và tác giả liên hệ khác nhau giữa Bảng 6 và Bảng 7 | Bảng 6 ghi họ tên tác giả và đánh dấu (*). Bảng 7 chỉ ghi "Số tác giả" kèm một ghi chú chung. Bảng 7 có cột "Liên quan đến đề tài" còn Bảng 6 thì không, dù dòng 2 của Bảng 6 là nền của M\textsubscript{5}. | Dùng cùng một bộ cột cho hai bảng.
[MINOR] Thông tin chỉ mục (Scopus Q) chỉ có ở một số dòng | Bảng 6 có ở dòng 3. Bảng 7 có ở dòng 1, 4, 6. Các dòng còn lại không ghi gì. | Ghi chỉ mục cho mọi dòng, hoặc ghi "chưa được chỉ mục".
[MINOR] Khóa trích dẫn không thống nhất dấu tiếng Việt cho cùng một cặp tác giả | Bảng 6 ghi "(Nguyễn và Nguyễn, 2026b)" nhưng lại ghi "(Nguyen và Nguyen, 2026a)". | Thống nhất một cách viết.
[MINOR] Cách viết hoa tên bài báo không đồng nhất | Bảng 7 dòng 4 viết hoa đầu mỗi từ ("Corporate Brownwashing and Firm Valuation in ASEAN-5 Disclosure Regimes"), các dòng khác chỉ viết hoa chữ đầu câu. | Giữ đúng như bản gửi tạp chí, nhưng ghi điều này trong ghi chú như Bảng 6 đã làm, hoặc thống nhất về kiểu viết hoa đầu câu.
[MINOR] Bảng 4 có ô bỏ trống | Dòng "Kết luận & & …" để trống cột "Tên chương". | Điền tên ô.
[MINOR] Ghi chú dưới hình chỉ có nguồn | Cả Hình 1–3 chỉ có "Nguồn: Thí sinh đề xuất", trong khi nhiều bảng có ghi chú đầy đủ hơn. | Thêm khối "Ghi chú:" cho mỗi hình, nêu ký hiệu và cách đọc, theo cùng khuôn với các bảng.

---

## 7. Spelling, Grammar & Style

## Agent 1: Spelling, Grammar & Style

Phạm vi: chỉ đọc /tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/main.tex (số dòng ghi theo file .tex). Các lỗi do pandoc chuyển đổi (`\label{ux...}`, chú thích trống "Bảng ." / "Hình .", siêu liên kết mục lục) không tính là lỗi của tác giả.

Nhận xét chung: văn bản đúng chính tả và dấu tiếng Việt. Tôi không tìm thấy lỗi gõ dấu. Không có từ đệm kiểu "đáng chú ý", "quan trọng là", "rõ ràng", "đáng kể". Câu bị động "được/bị ... bởi" gần như không xuất hiện. Lỗi chủ yếu nằm ở bốn chỗ: câu có nghĩa mơ hồ hoặc bị đảo nghĩa, dùng thuật ngữ không nhất quán với chính các định nghĩa đề cương đã đặt ra, chủ thể hành văn lẫn lộn, và cách viết số chưa thống nhất.

### Critical Issues (must fix before submission)

1. [CRITICAL] Dòng 339–341 (mục 4.1) | "Thị trường Việt Nam có thanh khoản hạn chế ..., nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển." → "..., nên chênh lệch giữa các mô hình có thể lớn hơn so với ở thị trường phát triển." | Câu hiện tại đọc thành "chênh lệch lớn hơn *ở* thị trường phát triển", tức ngược với ý tác giả. Đây là lập luận chính cho việc chọn bối cảnh Việt Nam.

2. [CRITICAL] Bảng 2, H₂ (dòng 597–600) và dòng 857–858 | "hệ số của độ phi thanh khoản dương ... và hệ số của tương quan đuôi âm" → "hệ số của độ phi thanh khoản mang dấu dương ... và hệ số của tương quan đuôi dưới mang dấu âm" | "tương quan đuôi âm" có hai cách hiểu: (a) biến là tương quan ở đuôi âm (đuôi dưới), hoặc (b) hệ số mang dấu âm. Vì giả thuyết được định nghĩa bằng dấu của hệ số, phát biểu này phải rõ một nghĩa.

3. [CRITICAL] Trang bìa, dòng 102–104, so với mục 10 (dòng 1352–1366) | Trang bìa ghi người hướng dẫn chỉ có "PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân". Mục 10 lại đề xuất "GS.TS. Nguyễn Đức Khương" làm người hướng dẫn chính, còn PGS.TS. Hà Hồng Hạnh là người hướng dẫn thứ hai → bổ sung cả hai người trên trang bìa theo đúng thứ tự ở mục 10 | Thông tin ở trang bìa mâu thuẫn với nội dung bên trong.

### Minor Issues

(Các mục [MAJOR] là lỗi riêng lẻ mà phản biện nhiều khả năng sẽ nêu. Chúng được xếp trước, ngay trong danh sách này.)

1. [MAJOR] Dòng 296–298 | "chế độ căng thẳng, một trạng thái thống kê có biến động cao và lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng" → "chế độ căng thẳng, một trạng thái thống kê mà mô hình chuyển chế độ ước lượng được, có biến động cao và lợi suất thị trường thấp" | Câu hiện tại có thể hiểu là "lợi suất thấp do mô hình gây ra".
2. [MAJOR] Dòng 816–817 | "hồi quy các thước đo rủi ro mô hình theo biến chế độ" → "hồi quy các thước đo rủi ro lựa chọn mô hình (R_t) và độ phân tán (D_t) theo biến chế độ" | Mục 4.1 (dòng 285–295) đã tách rõ "rủi ro mô hình", "bất định mô hình" và "rủi ro lựa chọn mô hình". Ở đây tác giả lại gộp chúng.
3. [MAJOR] Dòng 961–962 | "đề tài đo mức bất định khi chọn mô hình theo từng chế độ thị trường" → "đề tài đo rủi ro lựa chọn mô hình (mức hối tiếc) theo từng chế độ thị trường" | Câu này mâu thuẫn với định nghĩa ở dòng 294–295: "Độ phân tán ... chỉ báo hiệu mức bất định, không đo rủi ro".
4. [MAJOR] Dòng 367–368 (mục tiêu iii) | "các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm biến động, thanh khoản, tương quan cực trị và bầy đàn" → "..., gồm thanh khoản, tương quan cực trị và bầy đàn, sau khi kiểm soát biến động" | Ở câu hỏi 2, H₂ và dòng 832–833, biến động là biến kiểm soát, không phải biến kênh.
5. [MAJOR] Dòng 836 và Bảng 4 (dòng 1028–1029: "4.3.1 Phân phối rỗng và hiệu chuẩn") | "phân phối rỗng" → "phân phối dưới giả thuyết không (null distribution)" | Trong tiếng Việt, "rỗng" nghĩa là "trống" (empty). Đây là lỗi dịch máy móc từ "null".
6. [MAJOR] Dòng 564–568 | "chế độ thị trường tác động lên rủi ro lựa chọn mô hình ... Các biến kênh tác động lên chính quan hệ đó ... Cơ chế giảm thiểu tác động lên quan hệ ..." → "gắn với / có liên hệ với" | Dòng 860 nói đề tài "gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả". Động từ nhân quả "tác động" ở mô tả Hình 1 mâu thuẫn với tuyên bố đó.
7. [MAJOR] Bảng 2, H₃ (dòng 603–606) so với dòng 882–885 | Bảng ghi "mức hối tiếc và độ sụt giảm tối đa thấp hơn", tiêu chí ở 4.3.8 lại ghi "độ sụt giảm tối đa không cao hơn" → chọn một cách diễn đạt và dùng cho cả hai chỗ | Điều kiện ủng hộ giả thuyết được phát biểu theo hai cách khác nhau.
8. [MAJOR] Dòng 914–917 | "Nếu dữ liệu bác bỏ giả thuyết, ... khi đó rủi ro lựa chọn mô hình không đổi theo chế độ" → "Nếu dữ liệu không ủng hộ giả thuyết, ... khi đó không có bằng chứng rằng rủi ro lựa chọn mô hình thay đổi theo chế độ" | Người ta bác bỏ giả thuyết không (H₀), không "bác bỏ" giả thuyết nghiên cứu. Ngoài ra, không bác bỏ được H₀ không có nghĩa là chứng minh "không đổi".
9. [MAJOR] Dòng 422–424 | "giữ lại những mô hình chưa thể bị loại là kém hơn ở một mức tin cậy cho trước, nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ" → "giữ lại những mô hình mà dữ liệu chưa đủ bằng chứng để loại vì kém hơn, ở một mức tin cậy cho trước; vì vậy dữ liệu ít thông tin cho ra tập lớn, dữ liệu nhiều thông tin cho ra tập nhỏ" | Câu dịch sát từng chữ, phải đọc lại mới hiểu. Đây cũng là chỗ duy nhất dùng bị động "bị".
10. [MINOR] Dòng 104 | "Đại học Kinh tế Quốc Dân" → "Trường Đại học Kinh tế Quốc dân" | Viết hoa sai, không thống nhất với dòng 1312 và 1365.
11. [MINOR] Dòng 1213 và 1219 | "(Nguyễn và Nguyễn, 2026b)" nhưng "(Nguyen và Nguyen, 2026a)" | Cùng một nhóm tác giả mà trích dẫn khi có dấu, khi không dấu, nên người đọc dễ tưởng là hai nhóm khác nhau. Nên thống nhất, chẳng hạn trích tác giả Việt bằng họ tên đầy đủ có dấu theo quy ước trích dẫn tiếng Việt.
12. [MINOR] Dòng 982 (tiêu đề 4.5) so với dòng 1001 | "đến 3 chữ số" so với "(đến ba chữ số)" | Không thống nhất cách viết số. Nếu tiêu đề do mẫu của trường quy định thì sửa tiêu đề cột trong bảng.
13. [MINOR] Dòng 1233 so với 1299 | "chín bản thảo" so với "cả 9 bản thảo" → dùng thống nhất một cách viết.
14. [MINOR] Dòng 791 | "cửa sổ 6 tháng" (trong khi dòng 639 viết "ba tháng") → "cửa sổ sáu tháng".
15. [MINOR] Dòng 793–794 | "chỉ tính được từ khoảng năm thứ năm của mẫu" → "chỉ tính được từ khoảng năm thứ 5 của mẫu" hoặc "sau khoảng bốn năm đầu của mẫu" | Lặp "năm ... năm" nên khó đọc.
16. [MINOR] Dòng 309, 649 so với 732, 920, 925 và Bảng 5 | "quý IV/2022" so với "quý 4 năm thứ nhất", "quý 1" → thống nhất cách đánh số quý (số La Mã hoặc số Ả Rập).
17. [MINOR] Dòng 1314 | "từ tháng 07/2026" → "từ tháng 7/2026".
18. [MINOR] Dòng 1353–1354 | dấu ngoặc kép thẳng "chính sách tài khóa, ..." → dùng ``...'' như ở dòng 1180 | Trong LaTeX, dấu " thẳng in ra sai kiểu ngoặc.
19. [MINOR] Dòng 1213, 1271, 1381 | "Tạp chí Kinh tế - Luật và Ngân hàng" → "Kinh tế – Luật và Ngân hàng" (gạch ngang en, `--`) | Gạch nối có khoảng trắng hai bên dùng sai chức năng.
20. [MINOR] Dòng 274, 376, 384, 420, 703, 869 | "trung bình-phương sai" → "trung bình–phương sai" (en dash) | Gạch nối nối hai cụm nhiều âm tiết làm câu đọc thành "trung bình-phương / sai". Tương tự, tên ghép của hai người nên dùng en dash: "Black–Litterman", "Bai–Perron", "Moore–Penrose" (dòng 466, 726, 924, 1324).
21. [MINOR] Dòng 466 | "mô hình tự hồi quy trung bình trượt tích hợp" → "mô hình tự hồi quy tích hợp trung bình trượt (ARIMA)" | Thứ tự thành tố chưa đúng với ARIMA. Nên kèm từ viết tắt.
22. [MINOR] Dòng 725–726 | "nghịch đảo giả Moore-Penrose" → "giả nghịch đảo Moore–Penrose" | Dùng thuật ngữ chuẩn.
23. [MINOR] Dòng 427 và 814 | "tỷ số Sharpe hiệu chỉnh" (cho deflated Sharpe ratio) → "tỷ số Sharpe giảm phát (deflated Sharpe ratio)" | "hiệu chỉnh" dễ nhầm với "adjusted Sharpe ratio", vốn là một chỉ tiêu khác.
24. [MINOR] Dòng 385 | "nhà đầu tư né tránh mơ hồ" → "nhà đầu tư ngại mơ hồ" | Nên dùng song song với "ngại rủi ro" ở dòng 746.
25. [MINOR] Dòng 828 | "véc-tơ" → "vectơ" | Đây là chính tả phổ biến trong văn bản toán–kinh tế lượng tiếng Việt.
26. [MINOR] Dòng 732 | "ở chế độ khóa có dấu thời gian" → "ở dạng khóa có dấu thời gian" | "chế độ" là thuật ngữ trung tâm (regime). Dùng từ này cho "locked mode" gây trùng nghĩa.
27. [MINOR] Dòng 290 so với 879 | "tổn thất kỳ vọng" (định nghĩa rủi ro lựa chọn mô hình) so với "giá trị thiệt hại kỳ vọng mức 95%" (expected shortfall) → nên ghi "tổn thất kỳ vọng vượt ngưỡng (ES) mức 95%" và giữ "tổn thất kỳ vọng" cho một nghĩa duy nhất.
28. [MINOR] Dòng 467 | "trên 468 tuần" → "với 468 quan sát tuần" | "trên" có thể hiểu là "hơn 468".
29. [MINOR] Dòng 468 | "lợi nhuận cao hơn" → "lợi suất cao hơn" | Toàn văn dùng "lợi suất".
30. [MINOR] Dòng 389–391 | "nhóm tài liệu này chưa trả lời nhà đầu tư nên chọn mô hình nào" → "chưa trả lời câu hỏi nhà đầu tư nên chọn mô hình nào".
31. [MINOR] Dòng 416–417 | "thu được hiệu quả ngoài mẫu tốt hơn việc dùng tiêu chí để chọn một mô hình" → "tốt hơn so với khi dùng tiêu chí để chọn một mô hình".
32. [MINOR] Dòng 440–442 | "Tu (2010) ước tính nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất ..." → "Tu (2010) ước tính rằng nhà đầu tư nào bỏ qua chuyển chế độ sẽ chịu tổn thất ..." | Câu hiện tại dễ đọc nhầm, phải đọc lại.
33. [MINOR] Dòng 458 | "Vì bằng chứng trái chiều giữa các thị trường" → "Vì bằng chứng giữa các thị trường còn trái chiều" | Mệnh đề thiếu vị ngữ.
34. [MINOR] Dòng 451 | "đặt nền móng cho lý thuyết triển vọng" → "đề xuất lý thuyết triển vọng".
35. [MINOR] Dòng 402 | "nhỏ khi thị trường yên ắng" → "nhỏ khi thị trường ổn định" | "yên ắng" là từ khẩu ngữ.
36. [MINOR] Dòng 419 | "do mô hình bất ổn định" → "do mô hình không ổn định".
37. [MINOR] Dòng 518–523 | Hai câu liên tiếp cùng khẳng định "chưa công trình nào đo rủi ro ... theo chế độ thị trường" → gộp thành một câu và giữ phần "theo hiểu biết của thí sinh".
38. [MINOR] Dòng 327–330 | "Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này, cùng mức độ họ dùng mô hình định lượng để phân bổ danh mục, từ báo cáo của cơ quan quản lý và tài liệu ..." → "Dựa trên báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ, thí sinh sẽ xác định (i) khung quy định áp dụng cho nhóm tổ chức này và (ii) mức độ họ dùng mô hình định lượng để phân bổ danh mục." | Câu hiện tại lồng nhiều mệnh đề, khó theo dõi.
39. [MINOR] Dòng 273–274 | "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê. Mô hình gốc của lĩnh vực này..." → "Các tổ chức đầu tư thường phân bổ vốn dựa trên mô hình thống kê. Mô hình gốc của quản trị danh mục là..." | Câu mở đầu khái quát quá mức. "lĩnh vực này" chưa có từ nào để quy chiếu.
40. [MINOR] Dòng 647 | "bao trùm khủng hoảng tài chính toàn cầu" → "bao gồm".
41. [MINOR] Dòng 746 | "coi là ngang giá với danh mục" → "coi là tương đương với danh mục".
42. [MINOR] Dòng 748 | "danh mục biến động hơn" → "danh mục biến động mạnh hơn".
43. [MINOR] Dòng 798 | "thí sinh sẽ biện minh chúng" → "thí sinh sẽ giải trình cơ sở lựa chọn chúng" | "biện minh" mang sắc thái bào chữa.
44. [MINOR] Dòng 866–871 | "Cơ chế (i) kết hợp các mô hình ..." trong khi "Cơ chế (ii) là ...", "Cơ chế (iii) là ..." → "Cơ chế (i) là kết hợp mô hình ..." | Các vế song song chưa cùng cấu trúc.
45. [MINOR] Dòng 895 | "Thí sinh đăng ký trước kế hoạch phân tích trước khi ước lượng ..." và dòng 1166–1167 "trước khi đăng ký trước" → "Thí sinh đăng ký kế hoạch phân tích trước khi ước lượng ..." | Lặp "trước".
46. [MINOR] Dòng 906 | "Cạnh mỗi hệ số" → "Kèm theo mỗi hệ số".
47. [MINOR] Dòng 925 | "một bản thảo đang gửi tạp chí" → "một bản thảo đã gửi tạp chí".
48. [MINOR] Dòng 946–947 | "danh mục chỉ mua (không bán khống) là cấu hình cơ sở, các ràng buộc khác nằm trong kiểm tra độ bền" → thay dấu phẩy bằng dấu chấm phẩy | Hai mệnh đề độc lập nối bằng dấu phẩy (comma splice).
49. [MINOR] Dòng 957–958 | "Dựa trên phần tóm tắt của các công trình gần nhất, đề tài khác chúng ở bốn điểm." → "Đối chiếu với phần tóm tắt của các công trình gần nhất, đề tài khác chúng ở bốn điểm." | Trạng ngữ "dựa trên ..." không gắn được với chủ ngữ "đề tài" (dangling modifier).
50. [MINOR] Dòng 965–966 | "mở mẫu về trước năm 2019" → "mở rộng mẫu về trước năm 2019".
51. [MINOR] Dòng 738 và Bảng 4 dòng 1024–1025 | "là lệch khỏi kế hoạch" / "các lệch khỏi kế hoạch" → "là sai lệch so với kế hoạch" / "các sai lệch so với kế hoạch" | Thiếu danh từ trung tâm.
52. [MINOR] Dòng 1168–1169 | "áp dụng quy tắc gọi kết quả là không kết luận đã đăng ký" → "áp dụng quy tắc đã đăng ký trước về việc gọi kết quả là chưa đủ cơ sở kết luận" | Cụm "đã đăng ký" chưa rõ bổ nghĩa cho "quy tắc" hay "kết quả".
53. [MINOR] Bảng 5, dòng 1148 | "đo thời gian tính" → "đo thời gian tính toán".
54. [MINOR] Dòng 1051–1053 | "có tính liên ngành và tập trung vào kinh tế hành vi và quản lý trong lĩnh vực kinh tế, còn đề tài ..." → giảm bớt các chữ "và" và lặp "kinh tế".
55. [MINOR] Dòng 1054–1055 | "chương trình giảng dạy bằng tiếng Anh hoặc tiếng Việt, thuận lợi cho công bố quốc tế" → "chương trình có thể học bằng tiếng Anh, thuận lợi cho công bố quốc tế" | Như hiện tại, câu ngầm nói học bằng tiếng Việt cũng thuận lợi cho công bố quốc tế.
56. [MINOR] Dòng 1325–1326 | "Bản thảo về tương quan ... chuẩn bị cho kênh tương quan" → "Bản thảo ... giúp thí sinh chuẩn bị công cụ cho kênh tương quan" | Chủ ngữ bất động vật đứng với động từ hành động.
57. [MINOR] Dòng 1360 | "trùng với ba cấu phần của đề tài" → "phù hợp với ba cấu phần của đề tài".
58. [MINOR] Dòng 941–955 | Dùng "+" làm dấu đầu dòng → dùng "-" hoặc danh sách LaTeX | Văn bản hành chính học thuật tiếng Việt thường dùng gạch đầu dòng.
59. [MINOR] Tên bài tiếng Anh, Bảng 6 dòng 1216–1218 và tài liệu tham khảo dòng 1555–1557 | "using regime switching CAPM ... period 2019 - 2025" → "using regime-switching CAPM ... over the period 2019–2025" | Tính từ ghép đứng trước danh từ cần gạch nối; khoảng năm cần en dash. Ghi chú dòng 1230–1231 nói tên bài "giữ nguyên như khi công bố". Nếu đó đúng là tên chính thức thì giữ nguyên, nhưng nên kiểm tra lại.
60. [MINOR] Bảng 7, dòng 1276 | "Corporate Brownwashing and Firm Valuation in ASEAN-5 Disclosure Regimes" (viết hoa kiểu Title Case) → "Corporate brownwashing and firm valuation in ASEAN-5 disclosure regimes" | Các tên bài khác trong Bảng 6 và 7 đều viết hoa kiểu câu. Đây là bản thảo chưa công bố nên có thể sửa.
61. [MINOR] Tài liệu tham khảo dòng 1536–1538 | Lo và Mueller (2010) ghi "8(2)." nhưng thiếu số trang → bổ sung số trang (pp. 13–63) để thống nhất với các mục khác.
62. [MINOR] Tài liệu tham khảo dòng 1404–1405 | "Correcting for selection bias, backtest overfitting and non-normality" → "..., backtest overfitting, and non-normality" | Tên gốc của bài có dấu phẩy Oxford.

### Style Patterns to Fix Throughout

1. [MAJOR] Chủ thể hành văn không nhất quán (tương đương lỗi "inconsistent first person" trong tiếng Anh). Ba chủ thể dùng xen kẽ, có khi trong cùng một đoạn: "Đề tài ước lượng mô hình chuyển chế độ Markov" (dòng 659), "Thí sinh đăng ký trước kế hoạch phân tích" (dòng 731), "Luận án sẽ ghi kèm nguồn" (dòng 643). Ngoài ra, "đề tài" (một chủ đề) không thể tự "ước lượng" hay "hồi quy". Cách sửa: dùng "nghiên cứu" (hoặc "luận án") làm chủ thể cho mọi thao tác phương pháp, và chỉ dùng "thí sinh" cho các việc của cá nhân (học phần, đăng ký OSF, kế hoạch).
2. [MAJOR] Dùng thuật ngữ trái với định nghĩa của chính đề cương. Mục 4.1 tách ba khái niệm "rủi ro mô hình", "bất định mô hình" và "rủi ro lựa chọn mô hình", nhưng về sau lại dùng lẫn (Minor Issues 2–3). Ví dụ: "đề tài đo mức bất định khi chọn mô hình" (dòng 961). Cách sửa: rà toàn văn và chỉ dùng "rủi ro lựa chọn mô hình" cho R_t. Gọi D_t và kích thước tập tin cậy là "chỉ báo bất định".
3. [MAJOR] Dùng động từ nhân quả cho kết quả tương quan. Ví dụ: "Các biến kênh tác động lên chính quan hệ đó" (dòng 565). Cách sửa: thay "tác động" bằng "gắn với" hoặc "có liên hệ với" ở mọi chỗ mô tả giả thuyết, cho khớp với tuyên bố ở dòng 860.
4. [MINOR] Động từ rút gọn mang màu khẩu ngữ. Ví dụ: "thấy" thay cho "nhận thấy/cho thấy" ("Bessler và cộng sự (2017) thấy", dòng 383), "loại" thay cho "loại bỏ" ("cách làm này loại thiên lệch nhìn trước", dòng 663), "thay" thay cho "thay thế" (dòng 323), "đổi theo" thay cho "thay đổi theo" (dòng 447–448), "vượt" thay cho "vượt trội so với" (dòng 280, 384, 387, 421). Cách sửa: dùng dạng đầy đủ trong văn phong học thuật. Riêng "thấy" xuất hiện 14 lần trong mục 4.1–4.3.
5. [MINOR] Calque "không kết luận" (inconclusive). Ví dụ: "quy tắc gọi một kết quả là không kết luận" (dòng 736). Cụm này còn xuất hiện ở dòng 908, 1070, 1168. Cách sửa: dùng "chưa đủ cơ sở kết luận" và viết thống nhất ở mọi chỗ.
6. [MINOR] So sánh thiếu "so với". Ví dụ: "Rủi ro lựa chọn mô hình ở chế độ căng thẳng cao hơn ở chế độ bình thường" (Bảng 2, H₁, dòng 592–593). Cách sửa: thêm "so với" trong mọi phép so sánh "X ở A cao/lớn hơn ở B", nhất là chỗ so sánh có thể đọc thành ngược nghĩa (Critical Issue 1).
7. [MINOR] Cách viết số. Chưa có quy tắc nhất quán cho số dưới 10 trong lời văn: "ba tháng" và "6 tháng", "chín bản thảo" và "9 bản thảo", "ba chữ số" và "3 chữ số". Riêng "9 tín chỉ" (dòng 1060, 1088, 1146) được viết bằng số một cách nhất quán. Cách sửa: viết bằng chữ các số từ một đến chín trong lời văn. Giữ chữ số cho giá trị tham số (ρ = 3, 5, 10; ngưỡng 5), số tín chỉ, phần trăm và số trong bảng. Phần trăm ("10%", "95%"), dấu thập phân ("0,5", "3,41/4"), dấu phân cách hàng nghìn ("1.000") và định dạng ngày DD/MM/YYYY đều đã nhất quán theo chuẩn tiếng Việt, không cần sửa.
8. [MINOR] Dấu gạch. Gạch nối "-" đang được dùng ở những chỗ cần en dash: các cặp khái niệm ("trung bình-phương sai"), tên hai người ("Black-Litterman", "Bai-Perron", "Moore-Penrose"), và tên tạp chí có khoảng trắng ("Kinh tế - Luật"). Khoảng năm thì đã dùng `--` đúng ("2005--2015"). Cách sửa: dùng `--` cho các trường hợp trên. Giữ gạch nối thường cho các mã như "SR 11-7", "VN-Index", "ASEAN-5".
9. [MINOR] Phân biệt "long-run/long run" và "high-income/high income" (tính từ ghép trước danh từ): không áp dụng cho văn xuôi tiếng Việt. Quy tắc này chỉ áp dụng cho các tên bài tiếng Anh (xem Minor Issue 59).
10. [MINOR] Câu bị động "được/bị ... bởi": không thấy cấu trúc "bởi". Các chỗ dùng "được" ("H₁ được ủng hộ", "mô hình được chọn") đều tự nhiên. Chỉ cần sửa câu "chưa thể bị loại là kém hơn" (Minor Issue 9).
11. [MINOR] Từ đệm và trùng ngữ (tương đương "interestingly", "notably", "very unique"): không phát hiện trong phần nội dung chính. Cũng không có câu "This paper contributes..." kiểu kể lể. Mục "Đóng góp dự kiến" là mục bắt buộc của mẫu đề cương và đã chỉ ra khác biệt cụ thể so với từng công trình.
---

## Priority Action Items

Quy tắc tập hợp (lần chạy lại 1, 2026-10-14): mọi mục được Agent 1–6 gắn thẻ `[CRITICAL]`, `[MAJOR]` hoặc `[MINOR]` đều được liệt kê riêng, mỗi mục một dòng đánh số. Phần chữ sau nhãn nguồn là nguyên văn của agent (vị trí | vấn đề | cách sửa theo format của agent đó). Nhãn nguồn có dạng "(A[số agent] · [tiêu đề mục trong đầu ra agent] #[số thứ tự trong mục đó])".

Quy tắc khử trùng lặp: chỉ gộp các mục trùng nguyên văn, tức toàn văn giống hệt nhau sau khi chuẩn hóa khoảng trắng. Các mục cùng nói về một vấn đề nhưng do agent khác nhau viết (ví dụ A1 · Critical Issues #3 và A2 · Critical Inconsistencies #1 về người hướng dẫn trên trang bìa; A1 · Minor Issues #7, A2 · Critical Inconsistencies #4 và A5 · Cross-Reference Issues #2 về tiêu chí H3) không phải trùng nguyên văn, nên vẫn giữ riêng. Số mục trước khử trùng: 217 (CRITICAL 11, MAJOR 67, MINOR 139). Số mục trùng nguyên văn: 0. Số mục sau khử trùng: 217. Cộng thêm 1 mục `[CRITICAL]` về khoảng trống đóng góp mà skill bắt buộc đặt đầu danh sách (vì hạng tổng hợp là Incremental/Insufficient), tổng cộng 218 dòng: CRITICAL 12, MAJOR 67, MINOR 139.

Thứ tự xếp hạng theo triage hierarchy của skill: (0) mục khoảng trống đóng góp; (1) `[CRITICAL]` của Agent 3 và Agent 6 Part 1 (không có mục nào); (2) `[CRITICAL]` của Agent 6 Part 2 (Required 1–5); (3) các `[CRITICAL]` còn lại theo thứ tự agent (A1, rồi A2; A4 và A5 không có); (4) toàn bộ `[MAJOR]`; (5) toàn bộ `[MINOR]`. Skill không quy định thứ tự bên trong hai tầng MAJOR và MINOR. Coordinator áp cùng thứ tự ưu tiên agent như tầng CRITICAL (A3 → A6 → A1 → A2 → A4 → A5), và giữ nguyên thứ tự gốc trong đầu ra của từng agent.

**CRITICAL** (must fix — these could cause desk rejection or major referee objections):
1. [CRITICAL] (Khoảng trống đóng góp — Contribution Synthesis; Agent 8 Part 3 #2) Vị trí: phần đặt vấn đề và mục 4.3.7 (chuẩn hóa, phân phối rỗng) | Vấn đề: xếp hạng tổng hợp là Incremental (advocate) / Insufficient for target journal (skeptic); phần mới so với Tu (2010), Danielsson và cộng sự (2016), DeMiguel và cộng sự (2009) chưa được chứng minh là một đại lượng mới | Sửa (thay đổi duy nhất mà Synthesis chọn): xây một chuẩn mô phỏng hoặc lý thuyết cho mức hối tiếc dưới giả thuyết không, để tách phần thuần do nhiễu khỏi phần do đảo hạng thực, rồi dùng kết quả đó để phân biệt rõ với ba công trình trên ngay ở phần đặt vấn đề.
2. [CRITICAL] (A6 · Part 2 — Analyses: Required and Suggested — Required #1) **Phân tích công suất và mô phỏng thiết kế trước khi đăng ký.**
     - *Phân tích:* Mô phỏng DGP có chuyển chế độ, hiệu chuẩn theo VN-Index, với hiệu ứng H1 giả định, và tính xác suất đạt cả ba điều kiện của H1 với khoảng 28 cửa sổ. Cần định nghĩa rõ cách đếm "cửa sổ căng thẳng" khi $S_t$ là biến liên tục, rồi báo cáo số cửa sổ căng thẳng kỳ vọng.
     - *Vì sao thiếu là vấn đề:* Không có phân tích này, quy tắc "dưới 10 → không kết luận" có thể khiến câu hỏi trung tâm không thể trả lời được ngay từ thiết kế.
     - *Nếu kết quả tích cực:* Mô phỏng cho thấy công suất ≥ 0,8 với hiệu ứng có ý nghĩa kinh tế thì thiết kế chứng minh được tính khả thi. Nếu không đạt, đề cương phải chuyển sang mẫu đa thị trường.
3. [CRITICAL] (A6 · Part 2 — Analyses: Required and Suggested — Required #2) **Phân phối rỗng cân bằng CE và tách thành phần cơ học do phương sai.**
     - *Phân tích:* Tái lấy mẫu sao cho các mô hình có CE bằng nhau trong từng chế độ, không chỉ trung bình bằng nhau. Đồng thời báo cáo $R_t$ ở dạng tổn thất kinh tế chưa chuẩn hóa và dạng đã chuẩn hóa. Thêm một biến thể với $\rho \to 0$ (chỉ trung bình) để thấy phần do số hạng phương sai.
     - *Vì sao thiếu là vấn đề:* Như đang viết, $\beta > 0$ có thể chỉ phản ánh việc phương sai cao hơn ở chế độ căng thẳng.
     - *Nếu kết quả tích cực:* H1 vẫn đứng vững dưới phân phối rỗng cân bằng CE thì kết quả thực sự nói về *lựa chọn*, không phải về biến động.
4. [CRITICAL] (A6 · Part 2 — Analyses: Required and Suggested — Required #3) **Mốc chuẩn chọn ngẫu nhiên và độ bền theo quy tắc chọn.**
     - *Phân tích:* So sánh mức hối tiếc của quy tắc "tốt nhất 36 tháng" với (a) chọn ngẫu nhiên đều trong M, (b) chọn theo Sharpe, (c) chọn trong tập tin cậy mô hình, (d) các độ dài lịch sử 12/24/60 tháng.
     - *Vì sao thiếu là vấn đề:* Không có mốc chuẩn này thì không phân biệt được "khó chọn" với "quy tắc chọn tồi". Chọn ngẫu nhiên cũng là phép thử giả (placebo) tự nhiên cho thông tin chứa trong lịch sử hiệu quả.
     - *Nếu kết quả tích cực:* Chênh lệch giữa hối tiếc của quy tắc chọn và của chọn ngẫu nhiên tăng ở chế độ căng thẳng thì đó là bằng chứng rằng lịch sử hiệu quả mất giá trị thông tin khi thị trường đổi chế độ. Phát hiện này mạnh hơn nhiều so với H1 hiện tại.
5. [CRITICAL] (A6 · Part 2 — Analyses: Required and Suggested — Required #4) **Kiểm định giả cho định nghĩa chế độ và cho các biến kênh.**
     - *Phân tích:*
       - (a) Gán ngẫu nhiên các khối thời gian giả làm "căng thẳng", giữ nguyên tỷ lệ và độ dài khối.
       - (b) Thay $S_t$ bằng chế độ ước lượng trên một chuỗi không liên quan, hoặc bằng chế độ dời trễ/dời sớm $k$ cửa sổ.
       - (c) Ước lượng H2 với chi phí giao dịch bằng 0, để kiểm tra hệ số Amihud dương có phải do cấu trúc hay không.
       - (d) Đo bầy đàn theo đặc tả phi tuyến của Chang và cộng sự (2000), tức CSAD theo $|R_m|$ và $R_m^2$, thay cho CSAD thô. Đồng thời sửa chiều kỳ vọng của H4.
     - *Vì sao thiếu là vấn đề:* Không có các phép thử này thì không phân biệt được kênh kinh tế với hệ quả cơ học của cách xây dựng biến.
     - *Nếu kết quả tích cực:* Các phép thử giả không có ý nghĩa thống kê còn phép thử thật thì có, nên H2 và H4 trở nên đáng tin.
6. [CRITICAL] (A6 · Part 2 — Analyses: Required and Suggested — Required #5) **Sửa thứ tự đăng ký trước và kiểm soát thiên lệch dò tìm dữ liệu cho thước đo CE.**
     - *Phân tích:* Đăng ký trước *trước* đợt "ước lượng thử bảy mô hình trên giai đoạn 2019--2025", hoặc giới hạn ước lượng thử ở giai đoạn trước 2019. Cố định cửa sổ và lưới siêu tham số, kèm một quy tắc tinh chỉnh lồng nhau theo thời gian. Thay tỷ số Sharpe hiệu chỉnh bằng các kiểm định dò tìm dữ liệu áp dụng trực tiếp cho CE: Reality Check của White (2000), SPA của Hansen (2005), StepM của Romano và Wolf (2005) [UNVERIFIED — based on general knowledge; authors must confirm]. Xác định rõ họ giả thuyết cho Holm (có tính H4 hay không).
     - *Vì sao thiếu là vấn đề:* Đây là điểm mạnh được quảng bá của đề cương, nhưng lịch trình hiện tại vô hiệu hóa nó.
     - *Nếu kết quả tích cực:* Đăng ký trước đáng tin sẽ là một lợi thế thật sự so với các bài cùng chủ đề.
7. [CRITICAL] (A1 · Critical Issues (must fix before submission) #1) Dòng 339–341 (mục 4.1) | "Thị trường Việt Nam có thanh khoản hạn chế ..., nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển." → "..., nên chênh lệch giữa các mô hình có thể lớn hơn so với ở thị trường phát triển." | Câu hiện tại đọc thành "chênh lệch lớn hơn *ở* thị trường phát triển", tức ngược với ý tác giả. Đây là lập luận chính cho việc chọn bối cảnh Việt Nam.
8. [CRITICAL] (A1 · Critical Issues (must fix before submission) #2) Bảng 2, H₂ (dòng 597–600) và dòng 857–858 | "hệ số của độ phi thanh khoản dương ... và hệ số của tương quan đuôi âm" → "hệ số của độ phi thanh khoản mang dấu dương ... và hệ số của tương quan đuôi dưới mang dấu âm" | "tương quan đuôi âm" có hai cách hiểu: (a) biến là tương quan ở đuôi âm (đuôi dưới), hoặc (b) hệ số mang dấu âm. Vì giả thuyết được định nghĩa bằng dấu của hệ số, phát biểu này phải rõ một nghĩa.
9. [CRITICAL] (A1 · Critical Issues (must fix before submission) #3) Trang bìa, dòng 102–104, so với mục 10 (dòng 1352–1366) | Trang bìa ghi người hướng dẫn chỉ có "PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân". Mục 10 lại đề xuất "GS.TS. Nguyễn Đức Khương" làm người hướng dẫn chính, còn PGS.TS. Hà Hồng Hạnh là người hướng dẫn thứ hai → bổ sung cả hai người trên trang bìa theo đúng thứ tự ở mục 10 | Thông tin ở trang bìa mâu thuẫn với nội dung bên trong.
10. [CRITICAL] (A2 · Critical Inconsistencies #1) Trang bìa ↔ Mục 10 | Trang bìa chỉ ghi một người hướng dẫn: "Người hướng dẫn khoa học (dự kiến): **- PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân**". Mục 10 lại đề xuất hai người, trong đó người hướng dẫn **chính** là "GS.TS. Nguyễn Đức Khương", còn PGS.TS. Hà Hồng Hạnh là "Người hướng dẫn thứ hai (dự kiến)". Hai chỗ mâu thuẫn trực tiếp về người hướng dẫn chính. Cần ghi đủ cả hai người trên trang bìa, theo đúng thứ tự ở mục 10.
11. [CRITICAL] (A2 · Critical Inconsistencies #2) Mục 4.1 (định nghĩa) ↔ Bảng 2, 4.3.6, 4.3.7, Hình 1 | Mục 4.1 khẳng định: "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, **không đo rủi ro**." Thế nhưng ở các chỗ sau, chính hai đại lượng này lại được coi là thước đo rủi ro:
     - Bảng 2 xếp chúng vào cột "Thước đo chính" của H1 ("Kết quả phụ: độ phân tán mô hình, kích thước tập tin cậy mô hình").
     - Mục 4.3.6 có tiêu đề "Thước đo rủi ro lựa chọn mô hình" và gọi tập tin cậy là "Thước đo thứ ba".
     - Mục 4.3.7 viết "hồi quy các thước đo rủi ro mô hình… Với Y_t là D_t hoặc R_t", và đặt điều kiện H1 được ủng hộ là "β của D_t cùng dấu".
     - Hình 1 đặt "Độ phân tán D_t | Tập tin cậy mô hình" trong ô "Rủi ro lựa chọn mô hình".

     Như vậy, khái niệm then chốt mà tác giả cam kết "giữ nguyên nghĩa… trong toàn văn bản" lại bị dùng trái với định nghĩa của chính nó.
12. [CRITICAL] (A2 · Critical Inconsistencies #3) Mục tiêu (iii) ↔ Câu hỏi 2, Bảng 2, 4.3.7, Hình 1 | Biến động thực hiện lúc là biến kênh, lúc là biến kiểm soát:
     - Mục tiêu (iii) xếp nó vào nhóm biến kênh: "các biến kênh… gồm **biến động**, thanh khoản, tương quan cực trị và bầy đàn".
     - Câu hỏi 2, H2, H4 và Hình 1 ("Biến động thực hiện (kiểm soát)") lại coi nó là biến kiểm soát: "Sau khi kiểm soát biến động thực hiện, các biến kênh (thanh khoản, tương quan cực trị và… bầy đàn)".
     - Mục 4.3.7 vừa định nghĩa X_t là "véc-tơ biến kênh", vừa nói "Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát".

     Hệ quả là phép phân rã "β₀ − β₁" (β khi không có và khi có X_t), được giới thiệu là "phần chênh lệch giữa hai chế độ do các biến kênh giải thích", thực ra tính cả phần do biến động giải thích. Điều này mâu thuẫn với câu hỏi 2 ("sau khi kiểm soát biến động… giải thích được bao nhiêu phần chênh lệch").

**MAJOR** (should fix — will likely be raised by referees):
13. [MAJOR] (A3 · Causal Overclaiming (must address) #1) [4.3.2, đoạn diễn giải Hình 1, dòng 564–568] | "Theo Hình 1, chế độ thị trường tác động lên rủi ro lựa chọn mô hình (giả thuyết H1). Các biến kênh tác động lên chính quan hệ đó, tức giải thích một phần chênh lệch giữa hai chế độ (H2 và H4). Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục (H3)." | "Tác động" xuất hiện ba lần và trình bày khung phân tích như một mô hình nhân quả. Trong khi đó, "chế độ" chỉ là một nhãn thống kê, được ước lượng từ chính biến động và lợi suất, tức những đại lượng cấu thành R_t và D_t. Không có biến thể ngoại sinh nào cả. Đoạn này cũng mâu thuẫn trực tiếp với dòng 859–860 ("Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả"). Loại lỗi: (a), dùng ngôn ngữ nhân quả cho một liên hệ. | Fix (làm yếu ngôn ngữ): "Theo Hình 1, rủi ro lựa chọn mô hình được kỳ vọng khác nhau giữa các chế độ thị trường (H1). Các biến kênh được kỳ vọng có liên hệ với rủi ro lựa chọn mô hình và tương quan với phần chênh lệch giữa hai chế độ (H2, H4). Cơ chế giảm thiểu được kỳ vọng cho mức hối tiếc thấp hơn so với chọn một mô hình (H3)." Nên vẽ lại mũi tên trong Hình 1 thành đường liên hệ, hoặc ghi chú rằng mũi tên không mang nghĩa nhân quả.
14. [MAJOR] (A3 · Causal Overclaiming (must address) #2) [Bảng 2, H2, dòng 597–600] | "hệ số của độ phi thanh khoản dương (thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau) và hệ số của tương quan đuôi âm (tương quan cao làm các danh mục chỉ mua hội tụ)" | Hai cơ chế ("làm … cách xa nhau", "làm … hội tụ") được viết ở thể khẳng định, như sự thật đã được chứng minh. Thực ra chúng là giả thuyết, và hồi quy (5) không kiểm định được kênh nào. Hệ số dương của độ phi thanh khoản tương thích với nhiều giải thích khác, chẳng hạn cả hai cùng phản ánh một cú sốc chung. Loại lỗi: (b), cơ chế được viết như sự thật. | Fix: "(giả thuyết cơ chế: khi thanh khoản cạn, các mô hình có vòng quay khác nhau có thể cho kết quả sau chi phí cách xa nhau hơn)" và "(giả thuyết cơ chế: tương quan cao có thể khiến các danh mục chỉ mua hội tụ)". Nên thêm một câu nói rõ dấu của hệ số tương thích với cơ chế nhưng không xác lập cơ chế.
15. [MAJOR] (A3 · Causal Overclaiming (must address) #3) [4.1 Câu hỏi 2, dòng 352–355; Bảng 2 H2 "phần chênh lệch giữa hai chế độ do biến kênh giải thích", dòng 600–601; 4.3.7, dòng 849–852] | "chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?"; "phần chênh lệch giữa hai chế độ do biến kênh giải thích"; "Đề tài ước lượng phần chênh lệch giữa hai chế độ do các biến kênh giải thích bằng hiệu β0 − β1" | Hiệu β0 − β1 chỉ là mức thay đổi của hệ số khi thêm biến, theo kiểu phân rã trung gian Baron–Kenny. Muốn đọc nó là "phần do X giải thích" thì phải giả định X là trung gian ngoại sinh và không có biến gây nhiễu chung giữa X và Y. Ở đây độ phi thanh khoản và tương quan đuôi đều là kết quả của chính chế độ căng thẳng, nên chúng là biến kiểm soát xấu (bad controls), và β0 − β1 không có nghĩa nhân quả. "Do … giải thích" ngầm khẳng định quan hệ trung gian nhân quả. Loại lỗi: (a). | Fix: đổi thành "mức suy giảm của hệ số chế độ khi đưa biến kênh vào (β0 − β1), một thống kê mô tả về phần đồng biến chung, không phải ước lượng của hiệu ứng trung gian". Câu hỏi 2 nên sửa thành "…và hệ số chênh lệch giữa hai chế độ thay đổi bao nhiêu khi đưa các biến này vào?" Tên mục 5.4 trong Bảng 4 ("Phân rã chênh lệch theo chế độ") cũng nên sửa tương ứng.
16. [MAJOR] (A3 · Causal Overclaiming (must address) #4) [4.4 Đóng góp dự kiến, dòng 973–974] | "Về thực nghiệm, đề tài cung cấp bằng chứng cho thị trường Việt Nam về mức độ, thời điểm và các kênh của rủi ro lựa chọn mô hình." | "Các kênh" khẳng định đã xác lập cơ chế, trong khi thiết kế chỉ cho phép báo cáo liên hệ có điều kiện, và H4 chỉ ở mức thăm dò. Loại lỗi: (b). | Fix: "…về mức độ, thời điểm của rủi ro lựa chọn mô hình và các biến thị trường có liên hệ thống kê với nó." Tên Chương 5 nên đổi từ "Các biến kênh của rủi ro lựa chọn mô hình" thành "Các biến thị trường liên hệ với rủi ro lựa chọn mô hình".
17. [MAJOR] (A3 · Causal Overclaiming (must address) #5) [4.2 (5) và 4.4 Phạm vi nội dung, dòng 453–455 và 949–951; H4 Bảng 2, dòng 609–611] | "Bầy đàn … là một kênh hành vi có thể làm các mô hình cho kết quả khác nhau"; "độ phân tán chéo của lợi suất, một thước đo bầy đàn ở cấp thị trường" | Có hai tầng vượt mức. (i) Cơ chế "bầy đàn làm các mô hình cho kết quả khác nhau" không được lập luận ở đâu cả, chỉ được nêu ra. (ii) Mức phân tán chéo không phải thước đo bầy đàn. Trong chính Christie–Huang (1995) và Chang và cộng sự (2000), bầy đàn được suy ra khi độ phân tán *giảm*, hoặc tăng chậm hơn tuyến tính, so với |lợi suất thị trường|. Theo cách hiểu đó, "phân tán chéo cao" là dấu hiệu *ít* bầy đàn. Vì vậy, nếu H4 được ủng hộ thì kết quả không nói được gì về bầy đàn, và việc gọi phép thử này là "giao thoa với kinh tế hành vi" là vượt mức. | Fix: gọi biến này là "độ phân tán chéo của lợi suất (CSAD)". Nếu muốn nói đến bầy đàn, cần dùng hệ số phi tuyến của Chang và cộng sự (2000) ước lượng theo từng cửa sổ và đặt giả thuyết theo dấu của hệ số đó. Câu ở dòng 453–455 nên viết thành giả thuyết, kèm một lập luận cụ thể vì sao bầy đàn có thể làm khác biệt giữa các mô hình tăng hoặc giảm.
18. [MAJOR] (A3 · Causal Overclaiming (must address) #6) [4.3.10, dòng 914–917] | "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam." | Câu này tự tin quá mức theo chiều ngược lại. Không bác bỏ được H0 với khoảng 28 cửa sổ, trong đó chỉ một vài cửa sổ rơi vào chế độ căng thẳng, không chứng minh được rằng rủi ro "không đổi". Câu này cũng mâu thuẫn với quy tắc "không kết luận" ở dòng 907–908 của chính đề cương. Hơn nữa, H1 không được ủng hộ cũng không suy ra được "1/N đủ dùng". Đó là một kết luận khác, cần một phép thử riêng (1/N không thua mô hình nào, với khoảng tin cậy chặt). | Fix: "Nếu dữ liệu không ủng hộ giả thuyết, đề tài báo cáo kích thước hiệu ứng và khoảng tin cậy để xác định chênh lệch giữa hai chế độ có bị chặn trên bởi một mức nhỏ về mặt kinh tế hay không (kiểm định tương đương). Chỉ khi đó đề tài mới kết luận rủi ro lựa chọn mô hình không khác biệt đáng kể giữa các chế độ."
19. [MAJOR] (A3 · Causal Overclaiming (must address) #7) [4.3.1 Khung lý thuyết, dòng 545–547] | "nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng, tổn thất do chọn sai mô hình cũng tăng theo." | Mệnh đề nhân quả này được trình bày như một hệ quả tất yếu, nhưng nó không tất yếu. Chính H2 dự đoán rằng tương quan cao làm các danh mục hội tụ, khi đó mức hối tiếc có thể *giảm* dù sai số ước lượng tăng. Ngoài ra, phần "tăng do sai số ước lượng" chính là thứ mà phép chuẩn hóa theo sai số chuẩn bootstrap và phân phối rỗng (dòng 782–784, 835–839) được thiết kế để loại bỏ. Như vậy cơ chế lý thuyết được nêu và đại lượng thực sự được kiểm định không khớp nhau. Loại lỗi: (b). | Fix: "…tổn thất do chọn sai mô hình có thể tăng theo; tuy nhiên tương quan tăng có thể kéo các danh mục lại gần nhau, nên chiều tác động ròng là câu hỏi thực nghiệm." Đồng thời cần nói rõ H1, sau khi chuẩn hóa, kiểm định phần rủi ro lựa chọn *vượt quá* mức do nhiễu ước lượng.
20. [MAJOR] (A3 · Causal Overclaiming (must address) #8) [4.2 (2), dòng 393–394; và cuối (1), dòng 390–391] | "Các nghiên cứu đã đo rủi ro mô hình cho dự báo và định giá, nhưng chưa đo cho quyết định phân bổ."; "nhóm tài liệu này chưa trả lời nhà đầu tư nên chọn mô hình nào và chịu tổn thất bao nhiêu khi chọn sai." | Đây là cách mô tả tài liệu vượt mức, và mâu thuẫn với chính các nguồn đề cương trích. Kan và Zhou (2007) đo tổn thất lợi suất tương đương chắc chắn do sai số tham số trong quyết định phân bổ. DeMiguel và cộng sự (2009) báo cáo chênh lệch lợi suất tương đương chắc chắn của 14 mô hình so với 1/N. Tu (2010), được trích ở dòng 440–442, ước tính tổn thất lợi suất tương đương chắc chắn khi bỏ qua chuyển chế độ, tức là tổn thất của việc chọn sai mô hình trong quyết định phân bổ. Đây là tuyên bố ưu tiên chưa kiểm chứng. | Fix: thu hẹp khoảng trống cho đúng điểm mới: "Các nghiên cứu này đo tổn thất của từng mô hình so với một chuẩn, hoặc so với tham số thật; chưa nghiên cứu nào mà thí sinh tìm được đo tổn thất kỳ vọng của việc *chọn trước* một mô hình trong tập cạnh tranh và so sánh tổn thất đó giữa các chế độ." Tác giả cần xác nhận tuyên bố này trước khi nộp.
21. [MAJOR] (A3 · Generalization Issues #1) [Tên đề tài; 4.1 Mục tiêu, dòng 360–363; 4.4, dòng 941 và 955] | "đo lường và giải thích rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư trên thị trường chứng khoán Việt Nam"; "kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam" | Mẫu thực tế chỉ là rổ 30 mã thanh khoản và vốn hóa lớn nhất trên HOSE, danh mục chỉ mua, tái cân bằng hằng tháng, với một tập 7 mô hình. Câu "chỉ áp dụng trong phạm vi thị trường Việt Nam" vẫn rộng hơn mẫu: nó không bao phủ HNX, UPCoM, cổ phiếu vốn hóa nhỏ và thanh khoản thấp, mà theo chính H2 đây lại là nơi rủi ro lựa chọn có thể lớn nhất. | Fix: "Kết luận áp dụng cho danh mục chỉ mua gồm các cổ phiếu thanh khoản cao trên HOSE và cho tập bảy mô hình đã đăng ký; không suy rộng cho cổ phiếu thanh khoản thấp, các sàn khác hoặc tập mô hình khác."
22. [MAJOR] (A3 · Generalization Issues #2) [4.3.6, dòng 770–775; dùng xuyên suốt từ "nhà đầu tư"] | "Tại đầu mỗi cửa sổ đánh giá, nhà đầu tư chọn trước mô hình c có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước" | Mức hối tiếc R_t, và do đó toàn bộ "rủi ro lựa chọn mô hình", chỉ được định nghĩa với một quy tắc chọn cụ thể (chọn mô hình thắng trong 36 tháng). Nhưng lời văn của đề cương ("tổn thất kỳ vọng phát sinh khi nhà đầu tư phải chọn một mô hình", dòng 290–291) khái quát cho mọi nhà đầu tư và mọi cách chọn. Đề cương cũng tự thừa nhận chưa biết các công ty quản lý quỹ Việt Nam chọn mô hình thế nào (dòng 327–330, 952). | Fix: nói rõ thước đo này có điều kiện theo quy tắc chọn đã đăng ký. Nên thêm kiểm tra độ bền với các quy tắc khác (cửa sổ 12, 24, 60 tháng; chọn trong tập tin cậy mô hình; mức hối tiếc kỳ vọng khi chọn ngẫu nhiên đều).
23. [MAJOR] (A3 · Generalization Issues #3) [4.1, dòng 273] | "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê." | Câu mở đầu khẳng định như sự thật phổ quát, trong khi dòng 327–330 thừa nhận thí sinh *sẽ* xác định "mức độ họ dùng mô hình định lượng để phân bổ danh mục". Động cơ thực tiễn của đề tài ở Việt Nam vì vậy dựa trên một tiền đề chưa được chứng minh. | Fix: "Nhiều tổ chức đầu tư, chủ yếu ở các thị trường phát triển, phân bổ vốn có sự hỗ trợ của mô hình thống kê; mức độ áp dụng ở Việt Nam sẽ được xác định trong năm thứ nhất."
24. [MAJOR] (A3 · Missing Caveats #1) Ý nghĩa kinh tế so với ý nghĩa thống kê | 4.3.7 (tiêu chí H1, dòng 840–843), tiêu chí H2 (dòng 856–858), tiêu chí H3 (dòng 882–885) | Mọi tiêu chí "được ủng hộ" đều thuần túy thống kê: vượt phân vị 95% của phân phối rỗng, khoảng tin cậy loại trừ 0, đúng dấu. Không có ngưỡng ý nghĩa kinh tế tối thiểu nào được ấn định trước. Ngoài ra, việc chia R_t và D_t cho sai số chuẩn bootstrap (dòng 782–784) biến thước đo chính thành đại lượng không đơn vị, nên người đọc không biết mức hối tiếc là bao nhiêu điểm phần trăm lợi suất tương đương chắc chắn mỗi năm. Kích thước hiệu ứng hiện chỉ được báo cáo khi kết quả "không kết luận" (dòng 908–910). | Suggested text: "Song song với thước đo chuẩn hóa, đề tài luôn báo cáo mức hối tiếc thô theo điểm phần trăm lợi suất tương đương chắc chắn năm hóa, cùng khoảng tin cậy. Tệp đăng ký trước ấn định một ngưỡng ý nghĩa kinh tế tối thiểu (ví dụ X điểm cơ bản/năm, so với mức phí quản lý quỹ điển hình); một kết quả có ý nghĩa thống kê nhưng dưới ngưỡng này được báo cáo là không quan trọng về mặt kinh tế."
25. [MAJOR] (A3 · Missing Caveats #2) Khả năng thực thi giao dịch trong chế độ căng thẳng (giới hạn biên độ giá, ngày khóa sàn) | 4.3.8 và 4.3.10 (dòng 880–881, 912–914) | Cơ chế giảm thiểu (H3) và mọi lợi suất sau chi phí giả định giao dịch được ở giá đóng cửa. Trên HOSE, trong các phiên căng thẳng nhiều mã nằm sàn và không có người mua. Chi phí giao dịch dạng tham số cố định sẽ đánh giá thấp chi phí đúng vào lúc H3 được kiểm định, nên dễ phóng đại lợi ích của các cơ chế có vòng quay khác nhau. Đề cương có nhắc đến nguồn dữ liệu về biên độ dao động giá (dòng 643–644) nhưng không coi đó là mối đe dọa đối với kết luận. | Suggested text: "Trong ngày một mã chạm giá sàn (trần), lệnh bán (mua) của danh mục được giả định không khớp và chuyển sang phiên kế tiếp. Chi phí giao dịch được mô hình hóa tăng theo độ phi thanh khoản Amihud, và kết quả H3 được báo cáo cả với chi phí cố định lẫn chi phí phụ thuộc thanh khoản."
26. [MAJOR] (A3 · Missing Caveats #3) Kênh thanh khoản trong H2 có vận hành được trong thước đo hay không | Bảng 2 H2 và 4.3.8 (dòng 880–881) | Cơ chế của H2 ("thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau") chỉ vận hành nếu chi phí giao dịch tăng khi thanh khoản giảm. Nếu chi phí là một tham số cố định, độ phi thanh khoản chỉ có thể liên hệ với R_t qua lợi suất, và hệ số dương sẽ không phản ánh cơ chế đã nêu. | Suggested text: "Để kênh thanh khoản có thể quan sát được trong thước đo, chi phí giao dịch trong phân tích chính được mô hình hóa là hàm tăng của độ phi thanh khoản; phiên bản chi phí cố định nằm trong kiểm tra độ bền."
27. [MAJOR] (A3 · Missing Caveats #4) Chế độ căng thẳng hay *chuyển* chế độ | 4.3.6–4.3.7 (sau phương trình 4–5) | Với quy tắc chọn "thắng trong 36 tháng trước", mức hối tiếc cao trong một cửa sổ căng thẳng có thể chỉ phản ánh việc cửa sổ đó đến *sau* một giai đoạn bình thường. Mô hình thắng trong giai đoạn yên ắng bị chọn rồi thua, tức là do thời điểm chuyển chế độ chứ không phải do bản thân trạng thái căng thẳng. Hệ số β trong (5) không tách được hai cách giải thích này. | Suggested text: "Đề tài bổ sung vào (5) biến chỉ báo cửa sổ chuyển chế độ (chế độ của cửa sổ chọn khác chế độ của cửa sổ đánh giá), để phân biệt rủi ro lựa chọn gắn với trạng thái căng thẳng với rủi ro gắn với việc chuyển chế độ."
28. [MAJOR] (A3 · Missing Caveats #5) Biến kiểm soát xấu, quan hệ đồng thời và sai số đo của biến kênh | 4.3.7 (dòng 828–833, 852–856) | Độ phi thanh khoản, tương quan đuôi và biến động thực hiện được đo trên cùng cửa sổ với R_t, nên vừa là kết quả của chế độ vừa có thể cùng chịu một cú sốc với R_t (quan hệ đồng thời hoặc nhân quả ngược). Tương quan đuôi ước lượng trên cửa sổ 6 tháng chỉ có rất ít quan sát ở đuôi, nên sai số đo lớn và hệ số bị kéo về 0. Đề cương mới chỉ bàn về đa cộng tuyến (hệ số phóng đại phương sai). | Suggested text: "Các biến kênh được đo trên cùng cửa sổ với kết quả và có thể cùng phản ứng với một cú sốc; vì vậy hệ số γ không có nghĩa nhân quả. Đề tài báo cáo thêm phiên bản dùng biến kênh của cửa sổ trước (t−1), và báo cáo sai số chuẩn hoặc khoảng tin cậy bootstrap của bản thân tương quan đuôi để đánh giá mức sai số đo."
29. [MAJOR] (A3 · Missing Caveats #6) Tính không đồng nhất giữa các giai đoạn căng thẳng và khả năng cao không có kết luận | 4.3.6 (dòng 792–797), 4.3.10 (dòng 905–910), đoạn "Nếu dữ liệu ủng hộ các giả thuyết" (dòng 970) | Mức hối tiếc chỉ tính được từ khoảng năm thứ năm, và khủng hoảng toàn cầu chủ yếu dùng để ước lượng chế độ. Vì vậy phần mẫu tính được hối tiếc nhiều khả năng chỉ chứa 2–4 giai đoạn căng thẳng có nguyên nhân rất khác nhau (COVID-19, trái phiếu doanh nghiệp 2022…). Kết quả "chế độ căng thẳng" có thể phản ánh đặc thù của một giai đoạn. Với ngưỡng "dưới 10 cửa sổ căng thẳng thì không kết luận", kịch bản cơ sở có thể là không kết luận, nhưng phần đóng góp dự kiến không nói ra điều này. | Suggested text: "Đề tài luôn, chứ không chỉ khi kết quả không kết luận, báo cáo kích thước hiệu ứng theo từng giai đoạn căng thẳng và kết quả khi loại lần lượt từng giai đoạn. Với khoảng 28 cửa sổ, đề tài dự kiến số cửa sổ căng thẳng có thể dưới ngưỡng 10; khi đó đóng góp chính là thước đo, quy trình đăng ký trước và ước lượng khoảng của chênh lệch, không phải một kết luận ủng hộ hay bác bỏ H1."
30. [MAJOR] (A3 · Missing Caveats #7) Hàm ý thực tiễn: quy trình giám sát dùng chính những thước đo mà đề cương nói không đo rủi ro, và phát hiện chế độ bị trễ | 4.4, dòng 974–977 | "đo độ phân tán và tập tin cậy mô hình định kỳ, và kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng" mâu thuẫn với dòng 294–295 ("Độ phân tán … và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro"). Ngoài ra, xác suất lọc thường xác nhận chế độ căng thẳng muộn, nên việc "kích hoạt khi thị trường ở chế độ căng thẳng" có thể đến sau tổn thất. | Suggested text: "Thủ tục dùng độ phân tán và tập tin cậy mô hình như chỉ báo cảnh báo về bất định, không như thước đo rủi ro. Bước kích hoạt dựa trên xác suất lọc thời gian thực, và luận án báo cáo độ trễ nhận diện cùng lợi ích sau khi tính độ trễ đó."
31. [MAJOR] (A3 · Missing Caveats #8) Tuyên bố ưu tiên chưa kiểm chứng (phạm vi toàn cầu, không được rào đón) | 4.2, cuối các nhóm (2), (3), (4) và đoạn sau Bảng 1 | Các câu: "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục" (dòng 409–410); "chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường" (dòng 429–430); "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không" (dòng 447–448); "chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường" (dòng 519–520). Các câu này mang phạm vi *toàn cầu*, trong khi quy trình tìm kiếm được mô tả ở dòng 520–529 chỉ đỡ cho tuyên bố về *Việt Nam*, và thí sinh tự thừa nhận "mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn". Đây đều là tuyên bố ưu tiên chưa kiểm chứng. Tác giả phải xác nhận trước khi nộp. | Suggested text: mở đầu mỗi câu bằng "Trong phạm vi tìm kiếm đã mô tả, thí sinh chưa tìm thấy công trình nào…", hoặc giới hạn rõ "trên thị trường Việt Nam". Riêng câu ở dòng 447–448 nên được kiểm tra lại với tài liệu về hiệu quả danh mục trong thị trường tăng/giảm và trong khủng hoảng.
32. [MAJOR] (A6 · Part 2 — Analyses: Required and Suggested — Suggested #1) **Mở rộng đa thị trường hoặc thêm mẫu tham chiếu dài.**
     - *Phân tích:* Áp dụng đúng quy trình cho các thị trường ASEAN (đề cương đã nêu đây là hướng sau tốt nghiệp) hoặc cho danh mục ngành của Mỹ có lịch sử dài [UNVERIFIED — based on general knowledge; authors must confirm]. Sau đó ước lượng H1 trên dữ liệu bảng thị trường × cửa sổ.
     - *Vì sao quan trọng:* Đây là cách duy nhất để có đủ số giai đoạn căng thẳng, đồng thời đưa đề tài ra khỏi khuôn khổ "nghiên cứu một thị trường".
     - *Tính khả thi:* Cao với dữ liệu công khai, nhưng cần điều chỉnh kế hoạch bốn năm.
33. [MAJOR] (A6 · Part 2 — Analyses: Required and Suggested — Suggested #2) **Phân rã mức hối tiếc thành phần do sai số ước lượng và phần do sai đặc tả.**
     - *Phân tích:* Cho từng mô hình, so sánh CE với tham số "oracle" ước lượng trên toàn cửa sổ với CE từ tham số ước lượng thực. Cách tiếp cận theo tinh thần Kerkhof và cộng sự (2010) mà đề cương đã trích.
     - *Vì sao quan trọng:* Kiểm tra trực tiếp cơ chế mà khung lý thuyết nêu ("nếu sai số ước lượng và mức bất định cùng tăng ở chế độ căng thẳng").
     - *Tính khả thi:* Khả thi với dữ liệu sẵn có.
34. [MAJOR] (A6 · Part 2 — Analyses: Required and Suggested — Suggested #3) **Đo xác suất quá khớp khi kiểm định ngược (PBO) và độ ổn định thứ hạng theo chế độ.**
     - *Phân tích:* Ma trận chuyển thứ hạng của bảy mô hình giữa các cửa sổ; tương quan hạng Spearman giữa cửa sổ $t$ và $t+1$, tách theo chế độ; PBO theo Bailey, Borwein, López de Prado và Zhu (2017) [UNVERIFIED — based on general knowledge; authors must confirm].
     - *Vì sao quan trọng:* Trả lời trực tiếp khoảng trống mà đề cương nêu ("chưa xét thứ hạng thay đổi ra sao khi thị trường chuyển chế độ"). Các thước đo này cũng ít phụ thuộc vào thang đo phương sai.
     - *Tính khả thi:* Cao.
35. [MAJOR] (A6 · Part 2 — Analyses: Required and Suggested — Suggested #4) **Hàm hữu dụng và thước đo đuôi thay thế cho mức hối tiếc.**
     - *Phân tích:* Tính CE theo CRRA hoặc theo hữu dụng có tính độ lệch và độ nhọn. Tính mức hối tiếc theo CVaR và theo mức sụt giảm tối đa. Hiện nay các tiêu chí đuôi chỉ dùng cho H3.
     - *Vì sao quan trọng:* Trong chế độ căng thẳng, xấp xỉ trung bình–phương sai đánh giá thấp tổn thất đuôi. Kết luận H1 có thể đổi tùy hàm hữu dụng.
     - *Tính khả thi:* Cao.
36. [MAJOR] (A6 · Part 2 — Analyses: Required and Suggested — Suggested #5) **Truyền sai số ước lượng chế độ vào kết quả.**
     - *Phân tích:* Dùng xác suất lọc làm trọng số liên tục thay cho ngưỡng. Bootstrap cả bước ước lượng Markov. So sánh 2 với 3 chế độ và các định nghĩa theo ngưỡng sụt giảm hoặc biến động thực hiện (đề cương đã nêu). Báo cáo tỷ lệ trùng khớp giữa các định nghĩa.
     - *Vì sao quan trọng:* Đề cương tự nhận "Việc nhận diện chế độ tự nó là một dạng rủi ro mô hình". Sai số này cần đi vào khoảng tin cậy của $\beta$, không chỉ vào phần kiểm tra độ bền.
     - *Tính khả thi:* Trung bình, do tải tính toán khi ước lượng lại theo cửa sổ mở rộng.
37. [MAJOR] (A1 · Minor Issues #1) Dòng 296–298 | "chế độ căng thẳng, một trạng thái thống kê có biến động cao và lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng" → "chế độ căng thẳng, một trạng thái thống kê mà mô hình chuyển chế độ ước lượng được, có biến động cao và lợi suất thị trường thấp" | Câu hiện tại có thể hiểu là "lợi suất thấp do mô hình gây ra".
38. [MAJOR] (A1 · Minor Issues #2) Dòng 816–817 | "hồi quy các thước đo rủi ro mô hình theo biến chế độ" → "hồi quy các thước đo rủi ro lựa chọn mô hình (R_t) và độ phân tán (D_t) theo biến chế độ" | Mục 4.1 (dòng 285–295) đã tách rõ "rủi ro mô hình", "bất định mô hình" và "rủi ro lựa chọn mô hình". Ở đây tác giả lại gộp chúng.
39. [MAJOR] (A1 · Minor Issues #3) Dòng 961–962 | "đề tài đo mức bất định khi chọn mô hình theo từng chế độ thị trường" → "đề tài đo rủi ro lựa chọn mô hình (mức hối tiếc) theo từng chế độ thị trường" | Câu này mâu thuẫn với định nghĩa ở dòng 294–295: "Độ phân tán ... chỉ báo hiệu mức bất định, không đo rủi ro".
40. [MAJOR] (A1 · Minor Issues #4) Dòng 367–368 (mục tiêu iii) | "các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm biến động, thanh khoản, tương quan cực trị và bầy đàn" → "..., gồm thanh khoản, tương quan cực trị và bầy đàn, sau khi kiểm soát biến động" | Ở câu hỏi 2, H₂ và dòng 832–833, biến động là biến kiểm soát, không phải biến kênh.
41. [MAJOR] (A1 · Minor Issues #5) Dòng 836 và Bảng 4 (dòng 1028–1029: "4.3.1 Phân phối rỗng và hiệu chuẩn") | "phân phối rỗng" → "phân phối dưới giả thuyết không (null distribution)" | Trong tiếng Việt, "rỗng" nghĩa là "trống" (empty). Đây là lỗi dịch máy móc từ "null".
42. [MAJOR] (A1 · Minor Issues #6) Dòng 564–568 | "chế độ thị trường tác động lên rủi ro lựa chọn mô hình ... Các biến kênh tác động lên chính quan hệ đó ... Cơ chế giảm thiểu tác động lên quan hệ ..." → "gắn với / có liên hệ với" | Dòng 860 nói đề tài "gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả". Động từ nhân quả "tác động" ở mô tả Hình 1 mâu thuẫn với tuyên bố đó.
43. [MAJOR] (A1 · Minor Issues #7) Bảng 2, H₃ (dòng 603–606) so với dòng 882–885 | Bảng ghi "mức hối tiếc và độ sụt giảm tối đa thấp hơn", tiêu chí ở 4.3.8 lại ghi "độ sụt giảm tối đa không cao hơn" → chọn một cách diễn đạt và dùng cho cả hai chỗ | Điều kiện ủng hộ giả thuyết được phát biểu theo hai cách khác nhau.
44. [MAJOR] (A1 · Minor Issues #8) Dòng 914–917 | "Nếu dữ liệu bác bỏ giả thuyết, ... khi đó rủi ro lựa chọn mô hình không đổi theo chế độ" → "Nếu dữ liệu không ủng hộ giả thuyết, ... khi đó không có bằng chứng rằng rủi ro lựa chọn mô hình thay đổi theo chế độ" | Người ta bác bỏ giả thuyết không (H₀), không "bác bỏ" giả thuyết nghiên cứu. Ngoài ra, không bác bỏ được H₀ không có nghĩa là chứng minh "không đổi".
45. [MAJOR] (A1 · Minor Issues #9) Dòng 422–424 | "giữ lại những mô hình chưa thể bị loại là kém hơn ở một mức tin cậy cho trước, nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ" → "giữ lại những mô hình mà dữ liệu chưa đủ bằng chứng để loại vì kém hơn, ở một mức tin cậy cho trước; vì vậy dữ liệu ít thông tin cho ra tập lớn, dữ liệu nhiều thông tin cho ra tập nhỏ" | Câu dịch sát từng chữ, phải đọc lại mới hiểu. Đây cũng là chỗ duy nhất dùng bị động "bị".
46. [MAJOR] (A1 · Style Patterns to Fix Throughout #1) Chủ thể hành văn không nhất quán (tương đương lỗi "inconsistent first person" trong tiếng Anh). Ba chủ thể dùng xen kẽ, có khi trong cùng một đoạn: "Đề tài ước lượng mô hình chuyển chế độ Markov" (dòng 659), "Thí sinh đăng ký trước kế hoạch phân tích" (dòng 731), "Luận án sẽ ghi kèm nguồn" (dòng 643). Ngoài ra, "đề tài" (một chủ đề) không thể tự "ước lượng" hay "hồi quy". Cách sửa: dùng "nghiên cứu" (hoặc "luận án") làm chủ thể cho mọi thao tác phương pháp, và chỉ dùng "thí sinh" cho các việc của cá nhân (học phần, đăng ký OSF, kế hoạch).
47. [MAJOR] (A1 · Style Patterns to Fix Throughout #2) Dùng thuật ngữ trái với định nghĩa của chính đề cương. Mục 4.1 tách ba khái niệm "rủi ro mô hình", "bất định mô hình" và "rủi ro lựa chọn mô hình", nhưng về sau lại dùng lẫn (Minor Issues 2–3). Ví dụ: "đề tài đo mức bất định khi chọn mô hình" (dòng 961). Cách sửa: rà toàn văn và chỉ dùng "rủi ro lựa chọn mô hình" cho R_t. Gọi D_t và kích thước tập tin cậy là "chỉ báo bất định".
48. [MAJOR] (A1 · Style Patterns to Fix Throughout #3) Dùng động từ nhân quả cho kết quả tương quan. Ví dụ: "Các biến kênh tác động lên chính quan hệ đó" (dòng 565). Cách sửa: thay "tác động" bằng "gắn với" hoặc "có liên hệ với" ở mọi chỗ mô tả giả thuyết, cho khớp với tuyên bố ở dòng 860.
49. [MAJOR] (A2 · Critical Inconsistencies #4) Bảng 2 (H3) ↔ 4.3.8 ↔ Hình 1 | Tiêu chí và phạm vi của H3 khác nhau giữa ba chỗ:
     - Về độ sụt giảm tối đa: Bảng 2 yêu cầu "mức hối tiếc và độ sụt giảm tối đa **thấp hơn**", còn tiêu chí ủng hộ ở 4.3.8 chỉ yêu cầu "độ sụt giảm tối đa **không cao hơn**".
     - Về số cơ chế: Bảng 2 chỉ nêu hai cơ chế ("kết hợp mô hình và danh mục vững chắc"), trong khi 4.3.8 đánh giá ba cơ chế (thêm cơ chế (iii) "quy tắc chuyển chế độ") và Hình 1 đặt "Quy tắc theo chế độ" trong ô cơ chế giảm thiểu gắn với H3.
     - Về thước đo: Bảng 2 liệt kê thêm "giá trị thiệt hại kỳ vọng mức 95%; vòng quay", nhưng tiêu chí ủng hộ ở 4.3.8 không dùng hai thước đo này.
50. [MAJOR] (A2 · Critical Inconsistencies #5) H4 (Bảng 2) ↔ 4.2(5), 4.4 | Hướng tác động của H4 ngược với ý nghĩa bầy đàn mà đề tài nêu:
     - Mục 4.4 gọi độ phân tán chéo là "một thước đo bầy đàn ở cấp thị trường". Theo Christie và Huang (1995), được trích ở 4.2, bầy đàn biểu hiện bằng độ phân tán chéo **thấp**.
     - H4 lại phát biểu "độ phân tán chéo của lợi suất **cao** đi cùng rủi ro lựa chọn mô hình cao", tức là ít bầy đàn đi cùng rủi ro cao.
     - Điều đó trái với lập luận ở 4.2(5): bầy đàn là "một kênh hành vi có thể làm các mô hình cho kết quả khác nhau".

     Thêm vào đó, cột thước đo của H4 có hai đại lượng ("Độ phân tán chéo của lợi suất; thước đo bầy đàn"), nhưng 4.3.7 chỉ đưa độ phân tán chéo vào X_t.
51. [MAJOR] (A2 · Critical Inconsistencies #6) Hình 1 / 4.3.2 ↔ Bảng 2 (H2) ↔ 4.2(4) | Văn bản nói các biến kênh "giải thích một phần chênh lệch giữa hai chế độ (H₂ và H₄)". Tuy vậy:
     - H2 dự đoán hệ số của tương quan đuôi là âm.
     - Chính 4.2(4) dẫn Ang và Bekaert (2002): "tương quan và biến động cùng tăng ở chế độ xấu".

     Ghép hai điều này lại thì kênh tương quan sẽ **thu hẹp** chênh lệch giữa hai chế độ chứ không giải thích nó. Phép đo β₀ − β₁ gộp hai kênh có dấu ngược nhau, nên con số "bao nhiêu phần" mà câu hỏi 2 hứa trả lời không diễn giải được.
52. [MAJOR] (A2 · Critical Inconsistencies #7) 4.3.10 (Holm) ↔ 4.3.7 ↔ Bảng 2 | Có hai điểm không thống nhất về kiểm định bội và mức ý nghĩa:
     - "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho **bốn** giả thuyết". Trong khi đó, H4 được ghi là "(thăm dò)" và "Đề tài chỉ báo cáo H₄ như kết quả thăm dò", nên đưa H4 vào họ kiểm định khẳng định là mâu thuẫn.
     - Ngưỡng của H1 là "phân vị 95%" của phân phối rỗng, tức mức 5% một phía và chưa hiệu chỉnh. Ngưỡng này không khớp với ngưỡng Holm mức 10% đã đăng ký.
53. [MAJOR] (A2 · Critical Inconsistencies #8) 4.3.4 (số chế độ) ↔ 4.1, Hình 1, phương trình (5) | Văn bản để mở khả năng ba chế độ: "Số chế độ (hai hoặc ba) do tiêu chí thông tin quyết định". Nhưng toàn bộ khung phân tích là hai chế độ: Hình 1 chỉ có "Chế độ bình thường | Chế độ căng thẳng", và β "đo chênh lệch… giữa chế độ căng thẳng và chế độ bình thường". Nếu có ba chế độ thì không rõ "chế độ bình thường" là chế độ nào.
54. [MAJOR] (A2 · Critical Inconsistencies #9) Phương trình (5): định nghĩa S_t ↔ 4.3.4 ↔ 4.3.10 | Có hai vấn đề:
     - S_t là "tỷ lệ số ngày trong cửa sổ có xác suất lọc… vượt ngưỡng", tức cần xác suất lọc theo **ngày**. Nhưng 4.3.4 chỉ mô tả việc tính "Tại mỗi ngày tái cân bằng" (hằng tháng): "ước lượng lại tham số… và từ đó tính xác suất lọc tại ngày t".
     - S_t là biến liên tục, nhưng quy tắc "Khi số cửa sổ độc lập **ở chế độ căng thẳng** dưới 10, đề tài gọi kết quả là không kết luận" cần cách phân loại nhị phân một cửa sổ là "ở chế độ căng thẳng", và cách phân loại này chưa được định nghĩa.
55. [MAJOR] (A2 · Critical Inconsistencies #10) 4.3.6 (≈28 cửa sổ) + 4.3.5 + 4.3.10 ↔ Bảng 4 / 7.3 | Nhiều chi tiết do chính đề cương nêu khiến quy tắc "không kết luận" gần như chắc chắn được kích hoạt với H1:
     - chỉ có "khoảng 28 cửa sổ đánh giá độc lập";
     - khủng hoảng tài chính toàn cầu "chủ yếu phục vụ ước lượng chế độ", tức nằm ngoài phần mẫu tính được mức hối tiếc;
     - dữ liệu 2019–2025 chỉ "gồm hai giai đoạn căng thẳng";
     - ngưỡng tối thiểu là 10 cửa sổ căng thẳng.

      Trong khi đó, Bảng 4 (Chương 4: "Kiểm định H₁") và 7.3 (bài báo 1 "kiểm định H₁") được viết như thể sẽ có kết quả kiểm định. Đề cương nên nêu rõ tình huống "không kết luận" sẽ được trình bày thế nào trong cấu trúc chương và kế hoạch bài báo.
56. [MAJOR] (A2 · Critical Inconsistencies #11) 4.3.2 / Hình 1 ↔ 4.3.7 | Ngôn ngữ nhân quả và điều tiết không khớp với thiết kế liên hệ cộng tính:
      - "chế độ thị trường **tác động lên** rủi ro lựa chọn mô hình"; "Các biến kênh **tác động lên chính quan hệ đó**", tức là vai trò điều tiết.
      - Phương trình (5) là mô hình cộng tính không có số hạng tương tác, và phép đo β₀ − β₁ mang tính trung gian.
      - Mục 4.3.7 lại cam kết "gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả".

      Tương tự, câu "Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục (H₃)" không khớp với H3, vốn chỉ so sánh cơ chế giảm thiểu với chọn một mô hình.
57. [MAJOR] (A2 · Terminology Drift #1) "Rủi ro lựa chọn mô hình" / "rủi ro mô hình" / "bất định mô hình" | Mục 4.1 phân biệt ba khái niệm này, nhưng sau đó chúng bị dùng lẫn:
     - 4.3.7 viết "hồi quy các **thước đo rủi ro mô hình**" khi đang nói về R_t và D_t;
     - phần đóng góp ở 4.4 viết "đề tài **đo mức bất định** khi chọn mô hình theo từng chế độ", trong khi đối tượng đo là rủi ro lựa chọn.

     Đề xuất: dùng nhất quán "rủi ro lựa chọn mô hình" cho R_t, và gọi D_t cùng kích thước tập tin cậy là "chỉ báo bất định mô hình".
58. [MAJOR] (A2 · Terminology Drift #2) "Tương quan cực trị" / "tương quan đuôi" / "tương quan hiệu chỉnh theo biến động" | Ba cách gọi xuất hiện ở các chỗ khác nhau:
     - câu hỏi 2, mục tiêu (iii), 4.3.1 và Bảng 4 (mục 5.2) dùng "tương quan cực trị";
     - H2 và Hình 1 dùng "tương quan đuôi";
     - 4.3.7 đưa vào X_t cả "tương quan đuôi **và** tương quan hiệu chỉnh theo biến động", nhưng H2 chỉ có một hệ số tương quan.

     Đề xuất: chọn một tên gọi, định nghĩa biến cụ thể, và nói rõ biến tương quan thứ hai đóng vai trò gì đối với H2.
59. [MAJOR] (A2 · Terminology Drift #3) "Biến kênh" | Thuật ngữ này lúc bao gồm biến động thực hiện (mục tiêu (iii), định nghĩa X_t ở 4.3.7), lúc không (câu hỏi 2, Hình 1). Đề xuất: tách ký hiệu thành X_t (biến kênh) và V_t (biến động thực hiện, biến kiểm soát).
60. [MAJOR] (A4 · Mathematical Errors #1) Phương trình (5), dòng 826 | Chữ trong bài ghi "\(\beta\) đo chênh lệch của \(Y_{t}\) giữa chế độ căng thẳng và chế độ bình thường", nhưng \(S_{t}\) là "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng", tức một biến liên tục trong [0,1] chứ không phải biến giả. Vì vậy \(\beta\) là chênh lệch dự báo tuyến tính giữa một cửa sổ có toàn bộ số ngày ở chế độ căng thẳng (S=1) và một cửa sổ có toàn bộ số ngày ở chế độ bình thường (S=0). Với 6 tháng một cửa sổ, hai điểm này có thể ít hoặc không hề xuất hiện trong mẫu, nên đây là một phép ngoại suy. Ngoài ra, \(\beta\) còn được ước lượng *có điều kiện theo* \(X_{t}\) (trong đó luôn có biến động thực hiện). | Sửa thành: "\(\beta\) đo mức thay đổi của \(Y_{t}\) khi tỷ lệ ngày căng thẳng trong cửa sổ tăng từ 0 lên 1, với \(X_{t}\) giữ cố định". Một cách khác là định nghĩa \(S_{t}\) thành biến giả (chẳng hạn \(S_{t}=1\) khi tỷ lệ này vượt 0,5) nếu muốn giữ cách diễn giải "chênh lệch giữa hai chế độ".
61. [MAJOR] (A4 · Mathematical Errors #2) Phân rã \(\beta_{0}-\beta_{1}\), dòng 832–833 và 850–852 | Dòng 832–833 ghi "Biến động thực hiện luôn có mặt trong \(X_{t}\) với vai trò biến kiểm soát", trong khi \(\beta_{0}\) là hệ số "khi không có … \(X_{t}\)". Như vậy \(\beta_{0}\) không kiểm soát biến động thực hiện, và \(\beta_{0}-\beta_{1}\) gộp chung phần do biến động giải thích với phần do các biến kênh giải thích. Điều này mâu thuẫn với Câu hỏi 2 và H\textsubscript{2}, vốn đặt câu hỏi "sau khi kiểm soát biến động thực hiện". | Tách \(X_{t}=(RV_{t}, Z_{t}')'\) và định nghĩa \(\beta_{0}\) là hệ số khi chỉ có \(RV_{t}\), \(\beta_{1}\) là hệ số khi có cả \(RV_{t}\) và \(Z_{t}\). Phần do kênh giải thích khi đó là \(\beta_{0}-\beta_{1}\). Nếu muốn chia phần giải thích cho từng kênh thì nên dùng phân rã Gelbach (2016).
62. [MAJOR] (A4 · Mathematical Errors #3) Phương trình (4) và mục 4.3.8, dòng 874–875 | Bài viết suy ra \(R_{t}\ge 0\) vì "mô hình chọn trước thuộc \emph{M}". Sau đó, khi kiểm định H\textsubscript{3}, "đề tài loại cơ chế (ii) và (iii) khỏi \emph{M}, nên mức hối tiếc của hai cơ chế này có thể âm". Có ba vấn đề: (a) Cơ chế (ii) (danh mục vững chắc theo Garlappi và cộng sự, 2007) và cơ chế (iii) (theo Kritzman và cộng sự, 2012) chính là M\textsubscript{6} và M\textsubscript{7} trong Bảng 3. Loại chúng ra làm \(|M|\) giảm từ 7 xuống 5, nên \(D_{t}\), \(U_{o,t}\) và mức chuẩn hóa thay đổi theo. Bài không nói khi đó các thước đo này được tính lại hay không. (b) Cơ chế (i), kết hợp mô hình, cũng không phải là phần tử của \emph{M}, nên mức hối tiếc của nó cũng có thể âm, nhưng câu văn chỉ nhắc đến (ii) và (iii). (c) Bài chưa định nghĩa hình thức mức hối tiếc của một cơ chế, tức \(U_{o,t}-U_{k,t}\) với \(k\notin M\). | Định nghĩa rõ \(R^{(k)}_{t}=\max_{m\in M}U_{m,t}-U_{k,t}\) cho mọi cơ chế \(k\). Nêu rõ \emph{M} dùng trong H\textsubscript{3} là tập nào, và nói rõ rằng \(R^{(k)}_{t}\) có thể âm với cả ba cơ chế.
63. [MAJOR] (A4 · Mathematical Errors #4) Chuẩn hóa \(D_{t}\) và \(R_{t}\), dòng 782–784 | Câu "chia \(D_{t}\) và \(R_{t}\) cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình" không xác định được một đại lượng duy nhất: với 7 mô hình có 21 cặp chênh lệch. Bài cũng không cho ký hiệu riêng cho đại lượng đã chuẩn hóa, nên không rõ \(Y_{t}\) trong (5) là \(D_{t}\) và \(R_{t}\) thô hay đã chuẩn hóa. | Định nghĩa một ký hiệu, ví dụ \(\tilde{R}_{t}=R_{t}/\widehat{se}_{t}\) với \(\widehat{se}_{t}\) được nêu rõ (trung bình các cặp, hoặc sai số chuẩn của \(U_{c,t}-U_{o,t}\)). Ghi rõ "Với \(Y_{t}\) là \(\tilde{D}_{t}\) hoặc \(\tilde{R}_{t}\)".
64. [MAJOR] (A4 · Mathematical Errors #5) Phương trình (1), dòng 754–760 | Tần suất của \(\mu_{m,t}\) và \(\sigma^{2}_{m,t}\) (ngày, tuần hay tháng) và việc có quy đổi về năm hay không đều chưa được nêu. Với cửa sổ đánh giá 6 tháng và tái cân bằng hằng tháng, nếu dùng lợi suất tháng thì phương sai chỉ tính trên 6 quan sát. Bài cũng không nói \(\mu\) là lợi suất thô hay lợi suất vượt trội. Câu "mức lợi suất phi rủi ro mà nhà đầu tư … coi là ngang giá" chỉ đúng khi \(\mu\) là lợi suất thô (không trừ lãi suất phi rủi ro). Thêm nữa, công thức \(\mu-\frac{\rho}{2}\sigma^{2}\) chỉ đúng chính xác với hữu dụng bậc hai hoặc với CARA kết hợp phân phối chuẩn; với trường hợp khác nó là xấp xỉ. | Ghi rõ: "\(\mu_{m,t}\), \(\sigma^{2}_{m,t}\) tính từ lợi suất [ngày] sau chi phí, quy đổi năm", và thêm "(xấp xỉ bậc hai của lợi suất tương đương chắc chắn)".
65. [MAJOR] (A4 · Notation Inconsistencies #1) \(t\) | Ở dòng 662, \(t\) là ngày ("xác suất lọc tại ngày \emph{t}"). Ở dòng 753–754, (1)–(5), \(t\) là cửa sổ đánh giá 6 tháng ("cửa sổ đánh giá kết thúc tại thời điểm \emph{t}"). Ngay trong định nghĩa \(S_{t}\) (dòng 824–826), hai nghĩa này chồng lên nhau, vì \(S_{t}\) tổng hợp xác suất theo ngày trong cửa sổ \(t\). | Dùng \(d\) cho ngày (\(\xi_{d}\) là xác suất lọc) và \(t\) cho cửa sổ, chẳng hạn \(S_{t}=\frac{1}{|W_t|}\sum_{d\in W_t}\mathbf{1}\{\xi_{d}>\kappa\}\).
66. [MAJOR] (A4 · Undefined Notation #1) Các thành phần của \(\gamma\) | H\textsubscript{2} được phát biểu theo "hệ số của độ phi thanh khoản" và "hệ số của tương quan đuôi" (dòng 856–858), nhưng (5) chỉ có véc-tơ \(\gamma\). Bài không gán ký hiệu cho các phần tử của \(X_{t}\) (Amihud, tương quan đuôi, tương quan hiệu chỉnh, độ phân tán chéo, biến động thực hiện) hay cho các hệ số tương ứng. | Viết tường minh \(\gamma'X_{t}=\gamma_{1}ILLIQ_{t}+\gamma_{2}TC_{t}+\gamma_{3}AC_{t}+\gamma_{4}CSAD_{t}+\gamma_{5}RV_{t}\) ngay sau (5), và phát biểu H\textsubscript{2} thành \(\gamma_{1}>0,\ \gamma_{2}<0\) và H\textsubscript{4} thành \(\gamma_{4}>0\).
67. [MAJOR] (A4 · Regression Specification Issues #1) Phương trình (5) so với Bảng 2 (H\textsubscript{1}) | Bảng 2 ghi biến kết quả cho H\textsubscript{1} là "Kết quả phụ: độ phân tán mô hình, kích thước tập tin cậy mô hình" (dòng 595). Nhưng (5) chỉ cho phép "\(Y_{t}\) là \(D_{t}\) hoặc \(R_{t}\)" (dòng 818), và dòng 786–788 nói kích thước tập tin cậy chỉ là "thước đo mô tả". | Bỏ kích thước tập tin cậy khỏi cột "Thước đo chính" cho H\textsubscript{1}, hoặc thêm nó làm \(Y_{t}\) trong (5).
68. [MAJOR] (A4 · Regression Specification Issues #2) Phương trình (5) so với Bảng 2 (H\textsubscript{4}) | Bảng 2 liệt kê "Độ phân tán chéo của lợi suất; thước đo bầy đàn" (dòng 610–611). Trong khi đó \(X_{t}\) (dòng 828–832) chỉ có độ phân tán chéo, không có thước đo bầy đàn riêng (chẳng hạn hệ số phi tuyến của Chang và cộng sự, 2000). | Hoặc thêm biến bầy đàn vào \(X_{t}\), hoặc xóa "thước đo bầy đàn" khỏi Bảng 2 và ghi rõ rằng CSAD chính là thước đo bầy đàn (như dòng 949–950).
69. [MAJOR] (A4 · Regression Specification Issues #3) Số bậc tự do và suy diễn | Khoảng 28 quan sát (dòng 794–795) được dùng để ước lượng 7 tham số: \(\alpha\), \(\beta\) và 5 biến trong \(X_{t}\). Hai biến tương quan (tương quan đuôi và tương quan hiệu chỉnh theo biến động) gần như chắc chắn đa cộng tuyến với nhau và với \(RV_{t}\). Bài lại đồng thời dùng hai cách suy diễn: "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" (dòng 817–818) và "bootstrap khối dừng … cho các hệ số hồi quy" (dòng 812–813). Bài không nói cách nào quyết định kết luận, và cũng không nêu độ dài khối hay bandwidth HAC trên 28 cửa sổ không chồng lấn. | Nêu rõ tiêu chí suy diễn chính (các điều kiện của H\textsubscript{1} và H\textsubscript{2} đang dùng khoảng tin cậy bootstrap). Giới hạn \(X_{t}\) theo từng giả thuyết, hoặc báo cáo từng kênh riêng cộng với \(RV_{t}\). Thảo luận công suất kiểm định với n ≈ 28.
70. [MAJOR] (A4 · Regression Specification Issues #4) Quy tắc khi hệ số phóng đại phương sai (VIF) > 5, dòng 855–856 | Câu "báo cáo hai phương trình tách riêng" không nói đó là hai phương trình nào (tách \(S_{t}\) khỏi \(X_{t}\)? hay tách hai nhóm kênh?). Vì vậy quy tắc ra quyết định của H\textsubscript{2} không xác định được khi VIF vượt ngưỡng. | Viết rõ hai đặc tả, ví dụ (5a) \(Y_{t}=\alpha+\beta S_{t}+\delta RV_{t}+\varepsilon_{t}\) và (5b) \(Y_{t}=\alpha+\gamma'X_{t}+\varepsilon_{t}\), và nói rõ H\textsubscript{2} được đánh giá trên đặc tả nào.
71. [MAJOR] (A5 · Tables with Missing or Incomplete Notes #4) Bảng 2 | Tiêu chí ủng hộ H\textsubscript{3} trong bảng mâu thuẫn với mục 4.3.8. Bảng ghi "cho mức hối tiếc và độ sụt giảm tối đa thấp hơn", tức đòi hỏi giảm thật sự. Mục 4.3.8 ghi "độ sụt giảm tối đa không cao hơn", tức chỉ cần không tăng. | Thống nhất một tiêu chí, ví dụ sửa bảng thành "độ sụt giảm tối đa không cao hơn", và thêm ghi chú "Quy tắc quyết định: xem mục 4.3.7–4.3.8".
72. [MAJOR] (A5 · Tables with Missing or Incomplete Notes #5) Bảng 2 | Kỳ vọng về dấu ở dòng H\textsubscript{2} có thể đọc theo hai nghĩa: "hệ số của tương quan đuôi âm (tương quan cao làm các danh mục chỉ mua hội tụ)". Có thể hiểu là "hệ số của [tương quan đuôi] mang dấu âm", hoặc là "hệ số của [tương quan ở đuôi âm]" (khái niệm đuôi âm theo Longin–Solnik). Thân bài (dòng 857–858) lặp lại đúng cụm từ này. | Viết lại thành "hệ số của tương quan đuôi mang dấu âm (β < 0)" và định nghĩa tương quan đuôi (ngưỡng đuôi, tần suất) trong ghi chú.
73. [MAJOR] (A5 · Tables with Missing or Incomplete Notes #6) Bảng 2 | Ghi chú chỉ có "Nguồn: Thí sinh đề xuất". Bảng thiếu ba thông tin cần để tự đứng được: (a) định nghĩa chế độ căng thẳng / S\textsubscript{t}; (b) đơn vị và tần suất của lợi suất tương đương chắc chắn và mức hối tiếc (theo năm hay theo tháng, %); (c) thủ tục suy luận: phân phối rỗng 1.000 lần bootstrap, khoảng tin cậy bootstrap khối, hiệu chỉnh Holm ở mức 10%, quy tắc "không kết luận" khi có dưới 10 cửa sổ căng thẳng độc lập. | Thêm ghi chú: "S\textsubscript{t}: tỷ lệ ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng đăng ký trước. CEQ, R\textsubscript{t}: % [theo năm], sau chi phí, ρ = 5. R\textsubscript{t} và D\textsubscript{t} trong phân tích chính được chia cho sai số chuẩn bootstrap. Suy luận: bootstrap khối; Holm 10% cho bốn giả thuyết; kết quả gọi là không kết luận khi có dưới 10 cửa sổ căng thẳng độc lập."
74. [MAJOR] (A5 · Tables with Missing or Incomplete Notes #11) Bảng 3 | Bảng định nghĩa tập *M* (|*M*| = 7) dùng cho các phương trình (2)–(4), nhưng không có ghi chú nào cho biết: (a) M\textsubscript{6} (Garlappi và cộng sự, 2007) trùng với cơ chế giảm thiểu (ii) và M\textsubscript{7} (Kritzman và cộng sự, 2012) trùng với cơ chế (iii); (b) "Khi kiểm định H\textsubscript{3}, đề tài loại cơ chế (ii) và (iii) khỏi *M*"; (c) phép kiểm định trên tập mô hình tĩnh {M\textsubscript{1}, M\textsubscript{2}, M\textsubscript{3}, M\textsubscript{4}, M\textsubscript{6}}; (d) kết quả được báo cáo cả khi có lẫn khi không có M\textsubscript{5}. | Thêm cột "Tĩnh / theo chế độ" và ghi chú: "M\textsubscript{6}, M\textsubscript{7} đồng thời là cơ chế (ii), (iii) và bị loại khỏi *M* khi kiểm định H\textsubscript{3}; kết quả báo cáo cả khi có lẫn khi không có M\textsubscript{5}."
75. [MAJOR] (A5 · Figures with Missing or Incomplete Notes #4) Hình 2 | Hình và văn bản cùng để ngỏ một chi tiết thiết kế then chốt. Hình vẽ mỗi cửa sổ thành một khối "Ước lượng: 104 tuần | Đánh giá: 6 tháng", nên người đọc hiểu là ước lượng một lần cho mỗi cửa sổ 6 tháng. Văn bản lại ghi "mô hình được chọn sau đó tái cân bằng hằng tháng trong suốt cửa sổ". Cả hai không cho biết mỗi tháng có ước lượng lại trên cửa sổ trượt 104 tuần hay không. Hình cũng không vẽ khoảng 36 tháng kết quả ngoài mẫu dùng để chọn mô hình *c*. Thời kỳ khởi động (mục 4.3.6 viết "mức hối tiếc chỉ tính được từ khoảng năm thứ năm của mẫu") cũng không có trên hình. | Vẽ thêm đoạn "36 tháng chọn mô hình" trước mỗi cửa sổ đánh giá, các mốc tái cân bằng hằng tháng, và ghi rõ có ước lượng lại hằng tháng hay không. Thêm ghi chú: "Cửa sổ đánh giá 6 tháng không chồng lấn; khoảng 28 cửa sổ cho giai đoạn 2007–2026; cửa sổ trượt hằng tháng chỉ dùng cho phân tích phụ."
76. [MAJOR] (A5 · Figures with Missing or Incomplete Notes #6) Hình 3 | Tôi không đọc được chữ của hình (khung #6 rỗng), và ghi chú chỉ có "Nguồn: Thí sinh đề xuất". Vì vậy không kiểm chứng được nhận định "Hình 3 tóm tắt năm bước của quy trình…" và "đăng ký trước kế hoạch phân tích trước khi ước lượng chính thức tập mô hình ở bước 3". | Thêm ghi chú liệt kê năm bước, đánh dấu mốc đăng ký trước (Quý 4 Năm 1), và ghi rằng bước ước lượng thử (Quý 2 Năm 1, giai đoạn 2019–2025) diễn ra trước mốc này. Đề nghị tác giả kiểm tra lại hình gốc.
77. [MAJOR] (A5 · Cross-Reference Issues #1) Hình 1 và Mục tiêu (iii) | Hình 1 và thân bài mâu thuẫn về vai trò của biến động. Hình 1 đặt biến động là biến kiểm soát ("Biến kênh | Biến động thực hiện (kiểm soát)"), và Câu hỏi 2 cùng H\textsubscript{2} cũng vậy ("Sau khi kiểm soát biến động thực hiện"; "Biến động thực hiện luôn có mặt trong X\textsubscript{t} với vai trò biến kiểm soát"). Nhưng mục tiêu (iii) lại xếp biến động vào nhóm biến kênh: "xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm biến động, thanh khoản, tương quan cực trị và bầy đàn". | Bỏ "biến động" khỏi danh sách biến kênh ở mục tiêu (iii), hoặc nói rõ đây là biến kiểm soát.
78. [MAJOR] (A5 · Cross-Reference Issues #2) Bảng 2 và mục 4.3.8 | Tiêu chí ủng hộ H\textsubscript{3} về độ sụt giảm tối đa không thống nhất: bảng ghi "thấp hơn", thân bài ghi "không cao hơn". Chi tiết ở phần Bảng 2 bên trên.
79. [MAJOR] (A5 · Cross-Reference Issues #3) Bảng 3 và mục 4.3.8 | Bảng 3 không đánh dấu rằng M\textsubscript{6} và M\textsubscript{7} trùng với cơ chế (ii) và (iii). Văn bản lại ghi "đề tài loại cơ chế (ii) và (iii) khỏi *M*", trong khi *M* được định nghĩa là "tập bảy mô hình ở Bảng 3". Người đọc sẽ không biết H\textsubscript{3} được kiểm định trên tập *M* nào (5 hay 7 mô hình).

**MINOR** (polish — improves paper quality):
80. [MINOR] (A3 · Generalization Issues #4) [4.1, dòng 338–341] | "Thị trường Việt Nam có thanh khoản hạn chế và chịu nhiều cú sốc trong một lịch sử giao dịch ngắn, nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển." | Đây là một tuyên bố so sánh mà thiết kế một quốc gia không kiểm định được, vì không có thị trường đối chứng. Đoạn "thanh khoản hạn chế" cũng không có nguồn trích. | Fix: thêm nguồn cho đặc điểm thanh khoản và đổi thành "có thể khác so với thị trường phát triển; đề tài không so sánh trực tiếp". Nếu muốn giữ tuyên bố so sánh thì cần thêm một chuẩn đối chiếu, ví dụ chạy cùng quy trình trên dữ liệu Mỹ.
81. [MINOR] (A3 · Generalization Issues #5) [4.2 (1), dòng 375–376] | "Mọi mô hình phân bổ đều mang sai số ở đầu vào." | Khái quát quá mức: quy tắc 1/N (M1) không ước lượng tham số nào. | Fix: "Mọi mô hình phân bổ dựa trên tham số ước lượng đều mang sai số ở đầu vào."
82. [MINOR] (A3 · Generalization Issues #6) [Bảng 2, cột "Cơ sở" của H1] | "Danielsson và cộng sự (2016); Hansen và cộng sự (2011)" | Danielsson và cộng sự (2016) cho thấy rủi ro mô hình tăng theo bất định đối với *mô hình dự báo rủi ro* (VaR, rủi ro hệ thống), không phải đối với quyết định phân bổ. Dùng làm cơ sở trực tiếp cho H1 là ngoại suy. | Fix: ghi rõ đây là cơ sở gián tiếp, được ngoại suy từ bối cảnh dự báo rủi ro.
83. [MINOR] (A3 · Generalization Issues #7) [4.1, dòng 309–313] | "Quỹ Tiền tệ Quốc tế ghi nhận thị trường trái phiếu doanh nghiệp đóng băng trong quý IV/2022 … Những cú sốc này là các giai đoạn tham chiếu" | Cú sốc trên thị trường trái phiếu doanh nghiệp được dùng làm giai đoạn tham chiếu cho chế độ căng thẳng trên thị trường cổ phiếu mà không có lập luận về sự lan truyền sang cổ phiếu HOSE. | Fix: thêm một câu, có nguồn, về diễn biến VN-Index trong giai đoạn đó, hoặc nói rõ đây là giai đoạn ứng viên cần kiểm tra.
84. [MINOR] (A3 · Minor Language Issues #1) [4.1, dòng 301] | "Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách." | Đây là khẳng định nhân quả không có dẫn chứng. Các nguồn theo sau (Reinhart–Rogoff; Laeven–Valencia về khủng hoảng ngân hàng) chỉ cho thấy khủng hoảng thường xảy ra, không cho thấy việc chọn mô hình quan trọng hơn trong khủng hoảng. | Fix: "Nếu thứ hạng của các mô hình thay đổi trong khủng hoảng, câu hỏi chọn mô hình càng quan trọng; khủng hoảng tài chính lại lặp lại thường xuyên (…)."
85. [MINOR] (A3 · Minor Language Issues #2) [4.1, dòng 307–308] | "Dao và cộng sự (2021) cho thấy số ca mắc COVID-19 hằng ngày tác động tiêu cực đến lợi suất cổ phiếu." | Đây là cách mô tả tài liệu bằng ngôn ngữ nhân quả cho một nghiên cứu hồi quy chuỗi thời gian. | Fix: "…cho thấy số ca mắc COVID-19 hằng ngày có liên hệ âm với lợi suất cổ phiếu."
86. [MINOR] (A3 · Minor Language Issues #3) [4.1, dòng 311–312] | "Vu và cộng sự (2024) cho thấy các đợt sụt giảm giá cổ phiếu giai đoạn 2007--2022 lan truyền giữa các ngành." | "Lan truyền" là một tuyên bố về sự lây nhiễm, trong khi chính đề cương (dòng 444–447, Forbes–Rigobon) lưu ý rằng bằng chứng lây nhiễm thường biến mất sau khi hiệu chỉnh theo biến động. | Fix: "…ghi nhận các đợt sụt giảm giá xảy ra đồng thời hoặc nối tiếp giữa các ngành."
87. [MINOR] (A3 · Minor Language Issues #4) [4.3.6, dòng 781–784] | "Để loại tác động cơ học này, phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap" | Chia cho sai số chuẩn chỉ loại được phần do thang đo. Giá trị kỳ vọng của max của các đại lượng có nhiễu còn phụ thuộc vào tương quan giữa các mô hình, mà tương quan này đổi theo chế độ. | Fix: "Để giảm tác động cơ học này…", và nói rõ phân phối rỗng ở 4.3.7 mới là công cụ chính để xử lý phần còn lại.
88. [MINOR] (A3 · Minor Language Issues #5) [4.3.7, dòng 835] | "Để tách rủi ro lựa chọn mô hình khỏi nhiễu ước lượng và biến động" | "Tách" là quá mạnh, vì phân phối rỗng chỉ loại bỏ chênh lệch trung bình theo chế độ dưới các giả định của bootstrap khối. | Fix: "Để đối chiếu β với mức kỳ vọng khi các mô hình ngang chất lượng…"
89. [MINOR] (A3 · Minor Language Issues #6) [4.3.6, dòng 794–795; 4.3.10, dòng 906–907] | "khoảng 28 cửa sổ đánh giá độc lập"; "số cửa sổ độc lập ở chế độ căng thẳng" | Cửa sổ không chồng lấn không có nghĩa là độc lập. Chế độ có tính bền, và cửa sổ chọn 36 tháng của các cửa sổ liền kề chồng lên nhau, nên các cửa sổ căng thẳng tập trung thành cụm. | Fix: dùng "không chồng lấn", và báo cáo số giai đoạn căng thẳng *riêng biệt* làm đơn vị đếm hiệu dụng.
90. [MINOR] (A3 · Minor Language Issues #7) [4.3.4, dòng 663] | "cách làm này loại thiên lệch nhìn trước" | Cửa sổ mở rộng loại được thiên lệch nhìn trước trong tham số, nhưng lựa chọn họ mô hình và định nghĩa chế độ được đưa ra sau khi thí sinh đã thấy dữ liệu 2019–2025 (dòng 728–730), và định nghĩa thay thế "theo ngưỡng sụt giảm" có thể dùng thông tin hậu nghiệm. | Fix: "giảm thiên lệch nhìn trước trong ước lượng tham số".
91. [MINOR] (A3 · Minor Language Issues #8) [4.3.1, dòng 540–541] | "giải thích vì sao các mô hình cho trọng số khác nhau ngay cả khi dùng cùng dữ liệu" | Khác biệt trọng số chủ yếu đến từ mục tiêu, cấu trúc và tiên nghiệm khác nhau của các mô hình. Sai số ước lượng chỉ là một phần nguyên nhân. | Fix: "giải thích một phần vì sao…"
92. [MINOR] (A3 · Minor Language Issues #9) [Bảng 2 H2 và 4.3.7, dòng 857] | "hệ số của tương quan đuôi âm" | Cụm này đọc được theo hai nghĩa: "hệ số âm của tương quan đuôi" hoặc "hệ số của tương quan ở đuôi âm". Hai cách đọc dẫn đến dấu dự đoán khác nhau. | Fix: "hệ số của tương quan ở đuôi âm mang dấu âm".
93. [MINOR] (A3 · Minor Language Issues #10) [4.1, dòng 324–326] | "lần đầu thiết lập khuôn khổ quản lý rủi ro mô hình cho các ngân hàng" | Đây là tuyên bố "lần đầu" về văn bản quy phạm và chưa được kiểm chứng. Nội dung và ngày tháng của SR 26-2 (dòng 317–318) cũng cần đối chiếu với văn bản gốc. | Fix: tác giả xác nhận với văn bản gốc, hoặc viết "thiết lập khuôn khổ…" mà bỏ "lần đầu".
94. [MINOR] (A3 · Minor Language Issues #11) [4.4, dòng 971–972] | "Về lý thuyết, đề tài đưa ra khung khái niệm và thước đo rủi ro lựa chọn mô hình" | Mức hối tiếc là một khái niệm chuẩn trong lý thuyết quyết định. Gọi đây là đóng góp lý thuyết là cách nói quá. | Fix: "Về khái niệm và đo lường, đề tài đề xuất cách vận dụng mức hối tiếc để đo rủi ro lựa chọn mô hình theo chế độ cho quyết định phân bổ danh mục."
95. [MINOR] (A3 · Minor Language Issues #12) [4.2 (3), dòng 418–419] | "kết hợp dự báo bù được phần chất lượng dự báo mất đi do mô hình bất ổn định" | Cơ chế được gán cho Rapach và cộng sự (2010) dưới dạng khẳng định. | Fix: "…cho thấy kết hợp dự báo cải thiện hiệu quả ngoài mẫu, điều họ lý giải bằng việc giảm tác động của bất ổn định mô hình."
96. [MINOR] (A1 · Minor Issues #10) Dòng 104 | "Đại học Kinh tế Quốc Dân" → "Trường Đại học Kinh tế Quốc dân" | Viết hoa sai, không thống nhất với dòng 1312 và 1365.
97. [MINOR] (A1 · Minor Issues #11) Dòng 1213 và 1219 | "(Nguyễn và Nguyễn, 2026b)" nhưng "(Nguyen và Nguyen, 2026a)" | Cùng một nhóm tác giả mà trích dẫn khi có dấu, khi không dấu, nên người đọc dễ tưởng là hai nhóm khác nhau. Nên thống nhất, chẳng hạn trích tác giả Việt bằng họ tên đầy đủ có dấu theo quy ước trích dẫn tiếng Việt.
98. [MINOR] (A1 · Minor Issues #12) Dòng 982 (tiêu đề 4.5) so với dòng 1001 | "đến 3 chữ số" so với "(đến ba chữ số)" | Không thống nhất cách viết số. Nếu tiêu đề do mẫu của trường quy định thì sửa tiêu đề cột trong bảng.
99. [MINOR] (A1 · Minor Issues #13) Dòng 1233 so với 1299 | "chín bản thảo" so với "cả 9 bản thảo" → dùng thống nhất một cách viết.
100. [MINOR] (A1 · Minor Issues #14) Dòng 791 | "cửa sổ 6 tháng" (trong khi dòng 639 viết "ba tháng") → "cửa sổ sáu tháng".
101. [MINOR] (A1 · Minor Issues #15) Dòng 793–794 | "chỉ tính được từ khoảng năm thứ năm của mẫu" → "chỉ tính được từ khoảng năm thứ 5 của mẫu" hoặc "sau khoảng bốn năm đầu của mẫu" | Lặp "năm ... năm" nên khó đọc.
102. [MINOR] (A1 · Minor Issues #16) Dòng 309, 649 so với 732, 920, 925 và Bảng 5 | "quý IV/2022" so với "quý 4 năm thứ nhất", "quý 1" → thống nhất cách đánh số quý (số La Mã hoặc số Ả Rập).
103. [MINOR] (A1 · Minor Issues #17) Dòng 1314 | "từ tháng 07/2026" → "từ tháng 7/2026".
104. [MINOR] (A1 · Minor Issues #18) Dòng 1353–1354 | dấu ngoặc kép thẳng "chính sách tài khóa, ..." → dùng ``...'' như ở dòng 1180 | Trong LaTeX, dấu " thẳng in ra sai kiểu ngoặc.
105. [MINOR] (A1 · Minor Issues #19) Dòng 1213, 1271, 1381 | "Tạp chí Kinh tế - Luật và Ngân hàng" → "Kinh tế – Luật và Ngân hàng" (gạch ngang en, `--`) | Gạch nối có khoảng trắng hai bên dùng sai chức năng.
106. [MINOR] (A1 · Minor Issues #20) Dòng 274, 376, 384, 420, 703, 869 | "trung bình-phương sai" → "trung bình–phương sai" (en dash) | Gạch nối nối hai cụm nhiều âm tiết làm câu đọc thành "trung bình-phương / sai". Tương tự, tên ghép của hai người nên dùng en dash: "Black–Litterman", "Bai–Perron", "Moore–Penrose" (dòng 466, 726, 924, 1324).
107. [MINOR] (A1 · Minor Issues #21) Dòng 466 | "mô hình tự hồi quy trung bình trượt tích hợp" → "mô hình tự hồi quy tích hợp trung bình trượt (ARIMA)" | Thứ tự thành tố chưa đúng với ARIMA. Nên kèm từ viết tắt.
108. [MINOR] (A1 · Minor Issues #22) Dòng 725–726 | "nghịch đảo giả Moore-Penrose" → "giả nghịch đảo Moore–Penrose" | Dùng thuật ngữ chuẩn.
109. [MINOR] (A1 · Minor Issues #23) Dòng 427 và 814 | "tỷ số Sharpe hiệu chỉnh" (cho deflated Sharpe ratio) → "tỷ số Sharpe giảm phát (deflated Sharpe ratio)" | "hiệu chỉnh" dễ nhầm với "adjusted Sharpe ratio", vốn là một chỉ tiêu khác.
110. [MINOR] (A1 · Minor Issues #24) Dòng 385 | "nhà đầu tư né tránh mơ hồ" → "nhà đầu tư ngại mơ hồ" | Nên dùng song song với "ngại rủi ro" ở dòng 746.
111. [MINOR] (A1 · Minor Issues #25) Dòng 828 | "véc-tơ" → "vectơ" | Đây là chính tả phổ biến trong văn bản toán–kinh tế lượng tiếng Việt.
112. [MINOR] (A1 · Minor Issues #26) Dòng 732 | "ở chế độ khóa có dấu thời gian" → "ở dạng khóa có dấu thời gian" | "chế độ" là thuật ngữ trung tâm (regime). Dùng từ này cho "locked mode" gây trùng nghĩa.
113. [MINOR] (A1 · Minor Issues #27) Dòng 290 so với 879 | "tổn thất kỳ vọng" (định nghĩa rủi ro lựa chọn mô hình) so với "giá trị thiệt hại kỳ vọng mức 95%" (expected shortfall) → nên ghi "tổn thất kỳ vọng vượt ngưỡng (ES) mức 95%" và giữ "tổn thất kỳ vọng" cho một nghĩa duy nhất.
114. [MINOR] (A1 · Minor Issues #28) Dòng 467 | "trên 468 tuần" → "với 468 quan sát tuần" | "trên" có thể hiểu là "hơn 468".
115. [MINOR] (A1 · Minor Issues #29) Dòng 468 | "lợi nhuận cao hơn" → "lợi suất cao hơn" | Toàn văn dùng "lợi suất".
116. [MINOR] (A1 · Minor Issues #30) Dòng 389–391 | "nhóm tài liệu này chưa trả lời nhà đầu tư nên chọn mô hình nào" → "chưa trả lời câu hỏi nhà đầu tư nên chọn mô hình nào".
117. [MINOR] (A1 · Minor Issues #31) Dòng 416–417 | "thu được hiệu quả ngoài mẫu tốt hơn việc dùng tiêu chí để chọn một mô hình" → "tốt hơn so với khi dùng tiêu chí để chọn một mô hình".
118. [MINOR] (A1 · Minor Issues #32) Dòng 440–442 | "Tu (2010) ước tính nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất ..." → "Tu (2010) ước tính rằng nhà đầu tư nào bỏ qua chuyển chế độ sẽ chịu tổn thất ..." | Câu hiện tại dễ đọc nhầm, phải đọc lại.
119. [MINOR] (A1 · Minor Issues #33) Dòng 458 | "Vì bằng chứng trái chiều giữa các thị trường" → "Vì bằng chứng giữa các thị trường còn trái chiều" | Mệnh đề thiếu vị ngữ.
120. [MINOR] (A1 · Minor Issues #34) Dòng 451 | "đặt nền móng cho lý thuyết triển vọng" → "đề xuất lý thuyết triển vọng".
121. [MINOR] (A1 · Minor Issues #35) Dòng 402 | "nhỏ khi thị trường yên ắng" → "nhỏ khi thị trường ổn định" | "yên ắng" là từ khẩu ngữ.
122. [MINOR] (A1 · Minor Issues #36) Dòng 419 | "do mô hình bất ổn định" → "do mô hình không ổn định".
123. [MINOR] (A1 · Minor Issues #37) Dòng 518–523 | Hai câu liên tiếp cùng khẳng định "chưa công trình nào đo rủi ro ... theo chế độ thị trường" → gộp thành một câu và giữ phần "theo hiểu biết của thí sinh".
124. [MINOR] (A1 · Minor Issues #38) Dòng 327–330 | "Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này, cùng mức độ họ dùng mô hình định lượng để phân bổ danh mục, từ báo cáo của cơ quan quản lý và tài liệu ..." → "Dựa trên báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ, thí sinh sẽ xác định (i) khung quy định áp dụng cho nhóm tổ chức này và (ii) mức độ họ dùng mô hình định lượng để phân bổ danh mục." | Câu hiện tại lồng nhiều mệnh đề, khó theo dõi.
125. [MINOR] (A1 · Minor Issues #39) Dòng 273–274 | "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê. Mô hình gốc của lĩnh vực này..." → "Các tổ chức đầu tư thường phân bổ vốn dựa trên mô hình thống kê. Mô hình gốc của quản trị danh mục là..." | Câu mở đầu khái quát quá mức. "lĩnh vực này" chưa có từ nào để quy chiếu.
126. [MINOR] (A1 · Minor Issues #40) Dòng 647 | "bao trùm khủng hoảng tài chính toàn cầu" → "bao gồm".
127. [MINOR] (A1 · Minor Issues #41) Dòng 746 | "coi là ngang giá với danh mục" → "coi là tương đương với danh mục".
128. [MINOR] (A1 · Minor Issues #42) Dòng 748 | "danh mục biến động hơn" → "danh mục biến động mạnh hơn".
129. [MINOR] (A1 · Minor Issues #43) Dòng 798 | "thí sinh sẽ biện minh chúng" → "thí sinh sẽ giải trình cơ sở lựa chọn chúng" | "biện minh" mang sắc thái bào chữa.
130. [MINOR] (A1 · Minor Issues #44) Dòng 866–871 | "Cơ chế (i) kết hợp các mô hình ..." trong khi "Cơ chế (ii) là ...", "Cơ chế (iii) là ..." → "Cơ chế (i) là kết hợp mô hình ..." | Các vế song song chưa cùng cấu trúc.
131. [MINOR] (A1 · Minor Issues #45) Dòng 895 | "Thí sinh đăng ký trước kế hoạch phân tích trước khi ước lượng ..." và dòng 1166–1167 "trước khi đăng ký trước" → "Thí sinh đăng ký kế hoạch phân tích trước khi ước lượng ..." | Lặp "trước".
132. [MINOR] (A1 · Minor Issues #46) Dòng 906 | "Cạnh mỗi hệ số" → "Kèm theo mỗi hệ số".
133. [MINOR] (A1 · Minor Issues #47) Dòng 925 | "một bản thảo đang gửi tạp chí" → "một bản thảo đã gửi tạp chí".
134. [MINOR] (A1 · Minor Issues #48) Dòng 946–947 | "danh mục chỉ mua (không bán khống) là cấu hình cơ sở, các ràng buộc khác nằm trong kiểm tra độ bền" → thay dấu phẩy bằng dấu chấm phẩy | Hai mệnh đề độc lập nối bằng dấu phẩy (comma splice).
135. [MINOR] (A1 · Minor Issues #49) Dòng 957–958 | "Dựa trên phần tóm tắt của các công trình gần nhất, đề tài khác chúng ở bốn điểm." → "Đối chiếu với phần tóm tắt của các công trình gần nhất, đề tài khác chúng ở bốn điểm." | Trạng ngữ "dựa trên ..." không gắn được với chủ ngữ "đề tài" (dangling modifier).
136. [MINOR] (A1 · Minor Issues #50) Dòng 965–966 | "mở mẫu về trước năm 2019" → "mở rộng mẫu về trước năm 2019".
137. [MINOR] (A1 · Minor Issues #51) Dòng 738 và Bảng 4 dòng 1024–1025 | "là lệch khỏi kế hoạch" / "các lệch khỏi kế hoạch" → "là sai lệch so với kế hoạch" / "các sai lệch so với kế hoạch" | Thiếu danh từ trung tâm.
138. [MINOR] (A1 · Minor Issues #52) Dòng 1168–1169 | "áp dụng quy tắc gọi kết quả là không kết luận đã đăng ký" → "áp dụng quy tắc đã đăng ký trước về việc gọi kết quả là chưa đủ cơ sở kết luận" | Cụm "đã đăng ký" chưa rõ bổ nghĩa cho "quy tắc" hay "kết quả".
139. [MINOR] (A1 · Minor Issues #53) Bảng 5, dòng 1148 | "đo thời gian tính" → "đo thời gian tính toán".
140. [MINOR] (A1 · Minor Issues #54) Dòng 1051–1053 | "có tính liên ngành và tập trung vào kinh tế hành vi và quản lý trong lĩnh vực kinh tế, còn đề tài ..." → giảm bớt các chữ "và" và lặp "kinh tế".
141. [MINOR] (A1 · Minor Issues #55) Dòng 1054–1055 | "chương trình giảng dạy bằng tiếng Anh hoặc tiếng Việt, thuận lợi cho công bố quốc tế" → "chương trình có thể học bằng tiếng Anh, thuận lợi cho công bố quốc tế" | Như hiện tại, câu ngầm nói học bằng tiếng Việt cũng thuận lợi cho công bố quốc tế.
142. [MINOR] (A1 · Minor Issues #56) Dòng 1325–1326 | "Bản thảo về tương quan ... chuẩn bị cho kênh tương quan" → "Bản thảo ... giúp thí sinh chuẩn bị công cụ cho kênh tương quan" | Chủ ngữ bất động vật đứng với động từ hành động.
143. [MINOR] (A1 · Minor Issues #57) Dòng 1360 | "trùng với ba cấu phần của đề tài" → "phù hợp với ba cấu phần của đề tài".
144. [MINOR] (A1 · Minor Issues #58) Dòng 941–955 | Dùng "+" làm dấu đầu dòng → dùng "-" hoặc danh sách LaTeX | Văn bản hành chính học thuật tiếng Việt thường dùng gạch đầu dòng.
145. [MINOR] (A1 · Minor Issues #59) Tên bài tiếng Anh, Bảng 6 dòng 1216–1218 và tài liệu tham khảo dòng 1555–1557 | "using regime switching CAPM ... period 2019 - 2025" → "using regime-switching CAPM ... over the period 2019–2025" | Tính từ ghép đứng trước danh từ cần gạch nối; khoảng năm cần en dash. Ghi chú dòng 1230–1231 nói tên bài "giữ nguyên như khi công bố". Nếu đó đúng là tên chính thức thì giữ nguyên, nhưng nên kiểm tra lại.
146. [MINOR] (A1 · Minor Issues #60) Bảng 7, dòng 1276 | "Corporate Brownwashing and Firm Valuation in ASEAN-5 Disclosure Regimes" (viết hoa kiểu Title Case) → "Corporate brownwashing and firm valuation in ASEAN-5 disclosure regimes" | Các tên bài khác trong Bảng 6 và 7 đều viết hoa kiểu câu. Đây là bản thảo chưa công bố nên có thể sửa.
147. [MINOR] (A1 · Minor Issues #61) Tài liệu tham khảo dòng 1536–1538 | Lo và Mueller (2010) ghi "8(2)." nhưng thiếu số trang → bổ sung số trang (pp. 13–63) để thống nhất với các mục khác.
148. [MINOR] (A1 · Minor Issues #62) Tài liệu tham khảo dòng 1404–1405 | "Correcting for selection bias, backtest overfitting and non-normality" → "..., backtest overfitting, and non-normality" | Tên gốc của bài có dấu phẩy Oxford.
149. [MINOR] (A1 · Style Patterns to Fix Throughout #4) Động từ rút gọn mang màu khẩu ngữ. Ví dụ: "thấy" thay cho "nhận thấy/cho thấy" ("Bessler và cộng sự (2017) thấy", dòng 383), "loại" thay cho "loại bỏ" ("cách làm này loại thiên lệch nhìn trước", dòng 663), "thay" thay cho "thay thế" (dòng 323), "đổi theo" thay cho "thay đổi theo" (dòng 447–448), "vượt" thay cho "vượt trội so với" (dòng 280, 384, 387, 421). Cách sửa: dùng dạng đầy đủ trong văn phong học thuật. Riêng "thấy" xuất hiện 14 lần trong mục 4.1–4.3.
150. [MINOR] (A1 · Style Patterns to Fix Throughout #5) Calque "không kết luận" (inconclusive). Ví dụ: "quy tắc gọi một kết quả là không kết luận" (dòng 736). Cụm này còn xuất hiện ở dòng 908, 1070, 1168. Cách sửa: dùng "chưa đủ cơ sở kết luận" và viết thống nhất ở mọi chỗ.
151. [MINOR] (A1 · Style Patterns to Fix Throughout #6) So sánh thiếu "so với". Ví dụ: "Rủi ro lựa chọn mô hình ở chế độ căng thẳng cao hơn ở chế độ bình thường" (Bảng 2, H₁, dòng 592–593). Cách sửa: thêm "so với" trong mọi phép so sánh "X ở A cao/lớn hơn ở B", nhất là chỗ so sánh có thể đọc thành ngược nghĩa (Critical Issue 1).
152. [MINOR] (A1 · Style Patterns to Fix Throughout #7) Cách viết số. Chưa có quy tắc nhất quán cho số dưới 10 trong lời văn: "ba tháng" và "6 tháng", "chín bản thảo" và "9 bản thảo", "ba chữ số" và "3 chữ số". Riêng "9 tín chỉ" (dòng 1060, 1088, 1146) được viết bằng số một cách nhất quán. Cách sửa: viết bằng chữ các số từ một đến chín trong lời văn. Giữ chữ số cho giá trị tham số (ρ = 3, 5, 10; ngưỡng 5), số tín chỉ, phần trăm và số trong bảng. Phần trăm ("10%", "95%"), dấu thập phân ("0,5", "3,41/4"), dấu phân cách hàng nghìn ("1.000") và định dạng ngày DD/MM/YYYY đều đã nhất quán theo chuẩn tiếng Việt, không cần sửa.
153. [MINOR] (A1 · Style Patterns to Fix Throughout #8) Dấu gạch. Gạch nối "-" đang được dùng ở những chỗ cần en dash: các cặp khái niệm ("trung bình-phương sai"), tên hai người ("Black-Litterman", "Bai-Perron", "Moore-Penrose"), và tên tạp chí có khoảng trắng ("Kinh tế - Luật"). Khoảng năm thì đã dùng `--` đúng ("2005--2015"). Cách sửa: dùng `--` cho các trường hợp trên. Giữ gạch nối thường cho các mã như "SR 11-7", "VN-Index", "ASEAN-5".
154. [MINOR] (A1 · Style Patterns to Fix Throughout #9) Phân biệt "long-run/long run" và "high-income/high income" (tính từ ghép trước danh từ): không áp dụng cho văn xuôi tiếng Việt. Quy tắc này chỉ áp dụng cho các tên bài tiếng Anh (xem Minor Issue 59).
155. [MINOR] (A1 · Style Patterns to Fix Throughout #10) Câu bị động "được/bị ... bởi": không thấy cấu trúc "bởi". Các chỗ dùng "được" ("H₁ được ủng hộ", "mô hình được chọn") đều tự nhiên. Chỉ cần sửa câu "chưa thể bị loại là kém hơn" (Minor Issue 9).
156. [MINOR] (A1 · Style Patterns to Fix Throughout #11) Từ đệm và trùng ngữ (tương đương "interestingly", "notably", "very unique"): không phát hiện trong phần nội dung chính. Cũng không có câu "This paper contributes..." kiểu kể lể. Mục "Đóng góp dự kiến" là mục bắt buộc của mẫu đề cương và đã chỉ ra khác biệt cụ thể so với từng công trình.
157. [MINOR] (A2 · Terminology Drift #4) "Độ phân tán" | Cùng một từ chỉ hai đại lượng khác nhau: D_t, tức "độ phân tán mô hình" ở phương trình (3), và "độ phân tán chéo của lợi suất" ở H4. Đề xuất: luôn gọi đầy đủ "độ phân tán mô hình" và "độ phân tán chéo lợi suất", hoặc dùng ký hiệu riêng cho đại lượng thứ hai.
158. [MINOR] (A2 · Terminology Drift #5) Ký hiệu *M* | |M| = 7 ở 4.3.6, nhưng tập này bị đổi ở hai chỗ khác mà không có ký hiệu mới:
     - tập mô hình tĩnh ở 4.3.7 (M₁, M₂, M₃, M₄, M₆);
     - ở 4.3.8, "đề tài loại cơ chế (ii) và (iii) khỏi *M*", tức bỏ M₆ và M₇.

     Đề xuất: đặt ký hiệu riêng, ví dụ M^tĩnh và M^H3.
159. [MINOR] (A2 · Terminology Drift #6) "Bầy đàn" vs "phân tán chéo" | Bảng 4 (mục 5.3) và Hình 1 ("Phân tán chéo (thăm dò)") dùng hai tên cho cùng một kênh. Phần này gắn với vấn đề hướng tác động nêu ở mục Critical 5.
160. [MINOR] (A2 · Terminology Drift #7) Tên tác giả trong cặp trích dẫn 2026a/2026b viết không thống nhất:
     - Bảng 6 hàng 1 và tài liệu tiếng Việt: "Nguyễn và Nguyễn, 2026b" / "Nguyễn Thanh Bình, Nguyễn Văn Trung (2026b)";
     - các chỗ khác: "Nguyen và Nguyen (2026a)" / "Nguyen, T. B., Nguyen, V. T. (2026a)".

     Hậu tố a/b chỉ có nghĩa khi tên tác giả viết giống hệt nhau, nên cần thống nhất một cách viết.
161. [MINOR] (A2 · Minor Inconsistencies #1) 4.3.6, "mức hối tiếc chỉ tính được từ khoảng **năm thứ năm** của mẫu" ↔ chính các số liệu đi kèm | Cửa sổ ước lượng 104 tuần (2 năm) cộng 36 tháng kết quả ngoài mẫu (3 năm) bằng 5 năm đã trôi qua, nên mức hối tiếc chỉ bắt đầu từ năm thứ **sáu** (khoảng 2012 nếu mẫu bắt đầu năm 2007). Con số "khoảng 28 cửa sổ" khớp với mốc 2012 đến khoảng giữa năm 2026, không khớp với mốc "năm thứ năm" (sẽ cho khoảng 30–32 cửa sổ).
162. [MINOR] (A2 · Minor Inconsistencies #2) Bảng 2 (H1, "Kết quả phụ: … kích thước tập tin cậy mô hình") ↔ 4.3.6 ↔ 4.3.7 | Mục 4.3.6 nói chỉ "báo cáo kích thước tập như một thước đo mô tả", và tiêu chí ủng hộ H1 ở 4.3.7 không dùng đại lượng này. Vì vậy không nên xếp nó vào cột thước đo của H1.
163. [MINOR] (A2 · Minor Inconsistencies #3) 4.3.7 (VIF > 5 thì "báo cáo hai phương trình tách riêng và **không diễn giải riêng từng hệ số**") ↔ tiêu chí H2 | H2 được ủng hộ dựa trên dấu và khoảng tin cậy của **từng** hệ số, nên khi VIF vượt ngưỡng thì không rõ H2 được đánh giá thế nào.
164. [MINOR] (A2 · Minor Inconsistencies #4) 4.3.6 ↔ 4.3.7 | Tỷ số Sharpe được nói chỉ là "thước đo phụ, ở các cửa sổ có lợi suất vượt trội trung bình dương", tức loại phần lớn các cửa sổ căng thẳng. Nhưng thiên lệch chọn lọc lại được hiệu chỉnh "bằng tỷ số Sharpe hiệu chỉnh", trong khi việc chọn mô hình dựa trên lợi suất tương đương chắc chắn.
165. [MINOR] (A2 · Minor Inconsistencies #5) 4.3.8 ("loại cơ chế (ii) và (iii) khỏi *M*, nên mức hối tiếc của hai cơ chế này có thể âm") ↔ cơ chế (i) | Danh mục kết hợp ở cơ chế (i) cũng không thuộc *M*, nên mức hối tiếc của nó cũng có thể âm, nhưng văn bản không nói.
166. [MINOR] (A2 · Minor Inconsistencies #6) Câu hỏi 3 ("Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?") ↔ H3 ("**Ở chế độ căng thẳng**, sau chi phí giao dịch…") | Câu hỏi không giới hạn theo chế độ, còn giả thuyết thì có.
167. [MINOR] (A2 · Minor Inconsistencies #7) 4.3.4/4.3.6 ↔ 4.3.3 | Ngưỡng của M3 ("tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5") không bao giờ có hiệu lực ở cấu hình cơ sở, vì 30/104 ≈ 0,29. Ngưỡng này chỉ có tác dụng trong kiểm tra độ bền "dùng dữ liệu tháng", nhưng ở đó tỷ lệ được định nghĩa theo "quan sát tuần" nên không áp dụng trực tiếp được.
168. [MINOR] (A2 · Minor Inconsistencies #8) Bảng 1 (4 khoảng trống, gồm "(4)… bầy đàn") ↔ "Đóng góp dự kiến" ở 4.4 ("khác chúng ở bốn điểm") | Bốn điểm đóng góp không trùng với bốn khoảng trống: đóng góp có bài báo của chính thí sinh nhưng không có khoảng trống về bầy đàn.
169. [MINOR] (A2 · Minor Inconsistencies #9) Mục 5 ("đề tài nằm ở giao điểm của tài chính định lượng, quản lý và **tài chính hành vi**") ↔ 4.4 ("giao thoa với kinh tế hành vi ở **một phép thử giới hạn**") ↔ H4 "(thăm dò)" | Mục 5 nói thành phần hành vi mạnh hơn mức mà phần thiết kế thể hiện.
170. [MINOR] (A2 · Minor Inconsistencies #10) Mục 4.5 ("Ngoài phần mở đầu, kết luận…, luận án dự kiến gồm sáu chương") ↔ Bảng 4 | Chương 1 "Giới thiệu nghiên cứu" trùng chức năng với "phần mở đầu".
171. [MINOR] (A2 · Minor Inconsistencies #11) Viết hoa không thống nhất: trang bìa "Đại học Kinh tế Quốc **D**ân" ↔ mục 8.2 và mục 10 "Kinh tế Quốc **d**ân".
172. [MINOR] (A2 · Minor Inconsistencies #12) Cách diễn giải tài liệu được trích:
      - Kerkhof và cộng sự (2010) được tóm tắt là chỉ tách thành "rủi ro ước lượng và rủi ro đặc tả sai". Bài gốc có thêm thành phần thứ ba (rủi ro nhận dạng), nên cách tóm tắt chưa đầy đủ.
      - Khẳng định Thông tư 83/2025/TT-NHNN "**lần đầu** thiết lập khuôn khổ quản lý rủi ro mô hình" là một nhận định mạnh. Tài liệu tham khảo chỉ cho thấy đây là thông tư về "hệ thống kiểm soát nội bộ", nên chi tiết này cần được đối chiếu.
173. [MINOR] (A2 · Minor Inconsistencies #13) Mục 5 dẫn "Thông báo tuyển sinh năm 2026" và "Phụ lục 1 của Thông báo" làm căn cứ, nhưng văn bản này không có trong danh mục tài liệu tham khảo.
174. [MINOR] (A4 · Mathematical Errors #6) Đếm số cửa sổ, dòng 792–795 | Ước lượng cần 104 tuần (2 năm) và việc chọn mô hình cần 36 tháng (3 năm), tổng cộng 5 năm. Mức hối tiếc vì thế tính được *từ đầu năm thứ sáu*, không phải "từ khoảng năm thứ năm". Con số "khoảng 28 cửa sổ" thì khớp (2012–2026 xấp xỉ 14–14,5 năm, tức 28–29 cửa sổ 6 tháng). | Sửa thành "sau năm thứ năm" hoặc "từ năm thứ sáu".
175. [MINOR] (A4 · Mathematical Errors #7) Điều kiện cho M\textsubscript{3}, dòng 723–726 | Với rổ cố định N = 30 và cửa sổ T = 104 tuần, tỷ lệ là 30/104 ≈ 0,29, luôn nhỏ hơn 0,5, nên ở cấu hình cơ sở điều kiện này không bao giờ xảy ra. Ngoài ra, khi 0,5 < N/T < 1 thì ma trận hiệp phương sai mẫu vẫn khả nghịch. Nghịch đảo giả Moore-Penrose chỉ thực sự cần khi N ≥ T, nên nó không xử lý vấn đề "ước lượng kém" ở ngưỡng 0,5. | Nói rõ ngưỡng này chỉ có tác dụng trong kiểm tra độ bền dùng dữ liệu tháng (24 tháng cho 30 mã, N/T > 1). Nếu ý đồ là xử lý điều kiện kém thì nên dùng ngưỡng N/T ≥ 1 cho nghịch đảo giả, hoặc dùng co rút.
176. [MINOR] (A4 · Mathematical Errors #8) Định nghĩa chế độ căng thẳng, dòng 665–666 | "Chế độ căng thẳng là chế độ có phương sai điều kiện cao nhất và lợi suất kỳ vọng thấp hơn chế độ bình thường." Định nghĩa này bỏ ngỏ trường hợp chế độ có phương sai cao nhất lại không có lợi suất thấp hơn. Khi có ba chế độ, "chế độ bình thường" cũng không xác định (là một chế độ hay gộp hai chế độ còn lại). | Đặt quy tắc ưu tiên (chọn theo phương sai) và nói rõ "bình thường" là phần bù của chế độ căng thẳng.
177. [MINOR] (A4 · Notation Inconsistencies #2) \(M\) / M\textsubscript{k} | \emph{M} là tập mô hình (dòng 752), còn M\textsubscript{1}…M\textsubscript{7} là từng mô hình (Bảng 3). Chữ chỉ số mô hình trong các phương trình là \(m\). Cùng một chữ cái vừa chỉ tập hợp, vừa chỉ phần tử. | Dùng \(\mathcal{M}\) cho tập hợp, hoặc đổi nhãn mô hình thành \(m=1,\dots,7\).
178. [MINOR] (A4 · Notation Inconsistencies #3) \(c\) và \(o\) trong (4) | \(c\) là một mô hình nhưng phụ thuộc vào thời điểm chọn, vì mỗi cửa sổ chọn lại. \(o\) không phải một chỉ số mô hình cố định, mà "giá trị cao nhất trong \emph{M}". | Viết \(R_{t}=\max_{m\in M}U_{m,t}-U_{c_t,t}\), với \(c_t=\arg\max_{m}\widehat{CE}^{36}_{m,t}\).
179. [MINOR] (A4 · Notation Inconsistencies #4) \(\beta\), \(\beta_{0}\), \(\beta_{1}\) | \(\beta_{0}\) thường được hiểu là hệ số chặn. Ở đây hệ số chặn là \(\alpha\), còn \(\beta_{0}\) và \(\beta_{1}\) là \(\beta\) của hai đặc tả khác nhau. Ký hiệu này dễ gây nhầm. | Dùng \(\beta^{\text{(không kênh)}}\) và \(\beta^{\text{(có kênh)}}\), hoặc \(\beta^{R}\) và \(\beta^{F}\).
180. [MINOR] (A4 · Notation Inconsistencies #5) Cách viết \(|M|\) | Trong văn bản là \texttt{\textbackslash textbar\{\}\textbackslash emph\{M\}\textbackslash textbar\{\}} (dòng 753), còn trong phương trình là \(|M|\). | Thống nhất dùng `\(|M|=7\)`.
181. [MINOR] (A4 · Notation Inconsistencies #6) Vai trò của \(D_{t}\) | Dòng 293–295 ghi: "Độ phân tán giữa các mô hình … chỉ báo hiệu mức bất định, không đo rủi ro". Nhưng dòng 815–818 lại hồi quy "các thước đo rủi ro mô hình", trong đó \(Y_{t}\) có thể là \(D_{t}\), và H\textsubscript{1} yêu cầu "\(\beta\) của \(D_{t}\) cùng dấu". | Gọi \(D_{t}\) là "thước đo bất định" một cách nhất quán, kể cả trong câu mô tả hồi quy.
182. [MINOR] (A4 · Undefined Notation #2) Ngưỡng xác suất lọc và xác suất lọc | Bài nói "ngưỡng đăng ký trước" (dòng 825–826) và "xác suất lọc" (dòng 662) nhưng không có ký hiệu cho cả hai. | Thêm \(\xi_{d}=\Pr(s_{d}=\text{căng thẳng}\mid\mathcal{F}_{d})\) và ngưỡng \(\kappa\) ở mục 4.3.4.
183. [MINOR] (A4 · Undefined Notation #3) Đại lượng dùng để chọn \(c\) | "lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước" (dòng 770–772) là một đại lượng khác \(U_{m,t}\), vì cửa sổ là 36 tháng chứ không phải 6 tháng, nhưng không có ký hiệu. | Định nghĩa \(\widehat{CE}^{36}_{m,t}\) theo cùng công thức (1) trên 36 tháng trước \(t\).
184. [MINOR] (A4 · Undefined Notation #4) Chuỗi tham chiếu của "\emph{t}" và "cửa sổ" trong \(S_{t}\) | Câu "tỷ lệ số ngày trong cửa sổ" không nói rõ đó là cửa sổ đánh giá 6 tháng hay cửa sổ ước lượng 104 tuần. | Ghi rõ "cửa sổ đánh giá \(t\)".
185. [MINOR] (A4 · Regression Specification Issues #5) Biến kiểm soát vĩ mô | Mục 4.3.3 (dòng 652–653) bổ sung "chỉ số giá tiêu dùng, tỷ giá … và lãi suất điều hành làm biến kiểm soát" trong kiểm tra độ bền, nhưng không nói chúng vào (5) ở vị trí nào. | Thêm câu: "Trong kiểm tra độ bền, \(X_{t}\) được mở rộng thêm …".
186. [MINOR] (A4 · LaTeX Math Formatting #1) Dòng 765 và 767 | `\sum_{m \in M}^{}` có chỉ số trên rỗng (tàn dư của pandoc). | Bỏ `^{}`.
187. [MINOR] (A4 · LaTeX Math Formatting #2) Dòng 760–768, 777, 821 | Các phương trình được đặt inline bằng `\(...\)`, nên sẽ hiển thị cỡ chữ nhỏ (đặc biệt \(\frac{\rho}{2}\) và căn bậc hai trong (3)). | Nếu biên tập lại thì dùng `\begin{equation}…\label{eq:…}\end{equation}` và `\eqref`.
188. [MINOR] (A4 · LaTeX Math Formatting #3) Dòng 821 | `\gamma'X_{t}` dùng dấu phẩy trên (prime) cho chuyển vị và không phân biệt véc-tơ với vô hướng. | Dùng `\boldsymbol{\gamma}^{\top}\mathbf{X}_{t}`. Trong (5) cũng không cần `\cdot` giữa \(\beta\) và \(S_{t}\).
189. [MINOR] (A4 · LaTeX Math Formatting #4) Dòng 752–753 | Câu `\textbar{}\emph{M}\textbar{} = 7` được viết ở chế độ văn bản. | Viết thành `\(|M| = 7\)`.
190. [MINOR] (A4 · LaTeX Math Formatting #5) Tham chiếu phương trình | Chỉ có (5) được nhắc đến bằng số (dòng 824, 851). Các phương trình (1)–(4) được đánh số nhưng không bao giờ được tham chiếu. | Thêm tham chiếu, chẳng hạn "\(U_{m,t}\) theo (1)" và "mức hối tiếc (4)" tại dòng 782 và 841, hoặc bỏ đánh số các phương trình không được dùng.
191. [MINOR] (A5 · Tables with Missing or Incomplete Notes #1) Bảng 1 | Ghi chú chỉ có "Nguồn: Thí sinh tổng hợp". Bảng không nêu tiêu chí chọn bốn nhóm, trong khi phần tổng quan có sáu nhóm (1)–(6). Tên các dòng cũng không khớp với tên các nhóm trong tổng quan, ví dụ "Danh mục ở Việt Nam" và "Chế độ thị trường ở Việt Nam" không phải tiêu đề nhóm nào ở mục 4.2. | Thêm ghi chú: "Bốn nhóm được chọn vì gần đề tài nhất; nhóm 'Rủi ro mô hình' tương ứng mục (2), ba nhóm còn lại thuộc mục (6) Nghiên cứu về Việt Nam".
192. [MINOR] (A5 · Tables with Missing or Incomplete Notes #2) Bảng 1 | Phạm vi tra cứu làm căn cứ cho cột "Khoảng trống" chỉ nằm ở đoạn văn sau bảng ("SSRN, RePEc/IDEAS, ScienceDirect… thực hiện đến ngày 30/09/2026"; "chưa gồm Scopus, Web of Science và các tạp chí tiếng Việt"). Người đọc chỉ xem bảng sẽ không biết các khoảng trống này có giới hạn gì. | Thêm vào ghi chú: "Khoảng trống xác định theo tra cứu trên [cơ sở dữ liệu] đến 30/09/2026; chưa gồm Scopus, Web of Science và tạp chí tiếng Việt."
193. [MINOR] (A5 · Tables with Missing or Incomplete Notes #3) Bảng 1 | Hai dòng "Chế độ thị trường ở Việt Nam (Hoang và Luu, 2024)" và "Bầy đàn ở Việt Nam (Vo và Phan, 2017)" mỗi dòng chỉ dựa trên một công trình. Riêng Hoang và Luu (2024) được thân bài gọi là "một bản thảo công bố trực tuyến", nhưng bảng không ghi điều này. | Ghi rõ trong ghi chú rằng hai dòng này mỗi dòng có một nguồn và Hoang và Luu (2024) là bản thảo chưa qua phản biện.
194. [MINOR] (A5 · Tables with Missing or Incomplete Notes #7) Bảng 2 | Vai trò của các thước đo ở dòng H\textsubscript{1} không khớp thân bài. Bảng gộp "độ phân tán mô hình, kích thước tập tin cậy mô hình" chung là "Kết quả phụ". Nhưng ở mục 4.3.7, D\textsubscript{t} là một trong ba điều kiện để ủng hộ H\textsubscript{1} ("β của D\textsubscript{t} cùng dấu"). Ở mục 4.3.6, kích thước tập tin cậy mô hình chỉ là "một thước đo mô tả". Bảng cũng không nói rằng R\textsubscript{t} được chuẩn hóa. | Tách thành: "Kết quả chính: R\textsubscript{t} (chuẩn hóa); điều kiện phụ: dấu của β với D\textsubscript{t}; mô tả: kích thước tập tin cậy mô hình".
195. [MINOR] (A5 · Tables with Missing or Incomplete Notes #8) Bảng 2 | Tiêu đề bảng nói "cơ sở lý thuyết", nhưng cột "Cơ sở" chủ yếu liệt kê nguồn phương pháp hoặc thực nghiệm (Danielsson và cộng sự, 2016; Hansen và cộng sự, 2011). Các nguồn lý thuyết nêu ở mục 4.3.1 (Kan và Zhou, 2007; Gilboa và Schmeidler, 1989; Hansen và Sargent, 2008; Hamilton, 1989) không xuất hiện. | Đổi tiêu đề hoặc tên cột thành "Cơ sở lý thuyết và phương pháp", hoặc thêm các nguồn lý thuyết vào cột.
196. [MINOR] (A5 · Tables with Missing or Incomplete Notes #9) Bảng 2 | Ở dòng H\textsubscript{4}, "thước đo bầy đàn" không được định nghĩa. Christie và Huang (1995) dùng CSSD, còn Chang và cộng sự (2000) dùng CSAD, và phương trình (5) chỉ có "độ phân tán chéo của lợi suất". | Ghi rõ thước đo (CSSD hay CSAD) và tần suất tính.
197. [MINOR] (A5 · Tables with Missing or Incomplete Notes #10) Bảng 2 | Bảng không có cột liên kết mỗi giả thuyết với câu hỏi nghiên cứu và khoảng trống (1)–(4) ở Bảng 1. Liên kết này hiện chỉ có trong văn bản ("H\textsubscript{1} trả lời câu hỏi 1…"). | Thêm cột "Câu hỏi / Khoảng trống".
198. [MINOR] (A5 · Tables with Missing or Incomplete Notes #12) Bảng 3 | Bảng thiếu thông số chung cho mọi mô hình: chỉ mua (không bán khống), cửa sổ ước lượng 104 tuần dữ liệu tuần, tái cân bằng hằng tháng, siêu tham số chọn từ lưới với cùng ngân sách tinh chỉnh. Bảng cũng không nêu các trường hợp riêng: M\textsubscript{3} dùng nghịch đảo giả Moore–Penrose khi tỷ lệ số cổ phiếu trên số quan sát tuần vượt 0,5; quan điểm của M\textsubscript{4} lấy từ "một mô hình dự báo đơn giản" chưa được nêu tên. | Thêm ghi chú về các thông số chung và cột "Siêu tham số / đầu vào".
199. [MINOR] (A5 · Tables with Missing or Incomplete Notes #13) Bảng 4 | Văn bản ghi "Ngoài phần mở đầu, kết luận…, luận án dự kiến gồm sáu chương". Tuy vậy bảng có dòng "Kết luận" với ô "Tên chương" bỏ trống. Bảng cũng không cho biết "phần mở đầu" có trùng với "Chương 1: Giới thiệu nghiên cứu" hay không. | Điền tên ô (ví dụ "Kết luận và kiến nghị") và ghi chú rằng phần mở đầu là Chương 1, hoặc là một phần riêng.
200. [MINOR] (A5 · Tables with Missing or Incomplete Notes #14) Bảng 5 | Hai cam kết trong văn bản không có trong bảng. Mục 4.2 ghi "việc đọc toàn văn và mở rộng phạm vi tìm kiếm nằm trong kế hoạch năm thứ nhất", nhưng bảng chỉ ghi "đọc toàn văn các nguồn tổng quan" và không nhắc việc mở rộng sang Scopus, WoS và tạp chí trong nước. Bảng cũng thiếu mốc báo cáo số giai đoạn căng thẳng trong phần mẫu tính được mức hối tiếc (mục 4.3.6). | Bổ sung hai mục này vào Năm 1.
201. [MINOR] (A5 · Tables with Missing or Incomplete Notes #15) Bảng 5 | Thứ tự công việc khó theo dõi. Ước lượng thử ở Quý 2 diễn ra trước "làm sạch dữ liệu" ở Quý 3. Chuyên đề 3 ("thiết kế kiểm định có đăng ký trước", mục 7.2) là sản phẩm Năm 2, trong khi việc đăng ký trước đã xong ở Quý 4 Năm 1. | Thêm ghi chú giải thích thứ tự, hoặc chuyển chuyên đề 3 sang Năm 1.
202. [MINOR] (A5 · Tables with Missing or Incomplete Notes #16) Bảng 6 | Bảng không có dòng "Nguồn" và không ghi ngày chốt trong tiêu đề. Ngày chốt chỉ có ở ô của dòng 3 ("chưa xuất bản tại ngày 30/09/2026"), trong khi tiêu đề Bảng 7 có ngày chốt. Ở dòng 2, Nguyễn Văn Trung không có dấu (*), nhưng ghi chú không giải thích dòng này khác gì. | Thêm "tính đến 30/09/2026" vào tiêu đề. Ghi rõ tác giả liên hệ của dòng 2.
203. [MINOR] (A5 · Tables with Missing or Incomplete Notes #17) Bảng 7 | Có hai điểm chưa rõ. Cột "Số tác giả" không cho biết thí sinh là tác giả thứ mấy. Trạng thái "Đã sửa xong vòng 2 (mã 19322)" không cho biết bản sửa đã nộp lại và đang chờ quyết định hay chưa. | Thêm vị trí tác giả, hoặc ghi danh sách tác giả như Bảng 6. Viết lại trạng thái thành "Đã nộp bản sửa vòng 2, chờ quyết định".
204. [MINOR] (A5 · Tables with Missing or Incomplete Notes #18) Toàn đề cương | Không áp dụng cho bảng hiện có. Tuy nhiên mục 4.3.7 nêu hai cách suy luận cho phương trình (5): "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" và "bootstrap khối dừng… cho các hệ số hồi quy". Mục 4.3.10 hứa "Cạnh mỗi hệ số… báo cáo số cửa sổ độc lập và số giai đoạn căng thẳng độc lập". Đề cương không có bảng mẫu nào ghi rõ sẽ báo cáo loại sai số hay khoảng tin cậy nào. | Có thể thêm một bảng mẫu (bảng rỗng) cho phương trình (5) với các cột R\textsubscript{t}/D\textsubscript{t}, có hoặc không có X\textsubscript{t}, và các dòng: sai số chuẩn HAC hoặc khoảng tin cậy bootstrap khối, số cửa sổ, số giai đoạn căng thẳng độc lập, VIF, phân vị 95% của phân phối rỗng.
205. [MINOR] (A5 · Figures with Missing or Incomplete Notes #1) Hình 1 | Ghi chú chỉ có "Nguồn: Thí sinh đề xuất". Hình không có chú giải cho mũi tên liền và mũi tên nét đứt. Phần giải thích chỉ nằm trong thân bài: "Mũi tên nét đứt từ rủi ro lựa chọn mô hình sang kết quả danh mục không mang giả thuyết riêng". Ký hiệu R\textsubscript{t}, D\textsubscript{t}, S\textsubscript{t} và H\textsubscript{1}–H\textsubscript{4} cũng không được định nghĩa ở dưới hình. | Thêm ghi chú: "Mũi tên liền: quan hệ có giả thuyết; mũi tên nét đứt: quan hệ theo định nghĩa, không kiểm định. R\textsubscript{t}: mức hối tiếc; D\textsubscript{t}: độ phân tán; S\textsubscript{t}: tỷ lệ ngày căng thẳng trong cửa sổ."
206. [MINOR] (A5 · Figures with Missing or Incomplete Notes #2) Hình 1 | Hộp "Chế độ thị trường | Chế độ bình thường | Chế độ căng thẳng | (biến S\textsubscript{t})" cho người đọc cảm giác S\textsubscript{t} là biến nhị phân. Thực ra phương trình (5) định nghĩa S\textsubscript{t} là "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng". | Ghi "S\textsubscript{t}: tỷ lệ ngày căng thẳng (0–1)" trong hình hoặc trong ghi chú.
207. [MINOR] (A5 · Figures with Missing or Incomplete Notes #3) Hình 1 | Tôi không kiểm tra được hướng mũi tên và việc H\textsubscript{2}/H\textsubscript{4} trỏ vào quan hệ (tác động điều tiết) hay trỏ vào biến, vì tệp chữ chỉ có nhãn. Thân bài khẳng định "Các biến kênh tác động lên chính quan hệ đó". | Đề nghị tác giả kiểm tra lại hình gốc.
208. [MINOR] (A5 · Figures with Missing or Incomplete Notes #5) Hình 2 | Trục ngang chỉ ghi "thời gian", không có mốc năm hay thang đo. Hình trộn đơn vị tuần và tháng ("104 tuần", "6 tháng", "36 tháng"). | Ghi mốc ví dụ (ví dụ năm 2007 → khoảng 2012 → …) hoặc quy đổi sang một đơn vị thống nhất (104 tuần ≈ 24 tháng).
209. [MINOR] (A5 · Cross-Reference Issues #4) Bảng 1 và mục 4.2 | Cùng một chữ "nhóm" được dùng cho hai cách chia khác nhau. Mục 4.2 chia tài liệu thành sáu nhóm có đánh số (1)–(6). Bảng 1 có "bốn nhóm công trình", và các khoảng trống của bảng cũng đánh số (1)–(4). Hai dãy số trùng nhau nên dễ nhầm. | Đánh số khoảng trống là K1–K4 (hoặc G1–G4).
210. [MINOR] (A5 · Cross-Reference Issues #5) Mục 4.3.10 và Bảng 7 | Câu "dùng phương pháp Bai-Perron trong một bản thảo đang gửi tạp chí" không dẫn đến dòng cụ thể. | Thêm "(bản thảo số 5, Bảng 7)".
211. [MINOR] (A5 · Formatting Inconsistencies #1) Nhãn ghi chú dưới bảng không thống nhất | Bảng 1–5 dùng "Nguồn: …", còn Bảng 6–7 dùng "Ghi chú: …" và không có dòng Nguồn. | Dùng chung một khuôn cho mọi bảng: "Nguồn: …" rồi đến "Ghi chú: …" khi cần.
212. [MINOR] (A5 · Formatting Inconsistencies #2) Tên cột trích dẫn không thống nhất | Bảng 2 đặt tên cột là "Cơ sở", Bảng 3 là "Nguồn". Riêng ở Bảng 3, tên cột "Nguồn" trùng với dòng ghi chú "Nguồn: Thí sinh tổng hợp" ngay dưới bảng. | Đổi cột của Bảng 3 thành "Tài liệu gốc" hoặc "Cơ sở".
213. [MINOR] (A5 · Formatting Inconsistencies #3) Cách ghi tác giả và tác giả liên hệ khác nhau giữa Bảng 6 và Bảng 7 | Bảng 6 ghi họ tên tác giả và đánh dấu (*). Bảng 7 chỉ ghi "Số tác giả" kèm một ghi chú chung. Bảng 7 có cột "Liên quan đến đề tài" còn Bảng 6 thì không, dù dòng 2 của Bảng 6 là nền của M\textsubscript{5}. | Dùng cùng một bộ cột cho hai bảng.
214. [MINOR] (A5 · Formatting Inconsistencies #4) Thông tin chỉ mục (Scopus Q) chỉ có ở một số dòng | Bảng 6 có ở dòng 3. Bảng 7 có ở dòng 1, 4, 6. Các dòng còn lại không ghi gì. | Ghi chỉ mục cho mọi dòng, hoặc ghi "chưa được chỉ mục".
215. [MINOR] (A5 · Formatting Inconsistencies #5) Khóa trích dẫn không thống nhất dấu tiếng Việt cho cùng một cặp tác giả | Bảng 6 ghi "(Nguyễn và Nguyễn, 2026b)" nhưng lại ghi "(Nguyen và Nguyen, 2026a)". | Thống nhất một cách viết.
216. [MINOR] (A5 · Formatting Inconsistencies #6) Cách viết hoa tên bài báo không đồng nhất | Bảng 7 dòng 4 viết hoa đầu mỗi từ ("Corporate Brownwashing and Firm Valuation in ASEAN-5 Disclosure Regimes"), các dòng khác chỉ viết hoa chữ đầu câu. | Giữ đúng như bản gửi tạp chí, nhưng ghi điều này trong ghi chú như Bảng 6 đã làm, hoặc thống nhất về kiểu viết hoa đầu câu.
217. [MINOR] (A5 · Formatting Inconsistencies #7) Bảng 4 có ô bỏ trống | Dòng "Kết luận & & …" để trống cột "Tên chương". | Điền tên ô.
218. [MINOR] (A5 · Formatting Inconsistencies #8) Ghi chú dưới hình chỉ có nguồn | Cả Hình 1–3 chỉ có "Nguồn: Thí sinh đề xuất", trong khi nhiều bảng có ghi chú đầy đủ hơn. | Thêm khối "Ghi chú:" cho mỗi hình, nêu ký hiệu và cách đọc, theo cùng khuôn với các bảng.

Counts (theo thẻ gốc của agent, CRITICAL/MAJOR/MINOR): A1 3/12/61; A2 3/11/17; A3 0/19/16; A4 0/11/17; A5 0/9/28; A6 5/5/0; tổng 11/67/139 = 217. Cộng mục khoảng trống đóng góp: 12/67/139 = 218. A7 và A8 không gắn thẻ, đúng như format của skill. (Bản trước ghi A1 có 13 MAJOR; con số đúng là 12, vì dòng thứ 13 là câu chú thích của agent có nhắc chữ "[MAJOR]", không phải một mục.)
