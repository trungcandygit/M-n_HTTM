# Rà soát vòng 1 (B): văn phong, hộp giải thích và trình bày LaTeX của bản dài

Đối tượng: `latex/ban-dai/` (bản dài để thí sinh tự đọc), đối chiếu với `outputs/round-14/v14-text-round-14.txt`.
Ngày rà: 17/10/2026. Người rà: Claude (phiên rà soát B).

Skill đã nạp và áp dụng: vina-me (kèm references/giang-bai.md, dau-hieu.md, loi-thuong-gap.md), vietnamese-human-writing (master-writing-rules.md, R01–R53), scientific-writing, econ-write, sciwrite, consistency-checker.

Cách làm:

- Đọc toàn bộ nguồn `.tex` (main, macros, frontmatter, 10 tệp chương, phụ lục).
- Đọc `main.pdf` bằng `pdftotext -layout`, đọc `main.log`.
- Biên dịch thử trên bản sao ở thư mục tạm (scratchpad), áp bốn sửa đổi trình bày (mục 1, 2, 30, 31 dưới đây) để kiểm tra. Cả bốn chạy được: biên dịch không lỗi, vẫn 78 trang.
- Không sửa tệp nào trong repo ngoài báo cáo này.

Quy ước báo cáo: mỗi phát hiện ghi mức (MAJOR hoặc MINOR), vị trí `tệp:dòng` (tính từ `latex/ban-dai/`), mô tả và cặp sửa. Chuỗi **CŨ** chép nguyên từ `.tex` và chỉ xuất hiện một lần trong tệp đó. **MỚI** là chuỗi thay thế. Đề xuất không thêm sự kiện hay số liệu mới, chỉ dùng nội dung đã có ở chỗ khác trong bản dài hoặc trong v14.

Đánh giá chung: văn bản đã sạch hơn nhiều so với các vòng trước. Gần như không còn sáo ngữ hay khuôn câu máy, số thập phân và hàng nghìn viết đúng, H/M/K đều dùng macro chỉ số dưới, công thức viết đúng lối cổ điển, bảng không tô xám. Lỗi còn lại chủ yếu thuộc bốn loại:

- Hai lỗi trình bày nhìn thấy ngay trong PDF: mục "3. Đơn vị công tác" nuốt đoạn văn đi sau, và trang trắng in câu danh ngôn ngẫu nhiên.
- Vài chỗ tóm tắt hoặc hướng dẫn đọc nói lệch nội dung chính.
- Một số hộp lặp lại đúng đoạn văn ngay cạnh, hoặc đặt trước khi thuật ngữ được giải thích.
- Vài câu tối nghĩa do trật tự từ.

---

## A. Lỗi trình bày nhìn thấy trong PDF

### 1. MAJOR: ch00-thongtin.tex:12. Mục "3. Đơn vị công tác" nuốt đoạn giải thích tên đề tài

`\paragraph` là đề mục chạy liền dòng. Vì mục 3 để trống (đúng như v14), đoạn "Tên đề tài gồm ba vế…" bị in nối ngay sau "3. ĐƠN VỊ CÔNG TÁC." (PDF trang 1). Người đọc sẽ hiểu đoạn đó là nội dung của trường "Đơn vị công tác". Đã thử trên bản sao: thêm `\mbox{}\par` thì đoạn văn xuống dòng riêng.

```text
CŨ: \paragraph{3. Đơn vị công tác.}
MỚI: \paragraph{3. Đơn vị công tác.}\mbox{}\par
```

### 4. MINOR: phuluc.tex:114–115. Ô bảng dùng gạch dài `---` thay cho chữ

Theo vina-me, ô bảng không có giá trị thì viết thành chữ.

```text
CŨ: 23/12/2026 & Phiên giao dịch cuối của cổ phiếu niêm yết tại HNX & ---\\
MỚI: 23/12/2026 & Phiên giao dịch cuối của cổ phiếu niêm yết tại HNX & Mốc lịch chuyển sàn\\
```
```text
CŨ: 24--25/12/2026 & Tạm ngừng giao dịch & ---\\
MỚI: 24--25/12/2026 & Tạm ngừng giao dịch & Mốc lịch chuyển sàn\\
```

(Các mục 30, 31 và 32 về macro, nhãn danh sách và tên danh mục nằm ở phần F.)

---

## B. Câu tóm tắt, hướng dẫn đọc nói lệch nội dung chính

### 5. MAJOR: frontmatter/huongdandoc.tex:22. "Câu chuyện sáu câu" nói như thể đã biết trước kết luận

Câu "đề tài đề xuất Hà Nội nên chuyên môn hóa vào những thị trường mà HNX tiếp tục vận hành" mâu thuẫn với hai chỗ: ch04-1-lydo.tex:54 ("Đề tài không giả định Hà Nội sẽ đi theo hướng nào") và ch04-3c-kiemdinh.tex:207 ("đề tài không chọn trước tình huống nào"). Theo mục tiêu (iv), đề tài *tổng hợp định hướng cho* các thị trường ấy.

```text
CŨ: \item Từ ba câu trả lời, đề tài đề xuất Hà Nội nên chuyên môn hóa vào những thị trường mà HNX tiếp tục vận hành: trái phiếu, phái sinh và UPCoM.
MỚI: \item Từ ba câu trả lời, đề tài tổng hợp định hướng chuyên môn hóa cho những thị trường mà HNX tiếp tục vận hành: trái phiếu, phái sinh và UPCoM.
```

### 7. MAJOR: ch04-3a-khung.tex:13. Hộp tóm tắt 4.3.1 nói mắt xích cuối "chỉ được tổng hợp định tính"

Mắt xích cuối nối cấu trúc sàn với vai trò trung tâm tài chính. Mắt xích này *có* được ước lượng định lượng qua H₁ (phương trình 4.7), chỉ không được kiểm định nhân quả, đúng như thân bài viết ở dòng 18. Hộp tóm tắt vì vậy nói lệch thân bài.

```text
CŨ: Đề tài kiểm định hai mắt xích đầu; mắt xích cuối chỉ được tổng hợp định tính.
MỚI: Đề tài kiểm định hai mắt xích đầu; mắt xích cuối chỉ được ước lượng như một liên hệ có điều kiện (\HH{1}) rồi tổng hợp định tính thành hàm ý, không kiểm định quan hệ nhân quả.
```

### 8. MINOR: ch04-3b-chiso.tex:54. Hộp tóm tắt 4.3.5 gọi \MM{5} là "phức tạp nhất"

Thân bài (dòng 79) xếp bảy mô hình theo lượng tham số phải ước lượng và không gọi mô hình nào là phức tạp nhất. Hộp tóm tắt đưa ra một xếp hạng mà thân bài không có.

```text
CŨ: từ đơn giản nhất (1/N) đến phức tạp nhất (Black-Litterman có chuyển chế độ).
MỚI: từ mô hình không ước lượng tham số nào (1/N) đến các mô hình ước lượng nhiều tham số.
```

### 9. MINOR: ch04-3d-tincay.tex:7. Hộp tóm tắt 4.3.10 tối nghĩa và lệch thân bài

Cụm "khoảng mức giảm 22% của độ phi thanh khoản" khó hiểu. Hộp còn viết "gần như không phụ thuộc vào số cổ phiếu", trong khi thân bài (dòng 12) viết "chỉ phụ thuộc yếu".

```text
CŨ: với các giả định minh họa, khoảng mức giảm 22\% của độ phi thanh khoản. Lực kiểm định phụ thuộc vào số tháng trước và sau, độ biến động và mức tự tương quan của chuỗi chênh lệch, gần như không phụ thuộc vào số cổ phiếu.
MỚI: với các giả định minh họa, độ phi thanh khoản phải giảm khoảng 22\% trở lên. Lực kiểm định phụ thuộc vào số tháng trước và sau, độ biến động và mức tự tương quan của chuỗi chênh lệch, và chỉ phụ thuộc yếu vào số cổ phiếu.
```

Câu tương tự ở phụ lục D:

```text
CŨ: khoảng mức giảm 0,25 của logarit Amihud, tức độ phi thanh khoản giảm khoảng 22\%.
MỚI: logarit Amihud phải giảm khoảng 0,25 trở lên, tức độ phi thanh khoản giảm khoảng 22\%.
```

### 10. MINOR: huongdandoc.tex:10 và :40. Hướng dẫn đọc hứa nhiều hơn những gì bản dài có

