Xác nhận: đã gọi được công cụ Skill (peer-review) — "Launching skill: peer-review"

> **BẢN NHÁP LÀM VIỆC (working draft).** Văn bản do trợ lý AI soạn theo skill `peer-review` (K-Dense, v2.2), xử lý cục bộ, theo yêu cầu của chính tác giả. Đây không phải phản biện độc lập và không phải quyết định chấp nhận/từ chối. Tác giả (Nguyễn Văn Trung) là người chịu trách nhiệm cuối: cần tự đọc lại toàn văn, kiểm từng vị trí trích dẫn, từng con số, từng nguồn, rồi viết lại góp ý theo phán đoán chuyên môn của mình.

Tư liệu đã đánh giá: `scratchpad/paper/de-cuong-goc.md` (chuyển từ `ho-so/de-cuong-goc.docx` bằng pandoc) và `scratchpad/paper/hinh-van-ban.txt` (chữ trong Hình 1–2). Không đọc file nào khác trong `reports/`. Số dòng ghi trong báo cáo là số dòng của file `.md` đã chuyển đổi, không phải số trang của bản .docx.

## Số file skill đã đọc: 24

Đã đọc trọn mọi file trong `.claude/skills/peer-review/`:

1. `SKILL.md`
2. `references/ethical_review_practice.md`
3. `references/reporting_standards.md`
4. `references/statistical_reproducibility.md`
5. `references/common_issues.md`
6. `references/security_validation.md`
7. `references/tool_reference.md`
8. `assets/review_intake_template.json`
9. `assets/study_profile_template.json`
10. `assets/claim_evidence_matrix_template.csv`
11. `assets/statistical_reproducibility_template.json`
12. `assets/citation_references_template.csv`
13. `assets/reporting_checklist_template.csv`
14. `assets/reporting_guidelines.json`
15. `assets/review_scaffold_template.md`
16. `assets/source_ledger.csv`
17. `scripts/_common.py` (đọc toàn bộ mã)
18. `scripts/validate_review_intake.py` (đọc toàn bộ mã)
19. `scripts/select_reporting_guidelines.py` (đọc toàn bộ mã)
20. `scripts/validate_claim_evidence.py` (đọc toàn bộ mã)
21. `scripts/audit_statistics_reproducibility.py` (đọc toàn bộ mã)
22. `scripts/audit_citations.py` (đọc toàn bộ mã)
23. `scripts/generate_review_scaffold.py` (đọc toàn bộ mã)
24. `scripts/lint_review.py` (đọc toàn bộ mã)

Mỗi script chỉ được chạy sau khi đã đọc toàn bộ mã của nó và `_common.py`. Cả 7 script đều chỉ dùng thư viện chuẩn và không gọi mạng; điều này đã được kiểm tra khi đọc mã.

---

# Comments to authors

## Tóm tắt trung lập (dựa trên bằng chứng)

Đề cương đề xuất đo **rủi ro lựa chọn mô hình** trong phân bổ danh mục cổ phiếu trên HOSE, theo chế độ thị trường. Khái niệm này được định nghĩa là tổn thất kỳ vọng, đo bằng **mức hối tiếc** R_t, tức chênh lệch lợi suất tương đương chắc chắn (CE) giữa mô hình tốt nhất nhìn lại sau thực tế và mô hình chọn trước. Bản đồ định hướng (bước 2 của skill):

- **Câu hỏi:** CH1 (rủi ro lựa chọn mô hình thay đổi giữa chế độ bình thường và căng thẳng ra sao), CH2 (các biến kênh sau khi kiểm soát biến động thực hiện), CH3 (cơ chế giảm thiểu sau chi phí giao dịch).
- **Hệ thống/đơn vị:** rổ 30 cổ phiếu HOSE có thanh khoản và vốn hóa tự do lớn nhất, xác định tại từng thời điểm, kể cả mã đã hủy niêm yết. Đơn vị suy luận là cửa sổ đánh giá 6 tháng không chồng lấn, dự kiến "khoảng 28" cửa sổ trong giai đoạn 2007–2026.
- **"Phơi nhiễm":** S_t, tức tỷ lệ số ngày trong cửa sổ có xác suất lọc Markov của chế độ căng thẳng vượt ngưỡng.
- **Tập so sánh:** bảy mô hình M1–M7 (Bảng 3).
- **Kết quả:** R_t, D_t (độ phân tán CE) và kích thước tập tin cậy mô hình. Riêng H3 dùng thêm CE, độ sụt giảm tối đa, thiệt hại kỳ vọng 95% và vòng quay.
- **Phân tích:** phương trình (5) với sai số chuẩn HAC, bootstrap khối, phân phối rỗng 1.000 lần lặp, Holm 10% và quy tắc "không kết luận" khi có dưới 10 cửa sổ căng thẳng.
- **Tuyên bố chính:** H1–H4 (Bảng 2), đóng góp lý thuyết/thực nghiệm/thực tiễn (mục 4.4) và khoảng trống nghiên cứu (Bảng 1).

Đây là đề cương. Chưa có dữ liệu, mã hay kết quả, nên đánh giá chỉ xét thiết kế, tính nhất quán nội bộ và mức độ trình bày đủ để thẩm định.

## Điểm mạnh

1. **Khái niệm được tách bạch và giữ nhất quán.** Dòng 171–184 phân biệt rủi ro mô hình, bất định mô hình và rủi ro lựa chọn mô hình, khủng hoảng và chế độ căng thẳng: "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro."
2. **Đã nhận diện thiên lệch cơ học của mức hối tiếc** (dòng 625–630): "Kỳ vọng của R_t vẫn dương khi các mô hình ngang chất lượng, vì giá trị lớn nhất của các đại lượng có nhiễu tăng theo phương sai của nhiễu." Đề cương xử lý bằng chuẩn hóa và phân phối rỗng.
3. **Minh bạch về xung đột lợi ích với mô hình của chính tác giả** (dòng 571–573): "Vì M5 do thí sinh phát triển, đề tài xử lý M5 như mọi mô hình khác và báo cáo kết quả cả khi có lẫn khi không có M5". Dòng 577–580 cũng nói rõ việc đã xem dữ liệu 2019–2025.
4. **Có đăng ký trước và quy tắc "không kết luận" đặt trước** (dòng 580–587, 740–743). Hiếm thấy ở đề cương cấp nghiên cứu sinh.
5. **Đã tính đến thiên lệch sống sót và thiên lệch nhìn trước** (dòng 503–504, 522–525): rổ và xác suất lọc chỉ dùng dữ liệu có tại thời điểm đó.
6. **Lập luận rõ vì sao không dùng tỷ số Sharpe làm thước đo chính** trong chế độ có lợi suất vượt trội âm (dòng 593–597).
7. **Trung thực về giới hạn tìm kiếm tài liệu** (dòng 399–405): "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn".
8. **Bám tính nhất quán của tài liệu tham khảo:** công cụ đối chiếu cục bộ cho thấy 56 khóa trích dẫn trong thân bài khớp đúng 56 mục tài liệu, không thừa, không thiếu.

## Major comments

### Major comment M1

- Location: Mục 4.3.5 (dòng 577–587), mục 4.3.6 (dòng 643–645), Bảng 5 năm 1 (dòng 946–956); ma trận CL-08.
- Observation: Đăng ký trước được đặt ở quý 4 năm thứ nhất. Nhưng quý 2 năm thứ nhất đã "ước lượng thử bảy mô hình trên giai đoạn 2019--2025 để đo thời gian tính và số quan sát ở chế độ căng thẳng, quyết định phương pháp ước lượng cho M5", và "Các độ dài cửa sổ là giá trị dự kiến, và thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất." Đề cương chưa nói chạy thử sẽ cho thí sinh xem những đầu ra nào (chỉ thời gian tính và số quan sát, hay cả CE và thứ hạng mô hình).
- Evidence or criterion: Mục 4.3.5 tự nêu mục đích đăng ký trước là kiểm soát rủi ro "không thể khẳng định chưa từng thấy kết quả ở chế độ căng thẳng". Nguyên tắc tiền đăng ký (skill: `analysis.prespecification`, `design.blinding`): tham số chốt sau khi xem kết quả trên cùng dữ liệu kiểm định thì không còn là tham số đặt trước.
- Why it matters: Giai đoạn 2019–2025 chứa hai giai đoạn căng thẳng mà H1 và H3 phụ thuộc vào. Nếu độ dài cửa sổ hoặc phương pháp cho M5 được chọn sau khi đã thấy hiệu quả tương đối của các mô hình trong giai đoạn này, việc đăng ký ở quý 4 không còn bảo vệ được các kiểm định khẳng định.
- Requested action: Ghi rõ trong đề cương rằng chạy thử ở quý 2 chỉ xuất và chỉ xem các đại lượng không phải kết quả (thời gian tính, số quan sát, số giai đoạn căng thẳng, lỗi hội tụ), không xem CE, R_t hay thứ hạng mô hình. Nêu tiêu chí biện minh độ dài cửa sổ mà không dựa vào hiệu quả danh mục. Cam kết liệt kê các đầu ra đã xem trong tệp đăng ký. Còn việc có dời thời điểm chạy thử hay đăng ký hay không là vấn đề thiết kế, xem mục "chờ tác giả duyệt".

