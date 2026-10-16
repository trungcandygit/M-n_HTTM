# Nhật ký thay đổi vòng 12

Bản: `outputs/round-12/de-cuong-v12-round-12.docx` (sửa từ v11). Validate PASSED; 7 công thức OMML; 8 bảng; không tracked changes.

## Bằng chứng tuân thủ (2 agent)
- **Agent A** (`reports/r12-review-A.md`), 12 skill tuần tự: academic-paper-reviewer (re-review trong một ngữ cảnh; thiếu contract re_review và công cụ Agent, đã ghi lỗi nguyên văn), mhe-identification (Critic), aer-identification, review-methodology, liquidity-measures, statistical-power (tự tính MDE; khớp đề cương 0,643σ / 1,239σ / 1,760σ), review-pap (checklist trong một ngữ cảnh), scientific-writing, econ-write, **vina-me** (có chạy soat.mjs, bỏ qua "–" và "&" theo miễn trừ APA 7), **vietnamese-human-writing**, sciwrite. Kết quả: 0 CR, 2 MJ, 13 m, 34 sửa văn phong, bảng 16 thuật ngữ.
- **Agent B** (`reports/r12-review-B.md`), 7 skill tuần tự: vn-legal-verify, fact-checker, credible-claims, consistency-checker, citation-management (chỉ đọc), research-grants, peer-review. Kết quả: 0 CR, 1 MJ, 9 m.
- **Luồng chính:** proposal-revise (gộp), anthropic-skills:docx. Áp 79/80 thao tác; 1 thao tác của B trùng với sửa của A ở cùng tiêu đề 6.1.1.

## Đã sửa
| Mã | Nội dung |
|---|---|
| A-MJ1 | Quy tắc loại ngày liền sau dùng chính ngưỡng chung (dưới ±7%), không dùng mốc "từ 7%" trùng biên độ HOSE; tập ngày bị loại không còn đổi theo sàn dù giá trần làm tròn theo cách nào |
| A-MJ2 + B-MJ1 | Kênh biên độ khi UPCoM rời HNX (khả năng chính): đo mức chịu cú sốc biên độ của mọi mã bằng tỷ lệ ngày có lợi suất tuyệt đối từ ngưỡng chung trở lên, ước lượng trên mã HOSE đối chứng, ghi rõ là thước đo đại diện. Chọn cách của A vì cách của B dựa vào giả định UPCoM giữ biên độ riêng tại HOSE, chưa có văn bản xác nhận. Lấy thêm từ B: câu về cửa sổ 24 tháng khi hạn bị lùi, và cận UPCoM chỉ dùng khi còn dữ liệu |
| A-minor | Hiệu ứng theo tháng riêng cho mã có trụ sở Hà Nội; bỏ ví dụ HNX-Index; thước đo kênh chỉ số theo vốn hóa toàn phần (VN-Index không điều chỉnh tự do chuyển nhượng); trừ trung bình khi chuẩn hóa mức chịu cú sốc; định nghĩa chuỗi hệ số tương tác theo tháng, mức ý nghĩa hai phía; thêm tương tác với thanh khoản ban đầu; gọi tên hai chỉ báo nhạy với biên độ; "cắt đuôi" thành winsorize; bỏ "tách tác động của biên độ"; tiêu đề 6.1.1; mốc "dữ liệu đến ngày 30/6/2025"; σ là độ lệch chuẩn không điều kiện |
| B-minor | Điều 15.2.e NQ 57 viết đủ và dùng "cam kết"; chỉ tiêu công bố ghi "do thí sinh là tác giả chính" (Điều 12.3); mã chuyển sàn có thể vào FTSE ở kỳ sau, ghi ngày và ước lượng lại; "danh sách cổ phiếu đủ điều kiện" thống nhất; URL FTSE FAQ; nhãn thứ tự tác giả Eichengreen–Shah; nối văn bản xác nhận với chỉ tiêu (6) |
| Văn phong (34) | Sửa câu hiểu hai cách ("bác bỏ giả thuyết không thường xuyên hơn" thành "bác bỏ giả thuyết gốc với tần suất cao hơn"); tách các câu quá tải ở mục 4.3.7; làm rõ chủ ngữ; "công suất" thành "lực kiểm định"; định nghĩa αᵢ, τₜ ngay sau phương trình (5); tách đoạn ở idx 330 và các đoạn khác |
| Thuật ngữ | "kiểm tra độ bền" thành "kiểm tra độ vững" (4 chỗ); "biến chỉ" thành "biến giả" (4 chỗ). Giữ "Black-Litterman" có gạch nối vì đó là cách viết trong tên bài gốc |

## Nhãn còn lại
-       1 [CẦN BỔ SUNG số trang]
-       1 [CẦN NÊU TÊN hai chỉ báo]
-       1 [CẦN XÁC MINH các lần thay đổi biên độ trong giai đoạn 2009–2025]
-       1 [CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong VN-Index và quy chế phân bảng chính thức]
-       1 [CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong các chỉ số]
-       1 [CẦN XÁC MINH kế hoạch chuyển cổ phiếu đăng ký giao dịch theo khoản 4 Điều 4 Thông tư số 57/2021/TT-BTC]
-       1 [CẦN XÁC MINH phạm vi sàn của từng bài]
-       1 [CẦN XÁC MINH phạm vi sàn mà FTSE Russell sàng lọc trước ngày chuyển sàn]
-       1 [CẦN XÁC MINH quy tắc làm tròn giá trần và giá sàn theo bước giá của HOSE và HNX]
-       1 [CẦN XÁC MINH quy định bước giá theo từng thời kỳ]
-       1 [CẦN XÁC MINH số hiệu và ngày trên bản gốc; bản OCR chỉ đọc được tháng 9/2026]
-       1 [CẦN XÁC MINH thứ tự tác giả trên trang bài của tạp chí]
-       1 [CẦN XÁC MINH tập, số và trang]
-       1 [CẦN ĐỐI CHIẾU bản gốc của hai bài]
