# Tra cứu bộ quy tắc

Đọc đầy đủ các phần dưới đây khi áp dụng skill. Toàn văn bản người dùng cung cấp được giữ nguyên sau mục lục.

- [I. MỤC TIÊU VÀ NGUYÊN TẮC TỐI CAO](#i-mục-tiêu-và-nguyên-tắc-tối-cao)
- [II. NHÓM CẤM TUYỆT ĐỐI: MỨC 0](#ii-nhóm-cấm-tuyệt-đối-mức-0)
- [III. NHÓM CẤM NGÔN NGỮ: MỨC 1](#iii-nhóm-cấm-ngôn-ngữ-mức-1)
- [IV. NHÓM CẤM HÌNH THỨC VÀ DẤU CÂU](#iv-nhóm-cấm-hình-thức-và-dấu-câu)
- [V. NHÓM QUY TẮC BẮT BUỘC VỀ CẤU TRÚC CÂU](#v-nhóm-quy-tắc-bắt-buộc-về-cấu-trúc-câu)
- [VI. NHÓM QUY TẮC BẮT BUỘC VỀ TỪ VỰNG](#vi-nhóm-quy-tắc-bắt-buộc-về-từ-vựng)
- [VII. NHÓM QUY TẮC VỀ NỘI DUNG VÀ GIỌNG VĂN](#vii-nhóm-quy-tắc-về-nội-dung-và-giọng-văn)
- [VIII. KIỂM SOÁT VĂN BẢN THEO VỊ TRÍ](#viii-kiểm-soát-văn-bản-theo-vị-trí)
- [IX. NGƯỠNG KIỂM TRA VÀ PHÂN LOẠI LỖI](#ix-ngưỡng-kiểm-tra-và-phân-loại-lỗi)
- [X. QUY TRÌNH BIÊN TẬP BẮT BUỘC](#x-quy-trình-biên-tập-bắt-buộc)
- [XI. ĐIỀU KIỆN CHẤP NHẬN BẢN CUỐI](#xi-điều-kiện-chấp-nhận-bản-cuối)
- [XII. QUY ĐỊNH ĐẦU RA](#xii-quy-định-đầu-ra)

# MASTER WRITING RULES
## BỘ QUY TẮC VIẾT VĂN NGHIÊM NGẶT

### I. MỤC TIÊU VÀ NGUYÊN TẮC TỐI CAO

Tạo ra văn bản chính xác, tự nhiên, giàu thông tin, có giọng điệu phù hợp và không mang những công thức diễn đạt rập khuôn thường gặp trong văn bản AI.

Mỗi câu phải có lý do tồn tại. Mỗi đoạn phải có chức năng rõ ràng. Mỗi nhận định phải được hỗ trợ bằng thông tin, suy luận có căn cứ hoặc dụng ý nghệ thuật cụ thể.

Không đánh đổi tính chính xác, ý nghĩa, cảm xúc hoặc chất lượng văn bản để tối ưu một chỉ số thống kê.

Không được tuyên bố rằng một văn bản chắc chắn do con người viết chỉ vì đã tuân thủ các quy tắc này.

**Thứ tự ưu tiên bắt buộc:**

1. Giữ đúng yêu cầu và nội dung gốc.
2. Bảo đảm tính chính xác và nhất quán.
3. Tuân thủ đặc điểm của thể loại văn bản.
4. Bảo đảm câu văn rõ nghĩa, tự nhiên và có cá tính.
5. Loại bỏ các công thức ngôn ngữ sáo rỗng.
6. Kiểm tra dấu câu, bố cục và định dạng.
7. Đánh giá các chỉ số ngôn ngữ nếu có đủ dữ liệu.

Khi hai quy tắc xung đột, áp dụng quy tắc có thứ tự ưu tiên cao hơn.

---

### II. NHÓM CẤM TUYỆT ĐỐI: MỨC 0

Đây là các lỗi không được phép xuất hiện trong bản cuối.

**R01. Cấm bịa thông tin.**

Không bịa sự kiện, dữ liệu, tên riêng, chức danh, nghiên cứu, nguồn tham khảo, trích dẫn hoặc những chi tiết được trình bày như sự thật.

**R02. Cấm ngụy tạo độ tin cậy.**

Không viết "theo các chuyên gia", "nhiều nguồn xác nhận", "giới nghiên cứu nhận định" nếu không có nguồn xác định.

Không biến một nguồn đơn lẻ thành sự đồng thuận của nhiều nguồn.

**R03. Cấm phóng đại thiếu căn cứ.**

Không tự ý nâng quy mô hoặc ý nghĩa của sự kiện. Những khái niệm như "lịch sử", "đột phá", "vượt trội", "toàn diện" và "sâu rộng" chỉ được dùng khi có căn cứ rõ ràng.

**R04. Cấm dấu vết hệ thống AI.**

Không để lộ mã trích dẫn nội bộ, metadata, token hệ thống, tên công cụ, placeholder, chú thích nội bộ hoặc dấu định dạng chưa xử lý.

**R05. Cấm lời giao tiếp của chatbot trong nội dung.**

Không viết "Chắc chắn rồi", "Dưới đây là", "Tôi đã chỉnh sửa", "Hy vọng nội dung hữu ích" hoặc "Nếu bạn muốn tôi có thể" khi đầu ra được yêu cầu là một văn bản độc lập.

**R06. Cấm thay đổi dữ kiện để cải thiện văn phong.**

Không sửa sai số liệu, ý định của người nói, quan hệ nhân quả, thứ tự thời gian hoặc đặc điểm của nhân vật.

**R07. Cấm tạo ra nội dung không có chức năng.**

Không thêm câu chỉ để tăng độ dài, làm đầy đoạn, bổ sung từ khóa hoặc cải thiện các chỉ số.

**R08. Cấm cố tình tạo lỗi để giả lập giọng văn con người.**

Không cố tình viết sai chính tả, ngữ pháp, dấu câu hoặc logic.

---

### III. NHÓM CẤM NGÔN NGỮ: MỨC 1

Các lỗi sau phải được loại bỏ trong văn xuôi mặc định, trừ khi người dùng yêu cầu hoặc ngữ cảnh có lý do rõ ràng.

**R09. Cấm sáo ngữ trừu tượng.**

Không mặc định dùng:

- Khẳng định vị thế.
- Đóng vai trò then chốt.
- Mang ý nghĩa sâu sắc.
- Phản ánh rõ nét.
- Minh chứng cho.
- Tạo dấu ấn.
- Bước ngoặt lịch sử.
- Tầm ảnh hưởng sâu rộng.
- Phát triển không ngừng.
- Bức tranh toàn cảnh.
- Bức tranh đa chiều.
- Sự giao thoa.
- Hành trình khám phá.
- Di sản trường tồn.
- Sức mạnh vượt trội.
- Giá trị cốt lõi.
- Nền tảng vững chắc.
- Mở ra kỷ nguyên mới.
- Những thách thức và cơ hội.
- Triển vọng đầy hứa hẹn.
- Tạo nên một tương lai tốt đẹp.

Khi bắt gặp những cụm trên, ưu tiên thay bằng sự kiện, hành động, con số hoặc nhận định cụ thể.

Không thay một sáo ngữ bằng một sáo ngữ đồng nghĩa.

**R10. Cấm dùng tính từ để thay bằng chứng.**

Không viết "đặc biệt", "vĩ đại", "mạnh mẽ", "đáng kinh ngạc" hoặc "đáng chú ý" nếu không thể giải thích điều gì khiến đối tượng có đặc điểm đó.

**R11. Cấm từ nối tự động.**

Không dùng "ngoài ra", "bên cạnh đó", "hơn nữa", "tuy nhiên", "mặt khác", "do đó", "nhìn chung", "tóm lại" chỉ để bắt đầu câu hoặc nối hai đoạn.

Từ nối phải làm rõ một quan hệ logic có thật.

**R12. Cấm công thức đối lập phủ định.**

Không mặc định sử dụng:

- Không chỉ X mà còn Y.
- Không phải X mà là Y.
- Không đơn thuần là X.
- Không dừng lại ở X.
- Đây không chỉ là X.
- X không còn là Y.
- X thay vì Y.

Phải phát biểu trực tiếp nội dung muốn nói.

**R13. Cấm lạm dụng quy tắc bộ ba.**

Không tự động đưa ra ba yếu tố, ba luận điểm hoặc ba tính từ.

Số lượng ý phải phụ thuộc vào thông tin thực tế.

**R14. Cấm động từ vòng vo.**

Ưu tiên động từ trực tiếp. Không tự động chuyển "là", "có", "nói", "làm", "xây", "mua", "bán", "chỉ huy", "quyết định" thành những cụm từ trang trọng và dài hơn.

**R15. Cấm che giấu quan hệ thực tế.**

Không thay "ông chỉ huy quân đội" bằng "ông có mối liên hệ với công tác quân sự".

Chủ thể, hành động và quan hệ giữa các đối tượng phải được xác định rõ khi thông tin cho phép.

**R16. Cấm phân tích nông dưới hình thức sâu sắc.**

Không thêm một mệnh đề về ý nghĩa, giá trị, di sản hoặc xu hướng xã hội nếu mệnh đề đó không mang thêm thông tin hay lập luận.

**R17. Cấm nhận định kết thúc giả tạo.**

Không mặc định kết thúc một đoạn bằng thông điệp triết lý, bài học đạo đức hoặc lời ca ngợi.

**R18. Cấm cân bằng quan điểm máy móc.**

Không bắt buộc trình bày hai mặt ngang nhau nếu bằng chứng không tương xứng.

Không tạo ý kiến phản đối chỉ để văn bản có vẻ đa chiều.

**R19. Cấm giải thích lại điều vừa nói.**

Không thêm câu diễn giải mang cùng thông tin nếu nó không cải thiện độ rõ nghĩa hoặc phục vụ dụng ý nghệ thuật.

**R20. Cấm thay từ đồng nghĩa không cần thiết.**

Giữ nguyên thuật ngữ, tên riêng và cách gọi nhất quán khi điều đó giúp câu văn rõ hơn.

Không thay đổi từ chỉ nhằm tránh lặp một cách tuyệt đối.

---

### IV. NHÓM CẤM HÌNH THỨC VÀ DẤU CÂU

**R21. Không dùng em dash như dấu câu mặc định.**

Không sử dụng "—" để tạo nhịp kịch tính, chen lời giải thích hoặc nối hai nhận định.

Ưu tiên dấu phẩy, dấu chấm, dấu hai chấm hoặc viết lại câu.

**R22. Không dùng ngoặc kép cong trong văn bản mặc định.**

Ưu tiên dấu ngoặc kép thẳng " ".

Giữ nguyên ký tự đặc biệt nếu thuộc nguyên văn cần trích hoặc định dạng được yêu cầu.

**R23. Không trang trí văn bản bằng ký hiệu thừa.**

Không tự động thêm emoji, nhiều dấu chấm than, dấu ba chấm, đường phân cách hoặc biểu tượng.

**R24. Không lạm dụng in đậm.**

Chỉ in đậm khi cấu trúc tài liệu hoặc mục đích đọc thực sự yêu cầu.

Không sử dụng chữ in đậm để tạo cảm giác mọi ý đều quan trọng.

**R25. Không tự động chuyển văn xuôi thành danh sách.**

Một đoạn có quan hệ logic liên tục phải được trình bày bằng văn xuôi khi cách đó giúp người đọc hiểu tốt hơn.

**R26. Không áp đặt cùng một bố cục lên mọi bài.**

Không mặc định tạo các mục "Tổng quan", "Bối cảnh", "Vai trò", "Thách thức", "Triển vọng" và "Kết luận".

**R27. Không dùng câu mở đầu và kết thúc theo mẫu.**

Không mở bài bằng nhận xét phổ quát không có thông tin. Không kết bài bằng tuyên bố về tương lai khi không có căn cứ.

**R28. Không lạm dụng bảng.**

Chỉ dùng bảng khi cần đối chiếu nhiều thuộc tính hoặc làm rõ dữ liệu.

---

### V. NHÓM QUY TẮC BẮT BUỘC VỀ CẤU TRÚC CÂU

**R29. Độ dài câu phải biến thiên theo nội dung.**

Phải có câu ngắn, câu trung bình và câu dài khi thể loại cho phép.

Không duy trì một nhịp câu đều đặn xuyên suốt văn bản.

**R30. Câu ngắn phải xuất hiện tự nhiên.**

Với văn xuôi từ 20 câu trở lên, mục tiêu biên tập là ít nhất 8% câu có không quá 10 từ.

Đây là ngưỡng hiệu đính tự đặt, không phải ngưỡng phân loại AI được chứng minh.

Không tạo câu ngắn nếu câu đó không có chức năng rõ ràng.

**R31. Giới hạn câu quá dài.**

Với văn xuôi từ 20 câu trở lên, mục tiêu là không quá 15% câu có từ 41 từ trở lên.

Không sử dụng nhiều câu rất dài liên tục nếu làm giảm khả năng theo dõi.

Có thể vượt ngưỡng khi thể loại, ý nghĩa hoặc cấu trúc cú pháp đòi hỏi.

**R32. Không đặt mục tiêu cho độ dài câu trung bình.**

Không cố viết mỗi câu khoảng 30 từ.

Phải đánh giá phân bố và biến thiên, không chỉ trung bình.

**R33. Kiểm soát độ biến thiên.**

Với văn bản đủ dài, tính:

CV = độ lệch chuẩn độ dài câu / độ dài câu trung bình.

Nếu CV thấp hơn 0,50, phải kiểm tra nguy cơ câu văn quá đều.

Không bắt buộc sửa nếu sự đều đặn phục vụ thể loại hoặc mục đích rõ ràng.

Không thao túng câu chữ chỉ để đạt CV.

**R34. Kiểm soát burstiness đúng phương pháp.**

Chỉ so sánh burstiness khi các văn bản dùng cùng một công thức và cùng cách tách từ, tách câu.

Không lấy một giá trị burstiness đơn lẻ làm bằng chứng xác định nguồn gốc văn bản.

**R35. Không lặp cấu trúc cú pháp liên tục.**

Kiểm tra những câu có cùng mô hình:

- Chủ thể + hành động + nhận định ý nghĩa.
- Mệnh đề dẫn nhập + sự kiện + kết luận.
- Nhận định chung + ví dụ + thông điệp.
- Phủ định X + khẳng định Y.

Nếu các cấu trúc lặp không có dụng ý, phải tổ chức lại cách trình bày.

**R36. Không bắt buộc đoạn văn có độ dài cố định.**

Số câu trong mỗi đoạn phải tùy thuộc nội dung.

Không đều đặn tạo các đoạn có cùng số câu và cùng nhịp kết thúc.

---

### VI. NHÓM QUY TẮC BẮT BUỘC VỀ TỪ VỰNG

**R37. Ưu tiên từ chính xác hơn từ phức tạp.**

Không chọn từ dài hoặc hiếm chỉ vì nghe trang trọng.

Giữ lại từ chuyên ngành khi nó là cách diễn đạt chính xác nhất.

**R38. Không tối đa hóa sự đa dạng từ vựng.**

Không tránh mọi sự lặp từ.

Sử dụng lại từ khi việc đó giữ được tính nhất quán của chủ đề hoặc nhân vật.

**R39. Kiểm tra lặp 3-gram theo chức năng.**

Không cố giảm tỷ lệ lặp 3-gram xuống mức thấp nhất.

Không chủ động tăng tỷ lệ bằng sự lặp vô nghĩa.

Loại bỏ việc lặp lại cùng một thông tin mà không bổ sung ý nghĩa.

Giữ sự lặp cần thiết cho thuật ngữ, tên riêng hoặc nghệ thuật.

**R40. Diễn giải đúng Yule's K.**

Yule's K cao thường tương ứng với độ tập trung từ lớn hơn và độ đa dạng từ vựng thấp hơn theo phép đo này.

Không dùng Yule's K cao làm bằng chứng rằng từ vựng phong phú hơn.

Không đặt ngưỡng Yule's K cố định nếu không có tập dữ liệu đối chứng phù hợp.

**R41. Không ép tỷ lệ từ chức năng.**

Không cố điều chỉnh từ chức năng về một tỷ lệ chính xác.

Duy trì đầy đủ những thành phần ngữ pháp cần thiết.

**R42. Không ép độ dài từ.**

Không cố nâng số ký tự trung bình trên mỗi từ.

Không loại bỏ từ dài nếu từ đó cần thiết.

Không đồng nhất số ký tự với độ hoa mỹ.

**R43. Không lặp từ mở đầu theo khuôn.**

Không để nhiều đoạn liên tiếp bắt đầu bằng cùng một mẫu dẫn nhập.

Đánh giá sự lặp về chức năng và cảm giác đọc, không chỉ xét một từ đơn lẻ.

---

### VII. NHÓM QUY TẮC VỀ NỘI DUNG VÀ GIỌNG VĂN

**R44. Ưu tiên thông tin cụ thể.**

Khi có thể, xác định rõ người thực hiện, hành động, đối tượng, thời gian, địa điểm, nguyên nhân và hệ quả.

Không thêm chi tiết chưa xác minh chỉ để tăng tính cụ thể.

**R45. Mọi luận điểm phải có chức năng.**

Một nhận định phải được giải thích, chứng minh hoặc phát triển bằng lập luận.

Không sử dụng nhiều câu trừu tượng để tạo ấn tượng đang phân tích chuyên sâu.

**R46. Giọng văn phải phù hợp thể loại.**

- Văn học: ưu tiên nhân vật, hành động, cảm xúc, hình ảnh và nhịp kể.
- Phân tích: ưu tiên luận điểm, bằng chứng, phản biện và kết luận có căn cứ.
- Lịch sử: ưu tiên sự kiện, thời điểm, quan hệ nhân quả và nguồn.
- Khoa học: ưu tiên khái niệm chính xác, phương pháp, dữ liệu và giới hạn kết luận.
- Báo chí: ưu tiên thông tin kiểm chứng được, sự kiện và nguồn.
- Lời thoại: ưu tiên cá tính, hoàn cảnh, mục đích giao tiếp và cách nói tự nhiên.

Không dùng một kiểu văn phong chung cho tất cả.

**R47. Cho phép khác biệt có chủ đích.**

Không xóa những nét riêng hợp lý của người kể hoặc tác giả để tạo văn bản trơn tru tuyệt đối.

Không coi mọi cách dùng từ bất thường là lỗi.

**R48. Không ép tính tự nhiên bằng cảm xúc giả.**

Không thêm sự xúc động, hài hước, mỉa mai hoặc triết lý nếu nội dung không cần.

Không tự động làm một cảnh buồn trở nên bi thương hơn hoặc một sự kiện bình thường trở nên hùng tráng.

**R49. Không biến mọi đoạn thành kết luận.**

Các đoạn có thể lần lượt trình bày hành động, sự kiện, quan sát, chứng cứ và suy luận.

Không yêu cầu đoạn nào cũng phải kết bằng một câu khẳng định ý nghĩa.

---

### VIII. KIỂM SOÁT VĂN BẢN THEO VỊ TRÍ

**R50. Kiểm tra nhịp ở đầu văn bản.**

Phần mở đầu phải tiếp cận nội dung theo cách phù hợp, không nhất thiết đi từ khái niệm lớn đến vấn đề nhỏ.

Không tạo câu mở đầu quá dài chỉ để cung cấp mọi thông tin cùng lúc.

**R51. Kiểm tra nhịp ở phần giữa.**

Không duy trì các đoạn có cấu trúc giống hệt nhau.

Không bắt buộc mỗi đoạn có một câu chủ đề, ba câu triển khai và một câu tổng kết.

**R52. Kiểm tra nhịp ở phần cuối.**

Không tự động kéo dài câu để tổng hợp tất cả ý trước đó.

Không kết thúc bằng bài học, lời khuyên, nhận định về tương lai hoặc câu hỏi gợi mở nếu chúng không phục vụ mục đích viết.

**R53. Kiểm tra sự biến thiên trên toàn văn bản.**

Với văn bản dài, chia thành năm phần và quan sát độ dài câu, tỷ lệ câu ngắn, cách mở đầu và hình thức kết đoạn.

Nếu các phần giống nhau bất thường, kiểm tra lại cấu trúc nội dung.

Không buộc từng phần phải có thống kê khác nhau bằng mọi giá.

---

### IX. NGƯỠNG KIỂM TRA VÀ PHÂN LOẠI LỖI

**Lỗi nghiêm trọng: bắt buộc sửa.**

- Thông tin bịa hoặc sai lệch.
- Nguồn tham khảo không tồn tại hoặc không hỗ trợ nội dung.
- Mã AI, placeholder hoặc lời dẫn chatbot bị lộ.
- Mệnh đề khẳng định mạnh nhưng không có căn cứ.
- Nội dung tự mâu thuẫn.
- Thay đổi ý nghĩa ngoài yêu cầu.

**Lỗi văn phong: bắt buộc rà soát và sửa khi không có lý do giữ lại.**

- Sáo ngữ.
- Cấu trúc đối lập giả.
- Từ nối rập khuôn.
- Phóng đại.
- Thay từ đồng nghĩa không cần thiết.
- Câu tổng kết rỗng.
- Bố cục theo mẫu.
- Dấu câu và định dạng trang trí.
- Giọng văn không phù hợp.

**Chỉ số thống kê: dùng để phát hiện vấn đề cần kiểm tra.**

Với văn xuôi từ 20 câu trở lên:

| Chỉ số | Ngưỡng hiệu đính đề xuất | Xử lý |
|---|---|---|
| Câu rất ngắn, tối đa 10 từ | Ít nhất 8% | Kiểm tra nếu thấp hơn |
| Câu dài, từ 41 từ | Không quá 15% | Kiểm tra nếu cao hơn |
| CV độ dài câu | Từ 0,50 trở lên | Kiểm tra nếu thấp hơn |
| Độ dài câu trung bình | Không đặt ngưỡng | Xem phân bố |
| 3-gram lặp lại | Không đặt ngưỡng | Đánh giá chức năng lặp |
| Yule's K | Không đặt ngưỡng | So sánh cùng phương pháp |
| Tỷ lệ từ chức năng | Không đặt ngưỡng | Ưu tiên đúng ngữ pháp |
| Độ dài từ | Không đặt ngưỡng | Ưu tiên từ chính xác |
| Burstiness | Không đặt ngưỡng chung | Chỉ so sánh cùng công thức |

Các ngưỡng trong bảng là chuẩn hiệu đính nội bộ, không phải tiêu chuẩn khoa học để phân loại tác giả.

Ngưỡng thống kê chỉ được áp dụng khi cách tính rõ ràng và thể loại phù hợp.

Không tự khẳng định đã tính hoặc đạt một chỉ số nếu chưa thực sự đo được.

---

### X. QUY TRÌNH BIÊN TẬP BẮT BUỘC

**Vòng 1. Kiểm tra nội dung**

Đối chiếu văn bản với yêu cầu ban đầu.

Kiểm tra dữ kiện, logic, nhân vật, thông tin, quan hệ nhân quả và mục đích viết.

Loại bỏ mọi thông tin chưa được xác minh nhưng lại được trình bày như sự thật.

**Vòng 2. Kiểm tra ngôn ngữ**

Tìm tất cả từ sáo rỗng, cụm phóng đại, nhận định trừu tượng và động từ vòng vo.

Sửa bằng cách làm rõ thông tin, không chỉ thay bằng từ đồng nghĩa.

**Vòng 3. Kiểm tra cấu trúc**

Tìm những câu có cấu trúc đối lập giả, những đoạn lặp khuôn, những câu kết không có thông tin và những chỗ chuyển ý máy móc.

Sắp xếp lại mạch lập luận nếu cần.

**Vòng 4. Kiểm tra nhịp câu**

Đọc liên tục và quan sát:

- Câu có cùng độ dài xuất hiện liên tiếp hay không.
- Câu rất ngắn có chức năng rõ ràng hay không.
- Câu dài có thật sự cần thiết hay không.
- Các đoạn có quá đồng đều hay không.
- Phần kết có bị kéo dài hoặc tổng kết rập khuôn hay không.

Với văn bản đủ dài, thực hiện phép đo thống kê khi có công cụ.

**Vòng 5. Kiểm tra từ vựng**

Tìm sự thay đổi từ đồng nghĩa không cần thiết.

Kiểm tra các cụm từ và cấu trúc lặp lại.

Giữ nguyên những sự lặp giúp văn bản chính xác, nhất quán hoặc có giá trị nghệ thuật.

**Vòng 6. Kiểm tra hình thức**

Loại bỏ dấu câu trang trí, định dạng dư thừa, Markdown không đúng yêu cầu, ký hiệu lạ, placeholder và dấu vết chatbot.

Bảo đảm văn bản cuối phù hợp với định dạng người dùng yêu cầu.

**Vòng 7. Đọc lại như một tác phẩm hoàn chỉnh**

Không chỉ kiểm tra từng câu độc lập.

Đọc toàn văn để đánh giá tính liên tục của tư duy, sự chuyển tiếp giữa các đoạn, tính cách của người kể, nhịp điệu và tác dụng của đoạn kết.

Nếu văn bản trở nên gượng ép do áp dụng quá nhiều phép sửa, phải ưu tiên khôi phục cách diễn đạt tự nhiên và chính xác.

---

### XI. ĐIỀU KIỆN CHẤP NHẬN BẢN CUỐI

Chỉ chấp nhận bản thảo khi:

1. Không còn lỗi nghiêm trọng về dữ kiện hoặc logic.
2. Không còn dấu vết kỹ thuật hay lời dẫn chatbot ngoài yêu cầu.
3. Không có sự phóng đại thiếu căn cứ.
4. Không có các đoạn sáo rỗng dùng để thay thế thông tin.
5. Không lặp công thức câu một cách máy móc.
6. Nhịp câu phù hợp với nội dung và thể loại.
7. Các từ, thuật ngữ và tên gọi được sử dụng nhất quán.
8. Dấu câu và bố cục có chức năng thực sự.
9. Những chỉ số có thể đo đã được kiểm tra khi điều kiện cho phép.
10. Không có chỉnh sửa chỉ nhằm tối ưu thống kê nhưng làm giảm chất lượng.
11. Văn bản bảo toàn yêu cầu và sắc thái của người viết.
12. Mỗi đoạn đóng góp một giá trị cụ thể cho toàn bài.

Nếu có bất kỳ lỗi nghiêm trọng nào, phải sửa trước khi xuất bản.

Đối với lỗi văn phong, phải loại bỏ nếu không có dụng ý hoặc lý do ngữ cảnh đủ rõ để giữ lại.

---

### XII. QUY ĐỊNH ĐẦU RA

Khi được yêu cầu viết hoặc chỉnh sửa một văn bản, áp dụng bộ quy tắc này trong quá trình thực hiện.

Chỉ xuất ra sản phẩm cuối cùng theo đúng định dạng được yêu cầu.

Không tự thêm phần giới thiệu quá trình viết, danh sách những lỗi đã sửa, lời xin lỗi, lời bảo đảm chất lượng hoặc lời mời tiếp tục.

Không công bố những chỉ số thống kê chưa được tính toán thực tế.

Chỉ cung cấp báo cáo biên tập, phương pháp kiểm tra hoặc kết quả thống kê khi người dùng yêu cầu.

**NGUYÊN TẮC KẾT THÚC**

Viết điều cần nói, bằng cách diễn đạt chính xác và phù hợp nhất.

Không làm câu văn phức tạp hơn mức cần thiết.

Không dùng sự bóng bẩy thay cho thông tin.

Không dùng sự đều đặn thay cho cấu trúc.

Không dùng sự đa dạng giả tạo thay cho cá tính.

Không dùng chỉ số thống kê thay cho chất lượng viết.

Văn bản chỉ hoàn thành khi nội dung, logic, giọng điệu và hình thức cùng phục vụ mục đích của tác phẩm.
