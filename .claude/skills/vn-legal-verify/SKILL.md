---
name: vn-legal-verify
description: Đối chiếu mọi khẳng định pháp lý Việt Nam trong đề cương, luận án hay bài báo với văn bản gốc — số hiệu, ngày ký, ngày hiệu lực, điều/khoản/điểm, văn bản hợp nhất (VBHN), chuỗi sửa đổi, quy chế của Sở giao dịch — rồi gắn trạng thái KHỚP / LỆCH / CHƯA CÓ NGUỒN kèm trích nguyên văn. Dùng skill này bất cứ khi nào văn bản nhắc tới thông tư, nghị định, nghị quyết, quyết định, quy chế HOSE/HNX/VNX/UBCKNN, mốc thời gian do luật đặt, hoặc khi người dùng nói "kiểm tra pháp lý", "đối chiếu văn bản", "fact-check điều khoản", kể cả khi họ không nói rõ là cần đối chiếu. Không gọi mạng; chỉ làm việc trên file văn bản người dùng cung cấp.
---

# vn-legal-verify — đối chiếu pháp lý Việt Nam tới văn bản gốc

Mục đích: một hội đồng chuyên ngành sẽ đọc phần pháp lý của đề cương trước tiên và bắt lỗi ở đó nhanh nhất. Một mốc thời gian gán nhầm văn bản (ví dụ mốc do thông tư sửa đổi đặt nhưng ghi là của thông tư gốc) làm mất tin cậy của cả thiết kế dựa trên mốc đó. Skill này buộc mỗi khẳng định pháp lý đi tới đúng câu chữ trong văn bản gốc.

## Nguyên tắc

1. **Nguồn theo thứ bậc.** Công báo / bản có chữ ký > cổng văn bản của cơ quan ban hành (vbpl.vn, congbao.chinhphu.vn, trang của Bộ, Sở giao dịch) > trang thư viện văn bản (thuvienphapluat) > báo chí. Báo chí chỉ là manh mối để tìm văn bản; không bao giờ là nguồn cho khẳng định. Ghi rõ bậc của nguồn dùng để đối chiếu.
2. **Văn bản hợp nhất không phải văn bản gốc.** VBHN chỉ hợp nhất các văn bản tính đến ngày lập; văn bản sửa đổi sau đó không có trong VBHN. Luôn kiểm tra có văn bản nào sửa đổi **sau** ngày ký VBHN không, và điểm nào văn bản sửa đổi đó **không** đụng tới (điểm không bị sửa vẫn giữ hiệu lực).
3. **Gán mốc cho đúng văn bản.** Với mỗi mốc thời gian, xác định văn bản nào đặt ra mốc đó ở dạng hiện hành; dùng chú thích cuối trang của VBHN ("Điểm này được sửa đổi theo quy định tại khoản ... Điều ... Thông tư số ...") để truy nguồn.
4. **Không suy diễn phạm vi.** Một quy tắc nói về "cổ phiếu niêm yết mới" không tự động áp cho "cổ phiếu chuyển sàn". Khi áp quy tắc sang trường hợp văn bản không nêu tên, ghi rõ là suy diễn và gắn nhãn.
5. **Không bịa số hiệu.** Số hiệu, ngày, điều khoản đọc không rõ (OCR hỏng, bản scan) thì ghi đúng phần đọc được và gắn [CẦN XÁC MINH ...]; không "đoán cho đủ".

## Quy trình

**Bước 1 — Liệt kê khẳng định.** Quét văn bản cần kiểm, rút mọi câu có: số hiệu văn bản, ngày, mốc thời gian, tên cơ quan, nghĩa vụ/quyền, con số do văn bản quy định (biên độ, hạn, tỷ lệ). Mỗi khẳng định một dòng, kèm vị trí (mục, đoạn, idx).

**Bước 2 — Định danh văn bản.** Với mỗi khẳng định ghi: loại văn bản, số hiệu đầy đủ (vd "57/2021/TT-BTC"), cơ quan ban hành, ngày ký, ngày hiệu lực, tình trạng hiệu lực, văn bản sửa đổi/bổ sung/thay thế, VBHN hiện có (số hiệu, ngày).

**Bước 3 — Dựng chuỗi sửa đổi.** Vẽ chuỗi theo thời gian: văn bản gốc → các lần sửa (điểm nào, thành gì, hiệu lực từ ngày nào). Đặc biệt chú ý các mốc bị lùi nhiều lần — đây là thông tin cho thiết kế nghiên cứu (kỳ vọng thị trường, phản ứng trước sự kiện), không chỉ là chi tiết pháp lý.

**Bước 4 — Đối chiếu từng khẳng định.** Tìm câu trong văn bản gốc (grep theo số điều, từ khoá, ngày), trích **nguyên văn**, rồi gắn:
- **KHỚP**: câu nguồn nói đúng điều đề cương nói.
- **LỆCH**: sai số hiệu, ngày, điều khoản, phạm vi hoặc gán nhầm văn bản. Trích dòng nguồn và viết chuỗi thay thế chính xác.
- **KHỚP MỘT PHẦN / SUY DIỄN**: đúng một phần, hoặc đề cương mở rộng phạm vi ngoài chữ của văn bản.
- **CHƯA CÓ NGUỒN**: hồ sơ không chứa văn bản cần thiết. Đưa vào danh sách tài liệu cần tìm (Bước 6).

**Bước 5 — Kiểm trích dẫn trong bài và danh mục.** Tên văn bản trong danh mục tài liệu phải đúng trích yếu chính thức; có số hiệu, ngày ký; VBHN ghi số hiệu VBHN. Trích dẫn trong bài và mục danh mục khớp hai chiều.

**Bước 6 — Danh sách tài liệu cần tìm.** Mỗi mục CHƯA CÓ NGUỒN thành một dòng: tên chính xác, cơ quan/năm, số hiệu nếu biết, vì sao cần (mã lỗi), dùng ở đâu, cần phần nào, nơi tìm hợp pháp, từ khoá tiếng Việt/Anh, định dạng mong muốn, ưu tiên.

## Đầu ra (dùng đúng mẫu)

```
## Bảng đối chiếu pháp lý
| # | Khẳng định (vị trí) | Văn bản & điều khoản | Bậc nguồn | Trạng thái | Trích nguyên văn nguồn | Chuỗi thay thế (nếu LỆCH) |

## Chuỗi sửa đổi
<văn bản gốc> → <sửa 1: điểm, nội dung, hiệu lực> → ...

## Phát hiện theo mức
CRITICAL / MAJOR / MINOR — mỗi phát hiện: chuỗi gốc chính xác → chuỗi thay thế chính xác.

## Tài liệu cần tìm
(bảng theo Bước 6)
```

## Lỗi hay gặp cần soi kỹ

- Mốc của văn bản sửa đổi bị ghi là của văn bản gốc.
- Dựa vào VBHN mà quên văn bản sửa đổi ban hành sau ngày lập VBHN; hoặc ngược lại, tưởng văn bản sửa đổi đã sửa cả những điểm nó không đụng tới.
- Nhầm ngày ký với ngày hiệu lực.
- Dẫn quy định của Sở giao dịch (quy chế, quy tắc chỉ số) bằng tên mô tả thay cho trích yếu chính thức.
- Nhầm phạm vi thị trường: niêm yết, đăng ký giao dịch (UPCoM), trái phiếu, phái sinh có quy định riêng.
- Câu "báo chí cho biết ..." đứng cạnh một quy định đang có hiệu lực nói ngược lại.
