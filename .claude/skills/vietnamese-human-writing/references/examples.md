# Ví dụ áp dụng / Application examples

Các ví dụ dùng dữ kiện giả định riêng cho từng bài. Đây là minh họa biên tập, không phải kết quả thử nghiệm trên Claude hay bằng chứng về nguồn gốc tác giả.

These examples use task-local, hypothetical facts. They illustrate editing decisions; they are not Claude benchmark results or evidence of human authorship.

## 1. Giữ số liệu, bỏ lời ca ngợi / Preserve numbers, remove praise

**Đầu vào / Input**

"Dự án thư viện lớp học không chỉ khẳng định vai trò then chốt của nhà trường mà còn mở ra một tương lai đầy hứa hẹn. Sau hai tuần, học sinh góp được 120 quyển sách."

**Bản sửa / Revision**

"Sau hai tuần, học sinh góp được 120 quyển sách cho thư viện lớp học."

Giữ "hai tuần" và "120 quyển sách"; bỏ nhận định thiếu căn cứ. / Preserve the time and count; remove unsupported claims. R03, R06, R09, R12, R16.

## 2. Lời thoại dạy học / Educational dialogue

**Đầu vào / Input**

"Muốn đo góc, chúng ta cần tiến hành sử dụng thước đo góc. Có thể nói rằng đơn vị đo góc đóng vai trò quan trọng và được gọi là độ."

**Bản sửa / Revision**

"Muốn đo góc, chúng ta dùng thước đo góc. Đơn vị đo góc là độ."

Giữ đủ hai ý và thuật ngữ "góc"; bỏ động từ vòng vo. / Keep both ideas and the repeated term; remove indirect verbs. R14, R20, R38, R46.

## 3. Bảo toàn phần trích dẫn / Protect a quotation

**Yêu cầu / Request**

Biên tập câu dẫn, giữ nguyên lời trích: Đây là một nhận định vô cùng sâu sắc, minh chứng cho tinh thần trách nhiệm. Người trực ca nói: "Tôi sẽ ở lại đến khi ca sau tới."

**Bản sửa / Revision**

Người trực ca nói: "Tôi sẽ ở lại đến khi ca sau tới."

Giữ nguyên lời trích, bỏ đánh giá không có dữ kiện hỗ trợ. / Preserve the quote exactly; remove unsupported evaluation. R03, R06, R09, R10.

## 4. Không bịa để làm câu cụ thể hơn / Do not invent specifics

**Đầu vào / Input**

"Nhóm đã thử một phương pháp mới. Chưa có dữ liệu về kết quả."

**Bản sửa / Revision**

"Nhóm đã thử một phương pháp mới. Chưa có dữ liệu về kết quả."

Không thêm tỷ lệ cải thiện hoặc kết luận thành công. Giữ nguyên khi đầu vào đã rõ nghĩa. / Do not invent improvements or a success claim. Leave clear prose unchanged. R01, R06, R07, R44.

