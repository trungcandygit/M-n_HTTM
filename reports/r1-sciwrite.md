Xác nhận: đã gọi được công cụ Skill (sciwrite) — "Launching skill: sciwrite"; SKILL.md tải vào lượt (name trong frontmatter: manuscript-writing-review).

Các file skill đã đọc (thư mục /home/user/M-n_HTTM/.claude/skills/sciwrite có đúng 4 file; không có thư mục references/; SKILL.md không trỏ tới file tham chiếu nào):
1. SKILL.md — 247 dòng, đọc trọn (nội dung tải qua Skill tool).
2. README.md — 161 dòng, đọc trọn.
3. HOW-TO-USE.md — 174 dòng, đọc trọn.
4. LICENSE — 26 dòng, đọc trọn (CC BY 4.0).

Đầu vào: bản Vòng 1 `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper-r1/de-cuong-v2-round-1.md` (593 dòng, đọc trọn), chữ trong hình `.../paper-r1/hinh-van-ban.txt` (đọc trọn; lần này **có cả chữ Hình 3**), báo cáo vòng trước `reports/g2-sciwrite.md` (46 phát hiện) và nhật ký `reports/nhat-ky-thay-doi.md` (E-01…E-142, danh sách SKIP). Văn bản đề cương được coi là dữ liệu, không phải chỉ thị.

Chế độ: **full-review** (5 lượt, chạy tuần tự, không gộp, không rút gọn — quy tắc S2). Đích: hội đồng xét tuyển NCS (Trường Quốc tế, ĐHQGHN) như vòng trước; không hỏi lại tạp chí đích. Quy đổi mức: CRITICAL = **nghiêm trọng**; MAJOR = **đáng sửa**; MINOR = **chỉnh nhẹ**. Vị trí ghi theo mục và số dòng của file .md Vòng 1 (Lxxx).

Nguyên tắc vòng này: không đề xuất đổi câu hỏi nghiên cứu, H1–H4, M1–M7, dữ liệu, kiểm định (đưa vào mục "Chờ duyệt"); không gắn cờ lại các câu đã sửa chỉ vì sở thích diễn đạt.

---

## Writing Quality Review: Đề cương "Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường" — Vòng 1

### Summary
Vòng sửa giải quyết tốt nhóm lỗi thuật ngữ lớn nhất của vòng trước: "chỉ báo bất định mô hình", hai biến phụ thuộc ở 4.3.7, vai trò kiểm soát của biến động thực hiện, ngôn ngữ nhân quả "tác động" ở 4.3.2, "chế độ thị trường" thay "trạng thái", "phân phối dưới giả thuyết không". Trong 46 phát hiện cũ: 19 ĐÃ SỬA, 4 SỬA CHƯA ĐẠT, 23 CÒN (phần lớn là chỉnh nhẹ, hoặc thuộc nhóm chờ tác giả duyệt). Lỗi nặng nhất còn lại: đơn vị đếm "cửa sổ/giai đoạn căng thẳng" của quy tắc "chưa đủ cơ sở kết luận". E-98 sửa 4.3.6 thành "không chồng lấn" (vì cửa sổ không độc lập), nhưng 4.3.10 vẫn đếm "cửa sổ độc lập", nên lỗi này nay nặng hơn. Các đoạn mới chèn (bài toán 19, HNX) đưa vào một số lỗi mới: lặp gần nguyên văn giữa 4.1 và 4.4, danh sách cấu phần không khớp nhau, danh sách người dùng lệch với danh sách đã "chốt", "chỉ báo" bị dùng cho R_t, và các nhãn [CẦN ĐỐI CHIẾU]/[CẦN XÁC MINH] còn nằm trong văn bản nộp.

---

### Phần A — Đối chiếu 46 phát hiện vòng trước

