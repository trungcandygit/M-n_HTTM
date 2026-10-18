# Vòng 3, agent rà slide: 68/100 (bản hiện tại) -> 94/100 (bản sửa đã thử)

Bản sửa đầy đủ, đã biên dịch xelatex hai lượt trên bản sao: 0 lỗi, 0 overfull/underfull, 37 trang, mọi tiêu đề 1 dòng, chữ thấp nhất y = 236/255pt (slide kết), không vượt mép phải.
- Tệp sửa: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/build/slides.tex
- Diff so với repo: /tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/slides.diff
- Cách áp: chép tệp sửa đè `latex/slides/slides.tex` (diff lập trên bản hiện tại, đã có caption mới của did.tex). Phần mở đầu chỉ thêm 1 dòng: `\newtheorem{dinhnghia}{Định nghĩa} % [VN]` sau `\usepackage{presentation}`.

Kết quả tối giản (theo 3 góp ý mới): phần chính còn 20 slide nội dung + 4 slide mục; **2 bảng** (GFCI, lực kiểm định), trước là 13; `\al` ≤ 1 mỗi slide (trước có slide 3–4 lần); mọi danh sách là mục cha kết thúc bằng ":" + mục con; dùng đủ •/–/□ (slide lý thuyết) và 1./a./i. (giả thuyết, giai đoạn, bootstrap, bốn năm, kết luận); khung xám chứa công thức chính (MQI, khác biệt kép, Ḡ, mô hình H₁), mỗi khung kèm ≤ 3 gạch đầu dòng; slide hình chỉ có hình + 1 dòng caption; bỏ hết `\small` ở phần chính.

## CRITICAL

C1. [slide 6 cũ, "Khung phân tích"] Bỏ điều kiện "phần lớn quá trình phát triển" của Naeem (2023) (sai sự thật: Bắc Kinh có sàn quốc gia từ 2021) và nêu thay Hà Nội một hướng chuyên môn hóa, trái với khung "Đề tài không chọn hướng thay cho Hà Nội" ở slide 3 [G fact-checker, credible-claims; v14 đoạn 75: "câu hỏi ... là nên chuyên môn hóa vào những thị trường nào"]. Trong bản sửa, slide này gộp vào slide "Ba khối lý thuyết" (xem M2). Nếu chỉ sửa tại chỗ:
```text
CŨ: \item Hàm ý: Bắc Kinh lớn mạnh dù không có sàn cổ phiếu tầm quốc gia (Naeem, 2023) \so Hà Nội chọn chuyên môn hóa: trái phiếu, phái sinh, UPCoM, dữ liệu
MỚI: \item Hàm ý: Bắc Kinh lớn dù phần lớn thời gian không có sàn tầm quốc gia (Naeem, 2023); đề tài cung cấp căn cứ để Hà Nội chọn mảng chuyên môn hóa
```

## MAJOR

M1. [Kế hoạch, bảng rủi ro] Hai dòng trùng ý, cùng một cách xử lý [consistency-checker]. Bản sửa viết lại thành danh sách lồng nhau 1 cột. Nếu chỉ sửa tại chỗ:
```text
CŨ: Dữ liệu sau ngắn, rổ CS ít mã & Dùng mọi tháng có sẵn; rổ 20 mã\\
MỚI: 
```

M2. [Khung phân tích] Ý 1–2 (cơ chế sàn -> chất lượng -> khả năng đầu tư) không có nguồn; người dùng yêu cầu định tính có nguồn [A; v14 đoạn 111: Amihud, 2002; Huang & Stoll, 1996; Kan & Zhou, 2007; Markowitz, 1952]. Bản sửa thay slide 3 và slide 6 cũ bằng một slide "Ba khối lý thuyết nối chất lượng sàn với vị thế của Hà Nội": • Tích tụ (Gehrig; Kindleberger) / – phân vai (Lai) / □ Bắc Kinh (Naeem), □ Luxembourg (Yao); • Vi cấu trúc (Amihud; Huang & Stoll); • Danh mục (Kan & Zhou; Markowitz). Câu "không chọn thay Hà Nội" chuyển vào mục 4 của slide kết. Kan & Zhou (2007) có trong danh mục v14.

