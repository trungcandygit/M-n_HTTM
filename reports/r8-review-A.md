# Phản biện vòng 8, Agent A (phương pháp và cách viết)

Đề cương: "Hợp nhất sàn chứng khoán và chất lượng thị trường: Bằng chứng thực nghiệm từ HNX và vị thế tài chính Hà Nội" (bản v7). Người phản biện: Claude, Agent A. Ngày: 16/10/2026. Báo cáo chỉ đọc đề cương; tôi không sửa đề cương.

---

## (1) Bằng chứng tuân thủ

**File đã đọc (chỉ đọc):**
- `scratchpad/r8/dump-v7.txt`: đọc toàn văn, idx 0–525.
- `outputs/round-7/de-cuong-v7-round-7.docx`: dùng `zipfile` của Python để đọc `word/document.xml` và trích 7 công thức OMML. Dạng chữ của các công thức:
  (1) `MQIk,t = Σ_{j=1}^{J} wj zj,k,t`;
  (2) `Um,b,t = μm,b,t − (ρ/2)σ²m,b,t`;
  (3) `Gm,t = Um,H,t − Um,CS,t`;
  (4) `Gt = (1/M) Σ_{m∈M} Gm,t`;
  (5) `Ai,t = αi + τt + δ·Di·Postt + εi,t`;
  (6) `Ai,t = αi + τt + Σ_{k≠k0} δk·Di·1[t=k] + εi,t`;
  (7) `Zi,t = γi + θt + β·SMDc(i),y(t)−1 + λ′Wc(i),y(t)−1 + ui,t`.
- `reports/r7-review.md`: đọc toàn bộ để đối chiếu các lỗi đã sửa (xem cuối mục 5).
- `ho-so/TONG_HOP_TAI_LIEU_HNX_HOSE.txt` và `ho-so/tai-lieu-gop.txt`: chỉ grep để tìm độ lớn tác động thanh khoản trong Hisada (2018) và Amihud và cộng sự (1997), dùng làm mốc so với MDE. Không tìm được hệ số log Amihud nào dùng trực tiếp được, nên tôi không đưa con số nào từ hai nguồn này vào báo cáo.

**Thứ tự gọi skill (bằng Skill tool, tuần tự):**
1. academic-paper-reviewer (yêu cầu chế độ methodology-focus, chạy trong một ngữ cảnh);
2. mhe-identification (Critic);
3. aer-identification;
4. review-methodology;
5. liquidity-measures;
6. statistical-power;
7. econ-write;
8. scientific-critical-thinking.