| # cũ | Trạng thái | Mức hiện tại | Trích bản Vòng 1 / ghi chú |
|---|---|---|---|
| 1.1 | ĐÃ SỬA | — | L121 "vượt quy tắc chia đều vốn cho N tài sản (quy tắc 1/N) nhất quán" (E-06) |
| 1.2 | CÒN | chỉnh nhẹ | L121 "Khi không mô hình nào thắng ổn định, việc chọn mô hình trở thành một quyết định mang rủi ro riêng." → bỏ "việc" |
| 1.3 | CÒN | chỉnh nhẹ | L145 "và việc thay tham số tổng thể bằng ước lượng mẫu làm hiệu quả ngoài mẫu giảm" (E-25 chỉ bỏ "mạnh") → bỏ "việc" |
| 1.4 | CÒN | chỉnh nhẹ | L149 "thu được hiệu quả ngoài mẫu tốt hơn việc dùng tiêu chí để chọn một mô hình" → "tốt hơn cách chọn một mô hình theo tiêu chí" |
| 1.5 | CÒN | chỉnh nhẹ | L305 "Việc nhận diện chế độ tự nó là một dạng rủi ro mô hình" → "Bản thân nhận diện chế độ đã là một dạng rủi ro mô hình" |
| 1.6 | ĐÃ SỬA | — | L399 "trước khi nộp tệp đăng ký trước" (E-132) |
| 1.7 | CÒN | chỉnh nhẹ | L297 "Thí sinh đăng ký trước kế hoạch phân tích trước khi ước lượng chính thức tập mô hình ở bước 3." → "…kế hoạch phân tích, rồi mới ước lượng chính thức…" (nhật ký không ghi lý do bỏ qua) |
| 1.8 | CÒN | chỉnh nhẹ | L405 "Kinh nghiệm chuyên môn của thí sinh chủ yếu là kinh nghiệm nghiên cứu." → "…chủ yếu nằm ở nghiên cứu." |
| 2.1 | ĐÃ SỬA | — | L453 "Thí sinh chuẩn bị cho đề tài qua các công việc nghiên cứu đã làm." (E-137) |
| 2.2 | CÒN | chỉnh nhẹ | L247 "M~3~ dùng nghịch đảo giả Moore--Penrose và kết quả ghi rõ điều này." → "…và luận án ghi rõ điều này khi báo cáo kết quả." |
| 2.3 | CÒN | chỉnh nhẹ | L325 "Thủ tục này suy ra từ H~3~, chưa qua kiểm nghiệm với người dùng, và chỉ là tư liệu tham khảo" (câu này nay còn mâu thuẫn với câu đứng trước, xem M19) |
| 2.4 | ĐÃ SỬA | — | L151 "Bai và Perron (1998) phát triển phương pháp" (E-37) |
| 3.1 | ĐÃ SỬA | — | L123 "một trạng thái thống kê mà mô hình chuyển chế độ ước lượng được, có biến động cao và lợi suất thị trường thấp" (E-11) |
| 3.2 | CÒN | đáng sửa | L405 "Thí sinh chủ nhiệm đề tài nghiên cứu khoa học sinh viên "Nâng cao … Việt Nam", đạt Giải Nhất cấp Khoa…". Nhật ký bỏ qua với lý do "dữ kiện về tác giả". Đổi trật tự câu không đổi dữ kiện, nên vẫn giữ đề xuất của vòng trước. |
| 3.3 | CÒN | đáng sửa (chờ duyệt D8) | L213 "30 mã có giá trị giao dịch bình quân 3 tháng và vốn hóa tự do chuyển nhượng lớn nhất". Quy tắc xếp hạng do tác giả quyết. |
| 3.4 | ĐÃ SỬA | — | L127 tách thành hai câu (E-15) |
| 3.5 | CÒN | chỉnh nhẹ | L453 "Bản thảo về mô hình Black--Litterman nghịch đảo kết hợp học máy phân cụm (bản thảo số 1) giúp thí sinh làm quen với việc so sánh" → "Bản thảo số 1 (…) giúp thí sinh làm quen với so sánh…" |
| 3.6 | ĐÃ SỬA | — | L399 "áp dụng quy tắc đã đăng ký trước để gọi kết quả là chưa đủ cơ sở kết luận" (E-133) |
| 3.7 | CÒN | chỉnh nhẹ | L253 "vì khi lợi suất vượt trội trung bình âm (thường xảy ra ở chế độ căng thẳng) danh mục biến động mạnh hơn lại có…". E-91 chỉ đổi nội dung trong ngoặc, cấu trúc lồng ba tầng giữ nguyên và thiếu dấu phẩy sau ngoặc đóng. Sửa tối thiểu: "…(thường xảy ra ở chế độ căng thẳng), danh mục biến động mạnh hơn…" |
| 3.8 | ĐÃ SỬA | — | L249 "Tệp đăng ký cố định các nội dung sau: độ dài các cửa sổ; …" (E-89) |
| 3.9 | ĐÃ SỬA | — | L291 "Cơ chế (i) là kết hợp mô hình theo trọng số Bayes" (E-108) |
| 3.10 | ĐÃ SỬA | — | L123 tách câu định nghĩa (E-08) |
| 3.11 | CÒN | chỉnh nhẹ | 4.3.7 (L279–287) vẫn có 12 câu hoặc mệnh đề lấy "Đề tài/đề tài" làm chủ ngữ: "Đề tài so sánh…", "Đề tài hiệu chỉnh…", "đề tài hồi quy…", "đề tài hiệu chuẩn…", "Đề tài coi…", "Đề tài lặp lại…", "Đề tài ước lượng…", "Đề tài chỉ báo cáo…", "Đề tài gọi…" |
| 4.1 | ĐÃ SỬA | — | L123 "là chỉ báo bất định mô hình: chúng báo hiệu mức bất định, không đo rủi ro"; L198 "Kết quả phụ (chỉ báo bất định mô hình)"; L269 "Đại lượng thứ ba, dùng như chỉ báo bất định mô hình"; L323 "đề tài đo rủi ro lựa chọn mô hình (mức hối tiếc)"; Hình 1 "Chỉ báo: độ phân tán Dt". Còn biến thể mới, xem M16. |
| 4.2 | ĐÃ SỬA | — | L279 "đề tài hồi quy mức hối tiếc và độ phân tán mô hình theo biến chế độ" |
| 4.3 | ĐÃ SỬA | — | L141 "sau khi kiểm soát biến động thực hiện, gồm thanh khoản…". Lỗi gắn nhầm vế mới phát sinh, xem M9. |
| 4.4 | SỬA CHƯA ĐẠT | đáng sửa | Tên gọi đã thống nhất: "tương quan cực trị" là tên kênh, "tương quan đuôi" là biến đo (L181 "tương quan cực trị, đo bằng tương quan đuôi … và tương quan hiệu chỉnh theo biến động"). Phần còn thiếu: L283 đưa **hai** biến tương quan vào X_t, nhưng tiêu chí H2 (L200, L287) chỉ nói "hệ số của tương quan đuôi âm". Văn bản chưa nói vai trò của "tương quan hiệu chỉnh theo biến động" trong H2. Cần một câu ở L287, ví dụ "Tương quan hiệu chỉnh theo biến động là [biến kiểm soát / biến kiểm tra độ bền], không thuộc tiêu chí H~2~". Tác giả chọn vế nào (chờ duyệt). |
| 4.5 | ĐÃ SỬA | — | L191 "Theo Hình 1, H1 so sánh rủi ro lựa chọn mô hình giữa hai chế độ." (E-68). Hình vẽ vẫn để mũi tên kiểu biến điều tiết, xem M20. |
| 4.6 | CÒN (nặng hơn) | nghiêm trọng | L305 "Kèm mỗi hệ số, đề tài báo cáo số cửa sổ độc lập và số giai đoạn căng thẳng độc lập. Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10…"; L271 "số giai đoạn căng thẳng rơi vào phần mẫu"; L399 "quá ít giai đoạn căng thẳng"; Bảng 5 "số quan sát ở chế độ căng thẳng". Hiện có bốn đơn vị đếm, và E-98 tạo thêm mâu thuẫn trực tiếp (M14). |
| 4.7 | SỬA CHƯA ĐẠT | đáng sửa | 4.3.3 đã sửa (L215 "biến cố thị trường trái phiếu doanh nghiệp"). 4.3.5 còn nguyên: L249 "giai đoạn 2019--2025, gồm hai giai đoạn căng thẳng". Sửa: "gồm hai giai đoạn [mà mô hình chuyển chế độ xếp vào chế độ căng thẳng / có khủng hoảng lịch sử — tác giả xác định]". |
| 4.8 | SỬA CHƯA ĐẠT | đáng sửa | Thân bài và Hình 1 đã dùng "quy tắc chuyển chế độ". Còn hai chỗ: (a) Hình 3, Bước 5: "Kết hợp mô hình, danh mục vững chắc, quy tắc chế độ". Nhật ký ghi V-020 bỏ qua vì "Hình 3 là ảnh", nhưng E-142 đã sửa được chữ trong chính SmartArt này, nên chỗ này sửa được. Đổi thành "quy tắc chuyển chế độ". (b) L291 vẫn chưa gắn cơ chế (ii)/(iii) với M~6~/M~7~, trong khi câu cuối viết "đề tài loại cơ chế (ii) và (iii) khỏi *M*". Sửa: "Cơ chế (ii) là danh mục vững chắc (M~6~) … Cơ chế (iii) là quy tắc chuyển chế độ (M~7~)…", nếu đúng ý tác giả. |
| 4.9 | CÒN | nghiêm trọng (chờ duyệt D6) | L202 "kết hợp mô hình và danh mục vững chắc cho mức hối tiếc và độ sụt giảm tối đa thấp hơn" so với L291 "Đề tài đánh giá ba cơ chế" và L293 "độ sụt giảm tối đa không cao hơn". Tiêu chí của H3 nên chỉ ghi chờ duyệt, không tự sửa. |
| 4.10 | CÒN | đáng sửa | L204 "Độ phân tán chéo của lợi suất; thước đo bầy đàn" → "Độ phân tán chéo của lợi suất (thước đo bầy đàn cấp thị trường)", khớp L319 |
| 4.11 | ĐÃ SỬA | — | Câu "tác động lên chính quan hệ đó" đã bỏ khỏi L191 |
| 4.12 | ĐÃ SỬA | — | L149 "theo từng chế độ thị trường"; L181 "nối hai khối này với chế độ thị trường"; grep không còn "trạng thái thị trường" |
| 4.13 | ĐÃ SỬA | — | Hình 1 "Giá trị thiệt hại kỳ vọng 95%, vòng quay" |
| 4.14 | CÒN | chỉnh nhẹ | L412 "(Nguyễn và Nguyễn, 2026b)" bên cạnh "Nguyen và Nguyen (2026a)". Nhật ký: V-007 để tác giả chọn quy ước. |
| 4.15 | ĐÃ SỬA | — | L249 OSF; L451 VSTEP. Cách định nghĩa OSF có lỗi nhỏ, xem M22. |
| 4.16 | SỬA CHƯA ĐẠT | chỉnh nhẹ | Cách ghi quý đã thống nhất ("quý 4/2022"). Còn L329 "các tiểu mục đến 3 chữ số" so với L336 "(đến ba chữ số)". Nếu tiêu đề theo mẫu của Trường thì sửa ô Bảng 4 thành "3 chữ số". |
| 5.1 | CÒN | nghiêm trọng | Trang bìa: "**- PGS.TS. Hà Hồng Hạnh - Trường Đại học Kinh tế Quốc dân**". L465–467 ghi người hướng dẫn chính là GS.TS. Nguyễn Đức Khương. E-01 chỉ sửa tên trường. Ô "Cơ quan công tác:" và "3. Đơn vị công tác:" vẫn trống. Nhật ký ghi V-001 CHỜ DUYỆT; hội đồng vẫn thấy lỗi này ngay ở trang đầu. |
| 5.2 | CÒN | đáng sửa (chờ duyệt D5) | L305 "Holm (1979) ở mức 10% cho bốn giả thuyết"; L285 "phân vị 95%"; L269 "mức ý nghĩa 10%"; L287 "Đề tài chỉ báo cáo H~4~ như kết quả thăm dò." |
| 5.3 | CÒN | đáng sửa | L175 "Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn" trong khi các số liệu vẫn trình bày như dữ kiện: "151 cuộc khủng hoảng" (L125), "thường trên 2% mỗi năm, có thể tới 10%" (L151), "299 công ty niêm yết" (L155). Cần đối chiếu toàn văn trước khi nộp. |
| 5.4 | ĐÃ SỬA | — | L127 bỏ "lần đầu" (E-15) |
| 5.5 | CÒN | chỉnh nhẹ | L357 "theo Thông báo tuyển sinh năm 2026", "Phụ lục 1 của Thông báo": văn bản này chưa có trong mục 11 |
| 5.6 | CÒN | chỉnh nhẹ (chờ duyệt) | L247 "khi tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5". Với 30/104 ≈ 0,29, điều kiện chỉ kích hoạt ở rổ lớn. |
| 5.7 | CÒN | chỉnh nhẹ (chờ duyệt) | L291 "đề tài loại cơ chế (ii) và (iii) khỏi *M*, nên mức hối tiếc của hai cơ chế này có thể âm". Danh mục kết hợp ở cơ chế (i) cũng không thuộc *M*. |

