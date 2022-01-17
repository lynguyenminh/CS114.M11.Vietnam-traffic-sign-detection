

<h3 align="center" font-size= 14px;><b>Trường Đại Học Công Nghệ Thông Tin - ĐHQH TPHCM</b></h3>
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>
<h1 align="center"><b>Đồ án cuối kỳ môn Máy học - CS114.M11</b></h1>
<h2 align="center"><b>BÀI TOÁN NHẬN DIỆN BIỂN BÁO GIAO THÔNG TRONG KHU VỰC QUẬN BÌNH TÂN </b></h2>


### Giáo viên hướng dẫn

Họ tên | Email
--- | --- 
PGS.TS. Lê Đình Duy | duyld@uit.edu.vn
Ths. Phạm Nguyễn Trường An | truonganpn@uit.edu.vn


### Các thành viên của nhóm:
Họ tên | MSSV | Email | GitHub
--- | --- | -- | --
Nguyễn Minh Lý | 20521592 | 20521592@gm.uit.edu.vn | https://github.com/lynguyenminhuit
Nguyễn Đặng Nhật Hào | 20520490 | 20520490@gm.uit.deu.vn | https://github.com/cauhamau
Nguyễn Hồng Hậu | 20521300 | 20521300@gm.uit.edu.vn | https://github.com/Nguyen-Hong-Hau
</p>

# **BẢNG MỤC LỤC**