**Lỗi và cách xử lý:**
- academic-paper-reviewer: chế độ methodology-focus đòi orchestration hai lượt (Phase 1 không thấy bài, Phase 2 thấy bài) theo sprint contract `shared/contracts/reviewer/methodology_focus.json`, và đòi agent con. Lỗi nguyên văn khi tìm file contract: `ls: cannot access '/home/user/M-n_HTTM/.claude/skills/academic-paper-reviewer/shared/contracts/reviewer/': No such file or directory`. Phiên này cũng không có công cụ Agent. Vì vậy tôi tự đóng năm vai trò của panel (Journal-Fit, Methodology, Domain, Perspective, Devil's Advocate) trong cùng một ngữ cảnh. Năm vai này **không độc lập**, không có cam kết trước khi thấy bài, và cũng không phải đánh giá đã hiệu chuẩn (NOT_CALIBRATED). Tôi không chạy `check_acronyms.py` hay bất kỳ script nào của skill.
- statistical-power: không dùng `scripts/power.py` hay `simulate_power.py` của skill. Tôi tự viết script mô phỏng cục bộ tại `/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r8/mde_h3.py`, cùng `size_check.py` và `param_test.py` trong cùng thư mục. Script dùng NumPy; môi trường không có SciPy nên tôi thay bằng `statistics.NormalDist`. Script không dùng dữ liệu thật.
- mhe-identification: thư mục `references/sources/` không được cài (ghi chú đầu skill), nên tôi không dẫn trang nào của sách MHE.
- Tôi không tra web và không gửi câu chữ của đề cương ra ngoài.

---

## (2) Tổng hợp

**2 CRITICAL, 3 MAJOR, 11 MINOR.**

Phần lớn lỗi vòng 7 đã được sửa đúng (xem mục 5, phần đối chiếu). Hai lỗi CRITICAL mới đều nằm ở H3, giả thuyết xác nhận chính:
- **CR1.** Cách loại ngày chạm biên độ chưa loại được độ chệch cơ học do biên độ hẹp lại. Độ chệch này cùng chiều với giả thuyết.
- **CR2.** Kiểm định hoán vị theo ngày giả, trong cấu trúc cửa sổ của đề cương, có sai lầm loại I cao gấp khoảng 4–6 lần mức danh nghĩa ở ngưỡng Holm (theo mô phỏng dưới giả định AR(1)).

Ghi chú về ký hiệu: dump mã hóa ký tự "&" thành `&amp;`. Trong CHUỖI GỐC tôi chép đúng như dump; trong Word ký tự này là "&". Trong CHUỖI THAY THẾ tôi viết "&".

---

## (3) Phát hiện theo mức

### CRITICAL

**CR1. Loại ngày chạm biên độ không loại được độ chệch do biên độ hẹp lại. Độ chệch này cùng chiều với H3.**
- *idx:* 186, 179, 180, 270.
- *Skill phát hiện:* liquidity-measures (mục 4.1–4.2), mhe-identification (chọn mẫu theo biến kết quả).
- *Lý do:*
  - Trước sự kiện, cổ phiếu chuyển sàn chịu biên độ ±10%; sau sự kiện, ±7%. Nhóm đối chứng HOSE chịu ±7% ở cả hai giai đoạn.
  - Sau khi chuyển sàn, mọi ngày có |r| từ khoảng 7% đến 10% đều trở thành ngày chạm biên độ và bị loại. Các ngày còn lại vì vậy có |r| nhỏ hơn một cách cơ học, nên Amihud = |r|/DVOL giảm, kể cả khi thanh khoản thật không đổi.
  - Trước sự kiện, các ngày như vậy được giữ lại. Đây là chọn mẫu theo chính biến kết quả, và chỉ xảy ra ở nhóm xử lý. Độ chệch kéo δ về phía âm, đúng chiều H3 dự đoán.
  - Thêm vào đó, mã nhỏ ở HNX hay chạm biên độ. Sau khi loại ngày, một số tháng của các mã này còn quá ít ngày hợp lệ, và tỷ lệ tháng thiếu khác nhau giữa trước và sau sự kiện.
  - Cách sửa chuẩn: dùng một ngưỡng |r| chung thấp hơn biên độ hẹp nhất, áp cho cả hai nhóm và cả hai giai đoạn.
- *Sửa:*
  - idx 186. CHUỖI GỐC: `đề tài vì vậy tính Amihud sau khi loại các ngày chạm biên độ và ngày liền sau mỗi ngày đó, và dùng vòng quay làm thước đo đối chiếu.`
    CHUỖI THAY THẾ: `Loại các ngày chạm biên độ chưa đủ, vì sau khi chuyển sàn mọi ngày có lợi suất tuyệt đối từ khoảng 7% đến 10% trở thành ngày chạm biên độ và bị loại, nên các ngày còn lại có lợi suất tuyệt đối nhỏ hơn một cách cơ học. Đề tài vì vậy tính Amihud, ở cả hai nhóm và cả hai giai đoạn, chỉ trên các ngày có lợi suất tuyệt đối dưới một ngưỡng chung thấp hơn biên độ ±7% (giá trị cụ thể ghi trong tệp đăng ký) và không liền sau một ngày chạm biên độ; giá trị giao dịch chỉ gồm giao dịch khớp lệnh; tháng có ít hơn một số ngày hợp lệ tối thiểu, ghi trong tệp đăng ký, được ghi là thiếu; tỷ lệ ngày bị loại và tỷ lệ tháng thiếu được báo cáo theo nhóm và giai đoạn. Vòng quay, không chịu ảnh hưởng của biên độ theo cách này, là thước đo đối chiếu.`
  - idx 179. CHUỖI GỐC: `độ phi thanh khoản Amihud của các cổ phiếu chuyển sàn, tính sau khi loại ngày chạm biên độ và ngày liền sau, giảm so với nhóm đối chứng`
    CHUỖI THAY THẾ: `độ phi thanh khoản Amihud của các cổ phiếu chuyển sàn, tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày chạm biên độ, giảm so với nhóm đối chứng`
  - idx 180. CHUỖI GỐC: `Logarit độ phi thanh khoản Amihud loại ngày chạm biên độ và ngày liền sau (chính)`
    CHUỖI THAY THẾ: `Logarit độ phi thanh khoản Amihud trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung, loại ngày liền sau ngày chạm biên độ (chính)`
  - idx 270. CHUỖI GỐC: `trong đó Ai,t là logarit của độ phi thanh khoản Amihud tính sau khi loại các ngày chạm biên độ và ngày liền sau mỗi ngày đó;`
    CHUỖI THAY THẾ: `trong đó Ai,t là logarit của độ phi thanh khoản Amihud tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung (thấp hơn biên độ ±7%) và không liền sau một ngày chạm biên độ;` (chữ i,t viết chỉ số dưới như bản Word).

**CR2. Kiểm định hoán vị theo ngày giả, với cấu trúc cửa sổ của đề cương, có sai lầm loại I vượt xa mức danh nghĩa. Ngoài ra, thống kê kiểm định của H3 chưa được định nghĩa.**
- *idx:* 270, 224, 286.
- *Skill phát hiện:* statistical-power (mô phỏng), mhe-identification (suy luận cũng là một phần của nhận dạng), aer-identification (suy luận phải khớp với thiết kế).
- *Lý do:*
  - Chỉ có một lần xử lý, nên mọi suy luận dựa trên một chuỗi chênh lệch d_t. Thời kỳ tham chiếu dài 193 tháng (6/2009–6/2025). Với cửa sổ giả gồm 18 tháng loại trừ và 24 tháng sau, có 128 ngày giả nếu trượt theo tháng, nhưng chỉ khoảng 6 cửa sổ không chồng lấn.
  - Mô phỏng 3.000 lần dưới H0, với d_t theo AR(1), cho tỷ lệ bác bỏ thực tế sau. Ở mức danh nghĩa 0,0167 (ngưỡng Holm chặt nhất): 0,065 (φ = 0), 0,066 (φ = 0,3), 0,078 (φ = 0,6), 0,093 (φ = 0,8). Ở mức 0,05: 0,10–0,11. Kết quả gần như không đổi khi giai đoạn trước chỉ dài 24 tháng.
  - Nguyên nhân: 128 thống kê giả phụ thuộc mạnh vào nhau, nên phần đuôi của phân phối giả được ước lượng từ rất ít thông tin độc lập. Nếu dùng cửa sổ không chồng lấn thì có khoảng 6 ngày giả, và giá trị p nhỏ nhất đạt được là 1/7 ≈ 0,14, không bao giờ qua ngưỡng Holm.
  - Ngoài ra, Conley và Taber (2011) xây phân phối từ phần dư của **nhiều nhóm đối chứng**. Ở đây chỉ có một chuỗi chênh lệch, nên trích Conley và Taber cho phép hoán vị theo ngày chỉ đúng về tinh thần, chưa đúng về thủ tục.
  - Một kiểm định tham số trên d_t (ước lượng AR từ giai đoạn tham chiếu) cho kích thước 0,024–0,035 ở mức danh nghĩa 0,0167. Kết quả này gần mức danh nghĩa hơn nhiều, và còn có thể cải thiện bằng bootstrap tự hồi quy có hiệu chỉnh độ chệch của hệ số.
  - Phương trình (5) trên bảng không cân bằng và hiệu số trung bình của chuỗi d_t không cho cùng một con số, nên cần định nghĩa đúng một thống kê.
- *Sửa (giữ suy luận hoán vị trong thiết kế, chỉ đổi vai trò của nó):*
  - idx 270. CHUỖI GỐC: `đề tài dùng sai số chuẩn chịu được tự tương quan trên chuỗi này và suy luận hoán vị trên các ngày giả định trong giai đoạn tham chiếu (Conley &amp; Taber, 2011).`
    CHUỖI THAY THẾ: `gọi dt là chênh lệch trung bình logarit Amihud giữa các cổ phiếu chuyển sàn và cổ phiếu đối chứng ghép cặp trong tháng t, mỗi cặp có dữ liệu trong tháng có trọng số bằng nhau, thì thống kê kiểm định là trung bình của dt trong giai đoạn sau sự kiện trừ trung bình của dt trong cửa sổ trước. Giá trị p chính được tính bằng bootstrap tự hồi quy trên chuỗi dt: mô hình tự hồi quy ước lượng từ giai đoạn tham chiếu, bậc trễ chọn theo tiêu chí thông tin, hệ số được hiệu chỉnh độ chệch, và kích thước của kiểm định được kiểm tra bằng mô phỏng trước ngày đăng ký. Suy luận trên các ngày giả định trong giai đoạn tham chiếu, với cùng cấu trúc cửa sổ trước, 18 tháng loại trừ và 24 tháng sau, theo tinh thần của Conley và Taber (2011), được báo cáo như kiểm tra bổ sung, vì các cửa sổ giả chồng lấn nhau và chỉ tạo ra khoảng sáu cửa sổ độc lập.`
  - idx 270. CHUỖI GỐC: `H3 được ủng hộ khi δ âm và giá trị p hoán vị nhỏ hơn ngưỡng Holm tương ứng.`
    CHUỖI THAY THẾ: `H3 được ủng hộ khi δ âm và giá trị p bootstrap tự hồi quy nhỏ hơn ngưỡng Holm tương ứng; giá trị p hoán vị được báo cáo kèm.`
  - idx 286. CHUỖI GỐC: `giá trị p bootstrap khối cho H2 và giá trị p hoán vị cho H3.`
    CHUỖI THAY THẾ: `giá trị p bootstrap khối cho H2 và giá trị p bootstrap tự hồi quy cho H3.`
  - idx 224. CHUỖI GỐC: `tập ngày giả định cho suy luận hoán vị;`
    CHUỖI THAY THẾ: `bậc trễ, cách hiệu chỉnh độ chệch và số lần lặp của bootstrap tự hồi quy cho H3, kết quả mô phỏng kích thước của kiểm định, tập ngày giả định cho suy luận hoán vị;`
  - Bảng 2 (idx 181) có thể giữ Conley và Taber (2011). Nếu muốn dẫn nguồn cho bootstrap tự hồi quy hoặc kiểm định bất ổn cuối mẫu, xem mục 6 [CẦN XÁC MINH].

### MAJOR

**MJ1. Cửa sổ trước của δ dài 16 năm, nhưng đề cương chưa xử lý xu hướng hay điểm gãy trong chuỗi chênh lệch.**
- *idx:* 270.
- *Skill phát hiện:* mhe-identification (xu hướng song song trong giai đoạn dài), aer-identification.
- *Lý do:*
  - Theo phương trình (5), δ so sánh 24 tháng sau sự kiện với trung bình của 193 tháng trước. Nếu khoảng cách thanh khoản giữa HNX và HOSE trôi dần hoặc gãy trong giai đoạn 2009–2025, trung bình dài hạn là một phản thực kém, và δ chứa cả độ trôi đó.
  - Chính thí sinh có bản thảo về điểm gãy của thanh khoản theo Bai–Perron (Bảng 7, số 5), nên kiểm tra này nằm trong tầm tay.
  - Cửa sổ trước ngắn hơn làm giảm độ chệch nhưng làm MDE tăng khoảng 1,3 lần (mục 4). Đây là một đánh đổi cần cố định trước, trong tệp đăng ký.
- *Sửa:* idx 270. THÊM SAU chuỗi: `chỉ được ước lượng trong phương trình (6);`
  CHUỖI THÊM: ` vì giai đoạn tham chiếu dài 16 năm, đề tài kiểm định điểm gãy cấu trúc của chuỗi chênh lệch theo tháng trong giai đoạn này (Bai & Perron, 1998); cửa sổ trước của ước lượng chính bắt đầu sau điểm gãy cuối cùng được phát hiện theo quy tắc ghi trong tệp đăng ký, và ước lượng với cửa sổ trước 24 tháng (7/2023–6/2025) được báo cáo kèm;`

**MJ2. Bước giá khác nhau giữa các sàn, nhưng đề cương chưa xử lý. Bước giá làm méo tỷ lệ ngày lợi suất bằng 0 và Corwin–Schultz ở H2 và ở thước đo phụ của H3.**
- *idx:* 186.
- *Skill phát hiện:* liquidity-measures (mục 4.3).
- *Lý do:*
  - Với cổ phiếu giá thấp, bước giá chiếm tỷ lệ lớn của giá. Tỷ lệ ngày lợi suất bằng 0 và chênh lệch high-low khi đó phản ánh bước giá nhiều hơn chi phí giao dịch.
  - Bước giá của HNX và HOSE khác nhau [CẦN XÁC MINH quy định theo từng thời kỳ]. Vì vậy so sánh H2 và thay đổi của tỷ lệ ngày lợi suất bằng 0 trong H3 (thước đo phụ) gộp cả hiệu ứng bước giá. Đề cương mới xử lý biên độ.
- *Sửa:* idx 186. THÊM SAU chuỗi: `nên chỉ số được so sánh cả trên mẫu đối sánh theo quy mô và ngành và cả khi bỏ hai chỉ báo nhạy với biên độ.`
  CHUỖI THÊM: ` Bước giá cũng khác nhau giữa các sàn [CẦN XÁC MINH quy định bước giá theo từng thời kỳ], nên tỷ lệ ngày lợi suất bằng 0 và chênh lệch Corwin–Schultz phản ánh một phần bước giá thay vì chi phí giao dịch, nhất là ở cổ phiếu giá thấp; đề tài báo cáo hai chỉ báo này theo nhóm mức giá, và đọc thay đổi của tỷ lệ ngày lợi suất bằng 0 trong H3 cùng với thay đổi bước giá khi chuyển sàn.`

**MJ3. Đề cương chưa có hiệu ứng nhỏ nhất phát hiện được (MDE) ước tính trước cho H3, và mô tả nguồn quyết định công suất chưa đúng.**
- *idx:* 286.
- *Skill phát hiện:* statistical-power, scientific-critical-thinking ("không bác bỏ" khác "không có tác động").
- *Lý do:*
  - Công suất phụ thuộc vào phương sai và mức tự tương quan của **chuỗi chênh lệch**, không phải của "cú sốc chung". Phần cú sốc chung mà nhóm đối chứng cũng chịu đã bị trừ đi khi lấy hiệu.
  - Hội đồng và phản biện tạp chí sẽ hỏi H3 phát hiện được tác động cỡ nào. Bảng ở mục 4 cho thấy MDE có thể khoảng 20–40% Amihud khi chuỗi tự tương quan cao. Nếu chưa nói trước điều này, một kết quả không bác bỏ dễ bị đọc thành "không có tác động".
- *Sửa:*
  - idx 286. CHUỖI GỐC: `Công suất của H3 phụ thuộc vào số tháng trước và sau sự kiện và vào độ lớn của cú sốc chung theo tháng, không phụ thuộc vào số cổ phiếu, vì mọi cổ phiếu chuyển sàn cùng một ngày.`
    CHUỖI THAY THẾ: `Công suất của H3 phụ thuộc vào số tháng trước và sau sự kiện và vào phương sai và mức tự tương quan của chuỗi chênh lệch theo tháng; công suất chỉ phụ thuộc yếu vào số cổ phiếu, vì mọi cổ phiếu chuyển sàn cùng một ngày và phần nhiễu riêng của từng mã đã được bình quân trong chuỗi chênh lệch.`
  - idx 286. CHUỖI GỐC: `Thí sinh tính hiệu ứng nhỏ nhất phát hiện được trên chuỗi chênh lệch của giai đoạn 2009–2025 và ghi vào tệp đăng ký.`
    CHUỖI THAY THẾ: đoạn đề xuất ở mục 4 (câu đề xuất A).
  - idx 286. CHUỖI GỐC: `Nếu dữ liệu không ủng hộ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu bằng kích thước hiệu ứng và khoảng tin cậy.`
    CHUỖI THAY THẾ: `Nếu dữ liệu không ủng hộ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu bằng kích thước hiệu ứng và khoảng tin cậy; khi khoảng tin cậy chứa cả 0 lẫn những tác động lớn hơn hiệu ứng nhỏ nhất phát hiện được, kết quả được gọi là chưa đủ cơ sở kết luận, không phải bằng chứng về việc không có tác động.`

### MINOR

**m1. Câu khung lý thuyết ngầm một quan hệ nhân quả mà đề tài không kiểm định.** idx 117. Skill: scientific-critical-thinking.
CHUỖI GỐC: `và cấu trúc sàn định hình vai trò của mỗi trung tâm.`
CHUỖI THAY THẾ: `và cấu trúc sàn liên hệ với vai trò của mỗi trung tâm; đề tài không kiểm định quan hệ nhân quả ở mắt xích cuối này.`

**m2. Câu về bảy mô hình nói quá: lấy bình quân không "tách" được sai số ước lượng khỏi tác động của sàn.** idx 196. Skill: scientific-critical-thinking, econ-write.
CHUỖI GỐC: `bình quân theo bảy mô hình và độ phân tán giữa chúng tách hai nguồn này.`
CHUỖI THAY THẾ: `bình quân theo bảy mô hình làm kết luận ít phụ thuộc vào một mô hình, còn độ phân tán giữa các mô hình cho biết mức phụ thuộc đó.`

**m3. Ký hiệu trong công thức (4).** Skill: econ-write. OMML hiện là `1/M`, trong khi M là một tập (idx 227). Sửa OMML: đổi mẫu số `M` thành `|M|` (hoặc thay hẳn phân số bằng `1/7`). Không đổi chữ trong đoạn.

**m4. Phương trình (6) chưa có biến gộp các tháng trước 1/2024, và phép thử Rambachan–Roth chưa nói dùng tháng nào làm "trước sự kiện".** idx 272 và OMML (6). Skill: aer-identification.
- *Sửa OMML (6):* đổi chỉ số tổng thành `k ∈ {1/2024, …, 12/2028}, k ≠ k0`, và thêm số hạng `+ δpre·Di·1[t < 1/2024]` trước `εi,t`.
- *Sửa chữ:* CHUỖI GỐC: `Đề tài báo cáo độ nhạy của kết luận khi xu hướng song song bị vi phạm ở mức tương đương độ lệch lớn nhất trước sự kiện (Rambachan &amp; Roth, 2023).`
  CHUỖI THAY THẾ: `Đề tài kiểm định đồng thời các hệ số δk từ tháng 1/2024 đến tháng 5/2025 bằng 0, và báo cáo độ nhạy của kết luận khi xu hướng song song bị vi phạm ở mức tương đương độ lệch lớn nhất của các hệ số này, tức các tháng trước giai đoạn chuyển tiếp (Rambachan & Roth, 2023).`

**m5. Mẫu xử lý của H3 chưa rõ: toàn bộ mã chuyển sàn hay chỉ rổ CS 30 mã.** idx 270. Skill: review-methodology.
CHUỖI GỐC: `Di bằng 1 nếu cổ phiếu chuyển sàn;`
CHUỖI THAY THẾ: `Di bằng 1 nếu cổ phiếu chuyển sàn, tức mọi cổ phiếu niêm yết tại HNX được chuyển sang HOSE ngày 28/12/2026, không chỉ 30 mã của rổ CS;`

**m6. Lý do chọn Amihud và tỷ lệ ngày lợi suất bằng 0 dựa vào một nhận định chưa đối chiếu với bảng kết quả của Fong và cộng sự (2017).** idx 191. Skill: liquidity-measures (mục 3).
CHUỖI GỐC: `Amihud và tỷ lệ ngày lợi suất bằng 0 là chỉ báo chính vì hai thước đo này phản ánh tốt chi phí giao dịch trong một quốc gia ở thị trường mới nổi (Lesmond, 2005; Bekaert và cộng sự, 2007; Fong và cộng sự, 2017).`
CHUỖI THAY THẾ: `Amihud và tỷ lệ ngày lợi suất bằng 0 là chỉ báo chính vì hai thước đo này đã được dùng và so sánh với chuẩn dữ liệu trong ngày ở nhiều thị trường mới nổi (Lesmond, 2005; Bekaert và cộng sự, 2007; Fong và cộng sự, 2017) [CẦN ĐỐI CHIẾU bảng kết quả của Fong và cộng sự (2017)]; nếu có giá chào mua và chào bán đóng cửa cho một phần mẫu, đề tài báo cáo tương quan giữa các chỉ báo ngày và chênh lệch yết giá đóng cửa trên phần mẫu đó.`

**m7. Amihud danh nghĩa làm chỉ số MQI cập nhật sau năm 2025 tăng một cách cơ học.** idx 191. Skill: liquidity-measures (mục 4.6). Điểm z được cố định theo giai đoạn tham chiếu, trong khi giá trị giao dịch danh nghĩa tăng theo thời gian, nên Amihud giảm và MQI tăng dù chất lượng thị trường không đổi.
THÊM SAU chuỗi: `Các chỉ báo cổ phiếu được gộp lên cấp sàn bằng trung vị có trọng số theo vốn hóa.`
CHUỖI THÊM: ` Trước khi chuẩn hóa, độ phi thanh khoản Amihud được nhân với tỷ số giữa tổng vốn hóa của ba sàn trong tháng t và tổng vốn hóa tại tháng 6/2025, để chỉ số không tăng chỉ vì quy mô danh nghĩa của thị trường tăng.`

**m8. Ở H1, điểm z theo kỳ đổi khi tập trung tâm đổi.** idx 286. Skill: mhe-identification. Khi một trung tâm mới vào chỉ số, điểm z của các trung tâm cũ thay đổi theo, và hiệu ứng cố định không khử được thay đổi này.
CHUỖI GỐC: `Ở H1, đề tài kiểm tra độ bền trên mẫu các trung tâm có ít nhất năm kỳ,`
CHUỖI THAY THẾ: `Ở H1, đề tài kiểm tra độ bền trên mẫu các trung tâm có ít nhất năm kỳ và trên mẫu cân bằng gồm các trung tâm có mặt ở mọi kỳ được dùng, vì điểm z theo kỳ thay đổi khi tập trung tâm thay đổi,`

**m9. H4: rổ H ghép có hoàn lại, và cửa sổ ước lượng sau sự kiện chứa dữ liệu trước sự kiện.** idx 233, 234. Skill: review-methodology. Với cửa sổ 104 tuần, mọi cửa sổ đánh giá từ quý 1/2027 đến quý 4/2028 đều ước lượng trọng số một phần trên dữ liệu trước ngày 28/12/2026. M1 (1/N) không cần ước lượng nên cho phép so sánh sạch nhất.
- idx 233. CHUỖI GỐC: `ghép có hoàn lại với ngưỡng khoảng cách ghi trong tệp đăng ký.`
  CHUỖI THAY THẾ: `ghép có hoàn lại với ngưỡng khoảng cách ghi trong tệp đăng ký; mã HOSE được ghép nhiều lần nhận trọng số theo số lần ghép, và số mã khác nhau của rổ H được báo cáo.`
- idx 234. THÊM SAU chuỗi: `giai đoạn sau sự kiện dùng các cửa sổ từ quý 1/2027 đến quý 4/2028, tức 8 cửa sổ.`
  CHUỖI THÊM: ` Cửa sổ ước lượng của mọi cửa sổ đánh giá sau sự kiện đều chứa một phần dữ liệu trước ngày chuyển sàn, nên khoảng cách của các mô hình cần ước lượng gộp cả chất lượng thị trường mới lẫn tham số ước lượng trên dữ liệu cũ; khoảng cách của M1, không cần ước lượng, được báo cáo riêng như phép so sánh sạch nhất.`

**m10. Câu về Bắc Kinh dồn ba ý vào một chuỗi "dù … và … nên", khiến quan hệ lô-gic giữa các ý không rõ.** idx 80. Skill: econ-write.
CHUỖI GỐC: `Cặp Hà Nội và Thành phố Hồ Chí Minh có thể so sánh với cặp Bắc Kinh và Thượng Hải, dù Bắc Kinh từng là trung tâm tài chính lớn khi chưa có sở giao dịch chứng khoán (Naeem, 2023) và chỉ có sở giao dịch tầm quốc gia từ năm 2021 [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh], nên câu hỏi chuyên môn hóa (Yao, 2012) đặt ra cho Hà Nội sau đợt hợp nhất.`
CHUỖI THAY THẾ: `Cặp Hà Nội và Thành phố Hồ Chí Minh có thể so sánh với cặp Bắc Kinh và Thượng Hải. Bắc Kinh từng là trung tâm tài chính lớn khi chưa có sở giao dịch chứng khoán (Naeem, 2023) và chỉ có sở giao dịch tầm quốc gia từ năm 2021 [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh]. Trường hợp này cho thấy một thành phố có thể giữ vai trò trung tâm tài chính mà không cần sàn cổ phiếu, và đặt ra cho Hà Nội câu hỏi chuyên môn hóa (Yao, 2012) sau đợt hợp nhất.`

**m11. Câu thiếu chủ ngữ rõ, đọc như dịch.** idx 89. Skill: econ-write.
CHUỖI GỐC: `Các chỉ số và tệp đăng ký trước có được bất kể kết quả kiểm định.`
CHUỖI THAY THẾ: `Hai chỉ số và tệp đăng ký trước là sản phẩm có được dù kết quả kiểm định ra sao.`

---

## (4) Bảng MDE cho H3 và câu đề xuất

**Thiết lập.**
- d_t là chênh lệch theo tháng giữa trung bình log Amihud của nhóm chuyển sàn và trung bình log Amihud của nhóm đối chứng HOSE.
- Thống kê: δ̂ = trung bình d_t trong 24 tháng sau (1/2027–12/2028) trừ trung bình d_t trong 193 tháng trước (6/2009–6/2025). 18 tháng chuyển tiếp (7/2025–12/2026) bị loại.

**Giả định (đều là giả định, không phải số liệu thật):**
- Sau khi bỏ trung bình, d_t dừng và theo AR(1) với hệ số φ.
- σ là độ lệch chuẩn biên của d_t, đơn vị log điểm.
- Tôi dùng ký hiệu φ để tránh trùng với ρ, hệ số ngại rủi ro ở công thức (2).
- Công suất 80%. Kiểm định một phía (δ < 0), vì H3 có hướng.
- α = 0,05/3 ≈ 0,0167 là ngưỡng Holm chặt nhất khi H3 đứng đầu thứ tự; α = 0,05 là ngưỡng Holm lỏng nhất.
- Phương sai của δ̂ được tính đúng từ ma trận hiệp phương sai của AR(1). Mô phỏng (3.000 lần, kiểm định AR ước lượng từ giai đoạn tham chiếu) cho MDE lệch dưới 3% so với công thức.

**Bảng 1. MDE của δ, tính bằng log điểm (trong ngoặc: mức giảm Amihud tương ứng, 1 − e^(−MDE)).**

| σ (giả định) | φ (giả định) | SE(δ̂) | MDE, α = 0,0167 | MDE, α = 0,05 | MDE, α = 0,0167, cửa sổ trước 24 tháng |
|---|---|---|---|---|---|
| 0,10 | 0,0 | 0,022 | 0,064 (6%) | 0,054 | 0,086 (8%) |
| 0,10 | 0,3 | 0,029 | 0,087 (8%) | 0,072 | 0,115 (11%) |
| 0,10 | 0,6 | 0,042 | 0,124 (12%) | 0,104 | 0,165 (15%) |
| 0,10 | 0,8 | 0,059 | 0,176 (16%) | 0,147 | 0,232 (21%) |
| 0,20 | 0,0 | 0,043 | 0,129 (12%) | 0,108 | 0,171 (16%) |
| 0,20 | 0,3 | 0,058 | 0,173 (16%) | 0,145 | 0,230 (21%) |
| 0,20 | 0,6 | 0,083 | 0,248 (22%) | 0,208 | 0,329 (28%) |
| 0,20 | 0,8 | 0,119 | 0,352 (30%) | 0,295 | 0,464 (37%) |
| 0,30 | 0,0 | 0,065 | 0,193 (18%) | 0,161 | 0,257 (23%) |
| 0,30 | 0,3 | 0,087 | 0,260 (23%) | 0,217 | 0,346 (29%) |
| 0,30 | 0,6 | 0,125 | 0,372 (31%) | 0,311 | 0,494 (39%) |
| 0,30 | 0,8 | 0,178 | 0,528 (41%) | 0,442 | 0,696 (50%) |

Viết gọn theo bội số của σ, ở α = 0,0167: MDE ≈ 0,64σ (φ = 0), 0,87σ (φ = 0,3), 1,24σ (φ = 0,6), 1,76σ (φ = 0,8).

**Bảng 2. Kích thước thực tế của kiểm định hoán vị theo ngày giả (căn cứ của CR2).**
- Thiết lập: 128 ngày giả trượt theo tháng; mỗi ngày giả có 18 tháng loại trừ và 24 tháng sau; 3.000 lần mô phỏng dưới H0.

| φ | Tỷ lệ bác bỏ thực tế ở α danh nghĩa 0,0167 | ở α danh nghĩa 0,05 | Kiểm định AR tham số, ở α danh nghĩa 0,0167 |
|---|---|---|---|
| 0,0 | 0,065 | 0,099 | 0,024 |
| 0,3 | 0,066 | 0,098 | 0,025 |
| 0,6 | 0,078 | 0,100 | 0,029 |
| 0,8 | 0,093 | 0,112 | 0,035 |

**Cách đọc.**
- Cửa sổ trước dài giúp ít, vì phương sai của δ̂ chủ yếu đến từ trung bình 24 tháng sau sự kiện. Khi φ cao, 24 tháng sau chỉ tương đương vài quan sát độc lập.
- Cửa sổ trước 24 tháng (phương án của MJ1) làm MDE tăng khoảng 1,3 lần nhưng ít bị độ trôi dài hạn chi phối.
- Tôi không tìm được trong hồ sơ một độ lớn tác động lên log Amihud để so với MDE. Hisada (2018), Bảng 3, báo cáo hệ số ILLIQ nhưng bản OCR không đọc được giá trị [CẦN XÁC MINH].

**Câu đề xuất A** (thay chuỗi `Thí sinh tính hiệu ứng nhỏ nhất phát hiện được trên chuỗi chênh lệch của giai đoạn 2009–2025 và ghi vào tệp đăng ký.` ở idx 286):

> Với giả định chuỗi chênh lệch theo tháng là một quá trình tự hồi quy bậc một có hệ số φ và độ lệch chuẩn σ, giai đoạn trước dài 193 tháng (6/2009–6/2025), 18 tháng chuyển tiếp bị loại và giai đoạn sau dài 24 tháng, hiệu ứng nhỏ nhất phát hiện được của δ ở công suất 80% và mức ý nghĩa một phía 0,05/3 xấp xỉ 0,64σ khi φ = 0, 1,24σ khi φ = 0,6 và 1,76σ khi φ = 0,8. Chẳng hạn, với σ = 0,2 và φ = 0,6, đề tài chỉ phát hiện được mức giảm logarit Amihud từ khoảng 0,25 trở lên, tương đương độ phi thanh khoản giảm khoảng 22%. Các giá trị σ và φ này là giả định minh họa; thí sinh ước lượng hai tham số từ chuỗi chênh lệch của giai đoạn tham chiếu, tính lại hiệu ứng nhỏ nhất phát hiện được bằng mô phỏng theo đúng thủ tục kiểm định của H3, và ghi kết quả vào tệp đăng ký trước ngày 28/12/2026.

**Câu đề xuất B** (tùy chọn, đưa vào phụ lục hoặc tệp đăng ký): Bảng 1 ở trên, ghi chú rõ "σ và φ là giả định".

---

## (5) Nhận định ngắn theo từng skill

**academic-paper-reviewer.** Tôi đóng năm vai trong một ngữ cảnh, nên các vai không độc lập và không được hiệu chuẩn.
- *Journal-Fit:* Về độ chặt phương pháp, đề cương đã gần mức một bài nộp lĩnh vực vi cấu trúc thị trường (JFM/RF). Với JFE, điểm yếu là chỉ có một sự kiện, và H1/H4 làm bài bị dàn trải. Luận án vẫn cần H1/H4, nhưng bài báo tạp chí nên xoay quanh H3.
- *Methodology:* CR1, CR2, MJ1, MJ3.
- *Domain:* MJ2 và m6 (chọn chỉ báo trong điều kiện có bước giá và biên độ).
- *Perspective:* m7. Chỉ số dùng làm sản phẩm cho Hà Nội cần được chuẩn hóa theo quy mô danh nghĩa.
- *Devil's Advocate:* Phản biện mạnh nhất là có thể toàn bộ "tác động" H3 chỉ là cơ học của biên độ (CR1) cộng với suy luận quá dễ dãi (CR2). Hai lỗi cùng đẩy về phía bác bỏ H0. Lỗi CRITICAL này của vai Devil's Advocate đã được tôi xác nhận bằng mô phỏng, nên không thể kết luận "chấp nhận" khi chưa sửa.
- *Tín hiệu tổng hợp:* sửa vừa (major revision ở mức tạp chí). Không có vấn đề nào làm hỏng thiết kế cốt lõi.

**mhe-identification (Critic).**
- Câu hỏi viết lại: Y(1) − Y(0) của log Amihud cho các mã đang niêm yết tại HNX khi giao dịch trên HOSE, trong 24 tháng.
- Nguồn biến thiên: một quy định áp lên cả một sàn trong cùng một ngày. Biến thiên này ngoại sinh với từng doanh nghiệp, nhưng về mặt thống kê chỉ có một đơn vị xử lý.
- Đạt: kiểm soát xấu (ghép tại 30/6/2025 là trước xử lý); TWFE không gặp vấn đề vì không có xử lý so le.
- Chưa đạt: (i) đo lường. Biến kết quả bị cắt theo luật biên độ chỉ ở nhóm xử lý (CR1). Trong khung MHE, đây là một dạng chọn mẫu theo kết quả. (ii) Suy luận. Suy luận cũng là một phần của nhận dạng; khi chỉ có một đơn vị xử lý, kích thước của kiểm định phải được chứng minh, không thể mặc định (CR2).
- H1 vẫn chỉ là liên hệ có điều kiện, và đề cương đã gọi đúng như vậy.
- Kết luận: sau khi sửa CR1 và CR2, thiết kế H3 đủ tin cậy để đo tác động gộp của sàn. Nếu chưa sửa, một δ âm có ý nghĩa thống kê chưa phân biệt được với hiệu ứng cơ học.

**aer-identification.**
- Thiết kế 2×2 với một ngày xử lý: dùng TWFE là chấp nhận được.
- Còn thiếu: kiểm định đồng thời các hệ số trước sự kiện (m4); nói rõ cửa sổ trước dùng cho Rambachan–Roth (m4).
- Một đơn vị xử lý ở cấp tổng hợp vốn thuộc vùng phù hợp của synthetic control. Đề cương đã có nhóm đối chứng tổng hợp làm phương án dự phòng, nên tôi không đề xuất thêm.

**review-methodology.**
- Ngôn ngữ nhân quả nhìn chung khớp với thiết kế: H1 là liên hệ, H2 là so sánh, H3 là tác động gộp, H4 là ước lượng.
- Còn hai chỗ nói quá: m1, m2.
- Định nghĩa biến còn thiếu: mẫu xử lý (m5); số ngày tối thiểu và việc chỉ dùng giao dịch khớp lệnh (đã đưa vào câu thay của CR1).

**liquidity-measures.**
- Amihud: định nghĩa còn thiếu ngưỡng chung, số ngày tối thiểu, loại giao dịch thỏa thuận (CR1) và cách chuẩn hóa danh nghĩa (m7).
- Tỷ lệ ngày lợi suất bằng 0 và Corwin–Schultz: chưa xử lý bước giá (MJ2).
- Chi phí giao dịch ở cấu hình B dùng chênh lệch giá chào đóng cửa nhưng đề cương chưa tận dụng dữ liệu này để kiểm chứng các chỉ báo (m6).

**statistical-power.** Xem mục 4. Có hai điểm chính:
- MDE có thể lớn, khoảng 20–40% Amihud nếu φ ≥ 0,6. Cần nói trước điều này để kết quả không bác bỏ không bị đọc thành "không có tác động".
- Kiểm định hoán vị theo ngày giả có sai lầm loại I vượt mức danh nghĩa trong thiết kế này (CR2).

**econ-write.**
- Văn phong nhìn chung rõ: câu có chủ ngữ, hầu như không có văn quảng cáo.
- Còn các lỗi: câu lô-gic rối (m10), câu thiếu chủ ngữ (m11), ký hiệu (m3).
- Khi đưa MDE vào đề cương, dùng φ cho tự tương quan để không trùng với ρ (hệ số ngại rủi ro).

**scientific-critical-thinking.**
- Đề cương đã tách tốt giữa mô tả (H2, giai đoạn căng thẳng, so sánh theo quy mô) và kiểm định (H1–H3), giữa liên hệ (H1) và nhân quả (H3).
- Còn ba chỗ cần sửa: mắt xích "cấu trúc sàn → vai trò trung tâm" (m1); "bình quân tách nguồn" (m2); cần phân biệt "không bác bỏ" với "không có tác động" (MJ3).

**Đối chiếu các lỗi vòng 7 (đã sửa đúng hay chưa):**
- *Đã sửa đúng:* CR1 (UPCoM, idx 78, 79, 287, 355), MJ1 (Naeem dùng thứ hạng), MJ2 (GFCI chứa nhân tố WFE), MJ3 (cửa sổ mẫu của phương trình 5), MJ4 (TT57 và TT69), MJ5 (bài toán 19), MJ7 (QĐ 737), MJ8 (mục tiêu), m1, m2, m3, m5, m6, m8, m10, m11.
- *Sửa một phần:* m7. Chữ đã gộp các tháng trước 1/2024, nhưng OMML (6) chưa có số hạng gộp (xem m4 vòng này).
- *Chưa sửa:* MJ6 (NQ 57, tập trung toàn thời gian). Đây là quyết định của người dùng và thuộc phần Agent B nên tôi không nêu lại.
- *Ngoài phạm vi Agent A, chỉ ghi chú:* danh mục tài liệu tham khảo vẫn chưa theo APA 7 (m9 vòng 7); để Agent B xử lý.

---

## (6) Tài liệu cần tìm

| # | Tên | Tác giả/năm | Vì sao | idx | Nơi tìm | Từ khóa | Ưu tiên |
|---|---|---|---|---|---|---|---|
| 1 | Quy định biên độ dao động giá của HOSE, HNX và UPCoM theo từng thời kỳ 2009–2026 | Bộ Tài chính; HOSE; HNX | CR1: định ngưỡng chung; xác định ±7%/±10% áp dụng từ khi nào | 186, 270 | Thư viện Pháp luật; website HOSE, HNX | "biên độ dao động giá HOSE 7% thông tư", "quy chế giao dịch HNX biên độ 10%" | Cao |
| 2 | Quy định bước giá của HOSE và HNX theo thời kỳ | HOSE; HNX | MJ2 | 186 | Quy chế giao dịch của HOSE và HNX | "bước giá HOSE 10 50 100 đồng", "đơn vị yết giá HNX" | Cao |
| 3 | Bài về kiểm định bất ổn ở cuối mẫu (end-of-sample instability) | Andrews, D. W. K. (2003), *Econometrica* [CẦN XÁC MINH tập, trang] | CR2: cơ sở lý thuyết cho suy luận theo ngày giả khi cửa sổ sau ngắn | 270 | JSTOR; Econometric Society | "end-of-sample instability tests Andrews" | Cao |
| 4 | Bootstrap cho mô hình tự hồi quy có hiệu chỉnh độ chệch | Kilian, L. (1998), *Review of Economics and Statistics* [CẦN XÁC MINH] | CR2: thủ tục bootstrap tự hồi quy | 270 | JSTOR; MIT Press | "small-sample confidence intervals impulse response bias-corrected bootstrap Kilian" | Trung bình |
| 5 | Suy luận khác biệt kép khi có ít nhóm xử lý | Ferman, B., & Pinto, C. (2019), *Review of Economics and Statistics* [CẦN XÁC MINH] | CR2: hạn chế của Conley và Taber khi chỉ có một chuỗi | 270, 181 | RePEc/IDEAS | "Ferman Pinto inference differences-in-differences few treated groups" | Trung bình |
| 6 | Toàn văn và bảng kết quả của Fong, Holden và Trzcinka (2017) | Fong và cộng sự, 2017, *Review of Finance* | m6: chỉ báo nào tốt nhất theo tiêu chí nào, ở thị trường nào | 191 | Oxford Academic | "What are the best liquidity proxies for global research" | Cao |
| 7 | Goyenko, Holden và Trzcinka, so sánh chỉ báo ngày với dữ liệu trong ngày | Goyenko và cộng sự (2009), *Journal of Financial Economics* [CẦN XÁC MINH] | m6: kiểm chứng chỉ báo | 191 | ScienceDirect | "Do liquidity measures measure liquidity" | Trung bình |
| 8 | Abdi và Ranaldo, ước lượng chênh lệch từ giá đóng cửa, cao nhất và thấp nhất | Abdi & Ranaldo (2017), *Review of Financial Studies* [CẦN XÁC MINH] | MJ2: chỉ báo chi phí ít nhạy với bước giá hơn, dùng làm kiểm tra độ bền | 191 | Oxford Academic | "A simple estimation of bid-ask spreads from daily close, high, and low prices" | Thấp |
| 9 | Cách chuẩn hóa Amihud theo quy mô danh nghĩa của thị trường | Acharya & Pedersen (2005), *Journal of Financial Economics* [CẦN XÁC MINH] | m7 | 191 | ScienceDirect | "Asset pricing with liquidity risk normalized illiquidity" | Trung bình |
| 10 | Bảng 3 (ILLIQ) của Hisada (2018), bản PDF rõ chữ | Hisada, 2018 | Mốc độ lớn tác động để so với MDE (mục 4) | 81, 286 | Website IJEFI (econjournals) | "Hisada investor sentiment exchange merger liquidity" | Thấp |
| 11 | Tổng quan về kiểm định trước xu hướng (pretest) và cách báo cáo event study | Roth, J. (2022), *American Economic Review: Insights* [CẦN XÁC MINH] | m4: kiểm định đồng thời các hệ số trước sự kiện | 272 | AEA | "Pretest with caution event-study estimates" | Thấp |