Tổng phần A: **19 ĐÃ SỬA, 4 SỬA CHƯA ĐẠT, 23 CÒN**. 27 mục chưa xong chia theo mức: **3 nghiêm trọng, 8 đáng sửa, 16 chỉnh nhẹ**.

---

### Phần B — Vấn đề MỚI (theo 5 lượt, chạy tuần tự)

#### Pass 1: Clutter — 4 vấn đề mới

**M1** — 4.1, đoạn 3 (L125) — chỉnh nhẹ (lặp ý, do E-12)
- Gốc: "Khủng hoảng lặp lại thường xuyên, nên câu hỏi thứ hạng mô hình có thay đổi khi thị trường căng thẳng hay không có ý nghĩa thực tiễn. Khủng hoảng tài chính lặp lại qua nhiều thế kỷ (Reinhart và Rogoff, 2009)…"
- Sửa: "Khủng hoảng tài chính lặp lại qua nhiều thế kỷ (Reinhart và Rogoff, 2009), và Laeven và Valencia (2020) ghi nhận 151 cuộc khủng hoảng ngân hàng hệ thống trong giai đoạn 1970–2017; vì vậy, câu hỏi thứ hạng mô hình có thay đổi khi thị trường ở chế độ căng thẳng hay không có ý nghĩa thực tiễn."
- Lý do: "lặp lại" xuất hiện ở hai câu liền nhau. "khi thị trường căng thẳng" làm mờ phân biệt "khủng hoảng" với "chế độ căng thẳng" mà 4.1 vừa đặt ra.

**M2** — 4.2 (2), (3), (4), (6) và đoạn sau Bảng 1 — chỉnh nhẹ (rào đón lặp)
- Gốc: L147 "Trong phạm vi tìm kiếm mô tả ở cuối mục 4.2, thí sinh chưa tìm thấy nghiên cứu…"; L149 "song trong phạm vi tìm kiếm đó, thí sinh chưa tìm thấy công trình nào…"; L151 "trong phạm vi tìm kiếm đó, thí sinh chưa tìm thấy nghiên cứu nào…"; L155 "thí sinh chưa tìm thấy công trình đo tổn thất…"; L175 "Theo hiểu biết của thí sinh, chưa có nghiên cứu nào…".
- Sửa: giữ rào đón đầy đủ ở L147 và L175. Ở L149, L151, L155 rút còn "chưa thấy công trình nào … (trong cùng phạm vi tìm kiếm)", hoặc chỉ giữ phần nội dung khoảng trống.
- Lý do: cùng một rào đón lặp năm lần trong một mục là clutter. Ý rào đón (V-045) vẫn giữ nguyên, chỉ bớt lặp. Chữ "đó" ở L151 cũng đã cách xa cụm mà nó thay thế.

**M3** — Mục 5 (L357) — chỉnh nhẹ (do E-128)
- Gốc: "chương trình giảng dạy bằng tiếng Anh hoặc tiếng Việt; việc học bằng tiếng Anh thuận lợi cho công bố quốc tế"
- Sửa: "chương trình giảng dạy bằng tiếng Anh hoặc tiếng Việt; học bằng tiếng Anh thuận lợi cho công bố quốc tế"
- Lý do: lớp danh hóa "việc + V", cùng loại với 1.2–1.4.

**M4** — 4.3.5 (L249) và 4.3.3 (L215) — chỉnh nhẹ (do E-90, E-78)
- Gốc: "Tệp đăng ký cũng ghi kiểm tra độ bền trên cổ phiếu HNX (mục 4.3.3) là một phân tích phụ đăng ký trước"; "lặp lại phân tích chính trên cổ phiếu niêm yết trên Sở Giao dịch Chứng khoán Hà Nội (HNX)"
- Sửa: "Tệp đăng ký cũng xếp kiểm tra độ bền trên cổ phiếu HNX (mục 4.3.3) vào nhóm phân tích phụ"; "lặp lại phân tích chính với cổ phiếu niêm yết trên Sở Giao dịch Chứng khoán Hà Nội (HNX)"
- Lý do: "đăng ký … đăng ký trước" lặp trong cùng một câu; "trên … trên" lặp giới từ.

