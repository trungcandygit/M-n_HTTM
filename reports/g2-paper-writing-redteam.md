Xác nhận: đã gọi được công cụ Skill (paper-writing-skill) — "Launching skill: paper-writing-skill"

# Cổng 2 — Red-team độc lập theo `red_team_protocol.md` (skill paper-writing)

- Văn bản được rà: `/tmp/claude-0/-home-user-M-n-HTTM/ab114070-d2ea-5cad-86a9-3e021ab4cc42/scratchpad/paper/de-cuong-goc.md` (pandoc từ `ho-so/de-cuong-goc.docx`), chữ trong hình ở `hinh-van-ban.txt`; hình được kiểm tra thêm bằng bản PDF dựng từ docx bằng LibreOffice (trang 10, 15, 17).
- Phạm vi grep/đọc: dòng 155–1160 (mục 4 đến mục 10); bỏ mục lục tự động (dòng 37–153) và danh mục tài liệu (dòng 1161–1385), trừ khi ghi rõ. Mọi số dòng `Lxxx` trong báo cáo là số dòng của `de-cuong-goc.md`.
- Vai trò: reviewer độc lập, không viết văn bản này, không sửa đề cương, không đọc file khác trong `reports/` và không mở thư mục `scratchpad/paper/reviews/` (để không thấy đánh giá của người khác/tự đánh giá của tác giả, đúng yêu cầu "must NOT see the author's self-assessment").
- Không có `project_context.md`. Theo chỉ dẫn, ngữ cảnh kiểm soát (controlling idea / identity sentence) được lấy từ chính đề cương: **"Rủi ro lựa chọn mô hình trong quản trị danh mục đầu tư theo chế độ thị trường: Bằng chứng từ thị trường chứng khoán Việt Nam"** + CH1 (rủi ro lựa chọn mô hình thay đổi thế nào giữa chế độ bình thường và căng thẳng), CH2 (biến kênh có liên hệ và giải thích bao nhiêu phần chênh lệch, sau khi kiểm soát biến động thực hiện), CH3 (cơ chế nào giảm được rủi ro sau chi phí giao dịch). Term-map tạm dùng: các định nghĩa ở L171–184 làm "nguồn sự thật" (locked source of truth, S9).

## Số file skill đã đọc: 27

Đọc toàn văn (thư mục `/home/user/M-n_HTTM/.claude/skills/paper-writing-skill/`):

1. `SKILL.md` (nội dung do công cụ Skill nạp)
2. `red_team_protocol.md`
3. `loop_mode.md`
4. `brainstorming_guide.md`
5. `figure_synthesis_guide.md`
6. `README.md` (SKILL.md trỏ tới "see the README")
7. `CLAUDE.md` (harness tự nạp; đã đọc trọn)
8. `author_profile/editorial_principles.md`
9. `author_profile/craft_reference.md`
10. `author_profile/gate_mechanical.md`
11. `author_profile/gate_semantic.md`
12. `author_profile/compression_patterns.md`
13. `author_profile/rhetorical_moves.md`
14. `author_profile/intervention_types.md`
15. `writing_checklists/intro_questions.md`
16. `writing_checklists/evaluation_questions.md`
17. `writing_checklists/design_questions.md`
18. `writing_checklists/related_work_questions.md`
19. `section_rhetorical_moves/introduction.md`
20. `section_rhetorical_moves/evaluation.md`
21. `section_rhetorical_moves/design.md`
22. `section_rhetorical_moves/related_work.md`
23. `examples/netburst_project_context.md`
24. `figure_templates/figure_spec_template.md`
25. `figure_templates/prompt_templates.md`
26. `figure_templates/tikz_skeletons.md`
27. `figure_templates/venue_styles.md`

Không đọc/không chạy: `setup` (mã cài đặt, không được trỏ tới cho việc review, không chạy), `DESIGN.md`, `CHANGELOG.md`, `LICENSE`, `.gitignore` (SKILL.md và red_team_protocol.md không trỏ tới). `examples/project_context.md` được SKILL.md trỏ tới nhưng **không tồn tại** trong thư mục skill.

---

## 1. Kết quả gate mechanical (M1–M18, `gate_mechanical.md` Part C)

Cách chạy: (a) grep dòng trực tiếp (`g.sh`, lọc dòng 155–1160) cho M1; (b) script Python tự viết (`gate.py` nối đoạn, tách câu; `rules.py` áp regex theo câu) cho M2–M18, vì tiếng Việt xuống dòng giữa cụm từ làm grep theo dòng bỏ sót; (c) grep nguyên mẫu của skill trên `main.tex` (bản pandoc của cùng văn bản) cho M1/M15/M18. Script nằm ở `scratchpad/g2rt/`. Văn bản có 332 câu, 96 đoạn.

| Mã | Mẫu đã dùng (thích nghi tiếng Việt) | Số đếm | Ví dụ trích nguyên văn | Đánh giá |
|---|---|---|---|---|
| M1 gạch dài | `—\|–` (Unicode); `' -- '`; `'---'`; `[0-9]--[0-9]`; `' - '`. Trên `main.tex`: `---`=0, `—/–`=0, `' -- '`=1 | Unicode 0; `' -- '` trong thân 0; `---` 505 lần nhưng 0 ngoài dòng kẻ bảng pandoc; `số--số` 21 (khoảng năm/trang, ví dụ "1970--2017", "Quý 1--2"); `' - '` 8 (dấu trừ trong công thức L606/613/623/689, tên tạp chí "Kinh tế - Luật" L999/1048, tên bài giữ nguyên L1013) | Ngoài thân: bìa L27 "**HÀ NỘI -- 2026**"; L25 "PGS.TS. Hà Hồng Hạnh - Đại học…" | Thân văn bản sạch. Gạch nối khoảng số là gạch ngắn hợp lệ. Bìa: 1 hit (MINOR, quy ước trình bày bìa) |
| M2 phản đề/phủ định tu từ | `không phải…mà`, `chứ không`, `thay vì`, `không chỉ…mà còn`, `hơn là`, `, không gọi là`, `, chưa `, `, không ` | 15 câu | L180 "chỉ báo hiệu mức bất định, không đo rủi ro"; L698 "là liên hệ có điều kiện, không gọi là quan hệ nhân quả"; L740 "không kết luận, không gọi là ủng hộ hay bác bỏ" | Theo phép thử keep-vs-cut: 15/15 mang nội dung thật (ranh giới khái niệm, phạm vi, khoảng trống). Giữ. Vấn đề không nằm ở phủ định mà ở việc các câu "chưa… nào" là phổ quát chưa rào (xem S18/S21) |
| M3 câu kết bình luận | `điều này cho thấy`, `minh chứng`, `chính là điều`, `mới là`… | 0 | — | Sạch |
| M4 từ nhấn rỗng | `thực sự`, `thật sự`, `về bản chất`, `trên thực tế`, `thực chất`, `chính là`, `hoàn toàn`, `đơn giản là`, `(?<!căng )thẳng` | 1 | L163 "sai số ước lượng truyền thẳng sang trọng số danh mục" | Chấp nhận được (diễn giải Michaud 1989); không bắt buộc sửa |
| M5 tính từ cấm | `mới lạ`, `đáng kể`, `toàn diện`, `mạnh mẽ`, `vượt trội`, `hứa hẹn`, `quan trọng`, `then chốt`, `nổi bật`, `vững chắc`, `bền vững`, `giảm mạnh`, `biến động mạnh`, `lớn nhất`, `cấp bách` | 15 câu | L186 "Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách."; L260 "làm hiệu quả ngoài mẫu giảm mạnh" | 13/15 là thuật ngữ (vững chắc = robust, sai số chuẩn bền vững, lợi suất vượt trội = excess return, "lớn nhất" mô tả). 2 hit thật: "cấp bách" (L186), "giảm mạnh" (L260) → MINOR |
| M6 mở câu rào đón | `^(Hơn nữa\|Ngoài ra\|Bên cạnh đó\|Đáng chú ý\|Tuy nhiên\|Dù vậy\|Do đó\|Vì vậy\|Như vậy…)` | 1 | L269 "Dù vậy, DeMiguel và cộng sự (2009) không thấy hướng nào vượt 1/N…" | Có bước logic tương phản thật theo sau → giữ (ngoại lệ register trong M6) |
| M7 bộ ba trang trí | Đọc tay các liệt kê ba thành phần | 0 không hợp lý | L897 "học phần phương pháp, hội thảo định kỳ và cơ chế phản biện nội bộ" | Các bộ ba đều phân biệt, mang nội dung. Sạch |
| M8 câu dựng thế rỗng | `điểm mấu chốt`, `điểm khác biệt là`, `ý tưởng chính/cốt lõi` | 0 | — | Sạch |
| M9 ẩn dụ trang trí | `chìa khóa`, `bức tranh`, `đòn bẩy`, `cầu nối`, `nền móng`, `trụ cột`, `đóng băng`, `lan truyền`, `dồn trọng số` | 6 (5 câu) | L332–334 "đặt nền móng cho lý thuyết triển vọng… tổng hợp hai trụ cột của tài chính hành vi" | "đóng băng", "lan truyền", "dồn trọng số" là cách nói của nguồn (IMF, Vu và cộng sự, Michaud) → giữ. "nền móng", "trụ cột" → MINOR |
| M10 động từ thổi phồng | `mở ra`, `có tiềm năng`, `góp phần`, `hứa hẹn`, `sẵn sàng` | 0 | — | Sạch |
| M11 bị động | `\bđược\b\|\bbị\b\|\bbởi\b\|do mô hình` | 26 (25 câu) | L681 "Đề tài coi H~1~ được ủng hộ khi…"; L305 "chưa thể bị loại"; L183 "lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng" | Phần lớn "được" là nghĩa khả năng ("ước lượng được", "tính được"), không phải bị động. Bị động thật 9 ("được ủng hộ" ×3, "được chọn", "được mua bán lại", "bị loại", "bị từ chối", "được chấp nhận đăng" ×2) [sửa sau kiểm toán Cổng 3: bản cũ ghi ≈10; xem Phụ lục]: **xung đột với nguyên tắc tác giả — không khuyến nghị áp dụng** quy tắc zero-passive. Riêng L183 "do mô hình…" gây đọc sai → chuyển sang S5 (MAJOR) |
| M12 thừa chữ | `nhằm mục đích`, `để có thể`, `một cách`, `trong việc`, `về mặt`, `đối với`, `việc `, `sự `, `tiến hành` | 40 (37 câu) | L166–167 "vượt quy tắc chia đều vốn… một cách nhất quán"; L159 "việc chọn mô hình trở thành…" | 21 là "cộng sự" và 3 là "công việc/làm việc" (dương tính giả); 12 là "việc + động từ/danh từ" tự nhiên trong tiếng Việt; 2 "sự" khác ("sự kiện" là dương tính giả, "sự phù hợp" tùy chọn); 2 hit tùy chọn ("một cách nhất quán" → "nhất quán"; "đối với" L937) [sửa sau kiểm toán Cổng 3: bản cũ ghi ~28 cộng sự, ~11 việc; xem Phụ lục]. Không có lỗi đáng sửa bắt buộc |
| M13 từ rào yếu | `rất`, `khá`, `hơi`, `tương đối`, `chắc chắn` (trừ "tương đương chắc chắn"), `gần như`, `(?<!bình )thường` | 3 | L299 "dự báo kết hợp thường tốt hơn"; L323 "thường trên 2% mỗi năm"; L327 "gần như không còn dấu hiệu lây nhiễm" | Cả 3 là rào trung thực, khớp phát hiện của nguồn → giữ. **xung đột với nguyên tắc tác giả — không khuyến nghị áp dụng** việc xoá |
| M14 trạng từ tự chế / số thứ tự giả | Không có tương đương tiếng Việt cho `firstly/-wise`; kiểm "thứ nhất/thứ hai" | 0 | — | Không áp dụng (cách đếm "Lý do đầu tiên/thứ hai" là chuẩn tiếng Việt) |
| M15 `!` và câu hỏi tu từ | `[!?]`; grep `!` trên main.tex | 3 `?` trong thân; 1 `!` trong tên bài trích dẫn (Lo và Mueller 2010) | L233–242 ba câu hỏi nghiên cứu | Câu hỏi nghiên cứu, không phải tu từ; `!` nằm trong tên bài gốc → hợp lệ |
| M16 từ kêu/mơ hồ | `nhân tố`, `yếu tố`, `hiện nay`, `hiện tại`, `sở hữu`, `có ý nghĩa`, `tác động` | 9 | L435–439 "chế độ thị trường tác động lên rủi ro lựa chọn mô hình… Các biến kênh tác động lên chính quan hệ đó… Cơ chế giảm thiểu tác động lên quan hệ…" | 3 hit ở L435–439 là lỗi thật: ngôn ngữ nhân quả mâu thuẫn L698–699 → MAJOR (S18/S8). 6 hit còn lại gồm 2 mô tả nguồn, 2 "mức ý nghĩa" thống kê và 2 "tác động" kỹ thuật trong phần phương pháp (L625, L677), giữ [sửa sau kiểm toán Cổng 3: bản cũ gộp cả 6 vào nhóm mô tả nguồn/mức ý nghĩa; xem Phụ lục] |
| M17 động từ hoa mỹ | `khai thác`, `kiến tạo`, `đan xen`, `nắm bắt`, `giải mã`, `định hình`, `rèn` | 1 | L897 "Thí sinh muốn rèn các kỹ năng này" | Cách nói thông dụng; giữ (tùy chọn "phát triển") |
| M18 câu mở rỗng | `^(Trong (đề cương\|phần\|mục\|chương) này\|Phần này\|Mục này)`; mẫu gốc trên main.tex | 0 / 0 | — | Sạch |
| Part B cặp từ dễ nhầm | Không có tương đương trực tiếp; kiểm "do" mơ hồ chủ thể/nguyên nhân | 1 thật | L183 (như trên) | Chuyển sang S5 |
| Độ dài câu (base gate mục 5) | Đếm âm tiết (token cách nhau bởi khoảng trắng) | TB 25,8 âm tiết, trung vị 25; >40 âm tiết: 56 câu; >50: 24; >60 (≈ >40 từ tiếng Anh): 7 | L1137 (79), L892 (66), L877 (66), L171 (65), L667 (62), L714 (61), L257 (61) | Ngưỡng 40 âm tiết theo nghĩa đen quá chặt cho tiếng Việt (1 từ ≈ 1,4–1,5 âm tiết); 7 câu >60 âm tiết → MINOR |
| Trôi thuật ngữ / phân rã (Part C cuối) | Đếm cụm thuật ngữ và các "N + danh từ" | Xem S8/S9 | "tương quan cực trị" 5 / "tương quan đuôi" 3 / "tương quan đuôi âm" 2 / "tương quan hiệu chỉnh" 1; "quy tắc chuyển chế độ" 2 / "chiến lược theo chế độ" 1 / Hình 1 "Quy tắc theo chế độ" | Phát hiện ở S8, S9 |