1. [Tổng Quan Về Đồ Án](#tongquan)

2. [Xây Dựng Bộ Dữ Liệu](#dulieu)
3. [Training Và Đánh Giá Model](#training)

4. [Hướng Phát Triển Và Cải Tiến](#ungdung)
5. [Nguồn Tham Khảo](#thamkhao)

<a name="tongquan"></a>
# **1. Tổng Quan Về Đồ Án**

* **Ngữ cảnh ứng dụng**
  * Ở Việt Nam, giao thông đường bộ là loại hình giao thông phổ biến và phát triển nhất. Tính đến năm 2019, tổng số xe máy đăng kí của Việt Nam là khoảng 62 triệu chiếc. Cùng với sự gia tăng số lượng phương tiện nhanh chóng, hệ thống đường xá cũng liên tục được nâng cấp. Trong khi người dân tham gia giao thông, có những lúc bị xao nhãng, không chú ý đến những biển báo bên đường. Chính những thiếu sót đó có thể bị phạt hay dẫn đến tai nạn không mong muốn. Để khắc phục vấn đề này, chúng em đề xuất một hệ thống nhận diện biển báo ngay trong lúc tham gia giao thông. Ứng dụng sẽ chụp ảnh từ camera điện thoại, sau đó dùng mô hình máy học để nhận diện biển báo và thông báo đến người tham gia giao thông.
  * Đối tượng sử dụng là người điều khiển xe máy, có trang bị:
    * Điện thoại di động, ảnh chụp từ điện thoại có kích thước 1920x1080. 
    * Giá đỡ điện thoại gắn trên xe máy.
    
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/gia%20do%201.jpg?raw=true "Giá đỡ điện thoại")
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/gia%20do%202.jpg?raw=true "Giá đỡ điện thoại")
    
* **INPUT và OUTPUT Bài toán**
  * INPUT: 
    * Video được quay từ camera điện thoại gắn trên giá đỡ.
    * Điện thoại phải để thẳng đứng.
    
  * OUTPUT: 
    * Video với các thông tin:
      * Bbox bao quanh các biển báo được nhận diện đi kèm với tên + chỉ số biểu thị độ chính xác của biển báo nhận diện.

      
      


<a name="dulieu"></a>
# **2.Xây Dựng Bộ Dữ Liệu**
## Thu thập dữ liệu

  * Bài toán xác định rõ phạm vi thu thập dữ liệu là quận Bình Tân, với phạm vi khá nhỏ, chúng em tìm trên Internet thì chưa thấy ai thu thập data cho bài toán này.
  * Việc tự thu thập giúp chúng em kiểm soát góc chụp, nguồn, chất lượng, số lượng ảnh phù hợp với mục tiêu đề ra.

* **Thông tin thu thập dữ liệu**
  * Địa điểm: Các con đường trong phạm vi quận Bình Tân.
  * Cách thu thập: Sử dụng điện thoại quay video trong quá trình chạy xe. Tốc độ xe ở mức 40km/h (ở khu vực cho phép). Sau đó cắt những ảnh từ video ra đề làm data.
  * Thu thập dữ liệu lúc ban ngày, lúc chiều tối.
  

* **Khó khăn của việc thu thập dữ liệu**
  * Cần chụp các ảnh ban ngày, chiều tối để đa dạng các tình huống có thế xảy ra.
  * Đường đi qua đa phần là đường 1 chiều, nên chạy khá nhiều đường để chụp đủ số lượng ảnh.
  * Có nhiều biển báo có kèm theo thời gian, với khoảng thời gian khác nhau, chúng em cho vào class khác nhau. Do đó số lượng ảnh trong các class có chứa thời gian không được nhiều. Thường là đi hết 1 đường qua đường khác không gặp lại biển báo đó.
* **Các lần thu thập dữ liệu**
<!-- ### Các lần thu thập dữ liệu: -->
Lần thu thập | Ngày thu thập | Số lượng video | Số lượng ảnh sau khi lọc | Mục đích
--- | --- | -- | -- | --
1 | 29/12/2021 | 91 | 874 | Train & val
2 | 6/1/2022 | 49 | 877 | Train & val
3 | 15/1/2022 | 17 | Không cắt thành ảnh | Test

* **Sau 2 lần thu thập data đầu tiên, có tất cả 1751 ảnh, thuộc vào 70 class. Nhưng do có những class số lượng ảnh dưới 10, những ảnh label không đúng quy tắc ban đầu đề ra nên chúng em tiến hành loại bỏ. Sau cùng thu được 1448 ảnh thuộc 50 class bên dưới**

ID | Tên biển báo | Hình ảnh |  | ID | Tên biển báo | Hình ảnh
--- | --- | -- | -- | -- | --- | ---
0 | Cấm rẽ trái | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20re%20trai.png?raw=true "") |  | 25 | Cấm dừng và đỗ xe từ 6-20h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20dung%20va%20do%20xe%206-20.png?raw=true '')
1 | Cấm sử dụng còi | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20su%20dung%20coi.png?raw=true "") |  | 26 | Trọng lượng tối đa 10T | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/trong%20luong%20toi%20da%2010t.png?raw=true '')
2 | Đi thẳng | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/di%20thang.png?raw=true "") |  | 27 | Cấm đỗ xe từ 9-16h và 19h-22h | ![]( '')
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
18 | Đường dành cho xe moto | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/duong%20danh%20cho%20xe%20moto.png?raw=true "") |  | 43 | Cấm dừng và đỗ xe từ 6-9h và 16-20h | ![]( '')
19 | Cấm đi ngược chiều | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20di%20nguoc%20chieu.png?raw=true "") |  | 44 | Cấm đỗ xe từ 9-16h và 20-6h | ![]( '')
20 | Đi vào đường bên phải | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/huong%20phai%20di%20vong%20sang%20phai.png?raw=true "") |  | 45 | Ngoại lệ | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ngoai%20le.png?raw=true '')
21 | Cấm xe 3 hay 4 bánh thô sơ từ 5-13h và 16-22h | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20xe%203%204%20banh%20tho%20so%20thoi%20gian.png?raw=true "") |  | 46 | Chú ý chướng ngại vật phía trước | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/chu%20y%20chuong%20ngai%20vat%20phia%20truoc.png?raw=true '')
22 | Cấm đỗ xe vào ngày chẳn | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe%20ngay%20chan.png?raw=true "") |  | 47 | Cấm dừng và đỗ xe | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20dung%20va%20do%20xe.png?raw=true '')
23 | Cấm đỗ xe | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cam%20do%20xe.png?raw=true "") |  | 48 | Cắm rẽ phải | ![]( '')
24 | Bến xe bus | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/ben%20xe%20bus.png?raw=true "") |  | 49 | Đường có camera | ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/camere.png?raw=true '')

