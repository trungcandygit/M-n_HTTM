# Phản biện vòng 12, Agent A (phương pháp và văn phong tiếng Việt)

Đề cương: "Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội" (bản v11). Người phản biện: Claude, Agent A. Ngày: 16/10/2026. Báo cáo chỉ đọc đề cương, không sửa đề cương. Mục tiêu: xác nhận các sửa của vòng 11, tìm CRITICAL/MAJOR còn lại, và rà văn phong tiếng Việt học thuật cho toàn bài.

Quy ước: idx là số thứ tự đoạn trong `scratchpad/r12/dump-v11.txt`. Trong dump, chỉ số dưới viết liền ("Postt", "Es,i", "δk"); trong docx đó là chỉ số dưới định dạng Word, nên khi tìm chuỗi gốc trong docx cần bỏ qua định dạng này. Mọi CHUỖI GỐC dưới đây đã được kiểm bằng script: mỗi chuỗi xuất hiện đúng một lần trong dump. Ký hiệu `[XUỐNG ĐOẠN]` trong chuỗi thay thế nghĩa là tách đoạn tại đó.

---

## (1) Bằng chứng tuân thủ

**Tệp đã đọc (chỉ đọc):**
- `scratchpad/r12/dump-v11.txt`: đọc toàn văn, idx 0–612.
- `outputs/round-11/de-cuong-v11-round-11.docx`: đọc `word/document.xml` bằng `zipfile` (Python, `-I`), trích 7 công thức OMML. Công thức (5) là `A = α + τ + δ·D·Post + ε`. Công thức (6) có số hạng `δpre·Di·1[t<1/2024]`. Phần mở rộng theo mức chịu cú sốc (idx 331) và theo trụ sở (idx 334) **vẫn chỉ viết bằng lời, không có công thức hiển thị**.
- `reports/r10-review-A.md` (toàn bộ) và `outputs/round-11/nhat-ky-thay-doi-round-11.md` (toàn bộ).
- `ho-so/TaiLieu_Vong8_GopTXT_16-10-2026.txt`: grep có chủ đích.
  - Quy tắc chỉ số VNINDEX (dòng 2358–2363): "Chỉ số giá VNINDEX được tính toán dựa trên giá trị vốn hóa thị trường **không điều chỉnh tỷ lệ free-float** và không áp dụng giới hạn tỷ trọng vốn hóa". VNALLSHARE (dòng 2553–2556) thì có điều chỉnh free-float và phải qua sàng lọc. Đây là căn cứ của m3.
  - Giá trần, giá sàn (dòng 3782): chỉ có công thức "Giá tham chiếu × (100% ± Biên độ)", không có quy tắc làm tròn theo bước giá. Vì vậy MJ1 gắn nhãn [CẦN XÁC MINH] cho quy tắc làm tròn, và cách sửa đề xuất đúng dù quy tắc làm tròn ra sao.

**Thứ tự gọi skill (Skill tool, tuần tự):** academic-paper-reviewer → mhe-identification (Critic) → aer-identification → review-methodology → liquidity-measures → statistical-power → review-pap → scientific-writing → econ-write → vina-me → vietnamese-human-writing → sciwrite.