### Major comment M2

- Location: Mục 4.3.6 (dòng 640–643), 4.3.7 phương trình (5) (dòng 664–675), 4.3.10 (dòng 738–743); ma trận CL-04.
- Observation: Đề cương dự kiến "khoảng 28 cửa sổ đánh giá độc lập" và quy định "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Tuy nhiên S_t là một tỷ lệ liên tục ("tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng đăng ký trước"). Đề cương chưa định nghĩa một cửa sổ "ở chế độ căng thẳng" khi đếm, và chưa ước tính số cửa sổ căng thẳng kỳ vọng. Phương trình (5) có hệ số chặn, S_t và X_t gồm biến động thực hiện, độ phi thanh khoản Amihud, tương quan đuôi, tương quan hiệu chỉnh theo biến động và độ phân tán chéo, tức khoảng 7 tham số trên khoảng 28 quan sát. Kiểm tra độ bền còn thêm CPI, tỷ giá và lãi suất điều hành.
- Evidence or criterion: Skill `design.sample_size_precision`: cần có lý do về cỡ mẫu và độ chính xác, cùng số tham số so với số quan sát. Trong phần mẫu tính được mức hối tiếc (từ khoảng năm thứ năm), đề cương chỉ nêu hai đợt căng thẳng: COVID-19 năm 2020 và trái phiếu doanh nghiệp từ quý IV/2022. Khủng hoảng toàn cầu "chủ yếu phục vụ ước lượng chế độ".
- Why it matters: Nếu số cửa sổ căng thẳng kỳ vọng dưới 10, H1, kiểm định trung tâm, sẽ được xếp "không kết luận" ngay từ thiết kế. Với khoảng 7 tham số trên khoảng 28 quan sát, sai số chuẩn HAC và khoảng tin cậy bootstrap có thể không ổn định.
- Requested action: (a) Định nghĩa quy tắc đếm cửa sổ căng thẳng, ví dụ ngưỡng của S_t, và đưa quy tắc này vào danh mục đăng ký. (b) Nêu số cửa sổ căng thẳng kỳ vọng, dựa trên các giai đoạn đề cương đã liệt kê, kèm khoảng không chắc chắn. (c) Nêu số tham số của phương trình (5) ở cấu hình cơ sở và cấu hình kiểm tra độ bền so với số quan sát. Thay đổi thiết kế (nếu có) thuộc quyền tác giả, xem mục "chờ tác giả duyệt".

### Major comment M3

- Location: Mục 4.1 (dòng 175–179) và mục 4.3.6 (dòng 627–630); Bảng 2 dòng H1; ma trận CL-04.
- Observation: Khái niệm được định nghĩa theo đơn vị tổn thất: "*Rủi ro lựa chọn mô hình* là tổn thất kỳ vọng phát sinh khi nhà đầu tư phải chọn một mô hình trước lúc biết mô hình nào tốt nhất". Nhưng phân tích chính lại dùng đại lượng chuẩn hóa: "phân tích chính chia D_t và R_t cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình trong cùng cửa sổ." Trong khi đó Bảng 2 ghi thước đo chính của H1 là "mức hối tiếc (chênh lệch lợi suất tương đương chắc chắn ...)", không ghi phiên bản chuẩn hóa.
- Evidence or criterion: Skill `question.estimand_alignment`: câu hỏi, đại lượng mục tiêu, phân tích và diễn giải phải cùng nhắm vào một đại lượng.
- Why it matters: Mẫu số (sai số chuẩn bootstrap) nhiều khả năng lớn hơn ở chế độ căng thẳng, vì biến động cao hơn. Khi đó β của R_t chuẩn hóa đo chênh lệch tỷ lệ tín hiệu trên nhiễu, không phải chênh lệch tổn thất theo đơn vị CE. Hai đại lượng này có thể khác dấu, nên kết luận về H1 phụ thuộc vào việc chọn phiên bản nào.
- Requested action: Nêu rõ đại lượng mục tiêu chính của H1 (R_t theo đơn vị CE, hay R_t chuẩn hóa) và thống nhất cách gọi ở mục 4.1, Bảng 2 và mục 4.3.6. Cam kết báo cáo cả hai phiên bản, kèm giải thích khi chúng khác dấu. Việc chọn phiên bản nào làm chính là quyết định thiết kế, xem mục "chờ tác giả duyệt".

### Major comment M4

- Location: Câu hỏi 2 (dòng 236–239), mục tiêu (iii) (dòng 250–252), mục 4.3.7 (dòng 675, 688–691); ma trận CL-06.
- Observation: Câu hỏi 2 viết: "Sau khi kiểm soát biến động thực hiện, các biến kênh ... chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?". Mục tiêu (iii) lại xếp biến động vào nhóm biến kênh: "gồm biến động, thanh khoản, tương quan cực trị và bầy đàn". Mục 4.3.7 viết "Biến động thực hiện luôn có mặt trong X_t với vai trò biến kiểm soát", và phần do kênh giải thích là "β0 − β1, trong đó β0 và β1 là hệ số β của phương trình (5) khi không có và khi có X_t". Như vậy β0 − β1 gồm cả phần do biến động thực hiện hấp thụ.
- Evidence or criterion: Tính nhất quán nội bộ giữa câu hỏi, mục tiêu và công thức ước lượng (skill: `question.estimand_alignment`).
- Why it matters: Theo cách viết hiện tại, phần chênh lệch quy cho "biến kênh" có thể chủ yếu là biến động, đúng thứ mà Câu hỏi 2 yêu cầu kiểm soát. Người đọc sẽ không biết con số β0 − β1 trả lời câu hỏi nào.
- Requested action: Viết rõ β0 được ước lượng khi có hay không có biến động thực hiện. Thống nhất vai trò của biến động (biến kiểm soát hay biến kênh) ở Câu hỏi 2, mục tiêu (iii), Hình 1 (ô "Biến kênh" hiện có dòng "Biến động thực hiện (kiểm soát)") và mục 4.3.7.

### Major comment M5

- Location: Mục 4.3.2, diễn giải Hình 1 (dòng 435–439); mục 4.3.7 (dòng 698–699); ma trận CL-07.
- Observation: Hình 1 được diễn giải bằng ngôn ngữ tác động và điều tiết: "Theo Hình 1, chế độ thị trường tác động lên rủi ro lựa chọn mô hình (giả thuyết H1). Các biến kênh tác động lên chính quan hệ đó". Phép ước lượng lại là so sánh hệ số khi thêm biến (β0 − β1), một dạng suy giảm hệ số chứ không phải số hạng tương tác. Mục 4.3.7 lại tuyên bố: "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả."
- Evidence or criterion: Skill `common_issues.md`, mục Claim–evidence alignment: không dùng ngôn ngữ nhân quả cho thiết kế quan sát; khung lý thuyết (điều tiết) phải khớp với phép ước lượng (trung gian/suy giảm).
- Why it matters: Hội đồng xét tuyển đọc Hình 1 trước. Mũi tên "tác động lên quan hệ" gợi ý mô hình điều tiết với số hạng tương tác, nhưng đề cương không ước lượng mô hình đó. Câu về H3 ("Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục") cũng có cùng vấn đề.
- Requested action: Chỉnh lời diễn giải Hình 1 cho khớp với phép ước lượng thật và với tuyên bố phi nhân quả, ví dụ "liên hệ với", "giải thích một phần chênh lệch (theo nghĩa thống kê)". Không cần đổi phép kiểm định.

### Major comment M6

- Location: Bảng 2 dòng H3 (dòng 466–473), mục 4.3.8 (dòng 703–722), Bảng 3 (M6, M7); ma trận CL-12.
- Observation: (a) Bảng 2 viết: "kết hợp mô hình và danh mục vững chắc cho mức hối tiếc và độ sụt giảm tối đa thấp hơn". Mục 4.3.8 lại viết: "mức hối tiếc thấp hơn và độ sụt giảm tối đa không cao hơn so với chọn một mô hình, với khoảng tin cậy bootstrap khối loại trừ 0". "Thấp hơn" và "không cao hơn" là hai tiêu chí khác nhau, và điều kiện "khoảng tin cậy loại trừ 0" không khớp với tiêu chí "không cao hơn". (b) Bảng 2 chỉ nêu hai cơ chế, còn mục 4.3.8 có ba, thêm "(iii) quy tắc chuyển chế độ". (c) Cơ chế (ii) (danh mục vững chắc, Garlappi) và (iii) (Kritzman) trùng với M6 và M7 ở Bảng 3. Câu "đề tài loại cơ chế (ii) và (iii) khỏi M, nên mức hối tiếc của hai cơ chế này có thể âm" nghĩa là tập tham chiếu của R_t trong H3 (5 mô hình) khác tập tham chiếu trong H1 (7 mô hình), nhưng đề cương chưa nói rõ điều này.
- Evidence or criterion: Tính nhất quán nội bộ giữa giả thuyết và tiêu chí ủng hộ (skill: `results.complete_outcomes_harms`, `integrity.deviations_selective_reporting`).
- Why it matters: Hai tiêu chí khác nhau cho cùng một giả thuyết tạo kẽ hở chọn tiêu chí sau khi thấy kết quả. Khi tập tham chiếu khác nhau, R_t của H1 và R_t của H3 không so sánh trực tiếp được.
- Requested action: Thống nhất một phát biểu H3 (danh sách cơ chế, tiêu chí độ sụt giảm tối đa, kiểm định tương ứng) giữa Bảng 2 và mục 4.3.8. Nêu rõ "chọn một mô hình" là quy tắc chọn nào (quy tắc c trong 36 tháng?). Nêu tập M dùng cho R_t ở H3 và cách so sánh với H1.

