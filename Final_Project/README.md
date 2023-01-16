
<h3 align="center" font-size= 14px;><b>Trường Đại Học Công Nghệ Thông Tin - ĐHQH TPHCM</b></h3>
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>
<h1 align="center"><b>Đồ án cuối kỳ môn Máy học - CS114.M11</b></h1>
<h2 align="center"><b>BÀI TOÁN NHẬN DIỆN BIỂN BÁO GIAO THÔNG TRONG KHU VỰC <br>THÀNH PHỐ HỒ CHÍ MINH
 </br></h2>


### Giảng viên hướng dẫn

Họ tên | Email
--- | --- 
PGS.TS. Lê Đình Duy | duyld@uit.edu.vn
Ths. Phạm Nguyễn Trường An | truonganpn@uit.edu.vn

### Tên nhóm: LHH
### Các thành viên của nhóm
Họ tên | MSSV | Email | GitHub
--- | --- | -- | --
Nguyễn Minh Lý | 20521592 | 20521592@gm.uit.edu.vn | https://github.com/lynguyenminh
Nguyễn Đặng Nhật Hào | 20520490 | 20520490@gm.uit.deu.vn | https://github.com/cauhamau
Nguyễn Hồng Hậu | 20521300 | 20521300@gm.uit.edu.vn | https://github.com/Nguyen-Hong-Hau
</p>

<a name="phancong"></a>
**Phân công công việc**
Công Việc | Lý | Hào | Hậu
:---| :---| :---| :---
Quay vieo làm data |  | &#9745; |   
Label dữ liệu | &#9745; | &#9745; | &#9745;
Tìm hiểu và train YOLOv4 | &#9745; | &#9745; |   
Tìm hiểu và train YOLOv5 | &#9745; |  | &#9745;  
Đánh giá file weights | &#9745; | &#9745; |   
Hoàn thành nội dung báo cáo | &#9745; |  | &#9745;  
Chỉnh sửa format báo cáo |  |  | &#9745; 
Demo mô hình | &#9745; | &#9745; |   


