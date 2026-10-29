# Báo Cáo Thực Hành Chương 3: Flask Cơ Bản

Họ và tên: **Dương Chí Phú**  
Mã sinh viên: **22T1020317**  
Kho lưu trữ: `pmnm-hocphan`  
Thư mục: `chuong_03/`

---

## 1. Hướng dẫn chạy các bài tập
Mỗi bài tập là một file riêng biệt `bXX_ten.py`, có thể chạy bằng lệnh tiêu chuẩn:
```bash
flask --app bXX_ten run --debug --port 8000
```

---

## 2. Báo cáo Bài 1: Chạy ứng dụng Hello Flask
- **Lệnh chạy**:
  ```bash
  flask --app b01_hello run --port 8000
  ```
- **Kết quả hiển thị**:
  Khi truy cập `http://127.0.0.1:8000/`, trình duyệt trả về mã nguồn HTML:
  ```html
  <h1>Xin chào, Flask!</h1>
  ```

---

## 3. Báo cáo Bài 2: Traceback và Debugger
- Khi lưu file: Terminal báo `Detected change in '.../b02_traceback.py', reloading`.
- Truy cập `/chia-nhom`:
  - **Tên Exception**: `ZeroDivisionError: division by zero`
  - **File gây lỗi**: `b02_traceback.py`, dòng `return f"Mỗi nhóm làm {so_bai / so_nhom} bài"`
- Khi KHÔNG có `--debug`: Trình duyệt chỉ hiện `500 Internal Server Error`, ẩn hoàn toàn code.
- **Lý do không bật debug trên Production**: Tránh lộ mã nguồn, khóa bí mật, và tránh nguy cơ bị tấn công thực thi mã từ xa (RCE) qua console interactive của Werkzeug.

---

## 4. Báo cáo Bài 6: Dự đoán kết quả `url_for`
- `url_for("about")` $\rightarrow$ `/about`
- `url_for("post_detail", post_id=7)` $\rightarrow$ `/post/7`
- `url_for("post_detail", post_id=7, lang="vi")` $\rightarrow$ `/post/7?lang=vi`
- `url_for("user_profile", username="Nguyễn An")` $\rightarrow$ `/user/Nguy%E1%BB%85n%20An`
- `url_for("search", q="flask & python")` $\rightarrow$ `/search?q=flask+%26+python`
- `url_for("post_detail")` $\rightarrow$ Lỗi `BuildError` (thiếu tham số bắt buộc).
- `url_for("post_detail", post_id="abc")` $\rightarrow$ Lỗi `BuildError` (sai kiểu converter int).

---

## 5. Báo cáo Bài 13: Context trong `flask shell`
- **Lệnh thực hiện trong flask shell**:
  ```python
  flask --app b13_context shell
  >>> from flask import request, url_for
  >>> request.path
  # Kết quả: RuntimeError: Working outside of request context.
  
  >>> url_for("about")
  # Kết quả: RuntimeError: Working outside of application context.
  ```
- **Mô phỏng Request Context**:
  ```python
  >>> with app.test_request_context("/search?q=flask&page=2", method="POST"):
  ...     print(request.method)            # POST
  ...     print(request.path)              # /search
  ...     print(int(request.args.get("page"))) # 2
  ...     print(url_for("about"))          # /about
  ```
- **Giải thích**: Khối `with app.test_request_context(...)` chủ động đẩy (push) cả Application Context lẫn Request Context vào ngăn xếp luồng, giúp các proxy `request` và `url_for` hoạt động bình thường.

---

## 6. Báo cáo Bài 14: Bảng tìm và sửa lỗi
| Lỗi | URL / Thời điểm | Thông báo lỗi | Nguyên nhân | Cách sửa |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Khởi động** | `AssertionError: View function mapping is overwriting...: index` | Route `/about` bị đặt trùng tên hàm `index`. | Đổi tên hàm ở `/about` thành `def about():` |
| **2** | **Truy cập `/`** | `BuildError: Could not build url for endpoint 'home'` | Gọi `url_for("home")` nhưng tên endpoint là `index`. | Sửa `url_for("home")` thành `url_for("index")` |
| **3** | **Truy cập `/post/1`** | `TypeError: post() got an unexpected keyword argument 'id'` | URL là `<int:id>` nhưng tham số hàm là `post_id`. | Sửa URL thành `@app.route("/post/<int:post_id>")` |
| **4** | **Truy cập `/grade/3`** | `TypeError: The view function for 'grade' did not return a valid response...` | `score < 5` không có return (trả về `None`). | Thêm `return "Chưa đạt"` ở cuối hàm `grade()`. |
| **5** | **Bấm `/contact`** | `405 Method Not Allowed` | Route `/contact` chỉ có GET, không cho phép POST. | Thêm `methods=["GET", "POST"]` vào decorator route. |

---

## 7. Tổng hợp các lệnh kiểm thử (curl / URL)

### Bài 3: Lời chào
- URL: `http://127.0.0.1:8000/hello/` $\rightarrow$ `Xin chào, bạn!`
- URL: `http://127.0.0.1:8000/hello/Nam` $\rightarrow$ `Xin chào, Nam!`
- URL: `http://127.0.0.1:8000/hello/<script>` $\rightarrow$ được escape chống XSS.

### Bài 4: Bình phương
- URL: `http://127.0.0.1:8000/square/12` $\rightarrow$ `144`
- URL: `http://127.0.0.1:8000/square/-3` $\rightarrow$ `9`
- URL: `http://127.0.0.1:8000/square/abc` $\rightarrow$ `404 Not Found`

### Bài 5: Custom Converter
- URL: `http://127.0.0.1:8000/sum/1,2,3` $\rightarrow$ `{"numbers": [1, 2, 3], "sum": 6}`
- URL: `http://127.0.0.1:8000/sum/-1,4,10` $\rightarrow$ `{"numbers": [-1, 4, 10], "sum": 13}`
- URL: `http://127.0.0.1:8000/sum/1,,2` $\rightarrow$ `404 Not Found`

### Bài 7: GET & POST Login
```bash
curl -X POST http://127.0.0.1:8000/login
curl -i -X PUT http://127.0.0.1:8000/login
```

### Bài 8: Thông tin Request
```bash
curl "http://127.0.0.1:8000/info?x=1&y=2"
curl -X POST "http://127.0.0.1:8000/info?x=1&y=2"
```

### Bài 9: Máy tính qua URL
```bash
curl "http://127.0.0.1:8000/calc?a=5&b=3&op=add"
curl "http://127.0.0.1:8000/calc?a=5&b=0&op=div"   # Trả về 400 JSON chia cho 0
```

### Bài 10: API tiện ích
```bash
curl http://127.0.0.1:8000/api/time
curl "http://127.0.0.1:8000/api/random?min=1&max=50&count=5"
```

### Bài 11: Rút gọn link
```bash
curl -i http://127.0.0.1:8000/go/flask    # 302 Redirect
curl -i http://127.0.0.1:8000/go/sai_ma   # 404 Custom page
```

### Bài 12: Bộ đếm Counter
```bash
curl http://127.0.0.1:8000/counter
curl -X POST http://127.0.0.1:8000/counter
curl -X POST "http://127.0.0.1:8000/counter?step=5"
curl -i -X DELETE http://127.0.0.1:8000/counter
curl -i -X PUT http://127.0.0.1:8000/counter       # 405 Method Not Allowed
```
