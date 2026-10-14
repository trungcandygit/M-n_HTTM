Xác nhận: luồng chính gọi được công cụ Skill (review-pap), phản hồi "Launching skill: review-pap". Skill chạy ở luồng chính vì cần công cụ Agent (V7).

Số file skill đã đọc: 1/1 (.claude/skills/review-pap/SKILL.md).
Đối tượng: kế hoạch đăng ký trước và phần phương pháp (4.1, 4.3.1–4.3.10, 4.4, 7.4) trong đề cương. Đích đăng ký: OSF, vì đề cương ghi OSF Registries.
Báo cáo gốc của skill: scratchpad/paper/reviews/PAP_REVIEW_2026-10-13.md (bên dưới là nguyên văn).

## Bằng chứng tuân thủ (theo thứ tự SKILL.md)

| # | Bước | Làm? | Bằng chứng / trích đề cương |
|---|---|---|---|
| 1 | Phase 1 — phân tích đối số: token đầu "OSF" khớp danh sách → TARGET_REGISTRY = OSF; phần còn lại là đường dẫn | Làm | "đăng ký trước kế hoạch phân tích trên nền tảng OSF Registries" |
| 2 | Đường dẫn có tồn tại và là PAP chính hay không (nếu không thì quay về auto-detect) | Làm | File tồn tại và chứa giả thuyết, kết quả, đặc tả phân tích, nên không cần auto-detect |
| 3 | Bước 4 — tìm tài liệu hỗ trợ mà PAP nhắc tới | Làm | PAP hứa "Tệp đăng ký cố định…", nhưng chưa có tệp kèm |
| 4 | Bước 5 — tìm đệ quy các file hỗ trợ theo mẫu tên | Làm | find + grep -iE trên power, sample, mde, survey…: exit 1, không thấy file nào |
| 5 | Bước 6 — ghi lại kiểm kê | Làm | Mục File Inventory |
| 6 | Phase 2 — 6 agent general-purpose trong MỘT tin nhắn | Làm | 6 lời gọi Agent trong cùng một tin nhắn |
| 7 | Scope guard chép nguyên văn vào cả 6 prompt | Làm | Khối "Review ONLY the files listed…" |
| 8 | Thay TARGET_REGISTRY bằng "OSF" trong prompt Agent 6 (và Agent 3, mục 7) | Làm | "Adopt the persona and standards appropriate to `OSF`" |
| 9 | Agent 1 — 6 mục kiểm tra + format | Làm | A1-1: "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10…" |
| 10 | Agent 2 — 8 mục + format | Làm | A2-C2: "Khi kiểm định H~3~, đề tài loại cơ chế (ii) và (iii) khỏi *M*" |
| 11 | Agent 3 — 7 mục + format | Làm | A3-2: "Quý 2: ước lượng thử bảy mô hình trên giai đoạn 2019--2025" |
| 12 | Agent 4 — 7 mục + format | Làm | A4-M1: "khoảng 28 cửa sổ đánh giá độc lập" |
| 13 | Agent 5 — 6 mục + format | Làm | A5-Sample2: "một nhà cung cấp dữ liệu thương mại" |
| 14 | Agent 6 — 6 phần + xếp hạng | Làm | Part 1: "Borderline — cần sửa đổi đáng kể" |
| 15 | Phase 3 — lưu vào reviews/PAP_REVIEW_[ngày].md, kiểm tra -v2 | Làm | Chưa có file cũ → lưu PAP_REVIEW_2026-10-13.md |
| 16 | Cấu trúc báo cáo theo đúng thứ tự (Inventory, Overall, Recommendation, Priority, Agent 6, 2, 3, 4, 5, 1) | Làm | Đúng thứ tự trong file |
| 17 | Recommendation suy ra từ hạng của Agent 6 (Borderline → Substantial revision required) | Làm | Ghi đúng ánh xạ |
| 18 | Xếp ưu tiên theo hệ thứ bậc (3/6 > 4 > 2 > 5 > 1) | Làm | Mục 1–2 lấy từ Agent 6/3 |
| 19 | Báo người dùng 4 mục | Làm | Ghi trong báo cáo này; tóm tắt ở tin nhắn cuối phiên |

Sai lệch có chủ đích: prompt của mỗi agent có thêm ghi chú bối cảnh (đề cương tiếng Việt; nghiên cứu quan sát nên các mục RCT ghi "không áp dụng"), đặt SAU khối scope guard; đầu ra bằng tiếng Việt. Không bỏ bước nào.
Số thẻ thô (chưa khử trùng lặp): A1 7/23/18; A2 4/23/18; A3 2/13/12; A4 2/17/13; A5 2/14/11; A6 6/17/7 (CRITICAL/MAJOR/MINOR).

---

# Pre-Analysis Plan Review

**Study**: Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường: Bằng chứng từ thị trường chứng khoán Việt Nam
**PI(s)/Team**: Nguyễn Văn Trung (nghiên cứu sinh dự tuyển); người hướng dẫn dự kiến GS.TS. Nguyễn Đức Khương, PGS.TS. Hà Hồng Hạnh
**Date**: 2026-10-13
**Review Standard**: OSF

---

## File Inventory

- File PAP chính: `scratchpad/paper/de-cuong-goc.md`, văn bản pandoc trích từ `ho-so/de-cuong-goc.docx`. Kế hoạch phân tích nằm trong đề cương ở các mục 4.1, 4.3.1–4.3.10, 4.4 và 7.4. Trong file .docx, Hình 1–3 là hình vẽ; chữ của Hình 1–2 đã trích ra `scratchpad/paper/hinh-van-ban.txt`, chữ của Hình 3 không trích được.
- File hỗ trợ: không có. Tìm theo các mẫu power/sample/mde/survey/instrument/random/strata/analysis/code/mock/irb/ethics/consent đều không thấy. Thiếu cả năm nhóm: tính công suất, công cụ thu thập (không áp dụng), quy trình ngẫu nhiên hóa (không áp dụng; tương đương là quy trình dựng rổ cổ phiếu), mã/bảng mẫu, hồ sơ đạo đức (nhiều khả năng không áp dụng).
- Sổ đăng ký: OSF Registries theo đề cương ("đăng ký trước kế hoạch phân tích trên nền tảng OSF Registries vào quý 4 năm thứ nhất"). Chưa có mã đăng ký.

---

## Overall Assessment

Kế hoạch đo mức hối tiếc (theo lợi suất tương đương chắc chắn) khi chọn trước một trong bảy mô hình danh mục cho rổ 30 cổ phiếu HOSE. Nó kiểm định ba điều: mức hối tiếc có cao hơn ở chế độ căng thẳng không (H1), có liên hệ với các biến kênh không (H2/H4), và cơ chế giảm thiểu có tác dụng không (H3). Điểm mạnh chính là khung khái niệm tách bạch, phân phối rỗng để loại phần dương cơ học của mức hối tiếc, và việc thí sinh tự khai đã xem dữ liệu 2019–2025. Vấn đề nghiêm trọng nhất cần giải quyết trước khi đăng ký có hai mặt. Thứ nhất, kế hoạch ước lượng thử trên 2019–2025 rồi mới chốt độ dài cửa sổ và đăng ký, đúng trên phần dữ liệu căng thẳng quyết định H1. Thứ hai, với khoảng 28 cửa sổ, quy tắc "dưới 10 cửa sổ căng thẳng thì không kết luận" gần như chắc chắn bị kích hoạt, trong khi kế hoạch chưa có tính toán công suất và chưa định nghĩa "cửa sổ căng thẳng".

**Preliminary Recommendation**: Substantial revision required (Agent 6, Part 1: "Borderline — cần sửa đổi đáng kể").


## Priority Action Items

Thứ tự ưu tiên: Agent 3/6, rồi Agent 4, Agent 2, Agent 5, Agent 1. Các mục trùng giữa nhiều agent được gộp và ghi nguồn.

**CRITICAL**:
1. Ước lượng thử trên 2019–2025 (Quý 2) diễn ra trước khi đăng ký (Quý 4), và câu "biện minh chúng sau khi ước lượng thử" mở đường cho việc chọn tham số sau khi đã xem dữ liệu. Cách sửa: đăng ký trước, hoặc chỉ chạy thử trên dữ liệu mô phỏng hay giai đoạn trước 2012; khóa độ dài cửa sổ; báo cáo H1 hai tầng (A6-Part3.1/4.1; A3-2; A4-M9; A5-Impl1; A1-4).
2. Công suất: khoảng 28 cửa sổ trong khi ngưỡng là 10 cửa sổ căng thẳng. Cần định nghĩa "cửa sổ căng thẳng" (S_t là biến liên tục), đếm trước số cửa sổ căng thẳng dự kiến từ VN-Index, mô phỏng MDE. Nếu dưới 10 thì thiết kế lại hoặc đổi H1 thành bài toán ước lượng (A6-Part3.2/4.2; A3-1; A4-M1; A5-Sample1 & Docs1; A2-C3; A1-1).
3. Phương trình (5): khoảng 28 quan sát cho khoảng 7 tham số, nên HAC và bootstrap không đáng tin. Cần giới hạn X_t và dùng hiệu chỉnh mẫu nhỏ (A4-M2).
4. Đại lượng ước lượng của H1 chưa xác định: β0 hay β1; R_t thô hay chuẩn hóa; mẫu số chuẩn hóa lấy theo 21 cặp nào (A2-C1, C4; A3-3, 4; A4-M3; A1-2).
5. Tập M cho H3: cơ chế (ii)/(iii) chính là M6/M7 nên "loại khỏi M" làm thay đổi đối chứng; còn thiếu quy tắc gộp và chưa chọn biến thể chính cho cơ chế (i) (A2-C2; A3-8; A4-M7; A6-Part3.4; A1-14).
6. Holm 10% "cho bốn giả thuyết" chưa vận hành được: H1 dùng quy tắc ba điều kiện, H4 là thăm dò, các mức 5%, 10%, 95% lẫn lộn. Cần định nghĩa họ xác nhận {H1, H2, H3} với một p cho mỗi giả thuyết (A1-3 & Struct-2; A4-MT1; A6-Part3.5).
7. Chưa có bảng kế hoạch phân tích theo từng giả thuyết (biến kết quả, suy diễn, α, quy tắc quyết định) (A1-Struct1).
8. H2: "hệ số của tương quan đuôi âm" hiểu được hai cách, và có hai thước đo tương quan (A1-5; A6-Part3.4a).

**MAJOR**:
9. Phân phối rỗng chưa đủ ràng buộc, và có thể vẫn mang chênh lệch do phương sai (A4-M4; A3-6).
10. Mô hình chế độ chưa được đặc tả đủ: ngưỡng, tiêu chí thông tin, trường hợp K=3, hoán đổi nhãn (A4-M5; A1-6).
11. Phép phân rã β0−β1 gộp cả phần do biến động; cấu trúc điều tiết ↔ trung gian chưa nhất quán. Gợi ý dùng Gelbach (A4-M6; A3-7; A2-H2).
12. Không bác bỏ H0 đang được diễn giải thành "không đổi theo chế độ" và "1/N đủ dùng". Cần SESOI và TOST (A4-M8; A3-10; A1-18).
13. R_t phụ thuộc quy tắc chọn 36 tháng. Cần quy tắc thay thế và một thước đo không phụ thuộc quy tắc chọn (A3-5; A4-MT4).
14. Các yếu tố gây nhiễu theo thời gian (thể chế, phí, biên độ giá) trùng với giai đoạn căng thẳng (A3-9).
15. H4: chiều của độ phân tán chéo ngược với bầy đàn theo Christie–Huang; cần đưa H4 ra khỏi họ Holm (A3-11; A2-H4, H5).
16. Thiếu đặc tả CE: tần suất, năm hóa, lợi suất vượt trội hay lợi suất thô (A2-H7; A1-7; A6-Part3.3).
17. Chi phí giao dịch chưa có giá trị cơ sở; lưới siêu tham số và mô hình dự báo của M4 chưa nêu (A2-H8; A1-9, 10; A4-MT3).
18. Dữ liệu: chưa nêu tên nhà cung cấp, nguồn free-float, dữ liệu mã hủy niêm yết và quy tắc dựng rổ (A5-Sample2–4; A1-11; A4-M10).
19. Chưa có DMP, bảng mẫu, khung mã, bản nháp tệp OSF, codebook (A5-Docs2–5).
20. Thời gian của thí sinh: ba chương trình học khác và chín bản thảo (A5-Impl2).
21. Khối lượng tính toán của M5 (ABC-MCMC) và việc ước lượng Markov lại hằng tháng (A5-Impl3).
22. Mẫu kiểm tra sau đăng ký nằm ngoài khoảng "2007–2026" và chưa có quy tắc sử dụng (A2-Minor1; A5-Sample6; A1-21).
23. Thuật ngữ trôi nghĩa: rủi ro/bất định; biến động là kênh hay kiểm soát; các tên khác nhau của tương quan; "độ phân tán" chỉ hai khái niệm (A2-Term1–5).
24. Giấy phép dữ liệu thương mại có thể xung đột với cam kết tái lập (A5-Eth3).
25. Thiếu một số kiểm tra độ bền: placebo nhãn chế độ, bỏ lần lượt từng mô hình, bỏ lần lượt từng đợt căng thẳng, đặc tả MS khác (A4-R1–5).

**MINOR**:
26. Trang bìa ↔ mục 10 về người hướng dẫn; ô "Cơ quan công tác" bỏ trống; "Đại học Kinh tế Quốc Dân" (A1-minor 1–3; A5-Impl7).
27. "Từ khoảng năm thứ năm" nên sửa thành "từ đầu năm thứ sáu"; "cửa sổ độc lập" nên sửa thành "cửa sổ không chồng lấn" (A1-minor 4, 5; A3-12).
28. Câu hỏi 1 và 3 còn mở trong khi giả thuyết có hướng; nên rút gọn đoạn SR 11-7 và TT 83 (A3-minor 1, 2).
29. Ngưỡng N/T của M3 không bao giờ chạm; ES 95% trên cửa sổ 6 tháng chỉ có khoảng 6 điểm (A4-minor 2; A1-minor 15).
30. Trình tự chuyên đề 3 và việc đăng ký; số bài báo "hai đến ba" ↔ ba (A2-Minor 8, 9).
31. Tên tác giả Nguyễn/Nguyen 2026a/b; các từ viết tắt chưa giải thích (A1-minor 9, 13).

---

## Adversarial Referee Review & Registration Recommendation

## Agent 6: Phản biện đối kháng và khuyến nghị đăng ký (Adversarial Referee Review & Registration Recommendation)

*Phạm vi rà soát: mục 4.1, 4.2, 4.3.1–4.3.10, 4.4, 7.4 của `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/de-cuong-goc.md`, và văn bản trích từ Hình 1–2 trong `hinh-van-ban.txt`. Chuẩn áp dụng: OSF Registries cho nghiên cứu quan sát trên dữ liệu thứ cấp. Không sửa tệp nào.*

### Part 1 — Core Research Case

**Tóm tắt một câu:** Kế hoạch phân tích đo "rủi ro lựa chọn mô hình", tức mức hối tiếc về lợi suất tương đương chắc chắn khi chọn trước một trong bảy mô hình danh mục cho rổ 30 cổ phiếu HOSE. Kế hoạch kiểm định ba điều: mức hối tiếc có cao hơn ở chế độ căng thẳng (xác định bằng mô hình Markov) hay không (H1); nó có liên hệ với thanh khoản và tương quan đuôi hay không (H2), cùng phần thăm dò về bầy đàn (H4); và kết hợp mô hình hay danh mục vững chắc có giảm được nó sau chi phí giao dịch hay không (H3).

**Câu hỏi có quan trọng và trả lời được không?** Có quan trọng. Khái niệm được định nghĩa gọn và nhất quán: "*Rủi ro lựa chọn mô hình* là tổn thất kỳ vọng phát sinh khi nhà đầu tư phải chọn một mô hình trước lúc biết mô hình nào tốt nhất". Tuy vậy, câu hỏi khó trả lời được với dữ liệu hiện có. Chính PAP ước tính "khoảng 28 cửa sổ đánh giá độc lập", và "khủng hoảng tài chính toàn cầu chủ yếu phục vụ ước lượng chế độ". Như vậy các cửa sổ căng thẳng dùng để kiểm định gần như chỉ đến từ COVID-19 và đợt căng thẳng 2022. PAP lại tự đặt quy tắc "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Vì thế, khả năng cao là kết quả chính sẽ bị quy tắc của chính PAP xếp vào loại không kết luận.

**Nhận diện có hỗ trợ suy luận nhân quả không?** Không, và PAP thừa nhận đúng điều này: "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả". Lời văn ở chỗ khác lại vượt quá mức đó. Hình 1 viết "chế độ thị trường tác động lên rủi ro lựa chọn mô hình", "các biến kênh tác động lên chính quan hệ đó", và Câu hỏi 2 hỏi biến kênh "giải thích được bao nhiêu phần chênh lệch". Ngoài ra, giữa H1 và thước đo có một quan hệ cơ học. Chế độ căng thẳng được định nghĩa là "có phương sai điều kiện cao nhất". Trong khi đó $U_{m,t} = \mu_{m,t} - \frac{\rho}{2}\sigma^2_{m,t}$, nên chênh lệch CE giữa các mô hình tự động phóng to khi phương sai tăng.

**Mức độ ràng buộc của pre-specification:** chưa đủ. Nhiều thông số then chốt vẫn để ngỏ: lưới siêu tham số, quy tắc chọn siêu tham số, mô hình dự báo cho quan điểm của M4, ngưỡng xác suất lọc, mức chi phí giao dịch cơ sở, cặp mô hình dùng để chuẩn hóa mức hối tiếc, cách chọn giữa "trọng số Bayes" và "chỉ kết hợp các mô hình nằm trong tập tin cậy". Nghiêm trọng hơn, lịch trình cho thấy tác giả ước lượng thử trên chính phần dữ liệu chứa các đợt căng thẳng *trước* khi đăng ký.

**Xếp loại: Borderline — cần sửa đổi đáng kể (substantial revision needed).**

**Lý do:** Khung khái niệm rõ. Thiết kế có nhiều biện pháp tự kiểm soát tốt: phân phối rỗng, tập chỉ gồm mô hình tĩnh, quy tắc "không kết luận", khai báo dữ liệu đã xem. Nhưng tính "đăng ký trước" bị xói mòn ở hai điểm: các giai đoạn căng thẳng then chốt đã được xem, và kế hoạch còn ước lượng thử trên chúng trước khi khóa. Thêm vào đó, công suất của kiểm định chính gần như chắc chắn không đủ theo chính ngưỡng 10 cửa sổ mà PAP đặt ra. Nếu chưa sửa hai điểm này và chưa khóa các thông số còn để ngỏ, bản đăng ký chưa phải là một cam kết ràng buộc thực chất.

### Part 2 — Major Strengths

1. [MAJOR] **Định nghĩa khái niệm tách bạch và kiên định.** PAP phân biệt rủi ro mô hình, bất định mô hình và rủi ro lựa chọn mô hình. PAP cũng nói thẳng rằng "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro". Tương tự, PAP tách *khủng hoảng* (sự kiện lịch sử) khỏi *chế độ căng thẳng* (trạng thái thống kê), và chỉ kiểm định theo chế độ căng thẳng. Đây là nền tảng tốt cho việc đặt thước đo.
2. [MAJOR] **Minh bạch về dữ liệu đã xem.** PAP viết: "nên không thể khẳng định chưa từng thấy kết quả ở chế độ căng thẳng … và khai rõ những kết quả đã xem", và "báo cáo kết quả cả khi có lẫn khi không có M5". Hiếm PAP nào tự khai điều này. Đây là điểm cộng lớn về độ tin cậy, dù biện pháp xử lý đi kèm còn chưa đủ (xem Part 3).
3. [MAJOR] **Tự kiểm soát các tác động cơ học.** PAP có bốn biện pháp: (a) nêu rằng kỳ vọng của $R_t$ vẫn dương khi các mô hình ngang nhau và chuẩn hóa bằng sai số chuẩn bootstrap; (b) hiệu chuẩn β bằng phân phối rỗng sau khi "loại chênh lệch trung bình giữa các mô hình trong từng chế độ nhưng giữ nguyên tương quan chéo và biến động"; (c) lặp lại kiểm định trên tập tĩnh M1, M2, M3, M4, M6; (d) đặt ngưỡng VIF bằng 5 từ trước. Đây là những biện pháp mà một trọng tài tạp chí tốt sẽ đòi hỏi.
4. [MAJOR] **Thiết kế chống nhìn trước.** Chế độ được ước lượng theo cửa sổ mở rộng với xác suất lọc. Rổ cổ phiếu được xác định tại từng thời điểm "kể cả những mã đã hủy niêm yết". Kiểm định Bai–Perron "chỉ dùng để mô tả". Chọn CE làm thước đo chính có lập luận rõ (tỷ số Sharpe sai khi lợi suất vượt trội trung bình âm).
5. [MINOR] **Mỗi giả thuyết có khả năng đối lập và có quy tắc "không kết luận" đặt sẵn.** Ví dụ: "một quy tắc đơn giản như 1/N có thể thắng ổn định", hay "tương quan có thể tăng chỉ vì biến động tăng". Nhờ vậy, kết quả rỗng vẫn có giá trị diễn giải.

**Điểm mạnh dễ được tạp chí hàng đầu đánh giá cao nhất:** điểm 2 và 3. **Điểm mạnh đang được trình bày kém:**
- [MINOR] Phân phối rỗng (điểm 3b) là phần đáng giá nhất của thiết kế, nhưng chỉ được mô tả trong hai câu. Chưa rõ bootstrap theo khối dài bao nhiêu, và chưa rõ việc loại chênh lệch trung bình "trong từng chế độ" dùng phân loại chế độ nào (xác suất lọc hay ngưỡng).
- [MINOR] Việc khai báo dữ liệu đã xem đáng lẽ nên đi kèm một danh sách cụ thể các con số đã thấy, đính vào bản đăng ký.

### Part 3 — Major Weaknesses

1. [CRITICAL] **Tính "đăng ký trước" bị xói mòn trên đúng phần dữ liệu quyết định kết quả.** Bảng 5 ghi rằng ở "Quý 2: ước lượng thử bảy mô hình trên giai đoạn 2019--2025 để đo thời gian tính và số quan sát ở chế độ căng thẳng", còn đăng ký thì ở "Quý 4". Mục 4.3.6 viết thêm: "Các độ dài cửa sổ là giá trị dự kiến, và thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất". Giai đoạn 2019–2025 chứa hai đợt căng thẳng mà kiểm định H1 thực tế dựa vào, vì khủng hoảng tài chính toàn cầu chủ yếu dùng để ước lượng chế độ. Như vậy độ dài cửa sổ, siêu tham số và có thể cả ngưỡng đều có thể được chọn sau khi đã thấy kết quả ở chế độ căng thẳng. Mẫu kiểm tra sau đăng ký ("Dữ liệu phát sinh sau ngày đăng ký là mẫu kiểm tra riêng") chỉ dài vài tháng đến khoảng hai năm, tức chỉ vài cửa sổ 6 tháng, nên không cứu được tính xác nhận.
2. [CRITICAL] **Công suất không đủ, và quy tắc "không kết luận" gần như chắc chắn sẽ được kích hoạt.** Phép tính của chính PAP cho khoảng 28 cửa sổ. Ngưỡng là 10 cửa sổ ở chế độ căng thẳng. Với tỷ lệ thời gian căng thẳng điển hình và việc khủng hoảng tài chính toàn cầu nằm trong phần ước lượng, số cửa sổ căng thẳng nhiều khả năng dưới 10. Bản thân PAP chưa có bất kỳ phép tính số cửa sổ căng thẳng kỳ vọng hay hiệu ứng tối thiểu phát hiện được (MDE) nào. Ngoài ra, khái niệm "cửa sổ ở chế độ căng thẳng" chưa được định nghĩa, vì $S_t$ là "tỷ lệ số ngày" (biến liên tục). Cũng không thể ước lượng phương trình (5) với khoảng 28 quan sát cộng sai số chuẩn HAC, bootstrap khối và nhiều biến kênh mà vẫn có suy luận đáng tin. Các cửa sổ cũng không thực sự "độc lập": quy tắc chọn dùng 36 tháng nhìn lại, chồng lấn giữa các cửa sổ, và cửa sổ ước lượng 104 tuần cũng chồng lấn.
3. [MAJOR] **Thước đo chính chưa được đặc tả đến mức có thể tính lại.**
   - $\mu_{m,t}$ và $\sigma^2_{m,t}$ trên cửa sổ 6 tháng tính từ lợi suất ngày, tuần hay tháng? Nếu từ lợi suất tháng thì phương sai chỉ dựa trên 6 điểm.
   - Phép chuẩn hóa "chia … cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình" không nói rõ dùng cặp nào trong 21 cặp, hay lấy trung bình.
   - Mục 4.3.7 viết "β của $R_t$" mà không nói đó là $R_t$ đã chuẩn hóa hay chưa.
   - "36 tháng liền trước" ngoài mẫu được tính từ chuỗi tái cân bằng hằng tháng hay chuỗi cửa sổ không chồng lấn?

   Một bản đăng ký trên OSF phải đủ chi tiết để người khác tính lại đúng $R_t$.
