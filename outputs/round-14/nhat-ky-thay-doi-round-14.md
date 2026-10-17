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
