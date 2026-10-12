XÁC NHẬN: đã gọi được công cụ Skill cho review-paper

# KHÔNG CHẠY ĐƯỢC: thiếu công cụ Agent

Skill review-paper yêu cầu khởi chạy 8 agent song song bằng công cụ Agent (`subagent_type: "general-purpose"`). Trong phiên này không có công cụ Agent. Theo S4 (fail-closed) tôi dừng, không tự đóng vai 8 agent, không chạy bản rút gọn. Điều phối viên quyết định bước tiếp theo.

Lỗi nguyên văn khi tìm công cụ (ToolSearch, query `select:Agent`):

    No matching deferred tools found

Danh sách công cụ của phiên không có công cụ nào tên Agent hoặc Task. Công cụ gần nhất là `mcp__claude-code-remote__create_session`, nhưng đó là phiên khác, không phải subagent của skill, và không áp được scope guard hay kiểm soát nội dung đề cương. Tôi không dùng nó.

## Tham số và giả định
- Tham số: `/tmp/claude-0/-home-user-M-n-HTTM/52cff0a4-7be6-54b9-938a-7f1324974dca/scratchpad/dc/de-cuong.tex`. Token đầu không khớp tên tạp chí nào, nên TARGET_JOURNAL = `top-field` (Leading Field Journal).
- Giới hạn của đối tượng: đề cương KHÔNG có bảng kết quả, chỉ là kế hoạch nghiên cứu. Nếu chạy tiếp, các agent về nhất quán số liệu, bảng/hình, và nhận định kết quả phải ghi rõ giới hạn này.
- Khi chạy tiếp, phải thêm vào mọi agent con: scope guard của skill, và các quy tắc nội dung 1-3 trong quy-tac-cong2.md (không bịa; không đổi thiết kế cốt lõi, lỗi thiết kế vào mục "Lỗi thiết kế cần tác giả duyệt"; không viết quá lên).

## Bằng chứng tuân thủ
- Gọi Skill review-paper: LÀM (kết quả "Launching skill: review-paper", nội dung SKILL.md được nạp). Chứng: tham số `.../dc/de-cuong.tex`.
- Phase 1 (phân tích tham số, TARGET_JOURNAL): LÀM, chỉ phần phân tích tham số như trên.
- Phase 1 (khám phá tệp .tex, include-graph, danh sách hình/bảng): CHƯA LÀM. Lý do: dừng vì thiếu công cụ Agent. Tôi không đọc nội dung đề cương nên không có câu trích.
- Agent 1 (chính tả, ngữ pháp, văn phong): CHƯA LÀM, thiếu công cụ Agent.
- Agent 2 (nhất quán nội bộ, tham chiếu chéo): CHƯA LÀM, thiếu công cụ Agent.
- Agent 3 (khẳng định thiếu cơ sở, nhận diện): CHƯA LÀM, thiếu công cụ Agent.
- Agent 4 (toán, phương trình, ký hiệu): CHƯA LÀM, thiếu công cụ Agent.
- Agent 5 (bảng, hình, tài liệu đi kèm): CHƯA LÀM, thiếu công cụ Agent.
- Agent 6 (đánh giá phản biện: nhận diện, phân tích, định vị, phù hợp tạp chí): CHƯA LÀM, thiếu công cụ Agent.
- Agent 7 (người bênh vực đóng góp): CHƯA LÀM, thiếu công cụ Agent.
- Agent 8 (người hoài nghi đóng góp): CHƯA LÀM, thiếu công cụ Agent.
- Phase 3 (hợp nhất, Priority Action Items): CHƯA LÀM, không có đầu ra agent nào để hợp nhất. Không tạo reviews/ trong repo.

## Số vấn đề theo mức
Không có phát hiện nào, vì không agent nào chạy: NGHIÊM TRỌNG 0, ĐÁNG SỬA 0, CHỈNH NHẸ 0.

## File skill đã đọc
- Tệp đọc bằng Read: 1 (`/tmp/claude-0/-home-user-M-n-HTTM/52cff0a4-7be6-54b9-938a-7f1324974dca/scratchpad/dc/quy-tac-cong2.md`, quy tắc bắt buộc).
- Nội dung SKILL.md: nhận trọn qua kết quả của lệnh gọi công cụ Skill (base `/home/user/M-n_HTTM/.claude/skills/review-paper`), không mở bằng Read. Skill chỉ có SKILL.md, không trỏ tới references/, assets/, templates/ hay agents/.
- Tổng số file skill: 1.

## Điểm ngoài phạm vi (S5)
Skill yêu cầu lưu báo cáo vào `reviews/` trong thư mục bài báo. Tôi không tạo reviews/ mà lưu ở tệp này. Skill không đòi gửi dữ liệu ra ngoài.
