# Nhật ký thay đổi vòng 10–11

Bản: `outputs/round-11/de-cuong-v11-round-11.docx`. Validate PASSED; 7 công thức OMML; 8 bảng; không tracked changes; 10 nhãn [CẦN …].

## Bằng chứng tuân thủ
- **Vòng 10, bản v10 (trước phản biện):** mhe-identification (Drafter) để viết phần mở rộng H₃ theo kênh và theo trụ sở Hà Nội; anthropic-skills:docx để sửa XML.
- **Phản biện vòng 10, 2 agent:**
  - Agent A gọi tuần tự 10 skill: academic-paper-reviewer (5 vai trong một ngữ cảnh, vì thiếu contract và không có công cụ Agent), mhe-identification (Critic), aer-identification, review-methodology, liquidity-measures, statistical-power (có mô phỏng), scientific-critical-thinking, review-pap (áp checklist trong một ngữ cảnh), econ-write, sciwrite. Kết quả: 0 CR, 5 MJ, 7 m (`reports/r10-review-A.md`).
  - Agent B gọi tuần tự 7 skill: vn-legal-verify, fact-checker, credible-claims, consistency-checker, citation-management (chỉ đọc), research-grants, peer-review. Kết quả: 0 CR, 3 MJ, 17 m (`reports/r10-review-B.md`).
- **Luồng chính:** proposal-revise (gộp hai báo cáo), anthropic-skills:docx (sửa, validate). 59 thao tác.

## Đã sửa
| Mã | Nội dung |
|---|---|
| A-MJ1 | Quy tắc loại ngày liền sau đổi thành "ngày có lợi suất tuyệt đối từ 7% trở lên", áp chung cho mọi mã và mọi giai đoạn, để tập ngày bị loại không đổi theo sàn |
| A-MJ2 | Viết rõ số hạng Dᵢ·Postₜ·Eₛ,ᵢ và hiệu ứng theo tháng riêng cho từng mức chịu cú sốc, ước lượng trên mã đối chứng đo được cùng thước đo; giả định nhận dạng viết lại; báo cáo mã rơi khỏi mẫu |
| A-MJ3 | Suy luận cho hệ số tương tác dùng cùng thủ tục với δ (bootstrap tự hồi quy trên chuỗi hệ số theo tháng), vì phân cụm theo cổ phiếu và hoán vị giữa các mã bác bỏ quá thường xuyên; ghi MDE từng hệ số vào tệp đăng ký |
| A-MJ4 + B-MJ1 | Bỏ kênh FTSE: danh sách đủ điều kiện (dữ liệu đến 30/6/2026) chỉ gồm mã HOSE, nên không có biến thiên. Thay bằng mức chịu cú sốc chỉ số = vốn hóa tự do chuyển nhượng / giá trị giao dịch; FTSE chỉ dùng để làm sạch nhóm đối chứng |
| A-MJ5 + B-MJ3 | Phân tích theo trụ sở Hà Nội: bỏ "Hà Nội mất gì"; nêu kênh là sự chú ý và thông tin gắn với sàn; ba cách đọc kết quả (khác 0 / hẹp quanh 0 / chưa đủ cơ sở); ghi số mã và MDE vào tệp đăng ký; là phân tích phụ, không vào Holm |
| B-MJ2 | Amihud và cộng sự (1997) ghi nhận lan tỏa **dương**, nên chuyển sang câu về trường hợp δ bị đánh giá thấp |
| MINOR | Mục tiêu và Bảng 4 dùng "khác biệt theo mức chịu cú sốc" thay "tác động theo từng kênh"; ghi chú Bảng 2; thước đo bước giá; mô tả đúng ràng buộc của Rambachan–Roth; Coval & Moskowitz nói về nhà quản lý quỹ; giá trị p một phía trong Holm; Điều 4 TT 120 nêu đúng VNX và quyền điều chỉnh của UBCKNN; nới biên độ không tác động "như nhau"; thêm việc rút ngắn chu kỳ thanh toán; UPCoM sang HOSE là khả năng chính; GFCI Bảng 26 có cả nhân tố mức chỉ số; phương án dự phòng GFCI gồm cả "không được phép dùng"; ngày ký đổi thành "… tháng 10 năm 2026" (anh điền); APA 7 cho hai bài báo; thêm 4 DOI có trong hồ sơ; URL và tháng phát hành của GFCI 40 và FTSE; nhãn Daw & Hatfield thu hẹp; OSF có nghĩa tiếng Việt |
| Độ khớp NQ 57 | Chỉ tiêu (6) kèm văn bản xác nhận của ít nhất một đơn vị, ưu tiên HNX; mục 9 thêm cam kết thực hiện nghĩa vụ tại điểm e khoản 2 Điều 15 NQ 57 |
| Trình bày | Tách thêm 14 đoạn dài; mọi chỉ số dưới viết bằng định dạng Word |

## Không áp dụng
- B-m6, thêm "sàn khu vực ở Hoa Kỳ … nhờ lợi thế quy mô" cho Arnold và cộng sự (1999): Hisada (2018) chỉ viết "exchange mergers increase liquidity"; "lợi thế quy mô" là giả định của chính Hisada.
- B-m12, gắn nhãn [CẦN BỔ SUNG ngày đăng] cho hai bài báo: giữ năm, đưa ngày đăng vào danh sách tài liệu cần tìm.

## Lỗi tự phát hiện và đã sửa
Ở bản v10 (chưa gửi anh), công cụ tạo đoạn mới đã chép nhầm định dạng chỉ số dưới vào 7 run chứa cả câu. Lỗi đã sửa ở v11 và đã vá công cụ. Bản v9 đã gửi anh không bị lỗi này.
