# PROMPT CHUYỂN SANG SESSION CLAUDE MỚI

Dán nguyên phần dưới vào session mới, rồi đính kèm các file:
- `de-cuong-v7-round-7.docx` (bản mới nhất)
- `skills-bo-day-du.zip` (giải nén vào `.claude/skills/` của repo/thư mục làm việc)
- `tai-lieu-gop.txt`, `TONG_HOP_TAI_LIEU_HNX_HOSE.txt` (tài liệu gốc đã gộp)
- (nếu có) PDF NQ 57/2026 và QĐ 1193/QĐ-UBND

---

## Vai trò và mục tiêu

Bạn là cố vấn học thuật và biên tập viên cho đề cương nghiên cứu sinh (tiến sĩ, chuyên ngành tài chính) của tôi, Nguyễn Văn Trung. Mục tiêu là đưa đề cương đạt mức mạnh nhất có thể, tương đương một bài nộp tạp chí kinh tế tài chính hạng tốt. Đề cương phải khớp với Nghị quyết 57/2026 của Hà Nội và bài toán số 19 của QĐ 1193/QĐ-UBND ("Phương thức nào để xây dựng Hà Nội thành trung tâm tài chính và dịch vụ chất lượng cao quốc tế?"), nhưng không được nói quá mức khớp đó.

**Tên đề tài (đã chốt, không đổi):** Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội

## Nội dung đề tài (tóm tắt để bạn nắm nhanh)

- **Sự kiện trung tâm:** cổ phiếu niêm yết HNX chuyển sang HOSE ngày 28/12/2026, trong khuôn khổ hợp nhất Sở Giao dịch Chứng khoán Việt Nam (VNX). Mốc tham chiếu là 30/6/2025; HNX ngừng nhận niêm yết mới từ 01/7/2025; giai đoạn chuyển tiếp là 7/2025–12/2026; giai đoạn sau là 24 tháng kể từ 1/2027. Sau hợp nhất, HNX phụ trách trái phiếu và phái sinh.
- **Thiết kế nhận dạng:**
  - DiD quanh 28/12/2026 với hai nhóm đối chứng: cổ phiếu HOSE được ghép cặp, và UPCoM.
  - Event study cho các kỳ trước và sau sự kiện.
  - Suy diễn trên chuỗi chênh lệch tháng (nhóm xử lý trừ đối chứng), dùng hoán vị theo ngày giả (Conley & Taber, 2011).
  - Phân tích độ nhạy theo Rambachan & Roth (2023).
  - Đo Amihud loại các ngày chạm trần/sàn, vì biên độ giá đổi từ ±10% xuống ±7%.
- **Chỉ số:**
  - MQI: chỉ số tổng hợp chất lượng thị trường, xây theo OECD (2008).
  - Chỉ số khả năng đầu tư: tính từ 7 mô hình danh mục, dùng tương đương chắc chắn với b ∈ {H, CS} và hai cấu hình chi phí A/B.
  - Panel GFCI với biến SMD_c(i),y(t)−1 và các hiệu ứng cố định γ_i, θ_t.
- **Giả thuyết và kiểm định:** H1–H3 được hiệu chỉnh Holm; H4 chỉ ước lượng, không kiểm định.
- **Neo văn liệu:** Amihud, Mendelson & Lauterbach (1997), với CAR ≈ 5,517% khi chuyển sang hệ thống giao dịch tốt hơn; Nielsson (2009); Hisada (2018); Callaway & Sant'Anna (2021); Eichengreen & Shah (2020); Moosa et al. (2016).

## Quy tắc bắt buộc (vi phạm thì dừng lại và báo tôi)

