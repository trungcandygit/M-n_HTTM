# Vòng 5 (xác nhận), rà slide: 93/100 (bản repo) -> 96/100 (bản sửa)

Tệp sửa: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/v5/b/slides.tex
Diff: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/v5/slides-v5.diff
PDF thử: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/v5/b/slides.pdf
Biên dịch xelatex hai lượt trên bản sao: 0 lỗi, 0 overfull/underfull, 38 trang (thêm 1 phụ lục), tiêu đề 1 dòng (trang 31, 32, 37 chỉ là chỉ số dưới H). Đã xem ảnh -r 40 các trang đổi, so với wide.pdf trang 24–25.

## Xác nhận các lỗi vòng 4
Đã áp đủ C1 (lý do lực kiểm định), M1–M6 và các MINOR; không còn \so giữa câu, \small, "Black-Litterman". Khẳng định "chưa có so sánh HNX với HOSE" đã bỏ khỏi slide 2. Số mới đều có nguồn: 12%, 22%, 30% (ban-dai ch04-3d dòng 27–29), 117 trung tâm (v14 [87]), 4 công trình + 8 bản thảo, 30/9 và 9/10/2026 (v14 [252], [253], [262]). Hình khác biệt kép: không xét theo yêu cầu.

## CRITICAL
Không có.

## MAJOR (từ yêu cầu bổ sung của người dùng trong vòng 5; bản repo chưa đáp ứng, bản sửa đã xử lý)
M1. [phần chính, "hơi nhiều toán"] Phần chính có 4 công thức (MQI, DiD, Ḡ, GFCI) và ký hiệu rời ($d_t$, $\bar d$, $\phi$, $\sigma_d$, $|r|$). Nguồn: v14 [187–190], [206–207]. Sửa:
- tr. 9 MQI: khung dinhnghia bằng lời: "Chỉ số theo tháng cho từng sàn: trung bình ba chiều thanh khoản, hiệu quả thông tin, minh bạch; mỗi chiều là trung bình điểm z của các chỉ báo thành phần."
- tr. 20 Ḡ: khung bằng lời: "Lợi suất tương đương chắc chắn của rổ HOSE trừ của rổ chuyển sàn, tính sau chi phí giao dịch, lấy trung bình trên bảy mô hình phân bổ."; gạch 2: "Tương đương chắc chắn: lợi suất trung bình trừ phần phạt rủi ro, mức ngại rủi ro 5"; gạch 3: "\HH{4}: khoảng cách thu hẹp; 20 cửa sổ trước, 8 sau: \al{chỉ ước lượng}". Công thức Ḡ, U_m chuyển vào phụ lục H₄ (gạch 3).
- tr. 21 GFCI: khung bằng lời: "Điểm GFCI chuẩn hóa của từng trung tâm theo kỳ, hồi quy theo mức phát triển thị trường cổ phiếu; kiểm soát thu nhập, quản trị nhà nước, hiệu ứng cố định trung tâm và kỳ."; gạch: vòng quay, vốn hóa / GDP; "Sai số chuẩn phân cụm theo quốc gia; \HH{1}: hệ số dương"; "GFCI có nhân tố giao dịch cổ phiếu: hệ số \al{không là tác động nhân quả}". Phương trình và định nghĩa ký hiệu: slide mới "Phụ lục: mô hình cho \HH{1}".
- tr. 16 bootstrap: "Chênh lệch log Amihud giữa hai nhóm, theo tháng"; "Thống kê: trung bình sau trừ trung bình trước"; "Ước lượng mô hình tự hồi quy của chuỗi"; "Tỷ lệ thống kê giả không lớn hơn giá trị thật".
- tr. 17 lực: hàng "Tự tương quan của chuỗi chênh lệch", "Hiệu ứng nhỏ nhất (bội số độ lệch chuẩn)", "Độ lệch chuẩn 0,2: log Amihud / Amihud giảm".
- tr. 11: "$|r|$" -> "lợi suất tuyệt đối".
Kết quả: phần chính còn đúng một công thức hiển thị (DiD, trong khung assumption); ký hiệu còn lại chỉ là của phương trình này (δ ở tr. 18) và $\pm$.

