# Nhật ký thay đổi vòng 14 (vòng cuối, đóng cổng)

Bản cuối: `outputs/round-14/de-cuong-v14-round-14.docx` (bản rút gọn; bản dài để tự đọc là `outputs/round-13/de-cuong-v13-round-13.docx`). Bản chữ: `v14-text-round-14.txt`. Validate PASSED; 7 công thức OMML; 8 bảng; không tracked changes; bảng không nền xám.

## 1. Đối chiếu bộ tài liệu vòng 12 (skill vn-legal-verify)
| Nhãn ở v13 | Kết quả | Nguồn |
|---|---|---|
| Quy tắc làm tròn giá trần/sàn | Gỡ. HOSE làm tròn xuống giá trần, lên giá sàn theo đơn vị yết giá | V1 (Quy định giao dịch đăng website HOSE, kèm Tờ trình 51/TTr-HTGD ngày 26/4/2025), mục 5.1 |
| Bước giá theo thời kỳ | Thu hẹp. HOSE 10/50/100 đồng (V1); HNX 100 đồng (V3, V4: bản tóm tắt của công ty chứng khoán) → nhãn CẦN ĐỐI CHIẾU quy chế gốc HNX (QĐ 529/QĐ-SGDHN) và bước giá HOSE trước 12/9/2016 | V1, V3, V4, V6, W07 |
| Phạm vi sàn FTSE sàng lọc | Gỡ. Ground Rules v14.4 liệt kê cả Ho Chi Minh Stock Exchange và Hanoi Stock Exchange (Main market) | V7 → FTSE Russell (2026a) |
| Thứ tự tác giả Eichengreen & Shah | Gỡ. Eichengreen là tác giả thứ nhất | Crossref (X) |
| Tập, số, trang Daw & Hatfield | Gỡ, thêm DOI 10.1111/1475-6773.12993 | Crossref (X), PubMed (W12) |
| Kế hoạch chuyển UPCoM | Giữ nhãn; thêm: đợt chuyển 28/12/2026 không gồm UPCoM | W02 (Báo Đầu tư Chứng khoán, 06/10/2026) và thông báo VNX |
| Lịch sử biên độ 2009–2025 | Giữ nhãn (chưa có quyết định UBCKNN từng lần) | V1, V3, V5, W09, W10 |
| Cách HOSE xử lý mã chuyển sàn trong chỉ số | Giữ nhãn | W01, W05, W06 không nêu |
| QĐ 737 số hiệu, ngày | Giữ nhãn (cần đọc bằng mắt bản PDF) | |
| Phạm vi sàn bài của thí sinh | Giữ nhãn (thí sinh tự kiểm) | |

Tham khảo mới: Báo Đầu tư Chứng khoán (2026); Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh (2025); FTSE Russell (2026a), FAQ đổi thành 2026b; Tuổi Trẻ Online (2026a) bài phân bảng và (2026b) bài ngày 30/9/2026 có con số 299 mã.

## 2. Rút gọn (skill vina-me, vietnamese-human-writing; luồng chính, không agent)
Văn xuôi thân bài (mục 4.1 đến trước mục 11, không tính bảng): 14.477 → 11.602 chữ, giảm 19,9%; tính cả bảng: giảm 17,6%. Cách cắt: bỏ đoạn trùng giữa 4.1 và 4.2, gộp đoạn mô tả thủ tục, rút phần kênh biên độ/bước giá/chỉ số và trụ sở, rút danh mục tệp đăng ký, rút phần dữ liệu và chỉ số. Không bỏ giả thuyết, phương trình, kiểm định, phương án dự phòng hay cam kết NQ 57 nào.

Sửa lỗi định dạng có từ v12: đoạn "trong đó A..." dưới phương trình (5) bị mất chỉ số dưới ở Postₜ, αᵢ, τₜ và bị in nghiêng tràn (do một lần thay chuỗi ở vòng 12); đã dựng lại. Thêm chỉ số dưới cho M1 và δₖ ở hai chỗ còn thiếu.