- "Mỗi mục lớn mở bằng một hộp tóm tắt": thực tế mục 4.3 (mở bằng đoạn dẫn), 4.3.9, 4.5 và các chương 5–10 không có hộp tóm tắt.
- "Phụ lục A có bảng đối chiếu số công thức": phụ lục A chỉ có một câu đối chiếu, không có bảng.

```text
CŨ: Mỗi mục lớn mở bằng một hộp tóm tắt;
MỚI: Phần lớn các mục và tiểu mục của Chương~4 mở bằng một hộp tóm tắt;
```
```text
CŨ: Phụ lục~\ref{pl:kyhieu} có bảng đối chiếu số công thức.
MỚI: đầu Phụ lục~\ref{pl:kyhieu} ghi cách đối chiếu số công thức.
```

### 11. MINOR: ch04-3a-khung.tex:6. "phát hiện được tác động lớn đến đâu"

Mục 4.3.10 nói về hiệu ứng *nhỏ nhất* phát hiện được, phụ lục D cũng hỏi "phát hiện được tác động nhỏ đến đâu". Câu dẫn cũng gọi tắt "chỉ số chất lượng thị trường", thiếu chữ "vốn".

```text
CŨ: nói rõ đề tài phát hiện được tác động lớn đến đâu
MỚI: nói rõ đề tài phát hiện được tác động nhỏ đến đâu
```
```text
CŨ: dữ liệu (\ref{sec:dulieu}) và chỉ số chất lượng thị trường (\ref{sec:mqi})
MỚI: dữ liệu (\ref{sec:dulieu}) và Chỉ số chất lượng thị trường vốn (\ref{sec:mqi})
```

---

## C. Hộp giải thích thừa, sai chỗ hoặc giải thích sai

### 12. MAJOR: ch04-1-lydo.tex:92–94. Hộp "Chỗ dễ hiểu nhầm" về thứ bậc giả thuyết đặt quá sớm và lặp đoạn ngay trên

Hộp này có bốn vấn đề:

- Hộp nằm ở mục 4.1, trước khi H₁–H₄ được phát biểu (mục 4.3.2).
- Hộp dùng các thuật ngữ chưa được giải nghĩa: "thiết kế nhận dạng", "nhóm đối chứng", "cửa sổ", "kiểm định có lực".
- Hộp lặp gần nguyên dòng 90.
- Dòng 90 viết "kiểm định trọng tâm", hộp viết "kiểm định trung tâm", nên một ý có hai tên.

Đề xuất giữ hộp nhưng viết lại bằng lời thường, không còn thuật ngữ phải hẹn giải thích ở phần sau.

```text
CŨ: \emph{Dễ nghĩ là} bốn giả thuyết có vai trò ngang nhau. Thực ra chỉ \HH{3} là kiểm định trung tâm, vì đó là chỗ đề tài có thiết kế nhận dạng mạnh nhất (một sự kiện ngoại sinh, có nhóm đối chứng). \HH{1} chỉ cho kết luận về liên hệ có điều kiện, không phải quan hệ nhân quả. \HH{2} so sánh hai sàn có nhiều điểm khác nhau ngoài bản thân sàn. \HH{4} chỉ được ước lượng vì có quá ít cửa sổ để kiểm định có lực. Khi trình bày, nên giữ đúng thứ bậc này.
MỚI: \emph{Dễ nghĩ là} bốn giả thuyết có vai trò ngang nhau. Chỉ \HH{3} là kiểm định trọng tâm, vì ở đó việc đổi sàn do quyết định hành chính chứ không do doanh nghiệp chọn, và có cổ phiếu không chuyển sàn để so sánh. \HH{1} chỉ cho kết luận về liên hệ có điều kiện, không phải quan hệ nhân quả. \HH{2} so sánh hai sàn khác nhau ở nhiều điểm ngoài bản thân sàn. \HH{4} chỉ được ước lượng vì có quá ít quan sát để kiểm định đáng tin. Khi trình bày, nên giữ đúng thứ bậc này.
```

### 14. MINOR: ch04-2-tongquan.tex:84–86. Hộp về "chưa có nghiên cứu nào" lặp đoạn dòng 80

Dòng 80 đã nêu phạm vi tìm kiếm, ngày 30/9/2026, các cơ sở dữ liệu chưa tìm và giới hạn "mới đọc tóm tắt". Hộp nói lại đủ các ý đó. Đề xuất chỉ giữ phần hộp có thêm thông tin, tức cách nói khi trả lời hội đồng.

```text
CŨ: \emph{Dễ nghĩ là} câu \enquote{chưa có nghiên cứu nào} là một khẳng định tuyệt đối. Trong đề cương, khẳng định này luôn đi kèm phạm vi tìm kiếm (cơ sở dữ liệu nào, đến ngày nào) và giới hạn (mới đọc tóm tắt phần lớn nguồn). Khi trả lời hội đồng,
MỚI: \emph{Dễ nghĩ là} câu \enquote{chưa có nghiên cứu nào} là một khẳng định tuyệt đối. Nó chỉ đúng trong phạm vi tìm kiếm ở đoạn trên. Khi trả lời hội đồng,
```

### 15. MINOR: ch04-3b-chiso.tex:156 và :174–176. Câu về cửa sổ ước lượng của \MM{1} nói hai lần

Dòng 156 đã kết luận rằng cửa sổ ước lượng sau sự kiện vẫn chứa dữ liệu trước sự kiện, nên \MM{1} là phép so sánh sạch nhất. Hộp ở dòng 175 giải thích lại đúng ý đó, chi tiết hơn. Đề xuất để thân bài chỉ nêu việc làm, lý do để hộp nói.

```text
CŨ: Cửa sổ ước lượng sau sự kiện vẫn chứa dữ liệu trước ngày chuyển sàn, nên khoảng cách của \MM{1}, mô hình không cần ước lượng tham số, được báo cáo riêng như phép so sánh sạch nhất.
MỚI: Khoảng cách của \MM{1}, mô hình không cần ước lượng tham số, được báo cáo riêng như phép so sánh sạch nhất.
```

### 16. MINOR: ch04-3c-kiemdinh.tex:163–165. Hộp về hiệu ứng cố định theo trung tâm lặp dòng 161

Dòng 161 đã nói hiệu ứng cố định làm $\beta$ chỉ còn dựa vào biến thiên nhỏ của $\SMD$, và đề tài báo cáo cả hai đặc tả. Đề xuất rút hộp về phần có thêm thông tin, tức hiệu ứng cố định loại được những gì.

```text
CŨ: Nó loại được mọi đặc điểm không đổi của trung tâm (vị trí, ngôn ngữ, lịch sử), nhưng cũng loại luôn phần lớn biến thiên của $\SMD$, vì mức phát triển thị trường cổ phiếu của một nước ít thay đổi giữa các kỳ GFCI. Khi đó $\beta$ được ước lượng từ rất ít thông tin và có sai số lớn. Đề tài vì vậy báo cáo cả hai đặc tả, có và không có hiệu ứng cố định theo trung tâm, và đọc chúng cùng nhau.
MỚI: Nó loại được mọi đặc điểm không đổi của trung tâm (vị trí, ngôn ngữ, lịch sử), nhưng cái giá là $\beta$ chỉ còn dựa vào phần biến thiên nhỏ của $\SMD$ nêu ở đoạn trên. Vì vậy hai đặc tả được đọc cùng nhau.
```

### 17. MINOR: ch04-3d-tincay.tex:36–38. Hộp "không bác bỏ không có nghĩa là không có tác động" lặp tiểu mục đi ngay sau

Tiểu mục "Khi dữ liệu không ủng hộ giả thuyết" (dòng 44–48) trình bày lại đủ ý, chi tiết hơn (ba kiểu kết quả). Phụ lục D cũng nhắc lại. Đề xuất bỏ câu trùng trong hộp, chỉ giữ ví dụ 10%, là phần hộp có thêm.

```text
CŨ: Kết luận đúng trong trường hợp ấy là \enquote{chưa đủ cơ sở kết luận}, kèm khoảng tin cậy cho biết những tác động nào còn phù hợp với dữ liệu.
MỚI: Cách đọc đúng một kết quả như vậy được trình bày ngay dưới đây.
```

### 18. MINOR: ch04-3a-khung.tex:75. Hộp "Vì sao chỉ ba giả thuyết…" dùng "28 cửa sổ đánh giá" trước khi khái niệm cửa sổ được giải thích (mục 4.3.6)

```text
CŨ: \HH{4} không vào họ này vì chỉ có 28 cửa sổ đánh giá, quá ít để kiểm định có lực;
MỚI: \HH{4} không vào họ này vì chỉ có 28 cửa sổ đánh giá (28 quý, 20 quý trước và 8 quý sau sự kiện, mục~\ref{sec:khanangdautu}), quá ít để kiểm định có lực;
```