4. [MAJOR] **H2 và H3 có quy tắc quyết định mơ hồ hoặc dịch chuyển được.**
   - (a) Câu "hệ số của tương quan đuôi âm" có hai cách đọc: hệ số của *tương quan đuôi âm* (lower-tail), hoặc *hệ số* của tương quan đuôi mang dấu âm. Phần lập luận ("tương quan cao làm các danh mục chỉ mua hội tụ") gợi ý cách đọc thứ hai, nhưng văn bản không chốt. PAP cũng có hai thước đo tương quan ("tương quan đuôi và tương quan hiệu chỉnh theo biến động") mà không nói thước đo nào thuộc kiểm định H2.
   - (b) Hình 1 mô tả biến kênh như biến điều tiết ("tác động lên chính quan hệ đó"), nhưng phương trình (5) không có số hạng tương tác. Phép đo $\beta_0-\beta_1$ là logic trung gian, và với biến kênh đo đồng thời thì phép đo này không có diễn giải "giải thích".
   - (c) Cơ chế (i) là "theo trọng số Bayes … *hoặc* chỉ kết hợp các mô hình nằm trong tập tin cậy", tức có hai lựa chọn chưa chốt. "Trọng số Bayes" cho các quy tắc danh mục cũng chưa có hàm hợp lý được định nghĩa.
   - (d) Cơ chế (ii) và (iii) trùng với M6 và M7 ("Khi kiểm định H3, đề tài loại cơ chế (ii) và (iii) khỏi *M*"), nên khi kiểm định H3 thì tập so sánh và đối chứng "chọn một mô hình" thay đổi so với lúc kiểm định H1.
   - (e) H3 đòi điều kiện đồng thời trên ba tiêu chí cho ba cơ chế, nhưng chưa có quy tắc gộp: một cơ chế đạt là đủ, hay phải cả ba?
5. [MAJOR] **Khung suy luận thống kê không nhất quán.** "Holm (1979) ở mức 10% cho bốn giả thuyết" có ba vấn đề:
   - Họ kiểm định gồm cả H4, dù H4 được gọi là "thăm dò".
   - H1 được quyết định bằng một hội ba điều kiện (phân vị 95% của phân phối rỗng, khoảng tin cậy loại trừ 0, cùng dấu với $D_t$), không phải bằng một giá trị p, nên không rõ Holm được áp vào đâu.
   - H2 có hai hệ số và H3 có nhiều tiêu chí và cơ chế.

   Các mức ý nghĩa cũng lẫn lộn: 10% cho MCS, 10% cho Holm, 95% cho phân phối rỗng, và khoảng tin cậy chưa ghi mức. Vai trò của "tỷ số Sharpe hiệu chỉnh (Bailey và López de Prado, 2014)" trong kiểm định chính cũng không rõ.

**Điểm yếu dễ bị soi kỹ nhất:** điểm 1. Một người rà soát đăng ký sẽ chỉ ra ngay rằng việc ước lượng thử trên 2019–2025 rồi mới đăng ký làm mất ý nghĩa của "đăng ký trước" cho H1.

**Mức độ nghiêm trọng:**
- Điểm 1 và 2 *không nhất thiết làm hỏng hẳn thiết kế*, nhưng phải thiết kế lại phần xác nhận (xem Part 4). Nếu giữ nguyên, kết quả chính của luận án sẽ không thể tuyên bố là đã được đăng ký trước một cách có ý nghĩa.
- Điểm 3, 4 và 5 *sửa được trước khi đăng ký* bằng cách đặc tả thêm.

### Part 4 — Required Revisions Before Registration

1. [CRITICAL] **Đảo thứ tự giữa ước lượng thử và đăng ký, hoặc tách phần xác nhận khỏi dữ liệu đã xem.**
   - *Phải đổi:* (a) Đăng ký trước khi ước lượng thử ở Quý 2. Nếu cần ước lượng thử để đo thời gian tính, chỉ chạy trên dữ liệu mô phỏng hoặc trên giai đoạn trước 2019 không chứa các đợt căng thẳng dùng để kiểm định. (b) Khóa độ dài cửa sổ (104 tuần, 6 tháng, 36 tháng) ngay trong bản đăng ký, bỏ câu "sẽ biện minh chúng sau khi ước lượng thử". (c) Khai báo rõ rằng các cửa sổ căng thẳng 2020 và 2022 là *đã xem*, và báo cáo kết quả H1 theo hai tầng: toàn mẫu, và phần không chứa dữ liệu đã xem (trước 2019 cộng dữ liệu sau đăng ký).
   - *Vì sao:* nếu không làm vậy, mọi lựa chọn thiết kế đều có thể bị coi là hệ quả của việc đã thấy kết quả.
   - *Cải thiện:* biến lời "khai rõ những kết quả đã xem" thành một cơ chế bảo vệ có thể kiểm chứng.
2. [CRITICAL] **Bổ sung phân tích công suất và định nghĩa chính xác "cửa sổ căng thẳng".**
   - *Phải đổi:* (a) Định nghĩa cửa sổ căng thẳng, ví dụ $S_t$ vượt một ngưỡng ghi rõ. (b) Ghi giá trị ngưỡng xác suất lọc. (c) Ước tính trước số cửa sổ căng thẳng kỳ vọng nằm ngoài phần ước lượng (dùng dữ liệu VN-Index, không dùng kết quả danh mục). (d) Mô phỏng MDE của β trong (5) với khoảng 28 quan sát. (e) Nếu số cửa sổ căng thẳng kỳ vọng dưới 10, thiết kế lại phân tích chính thay vì chấp nhận "không kết luận". Các phương án gồm: đặt cửa sổ trượt hằng tháng làm phân tích chính, có hiệu chỉnh phụ thuộc; dùng cửa sổ 3 tháng; hoặc hạ tham vọng H1 xuống ước lượng kích thước hiệu ứng.
   - *Vì sao:* thiết kế tự dự báo kết quả "không kết luận" thì người rà soát sẽ hỏi PAP này cam kết điều gì.
   - *Cải thiện:* có lý lẽ định lượng cho tính khả thi của kiểm định chính.
3. [MAJOR] **Đặc tả đầy đủ thước đo $R_t$, $D_t$ và quy tắc chọn.**
   - *Phải đổi:* ghi tần suất lợi suất dùng tính $\mu$ và $\sigma^2$ trong (1); công thức chuẩn hóa cụ thể (cặp nào hay trung bình nào, số lần bootstrap, độ dài khối); và chọn rõ biến phụ thuộc chính của H1 là $R_t$ đã chuẩn hóa hay chưa. Nên đăng ký kèm *mã nguồn* tính $R_t$, chạy trên dữ liệu giả lập.
   - *Vì sao:* đây là kết quả chính, nên không thể còn độ tự do trong cách tính.
   - *Cải thiện:* người khác tái lập được, và các lựa chọn phân tích được khóa.
4. [MAJOR] **Khóa toàn bộ các thông số đang để ngỏ.**
   - *Phải đổi:* liệt kê giá trị cụ thể của lưới siêu tham số cho M2, M4, M5, M6, M7 và quy tắc chọn; mô hình dự báo cho quan điểm của M4; quy tắc đặt cận cho M6; mức chi phí giao dịch cơ sở (theo từng thời kỳ phí và thuế); quy tắc xử lý biên độ giá; chọn một trong hai phương án của cơ chế (i), hoặc đăng ký cả hai và tính vào họ so sánh bội.
   - *Vì sao:* mỗi thông số để ngỏ là một nhánh của "khu vườn rẽ nhánh".
   - *Cải thiện:* bản đăng ký thực sự ràng buộc.
5. [MAJOR] **Sửa quy tắc quyết định cho H2 và H3, và làm cho khung so sánh bội nhất quán.**
   - *Phải đổi:*
     - (a) Viết lại H2 thành dấu kỳ vọng rõ ràng cho từng biến, có ký hiệu, và chỉ định một thước đo tương quan chính.
     - (b) Thống nhất Hình 1 với phương trình (5): hoặc thêm số hạng tương tác $S_t \times X_t$ (điều tiết), hoặc đổi lời văn thành "liên hệ có điều kiện" (bỏ "tác động", "giải thích").
     - (c) Với H3, cố định tập so sánh và nêu quy tắc gộp giữa các cơ chế.
     - (d) Định nghĩa họ giả thuyết xác nhận (H1, H2, H3), đưa H4 ra khỏi họ Holm, và quy mọi quy tắc quyết định về một giá trị p hoặc một mức tin cậy thống nhất.
   - *Vì sao:* đây là những chỗ trọng tài sẽ dùng để nói PAP "có thể đọc theo cách nào cũng thắng".
   - *Cải thiện:* quy tắc quyết định trở nên kiểm chứng được và đối xứng.
6. [MINOR] **Xác nhận dữ liệu và kéo khớp mốc thời gian.**
   - *Phải đổi:* nêu tên nhà cung cấp dữ liệu thương mại; xác nhận dữ liệu vốn hóa tự do chuyển nhượng và các mã đã hủy niêm yết có sẵn từ 2007; xác nhận chuỗi lợi suất trái phiếu chính phủ 1 năm có từ 2007. Đồng bộ các mốc: mẫu "2007 đến 2026" nhưng đăng ký ở Quý 4 năm thứ nhất (muộn hơn 2026), vậy dữ liệu từ cuối 2026 đến ngày đăng ký thuộc tập nào?
   - *Vì sao:* nếu thiếu dữ liệu năm 2007–2010, số cửa sổ giảm thêm.
   - *Cải thiện:* kế hoạch dự phòng "thu hẹp rổ cổ phiếu hoặc giai đoạn mẫu" sẽ dựa trên căn cứ rõ ràng.

### Part 5 — Registration Fit and Strategic Positioning

- [MINOR] **Mức độ phù hợp với OSF:** phù hợp. Đây là nghiên cứu quan sát trên dữ liệu thứ cấp công khai, không phải RCT, nên các sổ đăng ký AEA RCT Registry hay ClinicalTrials không thích hợp. Nên dùng mẫu đăng ký trước dành cho *phân tích dữ liệu thứ cấp* trên OSF, vì mẫu này có mục bắt buộc khai báo mức tiếp xúc trước với dữ liệu, đúng với tình huống của đề tài [UNVERIFIED — tác giả phải xác nhận tên và nội dung mẫu hiện hành trên OSF]. Ở chế độ "khóa có dấu thời gian", cần đính kèm mã nguồn và danh sách kết quả đã xem.
- [MAJOR] **Tham vọng chưa khớp với khả năng của thiết kế.** Đề tài vừa muốn kiểm định chênh lệch theo chế độ (H1), vừa đo "phần chênh lệch do biến kênh giải thích" (H2), vừa đánh giá ba cơ chế trong chế độ căng thẳng (H3), và cả phần thăm dò (H4), trên khoảng 28 cửa sổ với rất ít cửa sổ căng thẳng. H2 và H3 đều được kiểm định *bên trong* chế độ căng thẳng hoặc theo chênh lệch giữa hai chế độ, nên chịu cùng ràng buộc công suất, còn nặng hơn H1.
- [MAJOR] **Tái định vị khuyến nghị:**
  - (a) Đặt H1 là giả thuyết xác nhận duy nhất. H2 và H3 chuyển thành giả thuyết thứ cấp, báo cáo kích thước hiệu ứng kèm khoảng tin cậy. H4 để ngoài phần đăng ký xác nhận.
  - (b) Đóng góp mạnh nhất có thể là *thước đo* (mức hối tiếc chuẩn hóa kèm phân phối rỗng) cùng một nghiên cứu mô phỏng cho thấy thước đo phân biệt được tình huống "bất định thật" với "nhiễu cơ học". Đóng góp này không phụ thuộc vào việc Việt Nam có đủ giai đoạn căng thẳng hay không.
  - (c) Cân nhắc mở rộng sang sàn HNX hoặc thêm một vài thị trường đối chiếu để tăng số giai đoạn căng thẳng độc lập. Nếu giữ phạm vi "chỉ HOSE", cần nói thẳng rằng đây là nghiên cứu ước lượng, không phải kiểm định.
- [MINOR] Câu nhận định khoảng trống ("chưa có nghiên cứu nào đo rủi ro lựa chọn mô hình theo chế độ thị trường … trên thị trường chứng khoán Việt Nam") đã có giới hạn phạm vi tìm kiếm trung thực. Tuy vậy, PAP cũng thừa nhận "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn", và phạm vi tìm kiếm chưa gồm Scopus, Web of Science và tạp chí tiếng Việt. Vì vậy bản đăng ký không nên dựa vào tuyên bố tính mới này cho đến khi tìm kiếm xong. Tôi không khẳng định có hay không có công trình trước đó [UNVERIFIED — tác giả phải xác nhận].

### Part 6 — Adversarial Questions to the Research Team

1. [CRITICAL] Kế hoạch có bước "ước lượng thử bảy mô hình trên giai đoạn 2019--2025" ở Quý 2, rồi mới đăng ký ở Quý 4, và nói độ dài cửa sổ sẽ được "biện minh … sau khi ước lượng thử". Vậy chính xác thông số nào trong bản đăng ký có thể bị ảnh hưởng bởi những gì nhóm đã thấy, và cơ chế nào ngăn điều đó?
2. [CRITICAL] Ngoài phần mẫu dùng để ước lượng chế độ, nhóm kỳ vọng có bao nhiêu cửa sổ 6 tháng ở chế độ căng thẳng? Nếu con số đó dưới 10, như phép tính khoảng 28 cửa sổ gợi ý, thì có phải PAP đang đăng ký một kết quả "không kết luận" từ trước? Hiệu ứng tối thiểu phát hiện được (MDE) của β là bao nhiêu?
3. [MAJOR] Chế độ căng thẳng được định nghĩa bằng phương sai cao, còn CE trừ đi $\frac{\rho}{2}\sigma^2$. Phép chuẩn hóa bằng sai số chuẩn bootstrap và phân phối rỗng loại bỏ được bao nhiêu phần của quan hệ cơ học giữa phương sai và mức hối tiếc? Nhóm có kết quả mô phỏng nào cho thấy β bằng 0 khi không có rủi ro lựa chọn thật không?
4. [MAJOR] "Hệ số của tương quan đuôi âm" nghĩa là gì: hệ số mang dấu âm, hay hệ số của tương quan ở đuôi dưới? Trong hai thước đo tương quan, thước đo nào là thước đo chính, và tương quan đuôi được tính thế nào trên một cửa sổ 6 tháng?
5. [MAJOR] Holm được áp dụng cho "bốn giả thuyết", trong khi H1 được quyết định bằng một hội ba điều kiện không phải giá trị p, và H4 lại là giả thuyết thăm dò. Giá trị p nào của H1, H2, H3 đi vào thủ tục Holm?
6. [MAJOR] Khi kiểm định H3, M6 và M7 bị loại khỏi *M*. Vậy nhà đầu tư "chọn một mô hình" chọn từ năm mô hình hay bảy mô hình? "Trọng số Bayes" cho các quy tắc danh mục dùng hàm hợp lý nào? Và nếu chỉ một trong ba cơ chế đạt tiêu chí thì H3 có được coi là được ủng hộ không?
7. [MAJOR] Nhà cung cấp dữ liệu nào bảo đảm có giá điều chỉnh, các mã đã hủy niêm yết và vốn hóa tự do chuyển nhượng theo thời điểm từ năm 2007? Nếu mẫu thực tế chỉ bắt đầu từ khoảng 2010, còn lại bao nhiêu cửa sổ tính được mức hối tiếc?
8. [MINOR] Quy tắc chọn "mô hình có CE cao nhất trong 36 tháng liền trước" là một quy tắc chạy theo mô hình vừa thắng. Kết quả H1 có nhạy với quy tắc chọn không? Ví dụ: mặc định 1/N, hoặc chọn trong tập tin cậy. Nếu nhạy, đâu là lý do để đăng ký riêng quy tắc này làm quy tắc chính?

---

## Internal Consistency, Hypotheses & Outcomes

## Agent 2: Internal Consistency, Hypotheses & Outcomes

Phạm vi rà soát: chỉ hai tệp được giao, gồm `de-cuong-goc.md` và `hinh-van-ban.txt`. Đây là nghiên cứu quan sát trên dữ liệu thị trường công khai. Vì vậy các hạng mục dành cho RCT (ITT/IV/LATE, phân nhóm ngẫu nhiên, nhánh can thiệp) và cho khảo sát (đối chiếu kết quả với câu hỏi khảo sát) được ghi **không áp dụng**. Lý do: đề cương nói rõ "không dùng khảo sát hay phương pháp định tính" (4.3.3). Ở đây, nguồn của từng kết quả được đối chiếu với bản ghi thị trường (giá, khối lượng, VN-Index, lợi suất trái phiếu), không đối chiếu với câu hỏi khảo sát. Mục 8 (đối chiếu tài liệu kèm theo) chỉ áp dụng cho Hình 1–2. Đề cương không đính kèm tệp tính công suất, công cụ thu thập hay tệp đăng ký OSF; tệp OSF sẽ được lập ở quý 4 năm 1.

### Critical Inconsistencies

1. [CRITICAL] 4.3.7, phương trình (5) và quy tắc H~1~ ↔ 4.3.7, đoạn phân rã β~0~ − β~1~ | Ước lượng lượng chính của H~1~ không xác định được. Đề cương viết "hồi quy các thước đo rủi ro mô hình theo biến chế độ và các biến kênh", tức β của H~1~ được ước lượng khi **có** X~t~. Nhưng đoạn sau định nghĩa "β~0~ và β~1~ là hệ số β của phương trình (5) khi không có và khi có X~t~". Quy tắc ủng hộ H~1~ chỉ ghi "β của R~t~ dương và vượt phân vị 95%…" mà không nói đó là β~0~ hay β~1~. Theo Hình 1, H~1~ là tác động tổng của chế độ, còn biến kênh "giải thích một phần chênh lệch". Nếu H~1~ dùng β~1~ (đã kiểm soát biến kênh) thì kiểm định H~1~ đánh giá thấp chính hiệu ứng mà H~2~ phân rã. | Giả thuyết chính có hai cách đọc và có thể cho kết luận ngược nhau. Cần ghi rõ: H~1~ dùng β~0~ (chỉ kiểm soát biến động thực hiện, hoặc không kiểm soát gì), còn β~1~ chỉ dùng cho H~2~.

2. [CRITICAL] 4.3.8, "Khi kiểm định H~3~, đề tài loại cơ chế (ii) và (iii) khỏi *M*" ↔ Bảng 3 (M~6~ "Danh mục vững chắc với nhiều niềm tin tiên nghiệm", M~7~ "Giảm tỷ trọng rủi ro theo xác suất chế độ căng thẳng") | Cơ chế (ii) "danh mục vững chắc… (Garlappi và cộng sự, 2007)" chính là M~6~, và cơ chế (iii) "quy tắc chuyển chế độ theo Kritzman và cộng sự (2012)" chính là M~7~. Hai cơ chế giảm thiểu đồng thời là thành viên của tập *M*. Khi loại chúng ra, tập *M* của H~3~ chỉ còn 5 mô hình, trái với "|*M*| = 7" ở công thức (2)–(3). Đối chứng "so với chọn một mô hình" cũng không còn rõ: chọn trong 7 hay trong 5 mô hình? Ngoài ra, cơ chế (i) (kết hợp mô hình) cũng không thuộc *M*, nên mức hối tiếc của nó cũng có thể âm, nhưng câu văn chỉ nhắc (ii) và (iii). | Quy tắc ủng hộ H~3~ ("mức hối tiếc thấp hơn… so với chọn một mô hình") phụ thuộc trực tiếp vào cách định nghĩa *M* và đối chứng. Cần lập bảng nêu tập *M* cho từng giả thuyết, và tách M~6~/M~7~ (thành viên tập cạnh tranh) khỏi cơ chế (ii)/(iii) (chiến lược giảm thiểu), hoặc giải thích vì sao chúng trùng nhau.

3. [CRITICAL] 4.3.7 (định nghĩa S~t~ là "tỷ lệ số ngày trong cửa sổ có xác suất lọc… vượt ngưỡng", một biến liên tục) ↔ 4.3.8 ("H~3~ được ủng hộ khi, ở chế độ căng thẳng…") và 4.3.10 ("Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10…") | Phép kiểm định H~1~/H~2~ dùng S~t~ liên tục. Trong khi đó, H~3~ và quy tắc "không kết luận" lại cần phân loại nhị phân từng cửa sổ 6 tháng là "căng thẳng" hay "bình thường", và đề cương không có quy tắc phân loại này (ví dụ S~t~ > 0,5?). | Ngưỡng 10 cửa sổ là điều kiện tiên quyết để gọi mọi kết quả là ủng hộ hay bác bỏ, nên phải định nghĩa được trước. Với khoảng 28 cửa sổ (4.3.6), cách phân loại sẽ quyết định kết luận.

4. [CRITICAL] 4.3.6 ("phân tích chính chia D~t~ và R~t~ cho sai số chuẩn bootstrap…") ↔ phương trình (4), Bảng 2 (kết quả chính là "chênh lệch lợi suất tương đương chắc chắn") và quy tắc H~1~ ("β của R~t~") | Kết quả chính có hai phiên bản: mức hối tiếc thô theo (4) và mức hối tiếc chuẩn hóa ("phân tích chính"). Bảng 2 và quy tắc ra quyết định không nói phiên bản nào được dùng. Mẫu số chuẩn hóa ("sai số chuẩn bootstrap của chênh lệch… giữa các mô hình") cũng không xác định: có 21 cặp mô hình, đề cương không nói lấy cặp nào hay lấy trung bình. | Biến phụ thuộc chính của giả thuyết chính chưa được định nghĩa duy nhất. Cần ký hiệu riêng (ví dụ R~t~^\*^ = R~t~/s~t~), viết công thức cho s~t~, và ghi rõ R~t~^\*^ là kết quả chính trong Bảng 2 và trong quy tắc H~1~.

### Hypothesis or Outcome Coverage Gaps

1. [MAJOR] H~2~ | Không chỉ định biến phụ thuộc. Quy tắc "H~2~ được ủng hộ khi hệ số của độ phi thanh khoản dương, hệ số của tương quan đuôi âm…" không nói Y~t~ là D~t~ hay R~t~. Lý giải trong Bảng 2 ("thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau", "các danh mục chỉ mua hội tụ") gợi ý độ phân tán D~t~, nhưng kết quả chính của toàn đề tài là R~t~. | Ghi rõ Y~t~ của H~2~ và lý do chọn. Nếu dùng cả hai, cần nêu quy tắc khi hai kết quả mâu thuẫn.

2. [MAJOR] H~2~, phần "phần chênh lệch giữa hai chế độ do biến kênh giải thích" (Bảng 2, Câu hỏi 2) | Đại lượng β~0~ − β~1~ chỉ được báo cáo, không có tiêu chí ủng hộ hay bác bỏ. Ngoài ra, X~t~ "luôn có" biến động thực hiện. Như vậy β~0~ ("khi không có X~t~") cũng bỏ luôn biến động thực hiện, và β~0~ − β~1~ gộp phần do biến động giải thích. Điều này trái với Câu hỏi 2 ("Sau khi kiểm soát biến động thực hiện… giải thích được bao nhiêu phần"). | Định nghĩa β~0~ là phương trình chỉ có S~t~ và biến động thực hiện, β~1~ là phương trình thêm các biến kênh. Báo cáo tỷ lệ (β~0~ − β~1~)/β~0~ kèm quy tắc diễn giải.

