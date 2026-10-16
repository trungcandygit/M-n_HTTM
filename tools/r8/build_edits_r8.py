import json, re

E = []
def rep(i, old, new): E.append({"id": i, "op": "replace", "old": old, "new": new})
def repall(i, old, new): E.append({"id": i, "op": "replace_all", "old": old, "new": new})

# ---------- Agent A ----------
rep("A-CR1a",
    "đề tài vì vậy tính Amihud sau khi loại các ngày chạm biên độ và ngày liền sau mỗi ngày đó, và dùng vòng quay làm thước đo đối chiếu.",
    "việc chỉ loại các ngày chạm biên độ chưa đủ, vì sau khi chuyển sàn mọi ngày có lợi suất tuyệt đối từ khoảng 7% đến 10% trở thành ngày chạm biên độ và bị loại, nên các ngày còn lại có lợi suất tuyệt đối nhỏ hơn một cách cơ học. Đề tài vì vậy tính Amihud, ở cả hai nhóm và cả hai giai đoạn, chỉ trên các ngày có lợi suất tuyệt đối dưới một ngưỡng chung thấp hơn biên độ ±7% (giá trị cụ thể ghi trong tệp đăng ký) và không liền sau một ngày chạm biên độ; giá trị giao dịch chỉ gồm giao dịch khớp lệnh; tháng có ít hơn số ngày hợp lệ tối thiểu ghi trong tệp đăng ký được coi là thiếu; tỷ lệ ngày bị loại và tỷ lệ tháng thiếu được báo cáo theo nhóm và giai đoạn. Vòng quay, không bị cắt theo biên độ như Amihud, là thước đo đối chiếu.")
rep("A-MJ2",
    "và cả khi bỏ hai chỉ báo nhạy với biên độ.",
    "và cả khi bỏ hai chỉ báo nhạy với biên độ. Bước giá cũng khác nhau giữa các sàn [CẦN XÁC MINH quy định bước giá theo từng thời kỳ], nên tỷ lệ ngày lợi suất bằng 0 và chênh lệch Corwin–Schultz phản ánh một phần bước giá thay vì chi phí giao dịch, nhất là ở cổ phiếu giá thấp; đề tài báo cáo hai chỉ báo này theo nhóm mức giá và đọc thay đổi của tỷ lệ ngày lợi suất bằng 0 trong H3 cùng với thay đổi bước giá khi chuyển sàn.")
rep("A-CR1b",
    "tính sau khi loại ngày chạm biên độ và ngày liền sau, giảm so với nhóm đối chứng",
    "tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung và không liền sau ngày chạm biên độ, giảm so với nhóm đối chứng")
rep("A-CR1c",
    "Logarit độ phi thanh khoản Amihud loại ngày chạm biên độ và ngày liền sau (chính)",
    "Logarit độ phi thanh khoản Amihud trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung, loại ngày liền sau ngày chạm biên độ (chính)")
rep("A-CR1d",
    "tính sau khi loại các ngày chạm biên độ và ngày liền sau mỗi ngày đó;",
    "tính trên các ngày có lợi suất tuyệt đối dưới ngưỡng chung (thấp hơn biên độ ±7%) và không liền sau một ngày chạm biên độ;")
rep("A-m5",
    "bằng 1 nếu cổ phiếu chuyển sàn;",
    "bằng 1 nếu cổ phiếu chuyển sàn, tức mọi cổ phiếu niêm yết tại HNX được chuyển sang HOSE theo lịch của VNX, không chỉ các mã của rổ CS;")
rep("A-MJ1",
    "chỉ được ước lượng trong phương trình (6);",
    "chỉ được ước lượng trong phương trình (6); vì giai đoạn tham chiếu dài 16 năm, đề tài kiểm định điểm gãy cấu trúc của chuỗi chênh lệch theo tháng trong giai đoạn này (Bai & Perron, 1998), cho cửa sổ trước của ước lượng chính bắt đầu sau điểm gãy cuối cùng được phát hiện theo quy tắc ghi trong tệp đăng ký, và báo cáo kèm ước lượng với cửa sổ trước 24 tháng (7/2023–6/2025);")