### Major comment M7

- Location: Mục 4.3.7 (dòng 681–684, 695–697), mục 4.3.10 (dòng 743–744).
- Observation: H1 dùng ngưỡng "vượt phân vị 95% của phân phối rỗng" cộng với "khoảng tin cậy bootstrap khối của β loại trừ 0", nhưng không nêu mức tin cậy của khoảng này. Đề cương cũng viết "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết", trong khi "Đề tài chỉ báo cáo H4 như kết quả thăm dò". H2 yêu cầu hai hệ số, H3 yêu cầu ba tiêu chí cùng lúc. Đề cương chưa nói Holm được áp dụng lên giá trị p nào khi một giả thuyết gồm nhiều điều kiện.
- Evidence or criterion: Skill `analysis.multiplicity`: cần xác định họ kiểm định và mức ý nghĩa trước khi đề xuất hiệu chỉnh. Giả thuyết thăm dò thường không nằm trong họ khẳng định.
- Why it matters: Nếu các mức ý nghĩa (5% một phía, khoảng tin cậy chưa nêu mức, Holm 10%) không khớp nhau, quy tắc "ủng hộ, bác bỏ, không kết luận" không tái lập được. Đây chính là phần tệp đăng ký trước cần chốt.
- Requested action: Nêu (a) mức tin cậy của mọi khoảng tin cậy; (b) họ kiểm định khẳng định (H1–H3, hay H1–H4); (c) với giả thuyết nhiều điều kiện, giá trị p hoặc thống kê nào đi vào thủ tục Holm; (d) quan hệ giữa phân vị 95% và mức 10% của Holm.

### Major comment M8

- Location: Mục 4.3.1 (dòng 414–417) đối chiếu với mục 4.2(2) (dòng 287–290); ma trận CL-03.
- Observation: Mục 4.3.1 viết: "Khối thứ hai là lý thuyết quyết định dưới bất định mô hình (Gilboa và Schmeidler, 1989; Hansen và Sargent, 2008), cung cấp cách đo tổn thất của một lựa chọn so với lựa chọn tốt nhất nhìn lại sau thực tế". Chính mục 4.2(2) lại mô tả Gilboa và Schmeidler (1989) là "tiêu chí chọn phương án tốt nhất trong tình huống xấu nhất", tức tiêu chí maxmin, còn Hansen và Sargent (2008) là "kiểm soát vững chắc trước sai đặc tả".
- Evidence or criterion: Skill `common_issues.md`, mục Citations: nguồn được trích phải hỗ trợ đúng mệnh đề. Theo mô tả của chính đề cương, maxmin và kiểm soát vững chắc không phải tiêu chí hối tiếc (so với phương án tốt nhất nhìn lại).
- Why it matters: Mức hối tiếc là thước đo trung tâm của đề tài. Nếu cơ sở lý thuyết của thước đo được gắn với nguồn không định nghĩa nó, phần khung lý thuyết dễ bị hội đồng chất vấn.
- Requested action: Tách hai vai trò trong câu: Gilboa–Schmeidler và Hansen–Sargent làm cơ sở cho các cơ chế vững chắc; còn tiêu chí hối tiếc thì cần một nguồn riêng mà tác giả đã đọc toàn văn, hoặc trình bày như định nghĩa do đề tài đặt ra. Báo cáo này không đề xuất nguồn cụ thể để tránh trích dẫn chưa kiểm chứng.

### Major comment M9

- Location: Mục 4.2(2) (dòng 290–292), 4.2(3) (dòng 311–312), 4.2(4) (dòng 329–330), đối chiếu với dòng 396–405; số liệu trích ở mục 4.1–4.2; ma trận CL-01, CL-02, CL-11.
- Observation: Nhận định về Việt Nam được giới hạn cẩn thận ("Theo hiểu biết của thí sinh ... Phạm vi tìm kiếm chưa gồm Scopus, Web of Science"). Ba nhận định phủ định ở phạm vi toàn cầu thì không có giới hạn tương tự: "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục."; "chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường."; "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không." Đề cương cũng trích nhiều con số cụ thể, ví dụ "Tu (2010) ước tính ... thường trên 2% mỗi năm, có thể tới 10%", "151 cuộc khủng hoảng ngân hàng hệ thống", "14 mô hình trên bảy bộ dữ liệu", "299 công ty niêm yết", "468 tuần", trong khi "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn".
- Evidence or criterion: Skill `common_issues.md`: tuyên bố mới lạ không được rộng hơn phạm vi tìm kiếm. Mọi con số trích dẫn phải được đối chiếu với nguồn gốc.
- Why it matters: Phủ định toàn cầu dễ bị bác chỉ bằng một phản ví dụ. Con số sai lệch so với toàn văn sẽ làm giảm độ tin cậy của toàn bộ phần tổng quan.
- Requested action: Thêm cho ba nhận định toàn cầu cùng loại giới hạn phạm vi tìm kiếm như nhận định về Việt Nam, ví dụ "trong phạm vi tài liệu thí sinh đã khảo sát". Trước khi nộp, đối chiếu từng con số với toàn văn. Báo cáo này không kiểm chứng được các con số vì không dùng mạng.

### Major comment M10

- Location: Mục 4.3.10 (dòng 747–750); ma trận CL-05.
- Observation: "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam."
- Evidence or criterion: Skill `statistical_reproducibility.md` (nguyên tắc ASA về giá trị p): không bác bỏ được H0 không chứng minh hiệu ứng bằng 0, nhất là khi chính đề cương thừa nhận "các kiểm định có công suất thấp". Kết luận "1/N đủ dùng" là một tuyên bố về hiệu quả tương đối của M1, không suy ra từ kết quả của H1.
- Why it matters: Câu này mâu thuẫn với quy tắc "không kết luận" mà đề cương đã đặt và có thể bị hội đồng xem là diễn giải quá mức.
- Requested action: Viết lại theo ba trường hợp đã đăng ký: ủng hộ; bác bỏ với khoảng tin cậy hẹp quanh 0 (khi đó mới nói "không có bằng chứng về chênh lệch đáng kể"); không kết luận. Nếu muốn giữ ý về 1/N, nêu nó như một kiểm định riêng (so sánh CE của M1 với các mô hình khác).

### Major comment M11

- Location: Mục 4.3.5 (dòng 585–587), mục 4.4 phạm vi thời gian (dòng 774–775), Bảng 5 năm 1 quý 4 (dòng 956).
- Observation: "Dữ liệu phát sinh sau ngày đăng ký là mẫu kiểm tra riêng". Ngày đăng ký là quý 4 năm thứ nhất, nhưng phạm vi thời gian ghi "dữ liệu từ 2007 đến 2026". Đề cương chưa cho biết năm thứ nhất bắt đầu khi nào, nên chưa rõ ngày đăng ký có rơi sau năm 2026 hay không, và mẫu kiểm tra riêng (nếu có) dài bao nhiêu cửa sổ 6 tháng.
- Evidence or criterion: Tính nhất quán giữa phạm vi thời gian và thiết kế kiểm tra ngoài mẫu (skill: `integrity.deviations_selective_reporting`).
- Why it matters: Nếu ngày đăng ký sau năm 2026, mẫu kiểm tra riêng nằm ngoài phạm vi đã nêu. Nếu nó chỉ gồm một vài cửa sổ, vai trò của nó nên được nói rõ (mô tả hay kiểm định).
- Requested action: Nêu mốc dự kiến của ngày đăng ký, độ dài dự kiến của mẫu kiểm tra riêng (số cửa sổ) và vai trò của nó, rồi điều chỉnh câu phạm vi thời gian cho khớp.

### Major comment M12