3. [MAJOR] H~2~ khi có đa cộng tuyến | 4.3.7 quy định: khi VIF > 5 thì "báo cáo hai phương trình tách riêng và không diễn giải riêng từng hệ số". Quy tắc ủng hộ H~2~ lại dựa trên dấu của *từng* hệ số. Không có quy tắc quyết định thay thế cho trường hợp này, và cũng không nói "hai phương trình tách riêng" là hai phương trình nào. | Nêu quy tắc ra quyết định cho nhánh có đa cộng tuyến, ví dụ mỗi biến kênh một phương trình, kèm hiệu chỉnh so sánh bội.

4. [MAJOR] H~4~ | Bảng 2 ghi hai thước đo ("Độ phân tán chéo của lợi suất; thước đo bầy đàn"), nhưng 4.3.7 chỉ định nghĩa biến "độ phân tán chéo của lợi suất (Christie và Huang, 1995; Chang và cộng sự, 2000)", tức không rõ dùng CSSD hay CSAD. "Thước đo bầy đàn" thứ hai không được mô tả. Hướng tác động cũng mâu thuẫn với khung bầy đàn. Theo Christie–Huang và Chang, bầy đàn biểu hiện bằng độ phân tán chéo **thấp**, nhưng H~4~ dự báo "độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao", còn 4.4 gọi độ phân tán chéo là "một thước đo bầy đàn ở cấp thị trường". | Chọn một thước đo (CSSD hoặc CSAD) và một đặc tả. Giải thích vì sao độ phân tán cao, tức ngược với bầy đàn, lại là kênh "bầy đàn", hoặc đổi dấu hay tên giả thuyết.

5. [MAJOR] H~4~ ↔ quy tắc hiệu chỉnh so sánh bội | H~4~ được dán nhãn "(thăm dò)", và đề cương viết "Đề tài chỉ báo cáo H~4~ như kết quả thăm dò", nhưng 4.3.10 lại "hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết". Một giả thuyết thăm dò không có quy tắc quyết định thì không thể nằm trong họ kiểm định xác nhận. | Áp Holm cho họ xác nhận H~1~–H~3~. Đưa H~4~ ra ngoài họ, hoặc lập họ riêng có nhãn thăm dò.

6. [MAJOR] Họ giả thuyết ↔ quy tắc Holm | Holm cần một giá trị p cho mỗi giả thuyết. Quy tắc H~1~ gồm ba điều kiện (phân vị 95% của phân phối rỗng, khoảng tin cậy loại trừ 0, D~t~ cùng dấu); H~2~ gồm hai hệ số; H~3~ gồm ba tiêu chí (CE, hối tiếc, MDD). Đề cương không nói p-value nào đi vào Holm, cũng không nêu mức tin cậy của các khoảng tin cậy bootstrap (90% hay 95%). Mức 10% của Holm cũng không khớp với "phân vị 95%" một phía của phân phối rỗng. | Với mỗi giả thuyết, nêu một thống kê kiểm định và một p-value duy nhất cho Holm. Các điều kiện còn lại trở thành tiêu chí phụ. Thống nhất mức ý nghĩa giữa các phần.

7. [MAJOR] Lợi suất tương đương chắc chắn U~m,t~ (thước đo nền của mọi kết quả) | Đề cương không nói tần suất lợi suất dùng để tính μ~m,t~ và σ²~m,t~ trên cửa sổ đánh giá 6 tháng (ngày, tuần hay tháng). Nếu dùng tháng thì chỉ có 6 quan sát. ES 95% được định nghĩa theo "5% số ngày xấu nhất", nên ngầm hiểu là lợi suất ngày, nhưng U~m,t~ không ghi. Đề cương cũng không nói có quy đổi theo năm hay không, trong khi ρ = 5 chỉ có nghĩa khi đơn vị được xác định. | Ghi rõ tần suất, cách quy đổi theo năm và số quan sát trên mỗi cửa sổ.

8. [MAJOR] Chi phí giao dịch | Mọi kết quả chính đều tính "sau chi phí giao dịch", nhưng 4.3.8 chỉ nói "tham số hóa chi phí giao dịch và kiểm tra độ nhạy". Không có giá trị cơ sở, và tham số này cũng không có trong danh sách tệp đăng ký (4.3.5: "độ dài các cửa sổ, siêu tham số…, số chế độ và ngưỡng xác suất lọc, mức ý nghĩa…"). | Đưa giá trị cơ sở của chi phí giao dịch (theo thời kỳ, như 4.3.3 đã hứa ghi nguồn) vào danh sách đăng ký.

9. [MAJOR] H~3~ | Bảng 2 nêu tiêu chí "mức hối tiếc và độ sụt giảm tối đa thấp hơn, lợi suất tương đương chắc chắn cao hơn", trong khi 4.3.8 yêu cầu "độ sụt giảm tối đa **không cao hơn**". Cơ chế (i) cũng chưa được xác định: "theo trọng số Bayes… **hoặc** chỉ kết hợp các mô hình nằm trong tập tin cậy", tức có hai biến thể mà không chọn biến thể chính. Không rõ H~3~ được ủng hộ khi một, hai hay cả ba cơ chế đạt tiêu chí. | Thống nhất tiêu chí MDD. Chọn một biến thể chính cho cơ chế (i). Nêu cách tổng hợp kết quả qua ba cơ chế (từng cơ chế riêng có hiệu chỉnh bội, hay "ít nhất một").

10. [MAJOR] Hiệu chỉnh thiên lệch chọn lọc cho H~3~ | Giả thuyết đối lập của H~3~ (4.3.2) được kiểm định "sau hiệu chỉnh thiên lệch chọn lọc (Bailey và López de Prado, 2014)". Nhưng 4.3.7 chỉ áp tỷ số Sharpe hiệu chỉnh, trong khi 4.3.6 hạ Sharpe xuống thước đo phụ và chỉ báo cáo nó "ở các cửa sổ có lợi suất vượt trội trung bình dương", tức gần như loại khỏi chế độ căng thẳng. Tiêu chí H~3~ dùng CE, không có hiệu chỉnh nào. | Nêu cách hiệu chỉnh thiên lệch chọn lọc cho CE, hoặc bỏ khẳng định rằng H~3~ được kiểm định sau hiệu chỉnh này.

11. [MAJOR] Biến kênh (X~t~) | Đề cương không nêu cách xây dựng, cửa sổ và cấp độ tính. Amihud tính cho cấp thị trường hay cho rổ 30 mã, theo ngày rồi lấy trung bình trong cửa sổ? "Tương quan đuôi" lấy ngưỡng nào, giữa các cặp cổ phiếu hay với chỉ số? "Tương quan hiệu chỉnh theo biến động" theo Forbes–Rigobon cần một giai đoạn tham chiếu nhưng không được nêu. Cũng không rõ H~2~ dùng tương quan đuôi hay tương quan hiệu chỉnh. | Viết công thức và nguồn dữ liệu cho từng biến kênh, và chỉ định biến tương quan dùng cho H~2~.

12. [MAJOR] Biến thăm dò nằm trong hồi quy xác nhận | 4.3.7 đưa "độ phân tán chéo của lợi suất" (biến của H~4~) vào X~t~ của phương trình (5), tức phương trình dùng cho cả H~1~ (nếu dùng β~1~) và H~2~. Như vậy biến thăm dò ảnh hưởng đến ước lượng xác nhận. | Tách đặc tả xác nhận (H~1~/H~2~) khỏi đặc tả thăm dò (thêm biến H~4~).

13. [MAJOR] Kết quả phụ D~t~ ↔ quy tắc H~1~ | Bảng 2 xếp độ phân tán mô hình là "Kết quả phụ", nhưng quy tắc H~1~ yêu cầu "β của D~t~ cùng dấu" làm điều kiện cần. Như vậy kết quả phụ trở thành điều kiện xác nhận, mà không được xét trong hiệu chỉnh bội. | Hoặc nâng D~t~ thành một phần của kết quả chính, hoặc bỏ nó khỏi điều kiện ủng hộ.

14. [MAJOR] Định nghĩa "chế độ bình thường" khi có ba chế độ | 4.3.4 cho phép "hai hoặc ba" chế độ và chỉ định nghĩa chế độ căng thẳng. Nếu có ba chế độ, nhóm tham chiếu của β (mà đề cương mô tả là "chênh lệch… giữa chế độ căng thẳng và chế độ bình thường") thực chất gộp hai chế độ không căng thẳng. Đề cương cũng không có quy tắc cho trường hợp chế độ có phương sai cao nhất không có lợi suất kỳ vọng thấp hơn. | Định nghĩa nhóm tham chiếu cho cả hai trường hợp số chế độ, và quy tắc gán nhãn dự phòng.

15. [MINOR] M~4~ | "Quan điểm của M~4~ lấy từ một mô hình dự báo đơn giản", nhưng không nói mô hình nào. Siêu tham số "từ một lưới cho trước, bằng cùng một quy tắc" chưa nêu lưới và quy tắc (đề cương hẹn cố định khi đăng ký). | Liệt kê ít nhất dạng mô hình dự báo và tiêu chí chọn siêu tham số.

16. [MINOR] Câu hỏi 3 ↔ H~3~ | Câu hỏi 3 hỏi chung "Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?", còn H~3~ chỉ kiểm định "Ở chế độ căng thẳng". Phần chế độ bình thường không có giả thuyết hay tiêu chí tương ứng. | Hoặc thu hẹp câu hỏi 3, hoặc ghi phân tích ở chế độ bình thường là mô tả hay thăm dò.

17. [MINOR] Bảng 1 (bốn khoảng trống) ↔ 4.3.2 ("Từ bốn khoảng trống ở Bảng 1, đề tài đề xuất… bốn giả thuyết") | Khoảng trống và giả thuyết không ánh xạ một-một. Các khoảng trống (1)–(3) cùng dẫn tới H~1~, khoảng trống (4) dẫn tới H~4~, còn H~2~ (thanh khoản, tương quan) và H~3~ (giảm thiểu) không có khoảng trống tương ứng. | Ghi rõ ánh xạ khoảng trống → giả thuyết, hoặc bỏ cách diễn đạt gợi ý tương ứng 4–4.

### Terminology Drift

1. [MAJOR] "Rủi ro lựa chọn mô hình" ↔ "bất định mô hình" ↔ "rủi ro mô hình" | 4.1 định nghĩa ba khái niệm riêng và khẳng định "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro". Thế nhưng Bảng 2 xếp chúng làm thước đo của H~1~ ("Rủi ro lựa chọn mô hình"). Hình 1 (hinh-van-ban.txt) đặt "Độ phân tán D~t~ | Tập tin cậy mô hình" trong ô "Rủi ro lựa chọn mô hình". 4.3.7 viết "hồi quy các thước đo **rủi ro mô hình**" với Y~t~ = D~t~ hoặc R~t~. 4.4 viết "đề tài đo **mức bất định** khi chọn mô hình". | Chỉ gọi R~t~ là "rủi ro lựa chọn mô hình", gọi D~t~ và kích thước MCS là "chỉ báo bất định mô hình", và sửa "thước đo rủi ro mô hình" ở 4.3.7 cùng Hình 1 theo đó.

2. [MAJOR] "Biến động" như biến kênh ↔ "biến động thực hiện" như biến kiểm soát | Mục tiêu (iii): "các biến kênh… gồm **biến động**, thanh khoản, tương quan cực trị và bầy đàn". Câu hỏi 2, H~2~, H~4~, 4.3.7 và Hình 1 ("Biến động thực hiện (kiểm soát)") lại coi biến động là biến kiểm soát, không phải biến kênh. | Bỏ "biến động" khỏi danh sách biến kênh ở mục tiêu (iii).

3. [MAJOR] "Tương quan cực trị" / "tương quan đuôi âm" / "tương quan đuôi" / "tương quan hiệu chỉnh theo biến động" | Câu hỏi 2, mục tiêu (iii), 4.3.1 và Chương 5 dùng "tương quan cực trị". Bảng 2 dùng "hệ số của tương quan đuôi âm". 4.3.7 dùng "tương quan đuôi và tương quan hiệu chỉnh theo biến động". Hình 1 dùng "tương quan đuôi". Cụm "hệ số của tương quan đuôi âm" vừa có thể hiểu là "tương quan ở đuôi âm" (lower-tail correlation), vừa có thể hiểu là "hệ số âm". 4.3.7 ("hệ số của tương quan đuôi âm") cho thấy nghĩa thứ hai, nhưng câu văn không phân biệt được. | Đặt một tên duy nhất, ví dụ "tương quan đuôi dưới ρ^−^~t~", và viết dấu kỳ vọng riêng: "hệ số của ρ^−^~t~ mang dấu âm".

4. [MAJOR] "Độ phân tán" dùng cho hai khái niệm khác nhau | "Độ phân tán mô hình" D~t~ (độ lệch chuẩn của U~m,t~ theo m) và "độ phân tán chéo của lợi suất" (biến kênh H~4~, đo độ phân tán giữa các cổ phiếu) cùng xuất hiện trong phương trình (5), một bên là Y~t~ và một bên nằm trong X~t~. Hình 1 viết tắt thành "Phân tán chéo". | Dùng hai tên tách bạch, ví dụ "độ phân tán giữa các mô hình (D~t~)" và "độ phân tán chéo của lợi suất cổ phiếu (CSAD~t~)".

