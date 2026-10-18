# Sổ tay kiểm tra slide bảo vệ đề cương (từ vòng 3)

Mỗi dòng là câu hỏi có/không; "không" là phát hiện. Xung đột: CLAUDE.md > template > v14, Shapiro > skill. Mức xem mục I.

## A. Quy tắc người dùng [CLAUDE.md]

- Mọi số, trích dẫn, DOI có trong v14; số minh họa ghi "minh họa".
- Không có δ = −0,25, Ḡ = 4,66, MQI = 0,3 như kết quả.
- Tên đề tài giữ nguyên; nội dung khớp v14.
- APA 7: "&" trong ngoặc, "và" ngoài ngoặc.
- H₁–H₄, M₁–M₇, K₁–K₄ có chỉ số dưới.
- Công thức: chỉ số dưới không dấu phẩy ($y_{it}$), không dấu nhân, tham số Hy Lạp, tên biến nhiều chữ viết đứng ($\mathrm{ILLIQ}_{im}$).
- Bảng mặc định, không nền xám; bảng viết tắt 3 cột.
- XeLaTeX; sty chỉ sửa tối thiểu, có [VN].
- Khoảng 30 phút; không \note.
- Tiêu đề nêu kết luận, 1 dòng.
- Có định tính (cơ chế, trực giác, hàm ý) có nguồn v14.
- Hình chỉ khi cần, kiểu figures.pdf: Dark2 #7570b3, #d95f02, #e7298a, nhãn trên đường, không chú giải.
- Agent không sửa repo, không render, không chạy script, không gọi mạng; chỉ rà slide đổi kèm đoạn v14; dùng kiểm máy của main.

## B. Hình thức

Template [template]:
- 11pt, dvipsnames; Boadilla + seagull; không nút điều hướng; lề 5mm; onehalfspacing; microtype.
- Phông Source Sans Pro, Source Code Pro, MnSymbol, mathastext (Hy Lạp Euler); bản XeLaTeX tương đương ghi [VN].
- Trang đầu: tiêu đề \huge, small caps, chữ thường, kẻ 1,5pt; author, date \large.
- Frametitle small caps, chữ thường, BlackGray.
- Màu BlackGray, DarkGray, LightGray; nhấn \al (RubineRed).
- Đầu dòng •, –, □ màu DarkGray; đánh số 1., a., i.
- figure/table + \caption \footnotesize DarkGray căn giữa; bảng `tabular*{\textwidth}` + booktabs, không kẻ dọc.
- Khung định lý nền LightGray, góc tròn, không bóng.
- Slide mục \heading; \lastslide kết thúc phần chính; backup sau đó, có nút quay về.
- Không số trang; ký hiệu \so, \then, \up, \down.

Quy tắc cứng [beamer], chỉnh theo template:
- Không \pause, \only, \onslide, \uncover; overlay chỉ kiểu \al[n], \includegraphics<n>.
- ≤ 7 ý/slide (tốt nhất 3–4 [slide-design-principles]); ý ≤ 2 dòng (~15 chữ); văn điện tín.
- ≤ 2 phương trình hiển thị, ≤ 5 ký hiệu mới, ≤ 2 khung/slide.
- Trong khung: một phương trình hoặc 2–3 ý; không \qquad, \vspace âm.
- Mỗi slide có yếu tố thực chất; slide toàn chữ ≤ 30%.
- Không \tiny; \footnotesize chỉ caption; nhãn hình ≥ \footnotesize.
- ≤ 3 \vspace/slide; \resizebox, [shrink] là cách cuối; allowframebreaks chỉ cho tài liệu.
- Bảng ≤ 7 cột, ≤ 10 dòng, số căn phải.
- TikZ: không chồng nhãn; điểm trên đường tính bằng \pgfmathsetmacro; rộng ≤ 14cm; liền = quan sát, đứt = phản thực.
- Ký hiệu nhất quán, định nghĩa trước khi dùng; không sót placeholder.
- Tràn trong khung không sinh cảnh báo: dựa vào bbox.

Ký hiệu [latex-econ-model][econ-write]: chữ trong công thức dùng \text; không `*`; \left( \right); không $$; Latin cho biến, Hy Lạp cho tham số, có tên gọi.

Thiết kế [slide-design-principles]: một ý mỗi slide; không cặp đỏ/xanh lá; ≤ 5 màu; không trích dẫn ngoài v14.

## C. Cấu trúc 30 phút

