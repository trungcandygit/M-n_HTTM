import json
A=json.load(open('../r10/edits-A.json',encoding='utf-8'))
byold={e['old']:e for e in A}
def setnew(prefix,new):
    for e in A:
        if e['old'].startswith(prefix): e['new']=new; return
    raise SystemExit('missing '+prefix)
# FTSE: gộp A-MJ4 và B-MJ1
setnew("và việc vào chỉ số FTSE chỉ liên quan",
 "và việc vào VN-Index cùng các chỉ số khác do HOSE xây dựng tạo áp lực cầu lớn hơn ở mã có vốn hóa tự do chuyển nhượng lớn so với giá trị giao dịch [CẦN XÁC MINH cách HOSE xử lý mã chuyển sàn trong các chỉ số].")
setnew("và biến chỉ mã thuộc danh sách dự kiến của FTSE Russell",
 "và tỷ số giữa vốn hóa tự do chuyển nhượng và giá trị giao dịch bình quân ngày (mức chịu cú sốc chỉ số). Việc FTSE Russell đưa cổ phiếu Việt Nam vào chỉ số không được coi là một kênh của việc chuyển sàn: danh sách cổ phiếu đủ điều kiện, lập với dữ liệu đến ngày 30/6/2026, chỉ gồm mã niêm yết tại HOSE (FTSE Russell, 2026), nên biến này không có biến thiên giữa các mã chuyển sàn và chỉ được dùng để loại mã khỏi nhóm đối chứng HOSE ở mục 4.3.8.")
# trụ sở: gộp A-MJ5 và B-MJ3
setnew("Nếu chênh lệch khác 0, kết quả cho biết",
 "Nếu chênh lệch khác 0, kết quả gợi ý vị trí sàn có liên hệ với thanh khoản của doanh nghiệp có trụ sở tại Hà Nội; nếu khoảng tin cậy hẹp quanh 0, kết quả không ủng hộ vai trò của vị trí sàn khi giao dịch đã điện tử hóa toàn quốc; nếu khoảng tin cậy rộng, kết quả được gọi là chưa đủ cơ sở kết luận theo quy tắc ở mục 4.3.10. Chênh lệch này không đo lượng thanh khoản mà thị trường vốn Hà Nội mất, vì mọi mã trong phép so sánh đều chuyển sang HOSE. Tệp đăng ký ghi số mã có trụ sở tại Hà Nội trong các mã chuyển sàn và hiệu ứng nhỏ nhất phát hiện được của hệ số này. Trong mọi trường hợp, kết quả là đầu vào định lượng cho định hướng chuyên môn hóa ở cuối mục 4.3.8.")
E=list(A)
def rep(i,o,n): E.append({"id":i,"op":"replace","old":o,"new":n})
def split(i,a): E.append({"id":i,"op":"split_before","anchor":a})
rep("B-MJ3b","[CẦN ĐỐI CHIẾU bản gốc của hai bài].",
 "[CẦN ĐỐI CHIẾU bản gốc của hai bài]. Hai bài này nói về khoảng cách giữa nhà đầu tư và doanh nghiệp, không nói về vị trí của sàn; khi sàn đổi, nhà đầu tư không đổi chỗ, nên kênh mà đề tài kiểm tra là sự chú ý và thông tin gắn với sàn niêm yết, chẳng hạn mức độ đưa tin và việc có mặt trong HNX-Index.")
rep("B-MJ2a","Amihud và cộng sự (1997) ghi nhận thanh khoản lan tỏa giữa các cổ phiếu liên quan; nếu nhóm đối chứng HOSE mất thanh khoản",
 "Nếu nhóm đối chứng HOSE mất thanh khoản")