### 21. MINOR: ch04-3c-kiemdinh.tex:200. Ví dụ "hai hướng lan tỏa" ghép "tốt lên" với một số âm, dễ đọc ngược

```text
CŨ: nhóm đối chứng tốt lên $-0{,}05$, và khác biệt kép đo được là $-0{,}15$
MỚI: nhóm đối chứng tốt lên (logarit Amihud giảm 0,05, tức thay đổi $-0{,}05$), và khác biệt kép đo được là $-0{,}15$
```

Các hộp còn lại trả lời đúng câu hỏi của chúng và đặt đúng chỗ. Ví dụ số đã được kiểm lại phép tính:

- Holm: 0,05/3 ≈ 0,0167.
- Bước giá: 1,25%, 0,125%, 0,33% và 0,17%.
- Giá trần: 1.210, 10.700, 53.500.
- MQI: −0,2 và 0,3.
- CE: 2,0% và −3,4%; Ḡ = 32,6/7 ≈ 4,66.
- DiD: e^−0,25 − 1 ≈ −22%; e^−0,40 − 1 ≈ −33%.
- Bảng MDE: 1 − e^−x.
- 193 tháng.

Tất cả đều đúng.

---

## D. Câu tối nghĩa, câu quá dài, dùng từ, lặp ý

### 22. MAJOR: ch04-1-lydo.tex:58. Trạng ngữ đặt sai chỗ làm sai nghĩa

"…gồm 299 mã tính đến phiên 30/9/2026 trong cùng một ngày" khiến người đọc gắn "trong cùng một ngày" vào phiên 30/9. Câu này cũng là lần đầu "nhóm đối chứng" xuất hiện trong thân bài mà chưa được giải nghĩa.

```text
CŨ: Đợt hợp nhất ở Việt Nam đổi sàn của toàn bộ cổ phiếu niêm yết tại HNX, gồm 299 mã tính đến phiên 30/9/2026 trong cùng một ngày (Tuổi Trẻ Online, 2026b). Sự kiện này cho phép so sánh cùng các cổ phiếu trước và sau khi đổi sàn với một nhóm đối chứng, về thanh khoản lẫn khả năng đầu tư.
MỚI: Đợt hợp nhất ở Việt Nam đổi sàn cho toàn bộ cổ phiếu niêm yết tại HNX trong cùng một ngày; tính đến phiên 30/9/2026, số cổ phiếu này là 299 mã (Tuổi Trẻ Online, 2026b). Sự kiện này cho phép so sánh cùng các cổ phiếu trước và sau khi đổi sàn với một nhóm đối chứng, tức các cổ phiếu tương đồng nhưng không chuyển sàn, về thanh khoản lẫn khả năng đầu tư.
```

### 23. MAJOR: ch04-3a-khung.tex:119. Câu trong hộp có hai cách hiểu, một cách ngược nghĩa

"Ở HOSE với biên độ hẹp hơn, hiện tượng dồn này xảy ra nhiều hơn ở HNX" có thể hiểu là hiện tượng xảy ra nhiều hơn *tại HNX*.

```text
CŨ: Ở HOSE với biên độ hẹp hơn, hiện tượng dồn này xảy ra nhiều hơn ở HNX, nên ngày hôm sau cũng mang dấu vết của biên độ.
MỚI: Biên độ ở HOSE hẹp hơn nên hiện tượng dồn này xảy ra ở HOSE nhiều hơn ở HNX, và ngày hôm sau cũng mang dấu vết của biên độ.
```

### 24. MAJOR: ch04-3b-chiso.tex:152. Câu tối nghĩa về thiên lệch khi giữ nguyên thành phần rổ

Phần sau dấu chấm phẩy dài 40 chữ, chủ ngữ "thiên lệch" bị hai mệnh đề "do…" che mất, động từ "tác động" đến rất muộn.

```text
CŨ: Thành phần hai rổ được giữ nguyên để so sánh cùng các cổ phiếu quanh sự kiện; vì hai rổ được lập theo cùng quy tắc, thiên lệch do thông tin tại ngày tham chiếu lỗi thời ở các cửa sổ xa hay do hồi quy về trung bình tác động lên cả hai rổ.
MỚI: Thành phần hai rổ được giữ nguyên để so sánh cùng các cổ phiếu quanh sự kiện. Cách làm này có hai nguồn thiên lệch: thông tin tại ngày tham chiếu lỗi thời dần ở các cửa sổ xa, và giá trị giao dịch có thể hồi quy về trung bình. Vì hai rổ được lập theo cùng quy tắc, cả hai nguồn thiên lệch này tác động lên cả hai rổ.
```

### 27. MAJOR: ch04-3d-tincay.tex:56. Câu dài khoảng 90 chữ, ba lần "nên", hai ngoặc trích dẫn

```text
CŨ: Thông báo của VNX chỉ áp dụng cho cổ phiếu niêm yết, nên đợt chuyển ngày 28/12/2026 không gồm UPCoM (Báo Đầu tư Chứng khoán, 2026; Sở Giao dịch Chứng khoán Việt Nam, 2026), nhưng hạn chuyển cổ phiếu UPCoM sang HOSE vẫn là hết ngày 31/12/2026 (Bộ Tài chính, 2023), nên UPCoM có thể chuyển sàn theo một đợt riêng trước hết ngày 31/12/2026, tức trước cửa sổ sau, hoặc trong cửa sổ sau nếu mốc này được lùi.
MỚI: Thông báo của VNX chỉ áp dụng cho cổ phiếu niêm yết, nên đợt chuyển ngày 28/12/2026 không gồm UPCoM (Báo Đầu tư Chứng khoán, 2026; Sở Giao dịch Chứng khoán Việt Nam, 2026). Tuy vậy, hạn chuyển cổ phiếu UPCoM sang HOSE vẫn là hết ngày 31/12/2026 (Bộ Tài chính, 2023). UPCoM vì vậy có thể chuyển sàn theo một đợt riêng trước hạn này, tức trước cửa sổ sau, hoặc trong cửa sổ sau nếu mốc này được lùi.
```

### 28. MINOR: ch04-1-lydo.tex:24. Câu đọc thành "lý do là một luận án tiến sĩ"

```text
CŨ: Lý do chọn vai trò \enquote{thước đo nền} là một luận án tiến sĩ có thể làm tốt việc đo,
MỚI: Đề tài chọn vai trò \enquote{thước đo nền} vì một luận án tiến sĩ có thể làm tốt việc đo,
```

### 29. MINOR: ch04-1-lydo.tex:13 và ch05-10.tex:12. "Sàn … chuyển vào HOSE"

Cổ phiếu chuyển sàn, còn sàn thì không. Hộp tóm tắt cũng viết "chưa ai đo được", mạnh hơn mức khẳng định có giới hạn phạm vi ở mục 4.2. Ngoài ra "tệp đăng ký trước" xuất hiện lần đầu ở đây mà chưa có lời giải nghĩa nào.

```text
CŨ: và sàn cổ phiếu niêm yết của Hà Nội sắp chuyển hết vào HOSE. Lúc này chưa ai đo được Hà Nội mất hay được gì từ việc đó.
MỚI: và toàn bộ cổ phiếu niêm yết trên sàn của Hà Nội sắp chuyển sang HOSE. Trong phạm vi tìm kiếm của thí sinh, chưa có nghiên cứu nào đo Hà Nội mất hay được gì từ việc đó.
```
```text
CŨ: Sản phẩm là hai chỉ số đo được, một tệp đăng ký trước, ba bài báo
MỚI: Sản phẩm là hai chỉ số đo được, một tệp đăng ký trước kế hoạch phân tích, ba bài báo
```
```text
CŨ: sự kiện được nghiên cứu là việc sàn cổ phiếu niêm yết của Hà Nội chuyển vào HOSE,
MỚI: sự kiện được nghiên cứu là việc toàn bộ cổ phiếu niêm yết tại HNX chuyển sang HOSE,
```

### 33. MINOR: ch04-1-lydo.tex:28. "Lợi suất tương đương chắc chắn" dùng trước khi được giải nghĩa

Định nghĩa chỉ xuất hiện ở ch04-3b-chiso.tex:105, trong khi thuật ngữ đã dùng ở 4.1 và 4.2 (dòng 30, 50). Đề xuất chèn lời giải nghĩa có sẵn từ dòng 105 vào lần dùng đầu tiên.