rep("A-CR2a",
    "đề tài dùng sai số chuẩn chịu được tự tương quan trên chuỗi này và suy luận hoán vị trên các ngày giả định trong giai đoạn tham chiếu (Conley & Taber, 2011).",
    "gọi dₜ là chênh lệch trung bình logarit Amihud giữa các cổ phiếu chuyển sàn và các cổ phiếu đối chứng ghép cặp trong tháng t, mỗi cặp có dữ liệu trong tháng có trọng số bằng nhau; thống kê kiểm định là trung bình của dₜ trong giai đoạn sau sự kiện trừ trung bình của dₜ trong cửa sổ trước. Giá trị p chính được tính bằng bootstrap tự hồi quy trên chuỗi dₜ: mô hình tự hồi quy được ước lượng trên giai đoạn tham chiếu, bậc trễ chọn theo tiêu chí thông tin, hệ số được hiệu chỉnh độ chệch, và kích thước của kiểm định được kiểm tra bằng mô phỏng trước ngày đăng ký. Suy luận trên các ngày giả định trong giai đoạn tham chiếu, với cùng cấu trúc cửa sổ trước, 18 tháng loại trừ và 24 tháng sau, theo tinh thần của Conley và Taber (2011), chỉ được báo cáo như kiểm tra bổ sung: các cửa sổ giả chồng lấn nhau và chỉ tạo ra khoảng sáu cửa sổ độc lập, và mô phỏng sơ bộ của thí sinh với chuỗi tự hồi quy bậc một cho thấy kiểm định này bác bỏ giả thuyết không thường xuyên hơn đáng kể so với mức danh nghĩa.")
rep("A-CR2b",
    "H3 được ủng hộ khi δ âm và giá trị p hoán vị nhỏ hơn ngưỡng Holm tương ứng.",
    "H3 được ủng hộ khi δ âm và giá trị p bootstrap tự hồi quy nhỏ hơn ngưỡng Holm tương ứng; giá trị p hoán vị được báo cáo kèm.")
rep("A-CR2c",
    "giá trị p bootstrap khối cho H2 và giá trị p hoán vị cho H3.",
    "giá trị p bootstrap khối cho H2 và giá trị p bootstrap tự hồi quy cho H3.")
rep("A-CR2d",
    "tập ngày giả định cho suy luận hoán vị;",
    "bậc trễ, cách hiệu chỉnh độ chệch và số lần lặp của bootstrap tự hồi quy cho H3 cùng kết quả mô phỏng kích thước của kiểm định; tập ngày giả định cho suy luận hoán vị; ngưỡng lợi suất tuyệt đối và số ngày hợp lệ tối thiểu khi tính Amihud; quy tắc chọn cửa sổ trước theo điểm gãy;")
rep("A-MJ3a",
    "Công suất của H3 phụ thuộc vào số tháng trước và sau sự kiện và vào độ lớn của cú sốc chung theo tháng, không phụ thuộc vào số cổ phiếu, vì mọi cổ phiếu chuyển sàn cùng một ngày.",
    "Công suất của H3 phụ thuộc vào số tháng trước và sau sự kiện và vào phương sai và mức tự tương quan của chuỗi chênh lệch theo tháng; công suất chỉ phụ thuộc yếu vào số cổ phiếu, vì mọi cổ phiếu chuyển sàn cùng một ngày và phần nhiễu riêng của từng mã đã được bình quân trong chuỗi chênh lệch.")
rep("A-MJ3b",
    "Thí sinh tính hiệu ứng nhỏ nhất phát hiện được trên chuỗi chênh lệch của giai đoạn 2009–2025 và ghi vào tệp đăng ký.",
    "Với giả định chuỗi chênh lệch theo tháng là một quá trình tự hồi quy bậc một có hệ số φ và độ lệch chuẩn σ, giai đoạn trước dài 193 tháng (6/2009–6/2025), 18 tháng chuyển tiếp bị loại và giai đoạn sau dài 24 tháng, hiệu ứng nhỏ nhất phát hiện được của δ ở công suất 80% và mức ý nghĩa một phía 0,05/3 xấp xỉ 0,64σ khi φ = 0, 1,24σ khi φ = 0,6 và 1,76σ khi φ = 0,8. Chẳng hạn, với σ = 0,2 và φ = 0,6, đề tài chỉ phát hiện được mức giảm logarit Amihud từ khoảng 0,25 trở lên, tương đương độ phi thanh khoản giảm khoảng 22%. Các giá trị σ và φ này là giả định minh họa; thí sinh ước lượng hai tham số từ chuỗi chênh lệch của giai đoạn tham chiếu, tính lại hiệu ứng nhỏ nhất phát hiện được bằng mô phỏng theo đúng thủ tục kiểm định của H3, và ghi kết quả vào tệp đăng ký trước ngày 28/12/2026.")