M3. [toàn deck] Mật độ vượt mức và lệch kiểu template theo góp ý mới: 13 bảng ở phần chính, `\al` 2–4 lần/slide (slide 1, Ba giai đoạn, Xử lý), ý dài 2–3 dòng, 12 chỗ `\small` (−12 theo I), 22 slide nội dung (> 20) [B; C; góp ý người dùng]. Cách sửa (đã nằm trong tệp sửa, thay nguyên khối frame):
- Slide 1: bảng mốc -> • Đợt chuyển sàn / • Hạn bị lùi hai lần (– TT 57/2021, 69/2023, 139/2025) / • Lịch VNX.
- Giả thuyết: bảng -> 1./a. theo ba câu hỏi; bỏ câu 22% (đã có ở slide lực và kết).
- Đóng góp, Thách thức, Cú sốc trùng, Điểm yếu, Kế hoạch: bảng -> •/– "Đã có / Bổ sung", "thay đổi: hệ quả".
- Ba giai đoạn: bảng -> 1./a. + cột nguồn dữ liệu.
- MQI, Khác biệt kép, Khả năng đầu tư, GFCI: công thức vào khung (MQI, Ḡ, H₁ dùng môi trường `dinhnghia` mới; DiD trong `assumption`), ≤ 3 gạch dưới khung.
- Bootstrap: cột phải thành 1./a. ba bước.
- Bốn năm: bảng -> 1.–4./a.; sáu chỉ tiêu thành danh sách – bên phải.
- Slide "Chuẩn bị" chuyển xuống phụ lục (bảng giữ nguyên ở đó).

M4. [Tác động là khoảng cách, hình] Caption 2 dòng, trái quy tắc "slide hình chỉ có hình + 1 dòng caption"; câu về tác động gộp đã có ở slide Điểm yếu.
```text
CŨ: \caption{Hình minh họa thiết kế, không phải dữ liệu; dải xám: 18 tháng chuyển tiếp, loại khỏi kiểm định chính. $\delta$ đo tác động gộp của sàn: biên độ, bước giá, hệ thống giao dịch, chỉ số.}
MỚI: \caption{Hình minh họa thiết kế, không phải dữ liệu; dải xám: 18 tháng chuyển tiếp, loại khỏi kiểm định chính.}
```

M5. [Phụ lục nghiên cứu sự kiện] $T_{kt}$ dùng mà chưa định nghĩa (−15 theo I) [B; v14 đoạn 176].
```text
CŨ: \item $k$ từ 1/2024 đến 12/2028; tháng gốc 6/2025; trước 1/2024 gộp một nhóm
MỚI: \item $T_{kt} = 1$ nếu tháng $t$ là $k$; $k$ từ 1/2024 đến 12/2028; tháng gốc 6/2025
```
(Ý "trước 1/2024 gộp một nhóm" bỏ để giữ 1 dòng; nếu muốn giữ, thêm thành ý riêng.)

M6. [Phụ lục ba cú sốc] $E_{si}$ chưa định nghĩa.
```text
CŨ: \caption{Tương tác $D_i\Post_tE_{si}$: phân tích phụ
MỚI: \caption{Tương tác $D_i\Post_tE_{si}$, $E_{si}$: mức chịu cú sốc $s$ của mã $i$; phân tích phụ
```

## MINOR