```text
CŨ: \emph{Khả năng đầu tư} của một rổ cổ phiếu là lợi suất tương đương chắc chắn sau chi phí giao dịch mà nhà đầu tư đa dạng hóa đạt được với rổ đó,
MỚI: \emph{Khả năng đầu tư} của một rổ cổ phiếu là lợi suất tương đương chắc chắn sau chi phí giao dịch mà nhà đầu tư đa dạng hóa đạt được với rổ đó, tức mức lợi suất phi rủi ro mà nhà đầu tư ngại rủi ro coi là ngang giá với danh mục trên rổ ấy,
```

### 34. MINOR: ch04-1-lydo.tex:33. "room ngoại" là tiếng nghề, lệch giọng văn và lệch với định nghĩa ở dòng 28

```text
CŨ: Hai rổ có cùng mức room ngoại vẫn có thể
MỚI: Hai rổ có cùng giới hạn sở hữu nước ngoài vẫn có thể
```

### 35. MINOR: ch04-1-lydo.tex:46. Một câu ba vế nối bằng hai dấu chấm phẩy

```text
CŨ: báo chí cho biết cổ phiếu UPCoM không thuộc diện chuyển trong đợt này (Báo Đầu tư Chứng khoán, 2026), và đến ngày 17/10/2026 chưa có văn bản công bố lịch chuyển cổ phiếu UPCoM; đề tài sẽ cập nhật lịch này khi VNX công bố (mục~\ref{sec:tincay}).
MỚI: báo chí cho biết cổ phiếu UPCoM không thuộc diện chuyển trong đợt này (Báo Đầu tư Chứng khoán, 2026). Đến ngày 17/10/2026 chưa có văn bản công bố lịch chuyển cổ phiếu UPCoM; đề tài sẽ cập nhật lịch này khi VNX công bố (mục~\ref{sec:tincay}).
```

### 36. MINOR: ch04-1-lydo.tex:86 và ch04-3c-kiemdinh.tex:7. "mức chịu cú sốc biên độ, bước giá, chỉ số" là chuỗi nén, người đọc ở 4.1 chưa biết "cú sốc chỉ số" là gì

```text
CŨ: kể cả khác biệt của tác động theo mức chịu cú sốc biên độ, bước giá, chỉ số (mục~\ref{sec:kiemdinh}) và theo trụ sở doanh nghiệp;
MỚI: kể cả khác biệt của tác động theo mức cổ phiếu chịu ba thay đổi quy tắc khi chuyển sàn (biên độ hẹp lại, bước giá nhỏ đi, được đưa vào chỉ số của HOSE; mục~\ref{sec:kiemdinh}) và theo trụ sở doanh nghiệp;
```
```text
CŨ: Các tương tác cho biết tác động khác nhau thế nào theo mức chịu cú sốc biên độ, bước giá, chỉ số và theo trụ sở doanh nghiệp.
MỚI: Các tương tác cho biết tác động khác nhau thế nào theo mức cổ phiếu chịu ba thay đổi quy tắc (biên độ, bước giá, việc vào chỉ số HOSE) và theo trụ sở doanh nghiệp.
```

### 37. MINOR: ch04-1-lydo.tex:100–102. Ý "sản phẩm có giá trị dù kết quả ra sao" nói hai lần liền, câu thứ hai khó hiểu

Câu "Một đề tài chỉ có giá trị khi giả thuyết được ủng hộ sẽ khuyến khích nhà nghiên cứu tìm cách cho giả thuyết được ủng hộ" có cụm chủ ngữ dài, phải đọc lại mới hiểu.

```text
CŨ: Điểm cuối cùng quan trọng với người cấp kinh phí. Một đề tài chỉ có giá trị khi giả thuyết được ủng hộ sẽ khuyến khích nhà nghiên cứu tìm cách cho giả thuyết được ủng hộ. Ở đây, ba sản phẩm (hai chỉ số và tệp đăng ký) có giá trị độc lập với chiều của kết quả, nên thành phố nhận được sản phẩm dùng được dù việc chuyển sàn làm thanh khoản tăng, giảm hay không đổi.
MỚI: Điểm cuối cùng quan trọng với người cấp kinh phí. Nếu đề tài chỉ có giá trị khi giả thuyết được ủng hộ, nhà nghiên cứu sẽ có động cơ tìm cách cho giả thuyết được ủng hộ. Ở đây thì khác: thành phố nhận được sản phẩm dùng được dù việc chuyển sàn làm thanh khoản tăng, giảm hay không đổi.
```

### 38. MINOR: ch04-2-tongquan.tex:26. Định nghĩa Corwin–Schultz nói lại gần nguyên văn dòng 24

```text
CŨ: Chênh lệch Corwin--Schultz ước lượng khoảng cách giữa giá mua và giá bán từ giá cao nhất và thấp nhất trong ngày.
MỚI: Chênh lệch Corwin--Schultz trả lời câu hỏi: người mua ngay phải trả cao hơn người bán ngay bao nhiêu.
```

### 39. MINOR: ch04-2-tongquan.tex:30. Con số 30% là giả định nhưng viết như dữ kiện

```text
CŨ: Biết một sàn có độ phi thanh khoản cao hơn sàn kia 30\% chưa cho biết nhà đầu tư mất bao nhiêu tiền.
MỚI: Giả sử biết một sàn có độ phi thanh khoản cao hơn sàn kia 30\%; con số ấy chưa cho biết nhà đầu tư mất bao nhiêu tiền.
```

### 40. MINOR: ch04-2-tongquan.tex:36, :40, :42. Ba chỗ dùng từ hoặc chủ ngữ chưa rõ

```text
CŨ: Đây là bằng chứng rằng thay đổi quy tắc giao dịch, không đổi doanh nghiệp, đủ làm thay đổi cả thanh khoản lẫn giá.
MỚI: Đây là bằng chứng rằng chỉ thay đổi quy tắc giao dịch, trong khi doanh nghiệp giữ nguyên, đã đủ làm thay đổi cả thanh khoản lẫn giá.
```
```text
CŨ: Trường hợp này gần với Việt Nam hơn Euronext ở chỗ là hợp nhất hai sàn trong một quốc gia.
MỚI: Trường hợp này gần với Việt Nam hơn Euronext ở chỗ đây là hợp nhất hai sàn trong một quốc gia.
```
```text
CŨ: Bằng chứng ở thị trường mới nổi còn ít và chưa đo khả năng đầu tư.
MỚI: Bằng chứng về hợp nhất sàn ở thị trường mới nổi còn ít và chưa đo khả năng đầu tư.
```

### 41. MINOR: ch04-3a-khung.tex:20. "được giao dịch cùng với nhiều lệnh hơn" là văn dịch

```text
CŨ: và nó được giao dịch cùng với nhiều lệnh hơn.
MỚI: và nó được giao dịch ở nơi tập trung nhiều lệnh hơn.
```

### 42. MINOR: ch04-3a-khung.tex:86. "chỉ số" không rõ là chỉ số nào, vì Chỉ số chất lượng thị trường vốn chưa được giới thiệu

```text
CŨ: Vì vậy, chỉ số được so sánh trên mẫu đối sánh theo quy mô và ngành,
MỚI: Vì vậy, Chỉ số chất lượng thị trường vốn của hai sàn được so sánh trên mẫu đối sánh theo quy mô và ngành,
```

### 43. MINOR: ch04-3a-khung.tex:102 và :104. Ý "chỉ bỏ ngày chạm biên độ thì hai giai đoạn tính trên hai tập ngày khác nhau" nói hai lần

Dòng 104 có ví dụ cụ thể và rõ hơn, nên bỏ câu ở dòng 102. Ở dòng 104, "chỉ số" nên gọi đúng tên.

```text
CŨ: Chỉ loại các ngày chạm biên độ thì chưa đủ, vì sau khi chuyển sàn mọi ngày lẽ ra có lợi suất tuyệt đối khoảng 7\% đến 10\% đều thành ngày chạm biên độ và bị loại.
MỚI: Chỉ loại các ngày chạm biên độ thì chưa đủ.
```
```text
CŨ: Tử số bị cắt bớt, nên chỉ số giảm, dù độ khó mua bán không đổi.
MỚI: Tử số bị cắt bớt, nên độ phi thanh khoản Amihud giảm, dù độ khó mua bán không đổi.
```

### 44. MINOR: ch04-3a-khung.tex:124. Khả năng đối lập của \HH{4} nằm lạc trong tiểu đề "Biên độ và ngưỡng lợi suất chung khi tính Amihud"