- Location: Trang bìa (dòng 23–25) và mục 10 (dòng 1145–1159).
- Observation: Trang bìa ghi "Người hướng dẫn khoa học (dự kiến): - PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân". Mục 10 lại ghi "Người hướng dẫn chính (dự kiến): GS.TS. Nguyễn Đức Khương" và PGS.TS. Hà Hồng Hạnh là "Người hướng dẫn thứ hai".
- Evidence or criterion: Tính nhất quán của hồ sơ hành chính.
- Why it matters: Đây là thông tin hội đồng tuyển sinh đối chiếu đầu tiên. Thông tin lệch giữa bìa và nội dung có thể gây hiểu nhầm về sự đồng ý của người hướng dẫn.
- Requested action: Ghi cả hai người hướng dẫn trên trang bìa theo đúng thứ tự ở mục 10, hoặc theo mẫu nhà trường yêu cầu. Thống nhất cách viết tên cơ quan ("Đại học Kinh tế Quốc Dân" ở bìa, "Trường Đại học Kinh tế Quốc dân" ở mục 10).

### Major comment M13

- Location: Bảng 2 dòng H2 (dòng 457–464), mục 4.3.7 (dòng 671–673, 695–697).
- Observation: Đề cương viết: "H2 được ủng hộ khi hệ số của độ phi thanh khoản dương, hệ số của tương quan đuôi âm". Cụm "tương quan đuôi âm" có thể hiểu là "hệ số âm" hoặc là "tương quan ở đuôi âm" (lower tail). X_t chứa hai biến tương quan ("tương quan đuôi và tương quan hiệu chỉnh theo biến động"), nhưng H2 chỉ nêu một biến. Ngoài ra, mục 4.2(4) dẫn Ang và Bekaert (2002): "tương quan và biến động cùng tăng ở chế độ xấu". Nếu hệ số của tương quan âm như H2 dự đoán, kênh tương quan sẽ làm giảm rủi ro ở chế độ căng thẳng, tức ngược chiều với H1. Đề cương chưa nêu dấu kỳ vọng của phần chênh lệch do kênh này giải thích.
- Evidence or criterion: Một giả thuyết cần phát biểu rõ dấu và biến (skill: `analysis.prespecification`).
- Why it matters: Phát biểu mơ hồ về dấu cho phép diễn giải kết quả theo hai cách, đúng điều mà đăng ký trước muốn ngăn.
- Requested action: Viết lại H2 cho rõ: "hệ số của [biến tương quan cụ thể] mang dấu âm". Nêu biến tương quan nào là biến kiểm định và biến nào là biến phụ. Nêu dấu kỳ vọng của phần chênh lệch giữa hai chế độ do từng kênh giải thích.

### Major comment M14

- Location: Mục 4.3.6 (dòng 593–597), mục 4.3.7 (dòng 657–659), mục 4.3.2 (dòng 490–492).
- Observation: Đề cương nói "Tỷ số Sharpe không phù hợp làm thước đo chính" và chỉ báo cáo Sharpe "ở các cửa sổ có lợi suất vượt trội trung bình dương". Nhưng hiệu chỉnh thiên lệch chọn lọc lại làm "bằng tỷ số Sharpe hiệu chỉnh (Bailey và López de Prado, 2014)", và giả thuyết đối lập của H3 nhắc "sau hiệu chỉnh thiên lệch chọn lọc".
- Evidence or criterion: Phân tích–thiết kế phải khớp nhau (skill: `analysis.method_design_alignment`).
- Why it matters: Thước đo chính là CE, có thể âm ở chế độ căng thẳng. Đề cương chưa cho biết thiên lệch chọn lọc của CE (và của quy tắc chọn c) được hiệu chỉnh như thế nào.
- Requested action: Nêu rõ hiệu chỉnh thiên lệch chọn lọc áp dụng cho thước đo nào, và nếu chỉ áp dụng cho Sharpe ở các cửa sổ có lợi suất vượt trội dương thì nói rõ đây là kết quả phụ. Nếu CE cũng cần hiệu chỉnh, nêu cách làm (ví dụ: phân phối rỗng ở mục 4.3.7 có đảm nhiệm vai trò này hay không).

### Major comment M15

- Location: Mục 5 (dòng 878–881) đối chiếu với mục 4.2(5) (dòng 340–341), mục 4.4 (dòng 780–784, 809–811).
- Observation: Mục 5 viết: "đề tài nằm ở giao điểm của tài chính định lượng, quản lý và tài chính hành vi". Trong nội dung, kênh hành vi chỉ có ở H4, "chỉ xét kênh này ở mức thăm dò", còn phần quản lý là một thủ tục "chưa qua kiểm nghiệm với người dùng". Ma trận CL-10.
- Evidence or criterion: Tuyên bố khái quát phải khớp với phạm vi thật (skill: claim–evidence, `scope`).
- Why it matters: Hội đồng của chương trình định hướng "kinh tế hành vi và quản lý" sẽ đối chiếu lời tuyên bố về sự phù hợp với nội dung. Khẳng định quá mức dễ bị hỏi lại.
- Requested action: Viết lại đoạn về sự phù hợp cho đúng tỷ trọng thật, ví dụ nói rõ cấu phần hành vi ở mức thăm dò và cấu phần quản lý là đề xuất thủ tục giám sát mô hình. Không cần đổi phạm vi đề tài.

### Major comment M16

- Location: Mục 4.3.4 (dòng 525–528).
- Observation: Đề cương viết: "Số chế độ (hai hoặc ba) do tiêu chí thông tin quyết định" và "Chế độ căng thẳng là chế độ có phương sai điều kiện cao nhất và lợi suất kỳ vọng thấp hơn chế độ bình thường." Đề cương chưa nói: khi có ba chế độ, chế độ nào là "bình thường" và chế độ thứ ba được xử lý ra sao; nếu chế độ có phương sai cao nhất không có lợi suất thấp hơn thì gán nhãn thế nào; làm sao giữ nhãn nhất quán khi ước lượng lại theo cửa sổ mở rộng (hoán đổi nhãn).
- Evidence or criterion: Skill `analysis.assumptions_diagnostics`. S_t, biến trung tâm của H1–H4, phụ thuộc trực tiếp vào quy tắc gán nhãn.
- Why it matters: Nếu quy tắc gán nhãn không đầy đủ, S_t có thể thay đổi tùy cách xử lý tình huống biên, đúng loại "bậc tự do của nhà nghiên cứu" mà đăng ký trước muốn khóa.
- Requested action: Bổ sung quy tắc gán nhãn đầy đủ cho cả trường hợp hai và ba chế độ, quy tắc xử lý khi hai điều kiện (phương sai cao nhất, lợi suất thấp hơn) không trùng nhau, và cách xử lý hoán đổi nhãn. Đưa các quy tắc này vào tệp đăng ký.

### Major comment M17

- Location: Mục 4.3.6, phương trình (1) (dòng 599–606), cửa sổ đánh giá 6 tháng (dòng 636–637).
- Observation: Đề cương viết: "gọi μ_{m,t} và σ²_{m,t} là trung bình và phương sai lợi suất danh mục sau chi phí của mô hình m" trên cửa sổ đánh giá 6 tháng, nhưng không nêu tần suất lợi suất dùng để tính (ngày, tuần hay tháng) và không nêu ρ = 5 áp dụng cho lợi suất theo kỳ nào (năm hóa hay không).
- Evidence or criterion: Skill `reproducibility.code_environment_parameters`: tham số cần cho tái lập.
- Why it matters: Với lợi suất tháng, mỗi cửa sổ chỉ có 6 quan sát để ước lượng phương sai, nên U_{m,t} và R_t sẽ rất nhiễu. Với lợi suất ngày, độ lớn của số hạng ρσ²/2 thay đổi theo cách năm hóa. Cả hai ảnh hưởng trực tiếp đến thước đo chính.
- Requested action: Nêu tần suất lợi suất trong cửa sổ đánh giá, cách năm hóa μ và σ², và đơn vị của ρ.

### Major comment M18

- Location: Mục 4.3.5 (dòng 569–571), mục 4.3.8 (dòng 703–706).
- Observation: "Đề tài chọn siêu tham số của M2, M4, M5, M6 và M7 từ một lưới cho trước, bằng cùng một quy tắc và cùng ngân sách tinh chỉnh." Đề cương chưa nêu quy tắc đó là gì (tiêu chí nào, trên dữ liệu nào) và dữ liệu tinh chỉnh có tách khỏi cửa sổ đánh giá hay không. Cơ chế (i) lại để ngỏ hai phương án: "kết hợp các mô hình theo trọng số Bayes ... hoặc chỉ kết hợp các mô hình nằm trong tập tin cậy". Trọng số Bayes đòi hỏi một hàm hợp lý hoặc điểm số cho từng quy tắc danh mục, và đề cương chưa định nghĩa hàm này.
- Evidence or criterion: Skill `common_issues.md`, mục Prediction and machine learning: tách dữ liệu tinh chỉnh khỏi dữ liệu đánh giá để tránh rò rỉ. Mỗi phương án phải được đặc tả trước.
- Why it matters: Nếu tinh chỉnh dùng chính cửa sổ đánh giá, CE ngoài mẫu sẽ bị thổi phồng không đều giữa các mô hình, ảnh hưởng trực tiếp đến R_t. Phương án "hoặc" chưa chốt cũng tạo thêm một nhánh phân tích.
- Requested action: Nêu tiêu chí và cửa sổ dữ liệu dùng để tinh chỉnh siêu tham số. Nêu phương án kết hợp chính cho H3, hoặc báo cáo cả hai và tính vào họ kiểm định. Định nghĩa đại lượng dùng làm trọng số Bayes cho các quy tắc danh mục.