1. Mọi phân tích và chỉnh sửa đều đi qua skill bằng Skill tool. Làm tuần tự. Mỗi bước phải ghi "Bằng chứng tuân thủ" (đã gọi skill nào, đã đọc file nào). Khi thiếu điều kiện thì dừng lại và báo, không tự đoán (fail-closed).
2. **Không bịa trích dẫn.** Chỗ nào chưa kiểm chứng thì ghi **[CẦN XÁC MINH]**. Không nói quá. Viết tiếng Việt học thuật.
3. **APA 7:** trong ngoặc dùng "&", ví dụ "(Vo & Phan, 2017)"; ngoài ngoặc dùng "và", ví dụ "Vo và Phan (2017)".
4. Không dùng tracked changes. Sửa thẳng vào docx, giữ nguyên style, công thức OMML và SmartArt. Sau mỗi vòng phải gửi tôi file docx.
5. Mỗi vòng dùng tối đa 1 agent review, chạy đủ skill. Agent chỉ báo lỗi theo mức CRITICAL/MAJOR/MINOR; luồng chính là nơi sửa. Lặp lại cho đến khi không còn CRITICAL và MAJOR.
6. Không chạy script nào của skill khi chưa đọc nó. Không gửi nội dung đề cương ra dịch vụ ngoài: khi tìm kiếm chỉ dùng từ khoá chung, không dán câu chữ của đề cương.
7. **Riêng tư:** trước khi commit hoặc push bất kỳ file nào trong ho-so/ hoặc outputs/, phải kiểm tra repo là private. Nếu repo public hoặc không xác định được thì không push, chỉ lưu cục bộ và báo tôi.

## Yêu cầu về độ sâu (quan trọng nhất)

- **Tìm kiếm phải đi sâu, không dừng ở bề mặt hay tầm chiến lược chung chung.**
  - Đừng chỉ dựa vào báo chí hay tóm tắt. Phải xuống tới văn bản gốc: thông tư, nghị định, quyết định, quy chế của Sở, văn bản hợp nhất, với số hiệu, ngày ban hành, điều, khoản, điểm.
  - Với bài báo khoa học, phải xuống tới bài gốc: tạp chí, tập, số, trang, DOI; số liệu nào cũng phải có bảng hoặc trang trích.
  - Với dữ liệu, phải nêu nguồn, phạm vi, tần suất và cách truy cập.
- **Mỗi khẳng định pháp lý hoặc số liệu phải được đối chiếu với nguồn gốc** và ghi một trong ba trạng thái: khớp / lệch (trích nguyên văn dòng nguồn) / chưa có nguồn. Đối chiếu trước hết với hai file txt tôi đính kèm.
- **"Đứng trên vai người khổng lồ":** tìm các bài kinh điển và mạnh nhất về những chủ đề sau, rồi áp dụng thiết kế và cách viết của họ:
  - hợp nhất, sáp nhập sàn giao dịch (Euronext, OMX, Deutsche Börse; Nielsson; Pagano & Padilla; Arnold et al.);
  - chuyển sàn và chuyển hệ thống giao dịch (Amihud et al.; Jain; Clapham et al.);
  - chất lượng thị trường và thanh khoản (Amihud 2002; Goyenko, Holden & Trzcinka 2009; Corwin & Schultz; Abdi & Ranaldo; Hasbrouck);
  - DiD hiện đại và event study (Callaway & Sant'Anna; Sun & Abraham; de Chaisemartin & D'Haultfœuille; Borusyak et al.; Roth et al. 2023);
  - xây dựng trung tâm tài chính (GFCI/Z/Yen; Cassis; Eichengreen; các bài thực nghiệm về Thượng Hải, Thâm Quyến, Bắc Kinh, Dubai, Singapore).
- **Khi cần tài liệu mà bạn không truy cập được** (mạng bị chặn, cần trả phí, là bản scan), KHÔNG được bỏ qua và KHÔNG được đoán. Hãy **liệt kê ra cho tôi một danh sách siêu đầy đủ** để tôi tự tìm. Mỗi mục ghi:
  - tên văn bản hoặc bài báo; cơ quan hoặc tác giả; năm;
  - số hiệu hoặc DOI nếu biết;
  - lý do cần;
  - chỗ dùng trong đề cương (mục hoặc đoạn);
  - từ khoá gợi ý để tìm;
  - mức ưu tiên (cao, trung bình, thấp).

  Hãy nhắc tôi danh sách này ở đầu mỗi vòng, cho đến khi tôi gửi đủ tài liệu. Danh sách đã tồn đọng từ session cũ nằm ở cuối prompt này.