- 15–20 slide chính, 3–5 backup [beamer][beamer-presentation].
- Động cơ 1–2 slide bằng dữ kiện, câu hỏi chính sách [Shapiro].
- Câu hỏi kinh tế, không "áp mô hình X cho Y" [Shapiro].
- Nêu đóng góp và vì sao có thêm thông tin [Shapiro].
- Xem trước kết quả trong 10 phút đầu [Shapiro][econ-write].
- Dữ liệu: nguồn và cấp đo từng biến; không kể bước làm sạch [Shapiro].
- Mô hình: phương trình, định nghĩa ký hiệu, giả định nhận dạng E(ε|·) = 0, đại lượng kết luận [Shapiro].
- Nêu 1–2 điểm yếu chính và cách kiểm [Shapiro].
- Hình hơn bảng; bảng chỉ cho độ lớn chính; kiểm tra độ vững gom thành ý [Shapiro].
- Có một kết luận cuối, không chỉ mô tả việc làm [Shapiro].
- 40–50% thời gian cho phần lõi; ≤ 4 slide hình thức liền nhau [beamer].
- Động cơ trước định nghĩa; ví dụ trong 2 slide [beamer].
- Kết bằng điều cần nhớ, không "Câu hỏi?" [beamer-presentation].

## D. Nhận dạng và suy luận

- Một câu nêu biến động ngoại sinh, nhóm xử lý, nhóm so sánh, ước lượng đích ATT [mhe-identification][review-methodology].
- 2×2/TWFE chỉ khi cùng một ngày, đối chứng không bao giờ bị xử lý, hiệu ứng đồng nhất; ngày lệch thì CS/SA/BJS và Goodman-Bacon [aer-identification].
- Sự kiện chạm mọi đơn vị cùng lúc thì hiệu ứng thời gian hấp thụ; cần nhóm so sánh [panel-data-guide].
- Xu hướng song song: ≥ 3–4 kỳ trước, kỳ gốc t = −1, kiểm định đồng thời có p; hình phẳng không chứng minh; độ nhạy Rambachan–Roth [aer-identification][econ-write].
- Nêu kỳ vọng trước sự kiện khi mốc pháp lý công bố sớm hoặc bị lùi; nêu đổi thành phần mẫu [econ-write][vn-legal-verify].
- Có kiểm định giả (ngày giả, biến kết quả giả) [aer-identification].
- Không biến kiểm soát sau xử lý [mhe-identification].
- Phân cụm theo cấp gán xử lý; một ngày sự kiện là cú sốc chung, cụm theo mã phóng đại độ chính xác [mhe-identification].
- Ít cụm (< 40–50): wild bootstrap hoặc hoán vị; 1–2 cụm xử lý: suy luận ngẫu nhiên [aer-identification][econ-write].
- Bootstrap tự hồi quy: nói lấy mẫu lại gì, bậc, số lần lặp, vì sao hợp phụ thuộc chuỗi; không nói quá [credible-claims].
- Holm: họ giả thuyết định trước, α cả họ, giả thuyết nào còn ý nghĩa [statistical-analysis][econ-write].
- MDE: tính trước, α hai phía 0,05, lực 0,80, đơn vị có nghĩa, có dải nhạy, tính phụ thuộc cụm; không "lực quan sát" [statistical-power].
- Kết quả không ý nghĩa: phân biệt "bằng 0 chính xác" với "không chính xác" [econ-write].
- Độ lớn kèm khoảng tin cậy; ý nghĩa thống kê khác tầm quan trọng [statistical-analysis][mostly-harmless-guide].
- Liên hệ có điều kiện viết "đi kèm", "gắn với", không "làm tăng", "gây ra" [review-methodology][credible-claims].
- Cơ chế là kiểm kênh cụ thể; dị biệt sau kết quả chính, định trước [econ-write].
- Không dùng "vững" như lời khen [mhe-identification].

## E. Thanh khoản [liquidity-measures]

- Chỉ báo đúng chiều: chi phí (Roll, Corwin–Schultz, Abdi–Ranaldo, ngày lợi suất 0), tác động giá (Amihud), hoạt động (vòng quay).
- Định nghĩa đủ đơn vị; nêu xử lý giá trị âm, DVOL = 0, ngày không giao dịch; mẫu số vòng quay nhất quán.
- Chỉ số tổng hợp nêu trọng số, không do một thành phần chi phối.
- Loại ngày chạm trần/sàn và ngày liền sau, có tỷ lệ và độ nhạy ngưỡng.
- Biên độ đổi cùng sự kiện thì gọi là tác động gộp.
- Bước giá lớn so với giá: kiểm theo nhóm giá.
- Nói rõ giá đóng cửa định kỳ, giao dịch thỏa thuận, mẫu cân bằng.
- Viện dẫn kiểm chứng (Goyenko, Holden & Trzcinka, 2009; Fong, Holden & Trzcinka, 2017) đúng tiêu chí.

## F. Đăng ký trước [review-pap]

