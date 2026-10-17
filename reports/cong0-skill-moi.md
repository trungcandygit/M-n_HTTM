# Cổng 0 — Kiểm tra skill mới trước khi dùng

Ngày 2026-10-15. Người dùng duyệt dùng các skill này ("kéo hết về, sửa theo").

| Skill | Nguồn (commit) | Giấy phép | Kiểm tra an toàn | Quyết định |
|---|---|---|---|---|
| statistical-power | K-Dense-AI/claude-scientific-skills @ a1043ef5 | MIT (LICENSE.md) | SKILL.md và references đã đối chiếu với nguồn; scripts/power.py, simulate_power.py chưa đọc hết nên KHÔNG chạy | Dùng ở chế độ hướng dẫn |
| fact-checker | franklee16/academic-research-skills @ 9a4b2db2 | Kho không có file LICENSE; frontmatter ghi MIT | Chỉ có SKILL.md; không có mã | Dùng cục bộ, không commit |
| consistency-checker | franklee16 @ 9a4b2db2 | Kho không có file LICENSE | scripts/ xử lý file LaTeX cục bộ (crossref_validator.py import subprocess); đề cương là .docx nên KHÔNG chạy scripts | Dùng checklist, không commit |
| mhe-identification | franklee16 @ 9a4b2db2 | Kho không có file LICENSE | Chỉ cài SKILL.md và references/research; không cài references/sources (trích nguyên văn sách có bản quyền) | Dùng ở chế độ Critic, không commit |

Đối chiếu: nội dung đã cài khớp với mã nguồn gốc; chỗ khác duy nhất là dòng chú thích nguồn gốc mà agent trước thêm vào. Quét mẫu nguy hiểm (curl, wget, requests, subprocess, os.system, eval, exec, rm -rf, token, api key, câu lệnh chèn): chỉ có `import subprocess` trong crossref_validator.py, và script này không được chạy.

Ràng buộc S5 vẫn áp dụng: không gửi nội dung đề cương ra dịch vụ ngoài; không chạy script chưa đọc. Các skill vẫn nằm trong `.git/info/exclude`, không commit lên repo public.

## Đợt 2 (2026-10-15): tìm skill nhiều sao theo yêu cầu người dùng

Nguồn danh mục: O0000-code/awesome-academic-skills @ 9142287 (CC0, có ghi giấy phép, số sao và việc gọi mạng của từng skill). Người dùng cho phép cài ("ok kéo đủ… Không cần thì thôi").

| Skill | Nguồn (commit) | Sao | Giấy phép | Quyết định | Lý do |
|---|---|---|---|---|---|
| econ-write | hanlulong/econ-writing-skill @ f2bf7a2 | 569 | MIT | **Cài** | Đã đọc SKILL.md; chỉ có file hướng dẫn, không có script; viết kinh tế học theo Cochrane, McCloskey, Shapiro |
| credible-claims | pedrohcgs/claude-code-my-workflow @ ae72617 | 1.5k | MIT | **Cài** | Đã đọc toàn văn; chống nói quá, tách liên hệ và nhân quả |
| grant-proposal | pedrohcgs @ ae72617 | 1.5k | MIT | Không cài | Chỉ chạy khi người dùng gọi tay; phụ thuộc các skill riêng của kho (interview-me, quality_reports); phần kiểm tra độ khớp đã có ở consistency-checker và research-grants |
| challenge | pedrohcgs @ ae72617 | 1.5k | MIT | Không cài | Cần chạy lưới đặc tả trên dữ liệu; đề cương chưa có dữ liệu |
| econ-audit | eabeam/econ-skills @ 1b0238d | – | CC-BY 4.0 | Không cài | Rà mã Stata/R/Python; đề cương chưa có mã |
| avoid-ai-writing | conorbronsdon/avoid-ai-writing @ 2eec2d4 | 3.5k | MIT | Không cài | Tự ghi chỉ hiệu chỉnh cho tiếng Anh; đề cương viết tiếng Việt |
| stop-slop | hardikpandya/stop-slop | 16.5k | MIT | Không cài | Viết cho văn blog tiếng Anh |
| literature-review (K-Dense writer) | K-Dense-AI/claude-scientific-writer @ 529b9f7 | 2.3k | MIT | Không cài | Gọi OpenRouter/parallel-web, trái S5 |
| humanizer, nature-skills, paperspine | – | 38k/37k/5k | MIT | Không cài | Gọi mạng, trái S5 |