## Minor comments

### Minor comment m1

- Location: Mục 4.3.6 (dòng 640–641) và mục 4.3.10 (dòng 739–740).
- Observation: Đề cương dùng cụm "khoảng 28 cửa sổ đánh giá độc lập" và "số cửa sổ độc lập". Các cửa sổ đánh giá không chồng lấn, nhưng lịch sử 36 tháng dùng để chọn mô hình và cửa sổ ước lượng 104 tuần thì chồng lấn giữa các cửa sổ.
- Evidence or criterion: Skill `design.unit_and_independence`.
- Why it matters: Chữ "độc lập" phóng đại lượng thông tin thực có. Chính đề cương đã dùng HAC và bootstrap khối vì nhận ra sự phụ thuộc này.
- Requested action: Thay bằng "không chồng lấn" hoặc thêm một câu giải thích sự phụ thuộc giữa các cửa sổ.

### Minor comment m2

- Location: Mục 4.3.3 (dòng 499–505).
- Observation: Đề cương viết: "rổ cổ phiếu gồm 30 mã có giá trị giao dịch bình quân ba tháng và vốn hóa tự do chuyển nhượng lớn nhất". Chưa rõ hai tiêu chí kết hợp ra sao (lọc tuần tự, điểm tổng hợp hay giao nhau); dữ liệu vốn hóa tự do theo thời điểm từ 2007 có sẵn hay không; mã ngừng giao dịch hoặc hủy niêm yết giữa cửa sổ được xử lý thế nào; dữ liệu thiếu xử lý thế nào.
- Evidence or criterion: Skill `data.inclusion_exclusion`, `data.missing_data`.
- Why it matters: Quy tắc lập rổ quyết định tập tài sản của cả bảy mô hình.
- Requested action: Nêu công thức xếp hạng, nguồn vốn hóa tự do theo thời điểm và quy tắc xử lý mã hủy niêm yết, ngừng giao dịch hoặc thiếu dữ liệu, hoặc ghi rõ các quy tắc này sẽ được chốt trong tệp đăng ký.

### Minor comment m3

- Location: Mục 4.3.5 (dòng 573–575).
- Observation: Đề cương viết: "Đề tài chỉ ước lượng trực tiếp M3 khi tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5". Ở cấu hình cơ sở, tỷ lệ này là 30/104 (khoảng 0,29), nên ngưỡng chỉ có tác dụng ở các cấu hình kiểm tra độ bền (ví dụ rổ VN100 hoặc dữ liệu tháng).
- Evidence or criterion: Tính rõ ràng của đặc tả.
- Why it matters: Người đọc có thể hiểu nhầm rằng nghịch đảo giả được dùng trong phân tích chính.
- Requested action: Nói rõ ngưỡng này áp dụng cho cấu hình nào.

### Minor comment m4

- Location: Mục 4.3.3 (dòng 515–516).
- Observation: Đề cương viết: "Kiểm tra độ bền dùng dữ liệu tháng, tái cân bằng hằng quý". Chưa rõ độ dài cửa sổ ước lượng khi dùng dữ liệu tháng (104 tuần tương ứng chỉ khoảng 24 quan sát tháng cho 30 cổ phiếu).
- Evidence or criterion: Skill `reproducibility.code_environment_parameters`.
- Why it matters: Với khoảng 24 quan sát cho 30 cổ phiếu, ma trận hiệp phương sai mẫu suy biến và cấu hình này thay đổi bản chất của M3.
- Requested action: Nêu độ dài cửa sổ ước lượng cho kiểm tra độ bền dùng dữ liệu tháng.

### Minor comment m5

- Location: Trang bìa (dòng 21) và mục 3 (dòng 35).
- Observation: Hai dòng "Cơ quan công tác:" và "3. Đơn vị công tác:" đang để trống.
- Evidence or criterion: Tính đầy đủ của hồ sơ.
- Why it matters: Ô trống trong hồ sơ nộp dễ bị coi là chưa hoàn thiện.
- Requested action: Điền thông tin, hoặc ghi rõ "Chưa có" hay nội dung tương đương theo mẫu của nhà trường.

### Minor comment m6

- Location: Mục 4.3.3 (dòng 506–507) và mục 4.3.10 (dòng 760–762).
- Observation: Đề cương viết: "Nguồn dữ liệu là HOSE và một nhà cung cấp dữ liệu thương mại." và "thí sinh lưu mã nguồn và tệp đăng ký trước". Chưa nêu tên nhà cung cấp, nơi lưu và mức công khai mã nguồn, phiên bản phần mềm và seed của bootstrap.
- Evidence or criterion: Skill `reproducibility.data_materials_access`, `reproducibility.code_environment_parameters`.
- Why it matters: Đây là các yếu tố tái lập. Hạn chế giấy phép dữ liệu là chính đáng nhưng nên nói rõ.
- Requested action: Nêu tên nhà cung cấp khi đã xác nhận (quý 1 năm thứ nhất), nơi lưu mã (ví dụ cùng dự án OSF với tệp đăng ký, nếu tác giả chọn), cách ghi phiên bản phần mềm và seed.

### Minor comment m7

- Location: Mục 4.3.8 (dòng 717–718).
- Observation: Đề cương viết: "Đề tài tham số hóa chi phí giao dịch và kiểm tra độ nhạy theo tham số này." Chưa có giá trị cơ sở, trong khi thước đo chính được tính "sau chi phí giao dịch".
- Evidence or criterion: Skill `analysis.prespecification`.
- Why it matters: Giá trị cơ sở ảnh hưởng đến xếp hạng các mô hình có vòng quay khác nhau, nên cần được đặt trước.
- Requested action: Nêu giá trị cơ sở (hoặc cách xác định từ phí và thuế theo thời kỳ) và khoảng kiểm tra độ nhạy, rồi đưa vào tệp đăng ký.

### Minor comment m8

- Location: Mục 11 Danh mục tài liệu tham khảo (dòng 1318–1319, 1277–1280); Bảng 6 (dòng 1004–1005, 1014).
- Observation: (a) Lo và Mueller (2010) thiếu số trang: "*Journal of Investment Management*, 8(2)." (b) Hoang và Luu (2024) là bài làm việc SSRN nhưng không kèm URL hay DOI. (c) Công cụ cục bộ cho thấy 49/56 mục không có DOI hay URL (có thể chấp nhận theo quy cách trích dẫn của trường, đây chỉ là lựa chọn). (d) Cùng một cặp tác giả được ghi "Nguyễn và Nguyễn, 2026b" ở Bảng 6 nhưng "Nguyen và Nguyen, 2026a" trong thân bài.
- Evidence or criterion: Kết quả `audit_citations.py`: status VALID, cảnh báo REFERENCE_HAS_NO_PERSISTENT_LOCATOR ×49.
- Why it matters: Đây là lỗi định dạng nhỏ nhưng dễ thấy trong hồ sơ.
- Requested action: Bổ sung số trang cho Lo và Mueller, URL SSRN cho Hoang và Luu, và thống nhất cách viết tên tác giả cho 2026a/2026b theo quy cách của trường. Việc bổ sung DOI là tùy chọn.

### Minor comment m9

- Location: Mục 4.4 (dòng 786–787) và tên đề tài.
- Observation: Đề cương viết: "Giới hạn khác: kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam." Mẫu thật sự hẹp hơn: 30 cổ phiếu HOSE có thanh khoản cao, danh mục chỉ mua.
- Evidence or criterion: Skill claim–evidence (`generalization`/`scope`).
- Why it matters: Kết quả có thể không đại diện cho cổ phiếu vốn hóa nhỏ hoặc cho sàn HNX và UPCoM.
- Requested action: Thu hẹp câu giới hạn cho khớp mẫu (cổ phiếu HOSE thanh khoản cao, danh mục chỉ mua). Tên đề tài có thể giữ nguyên.

### Minor comment m10

- Location: Mục 8.2 (dòng 1108–1111) đối chiếu với Bảng 5.
- Observation: Đề cương viết: "Thí sinh đang theo học ngành Kế toán hệ vừa làm vừa học tại Đại học Kinh tế Quốc dân (năm thứ ba), ngành Công nghệ thông tin hệ đào tạo từ xa ... và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 07/2026." Đồng thời có chín bản thảo đang phản biện (Bảng 7). Mục 4.3.10 (khả năng thực hiện) không nhắc đến quỹ thời gian.
- Evidence or criterion: Mục "khả năng thực hiện" của chính đề cương.
- Why it matters: Hội đồng có thể hỏi về quỹ thời gian dành cho kế hoạch bốn năm.
- Requested action: Tùy tác giả: có thể thêm một câu về cách bố trí thời gian giữa các chương trình đang theo học và kế hoạch luận án.