```text
CŨ: Với \HH{4}, quy tắc 1/N có thể xóa khoảng cách
MỚI: \subsubsection*{Khả năng đối lập của \HH{4}}

Với \HH{4}, quy tắc 1/N có thể xóa khoảng cách
```

### 45. MINOR: ch04-3a-khung.tex:134. Câu khoảng 75 chữ; Z/Yen và Long Finance xuất hiện mà không có lời giới thiệu

```text
CŨ: do Z/Yen công bố công khai từ năm 2007, được thí sinh số hóa từ báo cáo từng kỳ nếu Long Finance cho phép (nếu không, xem phương án dự phòng ở mục~\ref{sec:tincay}) và ghép với các chỉ báo
MỚI: do Z/Yen công bố công khai từ năm 2007. Thí sinh số hóa điểm từ báo cáo từng kỳ nếu Long Finance, nơi đăng tải báo cáo, cho phép (nếu không, xem phương án dự phòng ở mục~\ref{sec:tincay}), rồi ghép với các chỉ báo
```

(Chi tiết "nơi đăng tải báo cáo" lấy từ đường dẫn longfinance.net trong mục Wardle & Mainelli của danh mục tài liệu.)

### 46. MINOR: ch04-3a-khung.tex:164–166. "winsorize" dùng trước, giải nghĩa ở đoạn sau

Đề xuất gộp lời giải nghĩa vào lần dùng đầu.

```text
CŨ: Độ phi thanh khoản Amihud được winsorize tại phân vị 1\% và 99\% tính trên mẫu gộp các sàn trong từng tháng, để ngưỡng không đổi khi cổ phiếu đổi sàn.
MỚI: Độ phi thanh khoản Amihud được winsorize tại phân vị 1\% và 99\% tính trên mẫu gộp các sàn trong từng tháng, để ngưỡng không đổi khi cổ phiếu đổi sàn.
```

Thay vào đó, sửa đầu đoạn 166 cho khỏi cụt:

```text
CŨ: Winsorize nghĩa là thay các giá trị quá lớn
MỚI: Winsorize là thay các giá trị quá lớn
```

(Nếu muốn gọn hơn, có thể chuyển nguyên câu ở dòng 166 lên ngay sau câu ở dòng 164, trong cùng một đoạn.)

### 47. MINOR: ch04-3b-chiso.tex:18. Ký hiệu tháng viết thẳng, không đặt trong môi trường toán

```text
CŨ: tổng vốn hóa tháng t và tổng vốn hóa tháng 6/2025
MỚI: tổng vốn hóa tháng $t$ và tổng vốn hóa tháng 6/2025
```

### 49. MINOR: ch04-3b-chiso.tex:94. Khuôn "Thực ra…", "đặc biệt quan trọng"

```text
CŨ: Thực ra vẫn được sửa, nhưng mọi chỗ sửa được ghi lại
MỚI: Kế hoạch vẫn được sửa, nhưng mọi chỗ sửa được ghi lại
```
```text
CŨ: Với một sự kiện chỉ xảy ra một lần, điều này đặc biệt quan trọng, vì không ai lặp lại được nghiên cứu trên một sự kiện khác cùng loại.
MỚI: Với một sự kiện chỉ xảy ra một lần, việc ghi lại này càng cần, vì không ai lặp lại được nghiên cứu trên một sự kiện khác cùng loại.
```

### 50. MINOR: ch04-3b-chiso.tex:111. Ký hiệu $\mu$, $\sigma^2$, $\rho$ được định nghĩa hai đoạn trước công thức

Giữa định nghĩa và công thức là đoạn về hai cấu hình chi phí. Theo econ-write ("define every variable immediately after the equation"), nên báo trước cho người đọc rằng các ký hiệu này thuộc công thức nào.

```text
CŨ: Với mỗi mô hình, mỗi rổ (rổ CS gồm cổ phiếu chuyển sàn, rổ H gồm cổ phiếu HOSE được ghép với rổ CS) và mỗi cửa sổ đánh giá, $\mu$ và $\sigma^2$ là
MỚI: Công thức \eqref{eq:ce} dưới đây dùng ba ký hiệu. Với mỗi mô hình, mỗi rổ (rổ CS gồm cổ phiếu chuyển sàn, rổ H gồm cổ phiếu HOSE được ghép với rổ CS) và mỗi cửa sổ đánh giá, $\mu$ và $\sigma^2$ là
```

### 51. MINOR: ch04-3b-chiso.tex:118. Rổ CS đã được đặt tên ở dòng 111, nên gọi một tên

```text
CŨ: là chênh lệch giữa rổ H và rổ cổ phiếu chuyển sàn:
MỚI: là chênh lệch giữa rổ H và rổ CS:
```

### 52. MINOR: ch04-3c-kiemdinh.tex:20. Cách đọc hệ số logarit chưa chính xác

```text
CŨ: Vì $A_{it}$ là logarit, $\delta$ đọc gần đúng như phần trăm thay đổi khi nhỏ;
MỚI: Vì $A_{it}$ là logarit, khi $\delta$ nhỏ thì $100\delta$ xấp xỉ phần trăm thay đổi;
```

### 53. MINOR: ch04-3c-kiemdinh.tex:43. Hẹn "định nghĩa ở đoạn sau" nhưng định nghĩa nằm cách hai tiểu đề

Bản v14 viết gọn nên "đoạn sau" đúng với bản đó. Ở bản dài, $d_t$ được định nghĩa ở dòng 59, sau cả tiểu đề "Nhóm đối chứng". Theo giang-bai.md, nên giải nghĩa ngay tại chỗ dùng.

```text
CŨ: cửa sổ trước của ước lượng chính bắt đầu sau điểm gãy cấu trúc cuối cùng của chuỗi chênh lệch theo tháng định nghĩa ở đoạn sau (Bai \& Perron, 1998),
MỚI: cửa sổ trước của ước lượng chính bắt đầu sau điểm gãy cấu trúc cuối cùng (Bai \& Perron, 1998) của chuỗi chênh lệch logarit Amihud theo tháng giữa cổ phiếu chuyển sàn và cổ phiếu đối chứng (chuỗi $d_t$, định nghĩa đầy đủ ở phần suy luận bên dưới),
```

### 54. MINOR: ch04-3c-kiemdinh.tex:59 và phuluc.tex:158. "kích thước kiểm định" là thuật ngữ dịch, chưa được giải nghĩa

```text
CŨ: và kích thước kiểm định được kiểm tra bằng mô phỏng trước ngày đăng ký.
MỚI: và kích thước kiểm định (xác suất bác bỏ giả thuyết gốc khi thực ra không có tác động) được kiểm tra bằng mô phỏng trước ngày đăng ký.
```
```text
CŨ: kiểm tra kích thước bằng mô phỏng
MỚI: kiểm tra kích thước kiểm định bằng mô phỏng
```

### 55. MINOR: ch04-3c-kiemdinh.tex:78 và :80. Một khái niệm hai tên: "ngày sự kiện giả định" và "ngày sự kiện giả"

"Giả định" còn dễ đọc thành "giả thiết".

```text
CŨ: Suy luận trên các ngày sự kiện giả định trong giai đoạn tham chiếu,
MỚI: Suy luận trên các ngày sự kiện giả trong giai đoạn tham chiếu,
```

### 56. MINOR: ch04-3c-kiemdinh.tex:100. Lý do dùng vốn hóa toàn phần chưa rõ

```text
CŨ: vì VN-Index không điều chỉnh tỷ lệ tự do chuyển nhượng
MỚI: vì VN-Index tính trọng số theo vốn hóa toàn phần, không điều chỉnh tỷ lệ tự do chuyển nhượng
```

### 57. MINOR: ch04-3c-kiemdinh.tex:115. "tư cách được sàng lọc" là văn dịch

```text
CŨ: nên việc đổi sàn tự nó không thay đổi tư cách được sàng lọc của một mã
MỚI: nên việc đổi sàn tự nó không làm một mã mất hay có thêm tư cách đủ điều kiện
```

### 58. MINOR: ch04-3c-kiemdinh.tex:129. "Văn liệu" lệch với "tài liệu" dùng trong cả bản

```text
CŨ: Văn liệu cho thấy nhà quản lý quỹ
MỚI: Tài liệu cho thấy nhà quản lý quỹ
```

### 60. MINOR: ch04-3c-kiemdinh.tex:205–207. Đoạn "Từ bằng chứng đến định hướng cho Hà Nội" đặt sai chỗ

