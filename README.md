# Download tập ảnh dép lào
1. Download [trình duyệt](https://linuxize.com/post/how-to-install-google-chrome-web-browser-on-ubuntu-18-04/) google chome
2. Download [driver](https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.11/) google chome
3. Viết chương trình [lấy file](./src/getI.py) ảnh từ google images
4. Viết chương trình [chuẩn hóa](./src/standardized-image-names.py) tên file ảnh
5. Viết chương trình [phân chia](./src/split-list-image.py) 80% ảnh train 20% ảnh test

# Gán nhãn cho tập dữ liệu
1. Cài đặt công cụ [labelImg](https://github.com/tzutalin/labelImg)
2. [Tập ảnh](./data/images/)
3. [Tập nhãn](./data/labels/)

# Train dữ liệu
1. download [darknet](https://github.com/pjreddie/darknet)
2. Đưa dữ liệu ảnh vào /darknet/data/images/
3. Đưa file tọa độ rectangle vào /darknet/data/labels/
4. Đưa file train.txt gồm 80% ảnh trong tập dữ liệu và0 /darknet/
5. Đưa file val.txt gồm 20% ảnh trong tập dữ liệu vào /darknet/
6. Tạo file yolo.data, yolo.names
7. Download file darknet53.conv.74
8. Chỉnh sửa số liệu trong file darknet/cfg/yolov3.cfg ,filter and class
9. Chỉnh sửa file /darknet/examples/detector.c, tìm đến dòng 138
```c
if(i%2000==0 || (i < 1000 && i%100 == 0))
```
10. Bắt đầu train:
```sh
./darknet detector train yolo.data cfg/yolov3.cfg darknet53.conv.74
```

# Train dữ liệu trên google colab
1. Nén darknet thành darknet.zip
2. Upload lên google drive
3. Sử dụng [google colab]https://colab.research.google.com() để truy cập
4. chọn file -> new python 3 Notebooke
5. chọn runtime -> change runtime type -> đổi None sang GPU
6. Kết nối đến google drive

```python
from google.colab import drive
drive.mount('/content/drive')

```
7. giải nén file zip

```python
%cd /content
!unzip /content/drive/'My Drive'/ML/darknet.zip
%cd /content/darknet
```
8. Gán quyền thực thi

```python
!make
!chmod +x ./darknet
```
9. Tạo liên kết mềm sang google dive

```python
!rm /content/darknet/backup -r
!ln -s /content/drive/'My Drive'/ML/backup /content/darknet
```
10. tiến hanh train

```python
%cd /content/darknet
!./darknet detector train yolo.data cfg/yolov3.cfg backup/yolov3_900.weights
```

11. download file weight mới nhất trong thư mục [backup](https://drive.google.com/open?id=152WgfNtVDyHgF02hbkfqEv30mGADTxMe)

# Kiểm thử
1. Lấy file weight mới nhất trong tập [backup](https://drive.google.com/open?id=152WgfNtVDyHgF02hbkfqEv30mGADTxMe) ra sung_test
2. Lấy 1 tấm hình trong tập train ra test thử
3. Sử dụng lệnh:  python YOLO.py -i sung_test.jpg -cl yolo.names -w backup/yolov3.backup -c cfg/yolov3.cfg