# **BẢNG MỤC LỤC**
1. [Giải Trình Sau Vấn Đáp](#giaitrinh)
2. [Tổng Quan Về Đồ Án](#tongquan)
3. [Xây Dựng Bộ Dữ Liệu](#dulieu)
4. [Training Và Đánh Giá Model](#training)
5. [Hướng Phát Triển Và Cải Tiến](#ungdung)
6. [Demo mô hình](#demo)
7. [Nguồn Tham Khảo](#thamkhao)

<a name="giaitrinh"></a>
# **1. Giải Trình Sau Vấn Đáp**

[Phân công công việc.](#phancong)

[Minh chứng cho YOLO nhanh hơn RCNN.](#yolonhanh)

[Cách đánh giá FPS.](#danhgiafps)

[Phân tích những class có precall, precision thấp và đưa ra lý do.](#phantich)


<a name="tongquan"></a>
# **2. Tổng Quan Về Đồ Án**

## **2.1. Ngữ cảnh ứng dụng**
  * Ở Việt Nam, giao thông đường bộ là loại hình giao thông phổ biến và phát triển nhất. Tính đến năm 2019, tổng số xe máy đăng kí của Việt Nam là khoảng 62 triệu chiếc. Với sự gia tăng số lượng phương tiện nhanh chóng, hệ thống đường xá cũng ngày càng tiên tiến, hiện đại. Bên cạnh những mặt tích cực đó, vẫn tồn tại nhiều khía cạnh tiêu cực - vi phạm luật giao thông. Khi tham gia giao thông, đôi lúc vì quá chú tâm vào phương tiện trên đường mà quên mất sự có mặt của những biển báo. Chính những thiếu sót đó có thể bị phạt hoặc nguy hiểm hơn là dẫn đến tai nạn không mong muốn. Để khắc phục vấn đề này, chúng em đề xuất một mô hình máy học nhận diện biển báo ngay trong lúc tham gia giao thông.
  * Khu vực được lựa chọn để thu thập data và đánh giá thực nghiệm là Thành phố Hồ Chí Minh. 
  * Đối tượng sử dụng là người điều khiển xe máy, có trang bị:

    *	Điện thoại di động, ảnh chụp từ điện thoại có kích thước 1920x1080.

    *	Giá đỡ điện thoại gắn trên xe máy (như hình).

    
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/gia%20do%201.jpg?raw=true "Giá đỡ điện thoại")
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/gia%20do%202.jpg?raw=true "Giá đỡ điện thoại")

    Hình 2.1.  Cách đặt điện thoại trên giá đỡ phù hợp.
## **2.2. INPUT và OUTPUT Bài toán**
  * INPUT: 
    * Video được quay từ camera điện thoại gắn trên giá đỡ.
    
  * OUTPUT: 
    * Video với các thông tin:
      * Bbox bao quanh các biển báo của biển báo.
      * Tên biển báo.

      
      


<a name="dulieu"></a>
# **3.Xây Dựng Bộ Dữ Liệu**
## **3.1. Thu thập dữ liệu**
### **3.1.1. Thông tin thu thập dữ liệu**


*	Cách thức thu thập: Sử dụng điện thoại quay video trong quá trình chạy xe. Tốc độ xe ở mức 30-40 km/h (ở khu vực cho phép). Sau đó cắt những ảnh từ video ra để làm data.

*	Ảnh được chụp trên thiết bị điện thoại: Poco x3 pro.

*	Có thu thập data vào ban ngày, chiều tối.

*	Các lần thu thập dữ liệu

Lần thu thập | Ngày thu thập | Số lượng video | Số lượng ảnh sau khi lọc | Mục đích
--- | --- | -- | -- | --
1 | 29/12/2021 | 91 | 874 | Train & val
2 | 6/1/2022 | 49 | 877 | Train & val
3 | 15/1/2022 | 17 | Không cắt thành ảnh | Test   

Bảng 3.1.1.  Thông tin các đợt thu thập dữ liệu.


### **3.1.2. Công cụ label dữ liệu**
  * [LabelImg](https://github.com/tzutalin/labelImg). Lý do chúng em chọn LabelImg để label: 
    * Giao diện khá tốt với đầy đủ chức năng: open, load, aotusave,….
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/label%20img.png?raw=true "")
    * Định dạng của nhãn phù hợp để dùng YOLO train.
    * Dễ cài đặt.

  * Quy tắc khi label: 
    *	Label bounding box ôm gọn biển báo, tránh label rộng hơn, hay không label hết phần biển báo.
    *	Label những biển báo cách vị trí xe từ 0- 20m. Vì khi nhận diện để thông báo cho người tham gia giao thông, ta cần nhận diện và thông báo trước khi đi qua biển báo đó, để người đi điều chỉnh tốc độ hay chú ý hơn.
    *	Đối với những biển báo bị mất hơn 40% diện tích, thì sẽ bỏ qua. Lí do là ảnh đó có thể đánh mất một số features quan trọng, có thể làm cho model học sai.
    *	Đối với những biển báo có thời gian, cần label phần biển báo và khoảng thời gian áp dụng lên biển đó.
 
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/bb%20c%C3%B3%20thoi%20gian.png?raw=true 'label thời gian')


  * Đối với mỗi ảnh sau khi gán nhãn, sẽ tạo ra 1 file txt. Gọi là file annotation.
    


Hình 3.1.2.3. Ảnh và file annotation tương ứng.     

* Với w, h là khoảng cách từ tâm bounding box đến cạnh bên trái và vạnh bên trên của bức ảnh (như trong hình vẽ trên), các thành phần của 1 file annotaion như sau:      
  * Mỗi dòng là thông tin của 1 bounding box:
  * id: Thứ tự của class do mình định nghĩa.
  * Center: Là tọa độ tâm của bounding box (X_center, Y_center).Tính như sau:

   

![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/center.png?raw=true)  
  * Width, Height là chiều dài của bounding box theo chiều ngang và chiều cao của bức ảnh.

### **3.1.3. Kết quả thu thập dữ liệu**
Sau 2 lần thu thập data đầu tiên, có tất cả 1751 ảnh, thuộc vào 70 class. Nhưng do có những class số lượng ảnh dưới 15, những ảnh label không đúng quy tắc ban đầu đề ra nên chúng em tiến hành loại bỏ. Sau cùng thu được 1448 ảnh thuộc 50 class bên dưới:

ID | Tên biển báo | Hình ảnh |  | ID | Tên biển báo | Hình ảnh
--- | --- | -- | -- | -- | --- | ---
0 | Cấm rẽ trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20re%20trai.png?raw=true "") |  | 25 | Cấm dừng và đỗ xe từ 6-20h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20dung%20va%20do%20xe%206-20.png?raw=true '')
1 | Cấm sử dụng còi | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20su%20dung%20coi.png?raw=true "") |  | 26 | Trọng lượng tối đa 10T | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/trong%20luong%20toi%20da%2010t.png?raw=true '')
2 | Đi thẳng | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/di%20thang.png?raw=true "") |  | 27 | Cấm đỗ xe từ 9-16h và 19h-6h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe%209-16-19-6.png?raw=true '')
3 | Đường bị hẹp bên phải | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20bi%20hep%20ben%20phia.png?raw=true "") |  | 28 | Cấm xe tải 2.5T từ 6-9g và 16-22h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20xe%20tai%202.5t%20t%E1%BB%AB%206-9%2019-22.png?raw=true '')
4 | Đường bị hẹp bên trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20bi%20hep%20ben%20trai.png?raw=true "") |  | 29 | Cấm đỗ xe 6-9h và 16-21h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe%206-9%2016-21.png?raw=true '')
5 | Rẽ trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/re%20trai.png?raw=true "") |  | 30 | Bắt buộc rẽ trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/bat%20buoc%20re%20trai.png?raw=true '')
6 | Trẻ em | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/tre%20em.png?raw=true "") |  | 31 | Đường 1 chiều đi thẳng | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%201%20chieu%20di%20thang.png?raw=true '')
7 | Đường đi bộ sang ngang | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20di%20bo%20sang%20ngang.png?raw=true "") |  | 32 | Lane đi thẳng | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/lane%20di%20thang.png?raw=true '')
8 | Rẽ phải | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/re%20phai.png?raw=true "") |  | 33 | Cấm quay đầu | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20quay%20dau.png?raw=true '')
9 | Chỗ quay xe | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cho%20quay%20xe.png?raw=true "") |  | 34 | Đi chậm | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/di%20cham.png?raw=true '')
10 | Đường đi bộ cắt ngang | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20di%20bo%20cat%20ngang.png?raw=true "") |  | 35 | Cấm ô tô | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20oto.png?raw=true '')
11 | Tốc độ tối đa 60km/h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/toc%20do%20toi%20da%2060.png?raw=true "") |  | 36 | Cấm ô tô rẽ trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20o%20to%20re%20trai.png?raw=true '')
12 | Chỗ ngoặc vòng bên trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cho%20ngoac%20vong%20ben%20trai.png?raw=true "") |  | 37 | Cấp điện phía trên | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cap%20dien%20phia%20tren.png?raw=true '')
13 | Nơi giao nhau chạy theo vòng xuyến | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/noi%20giao%20nhau%20theo%20vong%20xuyen.png?raw=true "") |  | 38 | Cấm xe mô tô và 3 bánh loại có động cơ | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20xe%20moto%20va%203%20banh%20co%20dong%20co.png?raw=true '')
14 | Cấm đô xe ngày lẻ | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe%20ngay%20le.png?raw=true "") |  | 39 | Giao nhau đường không ưu tiên | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/giao%20nhau%20duong%20khong%20uu%20tien.png?raw=true '')
15 | Chỗ ngoặc vòng bên phải | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cho%20ngoac%20vong%20ben%20phai.png?raw=true "") |  | 40 | Giao nhau với đường ưu tiên | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/giao%20nhau%20duong%20uu%20tien.png?raw=true '')
16 | Đường không bằng phẳng | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20khong%20bang%20phang.png?raw=true "") |  | 41 | Nhiều chỗ ngoặc nguy hiểm liên tiếp | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/nhieu%20cho%20ngoac%20nguy%20hiem%20lien%20tiep.png?raw=true '')
17 | Tốc độ tối đa 50km/h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/toc%20do%20toi%20da%2050.png?raw=true "") |  | 42 | Đỗ xe | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/noi%20do%20xe.png?raw=true '')
18 | Đường dành cho xe moto | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20danh%20cho%20xe%20moto.png?raw=true "") |  | 43 | Cấm dừng và đỗ xe từ 6-9h và 16-20h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/C%E1%BA%A5m%20d%E1%BB%ABng%20v%C3%A0%20%C4%91%E1%BB%97%20xe%20t%E1%BB%AB%206-9h%20v%C3%A0%2016-20h.png?raw=true '')
19 | Cấm đi ngược chiều | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20di%20nguoc%20chieu.png?raw=true "") |  | 44 | Cấm đỗ xe từ 9-16h và 20-6h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/C%E1%BA%A5m%20%C4%91%E1%BB%97%20xe%20t%E1%BB%AB%209-16h%20v%C3%A0%2020-6h.png?raw=true '')
20 | Đi vào đường bên phải | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/huong%20phai%20di%20vong%20sang%20phai.png?raw=true "") |  | 45 | Ngoại lệ | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ngoai%20le.png?raw=true '')
21 | Cấm xe 3 hay 4 bánh thô sơ từ 5-13h và 16-22h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20xe%203%204%20banh%20tho%20so%20thoi%20gian.png?raw=true "") |  | 46 | Chú ý chướng ngại vật phía trước | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/chu%20y%20chuong%20ngai%20vat%20phia%20truoc.png?raw=true '')
22 | Cấm đỗ xe vào ngày chẳn | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe%20ngay%20chan.png?raw=true "") |  | 47 | Cấm dừng và đỗ xe | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20dung%20va%20do%20xe.png?raw=true '')
23 | Cấm đỗ xe | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe.png?raw=true "") |  | 48 | Cắm rẽ phải | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20re%20phai.png?raw=true '')
24 | Bến xe bus | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ben%20xe%20bus.png?raw=true "") |  | 49 | Đường có camera | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/camere.png?raw=true '')

