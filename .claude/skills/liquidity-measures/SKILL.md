---
name: liquidity-measures
description: Chọn, định nghĩa và phản biện chỉ báo thanh khoản và chất lượng thị trường tính từ dữ liệu ngày (Amihud, Roll, Corwin–Schultz, Abdi–Ranaldo, tỷ lệ ngày lợi suất bằng 0 / LOT, vòng quay) cho nghiên cứu thị trường cổ phiếu, đặc biệt thị trường có biên độ giá và bước giá lớn như Việt Nam. Dùng skill này bất cứ khi nào văn bản đo thanh khoản, xây chỉ số chất lượng thị trường, so sánh sàn, nghiên cứu chuyển sàn/hợp nhất sàn, hoặc khi người dùng hỏi "dùng chỉ báo thanh khoản nào", "Amihud có ổn không", "xử lý ngày chạm trần/sàn", kể cả khi họ không nhắc tên chỉ báo. Không gọi mạng.
---

# liquidity-measures — khung chọn và phản biện chỉ báo thanh khoản từ dữ liệu ngày

Mục đích: ở thị trường mới nổi không có dữ liệu lệnh trong ngày đầy đủ, mọi kết luận về "chất lượng thị trường" phụ thuộc vào việc chỉ báo ngày đo đúng cái gì. Một chỉ báo bị méo bởi biên độ giá hay bước giá có thể tạo ra "tác động" giả khi biên độ hoặc bước giá đổi cùng lúc với sự kiện. Skill này giúp chọn chỉ báo theo chiều thanh khoản cần đo, nêu giả định, và chỉ ra chỗ chỉ báo hỏng.

**Về trích dẫn:** thông tin xuất bản dưới đây ghi theo hiểu biết chung. Trước khi đưa vào đề cương, đối chiếu từng mục với bài gốc (tạp chí, tập, số, trang, DOI) và với bảng kết quả được trích. Mọi nhận định kiểu "chỉ báo X tốt nhất" phải kèm bảng hoặc trang của bài gốc; nếu chưa có bài gốc, gắn [CẦN ĐỐI CHIẾU].

## 1. Bản đồ chiều thanh khoản → chỉ báo

| Chiều | Chỉ báo ngày | Đo gì |
|---|---|---|
| Chi phí giao dịch (độ chặt) | Roll (1984); Corwin–Schultz (2012) high-low; Abdi–Ranaldo (2017) close-high-low; tỷ lệ ngày lợi suất bằng 0 (Lesmond, Ogden & Trzcinka, 1999) | ước lượng chênh lệch giá mua–bán theo % |
| Tác động giá (độ sâu) | Amihud (2002) ILLIQ | biến động giá trên một đơn vị giá trị giao dịch |
| Hoạt động giao dịch | vòng quay, số ngày có giao dịch | cường độ giao dịch, không phải chi phí |
| Khả năng hồi phục | tự tương quan lợi suất, tỷ lệ phương sai | tốc độ giá trở lại sau cú sốc |

Không gộp chiều này với chiều kia mà không nói rõ. Một chỉ số tổng hợp (vd chuẩn hoá z rồi lấy trung bình) phải nêu trọng số, chiều nào được đại diện, và chứng minh kết luận không do một thành phần chi phối.

## 2. Định nghĩa chuẩn (ghi đủ đơn vị)

- **Amihud:** ILLIQ_{i,m} = (1/D_{i,m}) Σ_d |r_{i,d}| / DVOL_{i,d}, với DVOL là giá trị giao dịch (đồng), D là số ngày có giao dịch trong tháng. Báo cáo thang đo (vd ×10^9), dùng log, đặt số ngày tối thiểu mỗi tháng, winsorize, và nói cách xử lý ngày DVOL = 0.
- **Roll:** S = 2√(−Cov(Δp_t, Δp_{t−1})). Không xác định khi hiệp phương sai dương; phải nêu quy tắc (gán 0, bỏ, hay dùng biến thể).
- **Corwin–Schultz:** dùng giá cao/thấp hai ngày liền. β = Σ_{j=0}^{1}[ln(H_{t+j}/L_{t+j})]², γ = [ln(H_{t,t+1}/L_{t,t+1})]², α = (√(2β) − √β)/(3 − 2√2) − √(γ/(3 − 2√2)), S = 2(e^α − 1)/(1 + e^α). Nêu cách điều chỉnh qua đêm và cách xử lý ước lượng âm.
- **Abdi–Ranaldo:** dùng giá đóng cửa c_t và trung điểm η_t = (ln H_t + ln L_t)/2. Ước lượng S² = 4·E[(c_t − η_t)(c_t − η_{t+1})]. Nêu cách lấy trung bình (theo cặp ngày hay theo tháng) và cách xử lý giá trị âm.
- **Zero-return / LOT:** tỷ lệ ngày lợi suất bằng 0 trong tháng. Nêu rõ: ngày không giao dịch có tính hay không.
- **Vòng quay:** khối lượng / số cổ phiếu lưu hành (hoặc tự do chuyển nhượng — nói rõ, và dùng nhất quán giữa các sàn).