rep("A-MJ3c",
    "Nếu dữ liệu không ủng hộ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu bằng kích thước hiệu ứng và khoảng tin cậy.",
    "Nếu dữ liệu không ủng hộ giả thuyết, đề tài vẫn trả lời được câu hỏi nghiên cứu bằng kích thước hiệu ứng và khoảng tin cậy; khi khoảng tin cậy chứa cả 0 lẫn những tác động lớn hơn hiệu ứng nhỏ nhất phát hiện được, kết quả được gọi là chưa đủ cơ sở kết luận, không phải bằng chứng về việc không có tác động.")
rep("A-m8",
    "Ở H1, đề tài kiểm tra độ bền trên mẫu các trung tâm có ít nhất năm kỳ,",
    "Ở H1, đề tài kiểm tra độ bền trên mẫu các trung tâm có ít nhất năm kỳ và trên mẫu cân bằng gồm các trung tâm có mặt ở mọi kỳ được dùng, vì điểm z theo kỳ thay đổi khi tập trung tâm thay đổi,")
rep("A-m1",
    "và cấu trúc sàn định hình vai trò của mỗi trung tâm.",
    "và cấu trúc sàn liên hệ với vai trò của mỗi trung tâm; đề tài không kiểm định quan hệ nhân quả ở mắt xích cuối này.")
rep("A-m2",
    "bình quân theo bảy mô hình và độ phân tán giữa chúng tách hai nguồn này.",
    "bình quân theo bảy mô hình làm kết luận ít phụ thuộc vào một mô hình, còn độ phân tán giữa các mô hình cho biết mức phụ thuộc đó.")
rep("A-m4",
    "Đề tài báo cáo độ nhạy của kết luận khi xu hướng song song bị vi phạm ở mức tương đương độ lệch lớn nhất trước sự kiện (Rambachan & Roth, 2023).",
    "Đề tài kiểm định đồng thời giả thuyết các hệ số δk từ tháng 1/2024 đến tháng 5/2025 bằng 0, và báo cáo độ nhạy của kết luận khi xu hướng song song bị vi phạm ở mức tương đương độ lệch lớn nhất của các hệ số này, tức các tháng trước giai đoạn chuyển tiếp (Rambachan & Roth, 2023).")
rep("A-m6",
    "Amihud và tỷ lệ ngày lợi suất bằng 0 là chỉ báo chính vì hai thước đo này phản ánh tốt chi phí giao dịch trong một quốc gia ở thị trường mới nổi (Lesmond, 2005; Bekaert và cộng sự, 2007; Fong và cộng sự, 2017).",
    "Amihud và tỷ lệ ngày lợi suất bằng 0 là chỉ báo chính vì hai thước đo này đã được dùng rộng rãi ở thị trường mới nổi (Lesmond, 2005; Bekaert và cộng sự, 2007) và đã được so sánh với chuẩn tính từ dữ liệu trong ngày trên mẫu toàn cầu (Fong và cộng sự, 2017); nếu có giá chào mua và chào bán đóng cửa cho một phần mẫu, đề tài báo cáo tương quan giữa các chỉ báo ngày và chênh lệch yết giá đóng cửa trên phần mẫu đó.")
rep("A-m7",
    "Các chỉ báo cổ phiếu được gộp lên cấp sàn bằng trung vị có trọng số theo vốn hóa.",
    "Các chỉ báo cổ phiếu được gộp lên cấp sàn bằng trung vị có trọng số theo vốn hóa. Trước khi chuẩn hóa, độ phi thanh khoản Amihud được nhân với tỷ số giữa tổng vốn hóa của ba sàn trong tháng t và tổng vốn hóa tại tháng 6/2025, để chỉ số không thay đổi chỉ vì quy mô danh nghĩa của thị trường thay đổi.")