### Minor comment m11

- Location: Tiêu đề các bảng và hình trong file chuyển đổi (ví dụ dòng 364, 430, 443).
- Observation: Trong file .md, tiêu đề hiện là "Bảng . Các nhóm nghiên cứu gần nhất ..." và "Hình . Khung phân tích ...", thiếu số thứ tự.
- Evidence or criterion: Nhiều khả năng đây là lỗi khi pandoc chuyển trường đánh số tự động, không phải lỗi của bản .docx.
- Why it matters: Nếu bản .docx cũng thiếu số, các tham chiếu "Bảng 1", "Hình 2" trong thân bài sẽ không khớp.
- Requested action: Mở bản .docx và xác nhận số bảng và số hình hiển thị đúng.

### Minor comment m12

- Location: Mục 4.3.7 (dòng 654–657).
- Observation: Đề cương viết: "lấy mẫu lặp theo khối liên tiếp (Ledoit và Wolf, 2008), và dùng bootstrap khối dừng (Politis và Romano, 1994)". Chưa nêu độ dài khối hay cách chọn độ dài khối, trong khi số quan sát chỉ khoảng 28.
- Evidence or criterion: Skill `analysis.clustering_repeated_measures`.
- Why it matters: Với chuỗi ngắn, độ dài khối ảnh hưởng mạnh đến độ rộng khoảng tin cậy.
- Requested action: Nêu độ dài khối hoặc quy tắc chọn độ dài khối, rồi đưa vào tệp đăng ký.

## Phương pháp, thống kê và khả năng tái lập (tóm tắt)

- Kiểm toán checklist (`audit_statistics_reproducibility.py`): 22 mục, trong đó 18 mục `partly_documented`, 2 mục `missing` (`data.missing_data`, `data.outliers_transformations`), 1 mục `verified_present` (đạo đức/quản trị dữ liệu) và 1 mục `not_applicable` (phân bổ ngẫu nhiên, vì đây là nghiên cứu quan sát trên dữ liệu thị trường). Phần lớn khoảng trống là **thiếu mô tả** ở mức đề cương, không phải lỗi thiết kế đã được chứng minh.
- Không có mã hay dữ liệu, nên không có phép tái lập nào được chạy hoặc được tuyên bố.
- **Cần chuyên gia:** kinh tế lượng tài chính (mô hình chuyển chế độ Markov với số chế độ chọn theo tiêu chí thông tin, bootstrap khối trên chuỗi ngắn, hiệu chuẩn phân phối rỗng). Công cụ báo trigger trên 8 mục và cảnh báo `SPECIALIST_REVIEW_NOT_REQUESTED`. Đề nghị tác giả nhờ người hướng dẫn hoặc một chuyên gia kinh tế lượng đọc riêng mục 4.3.4–4.3.7.

## Đạo đức, minh bạch, hình, bảng và trích dẫn

- **Đạo đức:** dữ liệu thị trường công khai, "Dữ liệu không chứa thông tin cá nhân". Không có đối tượng con người, nên không cần phê duyệt đạo đức. Xung đột lợi ích với M5 đã được tự công bố và có biện pháp xử lý (báo cáo có và không có M5). Không phát hiện vấn đề liêm chính nào.
- **Hình:** Hình 1 và Hình 2 được đối chiếu qua chữ trích trong `hinh-van-ban.txt`, khớp với thân bài (cửa sổ 104 tuần, 6 tháng, 36 tháng; các ô H1, H2/H4, H3). Ô "Biến kênh" của Hình 1 có dòng "Biến động thực hiện (kiểm soát)", liên quan đến M4. **Hình 3 không trích được chữ** (khung số 6 rỗng), nên chưa đánh giá được. Không áp dụng tiêu chí về xử lý ảnh, vì đây là sơ đồ.
- **Bảng:** đã đối chiếu Bảng 1–3 và Bảng 5 với thân bài (xem M6, M12, M13). Bảng 6–7 là danh mục công trình. Báo cáo này không kiểm chứng được tình trạng, mã bài hay hạng Scopus.
- **Trích dẫn:** 113 lần trích, 56 nguồn, khớp hoàn toàn với danh mục tài liệu (không có trích dẫn thiếu mục tài liệu, không có tài liệu không được trích). Việc kiểm tra nguồn có tồn tại và có hỗ trợ đúng mệnh đề hay không **chưa làm** vì không dùng mạng, xem M8 và M9.

## Limitations of this review (giới hạn)

- Không dùng mạng, nên không kiểm chứng được: sự tồn tại và nội dung của 56 nguồn; các văn bản SR 11-7, SR 26-2 (17/04/2026), Thông tư 83/2025/TT-NHNN; Thông báo tuyển sinh 2026 (mã số 9310116.01QTD, Nhóm 1, 9 tín chỉ); định hướng nghiên cứu của người hướng dẫn; tình trạng các bản thảo ở Bảng 6–7. **Tác giả cần tự kiểm các mục này.**
- Đánh giá dựa trên bản chuyển đổi pandoc. Bố cục trang, Hình 3 và định dạng bảng của bản .docx chưa được xem trực tiếp.
- Không có bộ hướng dẫn báo cáo nào trong danh mục của skill phù hợp với đề cương backtest tài chính (selector: `NO_BUNDLED_GUIDELINE_MATCH`). Theo skill, không ép dùng bộ gần nhất, nên không có checklist độ đầy đủ báo cáo.
- Người soạn là trợ lý AI, không phải chuyên gia kinh tế lượng tài chính được hội đồng chỉ định.

# Confidential comments to editor

> Không có biên tập viên hay hội đồng phản biện chính thức. Đây là bản tự đánh giá theo yêu cầu của tác giả. **Không có nội dung nào cần chuyển qua kênh riêng.** Mọi góp ý khoa học đã nằm trong phần gửi tác giả ở trên. Các dòng dưới đây chỉ là công bố quy trình.

## Reviewer disclosures

- Conflicts and editor clearance: Không phát hiện xung đột lợi ích (intake `conflict_status: none_identified`). Không có biên tập viên để duyệt.
- Competence limits or specialist review needed: Không kiểm chứng được nguồn và văn bản pháp lý khi không có mạng. Mô hình chuyển chế độ Markov, bootstrap khối và hiệu chuẩn phân phối rỗng cần chuyên gia kinh tế lượng tài chính xác nhận.
- Assistance or tools used and required disclosure: Trợ lý AI (Claude, chạy trong Claude Code) xử lý cục bộ theo yêu cầu của tác giả, dùng skill peer-review v2.2 và 7 script cục bộ chỉ dùng thư viện chuẩn. Không gửi nội dung ra dịch vụ ngoài. Nếu quy định của trường hoặc của hồ sơ Nghị quyết 57/2026/NQ-HĐND yêu cầu khai báo việc dùng AI hỗ trợ, tác giả tự khai theo đúng mẫu.
- Confidentiality or retention issue: Các file làm việc phái sinh nằm trong `scratchpad/peer-review/`. Kế hoạch là xóa sau khi tác giả xác nhận đã dùng xong (intake `retention_rule: delete_after_review`).

## Editorial-process or integrity concerns

Không có. Không phát hiện dấu hiệu bất thường về liêm chính. Báo cáo này không đưa ra quyết định chấp nhận hay từ chối.

---

# Danh sách phát hiện quy đổi theo mức

**NGHIÊM TRỌNG (3)**: ảnh hưởng đến độ tin cậy của kiểm định trung tâm H1:

1. M1: chạy thử bảy mô hình trên 2019–2025 (quý 2) và chốt độ dài cửa sổ trước khi đăng ký (quý 4); chưa nêu đầu ra nào sẽ được xem.
2. M2: chưa định nghĩa cách đếm "cửa sổ căng thẳng" và chưa ước tính số cửa sổ kỳ vọng so với ngưỡng 10; phương trình (5) có khoảng 7 tham số trên khoảng 28 quan sát.
3. M3: khái niệm (tổn thất theo đơn vị CE) lệch với thước đo chính (R_t chuẩn hóa); Bảng 2 và mục 4.3.6 không thống nhất.

**ĐÁNG SỬA (15)**:

