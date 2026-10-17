# Vòng đóng cổng 1, agent A: văn phong, đọc sửa, tách đoạn và mạch lập luận sau khi cắt (v14)

Tệp rà: `scratchpad/r14/v14-text.txt` (346 mục [idx]). Bản đối chiếu: `outputs/round-13/de-cuong-v13-round-13.docx` (đã giải nén `word/document.xml` vào `scratchpad/r14/v13x/`, chuyển thành `scratchpad/r14/v13-text.txt` để tìm chuỗi). Không sửa tệp đề cương. Không gửi câu chữ đề cương ra mạng.

## 1. Bằng chứng tuân thủ

Các skill được gọi tuần tự qua công cụ Skill, đúng thứ tự giao.

| # | Skill | Tệp tham chiếu đã đọc | Việc đã làm |
|---|---|---|---|
| 1 | vina-me | SKILL.md (kèm ghi chú miễn trừ APA 7); references/dau-hieu.md, cau-va-doan.md, loi-thuong-gap.md, lien-ket.md, tu-ngu.md | Trích phần văn xuôi từ [66] đến trước [261], bỏ bảng (`scratchpad/r14/prose-A2.txt`, mỗi đoạn cách một dòng trống). Chạy `node .claude/skills/vina-me/scripts/soat.mjs` → 132 đoạn, 300 câu, 36,1 chữ/câu, 2,3 câu/đoạn; cảnh báo: "đồng thời" (2), "không chỉ"; 18 gạch vừa và 29 "&" (miễn trừ APA 7: khoảng số, tên ghép, trích dẫn trong ngoặc); "CHIẾU" (nằm trong nhãn [CẦN ĐỐI CHIẾU], không đụng); một dấu "=" (trong ký hiệu 1[t = k], không đụng); "3 đoạn liền mở bằng câu hỏi" (là ba nhãn "Câu hỏi 1/2/3" [78]–[80], không phải câu hỏi tu từ, giữ). Đọc hai lượt (người mới; bắt văn máy) theo dau-hieu.md, loi-thuong-gap.md, lien-ket.md. |
| 2 | vietnamese-human-writing | references/master-writing-rules.md (toàn bộ, R01–R53, mục I–XII) | Áp 7 vòng rà cho văn khoa học (R46): vòng 1 dữ kiện và logic (đối chiếu v13), vòng 2 ngôn ngữ, vòng 3 cấu trúc, vòng 4 nhịp câu (dùng số đo của soat.mjs; không tự đo thêm chỉ số vì cấm chạy script khác), vòng 5 từ vựng/thuật ngữ (R20, R38), vòng 6 hình thức, vòng 7 đọc toàn văn. Đếm số chữ mỗi đoạn bằng lệnh đếm từ của shell để tìm đoạn trên 130 chữ: [68] 165, [82] 156, [95] 167, [97] 133, [98] 169, [107] 173, [116] 149, [120] 160, [170] 163, [172] 152, [175] 148, [181] 158, [185] 144, [240] 131, [255] 166. |
| 3 | sciwrite | SKILL.md (5 lượt soát) | Soát lượt 4 (thuật ngữ nhất quán, viết tắt ở lần đầu) và lượt 5 (số liệu, trích dẫn). Kiểm số: 193 tháng (6/2009–6/2025), 18 tháng chuyển tiếp, 20 cửa sổ (Q3/2020–Q2/2025), 8 cửa sổ (Q1/2027–Q4/2028), ba bản thảo "Có" ở Bảng 7 (số 1, 5, 7): đều khớp. Đối chiếu từng trích dẫn trong thân bài với danh mục tài liệu: không thấy tài liệu thiếu hay thừa (Arnold và cộng sự, 1999 là trích gián tiếp). |
| 4 | scientific-writing | SKILL.md | Không chạy các script của skill (bị cấm). Áp phần "Scientific fidelity" và đối chiếu tham chiếu chéo: mục 4.1, 4.3.2, 4.3.7, 4.3.8, 4.3.10; Bảng 1–7; Hình 1–3; phương trình (1)–(7): tất cả đều trỏ tới nội dung còn tồn tại. Phát hiện chỗ cắt làm mất định nghĩa (A-01), mất biện pháp xử lý (A-02), tạo mâu thuẫn (A-03). |
| 5 | econ-write | SKILL.md | Soát 4.1 ([68]–[91]): câu hỏi nghiên cứu, mục tiêu, đóng góp. Câu hỏi và kiểm định trọng tâm (H3) đã nêu rõ; phần đóng góp nói được "so với ai, thêm gì". Ghi nhận các điểm thuật ngữ (A-08, A-09) và khoảng trống K1 chưa nói rõ "thiếu gì" ([76], A-37). |
| 6 | review-methodology | SKILL.md (5 chiều) | Rà việc cắt có làm hở thiết kế: H1–H4, DiD, suy luận, nhóm đối chứng, phương án dự phòng. Kết quả: không mất giả thuyết, phương trình, kiểm định hay phương án dự phòng; nhưng danh mục đăng ký trước bị rút mất "quy tắc chọn cửa sổ trước theo điểm gãy" (A-04), đoạn H1 mất ước lượng bổ sung không có hiệu ứng cố định (A-02), định nghĩa biến kết quả chính lệch biên giữa các đoạn (A-05). |
| 7 | academic-paper-reviewer | SKILL.md | Chế độ re-review/methodology-focus yêu cầu đội agent và contract kiểm bằng script (`scripts/check_phase_conformance.py`, `check_panel_synthesis.py`, `check_acronyms.py`); trong lượt này không có công cụ tạo agent con và bị cấm chạy script ngoài soat.mjs, nên không chạy được: "không có Agent tool; script bị cấm theo giao việc". Đã áp checklist trong một ngữ cảnh. Phản biện mạnh nhất (vai Devil's Advocate): H3 là một sự kiện duy nhất, mọi suy luận dựa trên một chuỗi d_t theo tháng; việc cắt không làm yếu thêm luận điểm này, vì đề cương vẫn giữ bootstrap tự hồi quy, kiểm tra kích thước bằng mô phỏng, hiệu ứng nhỏ nhất phát hiện được và cách gọi "chưa đủ cơ sở kết luận". Không có vấn đề CRITICAL mới. |
| 8 | mhe-identification | SKILL.md (Critic mode) | Câu hỏi viết lại theo kết quả tiềm năng: thay đổi log Amihud của mã HNX khi chuyển sang HOSE so với khi không chuyển. Nguồn biến thiên: một ngày chuyển sàn chung, do quy định (không do doanh nghiệp chọn). Thiết kế 2×2 một ngày, nên TWFE hợp lệ; suy luận theo chuỗi thời gian (không phân cụm theo cổ phiếu) là đúng với cấu trúc cú sốc chung. Ghép theo độ phi thanh khoản trước sự kiện đã được nhận diện là rủi ro hồi quy về trung bình (Daw & Hatfield, 2018). Kết luận: thiết kế đo được tác động gộp của sàn; việc cắt không làm mất điều kiện nhận dạng nào. |
| 9 | aer-identification | SKILL.md | Đối chiếu Identification Gate: DiD một ngày (không so le), có phương án Callaway–Sant’Anna khi so le; kiểm định đồng thời các hệ số trước sự kiện; Rambachan–Roth; suy luận bootstrap tự hồi quy. Không có red flag nào trong danh sách của skill. |
| 10 | liquidity-measures | SKILL.md | Đối chiếu bảy bẫy ở mục 4: ngày chạm biên độ và ngày liền sau ([119]–[120], cùng một ngưỡng chung), biên độ khác nhau giữa sàn ([116]), bước giá ([117]–[118]), giao dịch thỏa thuận (chỉ khớp lệnh, [120]), thang tiền tệ (điều chỉnh theo tổng vốn hóa, [131]), sống sót (bảng cân bằng, [189]). Phát hiện ranh giới ngưỡng không nhất quán (A-05). Không thấy quy tắc xử lý ước lượng Corwin–Schultz âm và mẫu số của vòng quay, nhưng v13 cũng không có nên không xếp vào lỗi do cắt (không đề xuất mở rộng). |
| 11 | statistical-power | SKILL.md | Tính tay, không chạy script. Với φ = 0: (z(1−0,05/3) + z(0,80))·√(1/24 + 1/193) = (2,128 + 0,842)·0,2164 ≈ 0,643σ → 0,64σ, khớp. Với AR(1), phương sai trung bình mẫu n kỳ = σ²/n·[1 + 2Σ(1−k/n)φ^k]: φ = 0,6 cho 2,970·√(0,1537 + 0,0205) ≈ 1,240σ → 1,24σ, khớp; φ = 0,8 cho 2,970·√(0,3059 + 0,0456) ≈ 1,761σ → 1,76σ, khớp. Cửa sổ trước 24 tháng: hệ số tăng 1,33 (φ = 0), 1,33 (φ = 0,6), 1,32 (φ = 0,8) → "khoảng 1,3 lần", khớp. Ví dụ σ = 0,2, φ = 0,6: 1,24·0,2 = 0,248 ≈ 0,25; e^(−0,248) ≈ 0,780 → giảm khoảng 22%, khớp. Không có lỗi số. |
| 12 | review-pap | SKILL.md | Quy trình gốc cần 6 agent song song và lưu báo cáo vào `reviews/`; không chạy được: "không có Agent tool trong lượt này", và giao việc chỉ cho phép ghi một báo cáo. Đã áp checklist của 6 agent trong một ngữ cảnh lên các đoạn đăng ký trước [86], [142]–[143], [166], [192], Bảng 5. Kết quả: biến kết quả chính, họ kiểm định Holm, phân tích phụ, quy tắc lệch kế hoạch, xử lý rời mẫu đều còn; thiếu quy tắc chọn cửa sổ trước theo điểm gãy (v13 có, v14 bỏ) → A-04. |
| 13 | peer-review | SKILL.md | Văn bản của chính thí sinh, được giao rà nội bộ, xử lý cục bộ. Không chạy script intake/lint (bị cấm). Áp bước 4 (ánh xạ khẳng định với bằng chứng) và bước 5 (phương pháp, thống kê) trong một ngữ cảnh; không thêm phát hiện ngoài các mục đã ghi. |
| 14 | paper-writing-skill | SKILL.md; author_profile/editorial_principles.md và compression_patterns.md (đọc đề mục, áp nguyên tắc 4, 12, 14 và 7 phép nén) | Chỉ áp phần nguyên tắc biên tập và nén. Không đề xuất nén thêm. Ghi các chỗ lặp còn sót ở mục 4 (để thí sinh tự quyết, không bắt buộc sửa). Nguyên tắc 14 (khẳng định kỹ thuật nhắc lại phải mang theo trích dẫn) → A-17 (Holm). |

## 2. Tóm tắt

| Mức | Số lượng |
|---|---|
| CRITICAL | 0 |
| MAJOR | 5 |
| MINOR | 38 (trong đó 10 là tách đoạn) |

Kết luận ngắn: việc cắt 20% không làm mất giả thuyết, phương trình, kiểm định hay phương án dự phòng, và không tạo tham chiếu chéo tới nội dung đã xóa. Có năm chỗ hở cần vá trước khi đóng cổng: mất định nghĩa câu hỏi số 2 và số 4 của bài toán, câu lập luận về nhận dạng β của H1 bị cắt mất vế xử lý, một mâu thuẫn mới về giai đoạn chuyển tiếp, danh mục đăng ký trước thiếu quy tắc chọn cửa sổ trước, và ranh giới ngưỡng lợi suất ghi hai kiểu.

## 3. Danh sách phát hiện

Quy ước: chuỗi gốc chép nguyên văn từ v14-text.txt, không chứa ký tự "_", xuất hiện đúng một lần trong đoạn (đã kiểm bằng grep). Với bảng, chuỗi gốc xuất hiện đúng một lần trong cả tệp.

### MAJOR

**A-01. MAJOR. idx [213].** Lý do (scientific-writing, vina-me tu-ngu.md): bản cắt bỏ phần giải thích câu hỏi số 2 và số 4 của bài toán số 19. Câu hỏi số 1 và số 3 có được mô tả ở [68], nhưng số 2 và số 4 thì không có ở đâu trong v14, nên người đọc không biết phần nào nằm ngoài phạm vi. v13 có: "câu hỏi số 2 và số 4 về công nghệ tài chính và dịch vụ tài chính thế hệ mới nằm ngoài phạm vi".
- CHUỖI GỐC: `câu hỏi số 2 và số 4 nằm ngoài phạm vi`
- CHUỖI THAY THẾ: `câu hỏi số 2 và số 4 (về công nghệ tài chính và dịch vụ tài chính thế hệ mới) nằm ngoài phạm vi`

**A-02. MAJOR. idx [182].** Lý do (review-methodology, scientific-writing): quan hệ nhân quả trong câu bị đặt sai. β được xác định từ biến thiên trong từng quốc gia là do mô hình có hiệu ứng cố định theo trung tâm γ_i. Việc SMD thay đổi chậm chỉ làm biến thiên đó nhỏ đi. Bản cắt còn bỏ vế xử lý mà v13 có ("đề tài báo cáo thêm ước lượng không có hiệu ứng cố định theo trung tâm"), nên câu nêu lo ngại mà không có cách xử lý. Đây là khôi phục, không phải mở rộng thiết kế.
- CHUỖI GỐC: `Vì SMD thay đổi chậm, β chủ yếu được xác định từ biến thiên theo thời gian trong từng quốc gia.`
- CHUỖI THAY THẾ: `Vì mô hình có hiệu ứng cố định theo trung tâm, β được xác định từ biến thiên theo thời gian trong từng quốc gia, và biến thiên này nhỏ vì SMD thay đổi chậm; đề tài báo cáo thêm ước lượng không có hiệu ứng cố định theo trung tâm.`

**A-03. MAJOR (mâu thuẫn nội bộ phát sinh khi cắt). idx [125].** Lý do (vietnamese-human-writing vòng 1, scientific-writing): v14 viết giai đoạn chuyển tiếp "chỉ dùng trong phiên bản nghiên cứu sự kiện", nhưng [135] lại báo cáo chênh lệch Chỉ số chất lượng thị trường vốn trong giai đoạn chuyển tiếp ở dạng mô tả. v13 viết "được báo cáo riêng", không mâu thuẫn.
- CHUỖI GỐC: `chỉ dùng trong phiên bản nghiên cứu sự kiện`
- CHUỖI THAY THẾ: `được báo cáo riêng (phiên bản nghiên cứu sự kiện và phần mô tả), không dùng trong các kiểm định chính`

**A-04. MAJOR. idx [143].** Lý do (review-pap, review-methodology): [164] chọn cửa sổ trước của ước lượng chính theo điểm gãy cấu trúc cuối cùng. Đây là lựa chọn có thể làm đổi kết quả, và v13 có ghi nó trong danh mục đăng ký trước ("quy tắc chọn cửa sổ trước theo điểm gãy"). v14 bỏ mục này nên danh mục không còn "cố định trước mọi lựa chọn có thể ảnh hưởng tới kết quả" như câu mở đoạn cam kết.
- CHUỖI GỐC: `ngưỡng lợi suất khi tính Amihud;`
- CHUỖI THAY THẾ: `ngưỡng lợi suất khi tính Amihud; quy tắc chọn cửa sổ trước theo điểm gãy cấu trúc;`

**A-05. MAJOR. idx [120] và [163].** Lý do (liquidity-measures, sciwrite lượt 4): biến kết quả chính của H3 được định nghĩa hai kiểu. Bảng 2 và [172] viết "không liền sau ngày có lợi suất tuyệt đối từ ngưỡng chung trở lên" (lớn hơn hoặc bằng), còn [120] và [163] viết "không liền sau một ngày vượt ngưỡng này" (lớn hơn). Một ngày có lợi suất tuyệt đối đúng bằng ngưỡng sẽ bị xử lý khác nhau. Định nghĩa này đi vào tệp đăng ký nên cần một cách viết.
- [120] CHUỖI GỐC: `không liền sau một ngày vượt ngưỡng này`
- [120] CHUỖI THAY THẾ: `không liền sau một ngày có lợi suất tuyệt đối từ ngưỡng này trở lên`
- [163] CHUỖI GỐC: `không liền sau một ngày vượt ngưỡng này`
- [163] CHUỖI THAY THẾ: `không liền sau một ngày có lợi suất tuyệt đối từ ngưỡng này trở lên`

### MINOR

**A-06. MINOR. idx [69].** Lý do (vina-me tu-ngu.md "Chữ viết tắt", sciwrite acronym): GFCI xuất hiện trong thân bài lần đầu ở đây mà chưa có tên đầy đủ (chỉ có trong danh mục chữ viết tắt).
- CHUỖI GỐC: `đo bằng điểm GFCI`
- CHUỖI THAY THẾ: `đo bằng điểm Chỉ số Trung tâm Tài chính Toàn cầu (GFCI)`

**A-07. MINOR. idx [68] và [70].** Lý do (vina-me tu-ngu.md): HNX và HOSE dùng ở [68] trước khi được giải nghĩa ở [70]. Chuyển tên đầy đủ lên lần dùng đầu.
- [68] CHUỖI GỐC: `khi cổ phiếu niêm yết chuyển từ HNX sang HOSE.`
- [68] CHUỖI THAY THẾ: `khi cổ phiếu niêm yết chuyển từ Sở Giao dịch Chứng khoán Hà Nội (HNX) sang Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh (HOSE).`
- [70] CHUỖI GỐC: `từ Sở Giao dịch Chứng khoán Hà Nội (HNX) sang Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh (HOSE)`
- [70] CHUỖI THAY THẾ: `từ HNX sang HOSE`

**A-08. MINOR. idx [68].** Lý do (sciwrite lượt 4, R20): cùng một thứ gọi hai kiểu. [68] viết "câu hỏi thứ nhất/thứ ba", từ [78] trở đi đều viết "câu hỏi số 1/số 3" của bài toán.
- CHUỖI GỐC: `(câu hỏi thứ nhất của bài toán)`
- CHUỖI THAY THẾ: `(câu hỏi số 1 của bài toán)`
- CHUỖI GỐC: `(câu hỏi thứ ba)`
- CHUỖI THAY THẾ: `(câu hỏi số 3)`

**A-09. MINOR. idx [77].** Lý do (econ-write, sciwrite): "câu hỏi chính của bài toán" là khái niệm chưa định nghĩa. Ba câu hỏi gắn với câu hỏi số 1 và số 3 (ghi trong ngoặc ở [78]–[80]).
- CHUỖI GỐC: `mỗi câu gắn với câu hỏi chính của bài toán số 19:`
- CHUỖI THAY THẾ: `mỗi câu gắn với câu hỏi tương ứng của bài toán số 19 (ghi trong ngoặc):`

**A-10. MINOR. idx [75].** Lý do (vina-me cau-va-doan.md, phụ ngữ đứng xa từ nó bổ nghĩa): trích dẫn chen vào giữa làm "trong cùng một ngày" bị tách khỏi "đổi sàn".
- CHUỖI GỐC: `Đợt hợp nhất ở Việt Nam đổi sàn của toàn bộ cổ phiếu niêm yết tại HNX, gồm 299 mã tính đến phiên 30/9/2026 (Tuổi Trẻ Online, 2026), trong cùng một ngày.`
- CHUỖI THAY THẾ: `Đợt hợp nhất ở Việt Nam đổi sàn của toàn bộ cổ phiếu niêm yết tại HNX, gồm 299 mã tính đến phiên 30/9/2026, trong cùng một ngày (Tuổi Trẻ Online, 2026).`

**A-11. MINOR. idx [73].** Lý do (vina-me cau-va-doan.md, câu nhiều tầng): ba mệnh đề độc lập nối bằng dấu phẩy; dùng chấm phẩy ngăn vế lớn.
- CHUỖI GỐC: `chỉ áp dụng cho cổ phiếu niêm yết, báo chí cho biết`
- CHUỖI THAY THẾ: `chỉ áp dụng cho cổ phiếu niêm yết; báo chí cho biết`

**A-12. MINOR. idx [82].** Lý do (sciwrite lượt 4; scientific-writing, định nghĩa trước khi dùng): "mức thay đổi của tác động" khác tên với Bảng 4 ("Khác biệt của tác động theo mức chịu cú sốc"); "mức chịu cú sốc" được dùng lần đầu ở đây mà chưa trỏ tới chỗ định nghĩa.
- CHUỖI GỐC: `kể cả mức thay đổi của tác động theo mức chịu cú sốc biên độ, bước giá, chỉ số và theo trụ sở doanh nghiệp`
- CHUỖI THAY THẾ: `kể cả khác biệt của tác động theo mức chịu cú sốc biên độ, bước giá, chỉ số (mục 4.3.7) và theo trụ sở doanh nghiệp`

**A-13. MINOR (tách đoạn). idx [82]** (156 chữ, hai ý: bốn mục tiêu cụ thể; vai trò của bốn giả thuyết). Lý do: vina-me cau-va-doan.md "Tách đoạn".
- TÁCH TRƯỚC: `Trong bốn giả thuyết ở mục 4.3.2`

**A-14. MINOR. idx [84].** Lý do (scientific-writing, định nghĩa trước khi dùng): "Hai chỉ số" xuất hiện trước khi Chỉ số khả năng đầu tư được giới thiệu ([89], mục 4.3.6).
- CHUỖI GỐC: `Hai chỉ số và tệp đăng ký trước`
- CHUỖI THAY THẾ: `Hai chỉ số (chất lượng thị trường vốn và khả năng đầu tư) cùng tệp đăng ký trước`

**A-15. MINOR (tách đoạn). idx [95]** (167 chữ, ba chiều thước đo). Lý do: vina-me cau-va-doan.md.
- TÁCH TRƯỚC: `Hiệu quả thông tin được đo bằng`

**A-16. MINOR. idx [95].** Lý do (sciwrite lượt 4, R20): cùng chỉ báo, ở mục khác gọi là "tỷ lệ ngày (có) lợi suất bằng 0".
- CHUỖI GỐC: `tần suất ngày có lợi suất bằng 0`
- CHUỖI THAY THẾ: `tỷ lệ ngày có lợi suất bằng 0`

**A-17. MINOR. idx [95].** Lý do (vina-me tu-ngu.md, chọn từ hợp giọng trang trọng): "nối" là khẩu ngữ.
- CHUỖI GỐC: `Lang và cộng sự (2012) nối minh bạch với thanh khoản`
- CHUỖI THAY THẾ: `Lang và cộng sự (2012) liên hệ minh bạch với thanh khoản`

**A-18. MINOR (tách đoạn). idx [98]** (169 chữ: vấn đề và cách khắc phục; giới hạn và cách đề tài dùng). Lý do: vina-me cau-va-doan.md.
- TÁCH TRƯỚC: `Dù vậy, không mô hình nào`

**A-19. MINOR (tách đoạn). idx [107]** (173 chữ: ba khối lý thuyết; chuỗi nối và giới hạn). Lý do: vina-me cau-va-doan.md. Có thể giữ nguyên nếu muốn đoạn này đứng liền.
- TÁCH TRƯỚC: `Ba khối nối thành một chuỗi`

**A-20. MINOR. idx [114] (Bảng 2, dòng H4).** Lý do (sciwrite acronym, scientific-writing): "rổ H" dùng trong thân bài trước định nghĩa ở [146]; bảng cần tự đọc được.
- CHUỖI GỐC: `giữa rổ H và rổ cổ phiếu chuyển sàn thu hẹp`
- CHUỖI THAY THẾ: `giữa rổ H (rổ cổ phiếu HOSE đối sánh, mục 4.3.6) và rổ cổ phiếu chuyển sàn thu hẹp`

**A-21. MINOR. idx [114] (Bảng 2, dòng H2).** Lý do (sciwrite lượt 4): [130] định nghĩa chỉ báo là "số ngày trễ hạn công bố báo cáo tài chính quý"; Bảng 2 gọi "độ trễ công bố", dễ lẫn với "độ trễ giá" ngay trước nó.
- CHUỖI GỐC: `độ trễ giá, độ trễ công bố`
- CHUỖI THAY THẾ: `độ trễ giá, số ngày trễ hạn công bố`

**A-22. MINOR. idx [115].** Lý do (paper-writing-skill nguyên tắc 14, sciwrite lượt 5): thủ tục Holm được nhắc lần đầu ở ghi chú Bảng 2 mà chưa có trích dẫn (trích dẫn chỉ có ở [200]).
- CHUỖI GỐC: `hiệu chỉnh Holm ở mức 5%`
- CHUỖI THAY THẾ: `hiệu chỉnh Holm (1979) ở mức 5%`

**A-23. MINOR. idx [119].** Lý do (vina-me loi-thuong-gap.md, câu hai cách hiểu): sau khi chuyển sàn, lợi suất không thể nằm trong khoảng 7% đến 10%; ý muốn nói là những ngày lẽ ra có lợi suất như vậy.
- CHUỖI GỐC: `mọi ngày có lợi suất tuyệt đối khoảng 7% đến 10%`
- CHUỖI THAY THẾ: `mọi ngày lẽ ra có lợi suất tuyệt đối khoảng 7% đến 10%`

**A-24. MINOR. idx [120].** Lý do (vina-me cau-va-doan.md "Lời giải nghĩa chêm"): lời chêm giữa hai dấu phẩy đứng cạnh một chuỗi dấu phẩy khác làm câu khó tách; dùng ngoặc đơn.
- CHUỖI GỐC: `và vòng quay, thước đo không dùng lợi suất, là thước đo đối chiếu`
- CHUỖI THAY THẾ: `và vòng quay (thước đo không dùng lợi suất) là thước đo đối chiếu`

**A-25. MINOR (tách đoạn). idx [120]** (160 chữ: cách tính Amihud trên ngày hợp lệ; các tham số ghi vào tệp đăng ký và thước đo đối chiếu). Lý do: vina-me cau-va-doan.md.
- TÁCH TRƯỚC: `Giá trị ngưỡng và số ngày hợp lệ tối thiểu`

**A-26. MINOR. idx [123].** Lý do (scientific-writing, tham chiếu chéo mất khi cắt; vina-me "nói đúng mức chắc chắn"): v14 đọc như việc số hóa đã làm hoặc chắc chắn làm được, trong khi [203] có phương án dự phòng khi không được phép. v13 có câu trỏ tới phương án dự phòng thứ nhất.
- CHUỖI GỐC: `được thí sinh số hóa từ báo cáo từng kỳ sau khi xin phép Long Finance`
- CHUỖI THAY THẾ: `được thí sinh số hóa từ báo cáo từng kỳ nếu Long Finance cho phép (nếu không, xem phương án dự phòng ở mục 4.3.10)`

**A-27. MINOR. idx [154].** Lý do (vina-me loi-thuong-gap.md, nghĩa mơ hồ do nén): "thông tin lỗi thời" không rõ là thông tin gì. v13 nói rõ: thông tin tại ngày tham chiếu có thể lỗi thời ở các cửa sổ xa.
- CHUỖI GỐC: `thiên lệch do thông tin lỗi thời hay hồi quy về trung bình tác động lên cả hai`
- CHUỖI THAY THẾ: `thiên lệch do thông tin tại ngày tham chiếu lỗi thời ở các cửa sổ xa hay do hồi quy về trung bình tác động lên cả hai rổ`

**A-28. MINOR. idx [164].** Lý do (scientific-writing, định nghĩa trước khi dùng): "chuỗi chênh lệch theo tháng" dùng ở đây, định nghĩa (d_t) ở [166].
- CHUỖI GỐC: `của chuỗi chênh lệch theo tháng (Bai & Perron, 1998)`
- CHUỖI THAY THẾ: `của chuỗi chênh lệch theo tháng định nghĩa ở đoạn sau (Bai & Perron, 1998)`

**A-29. MINOR. idx [167].** Lý do (sciwrite lượt 4): ý là các ngày sự kiện giả định (placebo); "ngày giả định" đứng một mình chưa rõ nghĩa.
- CHUỖI GỐC: `Suy luận trên các ngày giả định`
- CHUỖI THAY THẾ: `Suy luận trên các ngày sự kiện giả định`

**A-30. MINOR (tách đoạn). idx [167].** Lý do (vina-me lien-ket.md, đổi đề tài thì xuống dòng): câu cuối chuyển từ suy luận cho δ sang phiên bản nghiên cứu sự kiện và dẫn tới phương trình (6).
- TÁCH TRƯỚC: `Phiên bản nghiên cứu sự kiện kiểm tra`

**A-31. MINOR. idx [170].** Lý do (vietnamese-human-writing vòng 1, nhất quán): [170] nói việc chuyển sàn đổi "ba quy tắc", còn [189] liệt kê bốn thay đổi (biên độ, bước giá, hệ thống giao dịch, tư cách thành phần chỉ số).
- CHUỖI GỐC: `Việc chuyển sàn đổi ba quy tắc cùng lúc, và mỗi quy tắc tác động mạnh yếu khác nhau tùy cổ phiếu:`
- CHUỖI THAY THẾ: `Việc chuyển sàn đổi nhiều quy tắc cùng lúc, trong đó ba quy tắc tác động mạnh yếu khác nhau tùy cổ phiếu:`

**A-32. MINOR (tách đoạn). idx [170]** (163 chữ: ba kênh; cách đo ba mức chịu cú sốc). Lý do: vina-me cau-va-doan.md.
- TÁCH TRƯỚC: `Ba mức chịu cú sốc tương ứng`

**A-33. MINOR. idx [172].** Lý do (vina-me cau-va-doan.md, chủ ngữ mờ): chủ ngữ của "được ước lượng" thành "mức chịu cú sốc biên độ", trong khi thứ được ước lượng trên mã HOSE đối chứng là hiệu ứng theo tháng riêng. "Chỉ đại diện" là cách nói tắt của thước đo gần đúng.
- CHUỖI GỐC: `và được ước lượng trên mã HOSE đối chứng; thước đo này chỉ đại diện cho mức chịu ràng buộc của biên độ`
- CHUỖI THAY THẾ: `và hiệu ứng theo tháng tương ứng được ước lượng trên mã HOSE đối chứng; thước đo này chỉ đại diện gần đúng cho mức chịu ràng buộc của biên độ`

**A-34. MINOR. idx [177].** Lý do (vina-me tu-ngu.md, từ Hán Việt ít dùng): "dị biệt" lệch với thuật ngữ "khác biệt của tác động" dùng ở Bảng 4.
- CHUỖI GỐC: `là ước lượng dị biệt trong cùng một thiết kế`
- CHUỖI THAY THẾ: `là ước lượng khác biệt của tác động trong cùng một thiết kế`

**A-35. MINOR. idx [178].** Lý do (vina-me loi-thuong-gap.md, hai cách hiểu): "hai rổ lấy mẫu đồng thời" đọc được như hai rổ được lập bằng cách lấy mẫu.
- CHUỖI GỐC: `trên chuỗi lợi suất tuần của hai rổ lấy mẫu đồng thời`
- CHUỖI THAY THẾ: `trên chuỗi lợi suất tuần của hai rổ, được lấy mẫu lại đồng thời`

**A-36. MINOR. idx [184].** Lý do (vina-me loi-thuong-gap.md, câu thiếu vị ngữ chính): "Thứ nhất, xu hướng song song, kiểm tra bằng…" chưa thành câu.
- CHUỖI GỐC: `Thứ nhất, xu hướng song song, kiểm tra bằng`
- CHUỖI THAY THẾ: `Thứ nhất là xu hướng song song, được kiểm tra bằng`

**A-37. MINOR. idx [186].** Lý do (vina-me cau-va-doan.md, trạng ngữ đầu câu ngăn bằng dấu phẩy).
- CHUỖI GỐC: `Vì vậy nhóm đối chứng HOSE`
- CHUỖI THAY THẾ: `Vì vậy, nhóm đối chứng HOSE`

**A-38. MINOR. idx [205].** Lý do (vina-me loi-thuong-gap.md, hai cách hiểu): hai điều kiện "hoặc" đi với hai cách xử lý "và", đọc như cả hai cách xử lý áp dụng cùng lúc.
- CHUỖI GỐC: `đề tài dùng toàn bộ tháng có sẵn và rổ 20 cổ phiếu`
- CHUỖI THAY THẾ: `đề tài dùng, tương ứng, toàn bộ tháng có sẵn hoặc rổ 20 cổ phiếu`

**A-39. MINOR. idx [76].** Lý do (econ-write, "however" của khoảng trống; scientific-writing): vế "còn các nghiên cứu khác xét nhiều nhóm yếu tố cùng lúc" chưa nói thiếu gì, trong khi đóng góp ở [83] là "đưa riêng" mức phát triển thị trường cổ phiếu vào mô hình.
- CHUỖI GỐC: `còn các nghiên cứu khác xét nhiều nhóm yếu tố cùng lúc`
- CHUỖI THAY THẾ: `còn các nghiên cứu khác xét nhiều nhóm yếu tố cùng lúc nên chưa tách riêng vai trò của thị trường cổ phiếu`

**A-40. MINOR. idx [64] (bảng chữ viết tắt).** Lý do (sciwrite acronym): ARIMA chỉ còn trong bảng chữ viết tắt. Bản cắt đã bỏ câu duy nhất dùng nó (v13, đoạn về Ta và Vuong, 2020).
- CHUỖI GỐC (một dòng của bảng): `ARIMA | Autoregressive Integrated Moving Average | Mô hình tự hồi quy tích hợp trung bình trượt`
- CHUỖI THAY THẾ: xóa cả dòng này khỏi bảng.

**A-41. MINOR (tách đoạn). idx [68]** (165 chữ: bối cảnh và bài toán số 19; phạm vi đề tài so với bài toán). Lý do: vina-me cau-va-doan.md.
- TÁCH TRƯỚC: `Đề tài không đề xuất mô hình trung tâm tài chính`

**A-42. MINOR (tách đoạn). idx [222].** Lý do (vina-me lien-ket.md): lý do thứ hai (ngôn ngữ giảng dạy) và lý do thứ ba (ngành tốt nghiệp, tín chỉ bổ sung) là hai ý khác nhau, còn lý do thứ nhất đã đứng thành đoạn riêng ở [221].
- TÁCH TRƯỚC: `Thứ ba, thí sinh tốt nghiệp`

**A-43. MINOR (tách đoạn). idx [255]** (166 chữ: hướng việc làm; cam kết nghĩa vụ theo Nghị quyết số 57/2026/NQ-HĐND). Lý do: vina-me cau-va-doan.md.
- TÁCH TRƯỚC: `Thí sinh cam kết thực hiện nghĩa vụ`

Ghi chú về mã: A-01 đến A-05 là MAJOR; A-06 đến A-43 là 38 mục MINOR.

## 4. Ghi chú không xếp mức (để điều phối viên quyết định, không bắt buộc sửa)

1. Nhãn xác minh thay đổi giữa v13 và v14. v13 có 13 nhãn, v14 còn 9. Các nhãn không còn: [CẦN XÁC MINH phạm vi sàn mà FTSE Russell sàng lọc trước ngày chuyển sàn] (nay [171] dẫn FTSE Russell, 2026a); [CẦN XÁC MINH quy tắc làm tròn giá trần và giá sàn…]; [CẦN XÁC MINH quy định bước giá theo từng thời kỳ] (có vẻ đã gộp thành [CẦN ĐỐI CHIẾU quy chế giao dịch gốc của HNX…] ở [117]); [CẦN XÁC MINH thứ tự tác giả trên trang bài của tạp chí]; [CẦN XÁC MINH tập, số và trang]. Agent A không đụng nhãn. Đề nghị xác nhận việc gỡ là có chủ đích và có nguồn.
2. Chỗ lặp còn sót sau khi cắt (paper-writing-skill, R19/R39): mốc "đăng ký trước … trước ngày 28/12/2026" xuất hiện ở [86], [142], [192] và Bảng 5; Kindleberger và Gehrig được tóm ba lần ([74], [93], [107]); việc loại mã thuộc danh sách FTSE Russell khỏi nhóm đối chứng HOSE được nêu hai lần ([171], [186]). Không sai; nếu còn cần rút thì câu cuối của [192] bỏ được mà không mất ý.
3. [74] dẫn Yao (2012) cho câu "Với Hà Nội, câu hỏi sau hợp nhất là nên chuyên môn hóa vào những thị trường nào". Yao nghiên cứu Luxembourg, nên câu đọc như Yao nói về Hà Nội. Câu này giống hệt v13, không do cắt.
4. Đoạn "Từ bằng chứng đến định hướng cho Hà Nội" ([190]) nằm trong 4.3.8 (thiết kế khác biệt kép), lệch chủ đề của mục. Vị trí này giống v13.
5. Nguồn của con số 299 mã ([75]) là Tuổi Trẻ Online (2026), nhưng mục [274] trong danh mục là bài về Bảng Chính và Bảng Tiêu chuẩn của HOSE. Nên kiểm lại bài đó có nêu 299 mã không (v13 cũng vậy, không do cắt; thuộc phạm vi đối chiếu nguồn).
6. Kiểm số hiệu ứng nhỏ nhất phát hiện được ([198]–[199]): tính tay khớp hết (xem mục 1, skill 11).