Bảng 3.1.3: Tên và hình ảnh của 50 classes.

### **3.1.4. Khó khăn của việc thu thập dữ liệu**
* Có nhiều biển báo có kèm theo thời gian áp dụng, với khoảng thời gian khác nhau, chúng em phân vào class khác nhau. Do đó số lượng ảnh trong các class có chứa thời gian không được nhiều. Thường là đi hết 1 đường qua đường khác không gặp lại biển báo có khoảng thời gian đó.


<img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20dung%20do%20xe1.jpg?raw=true" alt="drawing" width="270" height='480'/>
<img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20dung%20do%20xe2.jpg?raw=true" alt="drawing" width="270" height='480'/>

Hình 3.1.4. Biển “Cấm dừng và đỗ xe” có và không có thời gian.


## **3.2. Xử lý dữ liệu**

### **3.2.1. Chia tập train/val**

  * Sau khi label và lọc ảnh, còn lại 1448 ảnh. Tiến hành chia train/val với tỉ lệ 8/2:
    * Train: 1179 ảnh. Có đặc điểm sau: 

      *	Class có ít ảnh nhất là class ”Chỗ ngoặt vòng bên phải” (9 ảnh) và “Đường không bằng phẳng” (9 ảnh).
      *	Class có nhiều ảnh nhất là “Cấm dừng và đỗ xe” (102 ảnh).
      *	Số lượng các ảnh của các class chênh nhau khá lớn.
      *	Có 8 class có số lượng ảnh ít hơn 15

    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/8%20bien%20it.png?raw=true" alt="drawing" width="1000" height='300'/>

    Hình 3.2.1.1: Class có ít hơn 8 ảnh trong tập train.
    <!-- <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20train%201.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20train%202.png?raw=true" alt="drawing" width="400" height='300'/>
     -->

    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/train%20source%201.png?raw=true" alt="drawing" width="1000" height='700'/>

    Hình 3.2.1.2: Số lượng ảnh từng class trong tập train.

    * Val: 269 ảnh.
      *	Class có ít ảnh nhất là class ”Giao nhau đường ưu tiên” (1 ảnh).
      *	Class có nhiều ảnh nhất là “Cấm dừng và đỗ xe” (27 ảnh).
      *	Số lượng các ảnh của các class chênh nhau khá lớn.

    <!-- <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20val%201.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20val%202.png?raw=true " alt="drawing" width="400" height='300'/> -->

    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/val%201.png?raw=true" alt="drawing" width="1000" height='700'/>

    Hình 3.2.1.3: Số lượng ảnh từng class trong tập Val.