#### Pass 2: Voice and Verbs — 2 vấn đề mới

**M5** — 4.1, câu 1 (L121) — chỉnh nhẹ (do E-02)
- Gốc: "mức độ sử dụng ở các công ty quản lý quỹ Việt Nam sẽ được xác định ở năm thứ nhất."
- Sửa: "thí sinh sẽ xác định mức độ sử dụng ở các công ty quản lý quỹ Việt Nam trong năm thứ nhất (xem đoạn 3)."
- Lý do: câu bị động ẩn chủ thể. Ở L127 chính việc này đã được gán cho "thí sinh sẽ xác định…", nên câu chủ động có kèm tham chiếu thì nhất quán và không phải nói lại hai lần.

**M6** — 4.3.3 (L215) — đáng sửa (do E-78)
- Gốc: "Kết quả trên HNX là phân tích phụ đã đăng ký trước và không thay đổi kết luận về H1--H4."
- Sửa: "Kết quả trên HNX là phân tích phụ đã đăng ký trước; đề tài không dùng kết quả này để thay đổi kết luận về H~1~–H~4~."
- Lý do: câu gốc có thể đọc thành lời dự báo về kết quả ("kết quả HNX sẽ không làm đổi kết luận"), một điều chưa biết khi chưa có dữ liệu. Đưa chủ thể "đề tài" vào thì câu trở thành quy tắc mà tác giả cam kết. Ý định (phương án B của người dùng) giữ nguyên.

#### Pass 3: Sentence Architecture — 6 vấn đề mới

**M7** — 4.3.1, câu cuối (L181) — đáng sửa (do E-57)
- Gốc: "Các biến kênh lấy từ tài liệu về thanh khoản (Amihud, 2002), tương quan cực trị, đo bằng tương quan đuôi (tương quan của lợi suất ở vùng đuôi phân phối) và tương quan hiệu chỉnh theo biến động (Longin và Solnik, 2001; Forbes và Rigobon, 2002) và bầy đàn (Christie và Huang, 1995; Chang và cộng sự, 2000)."
- Sửa: "Các biến kênh lấy từ ba nhóm tài liệu: thanh khoản (Amihud, 2002); tương quan cực trị (Longin và Solnik, 2001; Forbes và Rigobon, 2002), đo bằng tương quan đuôi, tức tương quan của lợi suất ở vùng đuôi phân phối, và tương quan hiệu chỉnh theo biến động; và bầy đàn (Christie và Huang, 1995; Chang và cộng sự, 2000)."
- Lý do: danh sách ba kênh lồng thêm một danh sách hai biến, dùng hai chữ "và" cùng cấp và hai lớp ngoặc. Người đọc khó biết "bầy đàn" là kênh thứ ba hay biến đo thứ ba. SKILL.md khuyên dùng dấu hai chấm và chấm phẩy cho trường hợp này.

**M8** — 4.1, mục tiêu (iii) (L141) — chỉnh nhẹ (do E-22)
- Gốc: "(iii) xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, sau khi kiểm soát biến động thực hiện, gồm thanh khoản, tương quan cực trị và, ở mức thăm dò, bầy đàn;"
- Sửa: "(iii) sau khi kiểm soát biến động thực hiện, xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm thanh khoản, tương quan cực trị và, ở mức thăm dò, bầy đàn;"
- Lý do: "gồm …" đứng ngay sau "biến động thực hiện", nên có thể đọc thành biến động thực hiện gồm thanh khoản… Đưa trạng ngữ lên đầu mệnh đề, như cách Câu hỏi 2 (L137) đang viết.

**M9** — Mục 6, đoạn 2 (L363) — chỉnh nhẹ (do E-130)
- Gốc: "Công ty quản lý quỹ có dùng mô hình định lượng có thể cần một thủ tục giám sát mô hình có căn cứ thực nghiệm."
- Sửa: "Những công ty quản lý quỹ dùng mô hình định lượng có thể cần một thủ tục giám sát mô hình có căn cứ thực nghiệm."
- Lý do: ba chữ "có" mang ba nghĩa khác nhau trong một câu ngắn, khiến người đọc phải tìm vị ngữ.

**M10** — 4.3.7, đoạn 3 (L287) — chỉnh nhẹ (câu cũ, vòng trước bỏ sót)
- Gốc: "Đề tài ước lượng phần chênh lệch giữa hai chế độ do các biến kênh giải thích bằng hiệu $\beta_{0} - \beta_{1}$"
- Sửa: "Phần chênh lệch giữa hai chế độ mà các biến kênh giải thích được ước lượng bằng hiệu $\beta_{0} - \beta_{1}$"
- Lý do: "do các biến kênh giải thích bằng hiệu" có thể đọc thành "các biến kênh giải thích bằng hiệu". Dùng bị động ở đây hợp lệ (SKILL.md: nhấn vào đối tượng), và câu cũng bớt một chủ ngữ "Đề tài" (xem 3.11).

**M11** — 4.2 (2) (L147) — chỉnh nhẹ (do E-32)
- Gốc: "Avramov (2002) và Garlappi và cộng sự (2007) xử lý bất định mô hình trong phân bổ bằng kết hợp mô hình hoặc tối ưu hóa vững chắc"
- Sửa: "Avramov (2002) cùng Garlappi và cộng sự (2007) xử lý bất định mô hình trong phân bổ, lần lượt bằng kết hợp mô hình và tối ưu hóa vững chắc"
- Lý do: hai chữ "và" cùng cấp khiến ranh giới giữa hai nhóm tác giả không rõ. "lần lượt" cho biết mỗi nguồn gắn với cách tiếp cận nào; nếu tác giả không muốn khẳng định cách ghép này thì chỉ đổi "và" đầu thành "cùng".

**M12** — 4.3.10 (L305) — đáng sửa (do E-112)
- Gốc: "Đề tài không diễn giải việc không bác bỏ là bằng chứng rủi ro lựa chọn mô hình không đổi."
- Sửa: "Đề tài không diễn giải việc thiếu bằng chứng ủng hộ H~1~ là bằng chứng rằng rủi ro lựa chọn mô hình không đổi theo chế độ."
- Lý do: câu gốc không nói rõ "không bác bỏ" giả thuyết nào. Ngay trước đó văn bản dùng "ủng hộ hay bác bỏ" cho H1–H4, nên người đọc có thể hiểu "không bác bỏ H1", nghĩa ngược với ý tác giả. Câu cũng có hai phủ định lồng nhau.

#### Pass 4: Terminology — 11 vấn đề mới