Mục 4.3.8 nói về ba giả định của khác biệt kép, còn đoạn này nói về bước 5 của quy trình. Đề xuất chuyển nguyên hai đoạn (dòng 205 và 207) xuống ngay sau Hình 4.4 trong mục 4.3.9:

```text
CŨ: \paragraph{Từ bằng chứng đến định hướng cho Hà Nội.}
MỚI: (xóa ở đây cùng đoạn dòng 207; dán nguyên hai đoạn vào sau dòng "\end{figure}" của Hình~\ref{fig:quytrinh})
```

### 61. MINOR: ch04-3c-kiemdinh.tex:213. "năm bước" nhưng Hình 4.4 vẽ sáu ô (bước 0 đến bước 5)

```text
CŨ: Hình~\ref{fig:quytrinh} tóm tắt năm bước của quy trình:
MỚI: Hình~\ref{fig:quytrinh} tóm tắt quy trình gồm bước đăng ký trước (bước 0) và năm bước nghiên cứu:
```

### 62. MINOR: ch04-3d-tincay.tex:16. Câu khoảng 80 chữ gồm ba giả định và ba kết quả

```text
CŨ: Với giả định chuỗi chênh lệch theo tháng là một quá trình tự hồi quy bậc một có hệ số $\phi$ và độ lệch chuẩn không điều kiện $\sigma$, cửa sổ trước dài 193 tháng (6/2009--6/2025), 18 tháng chuyển tiếp bị loại và giai đoạn sau dài 24 tháng, hiệu ứng nhỏ nhất phát hiện được
MỚI: Giả định chuỗi chênh lệch theo tháng là một quá trình tự hồi quy bậc một có hệ số $\phi$ và độ lệch chuẩn không điều kiện $\sigma$, cửa sổ trước dài 193 tháng (6/2009--6/2025), 18 tháng chuyển tiếp bị loại và giai đoạn sau dài 24 tháng. Khi đó hiệu ứng nhỏ nhất phát hiện được
```

### 63. MINOR: ch04-3d-tincay.tex:58. "dùng, tương ứng, …" khó đọc

```text
CŨ: Nếu dữ liệu sau sự kiện ngắn hơn 24 tháng hoặc rổ CS có ít hơn 30 cổ phiếu đủ thanh khoản, đề tài dùng, tương ứng, toàn bộ tháng có sẵn hoặc rổ 20 cổ phiếu.
MỚI: Nếu dữ liệu sau sự kiện ngắn hơn 24 tháng, đề tài dùng toàn bộ tháng có sẵn; nếu rổ CS có ít hơn 30 cổ phiếu đủ thanh khoản, đề tài dùng rổ 20 cổ phiếu.
```

### 65. MINOR: ch05-10.tex:6. "giao thoa" là sáo ngữ (R09)

```text
CŨ: và giao thoa với quản lý ở phần định hướng chuyên môn hóa thị trường vốn Hà Nội.
MỚI: và liên quan đến quản lý ở phần định hướng chuyên môn hóa thị trường vốn Hà Nội.
```

### 66. MINOR: ch05-10.tex:123–125. Đoạn 125 nói lại đúng bốn mối liên hệ vừa nêu ở đoạn 123

Đề xuất bỏ đoạn 125, vì đoạn 123 đã đủ ý. Nếu muốn giữ một câu tóm thì rút gọn:

```text
CŨ: Mối liên hệ giữa công việc đã làm và đề tài có thể tóm lại như sau: điểm gãy cấu trúc (bản thảo số 4) dùng để chọn cửa sổ trước của \HH{3}; nghiên cứu sự kiện trên thanh khoản (bản thảo số 6) là khung của phương trình \eqref{eq:es}; Black-Litterman có chuyển chế độ (Nguyễn \& Nguyễn, 2026a) là mô hình \MM{5}; so sánh nhiều mô hình danh mục (bài số 4 ở Bảng~\ref{tab:congtrinh}) là cách xây dựng chỉ số khả năng đầu tư.
MỚI: Cụ thể, điểm gãy cấu trúc dùng để chọn cửa sổ trước của \HH{3}, và nghiên cứu sự kiện trên thanh khoản là khung của phương trình \eqref{eq:es}.
```

---

## E. Nhất quán thuật ngữ, viết hoa, dấu và tham chiếu

Đã kiểm các thuật ngữ được nêu trong yêu cầu. Bốn thuật ngữ sau dùng nhất quán, không cần sửa:

- "độ phi thanh khoản": 29 lần, không có biến thể như "độ kém thanh khoản".
- "rổ CS" và "rổ H": định nghĩa ở mục 4.3.6 và trong danh mục chữ viết tắt, dùng đúng.
- "nhóm đối chứng": không có biến thể như "nhóm so sánh".
- "lợi suất tương đương chắc chắn": 15 lần, một dạng.

Các chỗ lệch còn lại:

### 67. MINOR: tham chiếu viết cứng và tên gọi "mục 9" lệch "chương 9" (ch04-4-5-phamvi.tex:86, :120)

Bản dài đánh số 5–10 là chương. Phụ lục D cũng đã viết "chương~\ref{ch:9}".

```text
CŨ: như nêu ở mục~9,
MỚI: như nêu ở chương~\ref{ch:9},
```
```text
CŨ: chương~4 thành bài báo 3 (mục~7.3).
MỚI: chương~4 thành bài báo 3 (mục~\ref{sec:nckh}).
```

### 69. MINOR: Ngày tháng có số 0 đứng đầu, lệch với cách viết "1/2027", "6/2025" trong cả bản

Ba chỗ: ch04-3a-khung.tex:142 và :161, phuluc.tex:104.

```text
CŨ: từ ngày 01/7/2025 (Bộ Tài chính, 2023)
MỚI: từ ngày 1/7/2025 (Bộ Tài chính, 2023)
```
```text
CŨ: Từ ngày 01/7/2025, HNX không nhận niêm yết mới
MỚI: Từ ngày 1/7/2025, HNX không nhận niêm yết mới
```
```text
CŨ: 01/7/2025 & HNX ngừng tiếp nhận
MỚI: 1/7/2025 & HNX ngừng tiếp nhận
```

(Các ngày trong bảng công trình và chứng chỉ, như "09/10/2026" và "26/01/2026", nằm ở phần thông tin cá nhân theo v14; có thể giữ nguyên.)

### 70. MINOR: Gạch nối và gạch vừa trong tên hai tác giả chưa thống nhất

Văn bản dùng gạch vừa cho Corwin--Schultz và Tokyo--Osaka, nhưng gạch nối cho Bai-Perron (ch05-10.tex:123) và Black-Litterman (11 lần trong văn xuôi). Theo ghi chú áp dụng của vina-me, tên ghép hai người dùng gạch vừa. Không đụng tên bài báo và danh mục tài liệu (giữ như công bố).

```text
CŨ: độ phi thanh khoản Amihud và phương pháp Bai-Perron.
MỚI: độ phi thanh khoản Amihud và phương pháp Bai--Perron.
```

Với Black-Litterman: nếu đổi thì đổi đồng loạt trong văn xuôi các tệp ch04-2, ch04-3b, ch05-10 (trừ tên bài trong Bảng 8.1, 8.2 và mục 11). Nếu không đổi, nên ghi chú quy ước này trong mục Quy ước trình bày.

Tương tự, "chênh lệch mua-bán" (4 lần) và "Trung bình-phương sai" (ch04-2:46, ch04-3b:69) là hai khái niệm ghép, nên viết gạch vừa:

```text
CŨ: Tối ưu hóa trung bình-phương sai (Markowitz, 1952)
MỚI: Tối ưu hóa trung bình--phương sai (Markowitz, 1952)
```

### 71. MINOR: ch11-tailieu.tex:73 và :87. "Luận án Tiến sĩ" và "Luận án tiến sĩ" viết hoa không thống nhất

```text
CŨ: [Luận án Tiến sĩ Quản trị kinh doanh (DBA), Durham University]
MỚI: [Luận án tiến sĩ Quản trị kinh doanh (DBA), Durham University]
```

### 73. MINOR: huongdandoc.tex:17. "câu hỏi đó" không có từ để trỏ về

```text
CŨ: \item Hà Nội muốn trở thành trung tâm tài chính và dịch vụ chất lượng cao, và đưa câu hỏi đó vào bài toán số 19 của thành phố.
MỚI: \item Hà Nội muốn trở thành trung tâm tài chính và dịch vụ chất lượng cao quốc tế, và đưa câu hỏi làm cách nào để đạt được điều đó thành bài toán số 19 của thành phố.
```

---

