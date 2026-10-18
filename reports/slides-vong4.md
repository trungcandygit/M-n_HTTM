# Vòng 4, rà slide: 84/100 (bản hiện tại) -> 95/100 (bản sửa)

Tệp sửa: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/v4/slides.tex
Diff: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/slides-v4.diff
Biên dịch xelatex hai lượt (bản sao, hinh/ mới nhất, không sửa did.tex, did.dat): 0 lỗi, 0 overfull/underfull, 37 trang, tiêu đề phần chính 1 dòng (trang 31, 36 ở phụ lục chỉ là chỉ số dưới H₄, H₁–H₃), không chữ vượt mép.

## CRITICAL

C1. [tr. 17, "Lực kiểm định phụ thuộc chủ yếu vào số tháng"] Lập luận sai: "Mọi mã chịu chung một cú sốc mỗi tháng: thêm mã không làm nhiễu chung nhỏ đi". Cú sốc chung cho mọi mã bị triệt tiêu khi lấy chênh lệch (đã nằm trong τ_t, đúng như slide DiD và phụ lục "không phân cụm"); nhiễu còn lại là cú sốc tác động KHÁC NHAU lên hai nhóm. Slide vừa sai suy luận vừa mâu thuẫn với phụ lục. Nguồn: v14 [205]; ban-dai ch04-3d-tincay.tex dòng 14.
CŨ: \item Mọi mã chịu chung một cú sốc mỗi tháng: / \item Thêm mã không làm nhiễu chung nhỏ đi, thêm tháng thì có
MỚI: \item Nhiễu của chuỗi tháng $d_t$: / \item Cú sốc như nhau với mọi mã: triệt tiêu khi lấy chênh lệch / \item Cú sốc khác nhau giữa hai nhóm: thêm mã không giảm, thêm tháng thì giảm

## MAJOR

M1. [tr. 10 "Thách thức: bốn thay đổi" và tr. 18 "Điểm yếu"] Mâu thuẫn giữa hai slide: tr. 10 kể bước giá, biên độ, chỉ số, nơi đặt sàn; tr. 18 (và v14 [197]) kể biên độ, bước giá, hệ thống giao dịch, chỉ số. "Nơi đặt sàn" là kênh của phân tích phụ theo trụ sở (v14 [183]), không phải thay đổi quy tắc. Sửa: dựng lại theo 3 cấp đúng v14: • Quy tắc giao dịch (– Bước giá □ dưới 10.000 đồng: 100 xuống 10 đồng; – Biên độ ±10% xuống ±7% □ Amihud có thể giảm cơ học); • Hạ tầng và chỉ số (– Hệ thống giao dịch của HOSE; – Vào VN-Index). Kênh trụ sở giữ ở phụ lục.
M2. [tr. 21, mô hình H₁] α_i, τ_t không định nghĩa trên slide, lại trùng ký hiệu với slide DiD (ở đó i là mã, α_i là hiệu ứng mã). Nguồn: v14 [189]. Sửa: khung "Điểm GFCI chuẩn hóa $Z_{it}$ của trung tâm $i$ ở kỳ $t$:"; gạch 2: "$\alpha_i$, $\tau_t$: hiệu ứng cố định trung tâm, kỳ; cụm theo quốc gia; \HH{1}: $\beta > 0$". Gạch 3 bỏ khẳng định chung "GFCI đã chứa dữ liệu giao dịch" (v14 [190] chỉ nói 3/144 nhân tố của kỳ 40) -> "GFCI có nhân tố giao dịch cổ phiếu: β không là tác động nhân quả".
M3. [tr. 20, Ḡ] μ, σ² dùng mà chưa định nghĩa (−15 theo I); "7 mô hình" vừa ở gạch dưới vừa ngầm trong công thức. Nguồn: v14 [187–189]. Sửa: khung "Lợi suất tương đương chắc chắn của mô hình $m$: $U_m = \mu - \rho\sigma^2/2$; trung bình trên 7 mô hình:"; gạch 2: "$\mu$, $\sigma^2$: trung bình, phương sai lợi suất vượt trội sau chi phí; $\rho = 5$"; gạch 3: "\HH{4}: $\bar{G}$ thu hẹp; 20 cửa sổ trước, 8 sau: \al{chỉ ước lượng}".
M4. [tr. 2, "Khoảng trống"] "Chưa có so sánh chất lượng HNX với HOSE" khẳng định tuyệt đối; v14 [108] giới hạn "trong phạm vi tìm kiếm", chưa gồm Scopus, WoS. Sửa: "Chưa thấy nghiên cứu so sánh chất lượng HNX với HOSE".
M5. [tr. 11, "Xử lý"] "Loại mã giá dưới mức tối thiểu ...; báo cáo theo nhóm giá" lệch v14 [125]: mã giá thấp bị loại khỏi Amihud và "báo cáo riêng" (báo cáo theo nhóm giá là của tỷ lệ ngày lợi suất 0 và Corwin–Schultz, [123]). Sửa, đồng thời dựng 3 cấp: • Quy tắc: chỉ tính ngày có |r| dưới một ngưỡng chung, bỏ ngày liền sau: – Cùng ngưỡng cho mọi mã, mọi giai đoạn – Ngưỡng dưới mức tăng tối đa ở ±7%: □ Giá 1.140 đồng chỉ tăng được 6,14% □ Mã giá quá thấp: loại khỏi Amihud, báo cáo riêng.
M6. [toàn deck, theo yêu cầu tối giản mới] Cắt chữ, đưa chi tiết khỏi phần chính:
- tr. 1: gộp "Lịch VNX" thành 1 dòng; "(số mã tính đến phiên 30/9/2026)" vào trong ý 299 mã.
- tr. 13 DiD: bỏ "phụ: UPCoM" (đã ở tr. 18); rút gạch 2.
- tr. 15 Cú sốc trùng: bỏ "nới biên độ, giao dịch xuyên trưa" (chưa ban hành, v14 [195]: chỉ báo cáo thêm).
- tr. 18 Điểm yếu: bỏ lặp "Loại mã FTSE; biến giả nhóm bảng" (đã ở tr. 15).
- tr. 23 Kế hoạch: bỏ phương án "dữ liệu sau ngắn, rổ 20 mã"; rút 3 ý đăng ký trước.
- tr. 4 Giả thuyết: H₁ có chủ ngữ, ngắn: "thị trường cổ phiếu phát triển hơn đi kèm điểm GFCI cao hơn".