###  **3.2.2. Tăng cường dữ liệu:**
  * Tiến hành tăng cường dữ liệu trên tập train. Quá trình tăng cường được thực hiện trên Roboflow, với các kĩ thuật:

Tên kĩ thuật tăng cường | Lý do áp dụng
--- | --- 
Xoay ảnh từ -7 đến 7 độ | Khi điều khiển xe máy né các chướng ngại vật thì xe sẽ bị nghiêng một góc nhỏ.
Làm mờ ảnh | Khi xe chạy với tốc độ cao, camera của điện thoại sẽ không bắt nét kịp, làm cho ảnh mờ. 

  * Sau khi tăng cường, thu được gấp 3 lần số ảnh trong tập train ban đầu (3537 ảnh). Khi kiểm tra lại data sau khi tăng cường, có những ảnh xoay làm cho biển báo bị che mất, chúng em quyết định xóa. Cuối cùng còn 3342 ảnh.

  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/anh%20xoay%20lam%20mat%20bien%20bao.png?raw=true " ")  

Hình 3.2.2. Khi xoay làm mất biển báo.



### **3.2.3. Tổng kết bộ data sau cùng**
Bộ dataset sau cùng: 
  *	Tổng số lượng ảnh dùng để train+val là 3611 ảnh, thuộc về 50 classes.
  *	Bộ dữ liệu test: gồm 11 video.

  * Một số ảnh nằm trong bộ dữ liệu.
<p align ="middle">
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%201.jpg?raw=true" />
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%202.jpg?raw=true" />
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%203.jpg?raw=true" />
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%204.jpg?raw=true" />
</p>


<p align ="middle">   

  <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/tang%20cuong.png?raw=true" alt="drawing" width="1000" height='700'/>

  Hình 2.2.3.5. Số lượng ảnh mỗi class sau khi tăng cường trên tập train. 
</p>

<p align ="middle">   
  <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20vi%20tri%20bb.png?raw=true" alt="drawing" width="400" height='300'/>
  <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20kich%20thuoc%20bb.png?raw=true" alt="drawing" width="400" height='300'/>

  Hình 2.2.3.6. Phân bố kích thước, vị trí của bounding box trên tập Train.
</p>

<a name="training"></a>
# **4. Training Và Đánh Giá Model**
## **4.1. Hướng tiếp cận và chọn model để huấn luyện**

* Các thuật toán object detection bao gồm 2 nhóm chính:
  *	Họ các mô hình R-CNN (Region-Based Convolutional Neural Networks).
  *	Họ các mô hình YOLO (You Only Look Once).

<a name="yolonhanh"></a>
* Trong phần abstract của bài báo: https://www.researchsquare.com/article/rs-668895/latest.pdf. Có đề cập rằng mAP của Faster R-CNN đạt 87.96%, trong khi đó YOLOv3 chỉ đạt 80.17% (Đây cũng là con số khá tốt, chấp nhận được), nhưng Frames per second (FPS) cao gấp 8 lần so với Faster R-CNN.
* Dựa vào đặc điểm của bài toán chúng em đặt ra, yếu tố tốc độ nhận diện có vai trò quan trọng hơn so với độ chính xác. Do đó chúng em quyết định dùng YOLO để thực hiện bài toán này. Hai phiên bản chúng em chọn là YOLOv4, YOLOv5.