4. M4: vai trò của biến động thực hiện (kiểm soát hay kênh) không thống nhất; β0 − β1 gồm cả phần của biến động.
5. M5: ngôn ngữ "tác động" và mô hình điều tiết ở Hình 1 lệch với phép ước lượng và với tuyên bố phi nhân quả.
6. M6: tiêu chí H3 ở Bảng 2 khác mục 4.3.8 (độ sụt giảm "thấp hơn" và "không cao hơn"; 2 hay 3 cơ chế); cơ chế (ii)/(iii) trùng M6/M7; tập M của H3 khác tập của H1.
7. M7: mức ý nghĩa và họ kiểm định không khớp nhau (phân vị 95%, khoảng tin cậy chưa nêu mức, Holm 10% gồm cả H4 thăm dò).
8. M8: Gilboa–Schmeidler và Hansen–Sargent được dẫn làm cơ sở cho thước đo hối tiếc, trái với chính mô tả maxmin của đề cương ở mục 4.2(2).
9. M9: ba nhận định phủ định toàn cầu chưa có giới hạn phạm vi; nhiều con số trích từ nguồn mới đọc tóm tắt.
10. M10: diễn giải kết quả âm tính ("không đổi theo chế độ", "1/N đủ dùng") quá mạnh.
11. M11: mẫu kiểm tra sau đăng ký có thể nằm ngoài phạm vi 2007–2026; chưa nêu độ dài.
12. M12: người hướng dẫn ở trang bìa khác mục 10.
13. M13: dấu và biến trong H2 ("tương quan đuôi âm") mơ hồ; chiều của kênh tương quan có thể ngược với H1.
14. M14: hiệu chỉnh thiên lệch chọn lọc dựa trên Sharpe, trong khi thước đo chính là CE.
15. M15: tuyên bố về sự phù hợp với hướng hành vi và quản lý mạnh hơn nội dung thật.
16. M16: quy tắc gán nhãn chế độ chưa đầy đủ (ba chế độ, hai điều kiện lệch nhau, hoán đổi nhãn).
17. M17: chưa nêu tần suất lợi suất trong cửa sổ 6 tháng và đơn vị của ρ.
18. M18: quy tắc tinh chỉnh siêu tham số và trọng số Bayes cho cơ chế (i) chưa đặc tả; còn để "hoặc".

**CHỈNH NHẸ (12)**: m1 chữ "độc lập" của cửa sổ; m2 quy tắc lập rổ và dữ liệu thiếu; m3 phạm vi áp dụng ngưỡng 0,5 của M3; m4 cửa sổ ước lượng khi dùng dữ liệu tháng; m5 ô công tác để trống; m6 tên nhà cung cấp, nơi lưu mã, seed; m7 giá trị cơ sở của chi phí giao dịch; m8 định dạng tài liệu tham khảo; m9 câu giới hạn phạm vi; m10 quỹ thời gian; m11 số bảng/hình (kiểm trên .docx); m12 độ dài khối bootstrap.

Tổng: 3 + 15 + 12 = 30 phát hiện.

# Vấn đề thiết kế cốt lõi — chờ tác giả duyệt

Các điểm dưới đây chạm vào thiết kế. Báo cáo **không đề xuất đổi** câu hỏi nghiên cứu, H1–H4, M1–M7, dữ liệu hay phương pháp kiểm định. Tác giả và người hướng dẫn quyết định có thay đổi hay không. Các góp ý ở trên chỉ yêu cầu làm rõ hoặc thống nhất câu chữ.

1. **Thứ tự chạy thử và đăng ký trước (M1).** Có giữ việc chạy thử bảy mô hình trên 2019–2025 trước khi đăng ký, và chốt độ dài cửa sổ sau khi chạy thử, hay không? Nếu giữ, giới hạn đầu ra nào được xem.
2. **Khả năng kiểm định H1 có kết luận (M2).** Với khoảng 28 cửa sổ, ngưỡng 10 cửa sổ căng thẳng và khoảng 7 tham số, thiết kế hiện tại có nguy cơ cho kết quả "không kết luận" ngay từ đầu. Mọi thay đổi (cửa sổ, ngưỡng, số biến) đều là quyết định của tác giả.
3. **Thước đo chính của H1 (M3):** R_t theo đơn vị CE hay R_t chuẩn hóa theo sai số chuẩn bootstrap.
4. **Cách hiểu "biến kênh" (M4, M5, M13):** điều tiết (như Hình 1 gợi ý) hay suy giảm hệ số (β0 − β1 như mục 4.3.7). Biến động thực hiện có nằm trong β0 hay không. Dấu kỳ vọng của kênh tương quan so với H1.
5. **Tập tham chiếu và tiêu chí của H3 (M6):** cơ chế (ii) và (iii) trùng M6 và M7; tập M của H3 khác tập của H1; tiêu chí độ sụt giảm tối đa.
6. **Mẫu kiểm tra sau đăng ký (M11):** có giữ hay không, dài bao lâu, đóng vai trò mô tả hay kiểm định.

---

# Bằng chứng tuân thủ

Thư mục làm việc: `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/peer-review/` (gọi tắt là `W/`). Script chạy từ thư mục skill.