* **Chia tập train/val**
  * Sau khi label và lọc ảnh, còn lại 1448 ảnh. Tiến hành chia train/val với tỉ lệ 8/2:
    * Train: 1179 ảnh.
    
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20train%201.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20train%202.png?raw=true" alt="drawing" width="400" height='300'/>
    
    * Val: 269 ảnh.

    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20val%201.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20tap%20val%202.png?raw=true " alt="drawing" width="400" height='300'/>
   



* **Công cụ label dữ liệu**
  * [LabelImg](https://github.com/tzutalin/labelImg). Lý do chúng em chọn LabelImg để label: 
    * Giao diện khá tốt với đầy đủ chức năng: open, load, aotusave,….
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/label%20img.png?raw=true "")
    * Hỗ trợ gán nhãn trên định YOLO default txt format.
    * Dễ cài đặt.

  * Quy tắc khi label: 
    * Label bounding box ôm gọn biển báo, tránh label rộng hơn, hay không label hết phần biển báo.
    * Label những ảnh cách vị trí chụp từ 10-15m. Vì khi nhận diện để thông báo cho người tham gia giao thông, ta cần nhận diện và thông báo trước khi đi qua biển báo đó, để người đi điều chỉnh tốc độ hay chú ý hơn.
    * Đối với những biển báo có thời gian, cần label phần biển báo và khoảng thời gian áp dụng lên biển báo đó. 
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/bb%20c%C3%B3%20thoi%20gian.png?raw=true 'label thời gian')
    * Đối với những biển báo bị mất hơn 40% diện tích, thì sẽ bỏ qua. Lí do là ảnh đó có thể đánh mất một số feature quan trọng, có thể làm cho model học sai.
  * Format sau khi label
    * Đối với mỗi ảnh, sẽ có 1 file txt. Gọi là file annotation.
    ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cau%20truc%20annotation.png?raw=true 'Cấu trúc file annotation')
* **Thông tin về tập data**
  * Tăng cường dữ liệu: 
    * Tiến hành tăng cường dữ liệu trên tập train, do đó số ảnh train tăng gấp 3 lần ban đầu 3537 ảnh. Quá trình tăng cường được thực hiện trên Roboflow, với các kĩ thuật:
    	* Rotate ảnh góc từ -7 đến 7 độ.
	    * Làm mờ ảnh.

    * Tổng quan về bộ dữ liệu
      * Tổng số lượng ảnh dùng để train-val là 3806 ảnh, bao gồm 50 classes.
      * Bộ dữ liệu test: gồm 17  video.
      * Một số ảnh nằm trong bộ dữ liệu.
<p align ="middle">
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%201.jpg?raw=true" />
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%202.jpg?raw=true" />
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%203.jpg?raw=true" />
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%204.jpg?raw=true" />
</p>
    * Số ảnh trong từng class của tập train và val.

<p align ="middle">   
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20train%20+%20val%201.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20train%20+%20val.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20vi%20tri%20bb.png?raw=true" alt="drawing" width="400" height='300'/>
    <img src="https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/phan%20phoi%20kich%20thuoc%20bb.png?raw=true" alt="drawing" width="400" height='300'/>
</p>

<a name="training"></a>
# **3. Training Và Đánh Giá Model**
## Các bước cơ bản của quá trình training

<p align ="middle">
  <img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/cac%20buoc%20co%20ban%20qua%20trinh%20train.png?raw=true" />
</p>