<!-- </p> -->


## **4.2. Tổng quan về YOLOv4 và YOLOv5**
### **4.2.1. YOLOv4**
  * Tác giả ban đầu của yolo là Joseph Redmon. Sau đó Alexey Bochkovskiy cải tiến và tạo ra YOLOv4 (năm 2020).

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/joshep.jpg?raw=true" height='200' width='200' />
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/alexey.jpg?raw=true" height='200' width='200' />

Joseph Redmon (bên trái) và Alexey Bochkovskiy (bên phải)
</p>




  * Model Yolov4 sử dụng từ nhiều bộ dataset để train từ trước, đơn cử nhất là từ hai bộ dataset nổi tiếng là ImageNet (ILSVRC 2012 val) gồm 1000 object classes với gần 1,5 triệu ảnh dùng để huấn luyện và MS COCO (test-dev 2017) gồm 80 classes với 330000 ảnh dùng để huấn luyện, có thêm các bước tăng cường dữ liệu như blur,...
  * Repo Github: https://github.com/AlexeyAB/darknet
### **4.2.2. YOLOv5**
  * Tác giả chính là Glenn Jocher.

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/glenn.jpg?raw=true" height='200' width='200' />

Hình 3.2.2.1: Glenn Jocher
</p>

  * Github repo: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data

  * Hiện đang được phát triển bởi Ultralytics LLC (2020). Phiên bản này hiện khá triển vọng theo các số liệu được cung cấp bởi công ty phát triển. Tuy nhiên phiên bản YOLOv5 này chưa có paper chính thức được chấp nhận và cũng đang có nhiều tranh cãi xung quanh tính hiệu quả của mô hình đang được phát triển này.
  * YOLOv5 hiện đang có 5 model.

  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/yolo%20v5%20version.png?raw=true "5 mô hình của YOLOv5")

  Hình 3.2.2.2: Các mô hình và thông số cơ bản của YOLOv5 (Lấy từ repo gốc).

## **4.3. Các bước tiến hành train**
### **4.3.1. Môi trường train và đánh giá**
  * Môi trường train và đánh giá:
    * Google colab là một virtual cloud machine được google cung cấp miễn phí cho các nhà nghiên cứu. Đây là môi trường lý tưởng để phát triển các mô hình vừa và nhỏ. Điểm tuyệt vời ở google colab đó là môi trường của nó đã cài sẵn các packages machine learning và frame works deep learning thông dụng nhất.

  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/colab%20gpu.png?raw=true "Kiểm tra gpu của Colab")
  
   * Do quá trình tải dữ liệu lên Colab tốn thời gian, và sau mỗi phiên colab (khoảng 5 tiếng) thì dữ liệu sẽ mất hết. Do đó chúng em lưu trữ dữ liệu bài toán trên google drive, sau đó kết nối drive với colab.

### **4.3.2. YOLOv4**
* Để bắt đầu train, chúng em sử dụng file Pretrained Weights yolov4.conv.137 để tiếp tục train cho model của mình. Sử dụng weight này là vì: 
  * Sử dụng file Pretrained Weights giúp tiết kiệm thời gian train so với train lại toàn bộ model từ đầu.
  * Pretrain này được train trên tập MSCOCO, nhưng lớp cuối(Lớp dùng để phân loại) không được sử dụng để train tiếp trong bài này. Bằng cách sử dụng pretrain này, chúng ta có thể phát hiện những đặc trưng như: đường tròn, đường thẳng, các đặc trưng phức tạp từ tập MSCOCO, từ đó áp dụng tốt hơn vào bài toán.
* Quá trình training model:
  * Clone các source code cần thiết để train model - AlexyAB/darknet.
  * Set up lại các file cần thiết và tài nguyên để chuẩn bị cho việc training: 
    * Files yolo.names chứa tên các classes sẽ được detect trong bộ dataset.
    * File train.txt chứa các đường dẫn của ảnh trong tập train.
    * File val.txt chứa các đường dẫn của ảnh trong tập val.
    * File yolo.data cấu hình thông tin class, chỉ ra các file dữ liệu cần thiết.
    * File yolov4-custom.cfg: tinh chỉnh các thông số của quá trình train:
        * width, height=416,416(kích thước network).
        * Batch=64: Xử lý 64 ảnh trong 1 vòng lặp.
        * Subdivisions=16: chia nhỏ batch. 64/16 = 16 => xử lý 1 lần 16 ảnh trong mỗi batch. Cách chọn batch và subdivision phụ thuộc vào gpu của chúng ta. Do chúng em chọn được gpu Tesla T4 có bộ nhớ xấp xỉ 16Gb, nên để batch bằng 16.
        * Max_batches=100000 (= số class * 2000: khuyến nghị của tác giả).
        * classes=50.
        * filters=165 (= (số class + 5) * 3: khuyến nghị của tác giả).
    * Download file pretrain weights (yolov4.conv.137) cho lần training model đầu tiên.
    * Train.
    * File weights được lưu trong backup/yolov4-custom_last.weights sau mỗi 100 iters.
        