## F. Trình bày LaTeX: macro và tên danh mục

### 30. MINOR: macros.tex:31. Lời nguồn và ghi chú dưới bảng, hình bị căn giữa

`\nguon` nằm trong môi trường float đã `\centering` (qua `\myfloatalign`), nên ghi chú hai dòng có dòng cuối bị căn giữa, ví dụ dưới Bảng 4.1 và Bảng 8.2. Đã thử: thêm `\raggedright` thì ghi chú căn trái.

```text
CŨ: \newcommand{\nguon}[1]{\par\vspace{2pt}{\footnotesize #1\par}}
MỚI: \newcommand{\nguon}[1]{\par\vspace{2pt}{\raggedright\footnotesize #1\par}}
```

### 31. MINOR: macros.tex:14. Nhãn danh sách in chữ nhỏ giãn cách làm hỏng chỉ số dưới và chữ thường

Classicthesis in nhãn `description` bằng `\spacedlowsmallcaps`. Hệ quả nhìn thấy trong PDF:

- Phụ lục D in "H 1 CÓ PHẢI…": mất chỉ số dưới.
- "UPCOM" mất chữ "o" thường.
- "CH Í NH", "THIÊN L Ệ CH" bị giãn chữ lệch.
- Các câu hỏi dài trong phụ lục D và các nhãn "Câu hỏi 1:" ở mục 4.1 khó đọc.

Đã thử: định nghĩa lại nhãn thành chữ đậm thường thì cả ba chỗ (Hướng dẫn đọc, mục 4.1, phụ lục D) đều in đúng.

```text
CŨ: \newcommand{\Gbar}{\ensuremath{\bar{G}}}
MỚI: \newcommand{\Gbar}{\ensuremath{\bar{G}}}
\renewcommand{\descriptionlabel}[1]{\hspace*{\labelsep}\normalfont\bfseries #1}
```

### 32. MINOR: Tên "Danh sách bảng", "Danh sách hình vẽ" lệch với "Danh mục chữ viết tắt" và "Danh mục tài liệu tham khảo"

Đã thử dòng sau trong macros.tex, chạy đúng.

```text
CŨ: \newcommand{\Gbar}{\ensuremath{\bar{G}}}
MỚI: \newcommand{\Gbar}{\ensuremath{\bar{G}}}
\addto\captionsvietnamese{\renewcommand{\listtablename}{Danh mục bảng}\renewcommand{\listfigurename}{Danh mục hình}}
```

(Nếu áp cả mục 31 và 32 thì gộp hai dòng thêm vào cùng một chỗ sau `\Gbar`.)

### 74. MINOR: ch04-3c-kiemdinh.tex:102 và :181. Hai bảng không có số và tên, không vào Danh mục bảng

Mọi bảng khác đều có `\caption`. Hai bảng này là bảng nội dung (cú sốc và cách đo; thay đổi trùng thời gian và cách xử lý), không phải bảng tính tay trong hộp ví dụ.

```text
CŨ: \begin{center}
{\bangnho
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.2\textwidth} L L@{}}
MỚI: \begin{center}
\captionof{table}{Ba thay đổi quy tắc khi chuyển sàn và thước đo mức chịu cú sốc}\label{tab:cusoc}
{\bangnho
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.2\textwidth} L L@{}}
```
```text
CŨ: \begin{center}
{\bangnho
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.27\textwidth} L L@{}}
MỚI: \begin{center}
\captionof{table}{Thay đổi trùng thời gian ở HOSE và cách xử lý}\label{tab:trungthoigian}
{\bangnho
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.27\textwidth} L L@{}}
```

(Thêm caption thì số Bảng 4.4 hiện tại thành 4.6. Mọi tham chiếu dùng `\ref` nên tự cập nhật.)

### Cảnh báo trong main.log

Không có lỗi, không có Overfull, không có tham chiếu chưa định nghĩa. Các cảnh báo còn lại đều vô hại:

- titlesec/tocloft dùng chung với KOMA.
- csquotes chưa có kiểu cho tiếng Việt (đã xử lý bằng `\enquote` riêng).
- microtype không có bảng protrusion cho T5.
- Một Underfull ở danh mục chữ viết tắt.
- "Negative labelwidth" ở `phuluc.tex:170` (description `leftmargin=0pt`), không ảnh hưởng hình thức.

`main.out` rỗng nhưng dấu trang PDF vẫn đủ (gói bookmark ghi trực tiếp). Mục lục không liệt kê Danh mục bảng và Danh mục hình. Đây là lựa chọn được, không bắt buộc sửa.

---

## G. Nhận xét độ dài và cân đối (mục 5 của yêu cầu)

1. **Ý "H₄ chỉ ước lượng vì ít cửa sổ" lặp năm lần**: ch04-1:93, ghi chú Bảng 4.2, hộp Holm (ch04-3a:75), ch04-3b:178, ch04-3d:40. Nên giữ lý do đầy đủ ở hộp Holm, các chỗ khác chỉ nêu kết luận. Tương tự, "chưa đủ cơ sở kết luận, không phải bằng chứng không có tác động" xuất hiện ở hộp 4.3.10, tiểu mục ngay sau và phụ lục D (xem mục 17).
2. **Mục 4.3.7 dài nhất** (trang 24–31). Phần dài nhất là tương tác theo mức chịu cú sốc (dòng 96–125), với hai đoạn ba câu dài về suy luận cho hệ số tương tác. Đoạn đó đã đủ ý. Không cần thêm hộp ở đây.
3. **Các trang danh ngôn** (mục 2) chiếm khoảng 8 trang. Bỏ đi thì chiều dài thật của văn bản không đổi nhưng người đọc không bị ngắt mạch.
4. **Bốn chỗ còn khó hiểu, mỗi chỗ nên thêm một câu giải thích:**
   - "hệ số được hiệu chỉnh độ chệch" (ch04-3c:59): vì sao hệ số AR ước lượng trên mẫu ngắn bị chệch về 0. Đây là kiến thức nền, nhưng người đọc tự học sẽ vấp.
   - "vùng hỗ trợ chung": đã được giải nghĩa, tốt.
   - "trung vị có trọng số theo vốn hóa" (ch04-3b:16): nên nói một câu vì sao dùng trung vị thay vì trung bình, cụ thể là để vài mã cực đoan không chi phối.
   - "cửa sổ" có hai nghĩa: cửa sổ trước/sau của khác biệt kép (theo tháng) và cửa sổ ước lượng/đánh giá của chỉ số khả năng đầu tư (104 tuần, 3 tháng). Nên thêm một câu phân biệt hai nghĩa ở lần đầu dùng trong mục 4.3.6.
5. **Mục 4.1 hơi dày ở phần thuật ngữ**: đoạn dòng 28 định nghĩa ba khái niệm trong một đoạn. Theo vina-me, mỗi đoạn nên có tối đa một thuật ngữ mới. Có thể tách "Khả năng đầu tư" thành đoạn riêng, rồi đặt hộp "Chỗ dễ hiểu nhầm" ngay sau đoạn đó.
6. **Chương 5–10** gọn và cân đối, không cần thêm hộp.

---

## Bảng tổng hợp