rep("A-m9a",
    "ghép có hoàn lại với ngưỡng khoảng cách ghi trong tệp đăng ký.",
    "ghép có hoàn lại với ngưỡng khoảng cách ghi trong tệp đăng ký; mã HOSE được ghép nhiều lần nhận trọng số theo số lần ghép, và số mã khác nhau của rổ H được báo cáo.")
rep("A-m9b",
    "giai đoạn sau sự kiện dùng các cửa sổ từ quý 1/2027 đến quý 4/2028, tức 8 cửa sổ.",
    "giai đoạn sau sự kiện dùng các cửa sổ từ quý 1/2027 đến quý 4/2028, tức 8 cửa sổ. Cửa sổ ước lượng của mọi cửa sổ đánh giá sau sự kiện đều chứa một phần dữ liệu trước ngày chuyển sàn, nên khoảng cách của các mô hình cần ước lượng gộp cả chất lượng thị trường mới lẫn tham số ước lượng trên dữ liệu cũ; khoảng cách của M1, không cần ước lượng, được báo cáo riêng như phép so sánh sạch nhất.")
rep("A-m10",
    "Cặp Hà Nội và Thành phố Hồ Chí Minh có thể so sánh với cặp Bắc Kinh và Thượng Hải, dù Bắc Kinh từng là trung tâm tài chính lớn khi chưa có sở giao dịch chứng khoán (Naeem, 2023) và chỉ có sở giao dịch tầm quốc gia từ năm 2021 [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh], nên câu hỏi chuyên môn hóa (Yao, 2012) đặt ra cho Hà Nội sau đợt hợp nhất.",
    "Cặp Hà Nội và Thành phố Hồ Chí Minh có thể so sánh với cặp Bắc Kinh và Thượng Hải. Bắc Kinh là một trung tâm tài chính lớn dù không có sở giao dịch chứng khoán tầm quốc gia trong phần lớn giai đoạn phát triển của mình (Naeem, 2023) [CẦN XÁC MINH năm thành lập Sở Giao dịch Chứng khoán Bắc Kinh]. Trường hợp này cho thấy một thành phố có thể giữ vai trò trung tâm tài chính mà không cần sàn cổ phiếu, và đặt ra cho Hà Nội câu hỏi chuyên môn hóa (Yao, 2012) sau đợt hợp nhất.")
rep("A-m11",
    "Các chỉ số và tệp đăng ký trước có được bất kể kết quả kiểm định.",
    "Hai chỉ số và tệp đăng ký trước là sản phẩm có được dù kết quả kiểm định ra sao.")

# ---------- Agent B ----------
rep("B-MJ1a",
    "và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 07/2026.",
    "và chương trình thạc sĩ trực tuyến tại WorldQuant University từ tháng 7/2026. Nếu trúng tuyển, thí sinh cam kết theo học chương trình đào tạo tiến sĩ theo hình thức tập trung toàn thời gian, đáp ứng điều kiện tại khoản 3 Điều 11 Nghị quyết số 57/2026/NQ-HĐND (Hội đồng nhân dân thành phố Hà Nội, 2026), và trước khi nhập học sẽ hoàn thành, bảo lưu hoặc dừng các chương trình đang theo học nêu trên để dành toàn bộ thời gian cho học tập và nghiên cứu.")
rep("B-MJ1b",
    "Thời gian đào tạo đối với người có bằng đại học là bốn năm.",
    "Thời gian đào tạo đối với người có bằng đại học là bốn năm, theo hình thức tập trung toàn thời gian; thời gian này không vượt quá 48 tháng, là thời gian hỗ trợ tối đa theo Điều 13 Nghị quyết số 57/2026/NQ-HĐND (Hội đồng nhân dân thành phố Hà Nội, 2026).")