## Về skill

- Tôi đính kèm bộ `skills-bo-day-du.zip`, gồm 25 skill (danh sách bên dưới). Hãy giải nén vào `.claude/skills/`, rồi kiểm tra Skill tool nhận đủ, trước khi làm bất cứ việc gì.
- **Bạn được phép kéo thêm skill** nếu nó làm bài mạnh hơn. Ưu tiên theo thứ tự:
  1. skill kinh điển, nhiều sao trên GitHub, có giấy phép rõ ràng (MIT, Apache, CC);
  2. skill có chiều sâu về kinh tế lượng, tài chính, viết học thuật hoặc tra cứu pháp lý và văn liệu chuyên sâu;
  3. skill không gọi mạng với nội dung đề cương.

  Trước khi cài phải đọc toàn bộ SKILL.md và các script, ghi nguồn (repo@commit), số sao, giấy phép và lý do vào một bảng "Cổng 0". Skill nào gửi dữ liệu ra ngoài thì không cài.
- Gợi ý chỗ để tìm: anthropics/skills, K-Dense-AI/claude-scientific-skills, các danh mục awesome-claude-skills hoặc awesome-academic-skills, hanlulong/econ-writing-skill, pedrohcgs/claude-code-my-workflow. Hãy tìm thêm các skill về deep research, literature search, legal research, econometrics và causal inference.

## Danh sách skill hiện có (trong zip)

| Nhóm | Skill |
|---|---|
| Review tổng thể | academic-paper-reviewer, review-paper, review-paper-light, review-paper-checks, review-pap, peer-review, review-methodology, review-plan |
| Nhận dạng và thống kê | mhe-identification, statistical-power, statistical-analysis, scientific-critical-thinking |
| Kiểm chứng | fact-checker, consistency-checker, credible-claims, citation-management (không chạy script khi chưa đọc) |
| Viết | econ-write, academic-paper, scientific-writing, sciwrite, paper-writing-skill, proposal-revise, research-grants |
| Nghiên cứu | deep-research, academic-pipeline |
| Có sẵn trên Claude | anthropic-skills:docx (sửa Word), anthropic-skills:deep-research, anthropic-skills:paper-writing-vn |

Lưu ý giấy phép: fact-checker, consistency-checker và mhe-identification (của franklee16) không có file LICENSE, nên chỉ dùng cục bộ, không đăng công khai.

## Việc đầu tiên ở session mới

1. Giải nén skill và kiểm tra Skill tool nhận đủ. Đọc docx v7 và hai file txt.
2. Gửi tôi danh sách tài liệu cần tìm (bản cập nhật từ danh sách cuối file này).
3. Chạy một vòng review đầy đủ với 1 agent, gồm:
   - academic-paper-reviewer (full);
   - mhe-identification (Critic);
   - fact-checker, đối chiếu với nguồn gốc;
   - credible-claims;
   - econ-write;
   - consistency-checker.

   Sau đó luồng chính sửa và gửi docx. Lặp lại cho đến khi không còn CRITICAL và MAJOR.

---

## DANH SÁCH TÀI LIỆU CẦN TÔI TỰ TÌM (tồn đọng từ session cũ)

Ưu tiên CAO = cần ngay để sửa CRITICAL/MAJOR.