| # | Mức | Vị trí | Loại | Tóm tắt |
|---|---|---|---|---|
| 1 | MAJOR | ch00-thongtin.tex:12 | Trình bày PDF | Mục "3. Đơn vị công tác" nuốt đoạn giải thích tên đề tài |
| 2 | MAJOR | classicthesis-config.tex:651–652 | Trình bày PDF, nguồn | Trang trắng in danh ngôn ngẫu nhiên, nhiều câu gán sai tác giả |
| 5 | MAJOR | huongdandoc.tex:22 | Nhất quán | Nói như thể đã có kết luận, trái với 4.1 và 4.3.8 |
| 6 | MAJOR | huongdandoc.tex:19; ch04-1:13 | Nhất quán | Câu hỏi 1 bị kể thành "sàn giao dịch" |
| 7 | MAJOR | ch04-3a:13 | Hộp tóm tắt | Mắt xích cuối nói là "chỉ định tính", lệch thân bài |
| 12 | MAJOR | ch04-1:92–94 | Hộp sai chỗ | Hộp thứ bậc giả thuyết đặt trước khi có giả thuyết, dùng thuật ngữ chưa giải nghĩa, lặp dòng 90 |
| 13 | MAJOR | ch04-3c:71 | Ví dụ sai | Bootstrap AR: bước 3 thiếu phần $c + \phi d_{t-1}$ |
| 22 | MAJOR | ch04-1:58 | Câu sai nghĩa | Trạng ngữ "trong cùng một ngày" đặt sai chỗ |
| 23 | MAJOR | ch04-3a:119 | Câu hai nghĩa | "xảy ra nhiều hơn ở HNX" |
| 24 | MAJOR | ch04-3b:152 | Câu tối nghĩa | Thiên lệch khi giữ nguyên thành phần rổ |
| 25 | MAJOR | ch04-3c:207 | Logic | "Chưa đủ cơ sở kết luận" được coi như bằng chứng |
| 26 | MAJOR | phuluc.tex:173 | Gán nguồn | NQ 222 không nói về GFCI hay mất sàn |
| 27 | MAJOR | ch04-3d:56 | Câu quá dài | Khoảng 90 chữ, ba lần "nên" |
| 3 | MINOR | ch11:71 | Dấu | Nháy mở Michaud sai chiều |
| 4 | MINOR | phuluc:114–115 | Dấu | Ô bảng "---" |
| 8 | MINOR | ch04-3b:54 | Hộp tóm tắt | "phức tạp nhất" không có trong thân bài |
| 9 | MINOR | ch04-3d:7; phuluc:179 | Hộp tóm tắt | "khoảng mức giảm", lệch "phụ thuộc yếu" |
| 10 | MINOR | huongdandoc:10, :40 | Nhất quán | Hứa hộp tóm tắt ở mọi mục, hứa "bảng đối chiếu" không có |
| 11 | MINOR | ch04-3a:6 | Từ dùng sai | "tác động lớn đến đâu"; thiếu chữ "vốn" |
| 14 | MINOR | ch04-2:84–86 | Hộp thừa | Lặp dòng 80 |
| 15 | MINOR | ch04-3b:156/174 | Lặp ý | Thân bài và hộp nói cùng ý |
| 16 | MINOR | ch04-3c:163–165 | Hộp thừa | Lặp dòng 161 |
| 17 | MINOR | ch04-3d:36–38 | Hộp thừa | Lặp tiểu mục 44–48 |
| 18 | MINOR | ch04-3a:75 | Thuật ngữ trước định nghĩa | "28 cửa sổ đánh giá" |
| 19 | MINOR | ch04-3c:158 | Ví dụ | Đọc $\beta$ kiểu so sánh chéo, lệch đặc tả FE |
| 20 | MINOR | ch04-3c:154 | Nói quá | Điểm z "không bị ảnh hưởng" |
| 21 | MINOR | ch04-3c:200 | Ví dụ | "tốt lên −0,05" |
| 28 | MINOR | ch04-1:24 | Câu | "Lý do … là một luận án" |
| 29 | MINOR | ch04-1:13; ch05-10:12 | Từ dùng sai | "sàn chuyển vào HOSE"; "chưa ai đo"; "tệp đăng ký trước" chưa giải nghĩa |
| 30 | MINOR | macros.tex:31 | Trình bày | Ghi chú nguồn bị căn giữa |
| 31 | MINOR | macros.tex:14 | Trình bày | Nhãn danh sách in chữ nhỏ giãn cách, mất chỉ số dưới |
| 32 | MINOR | macros.tex | Trình bày | "Danh sách" và "Danh mục" không thống nhất |
| 33 | MINOR | ch04-1:28 | Thuật ngữ trước định nghĩa | Lợi suất tương đương chắc chắn |
| 34 | MINOR | ch04-1:33 | Từ dùng | "room ngoại" |
| 35 | MINOR | ch04-1:46 | Câu dài | Hai dấu chấm phẩy |
| 36 | MINOR | ch04-1:86; ch04-3c:7 | Thuật ngữ nén | "cú sốc biên độ, bước giá, chỉ số" |
| 37 | MINOR | ch04-1:100–102 | Lặp ý, câu khó | Sản phẩm có giá trị dù kết quả ra sao |
| 38 | MINOR | ch04-2:26 | Lặp ý | Định nghĩa Corwin–Schultz |
| 39 | MINOR | ch04-2:30 | Số giả định | 30% viết như dữ kiện |
| 40 | MINOR | ch04-2:36, 40, 42 | Câu | Ba chỗ dùng từ, chủ ngữ |
| 41 | MINOR | ch04-3a:20 | Văn dịch | "giao dịch cùng với nhiều lệnh hơn" |
| 42 | MINOR | ch04-3a:86 | Thuật ngữ mơ hồ | "chỉ số" |
| 43 | MINOR | ch04-3a:102/104 | Lặp ý | Ngày chạm biên độ |
| 44 | MINOR | ch04-3a:124 | Sai chỗ | Đối lập của H₄ dưới tiểu đề Amihud |
| 45 | MINOR | ch04-3a:134 | Câu dài | Z/Yen, Long Finance |
| 46 | MINOR | ch04-3a:164–166 | Thuật ngữ | winsorize |
| 47 | MINOR | ch04-3b:18 | Ký hiệu | "tháng t" |
| 48 | MINOR | ch04-3b:26 | Chính xác | Mốc của điểm 0 |
| 49 | MINOR | ch04-3b:94 | Văn máy | "Thực ra", "đặc biệt quan trọng" |
| 50 | MINOR | ch04-3b:111 | Ký hiệu | Định nghĩa xa công thức |
| 51 | MINOR | ch04-3b:118 | Nhất quán | "rổ cổ phiếu chuyển sàn" thay vì "rổ CS" |
| 52 | MINOR | ch04-3c:20 | Chính xác | Đọc hệ số logarit |
| 53 | MINOR | ch04-3c:43 | Tham chiếu xuôi | "định nghĩa ở đoạn sau" |
| 54 | MINOR | ch04-3c:59; phuluc:158 | Thuật ngữ | "kích thước kiểm định" |
| 55 | MINOR | ch04-3c:78 | Nhất quán | "ngày sự kiện giả định" và "ngày sự kiện giả" |
| 56 | MINOR | ch04-3c:100 | Giải thích | Lý do dùng vốn hóa toàn phần |
| 57 | MINOR | ch04-3c:115 | Văn dịch | "tư cách được sàng lọc" |
| 58 | MINOR | ch04-3c:129 | Nhất quán | "Văn liệu" |
| 59 | MINOR | ch04-3c:135 | Nói quá | Vị trí sàn "không còn quan trọng" |
| 60 | MINOR | ch04-3c:205–207 | Sai chỗ | Đoạn tổng hợp đặt trong mục khác biệt kép |
| 61 | MINOR | ch04-3c:213 | Nhất quán | "năm bước" nhưng hình có sáu ô |
| 62 | MINOR | ch04-3d:16 | Câu dài | Khoảng 80 chữ |
| 63 | MINOR | ch04-3d:58 | Câu | "dùng, tương ứng" |
| 64 | MINOR | ch04-4-5:80 | Nhất quán | "30 mã thanh khoản nhất" |
| 65 | MINOR | ch05-10:6 | Sáo ngữ | "giao thoa" |
| 66 | MINOR | ch05-10:123–125 | Lặp ý | Hai đoạn liên hệ công trình với đề tài |
| 67 | MINOR | ch04-4-5:86, 120 | Tham chiếu | "mục 9", "mục 7.3" viết cứng |
| 68 | MINOR | ch04-3c:45 | Nhất quán | "đảm bảo" và "bảo đảm" |
| 69 | MINOR | ch04-3a:142, 161; phuluc:104 | Định dạng ngày | "01/7/2025" |
| 70 | MINOR | ch05-10:123; ch04-2:46 và các chỗ khác | Dấu | Gạch nối và gạch vừa trong tên ghép |
| 71 | MINOR | ch11:73 | Viết hoa | "Luận án Tiến sĩ" |
| 72 | MINOR | phuluc:55 | Tham chiếu | $\phi$ xuất hiện lần đầu ở 4.3.7 |
| 73 | MINOR | huongdandoc:17 | Câu | "câu hỏi đó" không có từ để trỏ về |
| 74 | MINOR | ch04-3c:102, 181 | Trình bày | Hai bảng không có số và tên |

Tổng: 13 MAJOR, 61 MINOR. Số thứ tự không liên tục theo phần vì các phát hiện được nhóm theo loại; bảng trên liệt kê đủ.

Những gì chưa kiểm:

- Không render ảnh nên chưa kiểm vị trí chữ trong ba hình TikZ (Hình 4.1, 4.2, 4.3). pdftotext không cho thấy chữ chồng nhau, nhưng điều đó chưa đủ để kết luận.
- Không đối chiếu từng câu với v14 để tìm nội dung bị rơi; phần này thuộc rà soát vòng 1 (A).