**Lỗi và cách xử lý:**
- **academic-paper-reviewer.** Chế độ re-review cần họ contract `shared/contracts/re_review/` và agent con. Lỗi nguyên văn: `ls: cannot access '/home/user/M-n_HTTM/.claude/skills/academic-paper-reviewer/shared/contracts/re_review/': No such file or directory`. Phiên này không có công cụ Agent. Tôi tự đóng năm vai (Journal-Fit, Methodology, Domain, Perspective, Devil's Advocate) trong một ngữ cảnh; năm vai không độc lập, NOT_CALIBRATED. Không chạy `check_acronyms.py`.
- **review-pap.** SKILL.md đòi 6 agent song song và lưu `reviews/PAP_REVIEW_*.md`. Không có công cụ Agent nên tôi đọc SKILL.md và tự áp checklist của 6 agent trong một ngữ cảnh. Không tạo thư mục `reviews/`.
- **statistical-power.** Không chạy `scripts/power.py`, `simulate_power.py`; không cài gói (máy không có SciPy). Tôi tự viết `scratchpad/r12/sim/mde.py` (NumPy và `statistics.NormalDist`), tính chính xác phương sai của hiệu hai trung bình trên chuỗi AR(1) dừng với độ lệch chuẩn không điều kiện bằng 1. Không dùng dữ liệu thật.
- **mhe-identification.** Không có `references/sources/`, nên không dẫn trang sách MHE.
- **vina-me.** Đọc SKILL.md (có ghi chú miễn trừ APA 7), `dau-hieu.md`, `cau-va-doan.md`, `loi-thuong-gap.md`, `tu-ngu.md`, `lien-ket.md`. Chạy `node .../vina-me/scripts/soat.mjs` trên hai bản txt trong scratchpad (`body-v11.txt`, `body2-v11.txt`, idx 93–408, mỗi đoạn cách một dòng trống). Bỏ qua cảnh báo "–" và "&" theo miễn trừ.
- **vietnamese-human-writing.** Đọc SKILL.md và toàn bộ `references/master-writing-rules.md`; áp 7 vòng rà cho thể loại văn khoa học.
- Không tra web, không gửi câu chữ đề cương ra ngoài, không chạy script nào của skill ngoài `soat.mjs`.

---

## (2) Tổng hợp

**0 CRITICAL, 2 MAJOR, 13 MINOR.** Ngoài ra có 34 đề xuất sửa văn phong (mục 5) và 16 dòng thuật ngữ cần thống nhất (mục 6).

Thiết kế H3 chính (δ, chuỗi dₜ, bootstrap tự hồi quy, MDE) vững; các con số MDE ở idx 358–359 khớp phép tính chính xác của tôi. Hai MAJOR còn lại đều nằm ở phần đo lường và phần mở rộng của H3.

| Mã | Mức | idx | Một dòng |
|---|---|---|---|
| MJ1 | MAJOR | 217, 218, 227, 324 | Quy tắc loại ngày liền sau dùng mốc "từ 7% trở lên", đúng bằng biên độ của HOSE, nên việc ngày chạm biên độ ở HOSE có bị tính hay không phụ thuộc vào cách làm tròn giá trần; tập ngày bị loại của nhóm chuyển sàn vẫn đổi theo sàn. Dùng chính ngưỡng chung cho cả hai quy tắc. |
| MJ2 | MAJOR | 331, 364 | Hiệu ứng theo tháng của mức chịu cú sốc biên độ chỉ ước lượng được trên mã UPCoM, nhưng chính đề cương coi việc UPCoM chuyển sang HOSE trước 31/12/2026 là khả năng chính; khi đó tương tác theo biên độ không còn nhận dạng được. Cần phương án thay thế đăng ký trước. |
| m1 | MINOR | 334 | Phân tích trụ sở thiếu số hạng biến chỉ trụ sở Hà Nội nhân hiệu ứng tháng, ước lượng trên mã đối chứng, như đã làm với Eₛ,ᵢ·τₜ. |
| m2 | MINOR | 334 | Việc có mặt trong HNX-Index áp dụng cho mọi mã chuyển sàn, nên không tạo khác biệt theo trụ sở. |
| m3 | MINOR | 330 | VN-Index tính theo vốn hóa không điều chỉnh tự do chuyển nhượng; thước đo mức chịu cú sốc chỉ số đang dùng vốn hóa tự do chuyển nhượng. |
| m4 | MINOR | 331 | Eₛ,ᵢ chỉ chia cho độ lệch chuẩn, chưa trừ trung bình, nên δ trong phương trình mở rộng là tác động tại Eₛ,ᵢ = 0 (với nghịch đảo giá, mức này không có thật). |
| m5 | MINOR | 333 | Chưa nêu mức ý nghĩa và số phía cho các hệ số tương tác (nằm ngoài Holm). |
| m6 | MINOR | 333 | "Hệ số tương tác riêng cho từng tháng" chưa định nghĩa rõ là hiệu hệ số góc giữa mã chuyển sàn và mã đối chứng. |
| m7 | MINOR | 332 | Mức chịu cú sốc chỉ số gần với nghịch đảo vòng quay; cần thêm tương tác với mức thanh khoản ban đầu để tách hồi quy về trung bình. |
| m8 | MINOR | 224 | "hai chỉ báo nhạy với biên độ" chưa nêu tên. |
| m9 | MINOR | 233 | "cắt đuôi ở phân vị 1% và 99% mỗi tháng" chưa nói rõ là winsorize hay loại bỏ, và tính trên mẫu nào. |
| m10 | MINOR | 365 | "tách tác động của biên độ giá" bằng các mã tự chuyển sàn là nói quá. |
| m11 | MINOR | 397 | Tiêu đề 6.1.1 vẫn là "Tác động theo mức chịu cú sốc", lệch với idx 332 ("không đo riêng tác động của từng quy tắc"). |
| m12 | MINOR | 332 | "được đo trước ngày 30/6/2025" lệch với idx 330 ("bằng dữ liệu đến ngày 30/6/2025"). |
| m13 | MINOR | 358 | σ trong phép tính MDE phải là độ lệch chuẩn không điều kiện của chuỗi; nói rõ để người đọc tính lại được. |

---

## (3) Kiểm các sửa vòng 11

| Mã vòng 10 | Nội dung yêu cầu | idx v11 | Kết quả | Ghi chú |
|---|---|---|---|---|
| A-MJ1 | Quy tắc loại ngày liền sau không phụ thuộc sàn | 217, 218, 227, 324 | **CHƯA ĐẠT hoàn toàn** | Quy tắc đã chung cho mọi mã, nhưng mốc 7% trùng biên độ HOSE nên vẫn phụ thuộc sàn. Xem MJ1. |
| A-MJ2 | Viết rõ Dᵢ·Postₜ·Eₛ,ᵢ, Eₛ,ᵢ·τₜ, giả định nhận dạng, mã rơi khỏi mẫu | 331 | ĐẠT một phần | Đặc tả và giả định nhận dạng đúng. Còn thiếu phương án khi mất mã UPCoM (MJ2) và cách chuẩn hóa (m4). Chưa có công thức hiển thị. |
| A-MJ3 | Suy luận cho tương tác dùng cùng thủ tục với δ | 333, 357 | ĐẠT | Lập luận đúng và nhất quán với idx 357. Cần định nghĩa chuỗi hệ số theo tháng (m6) và mức ý nghĩa (m5). |
| A-MJ4 + B-MJ1 | Bỏ kênh FTSE, thay thước đo chỉ số | 330, 345 | ĐẠT | FTSE chỉ còn dùng để làm sạch nhóm đối chứng. Thước đo mới cần khớp cách tính VN-Index (m3) và tách khỏi mức thanh khoản ban đầu (m7). |
| A-MJ5 + B-MJ3 | Phân tích trụ sở: kênh, ba cách đọc, MDE, ngoài Holm | 334–336 | ĐẠT | Còn m1 (thiếu hiệu ứng tháng riêng cho mã Hà Nội) và m2 (HNX-Index). |
| B-MJ2 | Lan tỏa dương của Amihud và cộng sự (1997) | 347 | ĐẠT | Câu đã chuyển sang trường hợp δ bị đánh giá thấp. |
| m1 (v10) | Bỏ "tác động theo từng kênh" | 113, 397 | ĐẠT một phần | idx 113 đạt; tiêu đề 6.1.1 ở idx 397 còn chữ "Tác động" (m11). |
| m2 (v10) | Ghi chú Bảng 2 | 223 | ĐẠT | |
| m3 (v10) | Thước đo bước giá | 330 | ĐẠT | Câu trong ngoặc quá tải, xem V2 ở mục 5. |
| m4 (v10) | Mô tả Rambachan–Roth | 329 | ĐẠT | Câu đúng nội dung nhưng khó đọc, xem V4. |
| m5 (v10) | Coval và Moskowitz nói về nhà quản lý quỹ | 334 | ĐẠT | |
| m6 (v10) | Giá trị p một phía trong Holm | 360 | ĐẠT | |
| m7 (v10) | Tách đoạn dài | toàn bài | ĐẠT một phần | Còn idx 330 (khoảng 310 âm tiết) và 334 (khoảng 266 âm tiết) mang hơn một ý; điểm tách ở V1–V3. |
| B-minor | Điều 4 TT 120/2020; nới biên độ không "như nhau"; rút ngắn chu kỳ thanh toán; UPCoM sang HOSE là khả năng chính; GFCI 40 có nhân tố mức chỉ số; dự phòng GFCI gồm "không được phép"; ngày ký; OSF có nghĩa tiếng Việt | 224, 346, 364, 341, 363, 609, 85 | ĐẠT | Đối chiếu trực tiếp trên dump. |
| NQ 57 | Chỉ tiêu (6) có văn bản xác nhận; cam kết nghĩa vụ điểm e khoản 2 Điều 15 | 123, 525 | ĐẠT | |
| Số liệu MDE | 0,64σ; 1,24σ; 1,76σ; hệ số 1,3 khi cửa sổ trước còn 24 tháng; ví dụ 0,25 và 22% | 358–359 | ĐẠT | Tính chính xác (AR(1), 193/18/24 tháng, một phía 0,05/3, 80%): 0,643σ; 1,239σ; 1,760σ; tỷ số 1,33 ở cả ba giá trị φ. 1,24 × 0,2 = 0,248; e^(−0,25) = 0,78, tức giảm khoảng 22%. |
| Số phương án dự phòng | "năm phương án" | 363–364, 433 | ĐẠT | Đếm đủ năm trường hợp, khớp giữa hai nơi. |

---

## (4) Phát hiện phương pháp theo mức

### CRITICAL

Không có.

### MAJOR

**MJ1. Mốc "từ 7% trở lên" của quy tắc loại ngày liền sau trùng đúng biên độ HOSE, nên tập ngày bị loại vẫn phụ thuộc sàn.**
- *idx:* 217, 218, 227, 324.
- *Skill:* liquidity-measures (mục 4.1–4.2), mhe-identification (đo lường kết quả bị xử lý tác động), review-pap (Agent 4, định nghĩa kết quả phải cố định trước).
- *Lý do:*
  - Ở HOSE, lợi suất của một ngày chạm trần là 7% nếu giá trần không bị làm tròn, và thấp hơn 7% nếu giá trần được làm tròn xuống theo bước giá [CẦN XÁC MINH quy tắc làm tròn; hồ sơ dòng 3782 chỉ có công thức chưa làm tròn]. Lợi suất tính trên giá điều chỉnh còn có thể lệch thêm ở ngày giao dịch không hưởng quyền.
  - Vì vậy quy tắc "loại ngày liền sau một ngày có |r| ≥ 7%" nằm đúng trên ranh giới. Trước sự kiện, mọi ngày 7–10% của mã chuyển sàn kích hoạt quy tắc. Sau sự kiện, cùng một cú sốc bị chặn ở trần ±7% và có thể chỉ ghi được 6,9%, nên không kích hoạt. Mã đối chứng HOSE thì gần như không bao giờ kích hoạt. Tập ngày bị loại của nhóm chuyển sàn vì thế vẫn đổi đúng tại ngày xử lý, tức vấn đề mà sửa A-MJ1 muốn loại bỏ.
  - Cách sửa bền: dùng **chính ngưỡng chung c** (đã đặt thấp hơn mức lợi suất lớn nhất đạt được ở ±7%) cho cả hai quy tắc. Một cú sốc có |r| tiềm ẩn ≥ c vẫn được ghi nhận là |r| ≥ c dù cổ phiếu giao dịch với biên độ ±10% hay ±7%, nên tập ngày bị loại không phụ thuộc sàn, bất kể quy tắc làm tròn ra sao.
- *Sửa:*
  - idx 217. CHUỖI GỐC: `tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày có lợi suất tuyệt đối từ 7% trở lên, giảm so với nhóm đối chứng`
    → CHUỖI THAY THẾ: `tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày có lợi suất tuyệt đối từ ngưỡng chung trở lên, giảm so với nhóm đối chứng`
  - idx 218. CHUỖI GỐC: `loại ngày liền sau ngày có lợi suất tuyệt đối từ 7% trở lên (chính)`
    → CHUỖI THAY THẾ: `loại ngày liền sau ngày có lợi suất tuyệt đối từ ngưỡng chung trở lên (chính)`
  - idx 227. CHUỖI GỐC: `thấp hơn biên độ ±7% (giá trị cụ thể ghi trong tệp đăng ký) và không liền sau một ngày có lợi suất tuyệt đối từ 7% trở lên; quy tắc loại ngày liền sau áp dụng như nhau cho mọi cổ phiếu và mọi giai đoạn, kể cả khi cổ phiếu chuyển sàn còn giao dịch với biên độ ±10%, để tập ngày bị loại không thay đổi theo sàn;`
    → CHUỖI THAY THẾ: `thấp hơn mức lợi suất tuyệt đối lớn nhất có thể đạt được ở biên độ ±7% sau khi làm tròn giá trần và giá sàn theo bước giá (giá trị cụ thể ghi trong tệp đăng ký) và không liền sau một ngày có lợi suất tuyệt đối từ chính ngưỡng chung đó trở lên; quy tắc loại ngày liền sau dùng cùng ngưỡng cho mọi cổ phiếu và mọi giai đoạn, vì một biến động vượt ngưỡng chung vẫn được ghi nhận là vượt ngưỡng dù cổ phiếu giao dịch với biên độ ±10% hay ±7%, nên tập ngày bị loại không thay đổi theo sàn [CẦN XÁC MINH quy tắc làm tròn giá trần và giá sàn theo bước giá của HOSE và HNX];`
  - idx 324. CHUỖI GỐC: `(thấp hơn biên độ ±7%) và không liền sau một ngày có lợi suất tuyệt đối từ 7% trở lên;`
    → CHUỖI THAY THẾ: `(thấp hơn mức lợi suất lớn nhất đạt được ở biên độ ±7%) và không liền sau một ngày có lợi suất tuyệt đối từ ngưỡng chung trở lên;`

**MJ2. Tương tác theo mức chịu cú sốc biên độ mất nhận dạng trong chính kịch bản mà đề cương coi là khả năng chính.**
- *idx:* 331, 364.
- *Skill:* mhe-identification (giả định nhận dạng của triple-difference phải có nhóm đối chứng trong cả hai giai đoạn), aer-identification (Mechanism vs. Identification), review-pap (Agent 2: tính nhất quán giữa phương án dự phòng và đặc tả; Agent 4: quy tắc quyết định khi mất dữ liệu).
- *Lý do:*
  - Idx 331: các số hạng Eₛ,ᵢ·τₜ của mức chịu cú sốc biên độ chỉ ước lượng trên mã UPCoM, vì mã HOSE không có ngày 7–10%.
  - Idx 364: đề cương coi việc UPCoM chuyển sang HOSE chậm nhất hết 31/12/2026 là khả năng chính, và khi đó nhóm đối chứng UPCoM chỉ dùng đến tháng liền trước ngày chuyển.
  - Ghép hai câu lại: trong kịch bản chính, không có mã UPCoM nào ở giai đoạn sau sự kiện, nên Eₛ,ᵢ·τₜ của biên độ không ước lượng được cho các tháng sau và hệ số Dᵢ·Postₜ·E_biên độ,ᵢ chỉ còn dựa vào so sánh trong nội bộ mã chuyển sàn, không có đối chứng. Tệp đăng ký phải ghi trước phải làm gì trong trường hợp này.
  - Cách sửa đề xuất: khi mất UPCoM, đo mức chịu cú sốc biên độ của mọi mã (chuyển sàn và HOSE đối chứng) bằng một thước đo đo được ở cả hai sàn, là tỷ lệ ngày có |r| từ ngưỡng chung trở lên trước ngày 30/6/2025, rồi ước lượng Eₛ,ᵢ·τₜ trên mã HOSE. Thước đo này chỉ là đại diện cho mức chịu ràng buộc của biên độ, nên phải ghi rõ.
- *Sửa:*
  - idx 331. CHUỖI GỐC: `tức mã UPCoM với mức chịu cú sốc biên độ và mã HOSE với hai mức còn lại.`
    → CHUỖI THAY THẾ: `tức mã UPCoM với mức chịu cú sốc biên độ và mã HOSE với hai mức còn lại. Nếu cổ phiếu UPCoM chuyển sang HOSE trước khi hết cửa sổ sau, là khả năng chính theo mục 4.3.10, mã UPCoM không còn dùng được cho các tháng sau ngày chuyển; khi đó mức chịu cú sốc biên độ của mọi mã, cả mã chuyển sàn lẫn mã HOSE đối chứng, được đo bằng tỷ lệ ngày có lợi suất tuyệt đối từ ngưỡng chung trở lên trong dữ liệu đến ngày 30/6/2025, các số hạng tương ứng được ước lượng trên mã HOSE đối chứng, và hệ số tương tác theo biên độ được báo cáo kèm ghi chú rằng thước đo này chỉ đại diện cho mức chịu ràng buộc của biên độ.`
  - idx 364. CHUỖI GỐC: `Chỉ số chất lượng thị trường vốn của UPCoM dừng tại tháng đó, và ước lượng chính chỉ dựa vào nhóm đối chứng HOSE.`
    → CHUỖI THAY THẾ: `Chỉ số chất lượng thị trường vốn của UPCoM dừng tại tháng đó, ước lượng chính chỉ dựa vào nhóm đối chứng HOSE, và tương tác theo mức chịu cú sốc biên độ chuyển sang thước đo thay thế nêu ở mục 4.3.7.`

### MINOR

**m1. Thiếu hiệu ứng tháng riêng cho doanh nghiệp có trụ sở tại Hà Nội.** idx 334. *Skill:* mhe-identification, review-pap (Agent 4). *Lý do:* hệ số của Dᵢ·Postₜ × trụ sở so sánh mã Hà Nội với mã nơi khác trong nhóm chuyển sàn. Một cú sốc chung theo tháng riêng của doanh nghiệp Hà Nội sau năm 2027 sẽ bị gán cho việc chuyển sàn. Với mức chịu cú sốc, đề cương đã thêm Eₛ,ᵢ·τₜ ước lượng trên mã đối chứng; phân tích trụ sở cần cùng cách làm để nhất quán.
- CHUỖI GỐC: `kèm tương tác với quy mô và ngành để chênh lệch không chỉ phản ánh khác biệt về cơ cấu doanh nghiệp.`
  → CHUỖI THAY THẾ: `kèm số hạng tích giữa biến chỉ trụ sở tại Hà Nội và hiệu ứng cố định theo tháng, ước lượng trên các mã HOSE đối chứng có trụ sở tại Hà Nội, để cú sốc chung theo tháng riêng của doanh nghiệp Hà Nội không bị gán cho việc chuyển sàn, và kèm tương tác với quy mô và ngành để chênh lệch không chỉ phản ánh khác biệt về cơ cấu doanh nghiệp.`

**m2. HNX-Index không tạo khác biệt theo trụ sở.** idx 334. *Skill:* review-methodology (lập luận về cơ chế). *Lý do:* mọi mã chuyển sàn đều rời HNX-Index, bất kể trụ sở ở đâu, nên ví dụ này không minh họa kênh khác biệt theo trụ sở.
- CHUỖI GỐC: `chẳng hạn mức độ đưa tin và việc có mặt trong HNX-Index.`
  → CHUỖI THAY THẾ: `chẳng hạn mức độ đưa tin và sự chú ý của nhà đầu tư ở nơi đặt sàn; việc có mặt trong HNX-Index áp dụng chung cho mọi mã chuyển sàn nên tự nó không tạo khác biệt theo trụ sở.`

**m3. Thước đo mức chịu cú sốc chỉ số chưa khớp cách tính VN-Index.** idx 330. *Skill:* liquidity-measures. *Lý do:* theo Quy tắc chỉ số VNINDEX (Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh, 2026; hồ sơ dòng 2362–2363), VN-Index tính theo vốn hóa không điều chỉnh tỷ lệ tự do chuyển nhượng. Áp lực cầu theo VN-Index vì vậy tỷ lệ với vốn hóa toàn phần; vốn hóa tự do chuyển nhượng chỉ đúng với các chỉ số có điều chỉnh, như VNALLSHARE (có sàng lọc).
- CHUỖI GỐC: `tạo áp lực cầu lớn hơn ở mã có vốn hóa tự do chuyển nhượng lớn so với giá trị giao dịch`
  → CHUỖI THAY THẾ: `tạo áp lực cầu lớn hơn ở mã có vốn hóa lớn so với giá trị giao dịch`
- CHUỖI GỐC: `tỷ số giữa vốn hóa tự do chuyển nhượng và giá trị giao dịch bình quân ngày (mức chịu cú sốc chỉ số).`
  → CHUỖI THAY THẾ: `tỷ số giữa vốn hóa và giá trị giao dịch bình quân ngày (mức chịu cú sốc chỉ số); vì VN-Index tính theo vốn hóa không điều chỉnh tỷ lệ tự do chuyển nhượng (Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh, 2026), thước đo chính dùng vốn hóa toàn phần, còn thước đo theo vốn hóa tự do chuyển nhượng được báo cáo thêm cho các chỉ số có điều chỉnh tỷ lệ này.`

**m4. Chưa trừ trung bình khi chuẩn hóa Eₛ,ᵢ.** idx 331. *Skill:* mhe-identification, econ-write (định nghĩa tham số). *Lý do:* khi có Dᵢ·Postₜ·Eₛ,ᵢ, δ là tác động tại Eₛ,ᵢ = 0. Nếu Eₛ,ᵢ chỉ chia cho độ lệch chuẩn, điểm 0 của nghịch đảo giá ứng với giá vô cùng lớn, nên δ trong phương trình mở rộng mất ý nghĩa và không so được với δ của phương trình (5).
- CHUỖI GỐC: `chuẩn hóa theo độ lệch chuẩn giữa các mã chuyển sàn,`
  → CHUỖI THAY THẾ: `trừ trung bình và chia cho độ lệch chuẩn giữa các mã chuyển sàn, để δ trong phương trình mở rộng là tác động tại mức chịu cú sốc trung bình,`

**m5 và m6. Định nghĩa chuỗi hệ số tương tác theo tháng và mức ý nghĩa.** idx 333. *Skill:* review-pap (Agent 1, Agent 4), statistical-power. *Lý do:* "hệ số tương tác riêng cho từng tháng" có thể hiểu là hệ số góc trong nội bộ mã chuyển sàn, trong khi giả định nhận dạng ở idx 331 cần hiệu giữa hệ số góc của mã chuyển sàn và của mã đối chứng. Các hệ số này ngoài Holm nên phải nêu mức ý nghĩa và số phía; chiều của tác động theo mức chịu cú sốc không được dự báo trước nên hai phía là lựa chọn an toàn.
- CHUỖI GỐC: `đề tài ước lượng hệ số tương tác riêng cho từng tháng, rồi áp dụng bootstrap tự hồi quy cho chuỗi hệ số theo tháng này;`
  → CHUỖI THAY THẾ: `đề tài ước lượng, cho từng tháng, hệ số góc của logarit Amihud theo mức chịu cú sốc ở các mã chuyển sàn trừ hệ số góc tương ứng ở các mã đối chứng, rồi áp dụng bootstrap tự hồi quy cho chuỗi hiệu số theo tháng này, với thống kê kiểm định là trung bình sau sự kiện trừ trung bình trong cửa sổ trước và mức ý nghĩa hai phía 5%;`

**m7. Mức chịu cú sốc chỉ số gần với nghịch đảo vòng quay.** idx 332. *Skill:* liquidity-measures (mục 4.7), mhe-identification. *Lý do:* vốn hóa chia giá trị giao dịch bình quân ngày xấp xỉ nghịch đảo vòng quay, nên mã có mức chịu cú sốc chỉ số cao thường là mã kém thanh khoản lúc ban đầu. Mã kém thanh khoản có thể cải thiện nhiều hơn do hồi quy về trung bình. Số hạng Eₛ,ᵢ·τₜ trên mã HOSE khử được một phần, nhưng nên thêm tương tác với mức thanh khoản ban đầu và báo cáo hệ số có và không có tương tác này.
- CHUỖI GỐC: `đề tài vì vậy đưa thêm tương tác với quy mô và báo cáo tương quan giữa các mức chịu cú sốc.`
  → CHUỖI THAY THẾ: `đề tài vì vậy đưa thêm tương tác với quy mô và với logarit Amihud tại ngày 30/6/2025, vì mức chịu cú sốc chỉ số gần với nghịch đảo của vòng quay và có thể chỉ phản ánh hồi quy về trung bình của mã kém thanh khoản, và báo cáo tương quan giữa các mức chịu cú sốc.`

**m8. "hai chỉ báo nhạy với biên độ" chưa có tên.** idx 224. *Skill:* review-pap (Agent 1: định nghĩa phải tái lập được). *Lý do:* người đọc không biết bỏ chỉ báo nào; tôi không đoán thay tác giả. Sửa này gộp với việc tách câu dài (V14 ở mục 5).
- CHUỖI GỐC: `[CẦN XÁC MINH các lần thay đổi biên độ trong giai đoạn 2009–2025], nên chỉ số được so sánh cả trên mẫu đối sánh theo quy mô và ngành và cả khi bỏ hai chỉ báo nhạy với biên độ.`
  → CHUỖI THAY THẾ: `[CẦN XÁC MINH các lần thay đổi biên độ trong giai đoạn 2009–2025]. Vì vậy, chỉ số được so sánh trên mẫu đối sánh theo quy mô và ngành, và được tính lại sau khi bỏ hai chỉ báo nhạy với biên độ [CẦN NÊU TÊN hai chỉ báo].`

**m9. "cắt đuôi" chưa rõ cách làm và mẫu tính.** idx 233. *Skill:* liquidity-measures (mục 2: nói rõ winsorize), review-pap (Agent 4). *Lý do:* "cắt đuôi" có thể là loại bỏ quan sát hoặc thay bằng giá trị phân vị. Nếu phân vị tính riêng theo sàn, ngưỡng cắt của mã chuyển sàn đổi khi mã đổi sàn.
- CHUỖI GỐC: `độ phi thanh khoản Amihud được cắt đuôi ở phân vị 1% và 99% mỗi tháng;`
  → CHUỖI THAY THẾ: `độ phi thanh khoản Amihud được giới hạn tại phân vị 1% và 99% (winsorize), với phân vị tính trên mẫu gộp các sàn trong từng tháng để ngưỡng không thay đổi khi cổ phiếu đổi sàn;`

**m10. Nói quá về các mã tự chuyển sàn.** idx 365. *Skill:* review-methodology (ngôn ngữ nhân quả). *Lý do:* các mã này tự chọn thời điểm chuyển, nên không "tách" được tác động của biên độ.
- CHUỖI GỐC: `Các mã đã tự chuyển sàn trước năm 2026 còn được dùng làm phân tích phụ để tách tác động của biên độ giá.`
  → CHUỖI THAY THẾ: `Các mã đã tự chuyển sàn trước năm 2026 còn được dùng trong một phân tích phụ mang tính mô tả về tác động của biên độ giá; vì các mã này tự chọn thời điểm chuyển, kết quả không được diễn giải là tác động tách riêng của biên độ.`

**m11. Tiêu đề 6.1.1.** idx 397. *Skill:* review-pap (Agent 2, nhất quán thuật ngữ). 
- CHUỖI GỐC: `6.1.1 Tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số;`
  → CHUỖI THAY THẾ: `6.1.1 Khác biệt của tác động theo mức chịu cú sốc biên độ, bước giá và chỉ số;`

**m12. "đo trước ngày" và "dữ liệu đến ngày".** idx 332. *Skill:* scientific-writing (nhất quán mốc thời gian).
- CHUỖI GỐC: `Mọi mức chịu cú sốc được đo trước ngày 30/6/2025,`
  → CHUỖI THAY THẾ: `Mọi mức chịu cú sốc được đo bằng dữ liệu đến ngày 30/6/2025,`

**m13. Nói rõ σ trong phép tính MDE.** idx 358. *Skill:* statistical-power (báo cáo đủ tham số để tái lập). *Lý do:* các con số 0,64σ, 1,24σ, 1,76σ chỉ đúng khi σ là độ lệch chuẩn không điều kiện của chuỗi; nếu σ là độ lệch chuẩn của nhiễu, MDE lớn hơn 1/√(1−φ²) lần.
- CHUỖI GỐC: `có hệ số φ và độ lệch chuẩn σ,`
  → CHUỖI THAY THẾ: `có hệ số φ và độ lệch chuẩn không điều kiện σ,`

**Ghi chú không tính lỗi (econ-write, review-pap Agent 1):** phương trình mở rộng của (5) theo Eₛ,ᵢ và theo trụ sở vẫn chỉ viết bằng lời. Nếu còn chỗ, một công thức (5a) giúp hội đồng đọc nhanh; đây là đề xuất, không phải lỗi.

---

## (5) Bảng sửa văn phong

Tiêu chí chọn: chỉ những câu có lỗi thật (câu quá tải nhiều ý, chủ ngữ mờ, câu hiểu hai cách, văn dịch, từ dùng sai nghĩa, thuật ngữ không thống nhất). Giữ nguyên dữ kiện, số liệu, trích dẫn. Xếp theo mức ảnh hưởng: **A** làm sai hoặc khó hiểu nghĩa; **B** câu quá tải, khó theo dõi; **C** văn dịch, thiếu thống nhất. Những dòng sửa có liên quan tới MINOR ở mục 4 đã ghi chú để tránh sửa chồng.

| # | idx | Mức | Vấn đề (skill) | CHUỖI GỐC | CHUỖI THAY THẾ |
|---|---|---|---|---|---|
| V1 | 327 | A | "bác bỏ giả thuyết không thường xuyên hơn" đọc thành "không thường xuyên"; câu hiểu hai cách (vina-me, loi-thuong-gap) | `cho thấy kiểm định này bác bỏ giả thuyết không thường xuyên hơn đáng kể so với mức danh nghĩa` | `cho thấy kiểm định này bác bỏ giả thuyết gốc với tần suất cao hơn đáng kể so với mức danh nghĩa` |
| V2 | 330 | A | Đoạn khoảng 310 âm tiết, ba ý (cơ chế, cách đo, FTSE); ngoặc đơn chứa cả một câu (vina-me cau-va-doan; vietnamese-human-writing R25, R31) | `nghịch đảo của giá đóng cửa bình quân (mức chịu cú sốc bước giá; kết quả được báo cáo thêm với mức thay đổi của bước giá tương đối khi chuyển sàn, tính từ quy định bước giá của hai sàn tại ngày 30/6/2025, và trên tỷ lệ ngày lợi suất bằng 0), và` | `nghịch đảo của giá đóng cửa bình quân (mức chịu cú sốc bước giá), và` |
| V2b | 330 | A | Đưa phần vừa gỡ khỏi ngoặc thành câu riêng và tách đoạn FTSE | `Việc FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số không được coi là một kênh` | `Với mức chịu cú sốc bước giá, kết quả được báo cáo thêm với mức thay đổi của bước giá tương đối khi chuyển sàn, tính từ quy định bước giá của hai sàn tại ngày 30/6/2025, và với thước đo tỷ lệ ngày lợi suất bằng 0. [XUỐNG ĐOẠN] Việc FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số không được coi là một kênh` |
| V3 | 330 | B | Tách đoạn giữa phần cơ chế và phần cách đo | `[CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong các chỉ số]. Đề tài đo ba mức chịu cú sốc` | `[CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong các chỉ số]. [XUỐNG ĐOẠN] Đề tài đo ba mức chịu cú sốc` |
| V4 | 329 | A | Câu Rambachan–Roth khoảng 79 âm tiết, chủ ngữ của "không vượt" bị chôn (sciwrite Pass 3; vina-me) | `Đề tài kiểm định đồng thời giả thuyết các hệ số δk từ tháng 1/2024 đến tháng 5/2025 bằng 0, và báo cáo độ nhạy của kết luận khi thay đổi giữa hai tháng liên tiếp của độ lệch khỏi xu hướng song song sau tháng gốc không vượt` | `Đề tài kiểm định đồng thời giả thuyết các hệ số δk từ tháng 1/2024 đến tháng 5/2025 bằng 0. Độ nhạy của kết luận được đánh giá theo Rambachan và Roth (2023), với giả định rằng sau tháng gốc, mức thay đổi giữa hai tháng liên tiếp của độ lệch khỏi xu hướng song song không vượt quá` |
| V4b | 329 | A | (tiếp V4) | `lần thay đổi lớn nhất giữa hai tháng liên tiếp trong các tháng 1/2024–6/2025, kèm giá trị` | `lần mức thay đổi lớn nhất giữa hai tháng liên tiếp trong các tháng 1/2024–6/2025; đề tài báo cáo giá trị` |
| V4c | 329 | A | (tiếp V4; trích dẫn đã chuyển lên câu trên) | `nhỏ nhất làm kết luận thay đổi (Rambachan & Roth, 2023); vì giữa tháng gốc` | `nhỏ nhất làm kết luận thay đổi. Vì giữa tháng gốc` |
| V5 | 324 | A | Câu khoảng 205 âm tiết; định nghĩa αᵢ, τₜ nằm cuối, cách xa phương trình; "tháng... được ước lượng" sai nghĩa (tháng không được ước lượng) (econ-write: định nghĩa ngay sau phương trình) | `Postt bằng 1 từ tháng 1/2027; phương trình (5) được ước lượng trên giai đoạn tham chiếu` | `Postt bằng 1 từ tháng 1/2027; αi và τt là hiệu ứng cố định theo cổ phiếu và theo tháng. Phương trình (5) được ước lượng trên giai đoạn tham chiếu` |
| V5b | 324 | A | (tiếp V5) | `gồm tháng chuyển sàn, chỉ được ước lượng trong phương trình (6); vì giai đoạn tham chiếu dài 16 năm` | `gồm tháng chuyển sàn, chỉ được đưa vào phương trình (6). Vì giai đoạn tham chiếu dài 16 năm` |
| V5c | 324 | A | (tiếp V5; bỏ định nghĩa lặp ở cuối) | `(7/2023–6/2025); αi và τt là hiệu ứng cố định theo cổ phiếu và theo tháng.` | `(7/2023–6/2025).` |
| V6 | 361 | A | Câu "lối vườn": "và đối chiếu" bị đọc như vế của "vì" (sciwrite Pass 3) | `vì điểm z theo kỳ thay đổi khi tập trung tâm thay đổi, và đối chiếu danh sách nhân tố công bố của từng kỳ GFCI với các thành phần của SMD, báo cáo tỷ lệ kỳ có trùng lặp; vì kỳ GFCI 40 đã có trùng lặp` | `vì điểm z theo kỳ thay đổi khi tập trung tâm thay đổi. Đề tài cũng đối chiếu danh sách nhân tố công bố của từng kỳ GFCI với các thành phần của SMD và báo cáo tỷ lệ kỳ có trùng lặp. Vì kỳ GFCI 40 đã có trùng lặp` |
| V7 | 363 | A | Chủ ngữ mờ: "câu hỏi 3 dùng" (vina-me cau-va-doan) | `nếu sự kiện không diễn ra, câu hỏi 3 dùng các mã đã tự chuyển từ HNX sang HOSE trước năm 2026.` | `nếu sự kiện không diễn ra, đề tài trả lời câu hỏi 3 bằng các mã đã tự chuyển từ HNX sang HOSE trước năm 2026.` |
| V8 | 403 | A | Lặp "quản lý", hai vế chọi nhau (đề tài "thuộc... quản lý" rồi lại "giao thoa với quản lý") | `còn đề tài thuộc tài chính định lượng và quản lý, và giao thoa với quản lý ở phần` | `còn đề tài thuộc tài chính định lượng và giao thoa với quản lý ở phần` |
| V9 | 128 | A | "đã chuẩn hóa" hiểu hai cách (đã thành chuẩn, hay đã chuẩn hóa z); đề nghị tác giả xác nhận nghĩa | `Các thước đo đã chuẩn hóa, nhưng chưa được quy đổi` | `Các thước đo này đã được dùng phổ biến, nhưng chưa được quy đổi` |
| V10 | 334 | B | Đoạn khoảng 266 âm tiết, hai ý (văn liệu và kênh; dự báo và đặc tả) | `Nếu việc sàn niêm yết đặt cùng thành phố với trụ sở doanh nghiệp` | `[XUỐNG ĐOẠN] Nếu việc sàn niêm yết đặt cùng thành phố với trụ sở doanh nghiệp` |
| V11 | 104 | B | Câu khoảng 88 âm tiết; "đồng thời" nối gượng (vina-me dau-hieu D) | `, và thấy lợi suất bất thường tích lũy điều chỉnh theo thị trường đạt khoảng 5,5% trong giai đoạn từ năm ngày trước công bố đến 30 ngày sau khi cổ phiếu giao dịch theo cơ chế mới, đồng thời mức tăng thanh khoản đi cùng mức tăng giá.` | `. Trong giai đoạn từ năm ngày trước công bố đến 30 ngày sau khi cổ phiếu giao dịch theo cơ chế mới, lợi suất bất thường tích lũy điều chỉnh theo thị trường đạt khoảng 5,5%, và mức tăng thanh khoản đi cùng mức tăng giá.` |
| V12 | 105 | B | Câu khoảng 91 âm tiết; "với thị trường... được hợp nhất" là văn dịch | `với thị trường cổ phiếu của hai sở được hợp nhất ngày 16/7/2013, trên mẫu các cổ phiếu niêm yết tại Tokyo không niêm yết kép tại Osaka, và thấy thanh khoản của nhóm cổ phiếu này tăng trong ngắn hạn nhờ hiệu ứng cộng hưởng và tâm lý nhà đầu tư, trong đó hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, rồi giảm sau một năm.` | `trong đó thị trường cổ phiếu của hai sở hợp nhất ngày 16/7/2013. Trên mẫu các cổ phiếu niêm yết tại Tokyo không niêm yết kép tại Osaka, thanh khoản tăng trong ngắn hạn nhờ hiệu ứng cộng hưởng và tâm lý nhà đầu tư, rồi giảm sau một năm; hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ.` |
| V13 | 130 | B | "với thước đo là" treo cuối câu, xa động từ (văn dịch) | `sau khi thị trường cổ phiếu của Osaka được hợp nhất vào Tokyo năm 2013, hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, với thước đo là vòng quay và độ phi thanh khoản Amihud.` | `sau khi thị trường cổ phiếu của Osaka được hợp nhất vào Tokyo năm 2013, đo bằng vòng quay và độ phi thanh khoản Amihud; hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ.` |
| V14 | 224 | B | Câu khoảng 92 âm tiết; "nên" ở cuối cách nguyên nhân quá xa (vế sau xem m8) | `±15% ở UPCoM; theo Điều 4` | `±15% ở UPCoM. Theo Điều 4` |
| V15 | 277 | B | Câu khoảng 74 âm tiết, ba lớp điều kiện; "chênh lệch giá chào mua và chào bán" lệch thuật ngữ | `gồm phí giao dịch, thuế và một nửa chênh lệch giá chào mua và chào bán, lấy từ giá chào đóng cửa nếu nhà cung cấp dữ liệu có, nếu không thì dùng chênh lệch ước lượng từ giá cao nhất và thấp nhất theo tháng (Corwin & Schultz, 2012), nên đo thêm kênh chi phí giao dịch mà sàn tác động.` | `gồm phí giao dịch, thuế và một nửa chênh lệch mua-bán. Chênh lệch này lấy từ giá chào mua và chào bán đóng cửa nếu nhà cung cấp dữ liệu có; nếu không, đề tài dùng chênh lệch ước lượng từ giá cao nhất và thấp nhất theo tháng (Corwin & Schultz, 2012). Nhờ vậy, cấu hình B đo thêm kênh chi phí giao dịch mà sàn tác động.` |
| V16 | 341 | B | Câu khoảng 64 âm tiết, hai vế "vì" lồng nhau | `Vì điểm GFCI gộp kết quả khảo sát với các nhân tố định lượng, trong đó nhóm phát triển khu vực tài chính có vốn hóa,` | `Điểm GFCI gộp kết quả khảo sát với các nhân tố định lượng; nhóm phát triển khu vực tài chính có vốn hóa,` |
| V16b | 341 | B | (tiếp V16) | `Wardle & Mainelli, 2026), và vì trung tâm mạnh có thể kéo theo giao dịch cổ phiếu, đề tài gọi β là liên hệ có điều kiện.` | `Wardle & Mainelli, 2026). Vì phần trùng lặp cơ học này, và vì trung tâm mạnh có thể kéo theo giao dịch cổ phiếu, đề tài gọi β là liên hệ có điều kiện.` |
| V17 | 346 | B | Câu khoảng 90 âm tiết, ba hành động sau một "nên" | `(Thời báo Tài chính Việt Nam, 2026); nếu các thay đổi này` | `(Thời báo Tài chính Việt Nam, 2026). Nếu các thay đổi này` |
| V17b | 346 | B | (tiếp V17) | `có thể tác động mạnh hơn ở mã thường chạm biên độ, nên ngày áp dụng được ghi là` | `có thể tác động mạnh hơn ở mã thường chạm biên độ. Khi đó, ngày áp dụng được ghi là` |
| V18 | 230 | B | Ba vế nối bằng chấm phẩy, đổi chủ thể giữa chừng | `được thí sinh số hóa từ báo cáo từng kỳ; thí sinh sẽ xin phép Long Finance dùng bộ dữ liệu lịch sử trước khi phân tích; nếu không được phép, phương án dự phòng thứ nhất ở mục 4.3.10 được áp dụng.` | `được thí sinh số hóa từ báo cáo từng kỳ. Trước khi phân tích, thí sinh sẽ xin phép Long Finance dùng bộ dữ liệu lịch sử; nếu không được phép, đề tài áp dụng phương án dự phòng thứ nhất ở mục 4.3.10.` |
| V19 | 283 | B | "tính bằng điểm phần trăm mỗi năm" treo cuối câu, gắn nhầm vào "rổ CS"; thiếu vế so sánh | `Chỉ số khả năng đầu tư dương nghĩa là nhà đầu tư đa dạng hóa đạt lợi suất tương đương chắc chắn thấp hơn với rổ CS, tính bằng điểm phần trăm mỗi năm.` | `Chỉ số khả năng đầu tư tính bằng điểm phần trăm mỗi năm; giá trị dương nghĩa là nhà đầu tư đa dạng hóa đạt lợi suất tương đương chắc chắn thấp hơn với rổ CS so với rổ H.` |
| V20 | 357 | C | "công suất" là thuật ngữ kỹ thuật điện; trong thống kê dùng "lực kiểm định"; "và... và vào... và" lặp (vina-me tu-ngu) | `Công suất của H3 phụ thuộc vào số tháng trước và sau sự kiện và vào phương sai và mức tự tương quan của chuỗi chênh lệch theo tháng; công suất chỉ phụ thuộc yếu` | `Lực kiểm định của H3 phụ thuộc vào số tháng trước và sau sự kiện, cùng với phương sai và mức tự tương quan của chuỗi chênh lệch theo tháng; lực kiểm định chỉ phụ thuộc yếu` |
| V20b | 357 | C | (tiếp V20) | `công suất của các hệ số này cũng bị giới hạn` | `lực kiểm định của các hệ số này cũng bị giới hạn` |
| V20c | 358 | C | (tiếp V20) | `ở công suất 80% và mức ý nghĩa một phía` | `ở lực kiểm định 80% và mức ý nghĩa một phía` |
| V21 | 106 | C | "biểu hiện thành", "thắng ổn định" là văn nói, văn dịch | `Với nhà đầu tư, tác động của sàn biểu hiện thành khả năng đầu tư, được đo trên bảy mô hình phân bổ vì không mô hình nào thắng ổn định (DeMiguel và cộng sự, 2009).` | `Đối với nhà đầu tư, tác động của sàn thể hiện qua khả năng đầu tư; đề tài đo khả năng đầu tư trên bảy mô hình phân bổ vì không mô hình nào vượt trội một cách nhất quán (DeMiguel và cộng sự, 2009).` |
| V22 | 115 | C | "với suy luận phù hợp" là văn dịch ("with inference suited to") | `với suy luận phù hợp cho một sự kiện duy nhất,` | `dùng phương pháp suy luận phù hợp với một sự kiện duy nhất,` |
| V23 | 97 | C | "thanh khoản nhất" là văn nói | `gồm những mã thanh khoản nhất của nhóm này` | `gồm những mã có thanh khoản cao nhất trong nhóm này` |
| V24 | 103 | C | "của mình" là văn dịch ("its"); "câu hỏi chuyên môn hóa" mơ hồ | `trong phần lớn giai đoạn phát triển của mình (Naeem, 2023). Trường hợp này cho thấy một thành phố có thể giữ vai trò trung tâm tài chính mà không cần sàn cổ phiếu, và đặt ra cho Hà Nội câu hỏi chuyên môn hóa (Yao, 2012) sau đợt hợp nhất.` | `trong phần lớn quá trình phát triển (Naeem, 2023). Trường hợp này cho thấy một thành phố có thể giữ vai trò trung tâm tài chính mà không cần sàn cổ phiếu, và đặt ra cho Hà Nội câu hỏi nên chuyên môn hóa vào những thị trường nào (Yao, 2012) sau đợt hợp nhất.` |
| V25 | 227 | C | Chêm "không bị cắt theo biên độ như Amihud" giữa chủ ngữ và vị ngữ, đọc thành vòng quay "như Amihud" | `Vòng quay, không bị cắt theo biên độ như Amihud, là thước đo đối chiếu.` | `Vòng quay là thước đo đối chiếu, vì vòng quay không dùng lợi suất nên không bị cắt theo biên độ như Amihud.` |
| V26 | 286 | C | Chêm "không cần ước lượng" làm câu như có hai chủ ngữ | `khoảng cách của M1, không cần ước lượng, được báo cáo riêng như phép so sánh sạch nhất.` | `vì M1 không cần ước lượng tham số, khoảng cách của M1 được báo cáo riêng như phép so sánh sạch nhất.` |
| V27 | 287 | C | "một tác động hợp lý" mơ hồ | `có thể lớn hơn nhiều so với một tác động hợp lý;` | `có thể lớn hơn nhiều so với mức tác động có thể xảy ra trên thực tế;` |
| V28 | 326 | C | "nhóm xử lý" chỉ xuất hiện một lần; mọi chỗ khác gọi là cổ phiếu chuyển sàn (sciwrite Pass 4) | `giữa nhóm xử lý và nhóm đối chứng:` | `giữa nhóm cổ phiếu chuyển sàn và nhóm đối chứng:` |
| V29 | 360 | C | "bootstrap khối" lệch với "bootstrap khối dừng" ở idx 242, 337 | `giá trị p bootstrap khối cho H2` | `giá trị p bootstrap khối dừng cho H2` |
| V30 | 364 | C | "rổ chuyển sàn" lệch với "rổ CS" | `hoặc rổ chuyển sàn có ít hơn 30 cổ phiếu đủ thanh khoản` | `hoặc rổ CS có ít hơn 30 cổ phiếu đủ thanh khoản` |
| V31 | 433 | C | Như V30 | `hoặc rổ chuyển sàn quá ít mã` | `hoặc rổ CS quá ít mã` |
| V32 | 422 | C | Tên chỉ số viết tắt tùy tiện | `chỉ số chất lượng bản đầu` | `Chỉ số chất lượng thị trường vốn bản đầu` |
| V33 | 232 | C | "khi UPCoM có giao dịch" thiếu ý mốc bắt đầu | `Mẫu bắt đầu từ tháng 6/2009, khi UPCoM có giao dịch.` | `Mẫu bắt đầu từ tháng 6/2009, khi UPCoM bắt đầu có giao dịch.` |
| V34 | 523 | C | Ba câu liền cùng khuôn "… cho thí sinh kinh nghiệm với …" (vietnamese-human-writing R35, R43) | `Bài báo Nguyễn và Nguyễn (2026a) cho thí sinh kinh nghiệm với mô hình Black-Litterman` | `Qua bài báo Nguyễn và Nguyễn (2026a), thí sinh đã làm việc với mô hình Black-Litterman` |

Các dấu hiệu đã soát nhưng **không** đề xuất sửa: "đồng thời" (4 lần, ở idx 104 đã sửa trong V11, các chỗ còn lại dùng đúng nghĩa "cùng lúc"); "không chỉ" (2 lần, đều là phủ định thật, không phải khuôn "không chỉ… mà còn"); ba đoạn "Câu hỏi 1/2/3" mở bằng "Câu hỏi" là danh sách, không phải khuôn văn mẫu; "Đề tài" làm chủ ngữ cho hành động phân tích là quy ước chấp nhận được trong đề cương tiếng Việt.

---

## (6) Bảng thuật ngữ thống nhất

| Thuật ngữ (khái niệm) | Cách viết chọn dùng | Biến thể đang có (idx) | Ghi chú |
|---|---|---|---|
| Robustness check | kiểm tra độ vững | "kiểm tra độ bền" (237, 241, 361, 391); "kiểm tra độ vững" (125) | "Độ vững" là cách dùng phổ biến trong kinh tế lượng tiếng Việt và khớp với "danh mục vững chắc". Nếu tác giả muốn giữ "độ bền" thì sửa idx 125 cho thống nhất. |
| Statistical power | lực kiểm định | "công suất" (357, 358) | Xem V20. |
| Null hypothesis | giả thuyết gốc | "giả thuyết không" (327) | Tránh ký hiệu H0 vì dễ lẫn với H1–H4. Xem V1. |
| Treated group | nhóm cổ phiếu chuyển sàn; cổ phiếu chuyển sàn | "nhóm xử lý" (326); "mã chuyển sàn" (10 lần, ví dụ 330, 331, 333) | "mã chuyển sàn" dùng được khi nói từng mã; "nhóm xử lý" bỏ. |
| Rổ cố định của cổ phiếu chuyển sàn | rổ CS (sau lần định nghĩa đầu ở idx 276) | "rổ chuyển sàn" (364, 433); "rổ cổ phiếu chuyển sàn" (121, 220, 279, 276) | Giữ "rổ cổ phiếu chuyển sàn" ở Bảng 2 và chỉ tiêu (4) vì người đọc chưa gặp chữ CS. |
| Stationary bootstrap | bootstrap khối dừng | "bootstrap khối" (360) | Xem V29. |
| Bid-ask spread | chênh lệch mua-bán; chênh lệch mua-bán ước lượng (Corwin–Schultz); chênh lệch mua-bán yết giá đóng cửa | "chênh lệch giá chào mua và chào bán" (277); "chênh lệch yết giá đóng cửa" (236) | Xem V15. Ở idx 236 có thể giữ "chênh lệch yết giá đóng cửa" nếu thêm "mua-bán". |
| Winsorize | giới hạn tại phân vị … (winsorize) | "cắt đuôi" (233) | Xem m9. |
| Dummy variable | biến giả | "biến chỉ" (329, 334, 345) | "Biến chỉ" là dịch sát "indicator"; "biến giả" là thuật ngữ quen trong giáo trình kinh tế lượng. Nếu đổi thì đổi cả ba chỗ và chuỗi thay thế của m1. |
| Chỉ số chất lượng thị trường vốn (tên riêng) | Chỉ số chất lượng thị trường vốn (viết hoa chữ đầu) | "chỉ số chất lượng" (422); "Chỉ số chất lượng thị trường" trong Hình 1 (159, 182) | Hình 1 có thể giữ bản rút gọn vì ô hình hẹp. Xem V32. |
| Chỉ số khả năng đầu tư (tên riêng) | Chỉ số khả năng đầu tư (viết hoa chữ đầu) | viết thường ở 337, 428 | Thống nhất như Chỉ số chất lượng thị trường vốn. |
| Tên ghép hai người hoặc hai địa danh | gạch vừa trong văn bản: Corwin–Schultz, Bai–Perron, Black–Litterman, Moore–Penrose, Rambachan–Roth, Tokyo–Osaka | gạch nối: "Black-Litterman" (132, 244, 259, 262, 436, 523), "Bai-Perron" (523), "Moore-Penrose" (271); gạch vừa: "Corwin–Schultz" (225), "Tokyo–Osaka" (145, 347) | APA 7 dùng gạch vừa cho hai danh từ ngang hàng. Giữ nguyên gạch nối trong tên bài báo ở Bảng 6, Bảng 7 và danh mục tài liệu vì đó là tên gốc. |
| Đơn vị vận hành các thị trường còn lại | do HNX vận hành | "do HNX tổ chức" (98, 101); "HNX tổ chức thị trường" (349) | Giữ "tổ chức" khi diễn đạt lại văn bản pháp luật (idx 101, 349 dẫn Bộ Tài chính, 2023); ở idx 98, là định nghĩa của đề tài, dùng "vận hành" cho khớp idx 242, 325, 350, 526. |
| Tệp đăng ký trước kế hoạch phân tích | tệp đăng ký trước (lần đầu: tệp đăng ký trước kế hoạch phân tích, idx 118); sau đó "tệp đăng ký" | "tệp đăng ký" (14 lần), "tệp đăng ký trước" (6 lần) | Hai dạng đều chấp nhận được sau lần định nghĩa đầu; không cần sửa từng chỗ. |
| Mốc đo mức chịu cú sốc | bằng dữ liệu đến ngày 30/6/2025 | "đo trước ngày 30/6/2025" (332) | Xem m12. |
| Giai đoạn so sánh trước sự kiện | giai đoạn tham chiếu (6/2009–6/2025) là khái niệm dữ liệu; cửa sổ trước là phần của giai đoạn tham chiếu dùng trong ước lượng H3 (sau điểm gãy cuối cùng) | dùng đúng phân biệt ở 324, 326, 358; idx 358 gọi "cửa sổ trước dài 193 tháng (6/2009–6/2025)" | Đúng khi không có điểm gãy; có thể thêm "khi không có điểm gãy" ở idx 358 nếu muốn chặt. |

---

## (7) Nhận định theo skill

- **academic-paper-reviewer (re-review, 5 vai trong một ngữ cảnh, NOT_CALIBRATED).** Vòng 11 đã xử lý thực chất cả năm MAJOR của vòng 10 và ba MAJOR của Agent B. Devil's Advocate nêu phản biện mạnh nhất còn lại: phần mở rộng theo kênh dựa vào những nhóm đối chứng mà chính đề cương dự báo sẽ biến mất (MJ2), và quy tắc đo kết quả chính vẫn có một mép phụ thuộc sàn (MJ1). Cả hai sửa được bằng câu chữ, không đổi thiết kế. Không có DA-CRITICAL. Khuyến nghị: Minor Revision.
- **mhe-identification (Critic).** Câu hỏi: Y(1) − Y(0) của logarit Amihud cho cổ phiếu niêm yết HNX khi đổi sàn sang HOSE. Nguồn biến thiên: một ngày chuyển sàn do quy định, chung cho mọi mã, với nhóm đối chứng HOSE ghép cặp. Thiết kế 2×2 không so le nên TWFE không gặp lỗi Goodman-Bacon; suy luận trên chuỗi dₜ và bootstrap tự hồi quy là đúng cho trường hợp "một cụm xử lý theo thời gian". Phần dị biệt theo Eₛ,ᵢ là triple-difference: hợp lệ khi gradient theo Eₛ,ᵢ của nhóm đối chứng đo được trong cả hai giai đoạn, nên MJ2 là điều kiện cần. Phân tích trụ sở cần cùng cấu trúc (m1). Kết quả đo không được chịu ảnh hưởng của xử lý (MJ1).
- **aer-identification.** Gate: thiết kế DiD một ngày, không có cờ đỏ TWFE; có kiểm định đồng thời trước sự kiện và độ nhạy Rambachan–Roth; suy luận khớp thiết kế. Phần "cơ chế" theo mức chịu cú sốc đã được gắn nhãn là phân tích phụ và không đo riêng từng quy tắc, đúng tinh thần "Mechanism vs. Identification".
- **review-methodology.** Ngôn ngữ nhân quả nhìn chung đúng mức (H1 là "liên hệ có điều kiện", phần trụ sở là "ước lượng dị biệt"). Còn một chỗ nói quá ở idx 365 (m10).
- **liquidity-measures.** Ngưỡng chung, chỉ dùng giao dịch khớp lệnh, báo cáo tỷ lệ ngày bị loại và tháng thiếu: đạt. Ranh giới 7% của quy tắc loại ngày liền sau (MJ1), cách winsorize (m9), trọng số VN-Index (m3) và quan hệ giữa thước đo chỉ số với vòng quay (m7) là bốn chỗ còn sửa.
- **statistical-power.** MDE của δ khớp tính toán chính xác (0,643σ; 1,239σ; 1,760σ; tỷ số 1,33 khi cửa sổ trước còn 24 tháng). Lời khẳng định ở idx 357 rằng lực kiểm định của hệ số tương tác bị giới hạn bởi số tháng nhất quán với thủ tục suy luận ở idx 333. Còn thiếu mức ý nghĩa của hệ số tương tác (m5) và định nghĩa σ (m13).
- **review-pap (checklist 6 vai trong một ngữ cảnh).** Kết quả chính, họ Holm, quy tắc gọi kết quả chưa đủ cơ sở, chính sách lệch khỏi kế hoạch, phương án dự phòng: đều có. Đánh giá kiểu Agent 6: "Competitive, minor revisions needed". Hai chỗ chưa đủ chặt để đăng ký: phương án cho tương tác biên độ khi mất UPCoM (MJ2) và định nghĩa thống kê cho chuỗi hệ số tương tác (m5, m6).
- **scientific-writing.** Số liệu lặp lại khớp nhau giữa các mục (299 mã ở idx 106 và 344; 193, 18, 24 tháng; năm phương án dự phòng ở idx 363–364 và 433; 20 và 8 cửa sổ ở idx 121 và 286). Không thấy số liệu hay trích dẫn được thêm mà không có nguồn. Lệch mốc đo ở m12.
- **econ-write.** Phương trình (5) đã có lời dẫn và định nghĩa biến, nhưng định nghĩa αᵢ, τₜ bị đẩy về cuối một câu dài (V5). Phần mở rộng theo Eₛ,ᵢ nên có công thức riêng nếu còn chỗ. Đoạn Rambachan–Roth (V4) và đoạn kênh chỉ số (V2, V3) là hai chỗ người đọc dễ bỏ cuộc nhất.
- **vina-me.** `soat.mjs` trên bản tách đoạn: 130 đoạn, 321 câu, trung bình 40,1 chữ (âm tiết) mỗi câu, 2,5 câu mỗi đoạn; cảnh báo "đồng thời" (4), "không chỉ" (2), "CHIẾU" (nằm trong nhãn [CẦN ĐỐI CHIẾU], bỏ qua), 21 gạch vừa và 27 "&" (miễn trừ APA 7), một dấu "=" (trong "M = {M1, …, M7}", ký hiệu toán, bỏ qua), ba đoạn mở bằng "Câu hỏi" (danh sách câu hỏi nghiên cứu, bỏ qua). Lượt đọc người mới và lượt bắt văn máy cho ra các mục V1–V34; văn bản nhìn chung đã bỏ được khuôn văn mẫu, lỗi còn lại chủ yếu là câu quá tải ở mục 4.3.7.
- **vietnamese-human-writing (7 vòng, thể loại văn khoa học).** Vòng 1 (dữ kiện, logic): không thấy thông tin bịa; hai chỗ logic là m2 và V8. Vòng 2 (ngôn ngữ): không còn sáo ngữ mức R09. Vòng 3 (cấu trúc): đoạn 330, 334 hơn một ý. Vòng 4 (nhịp): đo trên 287 câu văn xuôi (idx 94–372, bỏ bảng), tách câu theo dấu chấm, đơn vị là âm tiết cách nhau bằng dấu cách: CV 0,72 (đạt ngưỡng ≥ 0,50), câu ≤ 10 âm tiết 8,4% (đạt ≥ 8%), câu ≥ 41 âm tiết 38% (vượt ngưỡng 15%). Ngưỡng R31 viết cho "từ", còn phép đo dùng âm tiết, nên con số 38% phóng đại; dù vậy các câu dài nhất (88–92 âm tiết ở idx 104, 105, 224, 346) là thật và đã có cách tách. Vòng 5 (từ vựng): bảng thuật ngữ ở mục 6. Vòng 6 (hình thức): dấu gạch vừa và "&" theo miễn trừ APA 7. Vòng 7 (đọc toàn văn): mạch từ 4.1 đến 4.5 liền; chỗ gãy là 4.3.7 dồn bốn ý lớn (phương trình, suy luận, mở rộng theo kênh, trụ sở) vào chín đoạn dài.
- **sciwrite.** Pass 1 (rườm rà): ít; Pass 2 (chủ động): đề cương dùng "đề tài" làm chủ thể nhất quán; Pass 3 (kiến trúc câu): vị ngữ bị chôn ở V4, V5, V6; Pass 4 (thuật ngữ): mục 6, nghiêm trọng nhất là "giả thuyết không" (V1) vì đọc sai nghĩa; Pass 5 (số và trích dẫn): khớp.