## MINOR
- [tr. 24 Năm 2–3] "Bài báo 1; H₁" dễ hiểu bài báo 1 là H₁; v14 bảng kế hoạch: bài 1 = H₂, bài 2 = H₃–H₄, bài 3 = H₁ -> đã ghi rõ.
- [tr. 3] "Bắc Kinh lớn dù ..." -> "Bắc Kinh: trung tâm lớn, phần lớn thời gian không có sàn quốc gia (Naeem, 2023)".
- [tr. 18] "gọi là chưa đủ cơ sở kết luận" -> "chưa đủ cơ sở kết luận".
- [trang đầu] "ĐHQGHN -- Hà Nội" -> "ĐHQGHN, Hà Nội" (còn từ vòng 3).
- [phụ lục bảy mô hình] "Black-Litterman" -> "Black--Litterman" (còn từ vòng 3).
- [phụ lục H₄, sự kiện, sai lệch, phân cụm] \so giữa câu -> dấu hai chấm.
- [phụ lục nghiên cứu sự kiện] thêm lại "trước 1/2024 gộp" (v14 [176]).
- [tr. 1, kết] Sự kiện chưa xảy ra (hôm nay 18/10/2026) mà viết thì hiện tại; chấp nhận vì là lịch đã công bố, nếu muốn: "theo lịch VNX".
- [phụ lục] còn 4 chỗ \small trong bảng phụ lục; 8 slide dự phòng.

## Đã đối chiếu v14, khớp
299 mã, 30/9/2026, 23/12, 28/12/2026; TT 57/2021 (2023), 69/2023 (hết 2025), 139/2025 (31/12/2026); bước giá HNX 100 đồng, HOSE 10 đồng dưới 10.000; biên độ ±10%/±7%; 1.140 đồng, 6,14%; QĐ 1193 bài toán 19; NQ 222/2025/QH15; GFCI 40: 67, 71, 117; giai đoạn 6/2009–6/2025, 7/2025–12/2026, 1/2027–12/2028; HNX ngừng niêm yết mới 1/7/2025; ghép tại 30/6/2025; MQI sáu chỉ báo, điểm z, ba chiều trọng số bằng nhau; MDE 0,64/1,24/1,76σ, 0,05/3 một phía, 193 tháng, 1,3 lần, 0,25 log ~ 22% (ghi minh họa); bootstrap AR (ban-dai ch04-3c dòng 71–80: rút phần dư có hoàn lại, p = tỷ lệ thống kê giả từ giá trị thật trở xuống); rổ CS ≤ 30, 20 + 8 cửa sổ, ρ = 5; Holm, p một phía theo từng H; Callaway & Sant'Anna (2021); OSF trước 28/12/2026; sáu chỉ tiêu, ít nhất một WoS Q1/Q2 (v14 [107]); "không do doanh nghiệp chọn" (ban-dai ch04-1 dòng 104); "phản ứng sớm" (ch04-3a dòng 168). Trích dẫn tác giả-năm và APA "&"/"và": đúng. Không có δ = −0,25, Ḡ = 4,66, MQI = 0,3.

## Điểm
- Hiện tại 84 = 100 − 10 (C1, lời không vượt bằng chứng/sai suy luận) − 3 (M1 không nhất quán) − 3 (M2 ký hiệu không nhất quán); M3 ký hiệu chưa định nghĩa tính nhẹ vì μ, σ² có ở phụ lục. Chưa đạt vì còn CRITICAL, MAJOR.
- Bản sửa 95: −1 \small ở phụ lục, −2 phụ lục dư, −2 Shapiro (phần lõi chưa có hình kết quả dự kiến ngoài did.tex). Hết CRITICAL, MAJOR.

## Chưa kiểm được
- Hình did.tex/did.dat mới của main: không xem (không render), không sửa.
- Thời lượng nói thực tế.