Không bổ sung skill sửa Word: anthropic-skills:docx (anthropics/skills, 172k sao) đã có và là lựa chọn tốt nhất trong danh mục.
Hai skill đã cài nằm trong `.git/info/exclude`, không commit.

## Đợt 3 (16/10/2026, vòng 8): bù 6 chỗ yếu

Cách làm: tìm qua các trang tổng hợp (skills.sh, openskillindex, tessl, claudskills) chỉ bằng từ khoá chung; clone nông vào scratchpad để đọc, không thao tác gì trên repo nguồn. Số sao lấy từ trang GitHub (API bị chặn). Quét mẫu: curl, wget, requests, urllib, subprocess, os.system, eval, exec, rm -rf, api key, token.

| # | Nhu cầu | Skill | Repo @ commit | Sao | Giấy phép | Đã đọc | Quét | Đề xuất | Lý do |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Kinh tế lượng | **aer-identification** | brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research @ e0b0c13 (thư mục 50-brycewang-aer-skills) | 4.6k (bộ sưu tập) | MIT (Bryce Wang 2026) | Toàn văn SKILL.md + estimator-playbook.md + agents/openai.yaml | Sạch, không script | **CÀI** | Có cổng nhận dạng, kiểm tra chéo 2×2 với few-cluster/permutation, Honest DiD, event study gộp đầu mút, sẵn câu trả lời phản biện. Bổ sung cho mhe-identification (nghiêng Critic) ở phía "người phản biện sẽ đòi gì" |
| 1 | Kinh tế lượng | **aer-robustness** | cùng repo @ e0b0c13 | 4.6k | MIT | Toàn văn SKILL.md; còn references/robustness-menu.md đọc trước khi cài | Sạch | **CÀI** | Pin kiểm tra độ bền: placebo ngày giả, placebo nhóm, outcome placebo, Honest DiD, MDE với kết quả null; khớp H3 |
| 1 | Kinh tế lượng | event-study (dariia-m) | cùng repo, thư mục 27 | – | Không có file LICENSE trong thư mục | SKILL.md + 3 file | Sạch | Không cài | Thiên về mã R; trùng aer-identification; giấy phép chưa rõ |
| 1 | Kinh tế lượng | causal-inference, identification-proofs (James-Traina) | cùng repo, thư mục 11 | – | (theo bộ sưu tập) | Phần đầu + đếm từ khoá | Sạch | Không cài | Rộng (IV, RDD, SCM), ít sâu ở 2×2 một sự kiện; proof chính thức không cần cho đề cương |
| 1 | Kinh tế lượng | difference-in-differences (sshtomar) | sshtomar/claude-code-skills-social-science @ cedc827 | – | MIT | Phần đầu + đếm từ khoá | Sạch | Không cài | Không có Rambachan–Roth, Conley–Taber, hoán vị |
| 2 | Vi cấu trúc | market-microstructure | HKUDS/Vibe-Trading @ 29aa084 | – | MIT | 120 dòng đầu + grep | Sạch | Không cài | Viết cho giao dịch định lượng (VPIN, TWAP); thiếu Corwin–Schultz, Abdi–Ranaldo, khung so sánh Goyenko–Holden–Trzcinka; Tessl chấm 57 điểm |
| 3 | Pháp lý VN | vn-pdpl | Sushegaad/Claude-Skills-GRC @ aab13e1 | – | MIT | Tên + phạm vi | – | Không cài | Chỉ về bảo vệ dữ liệu cá nhân, không liên quan |
| 3 | Pháp lý VN | vietnamese-law-mcp (ansvar-systems) | – | – | – | Chưa | Là MCP gọi mạng | Không cài ở phiên này | Không phải skill; cần cấu hình MCP |
| 4 | Trích dẫn | **check-citations** | PHY041/claude-skill-citation-checker (bản vendored trong repo bryce, thư mục 62) | 37 | MIT (khai trong README, upstream không có file LICENSE) | **Toàn văn SKILL.md và 721 dòng scripts/citation_checker.py** | Có `requests.get` tới api.crossref.org, api.semanticscholar.org, api.openalex.org; chỉ gửi DOI hoặc tiêu đề bài đã công bố, không gửi câu chữ đề cương; không ghi file, không subprocess | **CÀI, nhưng chưa chạy được** | Proxy chặn cả ba host (CONNECT 403). Cần anh mở mạng; trước khi đó dùng tra tay |
| 4 | Trích dẫn | bib-verify (OpenJudge), verify-refs (aperivue), validate-bib (pedrohcgs) | – | – | Apache/MIT | Đếm file + quét | verify-refs có 20 script, 14 file gọi mạng | Không cài | Trùng chức năng; verify-refs nặng và thiên y sinh |
| 5 | Pre-analysis plan | **preregister** | pedrohcgs/claude-code-my-workflow @ ae72617 | 1.7k | MIT (Pedro Sant'Anna) | Toàn văn SKILL.md | Sạch, không script | **CÀI có điều kiện** | Mẫu OSF với cờ MUST/SHOULD/MAY, cấm bịa, kiểm hướng giả thuyết, estimator, quy tắc loại ex ante. Có `disable-model-invocation: true` (phải gỡ thì Skill tool mới gọi được) và cần `templates/preregistration-template.md`, `templates/requirements-spec.md` (chép kèm, đọc trước) |
| 6 | Sửa docx | anthropic-skills:docx | anthropics/skills | 172k | – | đã có | – | Giữ | Không có lựa chọn mạnh hơn |

Chỗ trống không có skill đạt chuẩn: (2) đo thanh khoản và (3) tra cứu pháp lý Việt Nam. Hai phương án: (a) tự viết hai skill cục bộ dạng checklist (không gọi mạng, mọi trích dẫn mang nhãn cho đến khi đối chiếu với bài gốc), hoặc (b) để agent áp dụng thẳng quy trình đối chiếu KHỚP/LỆCH/CHƯA CÓ NGUỒN của prompt.

### Quyết định của người dùng (16/10/2026)
- Cài: **aer-identification** (SKILL.md, references/estimator-playbook.md, LICENSE; ghi nguồn trong NGUON.md). Không cài aer-robustness, check-citations, preregister.
- Tự viết 2 skill cục bộ (qua anthropic-skills:skill-creator; không gọi mạng, không script): **vn-legal-verify**, **liquidity-measures**. Bỏ bước chạy thử bằng subagent của skill-creator vì người dùng yêu cầu giảm agent; thay bằng dùng thật ở vòng 8 và rà lại sau vòng.
- Mạng: proxy chặn api.crossref.org, api.openalex.org, api.semanticscholar.org (CONNECT 403).
- Vòng 8: 2 agent song song (A: phương pháp và viết; B: kiểm chứng pháp lý và văn liệu).

## Đợt 4 (16/10/2026): skill viết tiếng Việt

Tìm trên GitHub bằng từ khóa chung ("claude skill Vietnamese academic writing", "skill viết luận văn tiếng Việt", "paper-writing-vn"). Không có skill riêng cho văn học thuật tiếng Việt hay cho định dạng luận án ĐHQGHN. Skill "paper-writing-vn" nêu trong prompt không tồn tại công khai.

| Skill | Repo @ commit | Sao | Giấy phép | Đã đọc | Quét | Quyết định | Lý do |
|---|---|---|---|---|---|---|---|
| **vina-me** | AnhTuan2111/vina-me @ dbeb502 | 0 | MIT | Toàn văn SKILL.md (2.486 từ); toàn văn scripts/soat.mjs (138 dòng) | soat.mjs chỉ `fs.readFileSync`; không mạng, không ghi tệp, không lệnh con | **CÀI** | Viết bằng tiếng Việt cho văn bản tiếng Việt: mạch lạc, liên kết câu, câu chủ đề, thuật ngữ nhất quán, nói đúng mức chắc chắn, dấu hiệu văn máy; có giọng trang trọng cho báo cáo/kiến nghị. Xung đột với APA 7 ở dấu "–" và "&": đã thêm ghi chú miễn trừ |
| **vietnamese-human-writing** | Seastorm136/vietnamese-human-writing-skill @ fcb14ee | 0 | MIT | Toàn văn SKILL.md; mục I–II và cấu trúc I–XII của master-writing-rules.md | Không có script | **CÀI** | 53 quy tắc, 7 vòng rà; thứ tự ưu tiên đặt độ chính xác và thể loại lên trước văn phong; có quy định riêng cho văn khoa học |
| viet-ky-thuat, viet-lach | mqa8668/claude-skills @ 0eff236 | – | MIT | Liệt kê tệp | Repo có script cài đặt và build tài liệu | Không cài | Thiên về tài liệu kỹ thuật phần mềm và bản song ngữ |
| academic-writing-skills | WenyuChiou/academic-writing-skills @ 06fbdfd | – | MIT | Liệt kê tệp | 8 script audit | Không cài | Tiếng Anh; trùng scientific-writing và sciwrite |
| academic-writing | David-Saeteros/claude-skills @ 18f912c | – | CC BY 4.0 | Liệt kê tệp | – | Không cài | Tiếng Anh; trùng econ-write |
| latex-thesis-zh và nhóm | bahayonghang/academic-writing-skills @ 8183f08 | – | – | Liệt kê tệp | – | Không cài | Luận án tiếng Trung, LaTeX |

Còn thiếu: skill định dạng theo quy chế ĐHQGHN và Trường Quốc tế. Chỉ viết được khi có văn bản quy chế.

## Vòng 5 (17/10/2026): skill ký hiệu kinh tế lượng và toán

Tìm bằng từ khoá chung ("github claude skill econometrics SKILL.md", "github claude skill math notation LaTeX equations SKILL.md"); không gửi câu chữ đề cương ra ngoài. Clone chỉ đọc vào scratchpad.

| Skill | Nguồn (commit) | Giấy phép | Tệp đã đọc hết | Quét curl/wget/requests/subprocess/eval/exec/rm -rf/token/api key | Quyết định |
|---|---|---|---|---|---|
| panel-data-guide | brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research @e0b0c13 (wentor-research-plugins) | CC BY-SA 4.0 | SKILL.md | Không có; chỉ chứa ví dụ mã Stata/R/Python trong khối code, không có script chạy | CÀI |
| mostly-harmless-guide | như trên | CC BY-SA 4.0 | SKILL.md | Không có; một URL nguồn trong metadata | CÀI |
| latex-econ-model | meleantonio/awesome-econ-ai-stuff @dd890d5 | CC0 1.0 | SKILL.md, index.md (bản trùng) | Không có; ba URL tài liệu tham khảo | CÀI |
| math-reasoning | lingzhi227/agent-research-skills @9e6c085 | Không có tệp giấy phép | SKILL.md, references/notation-guide.md, references/proof-templates.md | Không có | KHÔNG CÀI (không rõ giấy phép; nội dung thiên về ký hiệu học máy) |

Không skill nào gửi nội dung đề cương qua mạng.