**M13** — 4.3.10 (L305) so với 4.3.6 (L271) — **nghiêm trọng** (do E-98)
- Gốc: L271 "đề tài dự kiến có khoảng 28 cửa sổ đánh giá không chồng lấn". E-98 ghi lý do sửa: "Cửa sổ không chồng lấn nhưng không độc lập". Trong khi đó L305 viết: "đề tài báo cáo số cửa sổ độc lập và số giai đoạn căng thẳng độc lập. Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là chưa đủ cơ sở kết luận".
- Sửa (cần tác giả xác nhận, vì đây là đơn vị của một quy tắc đã đăng ký trước): dùng một tên duy nhất ở cả hai nơi. Ví dụ "cửa sổ căng thẳng không chồng lấn", định nghĩa ở 4.3.6 bằng ngưỡng S~t~ do tác giả chọn. L305 khi đó sửa thành "…báo cáo số cửa sổ không chồng lấn và số giai đoạn căng thẳng tách biệt. Khi số cửa sổ căng thẳng không chồng lấn dưới 10…". Đồng bộ thêm L131 ("giai đoạn căng thẳng độc lập"), L399 và Bảng 5 ("số quan sát ở chế độ căng thẳng").
- Lý do: văn bản vừa nói các cửa sổ không độc lập, vừa dùng "cửa sổ độc lập" làm đơn vị của quy tắc ra quyết định. Mâu thuẫn này do bản sửa tạo ra và làm 4.6 nặng thêm. Ngưỡng 10 và quy tắc thuộc nhóm chờ duyệt (D2).

**M14** — Đoạn bài toán 19 ở 4.1 (L129) so với đoạn ở 4.4 (L327) — đáng sửa (do E-18, E-125)
- Gốc: L129 "Cấu phần này gồm thước đo mức hối tiếc, thủ tục giám sát mô hình ba bước, mã nguồn công khai và tệp đăng ký trước." So với L327: "ở ba điểm … Điểm thứ hai là bằng chứng về các biến thị trường có liên hệ thống kê với rủi ro này. … Ba sản phẩm này là cấu phần phương pháp mà các nền tảng công nghệ phục vụ phân bổ vốn định lượng và giám sát thị trường có thể tích hợp". Câu "cấu phần phương pháp … mà các nền tảng công nghệ phục vụ phân bổ vốn định lượng và giám sát thị trường có thể tích hợp" xuất hiện gần nguyên văn ở cả hai đoạn.
- Sửa: (a) Thống nhất thành phần của "cấu phần phương pháp". Ở 4.4 viết: "Điểm thứ nhất và điểm thứ ba là cấu phần phương pháp mà … có thể tích hợp; điểm thứ hai là bằng chứng thực nghiệm phục vụ các cấu phần này". (b) Ở 4.1 chỉ nêu liên hệ và giới hạn phạm vi, rồi trỏ sang 4.4: "Phần đóng góp cho câu hỏi số 3 là một cấu phần phương pháp dùng lại được (mục 4.4)". Có thể bỏ câu liệt kê ở L129.
- Lý do: theo quy tắc Banana, cùng một tên "cấu phần phương pháp" đang chỉ hai tập hợp khác nhau (bốn mục, rồi ba "sản phẩm" có cả "bằng chứng"). Bằng chứng thực nghiệm không phải thứ một nền tảng "tích hợp" được. Câu lặp nguyên văn là clutter.

**M15** — 4.4 (L325, L327) — đáng sửa (do E-123, E-125)
- Gốc: L327 "Điểm thứ nhất là mức hối tiếc, một thước đo định lượng của rủi ro lựa chọn mô hình theo chế độ thị trường, dùng được làm chỉ báo giám sát." L325 "Thủ tục dùng độ phân tán và tập tin cậy mô hình như chỉ báo cảnh báo bất định".
- Sửa: L327 "…dùng được trong giám sát mô hình." L325 "…như chỉ báo bất định mô hình".
- Lý do: E-10 dành nhãn "chỉ báo" cho D_t và tập tin cậy ("chỉ báo bất định mô hình: chúng báo hiệu mức bất định, không đo rủi ro"). Gọi R_t là "chỉ báo" làm mờ đúng ranh giới mà bản sửa vừa dựng. "chỉ báo cảnh báo bất định" lại là biến thể thứ ba của cùng một nhãn.

**M16** — 4.1, đoạn 4 (L127) so với đoạn bài toán 19 (L129) — đáng sửa (do E-16, E-18)
- Gốc: L127 "người dùng kết quả của đề tài là công ty quản lý quỹ, các tổ chức đầu tư cổ phiếu khác và cơ quan giám sát thị trường chứng khoán" (nhật ký E-16: "Chốt một danh sách người dùng kết quả, dùng lại ở mục 6"). L129 "Một nhóm người dùng dự kiến … gồm Ủy ban Chứng khoán Nhà nước, Sở Giao dịch Chứng khoán Việt Nam, Sở Giao dịch Chứng khoán Hà Nội, Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam và các công ty quản lý quỹ…"
- Sửa (tác giả chọn, vì danh sách người dùng là quyết định USER-A): (a) mở rộng danh sách đã chốt ở L127 và mục 6 thành "…cơ quan quản lý, giám sát và các tổ chức hạ tầng thị trường chứng khoán"; hoặc (b) ở L129 phân nhóm rõ: "gồm cơ quan giám sát (Ủy ban Chứng khoán Nhà nước), các tổ chức hạ tầng thị trường (…) và các công ty quản lý quỹ…".
- Lý do: hai sở giao dịch và Tổng công ty Lưu ký không phải "cơ quan giám sát" hay "tổ chức đầu tư". Danh sách ở L129 vì thế đưa vào nhóm người dùng thứ tư mà danh sách "đã chốt" không có.

**M17** — 4.3.1 (L181) so với 4.4 (L325) — đáng sửa (do E-54 và E-121)
- Gốc: L181 "Mức hối tiếc, tức tổn thất của một lựa chọn so với lựa chọn tốt nhất nhìn lại sau thực tế trong tập mô hình cạnh tranh, là định nghĩa do đề tài đặt ra để đo rủi ro lựa chọn mô hình." So với L325: "đề tài đề xuất cách vận dụng mức hối tiếc để đo rủi ro lựa chọn mô hình" (nhật ký E-121: "Mức hối tiếc là khái niệm chuẩn").
- Sửa L181: "Đề tài vận dụng mức hối tiếc, tức tổn thất của một lựa chọn so với lựa chọn tốt nhất nhìn lại sau thực tế trong tập mô hình cạnh tranh, làm thước đo rủi ro lựa chọn mô hình."
- Lý do: một chỗ nói đề tài *đặt ra* định nghĩa, chỗ kia nói đề tài *vận dụng* một khái niệm có sẵn. Hai cách nói này tạo ra hai mức tuyên bố đóng góp khác nhau, và hội đồng sẽ hỏi cách nào đúng. Câu sửa cũng dùng động từ thay cho danh hóa "là định nghĩa do … đặt ra".