| # | Bước theo SKILL.md | Trạng thái | Trích ngắn từ đề cương làm chứng | Đầu ra script / ghi chú |
|---|---|---|---|---|
| S1 | Mandatory safety boundary 1: xác nhận ủy quyền | Đã làm | "Họ và tên thí sinh: NGUYỄN VĂN TRUNG" (tác giả là người yêu cầu) | intake `authorization.basis: author_request`, `documented: true` |
| S2 | Safety boundary 2: chính sách nơi nhận (review, bảo mật, AI) | Đã làm (một phần) | "ĐẠI HỌC QUỐC GIA HÀ NỘI / TRƯỜNG QUỐC TẾ" | Không có tạp chí/hội đồng phản biện. `checked: true` chỉ là khai báo theo bối cảnh ủy quyền; chưa đọc quy định AI của trường (không dùng mạng). Tác giả tự kiểm. |
| S3 | Safety boundary 3: xung đột, giới hạn năng lực, phạm vi, nhu cầu chuyên gia | Đã làm | "Vì M5 do thí sinh phát triển" (xung đột lợi ích phía tác giả, không phải phía người đánh giá) | intake: `none_identified`, 3 giới hạn năng lực, `specialist_review_needed: financial_econometrics` |
| S4 | Safety boundary 4: mặc định xử lý cục bộ | Đã làm | "Dữ liệu không chứa thông tin cá nhân" | `local_only: true`, `external_service_use: false`; không gọi mạng hay dịch vụ ngoài |
| S5 | Danh sách "Never" (không gửi ra ngoài, không bịa, không gọi skill khác, không công bố quyết định...) | Đã làm | "Đề tài gọi các kết quả này là liên hệ có điều kiện" | Không gọi skill khác; không có câu quyết định (lint 0 lỗi EDITORIAL_DECISION_LANGUAGE, 0 lỗi ROLE_IMPERSONATION_LANGUAGE) |
| S6 | Đọc `ethical_review_practice.md` trước khi xử lý | Đã làm | n/a | Đọc trước khi mở đề cương |
| S7 | Xóa/lưu giữ bản sao phái sinh | CHƯA LÀM | n/a | Lý do: tác giả cần các file bằng chứng ở `W/` để đối chiếu. Kế hoạch: xóa `W/` (và file phái sinh `local-citations.md`) sau khi tác giả xác nhận; đã ghi trong intake. |
| H1 | Human accountability: gắn nhãn bản nháp làm việc | Đã làm | n/a | Dòng cảnh báo "BẢN NHÁP LÀM VIỆC" ở đầu báo cáo |
| H2 | Người chịu trách nhiệm đọc toàn văn, kiểm từng mệnh đề, viết lại, nộp đúng kênh | CHƯA LÀM | "*(Ký và ghi rõ họ tên)*" | Lý do: thuộc trách nhiệm của tác giả, không phải của trợ lý |
| G | Intake gate (`validate_review_intake.py`) | Đã làm | "Tên đề cương nghiên cứu: RỦI RO LỰA CHỌN MÔ HÌNH..." | EXIT=0; `status: READY_FOR_LOCAL_REVIEW`; errors []; warnings: CONFIDENTIAL_NOTES_CHANNEL_UNAVAILABLE, COMPETENCE_LIMITS_MUST_BE_DISCLOSED, SPECIALIST_REVIEW_NEEDED. File: `W/completed-intake.json`, `W/intake-report.json` |
| 1 | Xác định phạm vi và bằng chứng có sẵn | Đã làm | "Đề tài dùng phương pháp định lượng trên dữ liệu thị trường công khai" | Tư liệu: .md và hinh-van-ban.txt; không có dữ liệu, mã hay đăng ký OSF (chưa tồn tại); Hình 3 không có chữ |
| 2 | Định hướng, không quyết định | Đã làm | "Câu hỏi 1: Rủi ro lựa chọn mô hình thay đổi thế nào giữa chế độ bình thường và chế độ căng thẳng?" | Mục "Tóm tắt trung lập" |
| 3 | Chọn hướng dẫn báo cáo (`select_reporting_guidelines.py`) | Đã làm | "Đề tài ước lượng mô hình chuyển chế độ Markov (Hamilton, 1989) cho lợi suất VN-Index" | EXIT=0; `status: VALID`; `selected_guidelines: []`; warning `NO_BUNDLED_GUIDELINE_MATCH`. File `W/local-profile.json`, `W/guideline-report.json` |
| 3b | Kiểm độ đầy đủ theo checklist (`--coverage`) | Không áp dụng | n/a | Lý do: không có hướng dẫn nào được chọn (backtest tài chính); skill cấm ép dùng bộ gần nhất |
| 4 | Ánh xạ tuyên bố–bằng chứng (`validate_claim_evidence.py`) | Đã làm | "Theo hiểu biết của thí sinh, chưa có nghiên cứu nào đo rủi ro lựa chọn mô hình theo chế độ" | EXIT=0; `status: VALID_WITH_ALIGNMENT_GAPS`; 12 tuyên bố; supported 1, partly_supported 8, unsupported 2, not_assessed 1; cần xử lý CL-01…CL-08, CL-10…CL-12. File `W/local-claim-matrix.csv`, `W/claim-report.json` |
| 5 | Phương pháp và thống kê (`audit_statistics_reproducibility.py`) | Đã làm | "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết." | EXIT=0; `status: VALID_WITH_REVIEW_GAPS`; 22 mục: partly_documented 18, missing 2, verified_present 1, not_applicable 1; warning `SPECIALIST_REVIEW_NOT_REQUESTED`; 8 trigger. File `W/local-statistics-reproducibility.json`, `W/stats-report.json` |
| 6 | Tái lập và minh bạch | Đã làm (ở mức kế hoạch) | "Về minh bạch, thí sinh lưu mã nguồn và tệp đăng ký trước" | Chưa có mã hay dữ liệu, nên không chạy tái lập và không tuyên bố tái lập; xem m6, m7, M17 |
| 7 | Đạo đức và liêm chính | Đã làm | "Dữ liệu không chứa thông tin cá nhân." | Không có đối tượng con người; xung đột lợi ích M5 đã tự công bố; không có mối lo liêm chính |
| 8a | Hình và bảng | Đã làm (một phần) | "Hình . Cửa sổ ước lượng, cửa sổ đánh giá và thời điểm chọn mô hình" | Hình 1–2 đối chiếu qua chữ trích; **Hình 3 chưa đánh giá** (không trích được chữ); tiêu chí xử lý ảnh không áp dụng (sơ đồ) |
| 8b | Trích dẫn (`audit_citations.py`) | Đã làm | "Michaud (1989); Kan và Zhou, 2007" | Đề cương dùng kiểu tác giả–năm, không phải `[@key]`, nên đã tạo bản phái sinh cục bộ `W/local-citations.md` (giữ số dòng, chỉ chứa khóa) và `W/local-references.csv`; đã loại thủ công 7 khóa giả do bảng bị ngắt cột. EXIT=0; `status: VALID`; 113 lần trích; 56/56 nguồn; missing [], uncited []; warnings: CITED_REFERENCE_NOT_VERIFIED ×56, REFERENCE_HAS_NO_PERSISTENT_LOCATOR ×49. Không kiểm tra sự tồn tại của nguồn. |
| 9 | Tạo scaffold và soạn góp ý (`generate_review_scaffold.py`) | Đã làm | n/a | EXIT=0; "Created local review scaffold: W/private-review.md"; 18 góp ý lớn và 12 góp ý nhỏ, mỗi góp ý đủ 5 trường |
| 10 | Tách kênh | Đã làm | n/a | `# Comments to authors` đứng trước `# Confidential comments to editor`; kênh sau chỉ có công bố quy trình |
| 11 | Lint và hoàn thiện (`lint_review.py`) | Đã làm | n/a | (a) Scaffold còn trống `W/private-review.md` (lưu bản gốc ở `W/private-review.scaffold-raw.md`): EXIT=1, REVISION_REQUIRED, 16 lỗi UNRESOLVED_SCAFFOLD_PLACEHOLDER + 10 lỗi ACTIONABILITY_FIELD_EMPTY (M1, m1), tức đúng các ô trống của mẫu. (b) Sau khi điền phần review vào scaffold: EXIT=0, READY_FOR_HUMAN_REVIEW, 0 lỗi, 0 cảnh báo, 30 góp ý. (c) Chính báo cáo này: EXIT=0, READY_FOR_HUMAN_REVIEW, 0 lỗi, 0 cảnh báo, 30 góp ý. Không có lỗi nào cần sửa trong báo cáo. Xem Phụ lục A. |
| C1 | Before handoff: kiểm mọi vị trí và bằng chứng | Đã làm | "khoảng 28 cửa sổ đánh giá độc lập" | Mọi trích dẫn được chép từ file .md; số dòng theo file .md |
| C2 | Bỏ phê bình không có căn cứ hoặc suy đoán | Đã làm | "nên không thể khẳng định chưa từng thấy kết quả" | Các điểm chưa chắc được viết thành câu hỏi hoặc yêu cầu làm rõ (vd M2, M11) |
| C3 | Ngôn ngữ chuyên nghiệp, không xúc phạm | Đã làm | n/a | Lint (báo cáo và private-review đã điền): 0 lỗi ABUSIVE_OR_DISMISSIVE_LANGUAGE, PERSONAL_ATTACK, EDITORIAL_DECISION_LANGUAGE, ROLE_IMPERSONATION_LANGUAGE. Lexicon của linter chỉ có tiếng Anh, nên văn bản tiếng Việt vẫn cần tác giả tự đọc giọng văn. |
| C4 | Nêu giới hạn đánh giá và nhu cầu chuyên gia | Đã làm | "Mẫu có ít giai đoạn căng thẳng độc lập, nên các kiểm định có công suất thấp." | Mục "Limitations" và "Cần chuyên gia" |
| C5 | Công bố việc dùng hỗ trợ | Đã làm | n/a | Mục Reviewer disclosures |
| C6 | Xóa mọi placeholder | Đã làm | n/a | Scaffold gốc có 16 placeholder; bản đã điền và báo cáo: 0 lỗi UNRESOLVED_SCAFFOLD_PLACEHOLDER và 0 lỗi ACTIONABILITY_FIELD_* |
| C7 | Không bịa trích dẫn, thí nghiệm, phân tích lại hay kết quả | Đã làm | "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn" | Không đề xuất nguồn mới (M8); không chạy lại phân tích; không công bố quyết định |
| C8 | Theo quy tắc xóa/lưu giữ đã ghi | CHƯA LÀM | n/a | Chờ tác giả xác nhận rồi mới xóa `W/` (xem S7) |
| X | Mục "Citing Scientific Agent Skills" | Bỏ qua theo chỉ thị | n/a | Không chèn trích dẫn skill vào đề cương |

Kết quả lint (`lint_review.py`): xem Phụ lục A ngay dưới.

# Phụ lục A — Đầu ra lint (bước 11), nguyên văn

Lệnh chạy từ `.claude/skills/peer-review/`, theo `references/tool_reference.md` (`python3 scripts/lint_review.py <review.md> -o <report.json>`). Báo cáo JSON chỉ chứa mã quy tắc và số dòng, không chứa nội dung.

**A1. Scaffold còn trống** (`W/private-review.md` lúc vừa sinh ra, nay lưu ở `W/private-review.scaffold-raw.md`; báo cáo JSON: `W/lint-scaffold-raw.json`)

```
EXIT=1
status: REVISION_REQUIRED   structured_comment_count: 2
errors:
  UNRESOLVED_SCAFFOLD_PLACEHOLDER  line:17, 21, 28, 29, 30, 31, 38, 39, 40, 41, 53, 61, 62, 63, 64, 68
  ACTIONABILITY_FIELD_EMPTY  M1:evidence_or_criterion, M1:location, M1:observation, M1:requested_action, M1:why_it_matters
  ACTIONABILITY_FIELD_EMPTY  m1:evidence_or_criterion, m1:location, m1:observation, m1:requested_action, m1:why_it_matters
warnings: []
```

Các lỗi này là ô trống của mẫu, không thuộc báo cáo. Đã xử lý bằng cách điền phần "Comments to authors" và "Confidential comments to editor" của báo cáo vào scaffold (giữ phần đầu intake của scaffold).

**A2. Scaffold đã điền** (`W/private-review.md`; `W/lint-private-review.json`)

```
EXIT=0
status: READY_FOR_HUMAN_REVIEW   valid: true   structured_comment_count: 30
channel_separation: {author_before_editor: true, author_heading_count: 1, editor_heading_count: 1}
errors: []
warnings: []
```

**A3. Chính báo cáo này** (`reports/g2-peer-review.md`, chạy trước khi nối Phụ lục A; `W/lint-report-v1.json`)

```
EXIT=0
status: READY_FOR_HUMAN_REVIEW   structured_comment_count: 30
channel_separation: {author_before_editor: true, author_heading_count: 1, editor_heading_count: 1}
errors: []
warnings: []
```

Kết quả chạy lại sau khi nối phụ lục: xem A4.

Lưu ý của skill: linter dựa trên quy tắc cấu trúc và từ vựng (lexicon tiếng Anh). Nó không đánh giá giá trị khoa học và không thay thế việc tác giả tự đọc lại.

**A4. Báo cáo sau khi nối Phụ lục A1–A3** (`W/lint-report-final.json`)

```
EXIT=0
status: READY_FOR_HUMAN_REVIEW   valid: true   structured_comment_count: 30
channel_separation: {author_before_editor: true, author_heading_count: 1, editor_heading_count: 1}
errors: []
warnings: []
```
