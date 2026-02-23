# BÁO CÁO THỰC NGHIỆM THUẬT TOÁN SẮP XẾP

## 1. Giới thiệu

Dự án này thực hiện việc cài đặt, thực nghiệm và so sánh hiệu năng của các thuật toán sắp xếp trong môn *Cấu trúc dữ liệu và Giải thuật (DSA)*.

Mục tiêu của bài thực nghiệm:

- Hiểu rõ nguyên lý hoạt động của từng thuật toán
- Phân tích độ phức tạp thời gian
- So sánh hiệu năng thực tế trên bộ dữ liệu lớn
- Đánh giá ảnh hưởng của trạng thái dữ liệu đầu vào

---

## 2. Thành phần dự án

- `Sorting_Experiment.py`  
  Mã nguồn thực hiện:
  - Chạy thuật toán
  - Đo thời gian thực thi
  - Ghi nhận kết quả
- `quicksort.py`, `mergesort.py`, `heapsort.py`
  Mã nguồn thực hiện thiết kế thuật toán.
- `data.py`
  Mã nguồn thực hiện tạo dữ liệu thử nghiệm.    

- `Sorting_Report.pdf`  
  Báo cáo chi tiết bao gồm:
  - Bảng số liệu
  - Biểu đồ minh họa
  - Nhận xét và phân tích kết quả thực nghiệm

- `Data.csv`  
  Mô tả cấu trúc và đặc điểm của bộ dữ liệu sử dụng trong thực nghiệm.
  Đường dẫn truy cập vào file data: https://drive.google.com/drive/folders/1trmuvN2KvEoMBooND346v9Q-tDx8xvyy?usp=sharing

---

## 3. Các thuật toán được thử nghiệm

- **QuickSort** – Thuật toán chia để trị, chọn phần tử chốt (pivot) ở giữa dãy.
- **MergeSort** – Thuật toán sắp xếp trộn, độ phức tạp ổn định O(n log n).
- **HeapSort** – Thuật toán sắp xếp vun đống, sử dụng cấu trúc Heap.
- **NumPy Sort** – Hàm sắp xếp mặc định của thư viện NumPy (dùng làm mốc so sánh).
- **Python Sort** - Hàm sắp xếp mặc định của kiểu list trong Python.
---

## 4. Quy mô và đặc điểm dữ liệu

- **Số lượng dãy:** 10 dãy dữ liệu  
- **Kích thước:** 1.000.000 phần tử mỗi dãy  
- **Loại dữ liệu:**  
  - Số nguyên  
  - Số thực  

- **Trạng thái ban đầu của dữ liệu:**  
  - Tăng dần  
  - Giảm dần  
  - Ngẫu nhiên  

---

## 5. Môi trường thực nghiệm

- Ngôn ngữ: Python  
- Thư viện sử dụng: NumPy  
- Công cụ đo thời gian: module `time`  

---