5. [MAJOR] Cơ chế giảm thiểu ↔ mô hình trong tập *M* | "Danh mục vững chắc" vừa là M~6~ (Bảng 3), vừa là cơ chế (ii) (4.3.8), vừa là "Danh mục vững chắc" trong Hình 1. "Quy tắc chuyển chế độ" (4.3.8, Chương 6.3) ↔ "Quy tắc theo chế độ" (Hình 1) ↔ M~7~ "Giảm tỷ trọng rủi ro theo xác suất chế độ căng thẳng" ↔ "chiến lược theo chế độ" (4.3.5). | Phân biệt rõ đâu là thành viên tập cạnh tranh và đâu là cơ chế giảm thiểu, và dùng một tên nhất quán cho mỗi đối tượng (xem Critical #2).

6. [MINOR] "Kết hợp mô hình" | Các cách gọi khác nhau: "kết hợp mô hình" (Bảng 2, 4.4), "kết hợp các mô hình theo trọng số Bayes" (4.3.8), "trung bình hóa mô hình Bayes" (4.2), "kết hợp quy tắc 1/N với quy tắc trung bình-phương sai" (vai trò đối chứng). | Đặt tên riêng cho biến thể chính, biến thể theo MCS và đối chứng Tu–Zhou.

7. [MINOR] "Chọn một mô hình" (H~3~) ↔ "mô hình chọn trước *c*" (4.3.6) | Không rõ đối chứng của H~3~ là mô hình *c* theo quy tắc 36 tháng hay một mô hình cố định. | Dùng "mô hình chọn trước *c*" xuyên suốt.

8. [MINOR] "Cửa sổ độc lập ở chế độ căng thẳng" ↔ "giai đoạn căng thẳng độc lập" (4.3.10, 4.3.6) | Hai đơn vị đếm khác nhau, nhưng quy tắc "không kết luận" chỉ dùng đơn vị thứ nhất và cả hai đều chưa được định nghĩa. | Định nghĩa cả hai và nêu đơn vị nào kích hoạt quy tắc.

9. [MINOR] "Giá trị thiệt hại kỳ vọng mức 95%" (Bảng 2, 4.3.8) ↔ "Thiệt hại kỳ vọng" (Hình 1) | Hình 1 bỏ mức tin cậy. | Thống nhất tên đầy đủ.

10. [MINOR] Vai trò của tập tin cậy mô hình | Bảng 2 xếp nó là "Kết quả phụ". 4.3.6 viết "báo cáo kích thước tập như một thước đo mô tả". 4.4 đưa nó vào thủ tục giám sát ("đo độ phân tán và tập tin cậy mô hình định kỳ"). | Chọn một vai trò (mô tả) và ghi thống nhất trong Bảng 2.

### Minor Inconsistencies

1. [MAJOR] 4.3.5 và 4.4 ("Dữ liệu phát sinh sau ngày đăng ký là mẫu kiểm tra riêng") ↔ 4.3.3 và 4.4 ("Giai đoạn mẫu dự kiến từ 2007 đến 2026") ↔ Bảng 5 ("Quý 4 [năm 1]: đăng ký trước") | Đề cương ký ngày 30/09/2026, nên ngày đăng ký (quý 4 năm 1) rơi vào khoảng cuối 2027, sau khi mẫu 2007–2026 đã kết thúc. Như vậy "mẫu kiểm tra riêng" nằm ngoài phạm vi thời gian đã khai. Dữ liệu năm 2027 trước ngày đăng ký không thuộc mẫu chính lẫn mẫu kiểm tra. Đề cương cũng không có quy tắc dùng mẫu kiểm tra trong kết luận về giả thuyết. | Mẫu kiểm tra ngoài thời gian là biện pháp chính để bù cho việc thí sinh đã xem dữ liệu 2019–2025. Cần nêu ngày kết thúc mẫu chính, độ dài kỳ vọng của mẫu kiểm tra (số cửa sổ 6 tháng) và vai trò của nó.

2. [MAJOR] 4.3.4 ("Số chế độ… do tiêu chí thông tin quyết định… và cố định khi đăng ký trước") và Bảng 5 năm 1 quý 2 (ước lượng thử "để đo… số quan sát ở chế độ căng thẳng") ↔ Bảng 5 năm 2 ("Quý 1--2: xác định chế độ thị trường") và 4.3.9 (đăng ký "trước khi ước lượng chính thức tập mô hình ở bước 3") | Để cố định số chế độ khi đăng ký thì phải ước lượng mô hình chế độ trước quý 4 năm 1, nhưng Bảng 5 đặt bước "xác định chế độ" vào năm 2 và không có mục nào ở năm 1. 4.3.6 cũng nói độ dài cửa sổ "sẽ biện minh… sau khi ước lượng thử", tức điều chỉnh tham số sau khi đã xem dữ liệu căng thẳng 2019–2025. | Ghi rõ trong Bảng 5 bước ước lượng chế độ sơ bộ ở năm 1, và giới hạn những gì được xem trong lần ước lượng thử.

3. [MAJOR] 4.3.10 và 7.4 (phương án dự phòng "thu hẹp… giai đoạn mẫu") và 4.4 ("mở mẫu về trước năm 2019 nếu dữ liệu cho phép") ↔ 4.3.6 (cần 104 tuần ước lượng cộng 36 tháng ngoài mẫu, nên "mức hối tiếc chỉ tính được từ khoảng năm thứ năm của mẫu") | Nếu mẫu thu hẹp về 2019–2025/2026, mức hối tiếc chỉ tính được từ khoảng 2024, tức khoảng 4–6 cửa sổ, thấp hơn nhiều so với ngưỡng 10 cửa sổ căng thẳng. Khi đó phương án dự phòng làm thiết kế không kiểm định được. Ước lượng thử năm 1 trên 2019–2025 cũng gặp giới hạn tương tự. | Nêu độ dài mẫu tối thiểu để thiết kế còn khả thi, và phương án thay thế (ví dụ rút ngắn cửa sổ chọn mô hình) được đăng ký trước.

4. [MAJOR] Hình 1 và 4.3.2 ("Các biến kênh tác động lên chính quan hệ đó"; "Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục") ↔ 4.3.7, 4.3.8 | Văn bản và hình mô tả quan hệ điều tiết (moderation). Nhưng phương trình (5) đưa X~t~ vào dạng cộng, không có tương tác S~t~ × X~t~, và phép phân rã β~0~ − β~1~ là lập luận trung gian (mediation). H~3~ cũng không kiểm định quan hệ rủi ro → kết quả, mà so sánh trực tiếp cơ chế với *c*. | Sửa lời diễn giải Hình 1 cho khớp với đặc tả thực tế, hoặc bổ sung số hạng tương tác.

5. [MINOR] 4.3.5 ("báo cáo kết quả cả khi có lẫn khi không có M~5~") và 4.3.7 (tập tĩnh M~1~, M~2~, M~3~, M~4~, M~6~) ↔ công thức (2)–(3) với "|*M*| = 7" | Các tập con làm |*M*| thay đổi trong khi công thức cố định là 7, và phân phối rỗng "1.000 lần tái lấy mẫu… của bảy mô hình" chưa được nêu cho tập con. | Viết công thức theo |*M*| tổng quát và nêu rằng phân phối rỗng được tính lại cho từng tập.

6. [MINOR] 4.3.3 (robustness: "dữ liệu tháng, tái cân bằng hằng quý") ↔ 4.3.5 (ngưỡng tỷ lệ cổ phiếu trên quan sát tuần ≤ 0,5) và 4.3.6 (cửa sổ 104 tuần) | Ở cấu hình cơ sở, 30/104 ≈ 0,29 nên ngưỡng không bao giờ kích hoạt. Ở cấu hình dữ liệu tháng, cửa sổ ước lượng và cách áp ngưỡng (theo quan sát tháng) chưa được định nghĩa. | Nêu độ dài cửa sổ và quy tắc ngưỡng cho cấu hình dữ liệu tháng.

7. [MINOR] 4.3.3 ("30 mã có giá trị giao dịch bình quân ba tháng **và** vốn hóa tự do chuyển nhượng lớn nhất") | Hai tiêu chí xếp hạng được nối bằng "và" mà không có quy tắc kết hợp (lọc tuần tự, xếp hạng tổng hợp?). | Nêu quy tắc chọn rổ cụ thể.

8. [MINOR] 7.3 ("hai đến ba bài báo") ↔ Bảng 5 (sản phẩm "Bài báo 1", "Bài báo 2 và 3") | Văn bản nêu một khoảng, bảng kế hoạch cam kết đủ 3 bài. | Thống nhất số bài.

9. [MINOR] 7.2 (chuyên đề 3: "thước đo… và thiết kế kiểm định có đăng ký trước") ↔ Bảng 5 (chuyên đề 3 là sản phẩm năm 2, còn đăng ký diễn ra ở quý 4 năm 1) | Chuyên đề về thiết kế đăng ký trước hoàn thành sau khi đã đăng ký. | Dời chuyên đề 3 về năm 1, hoặc ghi rõ nó là bản tổng hợp sau đăng ký.

10. [MINOR] 4.3.10 ("Nếu dữ liệu bác bỏ giả thuyết… quy tắc 1/N đủ dùng ở Việt Nam") ↔ 4.3.2 (giả thuyết đối lập của H~1~) | Việc H~1~ bị bác bỏ (rủi ro không đổi theo chế độ) không suy ra 1/N thắng ổn định. Đó là hai giả thuyết đối lập khác nhau và cần kiểm định riêng (ví dụ tần suất M~1~ là *o* hoặc *c*). | Nêu phép kiểm định riêng cho giả thuyết "1/N thắng ổn định".

11. [MINOR] 4.4 (thủ tục giám sát: "kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng", "suy ra từ H~3~") ↔ 4.3.8 | H~3~ so sánh cơ chế với *c* trong chế độ căng thẳng, không kiểm định quy tắc kích hoạt theo chế độ (chuyển sang kết hợp khi S~t~ vượt ngưỡng). | Ghi rõ đây là suy luận ngoài phạm vi kiểm định, hoặc thêm chiến lược này vào phần đánh giá.

12. [MINOR] Bảng 2, cột "Cơ sở" của H~3~ (Hoeting; Garlappi; Rapach) ↔ 4.3.8 (cơ chế (iii) theo Kritzman và cộng sự, 2012; Tu, 2010) | Cơ chế (iii) không có cơ sở tương ứng trong Bảng 2. | Bổ sung tài liệu cơ sở cho cơ chế (iii).

13. [MINOR] 4.3.5 (danh sách nội dung "cố định" trong tệp đăng ký) | Danh sách không gồm ngưỡng VIF (đã ấn định là 5 ở 4.3.7), mức ý nghĩa của MCS (10%), số lần bootstrap (1.000), độ dài khối bootstrap, quy tắc chọn *c* (36 tháng) và tập mô hình con. Các giá trị này nằm rải rác ở 4.3.6–4.3.7 nhưng không được nhắc lại trong danh sách đăng ký. | Gộp tất cả tham số đã ấn định vào một bảng đăng ký duy nhất.

14. [MINOR] Đối chiếu Hình 1–2 (hinh-van-ban.txt) với văn bản | Hình 2 khớp với 4.3.6 (104 tuần; 6 tháng; "chọn trước mô hình c có lợi suất tương đương chắc chắn cao nhất trong 36 tháng trước"). Hình 1 khớp về vị trí H~1~–H~4~, nhưng có các lệch thuật ngữ đã nêu ở Terminology #1, #3, #4, #5 và #9. Không có tài liệu kèm theo nào khác (tính công suất, tệp OSF) để đối chiếu.

Nhận xét chung: tiến độ năm 1–4 (Bảng 5) khớp với 7.3 và với cấu trúc chương 4–6 về thứ tự H~1~ → H~2~/H~4~ → H~3~. Các vấn đề nghiêm trọng nhất tập trung ở 4.3.6–4.3.8. Cụ thể, đó là việc xác định ước lượng lượng của H~1~ (β~0~ hay β~1~, R~t~ thô hay chuẩn hóa), sự trùng lặp giữa cơ chế giảm thiểu và M~6~/M~7~, và việc thiếu định nghĩa nhị phân cho "cửa sổ căng thẳng", định nghĩa mà cả H~3~ lẫn quy tắc "không kết luận" đều phụ thuộc.

---

## Identification Strategy, Causal Claims & Contribution

## Agent 3: Identification Strategy, Causal Claims & Contribution

*Ghi chú phạm vi:* Đây là nghiên cứu quan sát trên dữ liệu thị trường công khai ("không dùng khảo sát hay phương pháp định tính", mục 4.3.3). Vì vậy các tiêu chí dành cho RCT (ngẫu nhiên hóa, tuân thủ, hao hụt mẫu, lan tỏa) **không áp dụng**: không có can thiệp nào được phân bổ và không có đối tượng là con người. Ở đây, "nhận diện" nghĩa là so sánh theo thời gian giữa các cửa sổ có chế độ khác nhau. Câu hỏi cốt lõi là thước đo và quy tắc suy luận có tách được tác động của chế độ khỏi nhiễu cơ học, khỏi biến động và khỏi các thay đổi cấu trúc trùng thời điểm hay không.

### Major Identification or Design Problems

1. [CRITICAL] **Vị trí:** 4.3.6, 4.3.10, 7.4. **Vấn đề:** Thiết kế gần như chắc chắn sẽ tự đưa H1 vào nhóm "không kết luận". Đề cương ghi "đề tài dự kiến có khoảng 28 cửa sổ đánh giá độc lập", nhưng lại đặt quy tắc "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Mức hối tiếc chỉ tính được "từ khoảng năm thứ năm của mẫu", và "khủng hoảng tài chính toàn cầu chủ yếu phục vụ ước lượng chế độ". Như vậy, các giai đoạn căng thẳng còn lại chủ yếu là COVID-19 năm 2020 và đợt căng thẳng trái phiếu từ quý IV/2022. Với cửa sổ 6 tháng, các giai đoạn này nhiều khả năng chỉ tạo ra ít hơn 10 cửa sổ căng thẳng. **Tại sao nghiêm trọng:** Câu hỏi 1 là trục chính của luận án. Nếu kết quả "không kết luận" được dự báo trước ngay từ thiết kế thì nghiên cứu khẳng định không trả lời được câu hỏi này. Ngoài ra, $S_t$ là biến liên tục ("tỷ lệ số ngày trong cửa sổ có xác suất lọc… vượt ngưỡng"), nên "cửa sổ ở chế độ căng thẳng" chưa có định nghĩa để đếm. **Cách sửa:** (a) Đề cương đã hứa "báo cáo số giai đoạn căng thẳng rơi vào phần mẫu tính được mức hối tiếc" trước khi ước lượng mô hình danh mục. Nên làm việc này ngay trong đề cương, vì việc đếm chỉ dùng chỉ số, không lộ kết quả danh mục. (b) Định nghĩa "cửa sổ căng thẳng", ví dụ $S_t$ ≥ một ngưỡng đăng ký trước. (c) Thực hiện phân tích công suất bằng mô phỏng với số cửa sổ thực tế. (d) Cân nhắc những thay đổi làm tăng số quan sát căng thẳng: rút ngắn cửa sổ chọn mô hình 36 tháng, dùng cửa sổ đánh giá 3 tháng, hoặc dùng tần suất cao hơn có hiệu chỉnh phụ thuộc. Nếu không tăng được, cần định vị lại H1 là ước lượng kích thước hiệu ứng theo từng giai đoạn thay vì kiểm định xác nhận.

2. [CRITICAL] **Vị trí:** 4.3.5, 4.3.6, 7.4 (năm 1, quý 2–4). **Vấn đề:** Thời điểm đăng ký trước mâu thuẫn với lịch ước lượng thử. Trong quý 2 năm 1, thí sinh "ước lượng thử bảy mô hình trên giai đoạn 2019--2025 để đo thời gian tính và số quan sát ở chế độ căng thẳng", nhưng đến quý 4 mới đăng ký trước. Độ dài cửa sổ cũng được chọn sau khi xem kết quả thử: "thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất". Trong khi đó, mục 4.3.9 viết "Thí sinh đăng ký trước kế hoạch phân tích trước khi ước lượng chính thức tập mô hình". **Tại sao nghiêm trọng:** Giai đoạn 2019–2025 chứa chính hai giai đoạn căng thẳng chủ chốt của phần mẫu xác nhận. Ước lượng cả bảy mô hình trên giai đoạn này sẽ làm lộ thứ hạng mô hình theo chế độ trước khi cố định cửa sổ, siêu tham số và ngưỡng. Khi đó, đăng ký trước mất giá trị xác nhận với đúng những quan sát quyết định kết quả H1 và H3. Mẫu kiểm tra "dữ liệu phát sinh sau ngày đăng ký" chỉ dài khoảng 2–3 năm (4–6 cửa sổ 6 tháng) và chưa có quy tắc sử dụng. **Cách sửa:** Giới hạn bước chạy thử vào dữ liệu trước năm 2012, dữ liệu mô phỏng, hoặc chỉ đo thời gian tính mà không xuất kết quả lợi suất tương đương chắc chắn hay mức hối tiếc. Cố định độ dài cửa sổ trước bất kỳ bước chạy thử nào có kết quả. Trong tệp đăng ký, tách rõ phần nào là xác nhận, phần nào là thăm dò, và nêu cách dùng mẫu kiểm tra (ví dụ: dấu của $\beta$ phải lặp lại).

3. [MAJOR] **Vị trí:** 4.1 so với 4.3.6. **Vấn đề:** Đại lượng cần ước lượng (estimand) chính bị đổi so với định nghĩa ban đầu. Mục 4.1 định nghĩa rủi ro lựa chọn mô hình là "tổn thất kỳ vọng", đo bằng mức hối tiếc theo đơn vị lợi suất tương đương chắc chắn. Nhưng mục 4.3.6 viết "phân tích chính chia $D_{t}$ và $R_{t}$ cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình". Đại lượng sau khi chia là tỷ số tín hiệu trên nhiễu, không còn là tổn thất kinh tế. Văn bản cũng không nêu dùng sai số chuẩn của cặp nào trong 21 cặp mô hình. **Tại sao nghiêm trọng:** Ở chế độ căng thẳng, biến động cao làm sai số chuẩn tăng. Do đó $R_t$ chuẩn hóa có thể giảm ngay cả khi tổn thất tính bằng tiền tăng, và ngược lại. H1 có thể được "ủng hộ" hoặc "bác bỏ" chỉ vì cách chuẩn hóa. **Cách sửa:** Đăng ký trước một kết quả chính duy nhất. Có hai lựa chọn hợp lý: (i) $R_t$ thô theo đơn vị lợi suất tương đương chắc chắn, với phân phối rỗng để loại phần dương cơ học; hoặc (ii) bản chuẩn hóa, kèm định nghĩa chính xác mẫu số. Bản còn lại chỉ là kết quả phụ.

4. [MAJOR] **Vị trí:** 4.3.7, phương trình (5). **Vấn đề:** Không rõ $\beta$ nào dùng để kiểm định H1. Đề cương nêu "Biến động thực hiện luôn có mặt trong $X_{t}$", nhưng ở đoạn sau lại định nghĩa $\beta_0$ "khi không có" $X_t$. Đồng thời, chế độ căng thẳng được định nghĩa là "chế độ có phương sai điều kiện cao nhất". **Tại sao nghiêm trọng:** Nếu H1 dùng $\beta$ có kiểm soát biến động thực hiện, hai biến gần như trùng định nghĩa nên $\beta$ bị hấp thụ. Đây là trường hợp kiểm soát xấu (bad control) và đa cộng tuyến cấu trúc. Nếu H1 dùng $\beta$ không kiểm soát, kết quả chỉ là tương quan thô với biến động. Hai cách đọc cho câu trả lời khác hẳn nhau. **Cách sửa:** Nêu rõ H1 kiểm định $\beta_0$ (không có $X_t$) và giải thích nó là chênh lệch mô tả giữa các chế độ. Việc tách phần do biến động riêng chỉ đưa vào H2. Lý do là chính đề cương đã nói phân phối rỗng giữ nguyên biến động, nên phần "biến động thuần" đã được xử lý qua phân phối rỗng chứ không qua hồi quy.

5. [MAJOR] **Vị trí:** 4.3.6 (quy tắc chọn mô hình *c*). **Vấn đề:** Rủi ro lựa chọn mô hình được đo có điều kiện theo một quy tắc chọn duy nhất: "chọn trước mô hình *c* có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước". Cửa sổ nhìn lại 36 tháng gần như luôn bắc qua nhiều chế độ. Vì vậy, mức hối tiếc ở cửa sổ căng thẳng chủ yếu phản ánh độ trễ của quy tắc đuổi theo hiệu quả quá khứ tại thời điểm chuyển chế độ, không phải đặc tính của bản thân chế độ căng thẳng. **Tại sao nghiêm trọng:** Kết luận về "rủi ro lựa chọn mô hình" thực chất là kết luận về một quy tắc chọn cụ thể. Cách hiểu này hẹp hơn định nghĩa ở 4.1 ("chọn một mô hình trước lúc biết mô hình nào tốt nhất"). **Cách sửa:** Đăng ký trước thêm một thước đo không phụ thuộc quy tắc chọn, ví dụ $U_{o,t} - \overline{U}_t$, tức mức hối tiếc kỳ vọng nếu chọn ngẫu nhiên đều. Đăng ký thêm 1–2 quy tắc chọn thay thế, như nhìn lại 12 tháng hoặc chọn theo tập tin cậy mô hình. Tách cửa sổ chuyển chế độ (bình thường sang căng thẳng) khỏi cửa sổ căng thẳng kéo dài.

6. [MAJOR] **Vị trí:** 4.3.7 (phân phối rỗng). **Vấn đề:** Phân phối rỗng được tạo bằng cách "loại chênh lệch trung bình giữa các mô hình trong từng chế độ". Văn bản không nêu việc gán chế độ khi khử trung bình dùng xác suất lọc theo thời gian thực hay phân loại toàn mẫu. Văn bản cũng không nói rõ phân phối rỗng có giữ được cấu trúc phụ thuộc giữa cửa sổ chọn 36 tháng và cửa sổ đánh giá hay không. **Tại sao nghiêm trọng:** Phân phối rỗng là công cụ chính để tách "rủi ro lựa chọn" khỏi "nhiễu ước lượng". Nếu đặc tả sai, phần dương cơ học của $E[R_t]$ ("giá trị lớn nhất của các đại lượng có nhiễu tăng theo phương sai của nhiễu") không được loại đúng cách. **Cách sửa:** Viết thuật toán phân phối rỗng thành các bước cụ thể trong tệp đăng ký: chuỗi nào được khử trung bình, theo nhãn chế độ nào, độ dài khối bao nhiêu, và áp dụng lại toàn bộ quy trình chọn *c* trên mỗi mẫu bootstrap.

7. [MAJOR] **Vị trí:** 4.3.2 (Hình 1) so với 4.3.7. **Vấn đề:** Cấu trúc nhân quả của H2 không nhất quán giữa khung và kiểm định. Hình 1 mô tả biến kênh như biến điều tiết: "Các biến kênh tác động lên chính quan hệ đó". Nhưng kiểm định lại là phân rã kiểu trung gian $\beta_0 - \beta_1$, và phương trình (5) không có số hạng tương tác. Các biến kênh đo đồng thời trong cùng cửa sổ với $Y_t$ và đều là hệ quả của chế độ. Ngoài ra, biến động thực hiện "luôn có mặt trong $X_t$", nên $\beta_0 - \beta_1$ gộp cả phần do biến động, mà phần này gần như trùng định nghĩa chế độ. **Tại sao nghiêm trọng:** Đại lượng "chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ" (câu hỏi 2) không có cách hiểu rõ ràng. Phân rã này cũng nhạy với thứ tự đưa biến vào và với đa cộng tuyến, mà với khoảng 28 quan sát và nhiều biến kênh thì đa cộng tuyến gần như chắc chắn xảy ra. **Cách sửa:** Chọn một trong hai khung, điều tiết (tương tác $S_t \times X_t$) hoặc phân rã. Nếu giữ phân rã, dùng phân rã không phụ thuộc thứ tự biến (ví dụ kiểu Gelbach) và báo cáo riêng phần đóng góp của biến động. Giảm $X_t$ xuống tối đa 2–3 biến đăng ký trước. Chọn một thước đo tương quan đuôi duy nhất, thay vì "tương quan đuôi và tương quan hiệu chỉnh theo biến động".

8. [MAJOR] **Vị trí:** 4.3.8 (H3). **Vấn đề:** Phép so sánh của H3 thiếu đối chứng rõ ràng và có tính vòng tròn. (a) "so với chọn một mô hình" không nói rõ mô hình nào: *c* theo quy tắc 36 tháng, 1/N, hay mô hình tốt nhất trước đó. (b) Cơ chế (iii) "quy tắc chuyển chế độ" và M7 đều dùng xác suất căng thẳng, nhiều khả năng từ chính mô hình Markov sinh ra $S_t$. Khi đánh giá "ở chế độ căng thẳng", một chiến lược giảm tỷ trọng rủi ro khi $S_t$ cao sẽ có độ sụt giảm tối đa thấp hơn một cách cơ học. (c) Khi loại (ii) và (iii) khỏi *M* thì tập mô hình đối chứng của mức hối tiếc thay đổi, nên mức hối tiếc của H3 không so sánh được với H1. (d) Có ba cơ chế, mỗi cơ chế có biến thể (trọng số Bayes, tập tin cậy mô hình, Tu–Zhou), và bốn tiêu chí, nhưng hiệu chỉnh Holm chỉ tính "cho bốn giả thuyết". (e) Trọng số Bayes cần hàm hợp lý, trong khi các quy tắc danh mục không phải là mô hình xác suất có hàm hợp lý. **Tại sao nghiêm trọng:** H3 là cơ sở cho đề xuất thực tiễn, nhưng như hiện nay thì có quá nhiều cách để "ủng hộ" H3. **Cách sửa:** Đăng ký một đối chứng duy nhất, nên là mô hình *c* theo quy tắc chọn của H1. Đăng ký một cơ chế chính và một cách tính trọng số kết hợp cụ thể, ví dụ trọng số theo hiệu quả quá khứ hoặc trọng số đều trong tập tin cậy mô hình. Nếu thật sự dùng trọng số Bayes, phải định nghĩa hàm hợp lý. Cơ chế (iii) cần dùng tín hiệu chế độ lấy tại đầu cửa sổ. Hiệu chỉnh so sánh bội cần bao gồm cả các phép so sánh bên trong H3. Điều kiện "độ sụt giảm tối đa không cao hơn… với khoảng tin cậy loại trừ 0" cũng cần viết lại cho đúng logic: không thể đòi khoảng tin cậy loại trừ 0 cho một điều kiện "không cao hơn".

9. [MAJOR] **Vị trí:** 4.3.3, 4.3.7. **Vấn đề:** Mẫu có các yếu tố gây nhiễu theo thời gian chưa được xử lý. So sánh giữa các chế độ thực chất là so sánh giữa các giai đoạn. Trong 2012–2026, cấu trúc thị trường HOSE thay đổi: thành phần rổ 30 mã, biên độ giá, phí và thuế mà đề cương tự nêu là "theo từng thời kỳ", và mức trưởng thành của thị trường. Nếu các giai đoạn căng thẳng trùng với những thay đổi này, $\beta$ sẽ lẫn cả hai. Phần kiểm tra độ bền chỉ thêm chỉ số giá tiêu dùng, tỷ giá và lãi suất. **Tại sao nghiêm trọng:** Điều kiện tương đương với "lựa chọn trên biến quan sát được" (không có nhân tố thời gian bị bỏ sót tương quan với $S_t$) chưa được nêu ra hay bảo vệ. **Cách sửa:** Nêu giả định nhận diện một cách tường minh. Thêm kiểm tra với xu hướng thời gian hoặc biến giả theo giai đoạn thể chế. Báo cáo hiệu ứng theo từng giai đoạn căng thẳng, điều mà đề cương đã hứa ở 4.3.10, như bằng chứng chính chứ không chỉ là phụ lục.

10. [MAJOR] **Vị trí:** 4.3.10, 4.3.2. **Vấn đề:** Đề cương coi việc không bác bỏ H0 là ủng hộ giả thuyết đối lập. Văn bản viết "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam". Đề cương cũng nói mỗi giả thuyết "đi kèm một khả năng đối lập mà đề tài kiểm định cùng lúc", nhưng không có phép kiểm định nào được đặc tả cho "1/N thắng ổn định". **Tại sao nghiêm trọng:** Với công suất thấp, việc không bác bỏ H0 không chứng minh được hiệu ứng bằng 0. "Mức hối tiếc không đổi theo chế độ" cũng không suy ra được "1/N đủ dùng". Cách lập luận này làm H1 gần như không thể bác bỏ theo nghĩa thông tin. **Cách sửa:** Đăng ký trước kiểm định tương đương (ví dụ TOST với một ngưỡng tác động nhỏ nhất có ý nghĩa kinh tế, tính bằng điểm cơ bản lợi suất tương đương chắc chắn mỗi năm). Đăng ký riêng một kiểm định cho mệnh đề "M1 không bị mô hình nào vượt", ví dụ M1 có nằm trong tập tin cậy mô hình ở cả hai chế độ hay không.

11. [MAJOR] **Vị trí:** Bảng 2 (H4), 4.4. **Vấn đề:** Hướng diễn giải và giá trị cấu trúc của H4 có vấn đề. H4 dự báo "độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao", và 4.4 gọi đây là "một thước đo bầy đàn". Nhưng theo cách đo mà đề cương trích dẫn (Christie và Huang, 1995), bầy đàn biểu hiện ở độ phân tán chéo *thấp*. Nếu H4 được ủng hộ thì kết quả lại gắn rủi ro lựa chọn với *ít* bầy đàn hơn. Ngoài ra, độ phân tán chéo cao làm các danh mục có trọng số khác nhau cho lợi suất khác nhau một cách cơ học, nên liên hệ này có thể chỉ là cơ học, không mang ý nghĩa hành vi. **Tại sao nghiêm trọng:** Đây là cầu nối duy nhất với tài chính hành vi mà mục 5 dùng để biện minh việc chọn cơ sở đào tạo. **Cách sửa:** Đổi tên thành "độ phân tán chéo" và bỏ nhãn "bầy đàn". Nếu muốn giữ yếu tố bầy đàn, dùng hồi quy phi tuyến kiểu Chang và cộng sự (2000) để tạo chỉ báo bầy đàn và nêu rõ dấu kỳ vọng. Vì H4 là thăm dò, nên đưa nó ra khỏi nhóm "bốn giả thuyết" chịu hiệu chỉnh Holm.

12. [MINOR] **Vị trí:** 4.3.6. **Vấn đề:** Đề cương gọi 28 cửa sổ là "độc lập", trong khi mỗi lần chọn *c* dùng 36 tháng nhìn lại chồng lấn nhau. Vì thế $R_t$ có tự tương quan dù cửa sổ đánh giá không chồng lấn. **Cách sửa:** Bỏ chữ "độc lập", báo cáo cỡ mẫu hiệu dụng, và dùng bootstrap khối theo cửa sổ.

13. [MINOR] **Vị trí:** 4.3.4. **Vấn đề:** Nếu tiêu chí thông tin chọn ba chế độ thì chưa rõ chế độ nào là "bình thường", và chế độ thứ ba được xử lý thế nào trong $S_t$. **Cách sửa:** Đăng ký trước quy tắc gộp chế độ.

14. [MINOR] **Vị trí:** 4.3.7 so với 4.3.10. **Vấn đề:** Các mức ý nghĩa không thống nhất. H1 dùng "phân vị 95%" và khoảng tin cậy (mức chưa nêu), trong khi Holm dùng "ở mức 10%". **Cách sửa:** Thống nhất một mức ý nghĩa cho từng họ kiểm định.

### Overclaiming

1. [MAJOR] **Tuyên bố:** "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục" (4.2(2)); "chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường" (4.2(3)); "chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không" (4.2(4)). **Tại sao quá mức:** Đây là các khẳng định phủ định ở phạm vi toàn cầu, không giới hạn ở Việt Nam. Trong khi đó, chính đề cương thừa nhận việc tìm kiếm chưa gồm Scopus và Web of Science, và thí sinh "mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn". Tính đúng của các khẳng định này là [UNVERIFIED — authors must confirm]. **Cách viết tốt hơn:** Giới hạn khẳng định theo phạm vi tìm kiếm đã nêu ở cuối mục 4.2, ví dụ "Trong phạm vi tìm kiếm nêu trên, thí sinh chưa tìm thấy…". Tách rõ khẳng định cho Việt Nam khỏi khẳng định toàn cầu.

2. [MAJOR] **Tuyên bố:** Hình 1 và 4.3.2: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình"; "Các biến kênh tác động lên chính quan hệ đó"; cơ chế trong Bảng 2 "thanh khoản cạn làm các mô hình có vòng quay khác nhau cách xa nhau". **Tại sao quá mức:** Mục 4.3.7 đã cam kết đúng rằng "Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả", nhưng khung và câu hỏi 2 ("giải thích được bao nhiêu phần") vẫn dùng ngôn ngữ nhân quả. **Cách viết tốt hơn:** Thay "tác động lên" bằng "đi cùng" hoặc "liên hệ với". Đổi câu hỏi 2 thành "phần chênh lệch giữa hai chế độ giảm bao nhiêu khi đưa thêm các biến kênh vào hồi quy".

3. [MAJOR] **Tuyên bố:** Thủ tục giám sát gồm bước "kích hoạt kết hợp mô hình khi thị trường ở chế độ căng thẳng… Thủ tục này suy ra từ H~3~" (4.4). **Tại sao quá mức:** H3 chỉ so sánh kết hợp mô hình với chọn một mô hình *trong* chế độ căng thẳng, và đo chế độ bằng $S_t$ là tỷ lệ ngày căng thẳng trong chính cửa sổ đánh giá, tức thông tin chỉ có sau sự kiện. Phép thử này không kiểm định quy tắc "chỉ kích hoạt khi tín hiệu căng thẳng xuất hiện" so với "luôn kết hợp", và tín hiệu dùng để kích hoạt phải có sẵn tại đầu cửa sổ. **Cách viết tốt hơn:** Hoặc thêm vào kế hoạch một phép thử cho chính quy tắc kích hoạt, dùng tín hiệu có tại đầu cửa sổ và so với phương án luôn kết hợp. Hoặc viết lại thành "kết quả gợi ý xem xét kết hợp mô hình trong giai đoạn căng thẳng; quy tắc kích hoạt chưa được kiểm định".

4. [MAJOR] **Tuyên bố:** "Về lý thuyết, đề tài đưa ra khung khái niệm và thước đo rủi ro lựa chọn mô hình theo chế độ" (4.4). **Tại sao quá mức:** Mức hối tiếc là một khái niệm sẵn có trong lý thuyết quyết định mà chính đề cương dẫn. Đề tài không xây dựng mô hình lý thuyết hay mệnh đề nào mới. Đóng góp thực chất nằm ở đo lường và giao thức thực nghiệm. **Cách viết tốt hơn:** "Về phương pháp, đề tài đề xuất một giao thức đo mức hối tiếc khi chọn mô hình theo chế độ, không dùng thông tin nhìn trước và có hiệu chuẩn bằng phân phối rỗng."

5. [MINOR] **Tuyên bố:** "Nếu dữ liệu bác bỏ giả thuyết… quy tắc 1/N đủ dùng ở Việt Nam" (4.3.10). **Tại sao quá mức:** Không có phép kiểm định nào hỗ trợ kết luận này (xem mục 10 ở trên). **Cách viết tốt hơn:** "…khi đó đề tài báo cáo liệu M~1~ có nằm trong tập tin cậy mô hình ở cả hai chế độ hay không."

6. [MINOR] **Tuyên bố:** "chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển" (4.1). Câu này có lẽ định viết "lớn hơn so với thị trường phát triển". **Tại sao quá mức:** Thiết kế không có thị trường so sánh, nên không kiểm định được nhận định này. **Cách viết tốt hơn:** Sửa câu và ghi đây là động cơ nghiên cứu, không phải kết quả dự kiến. Phần so sánh giữa các thị trường đã được đưa vào hướng nghiên cứu sau tốt nghiệp ở mục 9.

7. [MINOR] **Tuyên bố:** "Giới hạn khác: kết luận chỉ áp dụng trong phạm vi thị trường Việt Nam" (4.4). **Tại sao chưa đủ:** Phạm vi suy rộng thực tế còn hẹp hơn: 30 mã thanh khoản nhất trên HOSE, chỉ mua, tái cân bằng tháng, tập bảy mô hình cụ thể và hệ số ngại rủi ro $\rho$ = 5. Kết quả áp dụng cho "công ty quản lý quỹ" có tập mô hình khác sẽ không tự động đúng. **Cách viết tốt hơn:** Nêu rõ kết luận có điều kiện theo tập *M*, theo rổ cổ phiếu và theo quy tắc chọn mô hình.

### Underused Strengths

1. **Điểm mạnh:** Đề cương định nghĩa khái niệm rất rõ và tách "bất định" khỏi "rủi ro": "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro". Đề cương cũng tách "khủng hoảng" (sự kiện lịch sử) khỏi "chế độ căng thẳng" (trạng thái thống kê). **Nên nhấn mạnh ở:** Phần đóng góp (4.4) và phần mở đầu của tệp đăng ký OSF. **Cách diễn đạt gợi ý:** Định vị đây là đóng góp về đo lường. Đề tài phân biệt thước đo tổn thất quyết định với thước đo bất định, trong khi theo đề cương, các nghiên cứu rủi ro mô hình được dẫn chỉ đo độ chênh giữa các dự báo.

2. **Điểm mạnh:** Đề cương nhận ra rằng mức hối tiếc dương một cách cơ học khi các mô hình ngang nhau ("Kỳ vọng của $R_{t}$ vẫn dương khi các mô hình ngang chất lượng") và đề xuất phân phối rỗng để hiệu chuẩn. Đề cương cũng làm lại kiểm định trên tập chỉ gồm các mô hình tĩnh để loại tác động của M5 và M7. **Nên nhấn mạnh ở:** 4.1 và 4.4. Đây là lý do chính khiến thiết kế đáng tin hơn một phép so sánh hiệu quả theo chế độ thông thường. **Cách diễn đạt gợi ý:** "Đề tài tách phần mức hối tiếc do nhiễu ước lượng khỏi phần do thứ hạng mô hình thay đổi theo chế độ."

3. **Điểm mạnh:** Thiết kế có nhiều biện pháp chống thiên lệch nhìn trước và thiên lệch sống sót. Rổ cổ phiếu được xác định "chỉ bằng dữ liệu có tại ngày đó", có tính cả mã đã hủy niêm yết. Xác suất lọc được tính theo cửa sổ mở rộng. Kiểm định Bai–Perron "không dùng làm biến chế độ". Mọi mô hình có "cùng ngân sách tinh chỉnh". Kết quả được báo cáo cả khi có lẫn khi không có M5. **Nên nhấn mạnh ở:** Một đoạn tóm tắt các biện pháp bảo đảm hiệu lực nội tại trong 4.3.10. **Cách diễn đạt gợi ý:** Gom thành một danh sách kiểm tra về rủi ro nhìn trước, sống sót và đào bới dữ liệu, kèm cách xử lý từng rủi ro.

4. **Điểm mạnh:** Thí sinh minh bạch về việc đã tiếp xúc với dữ liệu ("không thể khẳng định chưa từng thấy kết quả ở chế độ căng thẳng"), cam kết khai báo những gì đã xem, và có quy tắc "không kết luận" đăng ký trước. **Nên nhấn mạnh ở:** Tệp OSF. Đây đúng là thông tin mà các mẫu đăng ký cho phân tích dữ liệu thứ cấp yêu cầu ([UNVERIFIED — authors must confirm] tên và trường cụ thể của mẫu OSF phù hợp). **Cách diễn đạt gợi ý:** Biến điểm này thành một bảng "dữ liệu và kết quả đã thấy trước ngày đăng ký", ghi rõ giai đoạn và đại lượng. Kết hợp với cách sửa ở vấn đề 2 để điểm mạnh này không bị chính lịch chạy thử làm suy yếu.

5. **Điểm mạnh:** Lập luận dùng lợi suất tương đương chắc chắn thay cho tỷ số Sharpe khi lợi suất vượt trội trung bình âm là đúng và quan trọng riêng cho phân tích chế độ căng thẳng. **Nên nhấn mạnh ở:** 4.1, như một lý do phương pháp giải thích vì sao so sánh theo chế độ cần thước đo khác. **Cách diễn đạt gợi ý:** "Xếp hạng theo tỷ số Sharpe bị đảo chiều một cách cơ học ở chế độ căng thẳng; đề tài tránh vấn đề này bằng lợi suất tương đương chắc chắn."

6. **Điểm mạnh:** Giao thức đo có thể áp dụng cho thị trường khác. **Nên nhấn mạnh ở:** Phần đóng góp, thay cho cách định vị chủ yếu bằng "chưa có ở Việt Nam". **Cách diễn đạt gợi ý:** Phần đóng góp mới cho Việt Nam là bằng chứng thực nghiệm. Phần đóng góp có thể dùng rộng hơn là giao thức đã đăng ký trước.

### Minor Positioning Issues

1. [MINOR] **Vị trí:** Câu hỏi 1 và câu hỏi 3 (4.1). **Vấn đề:** "thay đổi thế nào" và "Cơ chế nào giảm được" là câu hỏi mở, trong khi H1 và H3 có hướng xác định. **Cách sửa:** Viết lại câu hỏi theo dạng có hướng, khớp với giả thuyết, ví dụ "Mức hối tiếc khi chọn mô hình có cao hơn ở chế độ căng thẳng không, và cao hơn bao nhiêu?".

2. [MINOR] **Vị trí:** 4.1 (đoạn về khung giám sát). **Vấn đề:** Đề cương dành nhiều chỗ cho SR 11-7, SR 26-2 và Thông tư 83/2025, rồi chính văn bản thừa nhận chúng không áp dụng cho công ty quản lý quỹ. Điều này làm mờ đối tượng người dùng kết quả. **Cách sửa:** Rút gọn đoạn này, hoặc nêu rõ khung quy định áp dụng cho công ty quản lý quỹ ngay khi đã xác định được.

3. [MINOR] **Vị trí:** Bảng 1 và đoạn "Đóng góp dự kiến". **Vấn đề:** Đóng góp được so với từng bài riêng lẻ (Ta và Vuong, 2020; Goutte và cộng sự, 2025; Hoang và Luu, 2024) "dựa trên phần tóm tắt". Cách so sánh này dễ bị phản biện cho rằng đã mô tả sai nội dung các bài. **Cách sửa:** Sau khi đọc toàn văn trong năm 1, cập nhật lại phần so sánh và ghi rõ đã đọc toàn văn trong tệp đăng ký.

4. [MINOR] **Vị trí:** 4.3.5 (M5). **Vấn đề:** Đưa mô hình do chính thí sinh phát triển vào tập cạnh tranh tạo xung đột lợi ích về mặt kết quả. Đề cương đã xử lý một phần bằng cách báo cáo cả khi có lẫn khi không có M5. **Cách sửa:** Đăng ký trước rằng mọi kết luận về H1–H3 phải đứng vững khi bỏ M5. Không diễn giải hiệu quả riêng của M5 như một phát hiện.

5. [MINOR] **Vị trí:** 7.4 và 4.3.5. **Vấn đề:** Mẫu kiểm tra sau ngày đăng ký (quý 4 năm 1 đến năm 3–4) quá ngắn để có ý nghĩa xác nhận cho H2 và H3, vốn được phân tích ở năm 3. **Cách sửa:** Ghi rõ mẫu kiểm tra chỉ dùng để xem dấu của kết quả có lặp lại hay không, không dùng để kiểm định.

6. [MINOR] **Mức phù hợp với OSF Registries:** Thiết kế đạt nhiều tiêu chí của một bản đăng ký nghiêm túc: có quy tắc "không kết luận", có hiệu chỉnh so sánh bội, có ghi nhận các lệch khỏi kế hoạch. Tuy vậy, người thẩm định nhiều khả năng sẽ soi kỹ năm điểm: (a) thời điểm chạy thử so với thời điểm đăng ký (vấn đề 2); (b) kết quả chính chưa duy nhất (vấn đề 3 và 4); (c) độ tự do trong H3 (vấn đề 8); (d) công suất thấp mà chưa có phân tích công suất bằng mô phỏng (vấn đề 1); (e) diễn giải kết quả không bác bỏ H0 (vấn đề 10). **Cách sửa:** Bổ sung vào tệp đăng ký: phân tích công suất bằng mô phỏng, một kết quả chính duy nhất cho mỗi giả thuyết, đối chứng duy nhất cho H3, kiểm định tương đương, và bảng dữ liệu đã thấy trước ngày đăng ký.

---

## Statistical Analysis Plan, Power & Multiple Testing

## Agent 4: Kế hoạch phân tích thống kê, công suất và kiểm định bội

Phạm vi: chỉ đọc `de-cuong-goc.md` (mục 4.1 phần câu hỏi nghiên cứu, Bảng 2, mục 4.3.1–4.3.10, 4.4) và `hinh-van-ban.txt`. Đây là nghiên cứu quan sát chuỗi thời gian. Các nội dung chỉ áp dụng cho RCT được ghi là **không áp dụng**: ICC, hệ số thiết kế (design effect), phân cụm sai số chuẩn theo đơn vị ngẫu nhiên hóa, không tuân thủ (non-compliance), lan tỏa (spillover) giữa nhóm can thiệp và nhóm đối chứng. Lý do: không có phân công can thiệp, không có cụm và không có người tham gia. Trong tài liệu này, "công suất" được hiểu là số cửa sổ đánh giá độc lập và số giai đoạn căng thẳng. "Hao hụt" được hiểu là mã hủy niêm yết, ngừng giao dịch và khoảng trống dữ liệu.

### Major Statistical or Power Problems

1. [CRITICAL] **H1 (và cả H2, H3) | Không có tính toán công suất hay MDE. Quy tắc "không kết luận" gần như chắc chắn sẽ được kích hoạt.**
   - **Bằng chứng:** đề cương viết "Với mẫu 2007--2026, đề tài dự kiến có khoảng 28 cửa sổ đánh giá độc lập" và "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Mức hối tiếc chỉ tính được từ khoảng năm 2012 ("chỉ tính được từ khoảng năm thứ năm của mẫu"). Giai đoạn 2012–2026 chỉ chứa vài giai đoạn căng thẳng mà chính đề cương nêu tên: COVID-19 năm 2020 và trái phiếu doanh nghiệp quý IV/2022. Vì vậy số cửa sổ 6 tháng thuộc chế độ căng thẳng nhiều khả năng chỉ khoảng 2–6, thấp hơn nhiều so với ngưỡng 10.
   - **Thiếu gì:** không có kích thước hiệu ứng giả định. Không có độ lệch chuẩn dự kiến của $R_t$ hoặc $D_t$. Không có MDE tính theo điểm cơ bản lợi suất tương đương chắc chắn. Đề cương chỉ nhắc chung chung: "các kiểm định có công suất thấp".
   - **Vì sao quan trọng:** như hiện tại, kết quả chính cho câu hỏi 1 gần như được định sẵn là "không kết luận". Câu "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu" vì thế không đứng vững.
   - **Khuyến nghị sửa:**
     - (a) Đếm trước, trên dữ liệu không dùng để đánh giá, số cửa sổ có $S_t$ vượt ngưỡng trong giai đoạn 2012–2026. Báo cáo con số này ngay trong đề cương.
     - (b) Mô phỏng công suất: sinh lợi suất bảy mô hình bằng bootstrap khối, cài thêm một chênh lệch hối tiếc giả định ở chế độ căng thẳng (ví dụ 50/100/200 điểm cơ bản CE năm hóa), rồi tính công suất của đúng quy tắc ba điều kiện cho H1.
     - (c) Định nghĩa một ngưỡng hiệu ứng có ý nghĩa kinh tế (SESOI) cho hối tiếc.
     - (d) Cân nhắc dùng cửa sổ chồng lấn kèm HAC hoặc bootstrap khối làm phân tích chính, hoặc rút ngắn cửa sổ đánh giá, để tăng số quan sát. Cần nói rõ đánh đổi về độ phụ thuộc giữa các quan sát.

2. [CRITICAL] **Phương trình (5) | Quá nhiều biến hồi quy so với số quan sát; suy diễn không đáng tin.**
   - **Bằng chứng:** $X_t$ gồm "độ phi thanh khoản Amihud…, tương quan đuôi và tương quan hiệu chỉnh theo biến động…, và độ phân tán chéo của lợi suất", và "Biến động thực hiện luôn có mặt trong $X_t$".
   - **Vấn đề:** cộng với $S_t$ và hệ số chặn, mô hình có khoảng 6–7 tham số trên khoảng 28 quan sát. Đề cương lại dùng "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan". HAC trên 28 điểm bị chệch nặng về phía quá nhỏ. Bootstrap khối trên 28 điểm thì chỉ có rất ít khối.
   - **Vì sao quan trọng:** tỷ lệ bác bỏ sai thực tế có thể cao hơn nhiều so với mức danh nghĩa.
   - **Khuyến nghị sửa:**
     - Giới hạn mỗi phương trình xác nhận ở $S_t$, biến động thực hiện và một biến kênh.
     - Dùng HAC có hiệu chỉnh mẫu nhỏ (fixed-b, Kiefer–Vogelsang) hoặc wild bootstrap. Đăng ký trước quy tắc chọn độ dài khối (ví dụ Politis–White, 2004) và độ dài trễ HAC.
     - Báo cáo một mô phỏng kích thước kiểm định (size) trên dữ liệu giả lập có cùng N.

3. [MAJOR] **Thước đo chính $R_t$ và $D_t$ | Ước lượng đích không rõ. Bước chuẩn hóa thiên lệch về phía giả thuyết rỗng.**
   - **Bằng chứng:** "phân tích chính chia $D_{t}$ và $R_{t}$ cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình trong cùng cửa sổ".
   - **Chưa rõ thứ nhất — chênh lệch nào:** không nói là chênh lệch giữa $o$ và $c$, trung bình theo 21 cặp, hay giá trị lớn nhất.
   - **Chưa rõ thứ hai — cách tính $\mu_{m,t}$, $\sigma^2_{m,t}$:** không nói là trên lợi suất ngày (khoảng 126 quan sát) hay tháng (6 quan sát), và có năm hóa hay không. Điều này quyết định ý nghĩa của $\rho=5$.
   - **Chệch có hệ thống:** ở chế độ căng thẳng, sai số chuẩn tăng, nên đại lượng đã chuẩn hóa tự động giảm. Khi đó $\beta$ đo "hối tiếc trên mỗi đơn vị nhiễu", không đo tổn thất kinh tế, và bị chệch về phía 0.
   - **Kiểm soát trùng lặp:** phân phối rỗng ở mục 4.3.7 đã nhằm loại tác động cơ học của giá trị lớn nhất, nên bước chuẩn hóa là kiểm soát lần thứ hai cho cùng một hiện tượng.
   - **Khuyến nghị sửa:**
     - Chọn một ước lượng đích chính duy nhất: $R_t$ thô, đo bằng điểm cơ bản CE năm hóa, hiệu chuẩn bằng phân phối rỗng.
     - Chuyển phiên bản chuẩn hóa sang kiểm tra độ bền.
     - Ghi rõ tần suất lợi suất, cách năm hóa và công thức sai số chuẩn dùng để chuẩn hóa (cặp mô hình, số lần lặp bootstrap, độ dài khối).

4. [MAJOR] **Phân phối rỗng của H1 | Cách xây dựng chưa đủ để ràng buộc và có thể không phải là rỗng thật.**
   - **Bằng chứng:** "loại chênh lệch trung bình giữa các mô hình trong từng chế độ nhưng giữ nguyên tương quan chéo và biến động".
   - **Vấn đề nội dung:** $U_{m,t}$ phụ thuộc cả $\sigma^2$. Khi chỉ loại chênh lệch trung bình, chênh lệch CE do phương sai khác nhau vẫn còn. Ở chế độ căng thẳng, phương sai giữa các mô hình phân hóa mạnh hơn, nên phân phối "rỗng" vẫn mang đúng hiệu ứng cần kiểm định.
   - **Chưa rõ:**
     - "Trong từng chế độ" xác định bằng cái gì (ngưỡng xác suất lọc nào).
     - Độ dài khối.
     - $S_t$ và $X_t$ được giữ cố định hay tái lấy mẫu.
     - Có ước lượng lại toàn bộ chuỗi chọn mô hình (36 tháng) trong mỗi lần lặp hay không.
   - **Khuyến nghị sửa:** định nghĩa rỗng là "kỳ vọng $U_m$ bằng nhau giữa các mô hình trong mỗi chế độ". Ví dụ: điều chỉnh tịnh tiến lợi suất từng mô hình để CE theo chế độ bằng nhau. Mô tả thuật toán từng bước, gồm độ dài khối, việc giữ $S_t$ cố định và việc lặp lại bước chọn mô hình $c$. Tăng số lần lặp lên ít nhất 5.000 nếu dùng phân vị đuôi.

5. [MAJOR] **Biến chế độ $S_t$ và mô hình Markov | Định nghĩa chưa khóa được.**
   - **Ngưỡng chưa có giá trị:** "ngưỡng đăng ký trước" chưa được cho giá trị cụ thể (0,5? 0,7?).
   - **Trường hợp ba chế độ:** với "Số chế độ (hai hoặc ba)", không rõ chế độ thứ ba được xếp vào "bình thường" hay "căng thẳng". Định nghĩa "phương sai điều kiện cao nhất và lợi suất kỳ vọng thấp hơn" có thể không thỏa khi chế độ có phương sai cao nhất lại có lợi suất kỳ vọng cao (ví dụ phục hồi mạnh sau khủng hoảng).
   - **Hoán đổi nhãn:** khi ước lượng lại theo cửa sổ mở rộng, nhãn chế độ có thể bị hoán đổi, nhưng đề cương chưa có quy tắc xử lý.
   - **Diễn giải $\beta$:** "$\beta$ đo chênh lệch của $Y_{t}$ giữa chế độ căng thẳng và chế độ bình thường" chỉ đúng khi $S_t\in\{0,1\}$. Với $S_t$ là tỷ lệ, $\beta$ là hiệu ứng tuyến tính ngoại suy từ 0 đến 100% số ngày căng thẳng.
   - **Khuyến nghị sửa:**
     - Đăng ký ngưỡng cụ thể.
     - Đặt quy tắc gộp chế độ khi K=3 và quy tắc gán nhãn theo phương sai ở mỗi lần ước lượng lại.
     - Cố định độ dài giai đoạn ước lượng ban đầu cùng tiêu chí thông tin dùng (AIC hay BIC).
     - Chọn một trong hai: $S_t$ nhị phân (đa số ngày vượt ngưỡng) hoặc liên tục, và diễn giải $\beta$ tương ứng.

6. [MAJOR] **H2 | Phép phân rã $\beta_0-\beta_1$ và biến kiểm soát có thể "ăn" mất hiệu ứng.**
   - **Mâu thuẫn trong định nghĩa $\beta_0$:** $\beta_0$ là hệ số "khi không có $X_t$", nhưng "Biến động thực hiện luôn có mặt trong $X_t$". Không rõ $\beta_0$ có kiểm soát biến động hay không.
   - **Tương quan cơ học:** $S_t$ được suy ra từ phương sai VN-Index, nên tương quan rất cao với biến động thực hiện. Điều kiện VIF > 5 gần như chắc chắn xảy ra, và khi đó quy tắc "báo cáo hai phương trình tách riêng" được kích hoạt. Tuy vậy chưa nói là hai phương trình nào.
   - **Phân rã phụ thuộc thứ tự:** khi có nhiều biến kênh, phép phân rã phụ thuộc thứ tự đưa biến vào.
   - **Biến kênh chưa xác định:** "tương quan đuôi" ước lượng trong cửa sổ 6 tháng cho 30 mã chưa có định nghĩa vận hành (ngưỡng đuôi, trung bình theo cặp hay theo chỉ số). Có hai thước đo tương quan (đuôi và hiệu chỉnh theo biến động), nhưng điều kiện xác nhận chỉ nói "hệ số của tương quan đuôi âm".
   - **Khuyến nghị sửa:**
     - Định nghĩa $\beta_0$ là phương trình có $S_t$ và biến động thực hiện.
     - Dùng phân rã Gelbach (2016), vốn không phụ thuộc thứ tự, cho phần giải thích của từng biến kênh.
     - Nêu rõ hai phương trình tách riêng khi VIF > 5.
     - Viết công thức vận hành cho từng biến kênh (cửa sổ, tần suất, ngưỡng đuôi, cách xử lý ngày khối lượng bằng 0 trong Amihud).
     - Chỉ định một thước đo tương quan là thước đo xác nhận.

7. [MAJOR] **H3 | Đa nhánh, so sánh không cố định và tiêu chí khó kiểm định.**
   - **Lựa chọn của nhà nghiên cứu:** "Cơ chế (i) kết hợp các mô hình theo trọng số Bayes… hoặc chỉ kết hợp các mô hình nằm trong tập tin cậy". Chữ "hoặc" là một lựa chọn để mở.
   - **Chưa nói điều kiện ủng hộ:** có ba cơ chế, nhưng không nói H3 được ủng hộ khi một, khi tất cả, hay khi một cơ chế được chỉ định trước vượt qua.
   - **Đối chứng chưa xác định:** "so với chọn một mô hình" chưa nói là mô hình chọn trước $c$ hay mô hình nào khác.
   - **Tập mô hình thay đổi giữa các giả thuyết:** M~6~ (Garlappi) trùng với cơ chế (ii), M~7~ (Kritzman) trùng với cơ chế (iii). Khi "loại cơ chế (ii) và (iii) khỏi *M*", tập *M* của H3 khác *M* của H1, nên hối tiếc giữa hai giả thuyết không so sánh được.
   - **Độ sụt giảm tối đa:** đây là thống kê trên một quỹ đạo duy nhất. Với vài cửa sổ căng thẳng, "khoảng tin cậy bootstrap khối loại trừ 0" cho độ sụt giảm tối đa gần như không có ý nghĩa thống kê.
   - **Khuyến nghị sửa:**
     - Chỉ định trước một cơ chế chính cho H3, các cơ chế còn lại là phụ. Hiệu chỉnh bội trong nhóm H3.
     - Cố định đối chứng là $c$.
     - Ghi rõ *M* cho từng giả thuyết.
     - Chuyển độ sụt giảm tối đa và CVaR thành thước đo mô tả.

8. [MAJOR] **Không có quy tắc phân biệt "không có khác biệt" với "không đủ bằng chứng".**
   - **Bằng chứng:** "khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam".
   - **Vì sao quan trọng:** không bác bỏ được H~0~ không chứng minh được rằng hiệu ứng bằng 0, nhất là khi công suất thấp như đề cương tự thừa nhận.
   - **Khuyến nghị sửa:** đăng ký một SESOI và một kiểm định tương đương (TOST) cho H1 và cho kết luận về 1/N. Chỉ phát biểu "không đổi theo chế độ" khi khoảng tin cậy nằm trọn trong ±SESOI.

9. [MAJOR] **Đăng ký trước và các bước phụ thuộc dữ liệu (tương đương "quy tắc điều chỉnh").**
   - **Bằng chứng:**
     - "Các độ dài cửa sổ là giá trị dự kiến, và thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất".
     - "Kết quả ước lượng thử ở quý 2 năm thứ nhất sẽ quyết định giữ phương pháp Bayes xấp xỉ hay thay bằng…".
     - "thu hẹp rổ cổ phiếu hoặc giai đoạn mẫu nếu dữ liệu không đủ".
     - Đăng ký "vào quý 4 năm thứ nhất".
   - **Vấn đề:** các bước ước lượng thử diễn ra trước khi đăng ký, nhưng đề cương không nói trên dữ liệu nào. Thí sinh lại đã xem dữ liệu 2019–2025.
   - **Mẫu kiểm tra riêng gần như rỗng:** "Dữ liệu phát sinh sau ngày đăng ký là mẫu kiểm tra riêng". Mẫu này chỉ kéo dài vài tháng đến cuối 2026 hoặc ngoài phạm vi thời gian đã nêu, nên gần như không có cửa sổ căng thẳng.
   - **Khuyến nghị sửa:**
     - Giới hạn ước lượng thử ở giai đoạn chỉ dùng cho ước lượng (trước khoảng 2012) hoặc ở dữ liệu mô phỏng.
     - Đặt trước tiêu chí định lượng cho việc thu hẹp rổ hoặc mẫu (ví dụ tỷ lệ thiếu > x%) và cho việc thay phương pháp ước lượng M~5~ (thời gian tính, chẩn đoán hội tụ).
     - Thừa nhận rằng mẫu kiểm tra sau đăng ký không đủ để kiểm định xác nhận, hoặc đề xuất một mẫu ngoài khác (ví dụ HNX, hay một thị trường cận biên tương tự).

10. [MAJOR] **Xử lý dữ liệu thiếu và mã hủy niêm yết (tương đương "hao hụt") | Chưa được đặc tả.**
    - **Đã có:** đề cương chỉ nói "kể cả những mã đã hủy niêm yết".
    - **Chưa có:**
      - Lợi suất tại ngày hủy niêm yết (dùng giá cuối, giả định −100%, hay lợi suất thay thế).
      - Cách xử lý ngừng giao dịch, ngày khối lượng bằng 0, giá chạm trần/sàn (biên độ dao động).
      - Trọng số của mã bị ngừng giao dịch giữa hai lần tái cân bằng.
      - Lãi suất phi rủi ro khi thiếu dữ liệu trái phiếu 1 năm ở giai đoạn đầu.
      - Dữ liệu vốn hóa tự do chuyển nhượng theo thời điểm (point-in-time) từ 2007.
    - **Vì sao quan trọng:** các lựa chọn này ảnh hưởng trực tiếp đến CE và biến Amihud, đúng ở các giai đoạn căng thẳng.
    - **Khuyến nghị sửa:** đăng ký trước một quy tắc cho từng trường hợp, kèm một phân tích độ nhạy theo các giả định lợi suất hủy niêm yết khác nhau.

### Multiple Testing or Specification Gaps

1. [MAJOR] **Holm cho bốn giả thuyết | Không thể áp dụng như đang viết.**
   - **Bằng chứng:** "Đề tài hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết".
   - **Vấn đề:**
     - Holm cần đúng một p-value cho mỗi giả thuyết. H1 lại dùng quy tắc ba điều kiện đồng thời, H2 hai hệ số, H3 ba tiêu chí cho ba cơ chế. Không rõ p-value nào đi vào thủ tục Holm.
     - H4 được ghi là "thăm dò" nhưng vẫn nằm trong họ bốn giả thuyết xác nhận.
     - Các mức ý nghĩa không thống nhất: phân vị 95% (5%, một phía) cho phân phối rỗng, Holm 10%, MCS 10%, và mức của "khoảng tin cậy… loại trừ 0" chưa nêu.
   - **Bổ sung:**
     - Định nghĩa họ xác nhận là {H1, H2, H3}, đưa H4 ra ngoài.
     - Cho mỗi giả thuyết một thống kê chính và một p-value: H1 là p-value một phía của $\beta_R$ so với phân phối rỗng; H2 dùng kiểm định giao–hợp (intersection–union), p = max của hai p-value một phía; H3 là p-value của cơ chế chính.
     - Áp dụng Holm trên các p-value này. Nêu rõ mức α, một phía hay hai phía, và mức của khoảng tin cậy.

2. [MAJOR] **Bội số bên trong H1 | Nhiều biến thể có thể dùng để chọn kết quả.**
   - **Các biến thể:** $R_t$ hoặc $D_t$; thô hoặc chuẩn hóa; tập đủ hoặc "tập chỉ gồm các mô hình tĩnh"; có hoặc không có M~5~ ("báo cáo kết quả cả khi có lẫn khi không có M~5~"); cửa sổ không chồng lấn hoặc "cửa sổ trượt hằng tháng"; ρ = 3/5/10.
   - **Bổ sung:** chỉ định một đặc tả chính duy nhất ($R_t$, tập đủ bảy mô hình, ρ = 5, cửa sổ không chồng lấn). Ghi nhãn rõ tất cả các biến thể còn lại là kiểm tra độ bền, không dùng để phát biểu "ủng hộ".

3. [MAJOR] **Siêu tham số và quy tắc tinh chỉnh | Chưa đủ ràng buộc.**
   - **Bằng chứng:** "từ một lưới cho trước, bằng cùng một quy tắc và cùng ngân sách tinh chỉnh"; "Quan điểm của M~4~ lấy từ một mô hình dự báo đơn giản".
   - **Bổ sung:**
     - Liệt kê lưới cho từng mô hình.
     - Nêu quy tắc chọn (ví dụ CE trên cửa sổ xác thực lồng bên trong 104 tuần ước lượng, không chạm cửa sổ đánh giá).
     - Đặc tả mô hình dự báo cho M~4~/M~5~ (biến, dạng hàm, độ tin cậy của quan điểm Ω).
     - Nêu ràng buộc chỉ mua và các giới hạn tỷ trọng.
     - Đặc tả hai biến thể M~3~ là ước lượng mẫu và nghịch đảo giả.

4. [MAJOR] **Quy tắc chọn mô hình $c$ | Chỉ có một quy tắc, nhưng $R_t$ phụ thuộc trực tiếp vào nó.**
   - **Bằng chứng:** "chọn trước mô hình *c* có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước".
   - **Bổ sung:** cố định quy tắc chính là quy tắc trên, và đăng ký các quy tắc thay thế (12/24/60 tháng, chọn theo Sharpe, chọn theo MCS) làm kiểm tra độ bền. Nói rõ cách xử lý khi các mô hình hòa nhau.

5. [MINOR] **Suy diễn | Nhiều phương pháp song song, chưa chỉ định cái nào là chính.**
   - **Bằng chứng:** có "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan", "bootstrap khối dừng (Politis và Romano, 1994) cho các hệ số hồi quy" và "khoảng tin cậy bootstrap khối" (Ledoit–Wolf).
   - **Bổ sung:** chỉ định một phương pháp suy diễn chính cho (5), kèm độ dài khối hoặc trễ, số lần lặp và loại khoảng tin cậy (percentile, BCa hay studentized).

6. [MINOR] **Vai trò của tỷ số Sharpe hiệu chỉnh (Bailey và López de Prado, 2014) | Không gắn với giả thuyết nào.**
   - **Bổ sung:** nói rõ tỷ số này dùng cho kiểm định nào. Nếu chỉ để mô tả, ghi rõ như vậy, và nêu số "lần thử" N đưa vào công thức.

7. [MINOR] **Tập tin cậy mô hình (MCS) | Thiếu tham số.**
   - **Bằng chứng:** "kèm số quan sát và công suất kiểm định".
   - **Bổ sung:** nêu hàm tổn thất, thống kê ($T_{max}$ hay $T_R$), độ dài khối, và cách tính "công suất" của MCS.

8. [MINOR] **Phân tích thăm dò (H4) | Đã gắn nhãn, nhưng còn mâu thuẫn.**
   - **Mâu thuẫn:** "phân tán chéo" vừa nằm trong $X_t$ của phương trình xác nhận H2, vừa là biến của H4 thăm dò.
   - **Bổ sung:** tách hẳn H4 thành phương trình riêng, ngoài họ Holm. Bỏ biến này khỏi đặc tả chính của H2, hoặc nói rõ nó chỉ đóng vai trò biến kiểm soát.

### Missing or Inadequate Robustness Checks

1. [MAJOR] **H1 | Thiếu kiểm định giả (placebo) cho biến chế độ.**
   - **Đặc tả gợi ý:** gán ngẫu nhiên nhãn căng thẳng theo khối (giữ nguyên tỷ lệ và độ dài các đợt), ước lượng lại $\beta$ 1.000 lần, rồi báo cáo vị trí của $\beta$ thực trong phân phối giả.

2. [MAJOR] **H1 | Thiếu kiểm tra độ nhạy theo thành phần tập *M*.**
   - **Lý do:** $D_t$ là độ lệch chuẩn trên bảy giá trị, nên rất nhạy với M~3~, mô hình thường có CE cực trị khi căng thẳng. Ngoài kiểm tra bỏ M~5~ và bỏ M~5~/M~7~, đề cương chưa có kiểm tra bỏ từng mô hình.
   - **Đặc tả gợi ý:** kiểm tra bỏ lần lượt từng mô hình (leave-one-model-out). Dùng thước đo phân tán bền (MAD/IQR) thay cho độ lệch chuẩn mẫu.

3. [MAJOR] **H1, H3 | Thiếu kiểm tra phụ thuộc vào một giai đoạn căng thẳng đơn lẻ.**
   - **Đặc tả gợi ý:** lần lượt loại từng giai đoạn căng thẳng (COVID-2020, quý IV/2022, …) và ước lượng lại. Báo cáo $\beta$ theo từng giai đoạn. Đề cương mới chỉ nói chung chung "báo cáo kích thước hiệu ứng cùng khoảng tin cậy theo từng giai đoạn".

4. [MAJOR] **Mô hình chế độ | Mới có định nghĩa thay thế theo ngưỡng; thiếu kiểm tra theo đặc tả mô hình và theo ngưỡng xác suất.**
   - **Đặc tả gợi ý:**
     - Mô hình MS chỉ chuyển phương sai, MS-AR, MS-GARCH.
     - Ngưỡng xác suất lọc 0,5/0,6/0,7/0,8.
     - So sánh xác suất làm trơn và xác suất lọc (chỉ để mô tả).
     - Số chế độ còn lại (2 so với 3).

5. [MAJOR] **Chi phí giao dịch và tính khả thi | "tham số hóa chi phí giao dịch" chưa có giá trị.**
   - **Đặc tả gợi ý:**
     - Giá trị cơ sở (phí + thuế + chênh lệch giá mua–bán, tính theo điểm cơ bản), lưới độ nhạy (ví dụ 0/25/50/100 điểm cơ bản một chiều), và chi phí tác động giá tỷ lệ với Amihud.
     - Mô phỏng biên độ trần/sàn: không khớp được lệnh khi giá chạm trần/sàn.
     - Chu kỳ thanh toán T+2/T+2.5 và giới hạn sở hữu nước ngoài, nếu liên quan.

6. [MINOR] **Thiết kế cửa sổ | Mới có kiểm tra theo tần suất dữ liệu tháng và tái cân bằng quý.**
   - **Đặc tả gợi ý:** cửa sổ đánh giá 3/12 tháng và cửa sổ ước lượng 52/156 tuần.
   - **Lưu ý:** với dữ liệu tháng, tỷ lệ N/T có thể vượt 0,5, kéo theo việc M~3~ chuyển sang nghịch đảo giả. Cần nêu trước độ dài cửa sổ ước lượng cho kiểm tra độ bền dùng dữ liệu tháng.

7. [MINOR] **Rổ cổ phiếu | Có đối chiếu VN30/VN100, nhưng chưa có biến thể theo kích thước rổ.**
   - **Đặc tả gợi ý:** rổ 20/50 mã, kèm cùng quy tắc chọn theo thời điểm.

8. [MINOR] **Biến kiểm soát vĩ mô | Chưa nói đưa vào phương trình nào.**
   - **Bằng chứng:** "bổ sung chỉ số giá tiêu dùng, tỷ giá… và lãi suất điều hành làm biến kiểm soát".
   - **Lưu ý:** với khoảng 28 quan sát, thêm ba biến nữa càng làm trầm trọng vấn đề số bậc tự do.
   - **Đặc tả gợi ý:** đưa từng biến một, hoặc gộp thành một chỉ số thành phần chính duy nhất.

### Minor Statistical Issues

1. [MINOR] **Phương trình (1) | Tần suất và đơn vị chưa nêu.**
   - **Vấn đề:** chưa nói CE tính trên lợi suất ngày hay tháng, lợi suất vượt trội hay lợi suất thô, có năm hóa hay không. ρ = 5 chỉ có nghĩa khi đơn vị đã rõ.
   - **Sửa:** ghi rõ đơn vị, ví dụ: lợi suất vượt trội tháng, năm hóa ×12.

2. [MINOR] **Tỷ lệ N/T của M~3~ | Ngưỡng gần như không bao giờ bị chạm trong cấu hình cơ sở.**
   - **Bằng chứng:** "tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5". Với 30/104 ≈ 0,29, ngưỡng không bao giờ bị chạm, nên quy tắc này chỉ có hiệu lực trong kiểm tra độ bền dùng dữ liệu tháng.
   - **Sửa:** ghi rõ điều này.

3. [MINOR] **Định nghĩa "cửa sổ độc lập ở chế độ căng thẳng" của quy tắc không kết luận.**
   - **Vấn đề:** chưa rõ cửa sổ được xếp là "căng thẳng" khi $S_t$ > bao nhiêu, và hai cửa sổ liền kề trong cùng một đợt có được tính là hai giai đoạn độc lập hay không.
   - **Sửa:** định nghĩa riêng "cửa sổ căng thẳng" và "giai đoạn căng thẳng độc lập" (ví dụ cách nhau ít nhất 12 tháng).

4. [MINOR] **Cửa sổ trượt hằng tháng | Chồng lấn nặng.**
   - **Vấn đề:** cửa sổ trượt hằng tháng chồng lấn 5/6, gây tự tương quan theo cấu trúc MA(5).
   - **Sửa:** dùng HAC với số trễ ít nhất 5, hoặc bootstrap khối có độ dài ít nhất 6.

5. [MINOR] **Tính một phía | Chưa nói rõ.**
   - **Vấn đề:** H1 có hướng ("dương và vượt phân vị 95%", tức một phía 5%), nhưng "khoảng tin cậy… loại trừ 0" không rõ là 90% hay 95%, một phía hay hai phía. Kích thước kiểm định của quy tắc ba điều kiện đồng thời không được tính.
   - **Sửa:** nêu rõ mức và phía của từng điều kiện, và nêu kích thước kiểm định tổng của quy tắc đồng thời.

6. [MINOR] **Mục "Quy tắc dừng/phân tích giữa kỳ" | Hầu như không áp dụng.**
   - **Lý do:** không có phân tích giữa kỳ theo nghĩa RCT. Các điểm quyết định phụ thuộc dữ liệu đã nêu ở mục Major 9.

7. **Không áp dụng (kèm lý do):**
   - **ICC, hệ số thiết kế, phân cụm theo đơn vị ngẫu nhiên hóa:** không có cụm hay ngẫu nhiên hóa; độ phụ thuộc được xử lý bằng HAC/bootstrap khối.
   - **Không tuân thủ, lan tỏa, LATE/IV:** không có can thiệp, không dùng biến công cụ.
   - **Hao hụt người tham gia:** không có người tham gia. Phần tương đương là dữ liệu thiếu và mã hủy niêm yết, đã nêu ở mục Major 10.

---

## Data, Sample, Implementation & Operational Plan

## Agent 5: Data, Sample, Implementation & Operational Plan

Phạm vi rà soát: chỉ hai tệp `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/de-cuong-goc.md` và `.../hinh-van-ban.txt`. Đây là nghiên cứu quan sát trên dữ liệu thị trường công khai. Vì vậy "mẫu" được hiểu là rổ cổ phiếu, giai đoạn và các cửa sổ đánh giá. "Ngẫu nhiên hóa", "nhánh can thiệp" và "đồng thuận" chỉ được xét ở dạng tương đương. Mục nào không áp dụng được thì ghi rõ "không áp dụng" kèm lý do.

### Sample or Data Access Concerns

1. [CRITICAL] **Theo chính quy tắc của đề cương, H~1~ nhiều khả năng sẽ ra "không kết luận", nhưng đề cương chưa ước tính trước số cửa sổ căng thẳng.** | Bằng chứng: "Với mẫu 2007--2026, đề tài dự kiến có khoảng 28 cửa sổ đánh giá độc lập, và khủng hoảng tài chính toàn cầu chủ yếu phục vụ ước lượng chế độ"; "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Phần mẫu tính được mức hối tiếc bắt đầu khoảng năm 2012 ("chỉ tính được từ khoảng năm thứ năm của mẫu"). Trong phần này, đề cương chỉ nêu các cú sốc 2020 (COVID-19) và từ quý IV/2022 (trái phiếu doanh nghiệp). Với cửa sổ 6 tháng không chồng lấn, khó có đủ 10 cửa sổ căng thẳng. Ngoài ra, $S_t$ là một tỷ lệ liên tục ("tỷ lệ số ngày trong cửa sổ có xác suất lọc... vượt ngưỡng"), nhưng đề cương chưa định nghĩa thế nào là một "cửa sổ ở chế độ căng thẳng" khi đếm. | Đề xuất: Việc xác định chế độ chỉ cần chuỗi VN-Index. Nên ước lượng mô hình Markov trên VN-Index trước khi đăng ký và báo cáo số cửa sổ căng thẳng dự kiến. Quy tắc phân loại cửa sổ (ví dụ $S_t$ > một ngưỡng) cần được cố định. Nếu số dự kiến dưới 10, cần thiết kế lại trước khi đăng ký: dùng cửa sổ ngắn hơn, cửa sổ chồng lấn có hiệu chỉnh phụ thuộc, hoặc mở rộng sang HNX/các thị trường ASEAN. Cũng có thể hạ H~1~ xuống mục tiêu ước lượng, thay vì để kế hoạch chính dẫn tới kết quả không kết luận.

2. [MAJOR] **Nhà cung cấp dữ liệu chưa có tên, quyền truy cập chưa được xác nhận.** | Bằng chứng: "Nguồn dữ liệu là HOSE và một nhà cung cấp dữ liệu thương mại"; "thí sinh xác nhận nguồn và độ dài dữ liệu trong quý 1 năm thứ nhất". Thông tin cơ quan công tác bị để trống ("Cơ quan công tác:"), và đề cương không có dòng ngân sách nào cho giấy phép dữ liệu. | Đề xuất: Nêu tên nhà cung cấp và loại giấy phép (cá nhân, học thuật hay qua trường). Nêu ai trả phí. Trước khi nhập học, xác nhận nhà cung cấp có ba loại dữ liệu cho năm 2007: giá điều chỉnh, khối lượng và mã hủy niêm yết.

3. [MAJOR] **Dữ liệu mã đã hủy niêm yết và vốn hóa tự do chuyển nhượng lịch sử chưa chắc có sẵn, mà cả hai là đầu vào của quy tắc chọn rổ theo thời điểm.** | Bằng chứng: "kể cả những mã đã hủy niêm yết"; "rổ cổ phiếu gồm 30 mã có giá trị giao dịch bình quân ba tháng và vốn hóa tự do chuyển nhượng lớn nhất, xác định chỉ bằng dữ liệu có tại ngày đó". Đề cương chưa nói tỷ lệ tự do chuyển nhượng lịch sử (từ 2007) lấy từ đâu, cũng chưa có phương án dự phòng nếu thiếu. | Đề xuất: Nêu nguồn cụ thể cho tỷ lệ free-float theo thời điểm. Nếu không có, đăng ký trước quy tắc thay thế, ví dụ vốn hóa toàn bộ, và đưa vào kiểm tra độ bền. Nêu cách xử lý lợi suất ở kỳ hủy niêm yết.

4. [MAJOR] **Quy tắc xây dựng rổ chưa đủ chi tiết để tái lập.** Đây là dạng tương đương của "khung chọn mẫu" và "giao thức ngẫu nhiên hóa". | Bằng chứng: "30 mã có giá trị giao dịch bình quân ba tháng và vốn hóa tự do chuyển nhượng lớn nhất". Đề cương chưa nói hai tiêu chí kết hợp ra sao (xếp hạng tổng hợp, lọc tuần tự hay trọng số). Đề cương cũng chưa nêu: thời gian niêm yết tối thiểu (mỗi mã cần đủ 104 tuần để ước lượng hiệp phương sai), cách xử lý mã bị đình chỉ hoặc tạm ngừng giao dịch, vùng đệm chống xoay vòng thành phần, và cách xử lý giá chạm trần/sàn hay giá không giao dịch. | Đề xuất: Viết giao thức xây dựng rổ dạng mã giả và đưa vào tệp đăng ký OSF, gồm thứ tự lọc, ngưỡng dữ liệu thiếu, quy tắc thay thế mã và tần suất cập nhật rổ.

5. [MAJOR] **Biến kết quả và biến kênh chưa được gắn với định nghĩa vận hành cụ thể (codebook).** | Bằng chứng: "tương quan đuôi và tương quan hiệu chỉnh theo biến động"; "độ phân tán chéo của lợi suất"; "Biến động thực hiện luôn có mặt trong $X_{t}$". Đề cương chưa nêu ngưỡng đuôi, cửa sổ tính Amihud, đơn vị (VND hay tỷ VND), CSSD hay CSAD, hay tần suất tính biến động thực hiện. Tham số chi phí giao dịch cũng chưa có giá trị: "Đề tài tham số hóa chi phí giao dịch". Lưới siêu tham số cũng chưa được nêu: "từ một lưới cho trước". | Đề xuất: Lập bảng biến gồm tên, công thức, tần suất, cửa sổ, nguồn và giả thuyết liên quan, rồi nộp kèm đăng ký trước. Ghi giá trị cơ sở và dải độ nhạy cho chi phí giao dịch (phí, thuế bán, trượt giá).

6. [MAJOR] **Mẫu kiểm tra "sau ngày đăng ký" quá ngắn và chưa có kế hoạch phân tích. Phân đoạn thời gian giữa mẫu chính và mẫu kiểm tra cũng chưa rõ.** | Bằng chứng: "Dữ liệu phát sinh sau ngày đăng ký là mẫu kiểm tra riêng"; đăng ký ở "Quý 4" năm 1; mẫu chính "từ 2007 đến 2026". Dữ liệu từ đầu 2027 đến ngày đăng ký không rõ thuộc mẫu nào. Đến năm 3, mẫu kiểm tra chỉ có khoảng 2–4 cửa sổ 6 tháng. | Đề xuất: Ghi ngày cắt mẫu chính. Nêu rõ mẫu kiểm tra dùng để làm gì (mô tả hay kiểm định xác nhận) và thừa nhận công suất của nó gần như bằng không.

7. [MINOR] **Lãi suất phi rủi ro và các biến vĩ mô chưa có nguồn.** | Bằng chứng: "lợi suất trái phiếu chính phủ kỳ hạn một năm làm lãi suất phi rủi ro"; "chỉ số giá tiêu dùng, tỷ giá đô la Mỹ so với đồng Việt Nam và lãi suất điều hành". Chuỗi lợi suất 1 năm từ 2007 có thể bị đứt quãng. | Đề xuất: Nêu nguồn (HNX, NHNN, GSO hoặc nhà cung cấp) và quy tắc nội suy hoặc thay thế khi thiếu.

8. [MINOR] **Giai đoạn ước lượng chế độ ban đầu chưa được xác định.** | Bằng chứng: "Số chế độ (hai hoặc ba) do tiêu chí thông tin quyết định trên giai đoạn ước lượng ban đầu". | Đề xuất: Ghi rõ ngày đầu và ngày cuối của giai đoạn này, và đưa vào tệp đăng ký.

9. [MINOR] **Phần khảo sát khung quy định và mức dùng mô hình của công ty quản lý quỹ chưa có phương pháp thu thập.** | Bằng chứng: "Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này, cùng mức độ họ dùng mô hình định lượng... từ báo cáo của cơ quan quản lý và tài liệu công bố của các công ty quản lý quỹ" (được xếp vào quý 1 năm 1). | Đề xuất: Nêu danh sách văn bản hoặc tổ chức cần rà soát, tiêu chí mã hóa, và nói rõ phần này chỉ phục vụ bối cảnh, không phải dữ liệu kiểm định.

### Implementation or Feasibility Risks

1. [MAJOR] **Ước lượng thử trên chính dữ liệu căng thẳng trước khi đăng ký, và chỉnh độ dài cửa sổ sau khi chạy thử, làm yếu giá trị của đăng ký trước.** | Vì sao quan trọng: Bảng 5 ghi "Quý 2: ước lượng thử bảy mô hình trên giai đoạn 2019--2025 để đo thời gian tính và số quan sát ở chế độ căng thẳng", trong khi đăng ký ở "Quý 4". Mục 4.3.6 viết thêm: "Các độ dài cửa sổ là giá trị dự kiến, và thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất". Giai đoạn 2019–2025 chứa cả hai giai đoạn căng thẳng chính của phần mẫu tính được hối tiếc. Thí sinh lại đã thừa nhận "không thể khẳng định chưa từng thấy kết quả ở chế độ căng thẳng". | Giảm thiểu: Chạy thử trên dữ liệu mô phỏng hoặc trên giai đoạn không dùng cho kiểm định (ví dụ 2007–2011). Chỉ đo thời gian tính, không xuất mức hối tiếc hay thứ hạng mô hình. Ghi nhật ký những gì đã xem và đưa vào tệp đăng ký. Cố định độ dài cửa sổ bằng lập luận lý thuyết hoặc mô phỏng, không dựa vào kết quả chạy thử.

2. [MAJOR] **Thí sinh có nhiều cam kết song song, có nguy cơ không đủ thời gian.** | Vì sao quan trọng: Mục 8.2 ghi thí sinh "đang theo học ngành Kế toán hệ vừa làm vừa học tại Đại học Kinh tế Quốc dân (năm thứ ba), ngành Công nghệ thông tin hệ đào tạo từ xa tại Học viện Công nghệ Bưu chính Viễn thông (năm thứ ba), và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 07/2026". Cùng lúc đó là "chín bản thảo đang ở các bước phản biện" (thí sinh là "tác giả liên hệ của cả 9 bản thảo") và 9 tín chỉ bổ sung trong hai quý đầu. Năm 1 vốn đã dồn nhiều việc nặng: xác nhận dữ liệu, chạy thử, làm sạch, đọc toàn văn, đăng ký trước. | Giảm thiểu: Nêu kế hoạch cụ thể sẽ hoàn thành, bảo lưu hay dừng chương trình nào trước khi nhập học. Ước tính số giờ mỗi tuần dành cho luận án. Đặt mốc kiểm tra tiến độ với người hướng dẫn.

3. [MAJOR] **Chưa ước tính khối lượng tính toán, nhất là M~5~ (ABC-MCMC) và Markov theo cửa sổ mở rộng ước lượng lại hằng tháng.** | Vì sao quan trọng: Mô hình chế độ được "ước lượng lại tham số chỉ bằng dữ liệu đến ngày đó" tại mỗi ngày tái cân bằng (khoảng 200+ lần trong 2007–2026). Mỗi lần lại nhân với lưới siêu tham số của năm mô hình, các kiểm tra độ bền (dữ liệu tháng, tái cân bằng quý, định nghĩa chế độ thay thế, ρ = 3/5/10) và cửa sổ trượt phụ. Đề cương chỉ viết "ước lượng được bằng phần mềm thống kê thông dụng" và để quyết định về phương pháp M~5~ sang quý 2. Đề cương không nói tới phần cứng, máy chủ hay kinh phí. | Giảm thiểu: Ước tính số lần ước lượng và thời gian CPU. Nêu hạ tầng tính toán (máy của trường, đám mây) và nguồn kinh phí. Đăng ký trước một phương án ước lượng thay thế cho M~5~ (ví dụ EM hoặc Hamilton filter) để dùng nếu ABC-MCMC quá chậm.

4. [MAJOR] **Đặc tả "nhánh" (bảy mô hình và ba cơ chế) chưa đủ để đánh giá độ trung thành khi triển khai.** Mục "treatment arms" theo nghĩa RCT không áp dụng, vì không có can thiệp lên đối tượng. Dạng tương đương ở đây là các chiến lược danh mục. | Vì sao quan trọng: Có nhiều chỗ còn để ngỏ: "Quan điểm của M~4~ lấy từ một mô hình dự báo đơn giản" (không nêu mô hình nào); "cùng một quy tắc và cùng ngân sách tinh chỉnh" (không nêu quy tắc); cơ chế (i) là "theo trọng số Bayes... hoặc chỉ kết hợp các mô hình nằm trong tập tin cậy" (chữ "hoặc" để lại một lựa chọn chưa chốt). Những chỗ này mở rộng không gian lựa chọn của nhà nghiên cứu. | Giảm thiểu: Mỗi mô hình và mỗi cơ chế cần một thẻ đặc tả: đầu vào, ràng buộc, lưới siêu tham số, quy tắc chọn siêu tham số và phương án chính so với phương án phụ.

5. [MINOR] **Lịch công bố dồn vào cuối kỳ, khó kịp yêu cầu công bố trước bảo vệ.** | Vì sao quan trọng: Bảng 5 ghi "Năm 3... viết bài báo 2 và 3", còn năm 4 quý 3–4 là "chỉnh sửa theo góp ý và bảo vệ". Thời gian phản biện thường từ 6 đến 18 tháng. Đề cương có nhắc "quy định công bố của chương trình đào tạo tiến sĩ" nhưng không đối chiếu lịch với quy định đó. | Giảm thiểu: Gửi bài báo 1 trước, sớm nhất có thể (ví dụ quý 4 năm 2). Liệt kê điều kiện công bố tối thiểu để được bảo vệ và lập mốc gửi bài.

6. [MINOR] **Chưa đề cập rủi ro khả năng thực thi trên HOSE ngoài thanh khoản.** | Vì sao quan trọng: Danh mục "chỉ mua" 30 mã chịu biên độ dao động giá, lô giao dịch, chu kỳ thanh toán và giới hạn sở hữu nước ngoài. Đề cương chỉ nêu "Luận án sẽ ghi kèm nguồn của biên độ dao động giá, mức thuế, phí giao dịch". | Giảm thiểu: Nêu cách mô phỏng lệnh không khớp được khi giá chạm trần/sàn. Nêu các giả định về lô và thanh toán.

7. [MINOR] **Thông tin người hướng dẫn không thống nhất trong văn bản, chưa thấy xác nhận cam kết.** | Vì sao quan trọng: Trang bìa ghi "Người hướng dẫn khoa học (dự kiến): PGS.TS. Hà Hồng Hạnh", nhưng mục 10 ghi "Người hướng dẫn chính (dự kiến): GS.TS. Nguyễn Đức Khương". | Giảm thiểu: Thống nhất thông tin. Nêu tình trạng chấp thuận của từng người hướng dẫn.

8. [MINOR] **Phương án dự phòng về dữ liệu còn chung chung.** | Vì sao quan trọng: Đề cương chỉ viết "thu hẹp rổ cổ phiếu hoặc giai đoạn mẫu". Thu hẹp giai đoạn lại làm vấn đề công suất ở mục Sample #1 nặng thêm. | Giảm thiểu: Nêu ngưỡng định lượng kích hoạt dự phòng (ví dụ dữ liệu hủy niêm yết phủ dưới X%). Nêu tác động dự kiến lên số cửa sổ căng thẳng trong từng kịch bản.

### Ethical or Regulatory Gaps

1. [MINOR] **Chưa nêu rõ tình trạng phê duyệt đạo đức (IRB).** | Nên trình bày ở: mục 4.3.3 hoặc 4.3.10. | Hành động: Đề tài không có đối tượng là con người, và đề cương đã ghi "Dữ liệu không chứa thông tin cá nhân". Vì vậy phê duyệt IRB nhiều khả năng không áp dụng. Dù vậy, nên viết một câu khẳng định không cần phê duyệt đạo đức, hoặc ghi là đã được đơn vị đào tạo miễn xét.

2. Không áp dụng: **đồng thuận tham gia (informed consent)**, vì không thu thập dữ liệu từ cá nhân và không có khảo sát hay phỏng vấn ("không dùng khảo sát hay phương pháp định tính"). Cũng **không áp dụng** với **nhóm dễ tổn thương**, vì không có người tham gia.

3. [MAJOR] **Giấy phép dữ liệu thương mại có thể xung đột với cam kết minh bạch và tái lập.** | Nên trình bày ở: mục 4.3.10 ("Về minh bạch") và tệp đăng ký OSF. | Bằng chứng: "thí sinh lưu mã nguồn và tệp đăng ký trước" và "điều khoản giấy phép dữ liệu" (chỉ hứa sẽ ghi kèm). | Hành động: Nêu rõ phần nào được công bố công khai (mã nguồn, chuỗi lợi suất danh mục đã tổng hợp, danh sách mã theo thời điểm) và phần nào bị giấy phép hạn chế (giá gốc). Nêu cách người khác có thể tái lập.

4. [MINOR] **Xung đột lợi ích về mặt trí tuệ với M~5~ đã được ghi nhận, nhưng chưa có cơ chế kiểm soát độc lập.** | Nên trình bày ở: mục 4.3.5. | Bằng chứng: "Vì M~5~ do thí sinh phát triển, đề tài xử lý M~5~ như mọi mô hình khác và báo cáo kết quả cả khi có lẫn khi không có M~5~". | Hành động: Cách xử lý hiện tại là hợp lý. Có thể bổ sung một bước để người hướng dẫn hoặc đồng nghiệp rà soát mã của các mô hình đối thủ, đảm bảo chúng được cài đặt không kém M~5~.

5. [MINOR] **Thủ tục giám sát mô hình được trình bày như hàm ý cho tổ chức và cơ quan giám sát.** | Nên trình bày ở: mục 4.4. | Hành động: Đề cương đã ghi "chưa qua kiểm nghiệm với người dùng, và chỉ là tư liệu tham khảo", như vậy là đủ. Nếu sau này thử nghiệm với công ty quản lý quỹ (mục 9) thì lúc đó mới phát sinh yêu cầu về đạo đức, bảo mật và thỏa thuận dữ liệu.

### Missing or Weak Supporting Documents

1. [CRITICAL] **Thiếu tính toán công suất hoặc mô phỏng thiết kế.** | Vì sao cần: Có rất ít cửa sổ ("khoảng 28 cửa sổ"), ngưỡng "dưới 10" cửa sổ căng thẳng, kiểm định ba điều kiện đồng thời cho H~1~, hiệu chỉnh Holm 10% cho bốn giả thuyết và phân phối rỗng 1.000 lần bootstrap. Chưa có con số nào cho biết thiết kế có khả năng phát hiện hiệu ứng hay không. Đề cương chỉ cam kết báo cáo "số quan sát và công suất kiểm định" sau khi phân tích. | Hành động: Lập bảng mô phỏng Monte Carlo. Mô phỏng chuỗi lợi suất của bảy mô hình với các mức chênh lệch hối tiếc khác nhau giữa hai chế độ, rồi tính xác suất thỏa cả ba điều kiện của H~1~ khi có N cửa sổ căng thẳng. Nộp kèm tệp đăng ký OSF.

2. [MAJOR] **Thiếu kế hoạch quản lý dữ liệu (DMP).** | Vì sao cần: Thiết kế phụ thuộc vào dữ liệu theo thời điểm (rổ, free-float, hủy niêm yết) từ một nhà cung cấp thương mại. Cần lưu ảnh chụp dữ liệu có dấu thời gian, quản lý phiên bản, theo dõi điều chỉnh giá, nêu rõ ràng buộc giấy phép và cách lưu trữ. | Hành động: Soạn DMP ngắn gồm nguồn, ngày tải, quy trình làm sạch, nơi lưu, quyền truy cập và phần được chia sẻ.

3. [MAJOR] **Thiếu bảng mẫu (mock tables) và khung mã (code shells).** | Vì sao cần: Đây là cách cụ thể nhất để khóa "nhóm kết quả chính" và đặc tả của phương trình (5). Bảng mẫu cho H~1~–H~4~ cần ghi rõ dòng, cột, sai số chuẩn, phân vị rỗng và cột "số cửa sổ căng thẳng độc lập" như đề cương đã hứa. | Hành động: Đưa bảng mẫu và khung mã (pipeline từ dữ liệu đến kết quả, có thể chạy trên dữ liệu mô phỏng) vào tệp đăng ký.

4. [MAJOR] **Thiếu bản nháp tệp đăng ký OSF.** | Vì sao cần: Đề cương liệt kê những gì tệp đăng ký "cố định": "độ dài các cửa sổ, siêu tham số của bảy mô hình, số chế độ và ngưỡng xác suất lọc, mức ý nghĩa...". Nhiều giá trị trong số này hiện vẫn chưa có, ví dụ ngưỡng xác suất lọc. | Hành động: Đính kèm bản nháp theo mẫu OSF Preregistration hoặc mẫu cho nghiên cứu dữ liệu thứ cấp, ghi rõ các ô còn để trống và thời điểm chốt từng ô.

5. [MAJOR] **Thiếu codebook biến và giao thức xây dựng rổ cổ phiếu.** Đây là dạng tương đương của "giao thức ngẫu nhiên hóa" và "khung chọn mẫu". | Vì sao cần: Xem mục Sample #4 và #5. | Hành động: Soạn hai tài liệu ngắn: giao thức chọn rổ theo thời điểm (mã giả) và codebook biến (định nghĩa, công thức, tần suất, nguồn).

6. Không áp dụng: **bảng hỏi hoặc công cụ khảo sát**, vì đề tài "không dùng khảo sát hay phương pháp định tính". Cũng **không áp dụng** với **giao thức ngẫu nhiên hóa** theo nghĩa RCT, vì không có phân nhóm can thiệp. Dạng tương đương đã được nêu ở mục 5.

7. [MINOR] **Thiếu ước tính nguồn lực (kinh phí dữ liệu, hạ tầng tính toán).** | Vì sao cần: Xem mục Implementation #3 và Sample #2. | Hành động: Thêm một bảng ngắn về nguồn lực (dữ liệu, máy tính, phần mềm) kèm nguồn tài trợ dự kiến.

---

## Clarity, Writing Quality & Pre-specification Completeness

## Agent 1: Clarity, Writing Quality & Pre-specification Completeness

Phạm vi rà soát: chỉ hai tệp `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/de-cuong-goc.md` và `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/hinh-van-ban.txt`. Đây là nghiên cứu quan sát trên dữ liệu thị trường công khai. Vì vậy các kiểm tra dành cho RCT hay khảo sát được đánh dấu "không áp dụng" và nêu lý do (xem mục Structural, ý 10). Tôi không sửa tệp nào.

### Critical Vagueness or Specification Gaps

1. [CRITICAL] 4.3.10 và 4.3.7, phương trình (5) | Chưa định nghĩa thế nào là một "cửa sổ ở chế độ căng thẳng", trong khi đó lại là ngưỡng của quy tắc không kết luận: "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận". Trong khi đó $S_t$ là biến liên tục: "tỷ lệ số ngày trong cửa sổ có xác suất lọc của chế độ căng thẳng vượt ngưỡng đăng ký trước". Khái niệm "số giai đoạn căng thẳng độc lập" cũng chưa được định nghĩa. | Quy tắc quyết định quan trọng nhất của PAP (ủng hộ, bác bỏ hay không kết luận) đang phụ thuộc vào một phân loại chưa có. Chỉ cần chọn ngưỡng $S_t$ sau khi xem dữ liệu (ví dụ $S_t>0$, $\geq 0{,}5$ hay $=1$) là đủ đẩy số cửa sổ căng thẳng qua lại mốc 10. Ngoài ra chưa rõ quy tắc này áp dụng cho H1 hay cho cả H2, H3, H4. Với khoảng 28 cửa sổ trong giai đoạn 2012–2026, nhiều khả năng H1–H3 sẽ rơi vào "không kết luận". | Cần định nghĩa bằng công thức, chẳng hạn: "cửa sổ $w$ là cửa sổ căng thẳng khi $S_w \geq 0{,}5$". Cần định nghĩa "giai đoạn căng thẳng độc lập" là chuỗi các cửa sổ căng thẳng liên tiếp, cách nhau ít nhất k cửa sổ bình thường. Cần nêu rõ quy tắc áp dụng cho những giả thuyết nào. Nên đưa ước tính số cửa sổ căng thẳng kỳ vọng (từ các cú sốc 2018, 2020, 2022) vào đề cương ngay từ bây giờ.

2. [CRITICAL] 4.3.6 so với Bảng 2 và 4.3.7 | Biến kết quả chính đang mơ hồ. Bảng 2 ghi "Kết quả chính: mức hối tiếc", nhưng 4.3.6 viết "phân tích chính chia $D_t$ và $R_t$ cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình trong cùng cửa sổ". Quy tắc H1 chỉ ghi "$\beta$ của $R_t$", không nói là $R_t$ thô hay $R_t$ đã chuẩn hóa. Mẫu số cũng chưa xác định: có 21 cặp mô hình, vậy dùng sai số chuẩn của cặp nào, hay trung bình, trung vị, hay của cặp (o, c)? Độ dài khối và số lần lặp của bootstrap này cũng chưa có. | Đây là lựa chọn biến kết quả chính, đúng loại "bậc tự do của nhà nghiên cứu" mà PAP phải khóa lại. Hai phiên bản của biến kết quả và nhiều cách chuẩn hóa sẽ tạo ra nhiều kết quả khả dĩ. | Cần ghi một câu duy nhất: "Biến kết quả chính của H1 là $\tilde R_t = R_t / \widehat{se}_t$, với $\widehat{se}_t$ = [công thức cụ thể], bootstrap khối dừng B = …, độ dài khối kỳ vọng = …". $R_t$ thô chuyển sang kết quả phụ.

3. [CRITICAL] 4.3.10, 4.3.7 và 4.3.8 | Kiểm định bội và mức ý nghĩa chưa được vận hành hóa. Đề cương viết "hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết", nhưng: (a) H1 dùng quy tắc ba điều kiện ("vượt phân vị 95% của phân phối rỗng", tức mức 5% một phía), nên không có một giá trị p duy nhất để đưa vào Holm; (b) H2 có hai hệ số; (c) H3 có ba cơ chế nhân ba tiêu chí (CE, mức hối tiếc, MDD); (d) H4 "chỉ báo cáo… như kết quả thăm dò" nhưng vẫn nằm trong họ bốn giả thuyết; (e) tệp đăng ký sẽ còn cố định "mức ý nghĩa", tức là mức ý nghĩa vẫn chưa chốt. | Không rõ họ kiểm định gồm những gì, giá trị p nào được hiệu chỉnh và mức 5% hay 10% được dùng. Người đọc thứ ba không thể tái tạo phán quyết. | Cần một bảng "họ kiểm định" liệt kê từng giá trị p (giả thuyết, thống kê, phía của kiểm định, cách tính p). Cần nói rõ Holm áp dụng ở cấp giả thuyết hay ở cấp hệ số, và nêu cách gộp nhiều điều kiện thành một p (ví dụ lấy p lớn nhất theo nguyên tắc intersection-union). Nên đưa H4 ra khỏi họ xác nhận. Cần thống nhất 5% hay 10%.

4. [CRITICAL] 4.3.5, 4.3.6, 4.3.9 và Bảng 5 | Nhiều lựa chọn then chốt được quyết định sau khi đã chạm vào dữ liệu chính. Các trích dẫn: "Quý 2: ước lượng thử bảy mô hình trên giai đoạn 2019--2025 để đo thời gian tính và số quan sát ở chế độ căng thẳng" (giai đoạn này nằm trong mẫu chính và chứa hai giai đoạn căng thẳng); "Các độ dài cửa sổ là giá trị dự kiến, và thí sinh sẽ biện minh chúng sau khi ước lượng thử ở năm thứ nhất"; việc đăng ký diễn ra ở Quý 4. | Độ dài cửa sổ, siêu tham số và số chế độ có thể bị điều chỉnh theo những gì đã thấy ở bản chạy thử trên chính các giai đoạn căng thẳng cần kiểm định. "Khai rõ những kết quả đã xem" là cần thiết nhưng chưa đủ. | Cần ghi rõ bản chạy thử chỉ xuất ra thời gian tính và số quan sát, không tính CE hay mức hối tiếc theo chế độ, hoặc chạy thử trên dữ liệu mô phỏng. Nếu buộc phải xem kết quả thì nên chốt độ dài cửa sổ ngay trong đề cương (104 tuần, 6 tháng, 36 tháng) và chỉ cho phép thay đổi theo một tiêu chí khách quan đã viết sẵn, ví dụ khi thời gian tính vượt X giờ.

5. [CRITICAL] 4.3.7, Bảng 2 (H2) | Dấu của giả thuyết H2 có hai cách đọc: "H~2~ được ủng hộ khi hệ số của độ phi thanh khoản dương, hệ số của tương quan đuôi âm…". Cụm "tương quan đuôi âm" vừa có thể hiểu là tương quan ở đuôi âm (lower-tail correlation), vừa có thể hiểu là "hệ số … âm". Phần chú thích trong Bảng 2 ("tương quan cao làm các danh mục chỉ mua hội tụ") gợi ý cách đọc "hệ số âm". Ngoài ra $X_t$ chứa hai biến tương quan ("tương quan đuôi và tương quan hiệu chỉnh theo biến động") nhưng không nói biến nào là biến kiểm định. | Một giả thuyết có hướng mà dấu mơ hồ thì kết quả theo dấu nào cũng có thể diễn giải thành "ủng hộ". | Nên viết lại: "hệ số của tương quan vượt ngưỡng ở đuôi dưới (Longin–Solnik, ngưỡng q = …) mang dấu âm". Cần chỉ định một biến tương quan duy nhất cho kiểm định xác nhận, biến còn lại đưa vào kiểm tra độ bền.

6. [MAJOR] 4.3.4 | Mô hình chế độ chưa được đặc tả đầy đủ. Các trích dẫn: "Số chế độ (hai hoặc ba) do tiêu chí thông tin quyết định trên giai đoạn ước lượng ban đầu" (chưa nói AIC, BIC hay HQ, và giai đoạn ban đầu dài bao lâu); dạng mô hình chưa có (chuyển đổi trung bình và phương sai? có số hạng AR? phân phối chuẩn hay t?); ngưỡng xác suất lọc chưa có giá trị. Nếu có ba chế độ thì chế độ nào là "bình thường"? Nếu chế độ có phương sai cao nhất không có lợi suất kỳ vọng thấp hơn thì xử lý thế nào? Khi ước lượng lại hằng tháng thì xử lý hoán đổi nhãn (label switching) ra sao? Trong một cửa sổ 6 tháng, xác suất lọc tính bằng bộ tham số của ngày nào? | $S_t$ là biến giải thích trung tâm, và mỗi lựa chọn trên đều thay đổi $S_t$. | Cần ghi cụ thể: "MS(k)-mean-variance, sai số Gauss, không AR; chọn k theo BIC trên 2007–20xx; ngưỡng xác suất 0,5". Với k = 3: gộp hai chế độ không căng thẳng thành "bình thường". Cần một quy tắc gán nhãn theo phương sai ở mỗi lần ước lượng lại, và một quy tắc dự phòng khi điều kiện về trung bình bị vi phạm.

7. [MAJOR] 4.3.6, phương trình (1) | Chưa nói lợi suất tương đương chắc chắn (CE) tính trên tần suất nào: ngày, tuần hay tháng trong cửa sổ 6 tháng? Có năm hóa không? Dùng lợi suất thô hay lợi suất vượt trội? Giá trị $\rho$ = 5 chỉ có nghĩa khi đơn vị đã được xác định. | Thứ hạng mô hình và $R_t$ thay đổi theo đơn vị đo. Với 6 quan sát tháng thì $\sigma^2$ gần như là nhiễu. | Cần ghi: "$\mu$, $\sigma^2$ ước lượng từ lợi suất ngày sau chi phí trong cửa sổ, năm hóa ×252, lợi suất vượt trội so với lãi suất TPCP 1 năm".

8. [MAJOR] 4.3.6 và Hình 2 | Quy trình ước lượng và chọn mô hình theo thời gian chưa rõ. Hình 2 vẽ mỗi cửa sổ gồm "Ước lượng: 104 tuần | Đánh giá: 6 tháng", nhưng văn bản lại viết mô hình "tái cân bằng hằng tháng trong suốt cửa sổ". Vậy cửa sổ 104 tuần có trượt theo từng tháng không? Câu "chọn trước mô hình *c* có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước" chưa nói CE 36 tháng được tính từ chuỗi lợi suất nào, cũng chưa có quy tắc khi hai mô hình bằng điểm. | Hai người tái tạo có thể dựng hai chuỗi lợi suất ngoài mẫu khác nhau. | Cần viết rõ: "tại mỗi tháng τ, ước lượng lại trên 104 tuần kết thúc ở τ; chuỗi ngoài mẫu là lợi suất tháng nối tiếp; *c* = argmax CE trên 36 tháng trước điểm đầu cửa sổ; khi bằng điểm, chọn mô hình có số thứ tự nhỏ hơn". Hình 2 cần cập nhật cho khớp.

9. [MAJOR] 4.3.5 và Bảng 3 | Đặc tả của các mô hình còn để ngỏ: "Quan điểm của M~4~ lấy từ một mô hình dự báo đơn giản" (mô hình nào?); M5 có thể thay phương pháp ước lượng ("quyết định phương pháp ước lượng cho M~5~"); M6 chưa có tập mơ hồ (ambiguity set) hay tham số; M7 "giảm tỷ trọng rủi ro" từ danh mục cơ sở nào, sang tài sản an toàn nào? Lưới siêu tham số và "cùng một quy tắc và cùng ngân sách tinh chỉnh" chưa được mô tả. Ràng buộc chỉ mua chỉ xuất hiện ở 4.4, chưa có ở 4.3.5. Chưa có trần trọng số. Chưa nói M3 tối ưu với $\rho$ nào. Câu "báo cáo kết quả cả khi có lẫn khi không có M~5~" không nói phiên bản nào là chính. | Mỗi mô hình là một đường rẽ nhánh. Nếu chỉ M7 được nắm giữ tiền mặt thì mức hối tiếc và D_t thay đổi một cách cơ học. | Cần thêm một bảng phụ lục cho từng mô hình: đầu vào, hàm mục tiêu, ràng buộc, lưới siêu tham số, quy tắc tinh chỉnh (ví dụ CE trung bình trên 36 tháng trước). Cần ghi tập M đầy đủ (có M5) là phân tích chính.

10. [MAJOR] 4.3.8 | Câu "Đề tài tham số hóa chi phí giao dịch và kiểm tra độ nhạy theo tham số này" không cho giá trị cơ sở. Chưa nói chi phí theo thời kỳ (thuế bán, phí môi giới) được áp như thế nào, và có tính tác động giá hay không. | Biến kết quả chính được đo "sau chi phí", nên chọn mức chi phí sau khi xem dữ liệu sẽ thay đổi H3 trực tiếp. | Cần ghi giá trị cơ sở (ví dụ X bps mỗi chiều cộng thuế bán theo quy định từng thời kỳ) và lưới kiểm tra độ nhạy (ví dụ 0/2X/4X).

11. [MAJOR] 4.3.3 | Câu "30 mã có giá trị giao dịch bình quân ba tháng và vốn hóa tự do chuyển nhượng lớn nhất" chưa nói cách kết hợp hai tiêu chí (lọc rồi xếp hạng? tổng thứ hạng?). Dữ liệu free-float giai đoạn trước 2012 có thể không có. Các tình huống sau chưa có quy tắc: mã mới vào rổ không đủ 104 tuần lịch sử, mã bị tạm ngừng giao dịch, lợi suất khi hủy niêm yết, chạm biên độ giá. | Thiếu quy tắc xử lý dữ liệu thiếu. Thành phần rổ thay đổi thì mọi kết quả thay đổi theo. | Cần ghi quy tắc từng bước: lọc theo yêu cầu đủ ≥ 104 tuần dữ liệu, xếp hạng theo …, thay thế mã khi …, lợi suất ngày hủy niêm yết = …, ngày thiếu dữ liệu xử lý bằng ….

12. [MAJOR] 4.3.7, phương trình (5) | Phương pháp suy diễn có hai hướng: "sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan" và "bootstrap khối dừng (Politis và Romano, 1994) cho các hệ số hồi quy". Số độ trễ HAC và độ dài khối chưa có. Với khoảng 28 quan sát, (5) chứa $S_t$ cùng ít nhất 5 biến trong $X_t$ (Amihud, tương quan đuôi, tương quan hiệu chỉnh, phân tán chéo, biến động thực hiện). Các biến kênh chưa được định nghĩa cách tính: trung bình trên 30 mã? đo trong cùng cửa sổ hay trễ một cửa sổ? CSAD hay CSSD? | Có thể chọn phương pháp suy diễn cho ra khoảng tin cậy hẹp hơn. Mô hình gần bão hòa khiến H2 khó có công suất (xem thêm mục Structural, ý 9). | Cần chỉ định một phương pháp suy diễn chính (ví dụ bootstrap khối dừng, độ dài kỳ vọng 3 cửa sổ, B = 1.999), HAC chỉ để đối chiếu. Cần một bảng định nghĩa biến kênh (công thức, tần suất, cách gộp, độ trễ). Nên giới hạn phương trình xác nhận ở $S_t$, biến động thực hiện và hai biến của H2.

13. [MAJOR] 4.3.7, đoạn phân rã | Câu "Khi hệ số này vượt ngưỡng, đề tài báo cáo hai phương trình tách riêng" không nói đó là hai phương trình nào, và khi đó H2 được phán quyết ra sao. Ngoài ra, phép phân rã $\beta_0 - \beta_1$ "khi không có và khi có $X_t$", trong khi "Biến động thực hiện luôn có mặt trong $X_t$". Như vậy phần được gọi là "do biến kênh giải thích" bao gồm cả phần của biến động, trái với cách đặt câu hỏi 2 là "Sau khi kiểm soát biến động thực hiện". | Quy tắc dự phòng mơ hồ biến thành lối thoát cho H2. Thước đo phân rã cũng không đo đúng điều câu hỏi 2 hỏi. | Nên định nghĩa $\beta_0$ là hệ số khi chỉ có biến động thực hiện, $\beta_1$ là hệ số khi có biến động thực hiện cùng các biến kênh. Cần nêu cụ thể hai phương trình tách riêng và quy tắc phán quyết H2 trong trường hợp đó.

14. [MAJOR] 4.3.8 và Bảng 2 (H3) | Đặc tả H3 có nhiều chỗ chưa khớp. (a) "kết hợp các mô hình theo trọng số Bayes … hoặc chỉ kết hợp các mô hình nằm trong tập tin cậy": chữ "hoặc" tạo hai phiên bản. Trọng số Bayes cho các quy tắc danh mục không có hàm hợp lý, và chưa nói tính thế nào. (b) Bảng 2 chỉ nêu "kết hợp mô hình và danh mục vững chắc", còn 4.3.8 có ba cơ chế. (c) Bảng 2 viết MDD "thấp hơn", còn 4.3.8 viết "độ sụt giảm tối đa không cao hơn". (d) "so với chọn một mô hình": mô hình được chọn theo quy tắc c hay một mô hình cố định? (e) "với khoảng tin cậy bootstrap khối loại trừ 0" áp dụng cho tiêu chí nào? (f) H3 được ủng hộ khi chỉ cần một cơ chế đạt hay khi cả ba đạt? (g) "loại cơ chế (ii) và (iii) khỏi M" trong khi M6 và M7 vốn là hai mô hình trong M. | Có 2 × 3 × 3 tổ hợp, đủ để luôn tìm ra một kết quả "thắng". | Cần chốt một quy tắc kết hợp chính và nêu công thức trọng số. Cần thống nhất Bảng 2 với 4.3.8. Cần định nghĩa biến chuẩn so sánh là "mô hình c theo quy tắc 36 tháng". Mỗi cơ chế là một giả thuyết con với tiêu chí chính là CE, có hiệu chỉnh Holm trong H3. Cần định nghĩa lại rõ tập M dùng cho H3.

15. [MAJOR] Bảng 2 (H4) và 4.3.7 | Bảng 2 ghi thước đo của H4 gồm "Độ phân tán chéo của lợi suất; thước đo bầy đàn", nhưng "thước đo bầy đàn" khác với phân tán chéo chưa được định nghĩa ở đâu, ví dụ hồi quy CCK chẳng hạn. H4 không có quy tắc quyết định ("chỉ báo cáo H~4~ như kết quả thăm dò") mà vẫn được tính vào Holm "cho bốn giả thuyết". | Một giả thuyết thăm dò mà không có tiêu chí thì có thể được nâng lên thành "phát hiện" tùy theo kết quả. | Cần ghi rõ H4 là thăm dò, không có phán quyết, chỉ báo cáo hệ số và khoảng tin cậy, không đưa vào họ Holm. Bỏ "thước đo bầy đàn" hoặc định nghĩa nó.

16. [MAJOR] 4.3.7, phân phối rỗng | Câu "loại chênh lệch trung bình giữa các mô hình trong từng chế độ" đòi hỏi phải phân loại chế độ theo ngày hoặc theo cửa sổ, nhưng cách phân loại chưa được định nghĩa (xem ý 1). Độ dài khối cũng chưa có. | Phân phối rỗng, và do đó phán quyết H1, thay đổi theo cách phân loại. | Cần ghi quy tắc phân loại (ví dụ theo xác suất lọc ngày > ngưỡng) và độ dài khối.

17. [MAJOR] 4.3.3, 4.3.4 và 4.4 | Danh sách kiểm tra độ bền dài nhưng không có quy tắc diễn giải. Có những cụm mơ hồ như "các ràng buộc khác nằm trong kiểm tra độ bền" và "định nghĩa chế độ thay thế theo ngưỡng sụt giảm và theo biến động thực hiện" (chưa có ngưỡng). Biến kiểm soát vĩ mô (CPI, tỷ giá, lãi suất điều hành) chưa rõ được đưa vào phương trình nào. | Kiểm tra độ bền không có quy tắc thì có thể được chọn lọc để báo cáo. | Cần liệt kê đầy đủ, có tham số cho từng kiểm tra. Cần cam kết báo cáo tất cả và nêu rõ kết luận chính dựa trên đặc tả chính bất kể kết quả kiểm tra độ bền.

18. [MAJOR] 4.3.10 | Câu "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam" đồng nhất việc không ủng hộ H1 với việc khẳng định không có khác biệt, trong khi chính đề cương thừa nhận "các kiểm định có công suất thấp". | Việc diễn giải kết quả âm tính bị thổi phồng. | Cần một ngưỡng hiệu ứng tối thiểu có ý nghĩa (SESOI) và kiểm định tương đương (TOST), hoặc chỉ được nói "không đủ bằng chứng". Cần định nghĩa "1/N đủ dùng" bằng tiêu chí đo được.

19. [MAJOR] 4.3.6 | Tập tin cậy mô hình được ghi là "ở mức ý nghĩa 10% ấn định trước", nhưng hàm tổn thất, thống kê ($T_R$ hay $T_{max}$) và độ dài khối bootstrap chưa có. Việc "kèm số quan sát và công suất kiểm định" cũng chưa nói công suất tính thế nào. | Kích thước tập tin cậy phụ thuộc vào các lựa chọn này. | Cần ghi cụ thể các tham số MCS và phương pháp tính công suất (ví dụ mô phỏng với hiệu ứng = …).

20. [MAJOR] 4.1 và 4.3.10 | Các giai đoạn tham chiếu ("khủng hoảng tài chính toàn cầu, đại dịch COVID-19 năm 2020 và căng thẳng trái phiếu doanh nghiệp từ quý IV/2022") chưa có mốc ngày cụ thể. "báo cáo kích thước hiệu ứng cùng khoảng tin cậy theo từng giai đoạn" chưa định nghĩa giai đoạn. Chưa có tiêu chí cho việc chế độ ước lượng "trùng với biến cố thực tế", và không có quy tắc xử lý nếu không trùng. | Phân tích dị biệt theo giai đoạn đã được hứa nhưng chưa được vận hành hóa. | Cần ghi ngày bắt đầu và kết thúc của từng giai đoạn tham chiếu, cùng tiêu chí trùng khớp (ví dụ ≥ 50% số ngày có xác suất lọc > ngưỡng) và hệ quả khi không đạt.

21. [MAJOR] 4.3.5 và 4.4 | Hai câu "Dữ liệu phát sinh sau ngày đăng ký là mẫu kiểm tra riêng" và "dữ liệu phát sinh sau ngày đăng ký trước là mẫu kiểm tra riêng" mâu thuẫn với phạm vi "từ 2007 đến 2026": đăng ký diễn ra ở Quý 4 năm thứ nhất, tức sau năm 2026. Chưa nói mẫu kiểm tra dùng cho kiểm định nào, có quy tắc quyết định gì, cỡ bao nhiêu cửa sổ, và được phân tích vào thời điểm nào. | Một mẫu kiểm tra không có quy tắc thì chỉ mang tính trang trí, hoặc bị dùng một cách chọn lọc. | Cần ghi ngày cắt dữ liệu của mẫu chính và ngày kết thúc mẫu kiểm tra. Cần nói rõ đó là kiểm tra mô tả (vì chỉ có 2–4 cửa sổ). Cần đưa việc phân tích mẫu kiểm tra vào Bảng 5.

### Minor Writing Issues

1. [MINOR] Trang bìa so với mục 10 | Trang bìa ghi "Người hướng dẫn khoa học (dự kiến): PGS.TS. Hà Hồng Hạnh", còn mục 10 ghi người hướng dẫn chính là "GS.TS. Nguyễn Đức Khương" và PGS.TS. Hà Hồng Hạnh là người thứ hai. | Cần thống nhất trang bìa với mục 10.
2. [MINOR] Trang bìa và mục 3 | "Cơ quan công tác:" và "Đơn vị công tác:" đang để trống. | Cần điền vào, hoặc ghi "Không".
3. [MINOR] Trang bìa | "Đại học Kinh tế Quốc Dân" không khớp với "Trường Đại học Kinh tế Quốc dân" ở mục 10. | Sửa thành "Trường Đại học Kinh tế Quốc dân".
4. [MINOR] 4.3.6 | "mức hối tiếc chỉ tính được từ khoảng năm thứ năm của mẫu": 104 tuần (2 năm) cộng 36 tháng (3 năm) nghĩa là bắt đầu từ năm thứ sáu. | Sửa thành "từ đầu năm thứ sáu (khoảng năm 2012)".
5. [MINOR] 4.3.6 và 4.3.10 | "khoảng 28 cửa sổ đánh giá độc lập" và "số cửa sổ độc lập": các cửa sổ không chồng lấn, nhưng việc chọn mô hình dùng 36 tháng chồng lấn và lợi suất có tự tương quan, nên chúng không độc lập. | Dùng "cửa sổ không chồng lấn".
6. [MINOR] 4.1, mục tiêu (iii) | Câu "các biến kênh … gồm biến động, thanh khoản, tương quan cực trị và bầy đàn" mâu thuẫn với câu hỏi 2 và H2, nơi biến động thực hiện là biến kiểm soát. | Bỏ "biến động" khỏi danh sách biến kênh.
7. [MINOR] 4.1, Bảng 2, Hình 1 và 4.3.6 | 4.1 viết "Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro", nhưng Bảng 2 xếp chúng là "Kết quả phụ" của rủi ro lựa chọn mô hình, Hình 1 đặt "Độ phân tán D_t" và "Tập tin cậy mô hình" trong ô "Rủi ro lựa chọn mô hình", còn 4.3.6 gọi kích thước tập là "thước đo mô tả". | Cần thống nhất vai trò (ví dụ "chỉ báo bất định, kết quả phụ") ở cả bốn chỗ, và chỉnh lại Hình 1.
8. [MINOR] 4.3.6 và 4.3.8 | Ký hiệu *M* bị dùng lại với nhiều nghĩa: "Gọi *M* là tập bảy mô hình", rồi tập tĩnh 5 mô hình, rồi "loại cơ chế (ii) và (iii) khỏi *M*". Số hạng \|M\| − 1 trong (3) thay đổi theo. | Đặt ký hiệu riêng: $M$, $M^{static}$, $M^{H3}$.
9. [MINOR] Nhiều chỗ | Một số từ viết tắt hoặc tên riêng chưa được giải thích ở lần dùng đầu: "OSF Registries", "VN30", "VN100", "ABC-MCMC" (Bảng 6), "VSTEP", "SR 11-7". | Thêm chú giải ở lần xuất hiện đầu tiên.
10. [MINOR] 4.3.3 | Câu "Kiểm tra độ bền dùng dữ liệu tháng, tái cân bằng hằng quý, và bổ sung chỉ số giá tiêu dùng … làm biến kiểm soát" gộp ba kiểm tra khác nhau vào một câu, nên không rõ biến vĩ mô chỉ dùng trong kiểm tra dữ liệu tháng hay dùng riêng. | Tách thành danh sách đánh số.
11. [MINOR] Bảng 2, ô H2 | Câu dài với hai lớp ngoặc đơn chứa cơ chế giải thích, khó đọc. | Tách thành: giả thuyết (dấu), rồi cơ chế ở dòng chú thích.
12. [MINOR] Bảng 2 và Hình 1 | Thuật ngữ chưa thống nhất: "giá trị thiệt hại kỳ vọng mức 95%" và "Thiệt hại kỳ vọng"; "tương quan cực trị", "tương quan đuôi" và "tương quan đuôi âm". | Chọn một thuật ngữ cho mỗi khái niệm và dùng nhất quán.
13. [MINOR] Mục 8 và mục 11 | Khóa trích dẫn không nhất quán: "Nguyễn và Nguyễn, 2026b" (có dấu) và "Nguyen và Nguyen, 2026a" (không dấu). | Thống nhất một quy ước.
14. [MINOR] 4.3.6 và 4.3.7 | 4.3.6 viết "chỉ báo cáo tỷ số Sharpe … ở các cửa sổ có lợi suất vượt trội trung bình dương", nhưng 4.3.7 viết "so sánh lợi suất tương đương chắc chắn và tỷ số Sharpe giữa các mô hình". Việc báo cáo có điều kiện như vậy là một dạng chọn mẫu. "Lợi suất vượt trội" cũng chưa nói so với lãi suất nào. | Ghi rõ "vượt trội so với TPCP 1 năm" và quy tắc báo cáo Sharpe.
15. [MINOR] Bảng 2 và 4.3.8 | "giá trị thiệt hại kỳ vọng mức 95% (tổn thất trung bình trong 5% số ngày xấu nhất)": một cửa sổ 6 tháng có khoảng 125 ngày, nên đuôi 5% chỉ còn khoảng 6 quan sát. | Ghi rõ ES được tính trên toàn bộ các ngày của chế độ, không tính theo từng cửa sổ.
16. [MINOR] Hình 3 | Tệp hinh-van-ban.txt không có văn bản trích từ Hình 3 (khung #1 và #6 trống), nên không thể đối chiếu với "năm bước" ở 4.3.9. | Kiểm tra lại hình gốc.

### Structural or Compliance Signals to Fix

1. [CRITICAL] Thiếu một bảng kế hoạch phân tích gắn với từng giả thuyết | Nên đặt ở 4.3.7, ngay sau Bảng 2 | Với mỗi giả thuyết từ H1 đến H4, bảng cần có: biến kết quả chính (công thức), biến giải thích, biến kiểm soát, mẫu (cửa sổ nào), phương pháp suy diễn (bootstrap, độ dài khối, B), phía kiểm định, α sau Holm, quy tắc ủng hộ, bác bỏ hoặc không kết luận. Hiện các thông tin này rải ở Bảng 2, 4.3.6, 4.3.7, 4.3.8 và 4.3.10, và có mâu thuẫn (xem các ý 2, 3, 14).
2. [CRITICAL] Hiệu chỉnh kiểm định bội đã được nêu nhưng chưa vận hành được | Nên đặt ở 4.3.10 | Cần định nghĩa họ kiểm định, giá trị p của các quy tắc nhiều điều kiện, và tách các phân tích thăm dò ra ngoài (xem ý 3).
3. [MAJOR] Chưa có quy tắc cho dữ liệu thiếu (hao hụt mẫu và không tuân thủ không áp dụng vì không có đối tượng nghiên cứu) | Nên đặt ở 4.3.3 | Cần quy tắc cho: mã tạm ngừng hoặc hủy niêm yết, mã thiếu lịch sử 104 tuần, ngày nghỉ hoặc ngày thiếu giá, dữ liệu free-float hoặc lợi suất TPCP bị thiếu ở giai đoạn đầu mẫu.
4. [MAJOR] Chính sách lệch khỏi kế hoạch còn mơ hồ: "thí sinh ghi mọi thay đổi sau đó là lệch khỏi kế hoạch"; "thu hẹp rổ cổ phiếu hoặc giai đoạn mẫu nếu dữ liệu không đủ" mà không có tiêu chí "không đủ" | Nên đặt ở 4.3.5 và 4.3.10 | Cần cam kết: (a) có bảng lệch kế hoạch ghi lý do và thời điểm; (b) luôn báo cáo song song kết quả theo kế hoạch gốc; (c) có tiêu chí định lượng cho "dữ liệu không đủ" (ví dụ < N mã có đủ dữ liệu ở năm 2007).
5. [MAJOR] Đề cương hoãn các tham số then chốt sang tệp OSF sau này: "Tệp đăng ký cố định độ dài các cửa sổ, siêu tham số của bảy mô hình, số chế độ và ngưỡng xác suất lọc, mức ý nghĩa…" | Nên đặt ở 4.3.5 | Cần nêu ngay các giá trị tạm thời (ngưỡng xác suất, lưới siêu tham số, chi phí giao dịch) và nói rõ tham số nào được phép thay đổi trước khi đăng ký, theo tiêu chí nào.
6. [MAJOR] Trình tự trong Bảng 5 bất hợp lý: "Quý 2: ước lượng thử bảy mô hình" diễn ra trước "Quý 3: làm sạch dữ liệu" và trước "Quý 4: đăng ký trước". Ngày đăng ký tuyệt đối chưa có, và việc phân tích mẫu kiểm tra không có trong kế hoạch | Nên đặt ở 7.4 | Cần đảo thứ tự làm sạch và chạy thử, ghi rõ năm dương lịch của "năm thứ nhất", và thêm mốc phân tích mẫu kiểm tra vào năm 3 hoặc năm 4.
7. [MAJOR] Phân tích dị biệt (theo giai đoạn, theo tập mô hình tĩnh, có hoặc không có M5) đã được hứa nhưng chưa có thứ bậc | Nên đặt ở 4.3.7 | Cần ghi rõ đặc tả nào là chính, đặc tả nào là phụ, và cách xử lý khi kết quả chính và phụ mâu thuẫn.
8. [MAJOR] Chưa có tính toán công suất hay hiệu ứng nhỏ nhất phát hiện được (MDE), dù đề cương thừa nhận "các kiểm định có công suất thấp" | Nên đặt ở 4.3.10 | Cần mô phỏng công suất trước khi đăng ký, với khoảng 28 cửa sổ và số cửa sổ căng thẳng dự kiến. Cần nêu MDE cho β của H1 và các hệ số của H2.
9. [MAJOR] Hứa quá khả năng thực hiện | Nên đặt ở 4.3.6, 4.3.7 và 7.3 | Với khoảng 28 cửa sổ, trong đó có lẽ chỉ vài cửa sổ căng thẳng sau năm 2012 ("khủng hoảng tài chính toàn cầu chủ yếu phục vụ ước lượng chế độ"), ngưỡng "dưới 10" khiến H1 đến H3 có xác suất cao rơi vào "không kết luận". Phương trình (5) với 6–7 tham số trên khoảng 28 quan sát gần bão hòa. Ba bài báo cho ba nhóm giả thuyết dựa trên cùng một mẫu nhỏ là khá tham vọng. Cần nêu thẳng điều này và cân nhắc dùng cửa sổ 3 tháng hoặc cửa sổ trượt có hiệu chỉnh chồng lấn làm phân tích chính, sau khi tính công suất.
10. [MINOR] Các mục không áp dụng | Mục 4.3.3 | Ngẫu nhiên hóa, kiểm tra cân bằng, hao hụt mẫu, tuân thủ, thiết kế bảng hỏi và phê duyệt đạo đức với người tham gia đều không áp dụng, vì đây là nghiên cứu quan sát trên dữ liệu thị trường công khai và đề cương đã ghi "Dữ liệu không chứa thông tin cá nhân". Nên ghi một câu nói rõ các mục này không áp dụng, và thêm điều khoản giấy phép dữ liệu thương mại liên quan đến việc chia sẻ dữ liệu tái tạo.
11. [MINOR] Khả năng tái tạo | Nên đặt ở 4.3.10 | Câu "thí sinh lưu mã nguồn và tệp đăng ký trước" chưa nói lưu ở đâu. Cần nêu kho lưu trữ (OSF hoặc GitHub), seed ngẫu nhiên cho bootstrap, phiên bản phần mềm, và việc dữ liệu thương mại có được chia sẻ hay chỉ chia sẻ mã.

---