- [MQI] chỉ số $j$, $t$ chưa giải nghĩa -> đã thêm "Với sàn $j$ và tháng $t$" trong khung (tệp sửa).
- [Phụ lục hướng sai lệch] "δ phóng đại", "δ bị đánh giá thấp" dễ hiểu sai dấu vì δ < 0:
```text
CŨ: \so $\delta$ phóng đại
MỚI: \so $|\delta|$ phóng đại
```
```text
CŨ: \so $\delta$ bị đánh giá thấp
MỚI: \so $|\delta|$ bị đánh giá thấp
```
- [Kết luận cũ, ý 5] "chỉ số chất lượng là một cấu phần" khẳng định quá; v14 đoạn 86 viết "có thể là". Bản sửa bỏ ý này.
- [Thách thức cũ] "Mã chịu mạnh nhất" thiếu chữ -> bản sửa bỏ cột (danh sách).
- [GFCI cũ, khung] từ nối "Vì vậy" -> bản sửa: "GFCI đã chứa dữ liệu giao dịch cổ phiếu: β không là tác động nhân quả".
- [`\so` giữa câu, H] còn ở các slide phụ lục (hướng sai lệch, không phân cụm, H₄); phần chính đã đổi thành dấu hai chấm.
- [`$\rightarrow$` trong ô bảng] chỉ còn ở phụ lục ba cú sốc; phần chính đổi thành "từ ... xuống ...".
- [Black–Litterman] gạch nối không nhất quán: phụ lục "Black-Litterman" (gạch ngắn), slide Chuẩn bị "Black--Litterman"; v14 cũng dùng cả hai. Nên thống nhất "Black--Litterman" (tên ghép hai người).
- [Trang đầu] `\date{... ĐHQGHN -- Hà Nội, 2026}`: gạch vừa làm dấu tách -> "ĐHQGHN, Hà Nội, 2026".
- [Phụ lục] 8 slide dự phòng (> 3–5); chấp nhận được vì không trình bày, có thể bỏ "mốc pháp lý" (trùng slide 1).
- [Hà Nội cần thước đo, bản sửa] ý "Trung tâm tài chính, dịch vụ chất lượng cao quốc tế" chiếm 2 dòng trong cột; giữ vì rút nữa sẽ lệch lời bài toán số 19.

## Đã đối chiếu v14, khớp
299 mã, 30/9/2026, 23/12 và 28/12/2026; TT 57/2021, 69/2023, 139/2025 (ký 30/12/2025) và các mốc 2023, hết 2025, 31/12/2026 (KHỚP); QĐ 1193/QĐ-UBND bài toán 19; NQ 222/2025/QH15; GFCI 40: 67, 71, Hà Nội không có, 117; Naeem 17 yếu tố; 0,64/1,24/1,76σ, 0,05/3 một phía, 193 tháng, 1,3 lần, σ = 0,2, 0,25 log ~ 22% (ghi minh họa); 1.140 đồng 6,14%; 7/2023–6/2025; FTSE bốn đợt 9/2026–9/2027; ρ = 5 (3, 10); 30 mã, rổ 20; 20 + 8 cửa sổ; 104 tuần; sáu cửa sổ độc lập; Daw & Hatfield (2018); Amihud và cộng sự (1997); kế hoạch bốn năm; 4 công trình + 8 bản thảo, cập nhật 9/10/2026; OSF trước 28/12/2026; Sở KH&CN Hà Nội. APA trong ngoặc dùng "&", ngoài ngoặc dùng "và": đúng. Thứ tự tên trong ngoặc theo chữ cái: đúng.

## Điểm
- Bản hiện tại 68 = 100 − 10 (C1, quy tắc A) − 10 (M2, quy tắc A) − 12 (`\small` ×12); ký hiệu chưa định nghĩa ở phụ lục tính nhẹ (−0, đã ghi M5–M6). Chưa đạt vì còn CRITICAL và MAJOR.
- Bản sửa 94: −3 ký hiệu không nhất quán (Black-Litterman), −1 phụ lục dùng `\small`, −2 phụ lục dư. Hết CRITICAL và MAJOR -> đạt.

## Chưa kiểm được
- Hình did.tex mới: chưa xem ảnh (không render); text trích ra cho thấy có nhãn trên đường, dải chuyển tiếp và nhãn "Tác động δ".
- Số lần lặp và cách chọn bậc AR của bootstrap: v14 không nêu (chỉ nêu AR(1) trong phần tính lực), nên không thêm lên slide.
- Thời lượng: ước 20 slide × khoảng 1,4 phút; chưa tập nói.