## 3. Kiểm chứng chỉ báo

Chỉ báo ngày cần được biện minh bằng các nghiên cứu so sánh với chuẩn dữ liệu trong ngày: Goyenko, Holden & Trzcinka (2009, *Journal of Financial Economics*) và Fong, Holden & Trzcinka (2017, *Review of Finance*, nghiên cứu toàn cầu). Khi viện dẫn, ghi rõ: tiêu chí so sánh (tương quan theo chuỗi thời gian hay chéo, RMSE), tần suất (tháng/ngày), mẫu thị trường, và chỉ báo nào thắng ở tiêu chí nào — lấy từ bảng của bài gốc. Nếu có dữ liệu giá mua/bán đóng cửa cho một phần mẫu, tự kiểm chứng: tính tương quan giữa chỉ báo ngày và chênh lệch yết giá đóng cửa trên mẫu đó.

## 4. Thị trường có biên độ giá và bước giá lớn — các bẫy bắt buộc kiểm

1. **Ngày chạm biên độ.** Lợi suất bị chặn tại trần/sàn, khối lượng thường thấp hoặc lệch một phía. Amihud bị méo (|r| bị cắt, DVOL nhỏ), Roll và các ước lượng high-low bị méo (H = L hoặc giá đóng cửa trùng biên). Quy tắc chuẩn: loại ngày chạm biên độ **và** ngày liền sau (vì phần điều chỉnh giá bị dồn sang); báo cáo tỷ lệ ngày bị loại theo sàn và thời kỳ; độ nhạy với ngưỡng "gần biên" (vd ≥ 95% biên độ).
2. **Biên độ khác nhau giữa sàn và đổi theo thời gian.** Chỉ báo không so sánh trực tiếp được giữa sàn có biên độ khác nhau. Khi một sự kiện (vd chuyển sàn) kéo theo đổi biên độ, tác động đo được gộp hiệu ứng biên độ với hiệu ứng sàn; nêu rõ đây là tác động gộp, hoặc tách bằng kiểm tra trên mẫu ngày cách xa biên.
3. **Bước giá lớn so với giá.** Với cổ phiếu giá thấp, bước giá chiếm tỷ lệ lớn của giá; Roll, Corwin–Schultz, Abdi–Ranaldo và tỷ lệ ngày lợi suất 0 phản ánh bước giá nhiều hơn chi phí thật. Kiểm tra theo nhóm mức giá; cân nhắc biến kiểm soát nghịch đảo giá; báo cáo khi quy định bước giá đổi.
4. **Phiên khớp lệnh định kỳ / cách tính giá đóng cửa.** Nếu giá đóng cửa là giá khớp định kỳ hoặc giá bình quân, chỉ báo dựa trên giá đóng cửa đổi ý nghĩa khi cơ chế đổi.
5. **Giao dịch thỏa thuận.** Nói rõ DVOL có gồm giao dịch thỏa thuận hay không; dùng nhất quán.
6. **Thang tiền tệ và lạm phát.** Amihud phụ thuộc mức giá và quy mô thị trường; khi so sánh dài hạn, chuẩn hoá theo thời kỳ hoặc dùng biến thể điều chỉnh theo vốn hoá thị trường.
7. **Sống sót và thành phần sàn.** Sàn đổi thành phần (niêm yết mới, hủy niêm yết, chuyển sàn) làm chỉ số cấp sàn thay đổi cơ học; báo cáo cả mẫu cân bằng.

## 5. Đầu ra khi phản biện một văn bản

```
## Bảng chỉ báo
| Chỉ báo | Chiều | Định nghĩa trong bài có đủ đơn vị/quy tắc? | Bẫy ở mục 4 áp dụng | Xử lý trong bài | Thiếu gì |

## Phát hiện (CRITICAL / MAJOR / MINOR)
mỗi phát hiện: chuỗi gốc chính xác → chuỗi thay thế chính xác; nêu tài liệu cần đối chiếu nếu dựa vào văn liệu.
```

## Tài liệu gốc cần đối chiếu trước khi trích

Amihud (2002, *Journal of Financial Markets*); Roll (1984, *Journal of Finance*); Lesmond, Ogden & Trzcinka (1999, *Review of Financial Studies*); Corwin & Schultz (2012, *Journal of Finance*); Abdi & Ranaldo (2017, *Review of Financial Studies*); Goyenko, Holden & Trzcinka (2009, *Journal of Financial Economics*); Fong, Holden & Trzcinka (2017, *Review of Finance*); Hasbrouck (2009, *Journal of Finance*). Tập, số, trang và DOI: [CẦN ĐỐI CHIẾU với bài gốc].