M2. [tr. 24 "Bốn năm, sáu chỉ tiêu"] Chưa nói rõ Hà Nội nhận gì, ai dùng, khi nào. Nguồn: v14 [86], [89]–[93], [221], Bảng 5 [245]. Sửa: thay slide này bằng một bảng kiểu "Basic table with note", tiêu đề "Hà Nội nhận bốn sản phẩm, mỗi sản phẩm có người dùng và mốc":
- Chỉ số chất lượng, ba sàn | Sở KH&CN, HNX | Năm 1; mã nguồn năm 4
- Tác động lên thanh khoản | HNX, HOSE, UBCKNN | Năm 2 (giữa kỳ), 3
- Chỉ số khả năng đầu tư | Tổ chức đầu tư | Năm 3
- Báo cáo định hướng chuyên môn hóa | Sở KH&CN, \al{HNX} | Năm 4
- caption: "Chỉ số chất lượng có thể là cấu phần của Hệ thống dữ liệu tài chính đô thị (bài toán số 19)."
Lưu ý trung thực: v14 chỉ cam kết công bố chỉ số kèm mã nguồn trên kho mở, không cam kết mở dữ liệu gốc (dữ liệu sở cần giấy phép, v14 [245] quý 1), nên slide không viết "dữ liệu mở". Gán người dùng theo từng dòng là chia danh sách chung ở v14 [221]; "HNX" ở báo cáo theo v14 [93] ("ưu tiên HNX"). Đăng ký trước (tr. 23) và ba bài báo không còn trên slide này; ba bài báo vẫn ở v14, nếu muốn giữ chỉ tiêu WoS Q1/Q2 thì thêm vào ý 3 của slide kết. Phần chính vẫn 4 bảng (giới hạn).

## MINOR
- [tr. 17] caption 2 dòng, quy tắc CLAUDE.md là 1 dòng (mẫu cho phép 2) -> "Lực 80\%, một phía 0,05/3; 193 tháng trước, 24 tháng sau; độ lệch chuẩn 0,2 là minh họa." (thêm lại 193/24 tháng, v14 [206]; lý do số tháng ở phụ lục không phân cụm).
- [tr. 17] "cú sốc riêng của nhóm chỉ giảm khi thêm tháng": cú sốc không giảm, nhiễu trung bình mới giảm; đã bỏ cùng caption.
- [phụ lục ba cú sốc] $\rightarrow$ trong ô bảng -> "xuống"; caption rút còn 1 dòng.
- [phụ lục Holm] caption 2 dòng -> "p một phía: cụm quốc gia (\HH{1}), bootstrap khối dừng (\HH{2}), tự hồi quy (\HH{3}); \HH{4} ngoài họ."
- [tr. 3] "Bài toán số 19: tìm phương thức" mơ hồ; giữ vì ô hẹp (v14 [83]: "Phương thức nào để xây dựng Hà Nội thành trung tâm tài chính...").
- [tên] slide viết "chỉ số chất lượng thị trường", v14 viết "Chỉ số chất lượng thị trường vốn"; nhất quán trong deck, chấp nhận.
- [trang đầu, tùy chọn] Nếu deck nộp xin hỗ trợ: v14 [288], [327] gắn đề cương với NQ 57/2026/NQ-HĐND (hỗ trợ đào tạo tối đa 48 tháng, Điều 13); có thể ghi vào \date. Không tự thêm.
- [phụ lục] 9 slide dự phòng (> 3–5); chấp nhận vì không trình bày.
- [tr. 16] một số ý cột trái xuống 2 dòng (≤ 2, đạt).

## Điểm
- Bản repo 93 = 100 − 2 (phụ lục dư) − 1 (caption 2 dòng) − 4 (mật độ ký hiệu, nay là yêu cầu của người dùng). Không còn CRITICAL; M1, M2 phát sinh từ yêu cầu mới.
- Bản sửa 96 = 100 − 2 (phụ lục 9 slide) − 2 (Shapiro: phần lõi chưa có hình kết quả dự kiến ngoài did.tex). Hết CRITICAL, MAJOR: đạt.

## Chưa kiểm được
- Thời lượng nói thực tế. Bố cục chỉ xem ở -r 40.