rep("B-MJ2a",
    "Ngược lại, Hisada (2018) nghiên cứu việc chuyển cổ phiếu từ Sở Giao dịch Chứng khoán Osaka sang Sở Giao dịch Chứng khoán Tokyo ngày 16/7/2013 và thấy thanh khoản tăng trong ngắn hạn nhờ hiệu ứng cộng hưởng và tâm lý nhà đầu tư, trong đó hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, rồi thanh khoản giảm sau một năm.",
    "Ngược lại, Hisada (2018) nghiên cứu việc hợp nhất Sở Giao dịch Chứng khoán Tokyo và Sở Giao dịch Chứng khoán Osaka, với thị trường cổ phiếu của hai sở được hợp nhất ngày 16/7/2013, trên mẫu các cổ phiếu niêm yết tại Tokyo không niêm yết kép tại Osaka, và thấy thanh khoản của nhóm cổ phiếu này tăng trong ngắn hạn nhờ hiệu ứng cộng hưởng và tâm lý nhà đầu tư, trong đó hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, rồi giảm sau một năm.")
rep("B-MJ2b",
    "còn Hisada (2018) thấy việc chuyển cổ phiếu từ Osaka sang Tokyo năm 2013 làm thanh khoản tăng trong ngắn hạn, hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, với thước đo là vòng quay và độ phi thanh khoản Amihud.",
    "còn Hisada (2018) thấy thanh khoản của các cổ phiếu sẵn có trên Sở Giao dịch Chứng khoán Tokyo tăng trong ngắn hạn sau khi thị trường cổ phiếu của Osaka được hợp nhất vào Tokyo năm 2013, hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ, với thước đo là vòng quay và độ phi thanh khoản Amihud.")
rep("B-MJ2c",
    "với suy luận phù hợp cho một sự kiện duy nhất, và ước lượng thêm tác động lên khả năng đầu tư.",
    "với suy luận phù hợp cho một sự kiện duy nhất, đo trực tiếp các cổ phiếu được chuyển sàn so với nhóm đối chứng, và ước lượng thêm tác động lên khả năng đầu tư.")
rep("B-MJ2d",
    "nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác.",
    "nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác. Ngược lại, Hisada (2018) cho thấy thanh khoản của cổ phiếu sẵn có trên sàn tiếp nhận cũng tăng trong ngắn hạn quanh đợt hợp nhất Tokyo–Osaka; nếu điều tương tự xảy ra với nhóm đối chứng HOSE, δ đánh giá thấp tác động.")
rep("B-MJ2e",
    "Tokyo–Osaka: hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ",
    "Tokyo–Osaka (cổ phiếu của sàn tiếp nhận): hiệu ứng tâm lý mạnh hơn ở cổ phiếu nhỏ")
rep("B-MJ3",
    "Đề tài cung cấp thước đo nền cho hai câu hỏi này: chất lượng thị trường vốn của Hà Nội thay đổi thế nào khi cấu trúc sàn giao dịch thay đổi.",
    "Đề tài cung cấp thước đo nền cho hai câu hỏi này: chất lượng giao dịch cổ phiếu khác nhau thế nào giữa sàn niêm yết của Hà Nội và sàn của Thành phố Hồ Chí Minh, và thay đổi thế nào khi cổ phiếu niêm yết chuyển từ HNX sang HOSE.")
rep("B-MJ4a",
    "H2: Trong giai đoạn 2009–2026, Chỉ số chất lượng thị trường vốn",
    "H2: Trong giai đoạn tham chiếu từ tháng 6/2009 đến tháng 6/2025, Chỉ số chất lượng thị trường vốn")
repall("B-MJ4b", "Giai đoạn 2009–2026", "Giai đoạn 6/2009–6/2025")
rep("B-MJ4c",
    "H2 được ủng hộ khi chênh lệch bình quân dương với khoảng tin cậy bootstrap khối dừng trên chuỗi tháng loại trừ 0 (Politis & Romano, 1994).",
    "H2 được ủng hộ khi chênh lệch bình quân trong giai đoạn tham chiếu dương và giá trị p bootstrap khối dừng trên chuỗi tháng (Politis & Romano, 1994) nhỏ hơn ngưỡng Holm tương ứng; khoảng tin cậy được báo cáo kèm theo. Chênh lệch trong giai đoạn chuyển tiếp từ tháng 7/2025 đến tháng 12/2026 được báo cáo riêng ở dạng mô tả, vì HNX không nhận niêm yết mới trong giai đoạn này nên thành phần sàn thay đổi có hệ thống.")
