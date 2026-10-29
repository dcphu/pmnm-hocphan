# Báo cáo: Phân tích sự rẽ nhánh từ MySQL sang MariaDB do xung đột lợi ích cộng đồng

## 1. Giới thiệu tổng quan
MySQL là hệ quản trị cơ sở dữ liệu quan hệ mã nguồn mở phổ biến nhất trên thế giới, được tạo ra vào năm 1995 bởi Michael "Monty" Widenius và công ty MySQL AB. MySQL đã trở thành nền tảng cốt lõi của ngăn xếp LAMP (Linux, Apache, MySQL, PHP/Perl/Python), thúc đẩy sự bùng nổ của mạng Internet trong những năm đầu thập niên 2000. Tuy nhiên, một bước ngoặt lịch sử đã diễn ra khi Sun Microsystems mua lại MySQL AB vào năm 2008 với giá 1 tỷ USD, và sau đó chỉ hai năm (2010), Oracle Corporation tiếp tục thâu tóm Sun Microsystems. Sự kiện này đã dấy lên làn sóng lo ngại sâu sắc trong cộng đồng mã nguồn mở về tương lai của MySQL, dẫn đến sự ra đời của một trong những nhánh rẽ (fork) thành công nhất lịch sử: **MariaDB**.

## 2. Nguyên nhân mâu thuẫn và động cơ rẽ nhánh
Sự rẽ nhánh của MySQL không xuất phát từ bất đồng kỹ thuật đơn thuần, mà đến từ **sự xung đột nghiêm trọng về văn hóa quản trị và mô hình kinh doanh** giữa tập đoàn sở hữu và cộng đồng mã nguồn mở:
- **Nỗi sợ bị thâu tóm và đóng mã**: Oracle vốn là tập đoàn sở hữu cơ sở dữ liệu thương mại đóng mã lớn nhất thế giới (Oracle Database). Việc Oracle nắm quyền kiểm soát MySQL khiến cộng đồng và các đối tác lớn lo ngại tập đoàn này sẽ kìm hãm sự phát triển của MySQL hoặc biến nó thành một phiên bản giới hạn nhằm buộc khách hàng phải mua sản phẩm thương mại đắt đỏ của Oracle.
- **Tính minh bạch bị thu hẹp**: Sau khi tiếp quản, Oracle dần hạn chế các thông tin cập nhật công khai. Họ ngừng công bố công khai các ca kiểm thử hồi quy (regression test cases), giảm tính tương tác trong việc xử lý các lỗi bảo mật từ cộng đồng và chuyển nhiều tính năng nâng cao vào phiên bản trả phí "MySQL Enterprise".
- **Hành động của tác giả gốc**: Michael "Monty" Widenius cảm thấy triết lý mở của dự án bị đe dọa nghiêm trọng. Ông đã phát động chiến dịch "Save MySQL" và vào năm 2009, ông cùng các nhà phát triển kỳ cựu của MySQL quyết định rẽ nhánh tạo ra **MariaDB** (đặt theo tên con gái út của ông là Maria, tương tự như MySQL được đặt theo con gái My).

## 3. Quá trình phát triển và chiến lược của MariaDB
Để cạnh tranh và thuyết phục người dùng chuyển đổi, đội ngũ sáng lập MariaDB đã áp dụng các chiến lược hết sức khôn ngoan:
- **Tương thích thay thế trực tiếp (Drop-in Replacement)**: MariaDB được thiết kế để tương thích hoàn toàn 1:1 với MySQL từ cấu trúc lệnh, API, giao thức kết nối cho đến cấu trúc tệp lưu trữ. Quản trị viên hệ thống có thể gỡ bỏ MySQL và cài đặt MariaDB mà không cần sửa đổi bất kỳ dòng mã nguồn ứng dụng nào.
- **Đổi mới kỹ thuật vượt trội**: MariaDB tích hợp nhanh chóng các công cụ lưu trữ (storage engines) tối ưu mới như Aria, XtraDB thay thế cho InnoDB truyền thống, giúp cải thiện đáng kể tốc độ truy vấn và độ bền vững dữ liệu.
- **Bảo đảm mô hình quản trị công bằng**: Năm 2012, Michael Widenius thành lập **MariaDB Foundation** – một tổ chức phi lợi nhuận độc lập nhằm nắm giữ thương hiệu và định hướng phát triển dự án, đảm bảo MariaDB sẽ luôn miễn phí, mở và không bao giờ bị thâu tóm bởi bất kỳ một tập đoàn đơn lẻ nào.

## 4. Kết quả và bài học rút ra
Sự rẽ nhánh này đã tạo nên một làn sóng dịch chuyển khổng lồ. Hàng loạt bản phân phối Linux hàng đầu thế giới như Red Hat Enterprise Linux (RHEL), CentOS, Debian, Fedora, Arch Linux và các gã khổng lồ công nghệ như Google, Wikipedia, WordPress đã chính thức loại bỏ MySQL mặc định để chuyển sang dùng MariaDB.

**Bài học quan trọng cho hệ sinh thái mã nguồn mở:**
1. **Sức mạnh của quyền tự do rẽ nhánh (Forking right)**: Bản quyền mã nguồn mở (GPL) chính là tấm khiên bảo vệ người dùng. Khi chủ sở hữu thương mại tìm cách độc quyền hoặc kìm hãm sự phát triển, cộng đồng hoàn toàn có quyền lực tạo ra một nhánh phát triển mới để bảo tồn tính tự do của phần mềm.
2. **Cân bằng giữa thương mại hóa và cộng đồng**: Các doanh nghiệp muốn mua lại các dự án nguồn mở cần phải tôn trọng tính minh bạch và lắng nghe cộng đồng. Sự áp đặt độc quyền sẽ ngay lập tức kích hoạt phản ứng tẩy chay và đẩy người dùng sang các giải pháp thay thế tự do hơn.