## 3. Cổng đóng 1: 2 agent
- **Agent A** (`reports/r14-gate1-A.md`), 14 skill: vina-me (chạy soat.mjs), vietnamese-human-writing, sciwrite, scientific-writing, econ-write, review-methodology, academic-paper-reviewer, mhe-identification, aer-identification, liquidity-measures, statistical-power (tính lại MDE: khớp), review-pap, peer-review, paper-writing-skill. Kết quả: 0 CRITICAL, 5 MAJOR, 38 MINOR (10 tách đoạn).
- **Agent B** (`reports/r14-gate1-B.md`), 11 skill: vn-legal-verify, fact-checker, credible-claims, consistency-checker, citation-management, research-grants, scientific-critical-thinking, academic-paper (citation-check), deep-research (fact-check), peer-review, proposal-revise. Kết quả: 0 CRITICAL, 3 MAJOR, 18 MINOR. Mọi khẳng định pháp lý khớp văn bản gốc.

### Đã sửa (76 thao tác, áp đúng chuỗi agent đưa)
| Mã | Nội dung |
|---|---|
| A-01 | Khôi phục mô tả câu hỏi số 2 và số 4 của bài toán 19 |
| A-02 | Sửa quan hệ nhân quả về β ở H1 và khôi phục ước lượng không có hiệu ứng cố định theo trung tâm |
| A-03 | Hết mâu thuẫn về giai đoạn chuyển tiếp (báo cáo riêng, không vào kiểm định chính) |
| A-04 | Thêm quy tắc chọn cửa sổ trước theo điểm gãy vào danh mục đăng ký trước |
| A-05 | Thống nhất định nghĩa ngày bị loại: "từ ngưỡng này trở lên" |
| B-M1 | Tách Tuổi Trẻ Online 2026a/2026b; con số 299 mã trỏ đúng bài 30/9/2026 |
| B-M2 | Ngưỡng Amihud: mức lợi suất tối đa giảm ở mã giá thấp (ví dụ 1.140 đồng → 6,14%); loại mã dưới mức giá tối thiểu ghi trong tệp đăng ký |
| B-M3 | Trình tự UPCoM: chuyển đúng hạn thì trước cửa sổ sau, chỉ vào cửa sổ sau nếu mốc bị lùi |
| MINOR | Viết tắt ở lần dùng đầu (GFCI, HNX, HOSE, rổ H); thuật ngữ thống nhất; trích dẫn cho mốc 01/7/2025 và TT 139; nhãn ngày giao dịch đầu tiên của UPCoM; trích yếu NQ 57; tên tiếng Anh HOSE; bỏ ARIMA; ký hiệu k; tiêu chí kỷ yếu theo NQ 57; 14 chỗ xếp nguồn theo bảng chữ cái (APA 7); nhãn Thông báo tuyển sinh; 10 chỗ tách đoạn; Yao (2012) không còn đọc như nói về Hà Nội |

### Không áp, để thí sinh quyết
- B-m13: đổi "văn bản xác nhận" thành "văn bản cam kết tiếp nhận hoặc sử dụng kết quả" ở chỉ tiêu (6) theo thuật ngữ TB 7215 (văn bản cam kết khó xin hơn).
- B-m15: DOI và URL còn thiếu ở một số mục danh mục (hồ sơ không có nên không điền).

## 4. Tự kiểm tra sau khi sửa (thay cho cổng 2, theo quyết định của thí sinh)
- validate.py: PASSED; 7 oMath; 8 bảng; 0 tracked changes.
- Quét định dạng: không còn ký hiệu mất chỉ số dưới, không còn đoạn in nghiêng tràn.
- Trích dẫn hai chiều: 78 mục danh mục đều được trích; không có trích dẫn trong bài thiếu mục.
- soat.mjs trên các đoạn đã sửa: chỉ còn "–" và "&" (miễn trừ APA 7) và chữ "CHIẾU" trong nhãn.