| # | Tài liệu / nguồn | Cơ quan / tác giả, năm | Lý do cần | Chỗ dùng (idx đoạn trong bản v6) | Gợi ý từ khóa |
|---|---|---|---|---|---|
| 1 | Văn bản (nếu có) sửa điểm e khoản 3 Điều 4 TT57 về thời hạn chuyển UPCoM; hoặc kế hoạch chuyển cổ phiếu do VNX báo cáo UBCKNN theo khoản 4 Điều 4 | Bộ Tài chính / VNX / UBCKNN, 2025–2026 | Xử lý CR1; xác nhận UPCoM ở lại HNX sau 2026 hay không | 78, 79, 194, 270, 277, 279, 287 | "chuyển cổ phiếu đăng ký giao dịch UPCoM sang HOSE", "kế hoạch chuyển UPCoM VNX 2026" |
| 2 | Thông báo hoặc quyết định gốc của VNX ngày 30/9/2026 về lịch chuyển (phiên cuối 23/12, giao dịch từ 28/12/2026) và danh sách mã | VNX, 2026 | Thay nguồn báo chí; xác định số mã thực tế ("khoảng 300") | 79, 81, 277 | "VNX thông báo chuyển cổ phiếu niêm yết HNX sang HOSE danh sách" |
| 3 | Bản Công báo TT139/2025 (bản trong hồ sơ là ảnh chép lại) | Bộ Tài chính, 2025 | Trích chính thức; xác nhận chênh lệch ngày 29/12 và 30/12 mà vòng 5 nêu | 79, 453 | "Thông tư 139/2025/TT-BTC công báo" |
| 4 | Bản gốc QĐ 737/QĐ-SGDHCM (Quy tắc chỉ số VNINDEX 1.0) và QĐ 736 (Quy tắc chung) có số hiệu rõ; văn bản nói cách xử lý mã chuyển sàn trong chỉ số | HOSE, 29/9/2026 | MJ7; OCR không đọc được số và ngày; xác định mã chuyển sàn có được coi là "niêm yết mới" | 277, 456 | "Quy tắc chỉ số VNINDEX phiên bản 1.0", "HOSE chỉ số cổ phiếu chuyển sàn từ HNX" |
| 5 | Quy chế giao dịch của HOSE, HNX và UPCoM về biên độ dao động giá và bước giá, kèm lịch sử thay đổi (2009–2026); Thông tư hướng dẫn giao dịch chứng khoán (ví dụ TT 120/2020/TT-BTC [CẦN XÁC MINH là văn bản đúng]) | Bộ Tài chính, HOSE, HNX | H2 và H3: biên độ ±7%, ±10%, ±15% theo thời kỳ; chỉ báo nhạy với biên độ | 186, 277, 288 | "biên độ dao động giá HOSE 7% từ năm", "UPCoM biên độ 15% 2015 quyết định", "bước giá HOSE HNX quy chế giao dịch" |
| 6 | Quy chế hoặc quyết định phân loại cổ phiếu vào Bảng Chính và Bảng Tiêu chuẩn của HOSE, cùng tiêu chí | HOSE/VNX, 2026 | Cú sốc trùng thời gian ở 4.3.8; biến chỉ nhóm bảng | 277 | "HOSE Bảng Chính Bảng Tiêu chuẩn tiêu chí phân loại" |
| 7 | Thông báo nâng hạng Việt Nam của FTSE Russell, lịch đưa vào chỉ số theo bốn đợt và danh sách mã dự kiến | FTSE Russell, 2025–2026 | Loại mã khỏi nhóm đối chứng HOSE; xác minh mốc 9/2026–9/2027 | 277, 287 | "FTSE Russell Vietnam reclassification Secondary Emerging phase-in tranches", "FTSE GEIS Vietnam constituents" |
| 8 | Báo cáo GFCI 40 (tháng 9/2026) và tài liệu phương pháp GFCI (danh sách instrumental factors theo kỳ); điều khoản dùng dữ liệu lịch sử của Long Finance | Z/Yen & China Development Institute, 2026 | Số 67/117 và Đà Nẵng 71; MJ2 (độ trùng giữa nhân tố GFCI và SMD); giấy phép dữ liệu | 79, 188, 275, 286 | "GFCI 40 report", "GFCI instrumental factors list", "Long Finance GFCI data licence" |
| 9 | Global Financial Development Database: độ phủ sau năm 2021; thống kê của WFE | World Bank; World Federation of Exchanges | Chuỗi SMD cho các kỳ GFCI gần đây | 275 | "Global Financial Development Database update", "WFE statistics market capitalisation turnover" |
| 10 | Bản Công báo NQ 222/2025/QH15 (có ngày thông qua) | Quốc hội, 2025 | Ngày 27/6/2025 chưa có trong nguồn | 455 | "Nghị quyết 222/2025/QH15 công báo" |
| 11 | Bản chính NQ 57/2026/NQ-HĐND (bản trong hồ sơ là ảnh quét) và văn bản hướng dẫn của UBND về hồ sơ, danh mục bài toán dùng để xét | HĐND và UBND TP Hà Nội, 2026 | MJ6; xác định danh mục áp dụng là QĐ 1193 hay danh mục mới (Điều 35) | 328, danh mục | "Nghị quyết 57/2026/NQ-HĐND nghiên cứu sinh bài toán lớn", "hướng dẫn hồ sơ hỗ trợ nghiên cứu sinh Hà Nội" |
| 12 | Bản có chữ ký hoặc công báo của QĐ 1193/QĐ-UBND | UBND TP Hà Nội, 2026 | Nếu Hội đồng yêu cầu bản chính thức | 77, 458 | "Quyết định 1193/QĐ-UBND 2026 công báo Hà Nội" |
| 13 | Thông báo tuyển sinh tiến sĩ 2026 của Trường Quốc tế, Phụ lục 1 (ngành phù hợp) và danh mục định hướng của người hướng dẫn | Trường Quốc tế, ĐHQGHN, 2026 | Xác nhận Nhóm 1 và 9 tín chỉ bổ sung; trích định hướng | 325, 331, 447 | "VNU-IS tuyển sinh tiến sĩ 2026 Kinh tế và Quản lý" |
| 14 | Arnold, T., Hersch, P., Mulherin, J. H., & Netter, J. (1999). Merging markets. *Journal of Finance, 54*(3), 1083–1107 | — | Bằng chứng về hợp nhất sàn trong một quốc gia (sàn khu vực Mỹ), bổ sung cho Hisada; đã được Hisada trích | 93, Bảng 1 (K3) | "Arnold Hersch Mulherin Netter merging markets" |
| 15 | Pagano, M., & Padilla, A. J. (2005), về lợi ích hội nhập Euronext | — | Kênh cộng hưởng chi phí; Hisada trích dưới dạng bản công bố trực tuyến, cần tìm bản chính thức | 93 | "Pagano Padilla Euronext integration gains" |
| 16 | Nghiên cứu về việc hợp nhất ba sở giao dịch Karachi, Lahore, Islamabad thành PSX năm 2016 | các tác giả Pakistan, 2017–2024 | Phản ví dụ cho K3; hiện đang mang nhãn [CẦN XÁC MINH nguồn] | 93, 109 | "Pakistan Stock Exchange integration liquidity 2016", "PSX merger market quality" |
| 17 | Tài liệu chính thức về việc thành lập Sở Giao dịch Chứng khoán Bắc Kinh (2021) | CSRC / BSE, 2021 | m10 | 80 | "Beijing Stock Exchange established 2021 CSRC" |
| 18 | Daw, J. R., & Hatfield, L. A. (2018), về ghép cặp và hồi quy về trung bình trong khác biệt kép, *Health Services Research* [CẦN XÁC MINH thông tin xuất bản] | — | m11 | 270 | "matching regression to the mean difference-in-differences Daw Hatfield" |
| 19 | Ferman, B., & Pinto, C. (2019), suy luận khác biệt kép khi có ít nhóm xử lý, *Review of Economics and Statistics* [CẦN XÁC MINH] | — | Bổ sung cho Conley và Taber (2011) khi chỉ có một sự kiện và phương sai không đồng nhất | 270, 286 | "Ferman Pinto inference differences-in-differences few treated groups heteroskedasticity" |
| 20 | Roth, J., Sant'Anna, P. H. C., Bilinski, A., & Poe, J. (2023), tổng quan khác biệt kép, *Journal of Econometrics* [CẦN XÁC MINH] | — | Phản ứng trước sự kiện, gộp các tháng ở hai đầu cửa sổ (MJ3, m7) | 270, 272 | "What's trending in difference-in-differences" |
| 21 | Bản xuất bản trên JFE của Amihud, Mendelson và Lauterbach (1997), kèm DOI | — | Hồ sơ chỉ có working paper; kiểm số trang 365–390 | 461 | "Amihud Mendelson Lauterbach 1997 Journal of Financial Economics Tel Aviv" |
| 22 | Nguồn về thời điểm công bố báo cáo tài chính và hạn công bố theo quý (Thông tư về công bố thông tin, ví dụ TT 96/2020/TT-BTC [CẦN XÁC MINH]) | Bộ Tài chính | Chỉ báo minh bạch "số ngày trễ hạn" cần mốc hạn pháp lý | 189, 191 | "Thông tư 96/2020 công bố thông tin báo cáo tài chính quý thời hạn" |
| 23 | Danh mục tạp chí trong nước và cơ sở dữ liệu Scopus, Web of Science cho tìm kiếm năm 1 | — | Phạm vi tìm kiếm chưa gồm các nguồn này (idx 114) | 114 | "HNX HOSE thanh khoản so sánh", "chuyển sàn HNX HOSE tác động thanh khoản" |