* Vì sao phải trích xuất đặc trưng ảnh?
  * Dưới góc nhìn của máy tính thì bức ảnh chẳng qua là những ma trận số đơn sơ. Còn đối với chúng ta, chúng ta nhận diện được ảnh là do nhận ra những đặc trưng của ảnh. Ví dụ với ảnh sau, những đặc trưng của biển báo: 
    * Hình tròn.
    *	Viền đỏ
    *	Dấu gạch hướng sang trái màu đỏ
    *	Dấu gạch màu trắng thẳng đứng ở giữa.
<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/minh%20hoa%20dac%20trung.jpg?raw=true" />
</p>


  * Giảm số chiều dữ liệu do bỏ đi những phần data không quan trọng. Gia tăng tốc độ training và dự đoán.

## Cách đánh giá bài toán và chọn model để huấn luyện
  * Các thuật toán object detection bao gồm 2 nhóm chính:
    * Họ các mô hình R-CNN (Region-Based Convolutional Neural Networks) giải quyết các nhiệm vụ định vị vật thể và nhận diện vật thể. Ưu điểm là độ chính xác cao.
    * Họ các mô hình YOLO (You Only Look Once), là một nhóm kỹ thuật thứ hai để nhận dạng đối tượng được thiết kế để nhận diện vật thể real time.

  * Cả 2 họ mô hình trên đều có ưu và nhược điểm khác nhau, khó mà có thế so sánh để tìm ra được mô hình nào gọi là tốt nhất. Tuy nhiên dựa vào đặc điểm của bài toán chúng em đặt ra, tốc độ nhận diện phải nhanh là yếu tố bắt buộc phải đáp ứng. Do đó chúng em quyết định dùng YOLO để thực hiện bài toán này.
  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/yolov4%20perform.png?raw=true "")
  * Hình trên là kết quả đánh giá các mô hình trên tập dữ liệu MS COCO (test-dev 2017) gồm 80 classes với 330000 ảnh dùng để huấn luyện. Nhận thấy rằng YOLO v4 có tốc độ predict nhanh, đồng thời độ chính xác chấp nhận được. Do đó chúng em quyết định dùng YOLO v4 để train và đánh giá mô hình.
  * Bên cạnh đó, YOLO cũng vừa ra phiên bản YOLOv5. Chúng em cũng tiến hành đánh giá trong bài toán này.



## Tổng quan về YOLOv4 và YOLOv5
* **YOLOv4**
  * Tác giả ban đầu của yolo là Joseph Redmon. Sau đó Alexey Bochkovskiy cải tiến và tạo ra YOLOv4 (năm 2020).
  ![]( "Joseph Redmon")
  ![]( "Alexey Bochkovskiy")

<p align ="middle">
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/joshep.jpg?raw=true" height='200' width='200' />
<img src = "https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/alexey.jpg?raw=true" height='200' width='200' />
</p>



  * Model Yolov4 sử dụng từ nhiều bộ dataset để train từ trước, đơn cử nhất là từ hai bộ dataset nổi tiếng là ImageNet (ILSVRC 2012 val) gồm 1000 object classes với gần 1,5 triệu ảnh dùng để huấn luyện và MS COCO (test-dev 2017) gồm 80 classes với 330000 ảnh dùng để huấn luyện, có thêm các bước tăng cường dữ liệu như blur,...
  * Repo Github: https://github.com/AlexeyAB/darknet
* **YOLOv5**
  * Tác giả chính là Glenn Jocher.
  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/glenn.jpg?raw=true "Glenn Jocher")
  * Hiện đang được phát triển bởi Ultralytics LLC (2020). Phiên bản này hiện khá triển vọng theo các số liệu được cung cấp bởi công ty phát triển. Tuy nhiên phiên bản YOLOv5 này chưa có paper chính thức được chấp nhận và cũng đang có nhiều tranh cãi xung quanh tính hiệu quả của mô hình đang được phát triển này.
  * YOLOv5 hiện đang có 5 model.
  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/yolo%20v5%20version.png?raw=true "5 mô hình của YOLOv5")