Notebook:    
https://drive.google.com/file/d/1wg5hRibL8OyRGRmt26cym3oYHFLmYB47/view?usp=sharing

### **4.3.3. YOLOv5**

* Chuẩn bị dữ liệu như cây thư mục sau: 

![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/thu%20muc%20tren%20may%20yolo%20v5.png?raw=true "")    
**Quá trình training model:**
  * Gitclone repo: https://github.com/ultralytics/yolov5
  * Cài môi trường như hướng dẫn trong repo.
  * Setup lại file yolov5/data/coco128.yaml.
  * Chạy lệnh để train. Sau khi chạy hết 1 epoch, file weight sẽ tự động lưu trong yolov5/runs/train.
Notebook:https://drive.google.com/file/d/11iV5XgZIJiwlzXp6pZC65bMGTJs-tQU0/view?usp=sharing



## **4.4. Đánh giá mô hình**
Sau khi thực hiện train model, để xác định model của chúng ta có đủ tốt hay chưa cũng như đảm bảo khả năng nhận diện trong tương lai ta cần có một phương pháp đánh giá với tiêu chí cụ thể. Đối với bài toán Object Detection, model thường được đánh giá dựa trên mAP,...Trong bài toán này, chúng em quyết định sử dụng mAP để đánh giá về độ chính xác model của mình. Ngoài ra, để đánh giá về mặt tốc độ, chúng em dùng FPS.
### **4.4.1.	mAP (mean Average Precision)**
Trước khi tìm hiểu khái niệm và cách tính mAP, chúng ta cần tìm hiểu các khái niệm liên quan.
#### **4.4.1.1.	IOU (Intersection over Union).**
IOU là hàm đánh giá độ chính xác của object detector trên tập dữ liệu, cụ thể được xác định bởi phép chia:  

![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/iou.png?raw=true ) 

Hình 3.6: Hình minh họa predicted bounding box với ground-truth bouding box.

Trong đó:   
* Area of overlap là diện tích phần giao giữa predicted bounding box với ground-truth bouding box.
* Area of Union là diện tích phần hợp giữa predicted bounding box với ground-truth bounding box.
* Với ground-truth bouding box là do ta xác định (trong lúc label data), predicted bounding box do model xác định.     

Với mỗi bài toán thường có IOU threshold nhất định (nhận giá trị từ 0 đến 1). Nếu IOU > threshold thì prediction được đánh giá là tốt. Trong đa số bài toán threshold thường được đặt bằng 0,5.  

Các tiêu chí đánh giá với IOU threshold:    
* True Positive (TP): Đối tượng được nhận dạng đúng với IOU ≥ threshold.
* False Positive (FP): Đối tượng được nhận dạng sai với IOU < threshold.
* False Nagative (FN): Đối tượng không được nhận dạng.

#### **4.4.1.2. Precision và Recall**
Precision - độ tin cậy của model, cho biết bao nhiêu % dự đoán Positive là True Positive.                                 	Precision =TP/(TP+FP)

Recall - độ nhạy của model cho biết model có thể đoán đúng được bao nhiêu Positive trong dữ liệu được cho.
Recall = TP/(TP+ FN)
#### **4.4.1.3. Precision Recall Curve và Average precision (AP)**
Precision và Recall thay đổi với mỗi Confidence threshold. Để quan sát tất cả các precision và recall tương ứng các threshold ta sử dụng Precision Recall Curve – đường đi qua tất các điểm với giá trị (recall, precision) ứng với từng threshold.

 ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/prc.png?raw=true)  
Hình 3.4.1: Precision-Recall Curve
			
AUC (Area Under the Curve ) - diện tích nằm dưới Curve giúp đánh giá model. Với Precision Recall Curve, Area Under the Curve (AUC) còn được gọi là  Average precision (AP). AP được xác định bởi công thức:   
<!-- ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/tinh%20ap.png?raw=true)   -->



![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ap.png?raw=true)  

R_k,P_k  lần lượt là Recall và Precision ứng với threshold thứ k    
n: số threshold
* AP lớn nếu vùng AUC này lớn, suy ra đường cong có xu hướng gần góc trên bên phải và có nghĩa là tại các threshold khác nhau thì Precision và Recall đều khá cao. Từ đó suy ra model tốt.
* AP nhỏ thì cả Precision và Recall đều khá thấp và model không tốt.




#### **4.4.1.4. mAP**
Trong bài toán Object Detection nói chung hay YOLO nói riêng thì mAP được định nghĩa là trung bình cộng giá trị AP của tất cả các class.
Trong đó:

![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/calcula%20mAP.png?raw=true)  

*	C là tập hợp tất cả các class
*	n là số class

mAP càng lớn thì thì đa số AP của từng class riêng biệt càng lớn dẫn đế model càng tốt. Từ đó việc train model sẽ cố gắng train model có mAP lớn nhất có thể. Đây là lí do hoàn hảo sử dụng để mAP đánh giá model.

### **4.4.2. FPS (Frame per second)**

