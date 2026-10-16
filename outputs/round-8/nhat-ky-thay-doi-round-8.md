# Nhật ký thay đổi vòng 8

Bản: `outputs/round-8/de-cuong-v8-round-8.docx` (sửa từ v7, không dùng tracked changes).
Kiểm tra kỹ thuật: validate PASSED; 7 công thức OMML, 7 bảng, SmartArt và mục lục giữ nguyên; 0 `w:ins`/`w:del`; render PDF 39 trang. LibreOffice không vẽ được các công thức OMML (bản v7 cũng vậy), nên khi xem công thức cần mở bằng Word.

## Bằng chứng tuân thủ
- Agent A (phương pháp và cách viết), gọi tuần tự: academic-paper-reviewer (tự đóng 5 vai trong một ngữ cảnh vì thiếu contract và công cụ Agent; đã ghi lỗi nguyên văn), mhe-identification (Critic), aer-identification, review-methodology, liquidity-measures, statistical-power (mô phỏng MDE cục bộ, không dùng dữ liệu thật), econ-write, scientific-critical-thinking. Báo cáo: `reports/r8-review-A.md`. Kết quả: 2 CRITICAL, 3 MAJOR, 11 MINOR.
- Agent B (kiểm chứng), gọi tuần tự: vn-legal-verify, fact-checker, credible-claims, consistency-checker (checklist, không chạy script), citation-management (chỉ đọc SKILL.md). Báo cáo: `reports/r8-review-B.md`. Kết quả: 0 CRITICAL, 4 MAJOR, 14 MINOR.
- Luồng chính: anthropic-skills:docx (đã đọc merge_runs.py, validate.py và các module phụ trước khi chạy); sửa bằng công cụ thay chuỗi xuyên run, 129/129 thao tác áp thành công.

## Đã sửa

| Mã | Nội dung |
|---|---|
| A-CR1 | Amihud tính trên các ngày có lợi suất tuyệt đối dưới một **ngưỡng chung thấp hơn ±7%**, cho cả hai nhóm và hai giai đoạn, loại ngày liền sau ngày chạm biên độ; chỉ giao dịch khớp lệnh; số ngày hợp lệ tối thiểu; báo cáo tỷ lệ ngày loại. Lý do: chỉ loại ngày chạm biên độ tạo độ chệch cơ học cùng chiều H3. Sửa ở mục 4.2, Bảng 2 (H3), phương trình (5). |
| A-CR2 | Suy luận chính cho H3 đổi sang **bootstrap tự hồi quy trên chuỗi chênh lệch dₜ** (định nghĩa rõ thống kê kiểm định); hoán vị theo ngày giả (Conley & Taber) chỉ là kiểm tra bổ sung, vì mô phỏng cho thấy nó bác bỏ quá thường xuyên. Cập nhật quy tắc quyết định H3, thủ tục Holm và nội dung tệp đăng ký. |
| A-MJ1 | Kiểm định điểm gãy (Bai & Perron, 1998) trong giai đoạn tham chiếu 16 năm; cửa sổ trước bắt đầu sau điểm gãy cuối; báo cáo kèm cửa sổ trước 24 tháng. |
| A-MJ2 | Bước giá khác nhau giữa sàn: báo cáo tỷ lệ ngày lợi suất 0 và Corwin–Schultz theo nhóm mức giá. |
| A-MJ3 | Đưa MDE của H3 vào đề cương (0,64σ đến 1,76σ theo mức tự tương quan; ví dụ minh họa khoảng 22% Amihud); phân biệt "chưa đủ cơ sở kết luận" với "không có tác động". |
| B-MJ1 (MJ6) | Theo quyết định của anh: thêm cam kết học **tập trung toàn thời gian** (NQ 57 Điều 11.3) ở mục 8.2, và thời gian 4 năm không vượt 48 tháng (Điều 13) ở mục 7.4; thêm NQ 57 vào danh mục. |
| B-MJ2 | Hisada (2018) mô tả lại đúng mẫu: cổ phiếu sẵn có trên Tokyo (sàn tiếp nhận), không phải cổ phiếu chuyển từ Osaka; dùng điểm này để nêu rủi ro lan tỏa sang nhóm đối chứng HOSE và làm rõ đóng góp. |
| B-MJ3 | Câu nối với bài toán 19 thu hẹp đúng phạm vi đo: chất lượng giao dịch cổ phiếu giữa sàn của Hà Nội và của TP.HCM, và thay đổi khi chuyển sàn. |
| B-MJ4 | H2 thống nhất giai đoạn tham chiếu 6/2009–6/2025 (Bảng 2, Hình 1), quy tắc quyết định theo giá trị p và ngưỡng Holm; giai đoạn chuyển tiếp chỉ mô tả. |
| MINOR (A) | m1 mắt xích nhân quả; m2 "bình quân bảy mô hình"; m4 kiểm định đồng thời δk 1/2024–5/2025, thêm số hạng δpre vào công thức (6); m5 mẫu xử lý là mọi mã chuyển sàn; m6 lý do chọn chỉ báo; m7 chuẩn hóa Amihud theo vốn hóa danh nghĩa; m8 mẫu cân bằng cho H1; m9 rổ H ghép có hoàn lại và M1 là so sánh sạch nhất; m10 câu Bắc Kinh; m11 câu thiếu chủ ngữ. m3 không cần sửa: công thức (4) đã dùng \|M\|. |
| MINOR (B) | m1 đơn vị công bố GFCI; m2 lịch VNX ghi rõ nguồn báo chí; m3 hạn UPCoM do TT69 đặt; m4 bỏ ngày chưa có nguồn của NQ 222; m5 K2 so với "ba vấn đề"; m6 cập nhật MQI cho UPCoM; m7 rổ CS tối đa 30 mã; m8 nội dung bài báo 3; m9 thêm ARIMA, GDP, OECD vào chữ viết tắt, ghi chú ký hiệu H; m10 thống nhất ngày (30/9/2026, tháng 7/2026, 18/3/2026); m11 thống nhất **Nguyễn & Nguyễn (2026a, 2026b)**; m12 **toàn bộ 68 mục danh mục chuyển sang APA 7** (có "&", năm trong ngoặc, tạp chí và tập in nghiêng, DOI dạng URL); m14 gỡ 9 nhãn bằng câu kế hoạch hoặc nguồn có trong hồ sơ. |

Không thêm DOI hay số trang nào từ trí nhớ. Mục Pakistan 2016 (chưa có nguồn) được thay bằng Arnold và cộng sự (1999, dẫn theo Hisada, 2018); câu chỉ nói điều Hisada nói ("exchange mergers increase liquidity").

## Nhãn còn lại trong v8 (cần tài liệu, xem danh sách tài liệu)
GFCI 40 (67/117, 71); thông báo gốc của VNX về lịch; kế hoạch chuyển UPCoM (khoản 4 Điều 4); năm thành lập Sở GDCK Bắc Kinh; "khoảng 300" mã; biên độ theo thời kỳ; bước giá theo thời kỳ; phạm vi sàn của các bài trước; cách HOSE xử lý mã chuyển sàn trong VN-Index; mốc FTSE và phân bảng; số hiệu/ngày QĐ 737; trích yếu NQ 57; Daw & Hatfield (2018); số trang Gehrig (2000).

## Việc anh cần xác nhận
- Câu cam kết ở mục 8.2 viết "hoàn thành, bảo lưu hoặc dừng các chương trình đang theo học". Nếu anh có phương án cụ thể cho từng chương trình, báo tôi để ghi chính xác.