- Có kết quả chính; mỗi giả thuyết một biến kết quả.
- Phương trình, hiệu ứng cố định, phân cụm, quy tắc chọn ước lượng định sẵn.
- Họ kiểm định, dữ liệu thiếu, hủy niêm yết, chỉ số tổng hợp định trước dữ liệu.
- Phân tích khám phá có nhãn; có chính sách sai lệch; không "nếu phù hợp".
- Không hứa lực vượt cỡ mẫu; không nói đã đăng ký nếu chưa.

## G. Chính xác, nhất quán, pháp lý, trích dẫn

- Số trên slide truy được về v14, làm tròn giống v14 [consistency-checker].
- Thuật ngữ, viết tắt, giai đoạn mẫu, N, phương trình giống nhau mọi slide; viết tắt giải lần đầu [consistency-checker][sciwrite].
- \hyperlink trỏ tới nhãn có thật [consistency-checker].
- Pháp lý: số hiệu, ngày ký khác ngày hiệu lực, điều khoản đúng; mốc của văn bản sửa đổi không gán văn bản gốc; VBHN thiếu sửa đổi sau; không mở phạm vi (niêm yết, UPCoM, chuyển sàn); gắn KHỚP/LỆCH/CHƯA CÓ NGUỒN [vn-legal-verify].
- Tác giả-năm có trong danh mục v14, đúng chính tả; không trích qua nguồn thứ cấp [citation-management][sciwrite].
- Không chọn lọc số, trục sai, bỏ điều kiện [fact-checker].
- Lời không vượt bằng chứng: minh họa khác kiểm chứng, giả định khác suy ra [credible-claims].
- Không suy từ cấp sàn xuống cấp mã; không ngoại suy ngoài mẫu [scientific-critical-thinking].

## H. Văn tiếng Việt [vina-me][vietnamese-human-writing][sciwrite]

- Không gạch dài; gạch vừa chỉ cho khoảng số, tên ghép.
- Không mũi tên, `~`, `=`, emoji trong câu; \so, \then chỉ làm đầu dòng.
- Thập phân dấu phẩy; không in hoa toàn chữ.
- Không sáo ngữ ("đóng vai trò then chốt", "mang ý nghĩa sâu sắc", "bức tranh toàn cảnh", "nền tảng vững chắc").
- Không tính từ thay bằng chứng ("đặc biệt", "mạnh mẽ", "đột phá").
- Không từ nối tự động ("bên cạnh đó", "hơn nữa", "do đó", "tóm lại").
- Không "không chỉ… mà còn", "không phải X mà là Y", bộ ba ép, câu hỏi tu từ.
- Động từ trực tiếp, bỏ "tiến hành", "thực hiện việc", "thông qua việc".
- Một khái niệm một tên.
- Câu có chủ ngữ; Hán Việt, chính tả đúng; giọng trang trọng, không "chúng ta".

## I. Thang điểm và mức

Bắt đầu 100, trừ [beamer]: biên dịch lỗi −100; tràn phương trình −20; TikZ tràn −15; chưa định nghĩa −15; Overfull > 10pt −10; tràn trong khung −10; điểm TikZ lệch −8; slide thưa −5; nhãn chồng −5; bảng không căn giữa −3; ký hiệu không nhất quán −3; \vspace > 3 −1; giảm cỡ chữ −1. Bổ sung [CLAUDE.md]: tiêu đề 2 dòng −5; vi phạm A −10. Đạt khi ≥ 90 và hết CRITICAL, MAJOR.

- CRITICAL: sai sự thật, lệch v14, số minh họa thành kết quả, bịa nguồn, pháp lý LỆCH, lời nhân quả vượt thiết kế, lỗi biên dịch, tràn.
- MAJOR: thiếu giả định, suy luận (D–F); mâu thuẫn giữa slide; tiêu đề 2 dòng hoặc không nêu kết luận; lệch template; vượt mật độ; sai quy tắc A.
- MINOR: chính tả, dấu, từ ngữ, căn chỉnh nhỏ.

## J. Mẫu báo cáo (≤ 150 dòng)

```
# Vòng N, agent X: NN/100
## CRITICAL
C1. [slide, tiêu đề] lý do [quy tắc; v14 mục]
CŨ: <nguyên văn slides.tex>
MỚI: <chỉ văn bản thay thế>
## MAJOR
M1. (như trên)
## MINOR
- [slide] lỗi -> sửa
## Chưa kiểm được
```

Đã đọc đủ: CLAUDE.md, Shapiro, template (tex, sty, README), SKILL.md và references của beamer, beamer-presentation, slide-design-principles; SKILL.md của beamer-check, latex-econ-model, aer-identification, review-methodology, liquidity-measures, vn-legal-verify, credible-claims, consistency-checker, vina-me, vietnamese-human-writing. Đọc lướt: các skill còn lại, phần DiD, phân cụm, trình bày, lỗi văn trong references; bỏ scripts, cài đặt, tra mạng, Bayes.