rep("B-m1",
    "do Z/Yen và China Development Institute công bố công khai và được thí sinh số hóa từ báo cáo từng kỳ",
    "do Z/Yen công bố công khai từ năm 2007 (từ năm 2015 cùng China Development Institute) và được thí sinh số hóa từ báo cáo từng kỳ")
rep("B-m2",
    "Theo lịch do Sở Giao dịch Chứng khoán Việt Nam (VNX) công bố ngày 30/9/2026, cổ phiếu niêm yết tại HNX giao dịch phiên cuối ngày 23/12/2026 và giao dịch trên HOSE từ ngày 28/12/2026 (Thời báo Tài chính Việt Nam, 2026).",
    "Theo Thời báo Tài chính Việt Nam (2026), lịch do Sở Giao dịch Chứng khoán Việt Nam (VNX) công bố ngày 30/9/2026 ấn định phiên giao dịch cuối của cổ phiếu niêm yết tại HNX là ngày 23/12/2026 và ngày bắt đầu giao dịch trên HOSE là ngày 28/12/2026 [CẦN ĐỐI CHIẾU thông báo gốc của VNX].")
rep("B-m3",
    "Thông tư số 139/2025/TT-BTC không sửa mốc này.",
    "mốc này do Thông tư số 69/2023/TT-BTC đặt, thay cho khung từ ngày 01/01/2025 đến hết ngày 30/6/2025 của Thông tư số 57/2021/TT-BTC, và Thông tư số 139/2025/TT-BTC không sửa mốc này.")
rep("B-lbl2",
    "[CẦN XÁC MINH văn bản hoặc kế hoạch của VNX về UPCoM]",
    "[CẦN XÁC MINH kế hoạch chuyển cổ phiếu đăng ký giao dịch do VNX xây dựng và báo cáo Ủy ban Chứng khoán Nhà nước theo khoản 4 Điều 4 Thông tư số 57/2021/TT-BTC]")
rep("B-m5",
    "Bảng 1 đối chiếu bốn nhóm công trình gần nhất với đề tài và nêu khoảng trống của từng nhóm.",
    "Bảng 1 đối chiếu bốn nhóm công trình gần nhất với đề tài và nêu khoảng trống của từng nhóm; khoảng trống K2 bổ sung cho ba vấn đề nêu ở mục 4.1.")
rep("B-m6",
    "Chỉ số chất lượng thị trường vốn được cập nhật theo tháng cho UPCoM và HOSE khi có dữ liệu mới.",
    "Chỉ số chất lượng thị trường vốn được cập nhật theo tháng cho HOSE, và cho UPCoM trong thời gian UPCoM còn do HNX vận hành, khi có dữ liệu mới.")
rep("B-m7",
    "chỉ áp dụng cho rổ 30 cổ phiếu chuyển sàn có thanh khoản cao nhất",
    "chỉ áp dụng cho rổ CS, gồm tối đa 30 cổ phiếu chuyển sàn có thanh khoản cao nhất")
rep("B-m8",
    "bài báo 3 trình bày bằng chứng quốc tế (H1) và định hướng cho Hà Nội.",
    "bài báo 3 trình bày bằng chứng quốc tế (H1) và so sánh vai trò của Hà Nội với các trung tâm trong khu vực.")
rep("B-m9H",
    "H: rổ cổ phiếu HOSE được ghép với rổ CS",
    "H: rổ cổ phiếu HOSE được ghép với rổ CS (khác với H1–H4, ký hiệu các giả thuyết)")
