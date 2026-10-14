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
| M11 bị động | `\bđược\b\|\bbị\b\|\bbởi\b\|do mô hình` | 26 (25 câu) | L681 "Đề tài coi H~1~ được ủng hộ khi…"; L305 "chưa thể bị loại"; L183 "lợi suất thị trường thấp do mô hình chuyển chế độ ước lượng" | Phần lớn "được" là nghĩa khả năng ("ước lượng được", "tính được"), không phải bị động. Bị động thật ≈10 ("được ủng hộ" ×3, "được chọn", "được mua bán lại", "bị loại", "bị từ chối", "được chấp nhận đăng"): **xung đột với nguyên tắc tác giả — không khuyến nghị áp dụng** quy tắc zero-passive. Riêng L183 "do mô hình…" gây đọc sai → chuyển sang S5 (MAJOR) |
| M12 thừa chữ | `nhằm mục đích`, `để có thể`, `một cách`, `trong việc`, `về mặt`, `đối với`, `việc `, `sự `, `tiến hành` | 40 (37 câu) | L166–167 "vượt quy tắc chia đều vốn… một cách nhất quán"; L159 "việc chọn mô hình trở thành…" | ~28 là "cộng sự" (dương tính giả); ~11 là "việc + động từ" tự nhiên trong tiếng Việt; 1 hit tùy chọn ("một cách nhất quán" → "nhất quán"). Không có lỗi đáng sửa bắt buộc |
| M13 từ rào yếu | `rất`, `khá`, `hơi`, `tương đối`, `chắc chắn` (trừ "tương đương chắc chắn"), `gần như`, `(?<!bình )thường` | 3 | L299 "dự báo kết hợp thường tốt hơn"; L323 "thường trên 2% mỗi năm"; L327 "gần như không còn dấu hiệu lây nhiễm" | Cả 3 là rào trung thực, khớp phát hiện của nguồn → giữ. **xung đột với nguyên tắc tác giả — không khuyến nghị áp dụng** việc xoá |
| M14 trạng từ tự chế / số thứ tự giả | Không có tương đương tiếng Việt cho `firstly/-wise`; kiểm "thứ nhất/thứ hai" | 0 | — | Không áp dụng (cách đếm "Lý do đầu tiên/thứ hai" là chuẩn tiếng Việt) |
| M15 `!` và câu hỏi tu từ | `[!?]`; grep `!` trên main.tex | 3 `?` trong thân; 1 `!` trong tên bài trích dẫn (Lo và Mueller 2010) | L233–242 ba câu hỏi nghiên cứu | Câu hỏi nghiên cứu, không phải tu từ; `!` nằm trong tên bài gốc → hợp lệ |
| M16 từ kêu/mơ hồ | `nhân tố`, `yếu tố`, `hiện nay`, `hiện tại`, `sở hữu`, `có ý nghĩa`, `tác động` | 9 | L435–439 "chế độ thị trường tác động lên rủi ro lựa chọn mô hình… Các biến kênh tác động lên chính quan hệ đó… Cơ chế giảm thiểu tác động lên quan hệ…" | 3 hit ở L435–439 là lỗi thật: ngôn ngữ nhân quả mâu thuẫn L698–699 → MAJOR (S18/S8). Các hit còn lại là mô tả nguồn hoặc "mức ý nghĩa" thống kê |
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
| 9 | **Evidence rule**: dán grep + findings làm hồ sơ; không báo clean khi chỉ đọc nhẩm | Đã làm | Số đếm grep ở mục 1 (ví dụ M11 = 26 khớp/25 câu; M2 = 15 câu); script ở `scratchpad/g2rt/` |
| 10 | **How to run**: reviewer tách biệt, chỉ nhận văn bản + checklist + controlling idea, không xem tự đánh giá của tác giả | Đã làm | Subagent riêng; controlling idea = tên đề tài + 3 câu hỏi (ghi ở đầu báo cáo); không mở `scratchpad/paper/reviews/` và `reports/` |
| 11 | Tác giả sửa mọi phát hiện, vòng lặp lặp lại đến khi reviewer trả clean | CHƯA LÀM | Ngoài phạm vi: nhiệm vụ cấm sửa file đề cương; cần vòng sau |

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