* FPS là tỉ lệ khung hình trên giây. FPS càng cao thì số khung hình xử lý trong 1 đơn vị thời gian càng nhiều. Hay nói cách khác, model có thể đáp ứng tác vụ real time.

### **4.4.3. Đánh giá model**

*	YOLOv4: Sau khi train 14k iters, chúng em nhận thấy giá trị loss không giảm đáng kể, giá trị loss chỉ nằm trong khoản 0.13-0.14 (khi train trên tập tăng cường) và 0.09-0.1 (khi train trên tập gốc), nên chúng em quyết định dừng train.
*	YOLOv5: sau khi train 140 epochs, giá trị mAP@.5 model đánh giá trên tập val chững lại và có xu hướng giảm nhẹ xung quanh 0.985. Cho rằng mô hình đã hội tụ, nên chúng em dừng train và chọn best.weights (weight có điểm mAP trên tập val cao nhất mà model lưu lại) để tiến hành đánh giá.

![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/danh%20gia.png?raw=true)  

<a name="danhgiafps"></a>
* Để tính được FPS, chúng em làm như sau:

YOLOv4 | YOLOv5 
--- | --- 
Khi predict trên video, FPS được tính tự động. | Khi predict trên video, có trả về thời gian trung bình khi xử lý 1 frame. Theo như định nghĩa FPS, chúng em lấy nghịch đảo giá trị thời gian trên là giá trị của FPS.
Tính FPS trung bình của 11 video trong tập test. | Tính FPS trung bình của 11 video trong tập test.


  *	Điểm mAP của mô hình train trên tập dữ liệu gốc cao hơn mô hình train trên tập tăng cường, chứng tỏ việc tăng cường dữ liệu không hiệu quả.
  *	Đối với tập tăng cường, YOLOv5 (0.985) thể hiện được rõ nhất sự chênh lệch về độ chính xác so với YOLOv4 (0.977).
  *	FPS của YOLOv5 cao hơn 4.5 lần so với YOLOv4. Với tốc độ này, YOLOv5 hoàn toàn đáp ứng tốt nhu cầu realtime trong tình huống đặt ra.
  *	YOLOv5 có kích thước tương đối nhẹ (55.1 MB), đồng thời độ chính xác cao. Trong tương lai, đây là mô hình đầy triển vọng để triển khai trên các thiết bị IoT.



<a name="phantich"></a>
Phân tích cụ thể trên YOLOv5: file weights `best_v5_augmentdata.pt` với `conf=0.5`

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/danhgia1.png?raw=true" />
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/danhgia2.png?raw=true" />

Hình 4.4.3.1. Đánh giá tập val trên file weights `best_v5_augmentdata.pt` với `conf=0.5`
</p>

* Class “tốc độ tối đa 60 Km/h” có precision thấp (0.445). Sau khi kiểm tra lại, nguyên nhân là do model detect ra những biển báo chúng em không label. Lý do không label là do chúng em chỉ quan tâm tới những biển báo cách xe ít hơn 20m. Hình dưới là bức ảnh minh họa cho trường hợp này.

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/toc%20do%2060%20loi.jpg?raw=true" />


Hình 3.4.3.2: Class “tốc độ tối đa 60Km/h” không label nhưng được detect.
</p>

* Class “Đường không bằng phẳng” có recall tương đối thấp(0.668). Trong tập val chỉ có 3 ảnh thuộc class này, với precall 0.668 nên sẽ có 1 ảnh predict sai.

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ko%20bang%20sai.jpg?raw=true" height=480 width=270 />

Hình 3.4.3.3: Ảnh có biển báo "Đường không bằng phẳng" không predict được.
</p>

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ko%20bang%20dung.jpg?raw=true" height=480 width=270/>
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/khong%20bang%20dung%201.jpg?raw=true" height=480 width=270/>

Hình 3.4.3.4,5: Ảnh có biển báo "Đường không bằng phẳng" predict đúng.

</p>


* Khi em thay confidence score thành 0.3, model có thể detect được biển báo này trong ảnh 3.4.3.3.

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/Picture8.jpg?raw=true" height=480 width=270/>
</p>

* Model detect biển báo này không tốt, thậm chí còn nhầm sang biển báo “Giao nhau với đường không ưu tiên” là do số ảnh của class “đường không bằng phẳng” là ít nhất trong các class (9 ảnh trên tập train chưa tăng cường).
* Do 2 biển báo này đều có hình tam giác, mà mô hình tính toán và dự đoán ra bounding box là hình chữ nhật. Do đó phần diện tích nhiễu (phần ngoài hình tam giác) ảnh hưởng rất lớn tới kết quả dự đoán mô hình.

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/giao%20nhau%20duong%20khong%20uu%20tien.png?raw=true" />
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20khong%20bang%20phang.png?raw=true" />
</p>

* Bên cạnh đó thì có một vài yếu tố môi trường bên ngoài làm cho model nhận diện không tốt.
<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cay%20che.png?raw=true" height=480 width=270/>

Hình 3.4.3.6: Biển báo bị cây che.

</p>