Kết luận mechanical: lớp "giọng máy" gần như sạch (0 gạch dài trong thân, 0 M3/M8/M10/M18). Các hit cần sửa: 2×M5, 2×M9, 3×M16 (thực chất là S18), 1×M11 (thực chất là S5), 1×M1 ở bìa, 7 câu quá dài. Một dấu hiệu văn máy nhẹ: 27/332 câu mở bằng "Đề tài", có chuỗi 4 câu liền ở L777–784.

---

## 2. Kết quả gate semantic S1–S31 (từng mục)

| Mã | Kết quả | Trích dẫn / ghi chú |
|---|---|---|
| S1 định nghĩa trước khi dùng | **Phát hiện (MAJOR)** | "lợi suất tương đương chắc chắn" dùng từ L167, định nghĩa ở L591–593; "tập tin cậy mô hình" dùng L180, định nghĩa L304–306; "vòng quay danh mục" dùng L168, định nghĩa L716–717; "độ sụt giảm tối đa", "giá trị thiệt hại kỳ vọng mức 95%" dùng ở Bảng 2 (L468–470), định nghĩa L715–716; "cửa sổ độc lập ở chế độ căng thẳng", "giai đoạn căng thẳng độc lập" (L227, L642, L739–741) không được định nghĩa trong khi $S_t$ là tỷ lệ liên tục; "phân phối rỗng" (L678) là cách dịch dễ hiểu sai; "biến kênh" (L236) không có câu định nghĩa |
| S2 thứ tự giới thiệu thuật ngữ | Phát hiện nhẹ | Chuỗi rủi ro mô hình → bất định mô hình → rủi ro lựa chọn mô hình → mức hối tiếc (L171–179) đúng thứ tự; lỗi thứ tự còn lại trùng S1 |
| S3 viết đầy đủ từ viết tắt | Phát hiện (MINOR) | "OSF Registries" (L580) chưa viết đầy đủ. HOSE (L346), VN-Index, SR 11-7 đều ổn |
| S4 theo dõi được đệ quy | **Phát hiện (MAJOR)** | Ý nghĩa của $\beta$ khi $S_t$ liên tục (L669–670: "β đo chênh lệch của $Y_t$ giữa chế độ căng thẳng và chế độ bình thường"); chuẩn so sánh của H3 khi loại cơ chế (ii), (iii) khỏi *M* (L710–712) chưa rõ là chọn trong 7 hay 5 mô hình; chưa rõ trong cửa sổ đánh giá 6 tháng, mỗi lần tái cân bằng tháng có ước lượng lại trên 104 tuần trượt hay không (L616–618, L636–637) |
| S5 dễ phân tích câu | **Phát hiện (MAJOR)** | L225–226 "chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển" (đọc thành "lớn hơn *tại* thị trường phát triển"); L182–183 "lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng" (đọc thành lợi suất thấp *vì* mô hình); "hệ số của tương quan đuôi âm" (L463–464, L695–696) đọc được là "hệ số của [tương quan đuôi âm]" (không nêu dấu) hoặc "hệ số … mang dấu âm"; L161–163 thiếu "mà"; L305–306 "dữ liệu kém thông tin cho tập lớn" (chữ "cho" mơ hồ) |
| S6 chú giải một lần | Không phát hiện đáng kể | "1/N", "lợi suất tương đương chắc chắn" mỗi thứ chú giải một lần; vấn đề là vị trí (S1), không phải lặp |
| S7 bám luận điểm, không mở mạch mới | Phát hiện (MAJOR + MINOR) | Đoạn khung giám sát L201–216 mở một nhiệm vụ mới ("Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này, cùng mức độ họ dùng mô hình định lượng") không gắn với câu hỏi/mục tiêu nào; mục (5) L332–335 nêu lý thuyết triển vọng và giới hạn kinh doanh chênh lệch giá nhưng không dùng lại ở đâu |
| S8 một từ cho một khái niệm | **Phát hiện (MAJOR)** | Tương quan cực trị/đuôi/đuôi âm/hiệu chỉnh theo biến động; quy tắc chuyển chế độ/chiến lược theo chế độ/Quy tắc theo chế độ (Hình 1)/quy tắc chế độ (Hình 3) cạnh M~7~; "mô hình chọn trước" vs "mô hình được chọn" (L618); "trạng thái thị trường" (L312, L418) vs "chế độ thị trường"; "cơ chế vững chắc" (L417) vs "danh mục vững chắc"; nhóm người dùng đổi giữa L211–212, L810–811, L900–902; "tác động" (L435–439) vs "liên hệ có điều kiện" (L698) |
| S9 term-map và bất biến phân rã | **Phát hiện (CRITICAL)** | H3 trong Bảng 2 (L466–473) gồm 2 cơ chế, còn 4.3.8 (L703), Hình 1, Hình 3, Chương 6 có 3 cơ chế; mục tiêu (iii) (L250–252) liệt kê 4 biến kênh *gồm biến động*, còn CH2 (L236–237), H2, H4 và Hình 1 coi biến động là biến kiểm soát; bìa (L23–25) ghi một người hướng dẫn là PGS.TS. Hà Hồng Hạnh, mục 10 (L1151–1159) ghi người hướng dẫn chính là GS.TS. Nguyễn Đức Khương; ngưỡng H3 về độ sụt giảm "thấp hơn" (Bảng 2) vs "không cao hơn" (L721); Holm "cho bốn giả thuyết" (L743–744) vs "chỉ báo cáo H~4~ như kết quả thăm dò" (L697–698). Các phân rã khác khớp: 3 câu hỏi, 4 mục tiêu, 4 khoảng trống, 7 mô hình, 5 bước, 6 chương, 3 bước thủ tục, 4 điểm khác biệt |
| S10 không trùng lặp | Phát hiện (MINOR, 1 MAJOR gộp vào S18) | Kết quả DeMiguel và cộng sự (2009) nêu hai lần (L165–168, L269–270); quy tắc "không kết luận" ba lần (L584–585, L739–743, L975–977); phương án dữ liệu dự phòng hai lần (L752–754, L973–975); hai câu khẳng định khoảng trống liền nhau L394–398 |
| S11 quy chiếu | Phát hiện (MINOR) | L159–160 "Mô hình gốc của lĩnh vực này" (lĩnh vực nào?) |
| S12 nói thẳng danh từ | **Phát hiện (MAJOR)** | Cơ chế (i) L703–706 "theo trọng số Bayes … hoặc chỉ kết hợp các mô hình nằm trong tập tin cậy" (chưa nói phương án chính); cơ chế (iii) L709–710 "đối chứng là giá trị của chuyển chế độ trong quyết định danh mục theo Tu (2010)" (chưa nói đại lượng được tính) |
| S13 chồng chú giải | Phát hiện (MAJOR) | L714–717 một câu chứa ba chú giải trong ngoặc ("(mức giảm lớn nhất từ đỉnh)", "(tổn thất trung bình trong 5% số ngày xấu nhất)", "(tỷ lệ danh mục được mua bán lại)"); L171–179 câu định nghĩa 65 âm tiết gộp định nghĩa + cách đo + chú giải |
| S14 bổ ngữ treo | Không phát hiện | Các mệnh đề "Để …," (L625, L677) đều có chủ ngữ đúng |
| S15 không có số mồ côi | Phát hiện (MINOR, quy trình) | Đề cương chưa có kết quả nên không có số tự tính. Số học nội bộ khớp: 2007–2026, cần 2 năm ước lượng + 3 năm kết quả ngoài mẫu, còn khoảng 14 năm = 28 cửa sổ 6 tháng (L640–641); 468 tuần = 9 năm 2011–2019 (L349–350). Ngưỡng N/T ≤ 0,5 (L573–575) không bao giờ bị vượt ở cấu hình cơ sở (30/104 ≈ 0,29). Số liệu trích từ nguồn (151 khủng hoảng; 14 mô hình/7 bộ dữ liệu; 2%/10% của Tu; 299 công ty; SR 26-2 ngày 17/04/2026; Thông tư 83/2025) không kiểm chứng được vì không dùng mạng; thí sinh tự nói mới đọc chủ yếu tóm tắt (L403–405) |
| S16 phê bình bằng số | Không áp dụng đầy đủ | Đề cương chưa có kết quả để đối đầu trực tiếp; thay vào đó, các nhận định về tài liệu phải nêu đúng thước đo của nguồn đo gì (xem S21) |
| S17 toàn vẹn dữ liệu | Không phát hiện | Việc đã dùng dữ liệu 2019–2025 được khai rõ (L577–587) |
| S18 rà rào đón | **Phát hiện (MAJOR)** | Câu mở L159 "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê." là phổ quát, trong khi L212–215 nói thí sinh *sẽ* xác định mức độ họ dùng mô hình định lượng; các câu "chưa thước đo nào" (L291), "chưa công trình nào" (L311, L395), "chưa nghiên cứu nào" (L329) chưa rào theo phạm vi tìm kiếm của chính L399–405; L747–750 suy từ không ủng hộ giả thuyết ra "rủi ro lựa chọn mô hình không đổi theo chế độ" là sai logic và mâu thuẫn quy tắc "không kết luận"; L754–755 "Các mô hình ở Bảng 3 ước lượng được bằng phần mềm thống kê thông dụng" mâu thuẫn L758–760 (M~5~ có thể phải đổi phương pháp) |
| S19 yêu cầu ↔ lời đáp | **Phát hiện (MAJOR)** | Khoảng trống nói "hậu quả … lên trọng số" (L220) và "thứ hạng thay đổi ra sao" (L222–223, L329–330), nhưng các thước đo $R_t$, $D_t$, tập tin cậy đều dựa trên lợi suất tương đương chắc chắn, không đo trọng số hay độ ổn định thứ hạng. Các yêu cầu khác có lời đáp: công suất thấp → 4.3.10; thủ tục giám sát → 4.4 và Chương 6.5 |
| S20 điểm mạnh trước | Phát hiện, **xung đột với nguyên tắc tác giả — không khuyến nghị áp dụng** | L226–228 nêu giới hạn công suất ngay trong lý do chọn đề tài; L403–405 thừa nhận mới đọc tóm tắt. Đây là hedging trung thực mà tác giả chủ trương giữ |
| S21 định vị trung thực | **Phát hiện (CRITICAL + MAJOR)** | L275–276 "Các nghiên cứu đã đo rủi ro mô hình cho dự báo và định giá, nhưng chưa đo cho quyết định phân bổ" và L290–292 "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục" bị chính các nguồn đề cương trích phủ định: Tu (2010) đo tổn thất lợi suất tương đương chắc chắn khi bỏ qua chuyển chế độ (L322–324); Kan và Zhou (2007) đo tổn thất do sai số tham số trong phân bổ (L164, L260–261); Garlappi và cộng sự (2007), Pflug và cộng sự (2012) xử lý bất định mô hình trong quyết định danh mục. L343–344 "Các công trình về Việt Nam xét riêng một mô hình, một phương pháp…" bị Goutte và cộng sự (2025) phủ định, vì công trình này so sánh 5 phương pháp × 4 cách gán trọng số (L351–353). Mục 5 L880–881 nói đề tài "nằm ở giao điểm của … tài chính hành vi", trong khi 4.4 L780–783 nói chỉ "giao thoa với kinh tế hành vi ở một phép thử giới hạn" |
| S22 mô tả hệ thống nền bằng năng lực | Không áp dụng | Không có hệ thống nền |
| S23 tiêu đề dạng khẳng định | Phát hiện, **xung đột với nguyên tắc tác giả và mẫu đề cương của Trường — không khuyến nghị áp dụng** | Các tiêu đề mục 4.1–11 do mẫu hồ sơ quy định |
| S24 bảng thay khối chữ | **Phát hiện (MAJOR)** | Quy tắc kết luận nằm rải ở L583–585, L681–686, L695–698, L718–722, L739–744; nên gom vào một bảng (không đổi kiểm định) |
| S25 không có khung chữ trong hình | Phát hiện (MINOR) | Hình 2 có dòng chú thích dài trong hình ("Đầu mỗi cửa sổ đánh giá: chọn trước mô hình c…"); Hình 3 là sơ đồ quy trình dạng hộp chữ, chấp nhận được |
| S26 số đặt trên cấu trúc | Không áp dụng | Không có hình dữ liệu trên cấu trúc |
| S27 đúng hình đúng mục | Không phát hiện | Hình 1 là sơ đồ khối khung phân tích, đặt đầu phần phương pháp |
| S28 đọc được khi nhìn | Phát hiện (MINOR), đã nhìn ảnh dựng | Bản dựng LibreOffice: Hình 3 ngắt dòng xấu "quy tắc chế / độ", "quy tắc / kết luận"; công thức (5) và ký hiệu toán trong dòng bị mất ở trang 12 (có thể do LibreOffice, cần kiểm trên Word/PDF xuất từ Word). Hình 1: mũi tên H~2~, H~4~ chỉ vào mũi tên H~1~ (biểu diễn biến điều tiết), trong khi phương trình (5) kiểm định phần chênh lệch được giải thích (β0 − β1) |
| S29 các lăng kính riêng | Đã chạy bốn lượt riêng: (a) mechanical, (b) dễ tiếp cận (S1–S6), (c) theo dõi đệ quy (S4/S5), (d) nhất quán (S8/S9) | Cả bốn lượt do cùng một reviewer độc lập chạy, không phải bốn reviewer khác nhau (ghi để minh bạch) |
| S30 hiệu chỉnh theo cách hội đồng đọc | Phát hiện (MINOR) | Hội đồng xét tuyển đọc đề cương rồi phỏng vấn. Mục 4.1 đưa câu hỏi nghiên cứu ở cuối mục (L231) là hợp lý; định nghĩa đối tượng (L171) đến ở đoạn 2. Điểm yếu cho lượt đọc đầu là C1 (định vị) và C4 (người hướng dẫn trên bìa) |
| S31 closure gate | **CHƯA CLEAN** | 4 CRITICAL và 21 MAJOR còn mở; chưa có vòng sửa và vòng closure reviewer |