**M18** — 4.4, đoạn "Nếu dữ liệu ủng hộ…" (L325) — đáng sửa (do E-123)
- Gốc: "quy tắc kích hoạt theo chế độ chưa được kiểm định trực tiếp trong H3. Thủ tục này suy ra từ H~3~, chưa qua kiểm nghiệm với người dùng"
- Sửa: "…quy tắc kích hoạt theo chế độ chưa được kiểm định trực tiếp trong H~3~. Thí sinh suy ra phần kết hợp mô hình của thủ tục từ kết quả H~3~; thủ tục chưa qua kiểm nghiệm với người dùng…". Câu này đồng thời xử lý 2.3.
- Lý do: hai câu liền nhau vừa nói H3 không kiểm định quy tắc kích hoạt, vừa nói cả thủ tục "suy ra từ H3". Câu sửa chỉ rõ phần nào của thủ tục dựa trên H3.

**M19** — Hình 1 (hinh-van-ban.txt) so với L191 và L287 — đáng sửa (đồ họa; V-118 bỏ qua)
- Gốc: "Mũi tên: … H2, H4 (biến kênh → mũi tên H1); H3 (cơ chế → mũi tên rủi ro → kết quả, nét đứt)".
- Sửa: vẽ H2/H4 thành mũi tên từ "Biến kênh" vào khối "Rủi ro lựa chọn mô hình", không cắm vào mũi tên H1. Nếu giữ hình hiện tại thì thêm chú giải: "Mũi tên cắm vào mũi tên H1 biểu thị phân rã β~0~ − β~1~, không phải tác động điều tiết."
- Lý do: mũi tên cắm vào một mũi tên khác là ký hiệu chuẩn của biến điều tiết. Phần chữ đã sửa sang "liên hệ thống kê" và "phép phân rã thống kê" (L287), nên hình nay nói khác chữ. Đây chính là lỗi 4.11 của vòng trước, chỉ chuyển từ chữ sang hình.

**M20** — Ký hiệu chỉ số dưới trong các câu mới — chỉnh nhẹ (do E-68, E-74, E-85, E-95, E-113, E-123, E-127)
- Gốc: L191 "H1 so sánh…", "H2 và H4 xét…", "H3 so sánh…"; L209 "H3 trả lời câu hỏi 3" (cùng câu với "H~1~", "H~2~"); L245 "khi không có M5"; L269 "tương đối với tập M" (không in nghiêng, trong khi cùng mục viết "*M*"); L307 "M5 cần phương pháp Bayes xấp xỉ"; L325 "trong H3"; L357 "(H4)".
- Sửa: "H~1~…H~4~", "M~5~", "*M*", như phần còn lại của văn bản.
- Lý do: ký hiệu không thống nhất khiến người đọc phải tự hỏi "M" và "*M*", "H3" và "H~3~" có phải cùng một đối tượng không.

**M21** — 4.3.5 (L249) — chỉnh nhẹ (do E-87)
- Gốc: "trên nền tảng OSF Registries của Open Science Framework (OSF)"
- Sửa: "trên nền tảng OSF Registries của Open Science Framework"
- Lý do: viết tắt "OSF" được định nghĩa sau khi đã dùng (ngay trong "OSF Registries"), và không xuất hiện lại ở chỗ nào khác (grep). SKILL.md yêu cầu tránh tạo viết tắt chỉ để tiện cho người viết.

**M22** — Bảng 4, dòng "Kết luận" (L350) so với 4.4 (L321) — chỉnh nhẹ (lệch do E-117)
- Gốc: "hạn chế (số giai đoạn căng thẳng, phạm vi Việt Nam)" so với L321 "kết luận chỉ áp dụng cho danh mục chỉ mua gồm các cổ phiếu thanh khoản cao trên HOSE, với tập bảy mô hình và quy tắc chọn mô hình đã đăng ký trước."
- Sửa: "hạn chế (số giai đoạn căng thẳng; phạm vi: danh mục chỉ mua, cổ phiếu thanh khoản cao trên HOSE, tập bảy mô hình)"
- Lý do: E-117 đã thu hẹp phạm vi khái quát nhưng Bảng 4 vẫn ghi phạm vi cũ.

**M23** — Hình 2 (hinh-van-ban.txt) so với 4.3.6 (L265) — chỉnh nhẹ
- Gốc: Hình 2: "chọn trước mô hình c có lợi suất tương đương chắc chắn cao nhất trong 36 tháng trước". L265: "có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước".
- Sửa chú thích Hình 2: "…lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước…"
- Lý do: thiếu "ngoài mẫu" khiến quy tắc chọn trong hình có thể bị hiểu là chọn theo kết quả trong mẫu.

#### Pass 5: Numbers and Citations — 1 vấn đề mới

**M24** — 4.1 (L129) và 4.4 (L327) — đáng sửa (do E-18, E-125; bắt buộc xử lý trước khi nộp)
- Gốc: "Quyết định số 1193/QĐ-UBND ngày 18/3/2026 của Ủy ban nhân dân thành phố Hà Nội \[CẦN ĐỐI CHIẾU bản chính thức\]"; "…các công ty quản lý quỹ có trụ sở chính tại Hà Nội \[CẦN XÁC MINH\]"; "sản phẩm "Hệ thống dữ liệu tài chính đô thị" của bài toán số 19".
- Sửa: (a) đối chiếu QĐ 1193 với bản chính thức (số hiệu, ngày, tên bài toán, nguyên văn câu hỏi số 3, tên sản phẩm), sau đó xóa các nhãn trong ngoặc vuông; (b) thêm QĐ 1193 vào mục 11. Nhật ký V-011 để việc này cho tác giả. (c) Xác minh trụ sở của từng tổ chức được liệt kê.
- Lý do: các câu trích nguyên văn một văn bản hành chính hiện chưa có nguồn trong danh mục. Nếu nộp nguyên trạng, hội đồng sẽ thấy các nhãn làm việc nội bộ. Phần đối chiếu số liệu thiết kế không phát hiện con số mới nào lệch (xem dòng "Đã kiểm" bên dưới).

Đã kiểm ở Pass 5 và thấy khớp: |M| = 7; 28 cửa sổ; 104 tuần, 6 tháng, 36 tháng (4.3.6, Hình 2, ghi chú Bảng 3); 9 tín chỉ (mục 5, 7.1, Bảng 5); chín bản thảo, trong đó ba bản liên quan (Bảng 7 và 8.2); "K1–K4" khớp "bốn khoảng trống" (L157, L185); năm bước của Hình 3 khớp năm bước ở 4.3.9, và "Đăng ký trước" trong Bước 3 khớp L297; mốc 30/09/2026 (L175, ghi chú Bảng 6, tên Bảng 7); "1.000 lần tái lấy mẫu", "ngưỡng 5", ρ = 5 (3 và 10). Các nguồn được nhắc trong câu mới (Kan và Zhou 2007, Tu 2010, Avramov 2002, Garlappi và cộng sự 2007) đều có trong mục 11.

---