rep("B-MJ2b","Ngược lại, Hisada (2018) cho thấy thanh khoản của cổ phiếu sẵn có trên sàn tiếp nhận cũng tăng trong ngắn hạn quanh đợt hợp nhất Tokyo–Osaka;",
 "Ngược lại, tác động lan tỏa có thể theo chiều dương: Amihud và cộng sự (1997) thấy khi một loại cổ phiếu của doanh nghiệp được chuyển sang cơ chế giao dịch tốt hơn, loại cổ phiếu còn lại của cùng doanh nghiệp cũng tăng giá, phù hợp với thanh khoản lan tỏa dương giữa các chứng khoán có giá trị tương quan; Hisada (2018) cho thấy thanh khoản của cổ phiếu sẵn có trên sàn tiếp nhận cũng tăng trong ngắn hạn quanh đợt hợp nhất Tokyo–Osaka.")
rep("B-MJ2c","nếu điều tương tự xảy ra với nhóm đối chứng HOSE, δ đánh giá thấp tác động.","Nếu điều tương tự xảy ra với nhóm đối chứng HOSE, δ đánh giá thấp tác động.")
rep("B-m1","và nêu rõ giao dịch tại các thị trường khác do HNX tổ chức","và nêu rõ trong hai ngày tạm ngừng, giao dịch tại các thị trường khác do HNX tổ chức")
rep("B-m2","biên độ do Sở giao dịch quyết định sau khi Ủy ban Chứng khoán Nhà nước chấp thuận (Bộ Tài chính, 2020)",
 "biên độ do Sở Giao dịch Chứng khoán Việt Nam quyết định sau khi Ủy ban Chứng khoán Nhà nước chấp thuận, và Ủy ban Chứng khoán Nhà nước có thể điều chỉnh biên độ khi cần ổn định thị trường (Bộ Tài chính, 2020)")
rep("B-m3","chúng tác động như nhau lên cổ phiếu chuyển sàn và nhóm đối chứng HOSE, và ngưỡng lợi suất chung",
 "chúng áp dụng chung cho cổ phiếu chuyển sàn và nhóm đối chứng HOSE nhưng có thể tác động mạnh hơn ở mã thường chạm biên độ, nên ngày áp dụng được ghi là một cú sốc trùng thời gian, ước lượng được báo cáo thêm với cửa sổ sau cắt tại ngày đó, và ngưỡng lợi suất chung")
rep("B-m4","đang nghiên cứu nới biên độ dao động giá và giao dịch xuyên trưa (Thời báo Tài chính Việt Nam, 2026)",
 "đang nghiên cứu nới biên độ dao động giá và giao dịch xuyên trưa, và Bộ Tài chính đặt vấn đề nghiên cứu rút ngắn chu kỳ thanh toán (Thời báo Tài chính Việt Nam, 2026)")
rep("B-m5","Nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt hoặc trong 24 tháng sau sự kiện,",
 "Theo văn bản hiện hành, cổ phiếu UPCoM phải được chuyển sang HOSE chậm nhất đến hết ngày 31/12/2026 (Bộ Tài chính, 2023), nên đề tài coi trường hợp sau là khả năng chính: nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt hoặc trong 24 tháng sau sự kiện,")
rep("B-m7","(3 trong 144 nhân tố của kỳ GFCI 40; Wardle & Mainelli, 2026)","(3 trong 144 nhân tố của kỳ GFCI 40, cùng bảng với nhân tố mức chỉ số cổ phiếu; Wardle & Mainelli, 2026)")
rep("B-m10a","Nếu không số hóa được điểm GFCI theo kỳ,","Nếu không số hóa được hoặc không được phép dùng điểm GFCI theo kỳ,")
rep("B-m10b","không số hóa được điểm GFCI;","không số hóa được hoặc không được phép dùng điểm GFCI;")
rep("B-m11","Hà Nội, ngày 30 tháng 9 năm 2026","Hà Nội, ngày … tháng 10 năm 2026")
rep("B-m12a","Tuổi Trẻ Online. (2026). HOSE chia cổ phiếu thành hai bảng Prime Board và Standard Board. Tuổi Trẻ Online. https://",
 "Tuổi Trẻ Online. (2026). HOSE dự kiến chia cổ phiếu thành hai bảng Prime Board và Standard Board. https://")