<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/bong%20toi%202.png?raw=true" height=480 width=270/>
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/bong%20toi%201.png?raw=true" height=480 width=270/>
	
Hình 3.4.3.7: Biển báo bị ảnh hưởng trong tối.

</p>

* Đối với biển báo ban đêm, ảnh chụp không được rõ nét do ảnh hưởng bởi ánh sáng đèn đường, chất lượng camera chụp ảnh. Do đó, ảnh ban đêm có khả năng sai cao hơn so với ảnh ban ngày.

<a name="ungdung"></a>
# **5. Ứng Dụng và Hướng Phát Triển**
## **5.1. Cải tiến**

Để có thể đưa mô hình này vào ứng dụng rộng rãi, cần phải cải tiến về một số khía cạnh:

**Về data:**
*	Thu thập đầy đủ các loại biển báo trong khu vực, với các góc nhìn khác nhau (sát lề trái, giữa đường, …). Trong đồ án này, chúng em chỉ thu thập trong khu vực quận Bình Tân và một số quận lân cận. Trong tương lai sẽ thu thập trên toàn thành phố.
*	Áp dụng các kĩ thuật label data mang tính khoa học hơn, hạn chế label bằng tay. Label bằng tay hiệu suất rất thấp.
*	Tìm hiểu thêm các kĩ thuật tăng cường data. Việc áp dụng không hiệu quả các kĩ thuật tăng cường dữ liệu trong đề tài này càng cho thấy tuy số lượng dữ liệu quan trọng nhưng chất lượng dữ liệu cũng là một yếu tố ảnh hưởng mạnh mẽ tới độ chính xác model.
*	Số lượng ảnh ở các lớp chênh lệch tương đối lớn, hay nói cách khác data bị mất cân bằng. Để giải quyết vấn đề này, ban đầu chúng em đề ra 2 cách:
  *	Copy ảnh ở những class ít lên, qua đó làm dày số lớp có ít ảnh. Nhưng nếu copy như thế, một ảnh có thể học 2-3 lần, dễ dẫn đến hiện tượng overfit.
  *	Lấy những ảnh ở class ít đi tăng cường data, cũng là làm dày dữ liệu nhưng ít nhất các ảnh không hoàn toàn giống nhau. Sẽ khó bị overfit hơn so với cách 1.
→ Chọn hướng giải quyết số 2. (chúng em không áp dụng kịp vào bài toán).

**Về thuật toán:** Hiện tại chúng em chỉ mới biết YOLO có khả năng detect realtime, chúng em sẽ tìm hiểu thêm các thuật toán khác, tiến hành chạy thử và thực nghiệm.

## **5.2. Hướng phát triển trong tương lai**

*	Hệ thống sẽ trả về thông tin nhận diện là âm thanh, để người dùng không phải nhìn liên tục vào màn hình điện thoại.
*	Việc detect cần yếu tố thời gian, do đó yêu cầu thiết bị có cấu hình mạnh. Nhưng đa phần các loại điện thoại di động bây giờ không được thiết kế để thực hiện tác vụ này. Chúng em sẽ triển khai model lên web, người dùng sẽ giao tiếp với hệ thống thông qua web. Khi đó ta chỉ cần quan tâm tới tốc độ mạng (Vấn đề về mạng thì dễ giải quyết hơn).
*	Hướng phát triển tiếp theo là kết hợp model này với Google Map, vì đa phần người dùng thường bật Google Map khi tham gia giao thông.


<a name="demo"></a>
# **6. Demo mô hình**

 [Demo.](./API/)

<a name="thamkhao"></a>
# **7. Tài liệu tham khảo**

**Tìm hiểu về model Yolov4:**

[1]https://phamdinhkhanh.github.io/2020/03/10/DarknetGoogleColab.html

[2]https://www.youtube.com/watch?v=mmj3nxGT2YQ

[3]https://towardsdatascience.com/yolov5-compared-to-faster-rcnn-who-wins-a771cd6c9fb4

**Tìm hiểu về yolov5**

[1]https://joaootavionf007.medium.com/orange-trees-detection-with-yolo-v5-in-uav-imagery-22ec29db922e

[2]https://github.com/ultralytics/yolov5

**Tìm hiểu về thang đo đánh giá**

[1]https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html

[2]https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html

[3]https://blog.paperspace.com/deep-learning-metrics-precision-recall-accuracy/

[4]https://blog.paperspace.com/mean-average-precision/

**Tìm hiểu về feature extraction**

[1]https://www.sciencedirect.com/topics/engineering/feature-extraction

**Tìm hiểu tổng quan YOLOv4, YOLOv5**

[1]https://medium.com/deelvin-machine-learning/yolov4-vs-yolov5-db1e0ac7962b

[2]https://aicurious.io/posts/tim-hieu-yolo-cho-phat-hien-vat-tu-v1-den-v5/

[3] https://www.researchsquare.com/article/rs-668895/latest.pdf


**Mẫu bài báo cáo**

[1]https://github.com/lphuong304/CS114.L21/blob/main/FINAL_PROJECT/Final_Report.md