### Bốn lớp lỗi phải săn (red_team_protocol)

- **Giọng máy (AI-sounding):** thấp. Dấu hiệu duy nhất: nhịp câu đơn điệu, nhiều câu mở "Đề tài…"/"Thí sinh…" (27 và 25 câu).
- **Khó tiếp cận:** dùng thuật ngữ trước khi định nghĩa (S1), "phân phối rỗng", ba câu dễ đọc sai (S5).
- **Thiếu mạch lạc:** trôi thuật ngữ (S8), lệch phân rã H3/biến kênh/người hướng dẫn (S9).
- **Phi logic:** nhận định khoảng trống bị chính nguồn trích phủ định (S21); suy "không ủng hộ" thành "không đổi" (S18); ngôn ngữ nhân quả cạnh tuyên bố "liên hệ có điều kiện" (S18/S8).

---

## 3. Danh sách phát hiện theo mức

Quy đổi: CRITICAL = NGHIÊM TRỌNG; MAJOR = ĐÁNG SỬA; MINOR = CHỈNH NHẸ. Mỗi mục ghi mã quy tắc gốc (M#/S#) làm nguồn gốc. Các đề xuất chỉ sửa chữ; không đổi câu hỏi nghiên cứu, H1–H4, M1–M7, dữ liệu hay phương pháp kiểm định.

### NGHIÊM TRỌNG (4)

**C1. [S21, S18] Khoảng trống "chưa đo cho quyết định phân bổ" bị chính nguồn trích phủ định.**
- Vị trí: L275–276, L290–292 (và L218–221, Bảng 1 dòng 1).
- Trích: "Các nghiên cứu đã đo rủi ro mô hình cho dự báo và định giá, nhưng chưa đo cho quyết định phân bổ." / "chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục."
- Đề xuất: "Các thước đo rủi ro mô hình chủ yếu gắn với dự báo rủi ro và định giá. Một số nghiên cứu danh mục đã đo tổn thất của một sai lầm cụ thể, như dùng tham số ước lượng thay cho tham số thật (Kan và Zhou, 2007) hoặc bỏ qua chuyển chế độ (Tu, 2010); thí sinh chưa tìm thấy nghiên cứu đo tổn thất khi nhà đầu tư phải chọn trước một mô hình trong một tập mô hình danh mục cạnh tranh." Sửa câu kết đoạn (2) theo cùng phạm vi.
- Lý do: L322–324 tự trích Tu (2010) đo tổn thất lợi suất tương đương chắc chắn do chọn mô hình sai. Hội đồng đọc hai đoạn cạnh nhau sẽ thấy mâu thuẫn. Phạm vi đúng của khoảng trống (chọn trong tập cạnh tranh, theo chế độ) vẫn giữ nguyên.

**C2. [S9] Tập cơ chế của H3 không khớp giữa các mục.**
- Vị trí: Bảng 2 L466–473 với 4.3.8 L703–712, Hình 1, Hình 3, Bảng 4 Chương 6.
- Trích: "H~3~: Ở chế độ căng thẳng, sau chi phí giao dịch, kết hợp mô hình và danh mục vững chắc cho mức hối tiếc…" và "Đề tài đánh giá ba cơ chế."
- Đề xuất: không đổi H3. Thêm một câu ở 4.3.8 nói rõ cơ chế (iii) thuộc hay không thuộc phép kiểm định H3, ví dụ: "H~3~ áp dụng cho cơ chế (i) và (ii); cơ chế (iii) được báo cáo như một đối chứng mô tả" hoặc ngược lại, theo quyết định của tác giả (xem mục Thiết kế, D2).
- Lý do: phân rã cùng một khái niệm phải đồng nhất về thành phần và số lượng giữa các mục.

**C3. [S9] Biến động thực hiện là biến kênh ở mục tiêu (iii) nhưng là biến kiểm soát ở CH2, H2, H4, Hình 1.**
- Vị trí: L250–252 với L236–237, L457–458, L475–476, L675.
- Trích: "(iii) xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình, gồm biến động, thanh khoản, tương quan cực trị và bầy đàn".
- Đề xuất: "(iii) xác định các biến kênh có liên hệ thống kê với rủi ro lựa chọn mô hình sau khi kiểm soát biến động thực hiện, gồm thanh khoản, tương quan cực trị và, ở mức thăm dò, bầy đàn".
- Lý do: mục tiêu phải khớp với câu hỏi nghiên cứu 2 đã cố định. Vấn đề liên quan trong phép phân rã β0 − β1 ghi ở D1.

**C4. [S9] Thông tin người hướng dẫn trên bìa mâu thuẫn mục 10.**
- Vị trí: L23–25 với L1145–1159.
- Trích: bìa "Người hướng dẫn khoa học (dự kiến): **- PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân**"; mục 10 "Người hướng dẫn chính (dự kiến): GS.TS. Nguyễn Đức Khương… Người hướng dẫn thứ hai (dự kiến): PGS.TS. Hà Hồng Hạnh".
- Đề xuất: bìa liệt kê cả hai người theo đúng thứ tự mục 10: "1. GS.TS. Nguyễn Đức Khương (hướng dẫn chính); 2. PGS.TS. Hà Hồng Hạnh, Trường Đại học Kinh tế Quốc dân". Thống nhất "Quốc dân" (mục 10 viết thường chữ "dân").
- Lý do: hội đồng đọc trang bìa đầu tiên. Lưu ý: nếu mẫu hồ sơ yêu cầu bìa chỉ ghi người hướng dẫn ngoài Trường, tác giả cần ghi rõ vai trò để tránh hiểu nhầm.

### ĐÁNG SỬA (21)

**J1. [S18, S8, M16] Ngôn ngữ nhân quả khi mô tả Hình 1.**
- Vị trí: L435–441. Trích: "chế độ thị trường tác động lên rủi ro lựa chọn mô hình… Các biến kênh tác động lên chính quan hệ đó… Cơ chế giảm thiểu tác động lên quan hệ…".
- Đề xuất: "Theo Hình 1, H~1~ so sánh rủi ro lựa chọn mô hình giữa hai chế độ. H~2~ và H~4~ xét các biến kênh có giải thích một phần chênh lệch đó hay không. H~3~ so sánh kết quả danh mục của các cơ chế giảm thiểu với kết quả của việc chọn một mô hình."
- Lý do: L698–699 khẳng định "liên hệ có điều kiện, không gọi là quan hệ nhân quả"; "tác động lên quan hệ" còn gợi biến điều tiết, khác với phép kiểm định β0 − β1.

**J2. [S5] "hệ số của tương quan đuôi âm" mơ hồ về dấu.**
- Vị trí: Bảng 2 L462–464; L695–697.
- Đề xuất: "hệ số của tương quan đuôi dưới mang dấu âm"; tương tự ở L695–696. Tác giả xác nhận dấu dự kiến là âm (chú giải trong Bảng 2 "tương quan cao làm các danh mục chỉ mua hội tụ" gợi dấu âm).
- Lý do: "đuôi âm" đã được dùng ở L326 với nghĩa đuôi trái của phân phối, nên người đọc có thể hiểu H2 không nêu dấu cho biến này.

**J3. [S5] So sánh thiếu "so với".**
- Vị trí: L224–226. Trích: "nên chênh lệch giữa các mô hình có thể lớn hơn ở thị trường phát triển."
- Đề xuất: "nên chênh lệch giữa các mô hình có thể lớn hơn so với ở các thị trường phát triển."
- Lý do: câu hiện tại đọc ra nghĩa ngược.

**J4. [S5, M11] "do mô hình… ước lượng" đọc thành quan hệ nguyên nhân.**
- Vị trí: L181–183. Trích: "*chế độ căng thẳng*, một trạng thái thống kê có biến động cao và lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng."
- Đề xuất: "*chế độ căng thẳng*, một trạng thái thống kê mà mô hình chuyển chế độ ước lượng được, có biến động cao và lợi suất thị trường thấp."

**J5. [S1, S4] Đơn vị "cửa sổ/giai đoạn căng thẳng độc lập" chưa định nghĩa.**
- Vị trí: L227, L642–643, L738–742. Trích: "Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận".
- Đề xuất: thêm một câu định nghĩa ngay sau phương trình (5), với ngưỡng do tác giả chọn và đăng ký trước, ví dụ: "Một cửa sổ đánh giá thuộc chế độ căng thẳng khi $S_t$ vượt [ngưỡng đăng ký trước]; một giai đoạn căng thẳng độc lập là một chuỗi ngày liên tiếp có xác suất lọc vượt ngưỡng."
- Lý do: $S_t$ là tỷ lệ liên tục, nên quy tắc "dưới 10 cửa sổ" hiện không áp dụng được một cách xác định.

**J6. [S5, S4] Diễn giải β khi $S_t$ liên tục.**
- Vị trí: L669–670. Trích: "$\beta$ đo chênh lệch của $Y_{t}$ giữa chế độ căng thẳng và chế độ bình thường".
- Đề xuất: "$\beta$ đo chênh lệch của $Y_t$ giữa một cửa sổ có toàn bộ số ngày ở chế độ căng thẳng ($S_t = 1$) và một cửa sổ không có ngày nào ở chế độ này ($S_t = 0$)."

**J7. [S1, S13] Dùng thuật ngữ trước khi định nghĩa; chú giải dồn vào một câu.**
- Vị trí: lợi suất tương đương chắc chắn (dùng L167, định nghĩa L591); vòng quay (L168 → L716); tập tin cậy mô hình (L180 → L304); độ sụt giảm tối đa, giá trị thiệt hại kỳ vọng (Bảng 2 → L714–716).
- Đề xuất: chuyển chú giải ngắn về lần dùng đầu. Ví dụ L167: "lợi suất tương đương chắc chắn (mức lợi suất phi rủi ro mà nhà đầu tư ngại rủi ro coi là ngang giá với danh mục)"; L180: "kích thước tập tin cậy mô hình (tập các mô hình chưa bị loại là kém hơn ở một mức tin cậy cho trước; xem mục 4.2)". Câu L714–717 giữ danh sách tiêu chí, bỏ ba ngoặc chú giải vì đã chú giải trước đó hoặc dưới Bảng 2.

**J8. [S18] Câu mở đầu phổ quát mâu thuẫn với điều thí sinh chưa biết.**
- Vị trí: L159. Trích: "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê."
- Đề xuất: "Nhiều tổ chức đầu tư dùng mô hình thống kê để phân bổ vốn."
- Lý do: L212–215 nói thí sinh sẽ xác định "mức độ họ dùng mô hình định lượng".

**J9. [S18, S10] Hai câu khoảng trống liền nhau, câu trước không rào, câu sau rào.**
- Vị trí: L394–398. Trích: "…chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường. Theo hiểu biết của thí sinh, chưa có nghiên cứu nào…"
- Đề xuất: "Bốn khoảng trống có chung một điểm: các công trình đo từng mô hình, từng chế độ hoặc từng hiện tượng riêng lẻ. Theo hiểu biết của thí sinh, chưa có nghiên cứu nào…" (giữ nguyên phần sau). Rào tương tự ở L311–312 và L329–330: "thí sinh chưa tìm thấy công trình nào…".
- Lý do: nhận định chỉ đúng trong phạm vi tìm kiếm nêu ở L399–405.

**J10. [S21, S18] Nhận định về tài liệu Việt Nam bị Goutte và cộng sự (2025) phủ định.**
- Vị trí: L343–344; Bảng 1 dòng 2 ("Đánh giá từng mô hình hoặc từng phương pháp").
- Trích: "Các công trình về Việt Nam xét riêng một mô hình, một phương pháp hoặc một hiện tượng."
- Đề xuất: "Các công trình về Việt Nam đánh giá một mô hình hoặc so sánh các phương pháp theo bình quân toàn mẫu; thí sinh chưa tìm thấy công trình đo tổn thất của việc chọn mô hình theo chế độ thị trường." Bảng 1 dòng 2: "Đánh giá từng mô hình hoặc so sánh phương pháp theo bình quân toàn mẫu".

**J11. [S19] Khoảng trống nêu "trọng số" và "thứ hạng" nhưng không có thước đo đóng lại.**
- Vị trí: L218–223, L329–330.
- Đề xuất (chỉ sửa chữ): L220 bỏ "trọng số và" ("chưa đo hậu quả của việc chọn sai mô hình lên kết quả danh mục"). Thêm vào L329–330 một câu nối thứ hạng với mức hối tiếc: "Khi thứ hạng đổi theo chế độ, mô hình chọn theo quá khứ dễ khác mô hình tốt nhất nhìn lại sau thực tế; mức hối tiếc đo tổn thất này." Phương án bổ sung thước đo thứ hạng là quyết định thiết kế (D7).

**J12. [S9] Ngưỡng độ sụt giảm của H3 khác nhau.**
- Vị trí: Bảng 2 L467–469 "mức hối tiếc và độ sụt giảm tối đa thấp hơn" với L719–722 "độ sụt giảm tối đa không cao hơn".
- Đề xuất: thống nhất một cách viết, theo quy tắc mà tác giả sẽ đăng ký trước.

**J13. [S9] Họ hiệu chỉnh Holm gồm cả giả thuyết thăm dò.**
- Vị trí: L743–744 "hiệu chỉnh so sánh bội theo Holm (1979) ở mức 10% cho bốn giả thuyết" với L697–698.
- Đề xuất: nói rõ họ kiểm định là H1–H3 hay H1–H4 (quyết định của tác giả, D5).

**J14. [S12] Cơ chế (i) và cơ chế (iii) chưa xác định rõ.**
- Vị trí: L703–706, L708–710.
- Đề xuất: cơ chế (i) nêu phương án chính và phương án phụ (ví dụ: "phương án chính là … ; phương án còn lại báo cáo trong kiểm tra độ bền", theo lựa chọn của tác giả). Cơ chế (iii) nói rõ đại lượng đối chứng, ví dụ: "đối chứng là chênh lệch lợi suất tương đương chắc chắn giữa phân bổ có tính đến chuyển chế độ và phân bổ bỏ qua chuyển chế độ, theo cách tính của Tu (2010)", nếu đó đúng là ý tác giả.

**J15. [S4, S12] Chuẩn "chọn một mô hình" khi kiểm định H3.**
- Vị trí: L710–712. Trích: "Khi kiểm định H~3~, đề tài loại cơ chế (ii) và (iii) khỏi *M*, nên mức hối tiếc của hai cơ chế này có thể âm."
- Đề xuất: thêm một câu: "Chuẩn so sánh 'chọn một mô hình' là mô hình $c$ chọn trong [7 / 5] mô hình còn lại." Tác giả chọn (D2).

**J16. [S18, S7] Suy luận khi dữ liệu không ủng hộ giả thuyết.**
- Vị trí: L747–750. Trích: "Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam."
- Đề xuất: "Nếu dữ liệu không ủng hộ H~1~, đề tài vẫn trả lời được câu hỏi 1: đề tài báo cáo kích thước hiệu ứng cùng khoảng tin cậy, và phân biệt trường hợp khoảng tin cậy hẹp quanh 0 với trường hợp không kết luận do công suất thấp. Kết luận về quy tắc 1/N dựa trên mức hối tiếc của M~1~."
- Lý do: không ủng hộ giả thuyết khác với có bằng chứng "không đổi", và câu hiện tại mâu thuẫn với quy tắc "không kết luận" ở L739–742.

**J17. [S21, S9] Mức độ "tài chính hành vi" ở mục 5 vượt mức đề tài làm.**
- Vị trí: L880–881. Trích: "còn đề tài nằm ở giao điểm của tài chính định lượng, quản lý và tài chính hành vi."
- Đề xuất: "còn đề tài thuộc tài chính định lượng và quản lý, và giao thoa với tài chính hành vi ở một phép thử thăm dò (H~4~)."
- Lý do: khớp với L780–783 và tình trạng thăm dò của H4.

**J18. [S8] Trôi thuật ngữ nhóm tương quan.**
- Vị trí: "tương quan cực trị" (L236, L251, L421, Bảng 4), "tương quan đuôi" (Bảng 2, L672), "tương quan đuôi âm" (L463, L696), "tương quan hiệu chỉnh theo biến động" (L672–673); Hình 1 "tương quan đuôi".
- Đề xuất: "tương quan cực trị" là tên kênh; hai thước đo là "tương quan đuôi dưới" và "tương quan hiệu chỉnh theo biến động". Dùng đúng ba tên này ở mọi nơi, kể cả Hình 1.

**J19. [S8] Tên cơ chế (iii) thay đổi theo mục.**
- Vị trí: L539 "chiến lược theo chế độ", L708 và Bảng 4 "quy tắc chuyển chế độ", Hình 1 "Quy tắc theo chế độ", Hình 3 "quy tắc chế độ"; M~7~ "Giảm tỷ trọng rủi ro theo xác suất chế độ căng thẳng".
- Đề xuất: chọn "quy tắc chuyển chế độ" cho cơ chế (iii), dùng thống nhất ở chữ và hình; nếu cơ chế (iii) chính là M~7~, ghi rõ "(tương ứng M~7~)".

**J20. [S24] Quy tắc kết luận nằm rải nhiều mục.**
- Vị trí: L583–585, L681–686, L695–698, L718–722, L739–744.
- Đề xuất: thêm một bảng "Quy tắc kết luận cho H1–H4" với các cột: giả thuyết | điều kiện ủng hộ | điều kiện "không kết luận" | thuộc họ Holm hay không | mức ý nghĩa. Bảng chỉ gom nội dung đã có, không đổi kiểm định.

**J21. [S7] Đoạn khung giám sát mở một nhiệm vụ không gắn mục tiêu.**
- Vị trí: L211–216. Trích: "Thí sinh sẽ xác định khung quy định áp dụng cho nhóm tổ chức này, cùng mức độ họ dùng mô hình định lượng để phân bổ danh mục…"
- Đề xuất: thêm một mệnh đề nối: "…; thông tin này phục vụ mục tiêu (iv) và thủ tục giám sát mô hình ở Chương 6", hoặc rút đoạn còn hai câu bối cảnh.

### CHỈNH NHẸ (25)

| # | Mã | Vị trí | Trích | Đề xuất | Lý do |
|---|---|---|---|---|---|
| m1 | M5 | L186 | "Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách." | "Đề tài chú ý đến khủng hoảng vì rủi ro mô hình tăng khi bất định tăng (Danielsson và cộng sự, 2016)." | Thay tính từ cảm xúc bằng lý do có nguồn đã trích |
| m2 | M5 | L260 | "làm hiệu quả ngoài mẫu giảm mạnh" | "làm hiệu quả ngoài mẫu giảm" (chỉ nêu mức cụ thể nếu đã đối chiếu toàn văn Kan và Zhou) | Tránh từ nhấn không có số |
| m3 | M9 | L332–334 | "đặt nền móng cho lý thuyết triển vọng… hai trụ cột" | "đề xuất lý thuyết triển vọng… hai nội dung chính" | Ẩn dụ không mang nội dung |
| m4 | S7 | L332–335 | Kahneman và Tversky (1979); Barberis và Thaler (2003) | Bỏ, hoặc nối một mệnh đề với H~4~ | Không dùng lại ở phần sau |
| m5 | S1, S5 | L678, Hình 3, Bảng 4 (4.3.1) | "phân phối rỗng" | "phân phối dưới giả thuyết không (null distribution)" ở lần đầu, sau đó dùng một tên | "rỗng" dễ hiểu thành "trống" |
| m6 | Nguyên tắc 2, S1 | L309, L658 | "tỷ số Sharpe hiệu chỉnh" | "tỷ số Sharpe giảm phát (deflated Sharpe ratio)" ở lần đầu | Tên chung chung, mọi điều chỉnh đều là "hiệu chỉnh" |
| m7 | S3 | L580 | "nền tảng OSF Registries" | "nền tảng Open Science Framework (OSF) Registries" | Viết đầy đủ từ viết tắt |
| m8 | S5 | L162–163 | "hai đại lượng nhà đầu tư chỉ ước lượng được" | "hai đại lượng mà nhà đầu tư chỉ ước lượng được" | Thiếu "mà" |
| m9 | S5 | L305–306 | "nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ" | "nên tập lớn khi dữ liệu kém thông tin và nhỏ khi dữ liệu nhiều thông tin" | "cho" mơ hồ |
| m10 | S8 | L618 | "mô hình được chọn sau đó tái cân bằng" | "mô hình $c$ sau đó tái cân bằng" | Thống nhất "mô hình chọn trước $c$" |
| m11 | S8 | L312, L418 | "trạng thái thị trường" | "chế độ thị trường" | Một tên cho một khái niệm |
| m12 | S8 | L417 | "cơ sở của các cơ chế vững chắc" | "cơ sở của danh mục vững chắc" | Như trên |
| m13 | S8 | L211–212, L810–811, L900–902 | "công ty quản lý quỹ và tổ chức đầu tư cổ phiếu" / "tổ chức đầu tư và cơ quan giám sát" / "nhà nghiên cứu… và công ty quản lý quỹ" | Chốt một danh sách người dùng và dùng lại nguyên văn | Nhất quán đối tượng hưởng lợi |
| m14 | S10 | L165–168 & L269–270; L584–585, L739–743, L975–977; L752–754 & L973–975 | Kết quả DeMiguel, quy tắc "không kết luận", phương án dự phòng dữ liệu lặp lại | Giữ ở mục gốc, chỗ khác ghi "(xem mục 4.3.10)" | Mỗi kết quả/lập luận nêu một lần |
| m15 | S15, S4 | L573–575 | "chỉ ước lượng trực tiếp M~3~ khi tỷ lệ số cổ phiếu trên số quan sát tuần không vượt 0,5" | Thêm: "Với 30 cổ phiếu và 104 tuần, tỷ lệ là 0,29; ngưỡng chỉ có tác dụng trong kiểm tra độ bền (ví dụ dữ liệu tháng)" nếu đúng ý tác giả | Điều kiện hiện không bao giờ xảy ra ở cấu hình cơ sở |
| m16 | S18 | L754–755 | "Các mô hình ở Bảng 3 ước lượng được bằng phần mềm thống kê thông dụng." | "Sáu mô hình ở Bảng 3 ước lượng được bằng phần mềm thống kê thông dụng; M~5~ cần phương pháp Bayes xấp xỉ (xem dưới)." | Khớp với L758–760 |
| m17 | S13 | L171–179 | Câu định nghĩa rủi ro lựa chọn mô hình (65 âm tiết) | Tách: câu 1 định nghĩa; câu 2 "Đề tài đo tổn thất này bằng *mức hối tiếc*…" | Một ý một câu |
| m18 | S25, S28 | Hình 2, Hình 3 (trang 12, 14 bản dựng) | Dòng chú thích trong Hình 2; "quy tắc chế / độ" | Đưa chú thích của Hình 2 vào chú giải dưới hình; nới khung chữ Hình 3 | Đọc được khi in |
| m19 | M1 | Bìa L27; L25 | "HÀ NỘI -- 2026"; "Hạnh - Đại học Kinh tế Quốc Dân" | Theo đúng mẫu bìa của Trường (ví dụ "HÀ NỘI – 2026" nếu mẫu dùng gạch ngắn), dùng dấu phẩy thay gạch ở L25 | Chỉ ở bìa; giữ nếu mẫu bắt buộc |
| m20 | Base gate mục 5 | L1137, L892, L877, L171, L667, L714, L257 | 7 câu > 60 âm tiết | Tách thành hai câu; câu liệt kê (L1137, L714) có thể giữ theo ngoại lệ "danh sách" | Tiếng Việt: 60 âm tiết ≈ 40 từ tiếng Anh |
| m21 | Craft Part 2 | L777–784 và các đoạn 4.3.7, 4.3.10 | 4 câu liền mở "Đề tài…" | Đổi cấu trúc vài câu (đưa điều kiện hoặc đối tượng lên đầu) | Nhịp đơn điệu là dấu hiệu văn máy |
| m22 | Checklist related work | Mục 4.2 (L255–405) | 6 nhóm tài liệu; khoảng 12.084 ký tự | Tùy chọn: giữ, vì Bảng 1 đã gom về 4 nhóm; ngưỡng 10K ký tự của skill là cho bài hội nghị | Thể loại đề cương khác bài báo hệ thống |
| m23 | S11 | L159–160 | "Mô hình gốc của lĩnh vực này" | "Mô hình gốc của phân bổ danh mục" | Quy chiếu mơ hồ |
| m24 | S15 (quy trình) | L188, L165, L323, L345, L202–203, L207 | 151 khủng hoảng; 14 mô hình/7 bộ dữ liệu; 2%/10%; 299 công ty; SR 26-2; Thông tư 83/2025 | Đối chiếu từng con số với toàn văn/văn bản gốc trước khi nộp | Reviewer không dùng mạng nên không kiểm chứng; thí sinh nói mới đọc chủ yếu tóm tắt |
| m25 | S28 | Trang 12 bản dựng LibreOffice | Công thức (5) và ký hiệu toán trong dòng không hiện | Kiểm bản PDF xuất từ Word trước khi nộp | Có thể là lỗi của LibreOffice, chưa phải lỗi tệp |

### Phát hiện ghi nhận nhưng **xung đột với nguyên tắc tác giả — không khuyến nghị áp dụng**

- M11 "active voice, no exceptions": ≈10 câu bị động thật ("H~1~ được ủng hộ", "bị loại", "được chấp nhận đăng"). Đây là văn phong học thuật tiếng Việt chuẩn.
- "Zero hedging" (SKILL.md, craft_reference): 48 dấu rào ("có thể", "dự kiến", "ở mức thăm dò", "theo hiểu biết của thí sinh"). Giữ; S18 còn yêu cầu thêm rào ở J8–J10.
- M13: "thường", "gần như" (L299, L323, L327) phản ánh đúng mức chắc chắn của nguồn.
- S23 / Nguyên tắc 3 "headings are claims": tiêu đề mục do mẫu hồ sơ của Trường quy định.
- S20 positives-first: giới hạn công suất (L226–228) và lời thừa nhận mới đọc tóm tắt (L403–405) là hedging trung thực.
- Introduction Move 5–6, "We show", Results Preview, Takeaway: đề cương chưa có kết quả; "Đóng góp dự kiến" viết có điều kiện ("Nếu dữ liệu ủng hộ…") là đúng.
- Câu trung bình ~21 từ: trung bình 25,8 âm tiết tiếng Việt, đã đạt.
- Pipeline viết hai lần phần mở đầu, nén 30–50%, `\smartparagraph`, checklist LaTeX trước khi nộp: không áp dụng cho red-team một đề cương .docx.

---

## 4. Kết luận closure gate (S31)

**CHƯA CLEAN.** Còn 4 NGHIÊM TRỌNG và 21 ĐÁNG SỬA (25 CHỈNH NHẸ). Theo S31, văn bản chỉ CLEAN khi một closure reviewer độc lập đọc lại toàn bộ sau khi sửa và trả về 0 CRITICAL/MAJOR. Báo cáo này là vòng red-team thứ nhất; chưa có vòng sửa và chưa có vòng closure.

---

## 5. Vấn đề thiết kế cốt lõi — chờ tác giả duyệt

Các điểm dưới đây chạm đến thiết kế; reviewer chỉ nêu, không đề xuất đổi câu hỏi, giả thuyết, mô hình, dữ liệu hay kiểm định.

- **D1. Phép phân rã β0 − β1 (L688–691).** β0 là hệ số khi không có $X_t$, mà $X_t$ luôn chứa biến động thực hiện (L675). Vì vậy "phần chênh lệch do các biến kênh giải thích" gồm cả phần của biến động, trong khi CH2 hỏi phần giải thích *sau khi kiểm soát* biến động. Tác giả quyết định β0 có chứa biến động hay không.
- **D2. Phạm vi H3.** (a) Cơ chế (iii) có thuộc H3 không (C2). (b) Cơ chế (ii) và (iii) trùng gần như hoàn toàn với M~6~ và M~7~ trong tập *M*; khi loại chúng khỏi *M* (L710–712), chuẩn "chọn một mô hình" là chọn trong 7 hay 5 mô hình (J15).
- **D3. Trọng số Bayes cho quy tắc danh mục.** Hoeting và cộng sự (1999), Avramov (2002) tính trọng số hậu nghiệm cho mô hình dự báo lợi suất có hàm hợp lý; các quy tắc danh mục M~1~–M~7~ không có hàm hợp lý chung. Cần xác định trọng số cơ chế (i) tính từ đâu, và phương án nào ("Bayes" hay "trong tập tin cậy") là phương án chính để đăng ký trước.
- **D4. Công suất thực tế.** Khoảng 28 cửa sổ từ khoảng 2012 (khủng hoảng 2008 chỉ phục vụ ước lượng chế độ, L641–642). Với vài giai đoạn căng thẳng sau 2012, quy tắc "dưới 10 cửa sổ căng thẳng → không kết luận" có thể khiến H1 không kết luận ngay từ thiết kế. Mẫu kiểm tra sau ngày đăng ký (đăng ký quý 4 năm 1) chỉ có vài cửa sổ. Tác giả đã dự kiến báo cáo số giai đoạn trước khi ước lượng; cần quyết định trước khi đăng ký.
- **D5. Họ kiểm định và mức ý nghĩa.** Holm 10% cho bốn giả thuyết, gồm H4 thăm dò; tập tin cậy mô hình ở 10%; ngưỡng phân vị 95% của phân phối dưới H0 cho H1. Cần một bộ mức ý nghĩa nhất quán.
- **D6. Cách hiểu vai trò biến kênh.** Hình 1 vẽ H2/H4 như biến điều tiết (mũi tên chỉ vào mũi tên H1); phương trình (5) và β0 − β1 kiểm định phần chênh lệch được giải thích (gần với trung gian). Cách sửa chữ ở J1 phụ thuộc lựa chọn này.
- **D7. Thứ hạng mô hình.** Khoảng trống nói về thay đổi thứ hạng (L222–223, L329–330) nhưng không có thước đo độ ổn định thứ hạng. Tác giả chọn giữa sửa chữ (J11) hoặc thêm một thống kê mô tả thứ hạng.
- **D8. Tái ước lượng trong cửa sổ đánh giá.** Mỗi lần tái cân bằng tháng trong cửa sổ 6 tháng, mô hình có ước lượng lại trên 104 tuần trượt không (L616–618, L636–637)? Cần cố định trong tệp đăng ký trước.
- **D9. Định nghĩa đơn vị "cửa sổ/giai đoạn căng thẳng độc lập"** (J5): ngưỡng của $S_t$ là một lựa chọn thiết kế cần đăng ký trước.
- **D10. Khả thi (ngoài văn phong).** Mục 8.2 (L1108–1111) cho biết thí sinh đồng thời học ba chương trình khác (Kế toán vừa làm vừa học, Công nghệ thông tin từ xa, thạc sĩ WorldQuant). Hội đồng có thể hỏi về thời gian dành cho luận án; tác giả cân nhắc có giải thích kế hoạch thời gian hay không.

---

## 6. Bằng chứng tuân thủ

### 6.1 Các bước của `red_team_protocol.md` (theo thứ tự)

| # | Bước | Trạng thái | Bằng chứng (trích ngắn từ đề cương / ghi chú) |
|---|---|---|---|
| 1 | **When**: chạy sau gate cơ học + style audit của tác giả, trước khi trình người dùng | Đã làm (đúng thời điểm Cổng 2) | Văn bản là bản tác giả đã hoàn thiện: "*Hà Nội, ngày 30 tháng 9 năm 2026*" (L1378) |
| 2 | Gate 1 **WRITE**: tác giả viết bản thảo | Không thuộc reviewer (đã có sẵn) | "**RỦI RO LỰA CHỌN MÔ HÌNH TRONG QUẢN TRỊ DANH MỤC ĐẦU TƯ THEO CHẾ ĐỘ THỊ TRƯỜNG…**" (L10–11) |
| 3 | Gate 2 **MECHANICAL** do tác giả chạy, dán output | CHƯA LÀM (phía tác giả) / không kiểm được | Không có output của tác giả trong dữ liệu đầu vào; theo giao thức, reviewer không được xem tự đánh giá của tác giả nên không mở `reviews/` hay `reports/` |
| 4 | Gate 3a: reviewer **tự chạy lại** grep `gate_mechanical.md` (gạch dài, phản đề, từ nhấn, từ cấm/kêu/hoa mỹ, bị động, thừa chữ) | Đã làm | Mục 1, bảng M1–M18 có số đếm; ví dụ M1 = 0 trong thân, M16 trúng "chế độ thị trường tác động lên rủi ro lựa chọn mô hình" (L435) |
| 5 | Gate 3b: áp `gate_semantic.md` S1–S31 với lăng kính người đọc mới | Đã làm | Mục 2, đủ 31 mục; ví dụ S21: "chưa đo cho quyết định phân bổ" (L276) |
| 6 | Gate 3c: nhất quán từ vựng + phân rã, không trùng lặp, mappability, định vị trung thực, nói thẳng danh từ | Đã làm | S8/S9/S10/S15/S21/S12 ở mục 2; ví dụ "gồm biến động, thanh khoản, tương quan cực trị và bầy đàn" (L251–252) |
| 7 | Gate 3d: săn bốn lớp lỗi (giọng máy, khó tiếp cận, thiếu mạch lạc, phi logic) | Đã làm | Mục 2, "Bốn lớp lỗi"; ví dụ phi logic: "khi đó rủi ro lựa chọn mô hình không đổi theo chế độ" (L748–749) |
| 8 | Gate 3e: từ chối cho qua cho đến khi sạch; trả danh sách phát hiện có mã quy tắc, dòng, cách sửa | Đã làm | Mục 3: 50 phát hiện, mỗi mục có M#/S#, số dòng, đề xuất sửa; kết luận CHƯA CLEAN |
| 9 | **Evidence rule**: dán grep + findings làm hồ sơ; không báo clean khi chỉ đọc nhẩm | Đã làm (lần đầu chỉ dán số đếm; output nguyên văn bổ sung ở bước 12) | Số đếm grep ở mục 1 (ví dụ M11 = 26 khớp/25 câu; M2 = 15 câu); script ở `scratchpad/g2rt/` |
| 10 | **How to run**: reviewer tách biệt, chỉ nhận văn bản + checklist + controlling idea, không xem tự đánh giá của tác giả | Đã làm | Subagent riêng; controlling idea = tên đề tài + 3 câu hỏi (ghi ở đầu báo cáo); không mở `scratchpad/paper/reviews/` và `reports/` |
| 11 | Tác giả sửa mọi phát hiện, vòng lặp lặp lại đến khi reviewer trả clean | CHƯA LÀM | Ngoài phạm vi: nhiệm vụ cấm sửa file đề cương; cần vòng sau |
| 12 | **Gate 2 / Evidence rule: "PASTE the raw output (hit counts + lines)… 'Audited' without pasted output is INVALID"**. Chạy lại grep M1–M18 và dán nguyên văn mọi dòng trúng | LÀM | Phụ lục "Output grep nguyên văn (M1–M18)" ở cuối báo cáo. Có mọi dòng trúng của mỗi mã, đặt trong khối code, kèm bảng đối chiếu số đếm. Ví dụ M11 dán đủ 25 câu/26 khớp, trong đó "Đề tài coi H~1~ được ủng hộ khi thỏa đồng thời ba điều kiện" (L677). Số đếm khớp §1. Đã sửa phần phân loại của M11, M12, M16 |

Chạy lại lần 1 sau kiểm toán Cổng 3 (2026-10-14).

### 6.2 Các bước MUST của `SKILL.md` áp dụng cho review

| Bước | Trạng thái | Bằng chứng / lý do |
|---|---|---|
| 1. Đọc SKILL.md | Đã làm | Nạp qua công cụ Skill ("Launching skill: paper-writing-skill") |
| 2. Đọc toàn bộ `author_profile/` | Đã làm | 7/7 file (danh sách ở trên) |
| 3. Hỏi người dùng đang làm bài nào | CHƯA LÀM | Nhiệm vụ cấm hỏi người dùng; bài được chỉ định sẵn: "Tên đề cương nghiên cứu (không quá 30 từ): Rủi ro lựa chọn mô hình…" (L29–31) |
| 4. Tìm `project_context.md` | Đã làm (không tìm thấy) | `find` trên scratchpad và repo (trừ `reports/` và thư mục skill): không có `project_context.md` |
| 5. Nếu có thì đọc như ràng buộc | Không áp dụng | Không có file |
| 6. Nếu không có thì chạy Structured Brainstorming (đọc `brainstorming_guide.md`, 6 pha tương tác, tạo `project_context.md`) | Đã đọc hướng dẫn; CHƯA LÀM phần tương tác và chưa tạo file | Nhiệm vụ cấm hỏi người dùng và cấm sửa văn bản; thay bằng identity sentence = tên đề tài + 3 câu hỏi: "Câu hỏi 1: Rủi ro lựa chọn mô hình thay đổi thế nào giữa chế độ bình thường và chế độ căng thẳng?" (L233–234) |
| 7. Tìm artifact của skill anh em (`exploration_log.md`, `braindump.md`, `plot_context.md`, WALTER, ghi chú survey) | Đã làm (không tìm thấy) | `find` không trả kết quả nào |
| Review: đọc `intervention_types.md`, áp theo thứ tự framing → cấu trúc → xoá nền → tăng cường đánh giá → thuật ngữ → claim-first → nén | Đã làm | Loại 1 framing: ổn định, không đề xuất đổi. Loại 2 cấu trúc: do mẫu hồ sơ quy định. Loại 3 xoá nền: J21, m4 ("đặt nền móng cho lý thuyết triển vọng", L332). Loại 4 tăng cường đánh giá: J20 (bảng quy tắc kết luận). Loại 5 thuật ngữ: J18, J19, m10–m13. Loại 6 đóng góp: không áp dụng (chưa có kết quả). Loại 7 làm rõ lập luận: J11, J16 |
| Review: ghi mức CRITICAL/MAJOR/MINOR và số nguyên tắc từ `editorial_principles.md` | Đã làm | Mỗi phát hiện có M#/S#; Nguyên tắc 2 (named over vague) ở m6; Nguyên tắc 3 ở mục xung đột; Nguyên tắc 14 (trích dẫn): kiểm khớp trích dẫn trong thân với danh mục, 53 mục tài liệu, 0 trích dẫn thiếu, 0 mục không được trích |
| Section checklists (`writing_checklists/*.md`) và `section_rhetorical_moves/*.md` | Đã làm, quy đổi mục | Introduction ↔ 4.1 (Stakes: "Tổ chức đầu tư phân bổ vốn bằng mô hình thống kê"; Gap có đánh số: "Tài liệu hiện có để ngỏ hai vấn đề"; Key abstraction: "rủi ro lựa chọn mô hình"; Results preview: không áp dụng). Related work ↔ 4.2 (6 nhóm, Bảng 1 gom 4; câu định vị L394–398 → J9, m22). Design/Evaluation ↔ 4.3 (baseline có tên M~1~–M~7~; thước đo được biện minh: "Tỷ số Sharpe không phù hợp làm thước đo chính, vì…" L593; ablation: "tập chỉ gồm các mô hình tĩnh" L685; robustness: "các định nghĩa chế độ thay thế" L744) |
| Mandatory Style Audit (a)(b)(c) trước khi trình/commit nội dung mới | Không áp dụng phần (a)(b) cho người viết; phần (c) red-team là chính báo cáo này | Reviewer không tạo hay sửa văn bản đề cương |
| `figure_synthesis_guide.md` (critique) và S28 kiểm bằng mắt | Đã làm phần kiểm bằng mắt; CHƯA LÀM spec/generate | Đã dựng PDF từ docx và xem Hình 1–3 (trang 10, 15, 17 bản dựng; trang 7, 12, 14 theo số in); không có `figure_spec.md`, và nhiệm vụ không yêu cầu tạo hình |
| `loop_mode.md` (ledger `notes/AUDIT_LEDGER.md`) | CHƯA LÀM | Không được gọi qua `/loop`; tạo ledger sẽ phải ghi vào thư mục bài, trái với lệnh không sửa file đề cương |
| Compression (Stage 5), Pre-Submission Mechanical Checklist (LaTeX) | Không áp dụng | Văn bản là .docx, không phải bài .tex nộp hội nghị; trang số: bản dựng 30 trang |
| `setup` | Không chạy | Theo lệnh: không chạy mã chưa đọc |

---

## Phụ lục — Output grep nguyên văn (M1–M18)

*Chạy lại lần 1 sau kiểm toán Cổng 3 (2026-10-14).* Phụ lục này bổ sung phần còn thiếu theo evidence rule của `red_team_protocol.md` ("PASTE the raw output (hit counts + lines)"). Mọi dòng trúng được dán nguyên văn, không cắt.

**Đầu vào và cách chạy**
- Văn bản: `scratchpad/paper/de-cuong-goc.md`, SHA-256 `ac4c0ea1cb2ddca5aac07424c3da9532eccfb98bef8eb4c5c3602603889eb9f9`. Phạm vi dòng 155–1160, giống lần chạy gốc.
- Script: đọc toàn văn `scratchpad/g2rt/g.sh`, `gate.py`, `rules.py` trước khi chạy. Cả ba chỉ xử lý văn bản cục bộ, không dùng mạng. Chạy bằng `python3 -I`. Output lưu ở `scratchpad/g2rt-rerun/`.
- M1: `g.sh` (grep theo dòng). Vì `g.sh` dùng `grep -o` nên chỉ in đoạn khớp; phụ lục dán thêm dòng đầy đủ.
- M2–M18 (trừ M7, M14): regex nguyên văn trong `rules.py`, áp lên từng câu của `g2rt/sents.json`. Đây đúng là tệp câu mà lần chạy gốc dùng. Wrapper `g2rt-rerun/dump.py` lấy nguyên khối `R` từ `rules.py` và chỉ đổi phần in: in **toàn bộ** câu trúng, kèm mọi đoạn khớp, thay vì 8 câu đầu cắt 60 ký tự.
- Ghi chú về tách câu: chạy lại `gate.py` từ đầu ra 331 câu, còn `g2rt/sents.json` gốc có 332 câu, vì bản gốc đã được chỉnh tay chỗ tách câu (L201, L275, L1131 tách đúng ở "Ở…"; L1151, L1157 gộp "GS.TS."/"PGS.TS."). Đã chạy `rules.py` trên cả hai: số đếm M2–M18 **giống hệt nhau**. Chỉ dòng Hedging (S18, ngoài M1–M18) lệch 43 so với 44 câu, còn số khớp vẫn là 48. Phụ lục dùng tệp gốc.
- Số dòng `Lxxx` trong output của `rules.py` là **dòng đầu đoạn** chứa câu, không phải dòng của chính câu đó. Bảng §1 dùng dòng thật, nên có thể lệch vài dòng (ví dụ M11 L171 trong output ứng với L183 ở §1).
- M7 (bộ ba trang trí) và M14 (trạng từ tự chế) không có grep tiếng Việt; §1 đã khai là đọc tay. Grep nguyên mẫu M14 trên `main.tex` cho 0 dòng (xem Part C bên dưới).

### Đối chiếu số đếm với bảng §1

| Mã | §1 ghi | Chạy lại | Khớp |
|---|---|---|---|
| M1 | Unicode 0; `' -- '` 0; `---` 505 lần, 0 ngoài dòng kẻ bảng; `số--số` 21; `' - '` 8 | 0; 0; 505 lần, 0; 21; 8 | Khớp |
| M2 | 15 câu | 15 khớp / 15 câu | Khớp |
| M3 | 0 | 0 | Khớp |
| M4 | 1 | 1 | Khớp |
| M5 | 15 câu (13 thuật ngữ, 2 thật) | 15 / 15 (13 + 2) | Khớp |
| M6 | 1 | 1 | Khớp |
| M8 | 0 | 0 | Khớp |
| M9 | 6 (5 câu) | 6 / 5 | Khớp |
| M10 | 0 | 0 | Khớp |
| M11 | 26 (25 câu); "bị động thật ≈10" | 26 / 25; bị động thật **9** | Số đếm khớp; phần phân loại **đã sửa** ≈10 thành 9 |
| M12 | 40 (37 câu); "~28 cộng sự, ~11 việc + động từ" | 40 / 37; cộng sự 21, công/làm việc 3, việc + V/N 12, sự khác 2, một cách 1, đối với 1 | Số đếm khớp; phần phân loại **đã sửa** |
| M13 | 3 | 3 | Khớp |
| M15 | 3 `?` + 1 `!` (tên bài) | 3 `?`; `!` = 1 dòng trên main.tex (L1537, tên bài) | Khớp |
| M16 | 9 (3 thật; còn lại là mô tả nguồn/mức ý nghĩa) | 9 (3 thật; 2 mô tả nguồn; 2 mức ý nghĩa; 2 "tác động" kỹ thuật của tác giả) | Số đếm khớp; phần mô tả **đã sửa** |
| M17 | 1 | 1 | Khớp |
| M18 | 0 / 0 | 0 / 0 | Khớp |
| Độ dài câu | 332 câu, TB 25,8; >40: 56; >50: 24; >60: 7 | Trên `sents.json` gốc: 332; 25,8; 56; 24; 7 | Khớp (chạy lại `gate.py` từ đầu: 331; 25,9; 56; 25; 10, do khác tách câu như ghi ở trên) |

Chỉnh sửa thân báo cáo: chỉ sửa câu phân loại trong các ô "Đánh giá" của M11, M12, M16 ở §1. Mỗi chỗ sửa có ghi chú "[sửa sau kiểm toán Cổng 3]". Không đổi số đếm, mức độ hay phát hiện nào.

### M1 — gạch dài (g.sh, dòng 155–1160)

```text
### M1 (g.sh, dòng 155–1160 của de-cuong-goc.md)
== M1 unicode —/– : 0 hits

== M1 ' -- ' : 0 hits

== M1 '---' tổng số lần (dòng 155–1160):
505
== M1 '---' trên dòng KHÔNG phải dòng kẻ bảng (chỉ gồm - và khoảng trắng):
== M1 số--số : 21 hits
189:0--2
192:5--2
197:7--2
346:5--2
350:1--2
353:5--1
354:2--2
359:9--2
577:9--2
640:7--2
949:1--2
952:9--2
958:1--2
959:3--4
962:1--2
963:3--4
966:1--2
967:3--4
1001:2--6
1009:1--9
1104:2--2
== M1 ' - ' : 8 hits
606: - 
613: - 
613: - 
623: - 
689: - 
999: - 
1013: - 
1048: - 

### M1 ngoài thân (dòng 1–154), tham khảo
25:**- PGS.TS. Hà Hồng Hạnh - Đại học Kinh tế Quốc Dân**
27:**HÀ NỘI -- 2026**
```

Dòng đầy đủ của các hit `số--số` và `' - '`:

```text
== M1 số--số, dòng đầy đủ
189:giai đoạn 1970--2017. Thị trường chứng khoán Việt Nam trải qua ít nhất
192:liệu 2005--2015. Dao và cộng sự (2021) cho thấy số ca mắc COVID-19 hằng
197:cổ phiếu giai đoạn 2007--2022 lan truyền giữa các ngành. Những cú sốc
346:(HOSE) giai đoạn 2005--2015 và tìm thấy bầy đàn, rõ hơn khi thị trường
350:2011--2019 và thu được danh mục có lợi nhuận cao hơn, rủi ro thấp hơn
353:VN100 giai đoạn 01/2015--11/2023. Hoang và Luu (2024), trong một bản
354:thảo công bố trực tuyến, phân tích VN-Index giai đoạn 2012--2023 và thấy
359:2019--2025 và chỉ đánh giá một mô hình.
577:Thí sinh đã dùng dữ liệu Việt Nam giai đoạn 2019--2025, gồm hai giai
640:năm của mẫu. Với mẫu 2007--2026, đề tài dự kiến có khoảng 28 cửa sổ đánh
949:        lượng của công ty quản lý quỹ. Quý 1--2: học bổ  ký trước; bộ dữ
952:        giai đoạn 2019--2025 để đo thời gian tính và số  
958:  Năm 2 Quý 1--2: xác định chế độ thị trường và ước      Bài báo 1; báo
959:        lượng bảy mô hình. Quý 3--4: đo rủi ro lựa chọn  cáo hội thảo;
962:  Năm 3 Quý 1--2: phân tích các biến kênh (H~2~, H~4~).  Bài báo 2 và 3
963:        Quý 3--4: đánh giá cơ chế giảm thiểu (H~3~),     
966:  Năm 4 Quý 1--2: hoàn thiện các chương, phần kết luận   Luận án
967:        và hàm ý quản trị. Quý 3--4: chỉnh sửa theo góp  
1001:       hạn, hiệu quả hoạt động và ổn 9, tr. 52--64; DOI                
1009:       portfolio optimization using  3, Số 1, tr. 81--99; DOI          
1104:khóa 2022--2026 tại Học viện Chính sách và Phát triển, xếp loại Giỏi
== M1 ' - ', dòng đầy đủ
606:$U_{m,t} = \mu_{m,t} - \frac{\rho}{2}\,\sigma_{m,t}^{2}$ (1)
613:$D_{t} = \sqrt{\frac{1}{|M| - 1}\sum_{m \in M}^{}\left( U_{m,t} - {\overline{U}}_{t} \right)^{2}}$
623:$R_{t} = U_{o,t} - U_{c,t}$ (4)
689:thích bằng hiệu $\beta_{0} - \beta_{1}$, trong đó $\beta_{0}$ và
999:  1    Nguyễn Thanh Bình, Nguyễn Văn Tạp chí Kinh tế - Luật và Ngân    Đã công bố
1013:       market period 2019 - 2025"                                      
1048:  2    Tác động của cấu trúc  2     Tạp chí Kinh tế -   Qua 2 vòng phản      Không
```

Phân loại: 21 hit `số--số` là gạch nối khoảng số/năm/trang, hợp lệ. 8 hit `' - '` gồm 5 dấu trừ trong công thức (L606, L613 ×2, L623, L689), 2 tên tạp chí "Kinh tế - Luật" (L999, L1048) và 1 tên bài giữ nguyên (L1013). Thân văn bản sạch. Ngoài thân: bìa L27 "HÀ NỘI -- 2026", 1 MINOR.

### M2 (phản đề / phủ định tu từ)

```text
== M2 antithesis/negation-as-rhetoric: 15 matches in 15 sentences
L171: Độ phân tán giữa các mô hình và kích thước tập tin cậy mô hình chỉ báo hiệu mức bất định, không đo rủi ro.  [khớp: ', không ']
L218: Danielsson và cộng sự, 2016) đo chênh lệch giữa các dự báo rủi ro, chưa đo hậu quả của việc chọn sai mô hình lên trọng số và kết quả danh mục.  [khớp: ', chưa ']
L218: Garlappi và cộng sự, 2007) xếp hạng mô hình theo bình quân toàn mẫu, chưa xét thứ hạng thay đổi ra sao khi thị trường chuyển chế độ.  [khớp: ', chưa ']
L275: Các thước đo trong nhóm này gắn với dự báo rủi ro và định giá; chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục.  [khớp: '; chưa ']
L314: Hành vi thị trường đổi theo chế độ; chưa nghiên cứu nào kiểm định thứ hạng của các mô hình danh mục có đổi theo hay không.  [khớp: '; chưa ']
L332: Bầy đàn, tức nhà đầu tư làm theo số đông thay vì dựa vào thông tin riêng, là một kênh hành vi có thể làm các mô hình cho kết quả khác nhau.  [khớp: 'thay vì']
L394: Bốn khoảng trống có chung một điểm: các công trình đo từng mô hình, từng chế độ hoặc từng hiện tượng riêng lẻ, chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường.  [khớp: ', chưa ']
L394: Theo hiểu biết của thí sinh, chưa có nghiên cứu nào đo rủi ro lựa chọn mô hình theo chế độ thị trường cho quyết định phân bổ danh mục trên thị trường chứng khoán Việt Nam.  [khớp: ', chưa ']
L497: Đề tài dùng phương pháp định lượng trên dữ liệu thị trường công khai, không dùng khảo sát hay phương pháp định tính.  [khớp: ', không ']
L521: Kiểm định điểm gãy của Bai và Perron (1998) trên toàn mẫu chỉ dùng để mô tả và đối chiếu với các cú sốc lịch sử, không dùng làm biến chế độ trong kiểm định giả thuyết.  [khớp: ', không ']
L688: Đề tài gọi các kết quả này là liên hệ có điều kiện, không gọi là quan hệ nhân quả.  [khớp: ', không gọi là']
L738: Khi số cửa sổ độc lập ở chế độ căng thẳng dưới 10, đề tài gọi kết quả là không kết luận, không gọi là ủng hộ hay bác bỏ, và đề tài báo cáo kích thước hiệu ứng cùng khoảng tin cậy theo từng giai đoạn.  [khớp: ', không gọi là']
L789: So với bài báo của chính thí sinh (Nguyen và Nguyen, 2026a), đề tài đặt M~5~ cạnh sáu mô hình khác, mở mẫu về trước năm 2019 nếu dữ liệu cho phép và đo chênh lệch giữa các mô hình thay vì đánh giá riêng M~5~.  [khớp: 'thay vì']
L802: Thủ tục này suy ra từ H~3~, chưa qua kiểm nghiệm với người dùng, và chỉ là tư liệu tham khảo cho tổ chức đầu tư và cơ quan giám sát.  [khớp: ', chưa ']
L1016: ISSN          2026, chưa brownwashing:  [khớp: ', chưa ']
```

Phân loại: 15/15 là ranh giới khái niệm/phạm vi/khoảng trống thật, giữ (đúng như bảng §1). L1016 là dòng bảng tài liệu (tên bài "…chưa brownwashing"), dương tính giả do tách câu.

### M3 (câu kết bình luận)

```text
== M3 editorializing closer: 0 matches in 0 sentences
```

### M4 (từ nhấn rỗng)

```text
== M4 vacuous intensifiers: 1 matches in 1 sentences
L159: Khung này cần lợi suất kỳ vọng và ma trận hiệp phương sai, hai đại lượng nhà đầu tư chỉ ước lượng được, và sai số ước lượng truyền thẳng sang trọng số danh mục (Michaud, 1989;  [khớp: 'thẳng ']
```

Phân loại: 1 hit "truyền thẳng" (L159, dòng thật L163). Đúng như bảng §1.

### M5 (tính từ cấm)

```text
== M5 banned adjectives: 15 matches in 15 sentences
L186: Khủng hoảng làm câu hỏi chọn mô hình trở nên cấp bách.  [khớp: 'cấp bách']
L186: Quỹ Tiền tệ Quốc tế ghi nhận thị trường trái phiếu doanh nghiệp đóng băng trong quý IV/2022, với bất động sản chiếm tỷ trọng lớn nhất trên thị trường này (International Monetary Fund, 2023).  [khớp: 'lớn nhất']
L257: Tối ưu hóa trung bình-phương sai dồn trọng số vào những tài sản có sai số ước lượng lớn (Michaud, 1989), và việc thay tham số tổng thể bằng ước lượng mẫu làm hiệu quả ngoài mẫu giảm mạnh (Kan và Zhou, 2007).  [khớp: 'giảm mạnh']
L257: Dù vậy, DeMiguel và cộng sự (2009) không thấy hướng nào vượt 1/N trên cả bảy bộ dữ liệu, và Pflug và cộng sự (2012) chứng minh quy tắc 1/N xấp xỉ tối ưu theo nghĩa vững chắc khi mức mơ hồ về mô hình đủ cao.  [khớp: 'vững chắc']
L275: Ở cấp lý thuyết quyết định, Gilboa và Schmeidler (1989) xây dựng tiêu chí chọn phương án tốt nhất trong tình huống xấu nhất khi nhà đầu tư có nhiều niềm tin tiên nghiệm, và Hansen và Sargent (2008) phát triển lý thuyết kiểm soát vững chắc trước sai đặc tả.  [khớp: 'vững chắc']
L332: Christie và Huang (1995) đo bầy đàn bằng độ phân tán chéo của lợi suất và không thấy bầy đàn khi giá biến động mạnh trên dữ liệu Mỹ.  [khớp: 'biến động mạnh']
L411: Hansen và Sargent, 2008), cung cấp cách đo tổn thất của một lựa chọn so với lựa chọn tốt nhất nhìn lại sau thực tế và là cơ sở của các cơ chế vững chắc.  [khớp: 'vững chắc']
L497: Tại mỗi ngày tái cân bằng, rổ cổ phiếu gồm 30 mã có giá trị giao dịch bình quân ba tháng và vốn hóa tự do chuyển nhượng lớn nhất, xác định chỉ bằng dữ liệu có tại ngày đó để tránh thiên lệch sống sót và thiên lệch nhìn trước.  [khớp: 'lớn nhất']
L536: Tập này bao phủ các hướng chính của tài liệu: quy tắc đơn giản, co rút hiệp phương sai, tối ưu hóa cổ điển, mô hình Black-Litterman, danh mục vững chắc và chiến lược theo chế độ.  [khớp: 'vững chắc']
L591: Tỷ số Sharpe không phù hợp làm thước đo chính, vì khi lợi suất vượt trội trung bình âm (đúng tình huống của chế độ căng thẳng) danh mục biến động hơn lại có tỷ số Sharpe ít âm hơn.  [khớp: 'vượt trội']
L591: Đề tài chỉ báo cáo tỷ số Sharpe như thước đo phụ, ở các cửa sổ có lợi suất vượt trội trung bình dương.  [khớp: 'vượt trội']
L625: Kỳ vọng của <EQ> vẫn dương khi các mô hình ngang chất lượng, vì giá trị lớn nhất của các đại lượng có nhiễu tăng theo phương sai của nhiễu.  [khớp: 'lớn nhất']
L654: Để kiểm định H~1~, H~2~ và H~4~, đề tài hồi quy các thước đo rủi ro mô hình theo biến chế độ và các biến kênh, với sai số chuẩn bền vững trước phương sai thay đổi và tự tương quan.  [khớp: 'bền vững']
L703: Cơ chế (ii) là danh mục vững chắc, tối ưu hóa cho tình huống xấu nhất trong nhiều niềm tin tiên nghiệm (Garlappi và cộng sự, 2007).  [khớp: 'vững chắc']
L714: Tiêu chí đánh giá gồm lợi suất tương đương chắc chắn, mức hối tiếc, độ sụt giảm tối đa (mức giảm lớn nhất từ đỉnh), giá trị thiệt hại kỳ vọng mức 95% (tổn thất trung bình trong 5% số ngày xấu nhất), vòng quay (tỷ lệ danh mục được mua bán lại) và hiệu quả sau chi phí giao dịch.  [khớp: 'lớn nhất']
```

Phân loại: 2 hit thật là "cấp bách" (L186) và "giảm mạnh" (L257, dòng thật L260). 13 dương tính giả do là thuật ngữ hoặc mô tả: "lớn nhất" ×4 (L186, L497, L625, L714), "vững chắc" ×5 (L257, L275, L411, L536, L703; nghĩa là robust), "vượt trội" ×2 (L591; excess return), "bền vững" ×1 (L654; sai số chuẩn bền vững), "biến động mạnh" ×1 (L332; mô tả Christie và Huang 1995).

### M6 (mở câu rào đón)

```text
== M6 throat-clearing opener: 1 matches in 1 sentences
L257: Dù vậy, DeMiguel và cộng sự (2009) không thấy hướng nào vượt 1/N trên cả bảy bộ dữ liệu, và Pflug và cộng sự (2012) chứng minh quy tắc 1/N xấp xỉ tối ưu theo nghĩa vững chắc khi mức mơ hồ về mô hình đủ cao.  [khớp: 'Dù vậy']
```

Phân loại: 1 hit "Dù vậy" (L257, dòng thật L269). Giữ vì có tương phản logic thật.

### M8 (câu dựng thế rỗng)

```text
== M8 grandiose setup: 0 matches in 0 sentences
```

### M9 (ẩn dụ trang trí)

```text
== M9 metaphor filler: 6 matches in 5 sentences
L159: Khung này cần lợi suất kỳ vọng và ma trận hiệp phương sai, hai đại lượng nhà đầu tư chỉ ước lượng được, và sai số ước lượng truyền thẳng sang trọng số danh mục (Michaud, 1989;  [khớp: 'truyền thẳng']
L186: Quỹ Tiền tệ Quốc tế ghi nhận thị trường trái phiếu doanh nghiệp đóng băng trong quý IV/2022, với bất động sản chiếm tỷ trọng lớn nhất trên thị trường này (International Monetary Fund, 2023).  [khớp: 'đóng băng']
L186: Vu và cộng sự (2024) cho thấy các đợt sụt giảm giá cổ phiếu giai đoạn 2007--2022 lan truyền giữa các ngành.  [khớp: 'lan truyền']
L257: Tối ưu hóa trung bình-phương sai dồn trọng số vào những tài sản có sai số ước lượng lớn (Michaud, 1989), và việc thay tham số tổng thể bằng ước lượng mẫu làm hiệu quả ngoài mẫu giảm mạnh (Kan và Zhou, 2007).  [khớp: 'dồn trọng số']
L332: *(5) Tài chính hành vi và bầy đàn.* Kahneman và Tversky (1979) đặt nền móng cho lý thuyết triển vọng, và Barberis và Thaler (2003) tổng hợp hai trụ cột của tài chính hành vi là giới hạn của kinh doanh chênh lệch giá và tâm lý nhà đầu tư.  [khớp: 'nền móng' | 'trụ cột']
```

Phân loại: "truyền thẳng" (L159), "đóng băng" (L186), "lan truyền" (L186), "dồn trọng số" (L257) là cách nói của nguồn, giữ. "nền móng" và "trụ cột" (L332) là 2 hit MINOR.

### M10 (động từ thổi phồng)

```text
== M10 hype verbs: 0 matches in 0 sentences
```

### M11 (bị động)

```text
== M11 passive (được/bị/bởi): 26 matches in 25 sentences
L159: Khung này cần lợi suất kỳ vọng và ma trận hiệp phương sai, hai đại lượng nhà đầu tư chỉ ước lượng được, và sai số ước lượng truyền thẳng sang trọng số danh mục (Michaud, 1989;  [khớp: 'được']
L171: Đề cương cũng phân biệt *khủng hoảng*, một sự kiện lịch sử, với *chế độ căng thẳng*, một trạng thái thống kê có biến động cao và lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng.  [khớp: 'do mô hình']
L186: Những cú sốc này là các giai đoạn tham chiếu để kiểm tra xem chế độ căng thẳng do mô hình ước lượng có trùng với biến cố thực tế hay không.  [khớp: 'do mô hình']
L236: Sau khi kiểm soát biến động thực hiện, các biến kênh (thanh khoản, tương quan cực trị và, ở mức thăm dò, hành vi bầy đàn) có liên hệ thống kê với rủi ro lựa chọn mô hình không, và chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?  [khớp: 'được']
L241: Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?  [khớp: 'được']
L257: Garlappi và cộng sự (2007) mô hình hóa nhà đầu tư né tránh mơ hồ với nhiều niềm tin tiên nghiệm và thu được danh mục ổn định hơn.  [khớp: 'được']
L294: Avramov (2002) áp dụng phương pháp này vào dự báo lợi suất cổ phiếu và thu được hiệu quả ngoài mẫu tốt hơn việc dùng tiêu chí để chọn một mô hình.  [khớp: 'được']
L294: Timmermann (2006) tổng hợp bằng chứng rằng dự báo kết hợp thường tốt hơn dự báo riêng lẻ, và Rapach và cộng sự (2010) cho thấy kết hợp dự báo bù được phần chất lượng dự báo mất đi do mô hình bất ổn định.  [khớp: 'được' | 'do mô hình']
L294: Cách thứ hai là thu hẹp tập mô hình: tập tin cậy mô hình của Hansen và cộng sự (2011) giữ lại những mô hình chưa thể bị loại là kém hơn ở một mức tin cậy cho trước, nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ.  [khớp: 'bị']
L343: Nguyen và cộng sự (2020) dùng ma trận hiệp phương sai co rút trên 468 tuần giai đoạn 2011--2019 và thu được danh mục có lợi nhuận cao hơn, rủi ro thấp hơn các phương pháp truyền thống.  [khớp: 'được']
L616: Tại đầu mỗi cửa sổ đánh giá, nhà đầu tư chọn trước mô hình *c* có lợi suất tương đương chắc chắn ngoài mẫu cao nhất trong 36 tháng liền trước; mô hình được chọn sau đó tái cân bằng hằng tháng trong suốt cửa sổ.  [khớp: 'được']
L636: Vì cần 104 tuần để ước lượng và 36 tháng kết quả ngoài mẫu để chọn mô hình, mức hối tiếc chỉ tính được từ khoảng năm thứ năm của mẫu.  [khớp: 'được']
L636: Trước khi ước lượng các mô hình danh mục, đề tài báo cáo số giai đoạn căng thẳng rơi vào phần mẫu tính được mức hối tiếc.  [khớp: 'được']
L677: Đề tài coi H~1~ được ủng hộ khi thỏa đồng thời ba điều kiện: <EQ> của <EQ> dương và vượt phân vị 95% của phân phối rỗng; khoảng tin cậy bootstrap khối của <EQ> loại trừ 0; và <EQ> của <EQ> cùng dấu.  [khớp: 'được']
L688: H~2~ được ủng hộ khi hệ số của độ phi thanh khoản dương, hệ số của tương quan đuôi âm và khoảng tin cậy bootstrap khối của cả hai loại trừ 0.  [khớp: 'được']
L714: Tiêu chí đánh giá gồm lợi suất tương đương chắc chắn, mức hối tiếc, độ sụt giảm tối đa (mức giảm lớn nhất từ đỉnh), giá trị thiệt hại kỳ vọng mức 95% (tổn thất trung bình trong 5% số ngày xấu nhất), vòng quay (tỷ lệ danh mục được mua bán lại) và hiệu quả sau chi phí giao dịch.  [khớp: 'được']
L714: H~3~ được ủng hộ khi, ở chế độ căng thẳng, cơ chế giảm thiểu cho lợi suất tương đương chắc chắn sau chi phí cao hơn, mức hối tiếc thấp hơn và độ sụt giảm tối đa không cao hơn so với chọn một mô hình, với khoảng tin cậy bootstrap khối loại trừ 0.  [khớp: 'được']
L738: Nếu dữ liệu bác bỏ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu: khi đó rủi ro lựa chọn mô hình không đổi theo chế độ, hoặc quy tắc 1/N đủ dùng ở Việt Nam.  [khớp: 'được']
L752: Các mô hình ở Bảng 3 ước lượng được bằng phần mềm thống kê thông dụng.  [khớp: 'được']
L918: Mỗi chuyên đề đứng độc lập được và đồng thời làm nền cho một chương của luận án.  [khớp: 'được']
L927: Nếu một bản thảo bị từ chối, thí sinh chuyển bản thảo sang tạp chí khác trong cùng năm.  [khớp: 'bị']
L983: Bảng 6 liệt kê các công trình đã công bố hoặc đã được chấp nhận đăng.  [khớp: 'được']
L1016: 3    Nguyễn Thanh Bình, Nguyễn Văn International Journal of          Đã được chấp Trung\*, Nguyễn Anh Tuấn,     Management and Sustainability     nhận đăng năm "GRI adoption and corporate   (Conscientia Beam);  [khớp: 'được']
L1115: Sự chuẩn bị cho đề tài đến từ các công việc nghiên cứu đã làm.  [khớp: 'bị']
L1115: Bản thảo về tương quan của các chỉ số lồng nhau (bản thảo số 6) chuẩn bị cho kênh tương quan.  [khớp: 'bị']
```

Phân loại 26 khớp:
- Bị động thật (9): "được chọn" L616; "được ủng hộ" L677, L688, L714; "được mua bán lại" L714; "bị loại" L294; "bị từ chối" L927; "được chấp nhận đăng" L983 và L1016 (dòng bảng).
- Dương tính giả, "được" chỉ khả năng hoặc "thu được" (12): L159, L236, L241, L257, L294 (Avramov), L294 (Rapach, "bù được"), L343, L636 ×2, L738, L752, L918.
- Dương tính giả, "bị" trong "chuẩn bị" (2): L1115 ×2.
- "do mô hình" (3): L171 (dòng thật L183) gây đọc sai, đã chuyển sang S5; L186 cùng cấu trúc "chế độ căng thẳng do mô hình ước lượng"; L294 "do mô hình bất ổn định" là quan hệ nguyên nhân, dương tính giả.

### M12 (thừa chữ)

```text
== M12 wordiness: 40 matches in 37 sentences
L159: DeMiguel và cộng sự (2009) so sánh 14 mô hình trên bảy bộ dữ liệu và không tìm thấy mô hình nào vượt quy tắc chia đều vốn cho N tài sản (quy tắc 1/N) một cách nhất quán, xét theo cả tỷ số Sharpe, lợi suất tương đương chắc chắn lẫn vòng quay danh mục.  [khớp: 'sự ' | 'một cách']
L159: Khi không mô hình nào thắng ổn định, việc chọn mô hình trở thành một quyết định mang rủi ro riêng.  [khớp: 'việc ']
L171: Đề cương cũng phân biệt *khủng hoảng*, một sự kiện lịch sử, với *chế độ căng thẳng*, một trạng thái thống kê có biến động cao và lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng.  [khớp: 'sự ']
L186: Dao và cộng sự (2021) cho thấy số ca mắc COVID-19 hằng ngày tác động tiêu cực đến lợi suất cổ phiếu.  [khớp: 'sự ']
L186: Vu và cộng sự (2024) cho thấy các đợt sụt giảm giá cổ phiếu giai đoạn 2007--2022 lan truyền giữa các ngành.  [khớp: 'sự ']
L218: Danielsson và cộng sự, 2016) đo chênh lệch giữa các dự báo rủi ro, chưa đo hậu quả của việc chọn sai mô hình lên trọng số và kết quả danh mục.  [khớp: 'việc ']
L257: Tối ưu hóa trung bình-phương sai dồn trọng số vào những tài sản có sai số ước lượng lớn (Michaud, 1989), và việc thay tham số tổng thể bằng ước lượng mẫu làm hiệu quả ngoài mẫu giảm mạnh (Kan và Zhou, 2007).  [khớp: 'việc ']
L257: Black và Litterman (1992) kết hợp lợi suất cân bằng của mô hình định giá tài sản vốn với quan điểm riêng của nhà đầu tư, và Bessler và cộng sự (2017) thấy cách tiếp cận này vượt cả danh mục trung bình-phương sai lẫn quy tắc 1/N về hiệu quả ngoài mẫu trên dữ liệu đa tài sản toàn cầu.  [khớp: 'sự ']
L257: Garlappi và cộng sự (2007) mô hình hóa nhà đầu tư né tránh mơ hồ với nhiều niềm tin tiên nghiệm và thu được danh mục ổn định hơn.  [khớp: 'sự ']
L257: Dù vậy, DeMiguel và cộng sự (2009) không thấy hướng nào vượt 1/N trên cả bảy bộ dữ liệu, và Pflug và cộng sự (2012) chứng minh quy tắc 1/N xấp xỉ tối ưu theo nghĩa vững chắc khi mức mơ hồ về mô hình đủ cao.  [khớp: 'sự ' | 'sự ']
L275: Kerkhof và cộng sự (2010) tách rủi ro mô hình thành rủi ro ước lượng và rủi ro đặc tả sai, rồi đưa cả hai vào vốn dự phòng.  [khớp: 'sự ']
L275: Boucher và cộng sự (2014) đề xuất hiệu chỉnh độ đo rủi ro theo kết quả kiểm định ngược, còn Danielsson và cộng sự (2016) cho thấy rủi ro mô hình của các mô hình rủi ro thị trường và rủi ro hệ thống tăng theo mức bất định và nhỏ khi thị trường yên ắng.  [khớp: 'sự ' | 'sự ']
L275: Lo và Mueller (2010) cảnh báo việc mô hình hóa tài chính theo chuẩn mực vật lý tạo ra cảm giác chính xác giả tạo, và phân loại các mức bất định.  [khớp: 'việc ']
L275: Các thước đo trong nhóm này gắn với dự báo rủi ro và định giá; chưa thước đo nào đo hậu quả của việc chọn mô hình lên kết quả danh mục.  [khớp: 'việc ']
L294: Hoeting và cộng sự (1999) trình bày phương pháp trung bình hóa mô hình Bayes;  [khớp: 'sự ']
L294: Avramov (2002) áp dụng phương pháp này vào dự báo lợi suất cổ phiếu và thu được hiệu quả ngoài mẫu tốt hơn việc dùng tiêu chí để chọn một mô hình.  [khớp: 'việc ']
L294: Timmermann (2006) tổng hợp bằng chứng rằng dự báo kết hợp thường tốt hơn dự báo riêng lẻ, và Rapach và cộng sự (2010) cho thấy kết hợp dự báo bù được phần chất lượng dự báo mất đi do mô hình bất ổn định.  [khớp: 'sự ']
L294: Cách thứ hai là thu hẹp tập mô hình: tập tin cậy mô hình của Hansen và cộng sự (2011) giữ lại những mô hình chưa thể bị loại là kém hơn ở một mức tin cậy cho trước, nên dữ liệu kém thông tin cho tập lớn và dữ liệu nhiều thông tin cho tập nhỏ.  [khớp: 'sự ']
L294: Các công cụ này có sẵn, song chưa công trình nào dùng chúng để đo tổn thất của việc chọn mô hình theo từng trạng thái thị trường.  [khớp: 'việc ']
L314: Kritzman và cộng sự (2012) dự báo chế độ bằng mô hình Markov, và chiến lược động của họ vượt chiến lược tĩnh khi kiểm định ngược.  [khớp: 'sự ']
L332: Chang và cộng sự (2000) tìm thấy bầy đàn ở Hàn Quốc và Đài Loan nhưng không thấy ở Mỹ và Hồng Kông.  [khớp: 'sự ']
L343: Nguyen và cộng sự (2020) dùng ma trận hiệp phương sai co rút trên 468 tuần giai đoạn 2011--2019 và thu được danh mục có lợi nhuận cao hơn, rủi ro thấp hơn các phương pháp truyền thống.  [khớp: 'sự ']
L343: Goutte và cộng sự (2025) so sánh năm phương pháp ra quyết định đa tiêu chí với bốn cách gán trọng số trên rổ VN100 giai đoạn 01/2015--11/2023.  [khớp: 'sự ']
L387: Bầy đàn ở Việt Nam (Vo và   Bằng chứng bầy đàn trên \(4\) Chưa gắn bầy Phan, 2017)                 HOSE                    đàn với rủi ro của việc chọn mô hình  [khớp: 'việc ']
L394: Bốn khoảng trống có chung một điểm: các công trình đo từng mô hình, từng chế độ hoặc từng hiện tượng riêng lẻ, chưa công trình nào đo rủi ro của việc chọn giữa các mô hình theo chế độ thị trường.  [khớp: 'việc ']
L394: Thí sinh mới đọc tóm tắt và thông tin thư mục của phần lớn các nguồn; việc đọc toàn văn và mở rộng phạm vi tìm kiếm nằm trong kế hoạch năm thứ nhất.  [khớp: 'việc ']
L475: Chang và phân tán chéo của lợi suất                              cộng sự (2000); cao đi cùng rủi ro lựa chọn                             Christie và mô hình cao                                             Huang (1995)  [khớp: 'sự ']
L484: Với H~3~, kết hợp mô hình có thể không vượt việc chọn một mô hình sau chi phí giao dịch và sau hiệu chỉnh thiên lệch chọn lọc (Bailey và López de Prado, 2014).  [khớp: 'việc ']
L563: M~7~   Giảm tỷ trọng rủi ro theo xác suất chế Kritzman và cộng sự (2012) độ căng thẳng  [khớp: 'sự ']
L703: Cơ chế (iii) là quy tắc chuyển chế độ theo Kritzman và cộng sự (2012), với đối chứng là giá trị của chuyển chế độ trong quyết định danh mục theo Tu (2010).  [khớp: 'sự ']
L789: Goutte và cộng sự (2025) so sánh các phương pháp ra quyết định đa tiêu chí trên rổ VN100; đề tài đo mức bất định khi chọn mô hình theo từng chế độ thị trường.  [khớp: 'sự ']
L877: Lý do đầu tiên là sự phù hợp về chuyên môn: theo Thông báo tuyển sinh năm 2026, chương trình Tiến sĩ Kinh tế và Quản lý có tính liên ngành và tập trung vào kinh tế hành vi và quản lý trong lĩnh vực kinh tế, còn đề tài nằm ở giao điểm của tài chính định lượng, quản lý và tài chính hành vi.  [khớp: 'sự ']
L937: Thời gian đào tạo đối với người có bằng đại học là bốn năm.  [khớp: 'đối với']
L1115: Sự chuẩn bị cho đề tài đến từ các công việc nghiên cứu đã làm.  [khớp: 'việc ']
L1115: Bản thảo về mô hình Black-Litterman nghịch đảo kết hợp học máy phân cụm (bản thảo số 1) giúp thí sinh làm quen với việc so sánh nhiều mô hình danh mục trên cùng dữ liệu.  [khớp: 'việc ']
L1115: Luận án chuyển trọng tâm từ đánh giá một mô hình sang câu hỏi chọn giữa nhiều mô hình, và các công việc trên cung cấp phần lớn công cụ cho bước chuyển này.  [khớp: 'việc ']
L1131: Sau khi tốt nghiệp, thí sinh dự kiến làm nghiên cứu và giảng dạy tài chính định lượng tại trường đại học hoặc viện nghiên cứu, hoặc làm việc ở bộ phận quản trị rủi ro và quản lý mô hình của tổ chức tài chính.  [khớp: 'việc ']
```

Phân loại 40 khớp: "sự " trong "cộng sự" 21 (dương tính giả); "việc " trong "công việc"/"làm việc" 3 (dương tính giả: L1115 ×2, L1131); "việc + động từ/danh từ" 12; "sự " khác 2 ("sự kiện" L171, là danh từ, dương tính giả; "sự phù hợp" L877, danh hóa, tùy chọn); "một cách" 1 (L159, tùy chọn); "đối với" 1 (L937, tùy chọn).

### M13 (từ rào yếu)

```text
== M13 weak qualifiers: 3 matches in 3 sentences
L294: Timmermann (2006) tổng hợp bằng chứng rằng dự báo kết hợp thường tốt hơn dự báo riêng lẻ, và Rapach và cộng sự (2010) cho thấy kết hợp dự báo bù được phần chất lượng dự báo mất đi do mô hình bất ổn định.  [khớp: 'thường']
L314: Tu (2010) ước tính nhà đầu tư bỏ qua chuyển chế độ chịu tổn thất lợi suất tương đương chắc chắn thường trên 2% mỗi năm, có thể tới 10%.  [khớp: 'thường']
L314: Về khủng hoảng, Longin và Solnik (2001) bác bỏ phân phối chuẩn đa biến ở đuôi âm của lợi suất, còn Forbes và Rigobon (2002) chỉ ra hệ số tương quan phụ thuộc vào biến động và, sau hiệu chỉnh, gần như không còn dấu hiệu lây nhiễm trong ba cuộc khủng hoảng họ khảo sát.  [khớp: 'gần như']
```

Phân loại: 3 rào trung thực khớp nguồn (L294 "thường", dòng thật L299; L314 "thường", L323; L314 "gần như", L327). Giữ.

### M15 (! và ?)

```text
== M15 ! and ?: 3 matches in 3 sentences
L233: Rủi ro lựa chọn mô hình thay đổi thế nào giữa chế độ bình thường và chế độ căng thẳng?  [khớp: '?']
L236: Sau khi kiểm soát biến động thực hiện, các biến kênh (thanh khoản, tương quan cực trị và, ở mức thăm dò, hành vi bầy đàn) có liên hệ thống kê với rủi ro lựa chọn mô hình không, và chúng giải thích được bao nhiêu phần chênh lệch giữa hai chế độ?  [khớp: '?']
L241: Cơ chế nào giảm được rủi ro lựa chọn mô hình sau chi phí giao dịch?  [khớp: '?']
```

Phân loại: 3 "?" là ba câu hỏi nghiên cứu (L233, L236, L241), không phải câu hỏi tu từ. "!" chỉ có trong tên bài Lo và Mueller (2010) thuộc danh mục tài liệu (xem Part C trên main.tex).

### M16 (từ kêu / mơ hồ)

```text
== M16 pompous/vague: 9 matches in 9 sentences
L186: Vo và Phan (2017) xét tác động của khủng hoảng tài chính toàn cầu lên hành vi nhà đầu tư trên dữ liệu 2005--2015.  [khớp: 'tác động']
L186: Dao và cộng sự (2021) cho thấy số ca mắc COVID-19 hằng ngày tác động tiêu cực đến lợi suất cổ phiếu.  [khớp: 'tác động']
L435: Theo Hình 1, chế độ thị trường tác động lên rủi ro lựa chọn mô hình (giả thuyết H~1~).  [khớp: 'tác động']
L435: Các biến kênh tác động lên chính quan hệ đó, tức giải thích một phần chênh lệch giữa hai chế độ (H~2~ và H~4~).  [khớp: 'tác động']
L435: Cơ chế giảm thiểu tác động lên quan hệ giữa rủi ro lựa chọn mô hình và kết quả danh mục (H~3~).  [khớp: 'tác động']
L577: Tệp đăng ký cố định độ dài các cửa sổ, siêu tham số của bảy mô hình, số chế độ và ngưỡng xác suất lọc, mức ý nghĩa, nhóm kết quả chính, quy tắc hiệu chỉnh so sánh bội và quy tắc gọi một kết quả là không kết luận.  [khớp: 'ý nghĩa']
L625: Để loại tác động cơ học này, phân tích chính chia <EQ> và <EQ> cho sai số chuẩn bootstrap của chênh lệch lợi suất tương đương chắc chắn giữa các mô hình trong cùng cửa sổ.  [khớp: 'tác động']
L625: Thước đo thứ ba là kích thước tập tin cậy mô hình (Hansen và cộng sự, 2011) ở mức ý nghĩa 10% ấn định trước.  [khớp: 'ý nghĩa']
L677: Đề tài lặp lại kiểm định trên tập chỉ gồm các mô hình tĩnh M~1~, M~2~, M~3~, M~4~ và M~6~, để loại tác động của M~5~ và M~7~ vốn chỉ đổi hành vi khi xác suất căng thẳng tăng.  [khớp: 'tác động']
```

Phân loại 9 khớp: 3 hit thật ở L435 (dòng thật L435–439), ngôn ngữ nhân quả, MAJOR (S18/S8). 2 mô tả nguồn (L186 ×2). 2 "mức ý nghĩa" thống kê (L577, L625). 2 "tác động" kỹ thuật do tác giả dùng trong phần phương pháp (L625 "tác động cơ học", L677 "loại tác động của M~5~ và M~7~"), không gây hiểu nhân quả, giữ.

### M17 (động từ hoa mỹ)

```text
== M17 fancy verbs: 1 matches in 1 sentences
L892: Thí sinh muốn rèn các kỹ năng này trong một môi trường có học phần phương pháp, hội thảo định kỳ và cơ chế phản biện nội bộ.  [khớp: 'rèn']
```

Phân loại: 1 hit "rèn" (L892, dòng thật L897). Tùy chọn.

### M18 (câu mở rỗng)

```text
== M18 content-free opener: 0 matches in 0 sentences
```

### M7, M14
Không có grep tiếng Việt. Đọc tay, kết quả ở §1: M7 = 0 bộ ba không hợp lý, M14 = 0. Grep nguyên mẫu M14 trên `main.tex` = 0 dòng.

### Part C nguyên mẫu của skill (`gate_mechanical.md`), chạy trên `scratchpad/paper/main.tex` (toàn file)

```text
### Part C nguyên mẫu của skill, chạy trên main.tex
== M1a '---' (main.tex, toàn file): 0 dòng
== M1b (main.tex, toàn file): 0 dòng
== M11 (main.tex, toàn file): 0 dòng
== M2 (main.tex, toàn file): 1 dòng
54: not o
== M3/M4/M8/M9 (main.tex, toàn file): 0 dòng
== M6 (main.tex, toàn file): 0 dòng
== M5/M16 (main.tex, toàn file): 3 dòng
1442:impact
1450:impact
1532:Robust
== M10 (main.tex, toàn file): 0 dòng
== M17 (main.tex, toàn file): 0 dòng
== M18 (main.tex, toàn file): 0 dòng
== M12 (main.tex, toàn file): 0 dòng
== M13 (main.tex, toàn file): 0 dòng
== M14 (main.tex, toàn file): 0 dòng
== M15 (main.tex, toàn file): 1 dòng
1537:hazardous to your wealth!'', \emph{Journal of Investment Management},
== PartB (main.tex, toàn file): 0 dòng
== M1 ' -- ' (main.tex)
106:\textbf{HÀ NỘI -- 2026}
== Dòng đầy đủ của các hit main.tex (M2 L54; M5/M16 L1442, L1450, L1532; M15 L1537):
54:% Scale images if necessary, so that they will not overflow the page
1441:
1442:Cont, R. (2006), ``Model uncertainty and its impact on the pricing of
1449:
1450:Dao, V. H., Nguyen, T. M. H., Vu, T. D. (2021), ``The impact of COVID-19
1531:
1532:Ledoit, O., Wolf, M. (2008), ``Robust performance hypothesis testing
1536:Lo, A. W., Mueller, M. T. (2010), ``Warning: Physics envy may be
1537:hazardous to your wealth!'', \emph{Journal of Investment Management},
```

Phân loại: `---` = 0 và `—/–` = 0. Có 1 dòng `' -- '` là bìa L106 "HÀ NỘI -- 2026" (đã ghi). Hit M2 "not o" ở L54 là chú thích LaTeX của pandoc, dương tính giả. Hit M5/M16 ("impact" ×2, "Robust") nằm trong tên bài thuộc danh mục tài liệu, dương tính giả. Hit M15 `!` là tên bài Lo và Mueller (2010).