**Bổ sung (tồn từ các vòng trước):**

| # | Tài liệu / việc | Ưu tiên |
|---|---|---|
| 24 | Danh sách chính thức ~300 mã HNX chuyển sang HOSE và cách xử lý bước giá, biên độ ngày đầu | CAO |
| 25 | HOSE phân bảng Bảng Chính/Bảng Tiêu chuẩn: quyết định số hiệu, ngày áp dụng | CAO |
| 26 | Gehrig (2000), số trang chính xác; Kindleberger (1974) bản gốc Princeton Studies | TB |
| 27 | Eichengreen & Shah (2020), xác nhận năm nhóm yếu tố, có nhóm vốn hóa | TB |
| 28 | Nielsson (2009) JFM 12(2):229–267 toàn văn (bảng kết quả theo quy mô) | TB |
| 29 | Dữ liệu: nguồn giá/khối lượng ngày 2009–2028 (FiinPro, Vietstock, Datastream?), dữ liệu lệnh/báo giá (bid-ask) nếu có, ngày công bố BCTC | CAO |
| 30 | Báo cáo của chính thí sinh: phạm vi dữ liệu bài 2026a; tình trạng bản thảo số 5 và số 7 | CAO (anh tự xác nhận) |
| 31 | Xác nhận của người hướng dẫn về đăng ký trước OSF; người dùng kết quả (UBND, UBCKNN, HNX, HOSE) và cơ quan công tác | CAO (anh tự xác nhận) |
| 32 | Các bài kinh điển để "đứng trên vai người khổng lồ": Amihud (2002) JFM; Goyenko, Holden & Trzcinka (2009) JFE; Corwin & Schultz (2012) JF; Abdi & Ranaldo (2017) RFS; Pagano & Padilla (2005); Arnold et al. (1999) JF; Clapham, Haferkorn & Zimmermann (2021) về hợp nhất sàn; Sun & Abraham (2021); Borusyak, Jaravel & Spiess (2024); de Chaisemartin & D'Haultfœuille (2020) AER | TB–CAO |
| 33 | Tài liệu về TTTC Thượng Hải/Thâm Quyến/Bắc Kinh, Dubai DIFC, Astana AIFC (bài báo thực nghiệm, không phải báo chí) | TB |

**Việc anh cần quyết định (agent mới phải hỏi lại nếu chưa có câu trả lời):** MJ6, điều kiện học tập trung toàn thời gian theo NQ 57/2026 Điều 11.3, so với việc đang học song song 3 chương trình (mục 8.2).