## 5. Nhãn còn lại (12)
Kế hoạch chuyển UPCoM; lịch sử biên độ 2009–2025; quy chế gốc HNX và bước giá HOSE trước 12/9/2016; ngày giao dịch đầu tiên của UPCoM; phạm vi sàn bài của thí sinh; cách HOSE xử lý mã chuyển sàn trong chỉ số; bản gốc Coval & Moskowitz, Loughran & Schultz; quy chế phân bảng; Thông báo tuyển sinh 2026; số hiệu, ngày QĐ 737; URL bài Tuổi Trẻ 30/9/2026; số trang Gehrig (2000).

Lưu ý: mục lục và danh mục bảng/hình có số trang tĩnh; mở bằng Word và cập nhật trường (F9) để số trang khớp sau khi rút gọn.

## 6. Cập nhật 17/10/2026: bài mã 19322 đã được đăng trực tuyến
Theo trang bài của tạp chí (https://malque.pub/ojs/index.php/msj/article/view/19322; Research Article, Accepted Articles, công bố ngày 09/10/2026; tác giả Nguyen Thanh Binh, Nguyen Van Trung, Nguyen Bach Diep, Ha Hong Hanh, Le Hong Minh):
- Chuyển bài từ Bảng 7 (dòng 1) sang Bảng 6 (dòng 4), trạng thái "Đã được chấp nhận đăng, công bố trực tuyến trong mục Accepted Articles ngày 09/10/2026". Tên tác giả và tên bài giữ như trên trang tạp chí.
- Ghi chú Bảng 6: các trạng thái tính đến 30/9/2026, riêng bài số 4 cập nhật đến 09/10/2026.
- Bảng 7 còn 8 bản thảo, đánh số lại 1–8; "chín" thành "tám", "ba bản thảo liên quan trực tiếp" thành "hai".
- Tham chiếu trong thân bài: bản thảo số 5 thành số 4, số 7 thành số 6 (mục 4.3.5 và 8.2); "bản thảo số 1" thành "bài báo số 4 ở Bảng 6".
- Validate PASSED; 7 công thức; 8 bảng.

## 7. Cập nhật 17/10/2026: công thức viết theo kiểu kinh tế lượng cổ điển
Theo yêu cầu của thí sinh (kiểu Yᵢ = β₁ + β₂Xᵢ + εᵢ; chỉ số dưới viết liền, không dấu phẩy):
- (1) MQIⱼₜ = (TKⱼₜ + HQⱼₜ + MBⱼₜ)/3 thay cho tổng có trọng số wⱼ = 1/(3·n_d(j)); kết quả không đổi (mỗi chỉ báo vẫn có trọng số 1/9, 1/6 hoặc 1/3). Sàn đổi ký hiệu từ k sang j để k chỉ dùng cho tháng sự kiện ở (6).
- (2) U = μ − (ρ/2)σ²; (3) Gₘ = Uₘ(H) − Uₘ(CS); (4) Ḡ = (G₁ + G₂ + … + G₇)/7; chỉ số cửa sổ t và rổ b được nói bằng lời.
- (5) Aᵢₜ = αᵢ + τₜ + δDᵢPostₜ + εᵢₜ.
- (6) Aᵢₜ = αᵢ + τₜ + Σₖ δₖDᵢTₖₜ + εᵢₜ; Tₖₜ thay cho 1[t = k]; nhóm các tháng trước 1/2024 nói bằng lời.
- (7) Zᵢₜ = γᵢ + θₜ + βSMDᵢₜ + λWᵢₜ + uᵢₜ; bỏ chỉ số lồng c(i), y(t)−1, nói bằng lời "đo ở quốc gia chứa trung tâm i, năm liền trước kỳ t".
- Viết lại các đoạn "trong đó" và các chỗ nhắc ký hiệu (Eₛᵢ, Gₘ, Dᵢ × Postₜ). Không còn chỉ số dưới nào có dấu phẩy. Validate PASSED; 7 công thức; 8 bảng.
- Bỏ dấu nhân (· và ×): tích viết liền theo kiểu sách kinh tế lượng (DᵢPostₜ, Eₛᵢτₜ).

## 8. Cập nhật 17/10/2026: soát ký hiệu bằng 3 skill kinh tế lượng mới
Bằng chứng tuân thủ: gọi qua Skill tool panel-data-guide, mostly-harmless-guide, latex-econ-model (cài ở vòng 5 cổng 0).
- panel-data-guide: ký hiệu dữ liệu bảng Yᵢₜ (chỉ số dưới viết liền), hiệu ứng cố định αᵢ: khớp.
- mostly-harmless-guide: khác biệt kép là hồi quy hai chiều hiệu ứng cố định với biến xử lý; phiên bản nghiên cứu sự kiện có các biến trước sự kiện để kiểm tra xu hướng: khớp (5), (6).
- latex-econ-model: "ký hiệu nhất quán trong toàn bài", "chữ dùng làm tên viết thẳng", "tham số là chữ Hy Lạp", "nhân ngầm định".
Sửa: (7) đổi γᵢ, θₜ, uᵢₜ thành αᵢ, τₜ, εᵢₜ để cùng bộ ký hiệu với (5), (6): Zᵢₜ = αᵢ + τₜ + βSMDᵢₜ + λWᵢₜ + εᵢₜ. "Post" và "SMD" viết chữ đứng. Bổ sung "εᵢₜ là sai số" trong lời giải thích (5) và (7). Validate PASSED.

## 9. Cập nhật 17/10/2026: thí sinh trả lời nhãn
- Phạm vi sàn bài Nguyễn và Nguyễn (2026a) và bản thảo số 4, số 6: HOSE. Ghi vào mục 4.3.5, gỡ nhãn.
- Thông báo tuyển sinh: thí sinh quyết không cần số hiệu; gỡ nhãn.
- URL Tuổi Trẻ Online (2026b): https://tuoitre.vn/toan-bo-co-phieu-tren-hnx-se-chuyen-sang-hose-tu-28-12-100260930201353937.htm; gỡ nhãn.
- Lưu bài Thời báo Tài chính Việt Nam ngày 30/9/2026 ("Chốt thời điểm chuyển toàn bộ cổ phiếu niêm yết về HOSE") vào ho-so/. Bài khớp lịch VNX đã dẫn; không nêu số hiệu QĐ 737, không nêu lịch UPCoM, không nêu ngày của bài "Chuyển toàn bộ cổ phiếu HNX sang HOSE trong năm 2026…" nên ba nhãn tương ứng giữ nguyên.
Còn 9 nhãn. Validate PASSED.

## 10. Cập nhật 17/10/2026: tìm kiếm web (từ khoá chung, không gửi câu chữ đề cương)
| Nhãn | Kết quả | Nguồn (bậc) | Xử lý |
|---|---|---|---|
| Ngày giao dịch đầu tiên của UPCoM | 24/6/2009, nhiều nguồn khớp | nhadautu.vn, vneconomy.vn, vnexpress.net, BSC (báo chí, công ty chứng khoán) | Gỡ nhãn; ghi "khi UPCoM khai trương (ngày 24/6/2009)" |
| Bản gốc Coval & Moskowitz (1999), Loughran & Schultz (2005) | Tóm tắt khớp câu dẫn: nhà quản lý quỹ Mỹ ưa cổ phiếu doanh nghiệp có trụ sở gần; doanh nghiệp nông thôn giao dịch ít hơn, ít chuyên gia phân tích hơn, chi phí giao dịch cao hơn | IDEAS/RePEc (tóm tắt) | Gỡ nhãn; thêm DOI 10.1111/0022-1082.00181 cho Coval & Moskowitz |
| Số trang Gehrig (2000) | 415–445 (đa số nguồn; một nguồn ghi 415–446) | Các bài trích dẫn trên Springer, ScienceDirect | Điền 415–445 |
| Bước giá HOSE trước 12/9/2016 | Báo chí: 100 đồng (dưới 50.000), 500 đồng (50.000–dưới 100.000), 1.000 đồng (từ 100.000); quyết định 341/QĐ-SGDHCM ngày 22/8/2016 | vnbusiness.vn (báo chí) | Thu hẹp nhãn về hai quy chế gốc |
| QĐ 737/QĐ-SGDHCM | Không tìm thấy; chỉ thấy QĐ 747/QĐ-SGDHCM (HOSE-Index 4.0, 2025) | thitruongtaichinhtiente.vn | Giữ nhãn; thí sinh đọc bản PDF gốc |
| Lịch chuyển UPCoM; cách HOSE đưa mã chuyển sàn vào chỉ số; quy chế phân bảng; các lần đổi biên độ 2009–2025 | Không có văn bản chính thức (chỉ có: UPCoM ±15% từ 20/6/2017 theo vneconomy) | | Giữ nhãn |
Truy cập trực tiếp các trang báo bị chặn (ENOTFOUND), nên chỉ đối chiếu qua kết quả tìm kiếm. Còn 6 nhãn. Validate PASSED.

## 11. Cập nhật 17/10/2026: đối chiếu QĐ 529/QĐ-SGDHN (skill vn-legal-verify)
| Khẳng định (4.3.2) | Văn bản & điều khoản | Bậc nguồn | Trạng thái | Trích nguyên văn |
|---|---|---|---|---|
| Bước giá khớp lệnh cổ phiếu ở HNX là 100 đồng cho mọi mức giá | QĐ 529/QĐ-SGDHN ngày 25/8/2016, Quy chế kèm theo, Điều 23 khoản 1; hiệu lực 12/9/2016, thay QĐ 345/QĐ-SGDHN ngày 29/7/2013 | 3 (thuvienphapluat, do thí sinh dán) | KHỚP | "Đơn vị yết giá quy định đối với giao dịch khớp lệnh cổ phiếu là 100 đồng" |
Mức 100 đồng hiện hành cũng khớp bản tóm tắt quy định HNX năm 2025 (V3, bộ tài liệu vòng 12). Thêm mục danh mục "Sở Giao dịch Chứng khoán Hà Nội. (2016)", dẫn trong bài (…, 2016, Điều 23). Nhãn thu hẹp còn: bước giá của HOSE trước 12/9/2016 (QĐ 341/QĐ-SGDHCM). Quy chế 529 không quy định chiều làm tròn giá trần/sàn; không ảnh hưởng thiết kế vì ngưỡng Amihud đặt theo quy tắc làm tròn của HOSE. Lưu bản trích ở ho-so/TaiLieu_Vong14_QD529-SGDHN_2016_trich.txt. Validate PASSED.

## 12. Cập nhật 17/10/2026: gỡ hết nhãn (thí sinh giao quyết định)
- QĐ 737/QĐ-SGDHCM: số 737, ngày 29/9/2026 theo tên tệp công bố của VNX (…20260929_QD737_SGDHCM_QTCS-VNINDEX.pdf), khớp với căn cứ CV 1314/SGDVN-CLPT ngày 25/9/2026 trong văn bản; thêm URL.
- QĐ 341/QĐ-SGDHCM ngày 22/8/2016 (hiệu lực 12/9/2016, thay QĐ 314/QĐ-SGDHCM; theo thuvienphapluat): thêm vào danh mục; dùng làm mốc đổi bước giá HOSE. Không nêu số bước giá HOSE trước 2016 vì báo chí ghi không thống nhất.
- Lịch sử biên độ, bước giá: chuyển thành việc của quý 1 năm thứ nhất (lập bảng theo thời kỳ từ quyết định gốc).
- Lịch chuyển UPCoM, cách HOSE đưa mã chuyển sàn vào chỉ số, quy chế phân bảng: ghi đúng tình trạng (chưa có văn bản đến 17/10/2026) và cách đề tài cập nhật khi có công bố.
- Chỉ tiêu (6) và mục 4.4: "văn bản xác nhận hoặc cam kết sử dụng kết quả".
Không còn nhãn [CẦN…]. Validate PASSED. DOI: đang tìm, bổ sung ở bản sau.