### Top 5 Priority Revisions
1. **Thống nhất đơn vị đếm của quy tắc "chưa đủ cơ sở kết luận"** (M13 và 4.6). Bỏ "cửa sổ độc lập" vì đã mâu thuẫn với "không chồng lấn"; dùng một tên được định nghĩa bằng ngưỡng S~t~. Ngưỡng do tác giả chọn (D2).
2. **Sửa trang bìa cho khớp mục 10** (5.1): ghi đủ hai người hướng dẫn và điền hoặc ghi "Không" cho ô cơ quan/đơn vị công tác.
3. **Gỡ các nhãn [CẦN ĐỐI CHIẾU]/[CẦN XÁC MINH] sau khi đối chiếu, và thêm QĐ 1193 vào danh mục** (M24).
4. **Làm gọn hai đoạn bài toán 19** (M14, M15, M16): một định nghĩa "cấu phần phương pháp", không lặp nguyên văn, không gọi R~t~ là "chỉ báo", danh sách người dùng khớp danh sách đã chốt.
5. **Đồng bộ các tuyên bố còn lệch nhau**: "đặt ra định nghĩa" và "vận dụng" mức hối tiếc (M17); "suy ra từ H3" và "chưa kiểm định trong H3" (M18); mũi tên Hình 1 (M19); "quy tắc chế độ" ở Hình 3 và ánh xạ (ii)/(iii) sang M~6~/M~7~ (4.8).

---

### Chờ duyệt (chạm câu hỏi, H1–H4, M1–M7, dữ liệu, kiểm định — chỉ nêu, không đề xuất sửa)
- **D1. Công suất.** Có khoảng 28 cửa sổ không chồng lấn, trong khi quy tắc cần ít nhất 10 cửa sổ căng thẳng. Khả năng rơi vào "chưa đủ cơ sở kết luận" ngay từ thiết kế vẫn như vòng trước.
- **D2. Ngưỡng S~t~ để xếp một cửa sổ vào nhóm căng thẳng, và đơn vị đếm của quy tắc** (M13). Tệp đăng ký (L249) mới chỉ có "ngưỡng xác suất lọc" ở cấp ngày.
- **D3. Chiều của H4.** L204 viết "độ phân tán chéo của lợi suất cao đi cùng rủi ro lựa chọn mô hình cao", và L319 gọi độ phân tán là "một thước đo bầy đàn". Theo Christie và Huang (1995), bầy đàn ứng với độ phân tán *thấp*.
- **D4. β~0~ không có X~t~ nên cũng không kiểm soát biến động thực hiện.** E-107 đã thêm câu giới hạn diễn giải, nhưng Câu hỏi 2 ("Sau khi kiểm soát biến động thực hiện … giải thích được bao nhiêu phần") vẫn chưa khớp với cách đặc tả β~0~.
- **D5. Họ so sánh bội và các ngưỡng** (5.2).
- **D6. H3:** số cơ chế (Bảng 2 nêu 2, 4.3.8 nêu 3) và điều kiện "thấp hơn" hay "không cao hơn" cho độ sụt giảm tối đa (4.9). Câu mới L325 "quy tắc kích hoạt theo chế độ chưa được kiểm định trực tiếp trong H3" cũng cần khớp với việc 4.3.8 có đánh giá cơ chế (iii).
- **D7. Tiếp xúc dữ liệu trước khi đăng ký.** Bảng 5, Quý 2 năm 1: "ước lượng thử bảy mô hình trên giai đoạn 2019--2025 để đo … số quan sát ở chế độ căng thẳng".
- **D8. Quy tắc chọn rổ 30 mã** (3.3), và cách xác định "tập cổ phiếu thanh khoản cao … theo cùng cách" cho HNX (L215).
- **D9 (mới).** Tiêu chí H1 (L285) đòi "β của D~t~ cùng dấu", tức dùng một chỉ báo bất định (theo L123 là "không đo rủi ro") làm điều kiện chấp nhận một giả thuyết về rủi ro. Tác giả cần xác nhận đây là chủ ý.
- **D10.** Vai trò của "tương quan hiệu chỉnh theo biến động" trong H2 (4.4); mức hối tiếc âm của cơ chế (i) (5.7); điều kiện 0,5 của M~3~ (5.6).

---

## Ghi chú áp dụng cho tiếng Việt (quy tắc gốc viết cho tiếng Anh)
1. **Bảng cụm từ thừa (Pass 1):** các cụm tiếng Anh ("Due to the fact that", "In order to"…) không có trong văn bản tiếng Việt. Đã thay bằng các mẫu thừa tương đương: "việc/sự + V" ở đầu chủ ngữ, lặp từ trong câu ("đăng ký … đăng ký trước", "trên … trên"), lặp ý giữa hai câu liền nhau, và rào đón lặp.
2. **Cụm mở đầu thừa:** đã grep các dạng "Cần nhấn mạnh", "Đáng chú ý", "Như đã biết", "Có thể thấy" trong bản Vòng 1, kết quả 0. "Theo hiểu biết của thí sinh" (L175) là rào đón cần thiết nên giữ.
3. **Bị động "to-be + past participle" (Pass 2):** tiếng Việt không chia động từ. Đã nhận diện bị động qua "được/bị" và qua bị động ý niệm, và loại các chữ "được" mang nghĩa khả năng ("ước lượng được", "tính được").
4. **Mặc định chủ thể "We":** không áp dụng. Giữ quy ước "đề tài/thí sinh/luận án"; chỉ gán "thí sinh" hoặc "đề tài" khi câu bị động che chủ thể (M5, M6).
5. **Danh hóa "noun + of":** thay bằng các mẫu "việc/sự + V" và "là định nghĩa do … đặt ra" (M17).
6. **Ngưỡng ~12 từ cho vị ngữ bị chôn:** đếm theo từ (khoảng 18 tiếng). Đã áp dụng cho 3.2 (còn) và M10.
7. **Acronym ở Abstract/thân bài/chú thích:** đề cương không có Tóm tắt nên vế "Abstract" không áp dụng. Đã kiểm thân bài và chú thích hình, bảng (OSF, VSTEP, HNX, VN100, ARIMA).
8. **Dấu gạch ngang (—):** văn học thuật tiếng Việt ít dùng, nên vòng này chỉ đề xuất dấu hai chấm và chấm phẩy (M7).
9. **"N ở Abstract khớp Table 1":** đề cương chưa có kết quả, nên đã thay bằng đối chiếu các con số thiết kế giữa các mục, bảng và hình.

---

## Bằng chứng tuân thủ

