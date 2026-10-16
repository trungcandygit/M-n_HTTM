# Nhật ký thay đổi vòng 13 (sửa trình bày và rút gọn, không chạy agent)

Bản: `outputs/round-13/de-cuong-v13-round-13.docx` (sửa từ v12). Validate PASSED; 7 công thức OMML; 8 bảng; không tracked changes. Theo yêu cầu của thí sinh, vòng này không mở agent phản biện.

## Bằng chứng tuân thủ
- **vina-me** (Skill tool): áp mục "Khi sửa văn có sẵn" (sửa cấu trúc câu và đoạn trước, giữ dữ kiện, con số, trích dẫn) và điều 3 (không rút câu cho vừa một mốc số chữ; bỏ hẳn ý lặp). Chạy `scripts/soat.mjs` trên 18 đoạn viết lại: chỉ còn "–" trong tên ghép Tokyo–Osaka và "&" trong trích dẫn APA 7 (đều được miễn), và chữ "CHIẾU" trong nhãn [CẦN ĐỐI CHIẾU].
- **vietnamese-human-writing** (Skill tool): đọc toàn bộ `master-writing-rules.md`; áp R19 (bỏ câu diễn giải lại điều đã nói), R39 (bỏ thông tin lặp giữa 4.1 và 4.2), R31 (tách câu quá dài), R06 (không đổi dữ kiện).
- **anthropic-skills:docx**: sửa trực tiếp XML, validate với `--original`.

## Định dạng bảng
- Bỏ nền xám E7E6E6 ở dòng tiêu đề của style "Table" (áp cho cả 8 bảng). Giữ khung đơn và chữ đậm ở dòng tiêu đề.
- Bảng chữ viết tắt tách thành 3 cột: Chữ viết tắt | Tiếng Anh | Tiếng Việt. Thêm tên tiếng Anh chính thức của HNX, HOSE, UPCoM, VNX. Hai ký hiệu CS và H là ký hiệu riêng của đề tài nên cột tiếng Anh ghi "Không có".

## Rút gọn (thân bài từ mục 4.1 đến trước mục 11: khoảng 17.500 xuống 16.900 chữ, giảm khoảng 3,5%)
| Mục | Thay đổi |
|---|---|
| 4.1 | Gộp hai đoạn về phân vai trung tâm (Bắc Kinh, Thượng Hải) thành một; gộp hai đoạn bằng chứng quốc tế (Tel Aviv, Euronext, Tokyo–Osaka) thành một đoạn ngắn và trỏ sang mục 4.2; rút đoạn mốc UPCoM; rút đoạn sản phẩm. Định nghĩa UPCoM ở lần dùng đầu |
| 4.2 | Rút đoạn hợp nhất sàn (C) |
| 4.3.2 | Gộp hai đoạn về ngưỡng lợi suất khi tính Amihud; rút đoạn giải thích Hình 1 |
| 4.3.7 | Rút các đoạn mức chịu cú sốc, FTSE, tương tác, suy luận cho hệ số tương tác, phân tích theo trụ sở (bỏ một đoạn lặp); rút câu Conley–Taber |
| 4.3.8, 4.3.10 | Rút đoạn tác động lan tỏa và đoạn phương án UPCoM |

Không bỏ giả thuyết, phương trình, kiểm định, phương án dự phòng, trích dẫn hay nhãn xác minh nào.

## Nhãn
- Gỡ "[CẦN NÊU TÊN hai chỉ báo]": hai chỉ báo bị biên độ cắt trực tiếp là độ phi thanh khoản Amihud và chênh lệch Corwin–Schultz (đều tính từ mức biến động giá). **Đây là lựa chọn thiết kế; thí sinh xem lại.**
- Còn 13 nhãn (danh sách như vòng 12, trừ nhãn trên).