repall("B-m10a", "30/09/2026", "30/9/2026")
repall("B-m11a", "Nguyen & Nguyen, 2026a", "Nguyễn & Nguyễn, 2026a")
repall("B-m11b", "Nguyen và Nguyen (2026a)", "Nguyễn và Nguyễn (2026a)")
rep("B-l5",
    "Bằng chứng về hợp nhất các sàn trong một quốc gia ở thị trường mới nổi còn ít, ví dụ trường hợp Pakistan hợp nhất ba sở giao dịch năm 2016 [CẦN XÁC MINH nguồn], và chưa đo khả năng đầu tư.",
    "Bằng chứng về hợp nhất sàn chủ yếu đến từ thị trường phát triển; chẳng hạn, Arnold và cộng sự (1999, dẫn theo Hisada, 2018) thấy hợp nhất sàn làm thanh khoản tăng. Bằng chứng ở thị trường mới nổi còn ít và chưa đo khả năng đầu tư.")
rep("B-l7",
    "thí sinh liên hệ Long Finance về giấy phép dùng bộ dữ liệu lịch sử [CẦN XÁC MINH].",
    "thí sinh sẽ xin phép Long Finance dùng bộ dữ liệu lịch sử trước khi phân tích; nếu không được phép, phương án dự phòng thứ nhất ở mục 4.3.10 được áp dụng.")
rep("B-l8",
    "Dữ liệu minh bạch gồm thời điểm công bố báo cáo tài chính [CẦN XÁC MINH nguồn và điều khoản sử dụng].",
    "Dữ liệu minh bạch gồm thời điểm công bố báo cáo tài chính theo quý, lấy từ trang công bố thông tin của HNX và HOSE hoặc từ nhà cung cấp dữ liệu thương mại; nguồn, điều khoản sử dụng và hạn công bố theo quy định được xác nhận trong quý 1 năm thứ nhất (Bảng 5).")
rep("B-l11",
    "gồm phí giao dịch, thuế và một nửa chênh lệch giá chào mua và chào bán đóng cửa [CẦN XÁC MINH dữ liệu lệnh],",
    "gồm phí giao dịch, thuế và một nửa chênh lệch giá chào mua và chào bán, lấy từ giá chào đóng cửa nếu nhà cung cấp dữ liệu có, nếu không thì dùng chênh lệch ước lượng từ giá cao nhất và thấp nhất theo tháng (Corwin & Schultz, 2012),")
rep("B-l12",
    "đề tài dùng số liệu của Liên đoàn các Sở Giao dịch Thế giới [CẦN XÁC MINH].",
    "đề tài dùng số liệu của Liên đoàn các Sở Giao dịch Thế giới, sau khi kiểm tra độ phủ và điều khoản sử dụng.")
rep("B-l15",
    "Nếu được các tổ chức đồng ý, thí sinh lấy ý kiến chuyên gia không chính thức [CẦN XÁC NHẬN với người hướng dẫn].",
    "Nếu người hướng dẫn và các tổ chức liên quan đồng ý, thí sinh lấy ý kiến chuyên gia không chính thức.")
rep("B-l16",
    "kết quả H1 được trình bày như liên hệ mô tả [CẦN XÁC MINH danh sách nhân tố từng kỳ].",
    "kết quả H1 được trình bày như liên hệ mô tả.")
rep("B-l17",
    "HNX, HOSE và các tổ chức đầu tư [CẦN XÁC MINH].",
    "HNX, HOSE và các tổ chức đầu tư.")
rep("B-l10",
    "với sự góp ý của người hướng dẫn dự kiến [CẦN XÁC NHẬN],",
    "sau khi xin góp ý của người hướng dẫn dự kiến,")