rep("B-m12b","nghiên cứu giao dịch xuyên trưa và nới biên độ. Thời báo Tài chính Việt Nam. https://","nghiên cứu giao dịch xuyên trưa và nới biên độ. https://")
rep("B-m13a","Journal of Financial Economics, 45(3), 365–390.","Journal of Financial Economics, 45(3), 365–390. https://doi.org/10.1016/S0304-405X(97)00021-4")
rep("B-m13b","The Journal of Finance, 67(2), 719–760.","The Journal of Finance, 67(2), 719–760. https://doi.org/10.1111/j.1540-6261.2012.01729.x")
rep("B-m13c","Review of International Economics, 28(1), 62–81.","Review of International Economics, 28(1), 62–81. https://doi.org/10.1111/roie.12441")
rep("B-m13d","Urban Studies, 49(6), 1275–1296.","Urban Studies, 49(6), 1275–1296. https://doi.org/10.1177/0042098011408143")
rep("B-m14a","Wardle, M., & Mainelli, M. (2026). The Global Financial Centres Index 40. Z/Yen Group & China Development Institute.",
 "Wardle, M., & Mainelli, M. (2026, September). The Global Financial Centres Index 40. Z/Yen Group & China Development Institute. https://www.longfinance.net/media/documents/GFCI_40_Report_2026.09.16_v1.2.pdf")
rep("B-m14b","FTSE Russell. (2026). Reclassification","FTSE Russell. (2026, August). Reclassification")
rep("B-m15","4138–4156. [CẦN XÁC MINH]","4138–4156. [CẦN XÁC MINH tập, số và trang]")
rep("B-m16","nền tảng khoa học mở OSF_PLACEHOLDER","x")  # placeholder bỏ dưới
E.pop()
rep("B-m16","Open Science Framework","nền tảng khoa học mở (Open Science Framework)")
# độ khớp
rep("F-item6","gửi Sở Khoa học và Công nghệ Hà Nội trong năm thứ tư.",
 "gửi Sở Khoa học và Công nghệ Hà Nội trong năm thứ tư, kèm văn bản xác nhận nhu cầu sử dụng kết quả của ít nhất một đơn vị, ưu tiên HNX, đơn vị tiếp tục vận hành thị trường trái phiếu và chứng khoán phái sinh tại Hà Nội.")
rep("F-art15","Ở cả hai hướng, thí sinh có thể duy trì Chỉ số chất lượng thị trường vốn cùng người dùng thực tế.",
 "Ở cả hai hướng, thí sinh có thể duy trì Chỉ số chất lượng thị trường vốn cùng người dùng thực tế. Thí sinh sẵn sàng thực hiện nghĩa vụ tại điểm e khoản 2 Điều 15 Nghị quyết số 57/2026/NQ-HĐND: tham gia mạng lưới chuyên gia của Thành phố và cung cấp luận cứ khoa học cho bài toán số 19 khi được mời (Hội đồng nhân dân thành phố Hà Nội, 2026).")
# tách đoạn (A-m7)
for k,a in enumerate(["Hệ số tương tác cho biết tác động thay đổi thế nào","Sai số chuẩn phân cụm theo cổ phiếu và suy luận hoán vị",
 "Vì vậy nhóm đối chứng HOSE loại các mã","Ngoài ra, Ủy ban Chứng khoán Nhà nước cho biết","Đề tài vì vậy tính Amihud, ở cả hai nhóm và cả hai giai đoạn",
 "Ngày cổ phiếu bị đình chỉ giao dịch bị loại","Giai đoạn căng thẳng chỉ dùng cho phân tích mô tả","Chẳng hạn, với σ = 0,2 và φ = 0,6",
 "Đề tài có bốn mục tiêu cụ thể.","Trong bốn giả thuyết, H3 là kiểm định trọng tâm","Đề tài dùng hai cấu hình chi phí.",
 "Vì số cửa sổ ít và lợi suất tương đương chắc chắn có phương sai lớn","Giữ nguyên thành phần rổ giúp so sánh","Chênh lệch này không đo lượng thanh khoản"]):
    split(f"SPL{k}",a)
json.dump(E,open('../r10/edits-r11.json','w',encoding='utf-8'),ensure_ascii=False,indent=1); print(len(E))