## Các bước tiến hành train
* **Môi trường train và đánh giá**
  * Môi trường train và đánh giá:
    * Google colab là một virtual cloud machine được google cung cấp miễn phí cho các nhà nghiên cứu. Đây là môi trường lý tưởng để phát triển các mô hình vừa và nhỏ. Điểm tuyệt vời ở google colab đó là môi trường của nó đã cài sẵn các packages machine learning và frame works deep learning thông dụng nhất.
  ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/colab%20gpu.png?raw=true "Kiểm tra gpu của Colab")
  
   * Do quá trình tải dữ liệu lên Colab tốn thời gian, và sau mỗi phiên colab (khoảng 5 tiếng) thì dữ liệu sẽ mất hết. Do đó chúng em lưu trữ dữ liệu bài toán trên google drive, sau đó kết nối drive với colab.
  * **YOLOv4**   
    * Để bắt đầu train, chúng em sử dụng file Pretrained Weights yolov4.conv.137 để tiếp tục train cho model của mình.
    * Giải thích vì sao sử dụng file pretrained weights yolov4.conv.137:
      * Sử dụng file Pretrained Weights giúp tiết kiệm thời gian train lại toàn bộ model từ đầu.
      * Pretrain này được train trên tập MSCOCO, nhưng lớp cuối cùng không được sử dụng để train tiếp. Bằng cách sử dụng pretrain này, chúng ta có thể phát những đặc trưng như: đường tròn, đường thẳng, các đặc trưng phức tạp từ tập MSCOCO, từ đó áp dụng tốt hơn vào bài toán.
    * Quá trình training model:
      1.	Upload bộ dữ liệu đã được nhóm chuẩn bị sẵn lên Drive
      2.	Clone các source code cần thiết để train model - AlexyAB/darknet
      3. Set up lại các file cần thiết và tài nguyên để chuẩn bị cho việc training
      Files yolo.names chứa tên các classes sẽ được detect trong bộ dataset.
          * File train.txt chứa các path của ảnh trong tập train.
          * File val.txt chứa các path của ảnh trong tập val.
          * File yolo.data chứa tên file set up cần thiết cho tập train.
          * File yolov4-custom.cfg. Các thông số mà em tinh chỉnh có ý nghĩa ảnh hưởng tới quá trình trainning như sau:
              * width, height=416,416(kích thước network).
              * Batch=64.
              * Subdivisions=16.
              * max_batches=100000 (khuyến nghị của tác giả)
              * classes=50.
              * filters=165 (khuyến nghị của tác giả).

      3.	Dowload file pretrain weights (yolov4.conv.137) cho lần training model đầu tiên.
      4.	Train.
      5.	File weights được lưu trong backup/yolov4-custom_last.weights sau mỗi 100 iters.

  * **YOLOv5**
    * Chuẩn bị dữ liệu như cây thư mục sau: 


      ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/thu%20muc%20tren%20may%20yolo%20v5.png?raw=true "")

      1. Gitclone repo: https://github.com/ultralytics/yolov5
      2. Up data lên drive.

        ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/thu%20muc%20tren%20colab%20yolov5.png?raw=true " ")

      3. Cài môi trường như hướng dẫn trong repo.
      4. Setup lại file yolov5/data/coco128.yaml.

      ![](https://github.com/lynguyenminhuit/CS114.M11/blob/master/Final_Project/Image%20in%20report/c%C3%B4c128.png?raw=true "")
      5. Chạy lệnh để train.
    Sau khi chạy hết 1 epoch, file weight sẽ tự động lưu trong yolov5/runs/train.




## Đánh giá mô hình





<a name="ungdung"></a>
<h1>4. Ứng Dụng và Hướng Phát Triển </h1>

## Để có thể đưa mô hình này vào ứng dụng rộng rãi, cần phải cải tiến về một số khía cạnh:
* **Về Data**
  * Thu thập tất cả các loại biển báo trong khu vực, với các góc nhìn khác nhau (sát lề trái, giữa đường, …). Nếu làm tốt ở khu vực quận BÌnh Tân, chúng em sẽ mở rộng ra thêm các quận khác, và sau đó là cả thành phố.
  * Quy trình label phải được kiểm tra kĩ lưỡng. Với số lượng class lớn, rất dễ xảy ra chọn nhầm nhãn trong lúc label.
  * Tìm hiểu thêm các kĩ thuật tăng cường data. Mỗi kĩ thuật tăng cường đều có ưu nhược điểm, vì vậy không thể áp dụng một cách bừa bãi vào dữ liệu.
  * Số lượng ảnh ở các lớp chênh lệch tương đối lớn, hay nói cách khác data bị mất cân bằng. Để giải quyết vấn đề này, ban đầu chúng em đề ra 2 cách: 
    * Copy ảnh ở những class ít lên, qua đó làm dày số lớp có ít ảnh. Nhưng nếu copy như thế, một ảnh có thể học 2-3 lần, dễ dẫn đến hiện tượng overfit.
    * Lấy những ảnh ở class ít đi tăng cường data, cũng là làm dày dữ liệu nhưng ít nhất các ảnh không hoàn toàn giống nhau. Sẽ khó bị overfit hơn so với cách 1. 

    <span>&#8594;</span> Chọn hướng giải quyết số 2. (Mới nghĩ ra gần đây, chúng em không áp dụng kịp vào model).
* **Về Model**
  * Hiện tại chúng em chỉ mới biết YOLO có khả năng detect realtime, chúng em sẽ tìm hiểu thêm các thuật toán khác, tiến hành chạy thử và thực nghiệm.


* **Hướng phát triển trong tương lai**
  * Thông báo bằng âm thanh khi phát hiện biển báo, để người dùng không phải liên tục nhìn vào điện thoại, không khéo lại phản tác dụng.
  * Việc detect cần yếu tố thời gian, do đó yêu cầu thiết bị có cầu hình mạnh. Nhưng đa phần các loại điện thoại di động bây giờ không được thiết kế để thực hiện tác vụ detect này. Chúng em sẽ triển khai model lên web, người dùng sẽ giao tiếp với hệ thống thông qua web. Khi đó cần quan tâm việc ảnh hưởng của tốc độ mạng.
  * Hướng phát triển tiếp theo là kết nối model này với Google Map, tại đa phần người dùng thường bật Google Map khi tham gia giao thông.

 
<a name="thamkhao"></a>
# 5. Nguồn Tham Khảo:

* Tìm hiểu về model Yolov4:


[1]https://phamdinhkhanh.github.io/2020/03/10/DarknetGoogleColab.html

[2]https://www.youtube.com/watch?v=mmj3nxGT2YQ

[3]https://towardsdatascience.com/yolov5-compared-to-faster-rcnn-who-wins-a771cd6c9fb4

*	Tìm hiểu về yolov5

[1]https://joaootavionf007.medium.com/orange-trees-detection-with-yolo-v5-in-uav-imagery-22ec29db922e

[2]https://github.com/ultralytics/yolov5

*	Tìm hiểu về thang đo đánh giá

[1]https://blog.paperspace.com/deep-learning-metrics-precision-recall-accuracy/

[2]https://blog.paperspace.com/mean-average-precision/

*	Tìm hiểu về feature extraction

[1]https://www.sciencedirect.com/topics/engineering/feature-extraction

*	Tìm hiểu tổng quan YOLOv4, YOLOv5

[1]https://medium.com/deelvin-machine-learning/yolov4-vs-yolov5-db1e0ac7962b

[2]https://aicurious.io/posts/tim-hieu-yolo-cho-phat-hien-vat-tu-v1-den-v5/

*	Mẫu bài báo cáo

[1]https://github.com/lphuong304/CS114.L21/blob/main/FINAL_PROJECT/Final_Report.md