# ---------- Danh mục APA 7 (bảng mục 5 của Agent B) ----------
txt = open("/home/user/M-n_HTTM/reports/r8-review-B.md", encoding="utf-8").read()
sec = txt.split("## (5)")[1].split("## (6)")[0]
override = {
    "455": "Quốc hội. (2025). *Nghị quyết số 222/2025/QH15 về Trung tâm tài chính quốc tế tại Việt Nam*.",
    "457": "Thời báo Tài chính Việt Nam. (2026). Chốt thời điểm chuyển toàn bộ cổ phiếu niêm yết về HOSE. *Thời báo Tài chính Việt Nam*. https://thoibaotaichinhvietnam.vn/chot-thoi-diem-chuyen-toan-bo-co-phieu-niem-yet-ve-hose-204623.html",
    "461": "Amihud, Y., Mendelson, H., & Lauterbach, B. (1997). Market microstructure and securities values: Evidence from the Tel Aviv Stock Exchange. *Journal of Financial Economics*, *45*(3), 365–390.",
    "475": "Daw, J. R., & Hatfield, L. A. (2018). Matching and regression to the mean in difference-in-differences analysis. *Health Services Research*, *53*(6), 4138–4156. [CẦN XÁC MINH]",
    "486": "Hoang, V.-M. D., & Luu, D. T. (2024). *Modelling volatility dynamics and identifying regime switching in a frontier stock market: The case of Vietnam* (SSRN Working Paper No. 4867203; bản sửa ngày 17/9/2025). SSRN.",
    "507": "Nguyễn, T. B., & Nguyễn, V. T. (2026a). Black-Litterman portfolio optimization using regime switching CAPM and ABC-MCMC: Empirical evidence from the Vietnamese stock market period 2019–2025. *Tạp chí Nghiên cứu Chính sách và Phát triển*, *3*(1), 81–99. https://doi.org/10.63640/3030-4091/jpd.apd.194",
    "514": "VietnamPlus. (2026a). Ho Chi Minh City jumps 17 places in Global Financial Centres Index. *VietnamPlus*. https://en.vietnamplus.vn/ho-chi-minh-city-jumps-17-places-in-global-financial-centres-index-post352894.vnp",
    "515": "VietnamPlus. (2026b). Vietnam International Financial Centre in Da Nang ranked 71st globally. *VietnamPlus*. https://en.vietnamplus.vn/vietnam-international-financial-centre-in-da-nang-ranked-71st-globally-post352933.vnp",
}
n = 0
for line in sec.splitlines():
    m = re.match(r"^\| (\d{3}|mới) \| (.*?) \| (.*) \|$", line)
    if not m:
        continue
    idx, old, new = m.groups()
    if idx == "mới":
        E.append({"id": "APA-NQ57", "op": "new_para_md_after",
                  "anchor": "Bộ Tài chính (2025), Thông tư số 139/2025",
                  "text": "Hội đồng nhân dân thành phố Hà Nội. (2026). *Nghị quyết số 57/2026/NQ-HĐND ngày 15/6/2026* [CẦN BỔ SUNG trích yếu đầy đủ theo bản chính]."})
        continue
    new = override.get(idx, new)
    old = old.replace("Nguyen, T. B., Nguyen, V. T. (2026a)", "Nguyen, T. B., Nguyen, V. T. (2026a)")
    E.append({"id": f"APA-{idx}", "op": "para_md", "anchor": old[:60], "text": new})
    n += 1
print("APA rows", n)
# NQ57 phải chèn sau khi mục TT139 đã được viết lại -> anchor theo chuỗi mới
for e in E:
    if e["id"] == "APA-NQ57":
        e["anchor"] = "Bộ Tài chính. (2025). Thông tư số 139/2025"
# đưa NQ57 xuống cuối danh sách
E = [e for e in E if e["id"] != "APA-NQ57"] + [e for e in E if e["id"] == "APA-NQ57"]

# chữ viết tắt
E.append({"id": "ABB-ARIMA", "op": "para_md", "anchor": "CS: rổ cổ phiếu chuyển sàn",
          "text": "ARIMA: mô hình tự hồi quy tích hợp trung bình trượt (Autoregressive Integrated Moving Average)"})
E.append({"id": "ABB-CS", "op": "new_para_md_after", "anchor": "ARIMA: mô hình tự hồi quy",
          "text": "CS: rổ cổ phiếu chuyển sàn"})
E.append({"id": "ABB-GDP", "op": "new_para_md_after", "anchor": "CS: rổ cổ phiếu chuyển sàn",
          "text": "GDP: tổng sản phẩm trong nước (Gross Domestic Product)"})
E.append({"id": "ABB-OECD", "op": "new_para_md_after", "anchor": "MQI: Chỉ số chất lượng thị trường vốn (Market",
          "text": "OECD: Tổ chức Hợp tác và Phát triển Kinh tế (Organisation for Economic Co-operation and Development)"})

json.dump(E, open("/tmp/claude-0/-home-user-M-n-HTTM/4e27f401-94ba-5f3b-a0cc-9ab9bcbca829/scratchpad/r8/edits-r8.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E))