| # | Bước theo thứ tự trong SKILL.md | Trạng thái | Lý do / trích từ đề cương Vòng 1 |
|---|---|---|---|
| 1 | Review Modes: xác định chế độ | LÀM: full-review | Nhiệm vụ yêu cầu chạy đủ 5 lượt trên toàn văn, từ "Nhiều tổ chức đầu tư dùng mô hình thống kê…" (L121) đến "*Hà Nội, ngày 30 tháng 9 năm 2026*" (L587), cộng trang bìa và chữ trong Hình 1–3 |
| 2 | Pass 1: bảng cụm từ thừa | LÀM (bản tiếng Việt, mục 1 phần Ghi chú) | "việc học bằng tiếng Anh thuận lợi" (M3); 1.2–1.5 còn "việc chọn mô hình trở thành" |
| 3 | Pass 1: cụm mở đầu thừa | LÀM, không thấy | grep 0 kết quả; giữ "Theo hiểu biết của thí sinh" |
| 4 | Pass 1: redundancy | LÀM | "Khủng hoảng lặp lại thường xuyên … Khủng hoảng tài chính lặp lại qua nhiều thế kỷ" (M1); "Tệp đăng ký cũng ghi … là một phân tích phụ đăng ký trước" (M4) |
| 5 | Pass 2: quy trình bị động → chủ động (tìm mẫu, xác định chủ thể, dựng lại S–V–O) | LÀM | "mức độ sử dụng … sẽ được xác định ở năm thứ nhất" → "thí sinh sẽ xác định…" (M5); "và không thay đổi kết luận về H1--H4" (M6) |
| 6 | Pass 2: danh hóa / động từ bị chôn | LÀM | "là định nghĩa do đề tài đặt ra để đo" → "Đề tài vận dụng … làm thước đo" (M17) |
| 7 | Pass 2: khi nào chấp nhận bị động (không chuyển máy móc) | LÀM | Giữ "Mức hối tiếc được định nghĩa tương đối với tập M" (L269); đề xuất bị động ở M10 để nhấn đối tượng |
| 8 | Pass 3: vị ngữ bị chôn | LÀM | 3.2 còn: "Thí sinh chủ nhiệm đề tài nghiên cứu khoa học sinh viên "Nâng cao…", đạt Giải Nhất" |
| 9 | Pass 3: dấu câu (hai chấm, gạch ngang, chấm phẩy) | LÀM | "Các biến kênh lấy từ tài liệu về thanh khoản (Amihud, 2002), tương quan cực trị, đo bằng … và … và bầy đàn" (M7) |
| 10 | Pass 3: biến thiên độ dài câu | LÀM | 3.11 còn: chuỗi câu "Đề tài …" ở 4.3.7; đoạn "Đóng góp dự kiến" giữ phép song song có chủ đích |
| 11 | Pass 4: Banana Rule | LÀM | "dùng được làm chỉ báo giám sát" cho R~t~ (M15); "quy tắc chế độ" ở Hình 3 (4.8) |
| 12 | Pass 4: keyword audit bước 1 (trích thuật ngữ từ Phương pháp) | LÀM | Từ 4.3: "mức hối tiếc", "chỉ báo bất định mô hình", "cửa sổ đánh giá không chồng lấn", "tương quan đuôi", "tương quan hiệu chỉnh theo biến động", "quy tắc chuyển chế độ", "chưa đủ cơ sở kết luận", "cấu phần phương pháp" |
| 13 | Pass 4: bước 2 (đối chiếu sang các mục khác, Bảng, Hình) | LÀM, gồm cả Hình 3 (lần này đã có chữ) | Hình 3: "Kết hợp mô hình, danh mục vững chắc, quy tắc chế độ"; Hình 2: "cao nhất trong 36 tháng trước" (M23) |
| 14 | Pass 4: bước 3 (gắn cờ từ đồng nghĩa) | LÀM | "số cửa sổ độc lập" so với "cửa sổ đánh giá không chồng lấn" (M13) |
| 15 | Pass 4: acronym austerity | LÀM (vế Abstract không áp dụng, xem Ghi chú mục 7) | "OSF Registries của Open Science Framework (OSF)" (M21); VSTEP và HNX đã có định nghĩa |
| 16 | Pass 5: N ở Abstract khớp Bảng 1 | CHƯA LÀM nguyên văn: đề cương không có Tóm tắt hay kết quả. Đã thay bằng đối chiếu số liệu thiết kế | "khoảng 28 cửa sổ đánh giá không chồng lấn" đối chiếu với 104 tuần, 36 tháng, 2007–2026 |
| 17 | Pass 5: % khớp số thô | LÀM (trên số có trong văn bản) | "chín bản thảo … trong đó ba bản thảo liên quan" khớp cột "Có" của Bảng 7 |
| 18 | Pass 5: chữ số có nghĩa | LÀM | "3,41/4, tương đương 8,06/10"; "không vượt 0,5"; "1.000 lần tái lấy mẫu" |
| 19 | Pass 5: Hình khớp Bảng/văn bản | LÀM với Hình 1–3 | Hình 1 "H2, H4 (biến kênh → mũi tên H1)" (M19); Hình 3 có năm bước, khớp L297 |
| 20 | Pass 5: Telephone Game | LÀM | 5.3 còn: "Thí sinh mới đọc tóm tắt…"; nguồn mới chưa có trong danh mục: "Quyết định số 1193/QĐ-UBND … \[CẦN ĐỐI CHIẾU bản chính thức\]" (M24) |
| 21 | Output Format: Summary, Pass 1–5 (có số vấn đề), Top 5 | LÀM | Phần A đối chiếu 46 phát hiện cũ; phần B có 24 vấn đề mới, chia theo 5 lượt; Top 5 |
| 22 | Severity CRITICAL/MAJOR/MINOR | LÀM, quy đổi sang nghiêm trọng / đáng sửa / chỉnh nhẹ | M13 "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10" xếp nghiêm trọng |
| 23 | Constraint: không đổi nội dung khoa học | LÀM | Các điểm chạm thiết kế đưa vào "Chờ duyệt", ví dụ D9 "$\beta$ của $D_{t}$ cùng dấu" |
| 24 | Constraint: tôn trọng quy ước ngành, hỏi tạp chí đích | LÀM một phần: không hỏi, vì nhiệm vụ đã xác định bối cảnh (đề cương NCS tiếng Việt) và đích được giữ như vòng trước | Giữ chủ thể "đề tài/thí sinh", ví dụ "thí sinh sẽ xác định khung quy định" (L127) |
| 25 | Constraint: giữ giọng tác giả | LÀM | Không gắn cờ lại các câu đã sửa đạt yêu cầu, ví dụ L191 "Theo Hình 1, H1 so sánh rủi ro lựa chọn mô hình giữa hai chế độ." |
| 26 | Constraint: cụ thể (mỗi đề xuất có câu gốc và câu sửa) | LÀM | Chỗ cần dữ kiện của tác giả (M13, M16, 4.4, 4.7) dùng mẫu có chỗ trống hoặc phương án để tác giả chọn, không tự điền |
| 27 | Interactive mode (chờ người dùng xác nhận từng đoạn) | KHÔNG ÁP DỤNG | Chế độ đã chọn là full-review, không phải interactive |

Ghi chú tuân thủ nhiệm vụ: không sửa đề cương; không git commit; không dùng mạng; chỉ đọc thêm hai file bối cảnh được chỉ định (g2-sciwrite.md, nhat-ky-thay-doi.md).
