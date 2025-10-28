# OLM – Test Case Automation (Thông tin & Cài đặt Tài khoản)

## Điều kiện chung
- Truy cập [https://olm.vn/](https://olm.vn/)
- Đăng nhập bằng:
  - **Username**: `12a10_phanthanhviet`
  - **Password**: `Vietba"123`
- Hover vào **Avatar/Tên tài khoản** để mở dropdown:
  - `span.ml-1.font-weight-bold.text-white.opacity-header.text-truncate.align-text-top.d-none.d-xl-inline-block.mw-100`
- Chọn menu theo từng test (Thông tin hoặc Cài đặt).

---

## 1️⃣ Thông tin tài khoản – Kiểm tra hiển thị & read-only

| ID | Mô tả | Bước thực hiện | Kết quả mong đợi |
|----|------|---------------|------------------|
| AUTO-INFO-001 | Xác minh các trường chỉ đọc | 1. Hover avatar → click **Thông tin** (`a[href="https://olm.vn/thong-tin-tai-khoan/info"]`). <br>2. Đọc giá trị các trường: Tên hiển thị, Tên đăng nhập, Email, Email phụ huynh, Số điện thoại. | 2.1 Tất cả trường hiển thị chính xác, thuộc tính readonly, không cho phép chỉnh sửa. |

---

## 2️⃣ Cài đặt tài khoản – Automation

| ID | Mô tả | Bước thực hiện | Locator chính | Kết quả mong đợi |
|----|------|---------------|--------------|------------------|
| AUTO-SET-001 | Chọn Tỉnh/Thành phố | 1. Hover avatar → click **Cài đặt tài khoản** (`a[href="https://olm.vn/thong-tin-tai-khoan/setting"]`). <br>2. Click dropdown Tỉnh/Thành phố và chọn **Hưng Yên**. | `span.select2-selection.select2-selection--single[aria-labelledby="select2-province-rx-container"]` | 2.1 Dropdown hiển thị “Hưng Yên”, toast “Cập nhật trường thành công”. |
| AUTO-SET-002 | Chọn Xã/Phường | 1. Ở trang Cài đặt tài khoản. <br>2. Click dropdown Xã/Phường và chọn 1 xã bất kỳ. | `span.select2-selection.select2-selection--single[aria-labelledby="select2-commune-ll-container"]` | 2.1 Danh sách Trường tương ứng được load. |
| AUTO-SET-003 | Chọn Trường | 1. Click dropdown Trường, chọn “Trường Tiểu học Hợp Hưng”. | `select.custom-select.select-address[name="school"]` | 1.1 Trường được chọn, toast “Cập nhật trường thành công”. |
| AUTO-SET-004 | Tìm kiếm trường hợp lệ | 1. Nhập tên trường hợp lệ vào ô tìm kiếm. | `input.form-control[name="search"]` | 1.1 Kết quả hiển thị khớp tên tìm kiếm. |
| AUTO-SET-005 | Tick/Untick nhận thông báo Zalo | 1. Tick/untick checkbox Zalo. | `input#subscribe-zalo[name="subscribe_zalo"]` | 1.1 Trạng thái thay đổi và lưu, toast “Cập nhật trường thành công”. |
| AUTO-SET-006 | Tick/Untick nhận thông báo Email | 1. Tick/untick checkbox Email. | `input#subscribe-email[name="subscribe"]` | 1.1 Trạng thái thay đổi và lưu, toast “Cập nhật trường thành công”. |
| AUTO-SET-007 | Chọn nhiều Lớp | 1. Tick nhiều checkbox lớp. | Ví dụ: `input#select-grade-1`, `input#select-grade-2` … | 1.1 Các lớp được chọn hiển thị và lưu thành công. |
| AUTO-SET-008 | Chọn nhiều Môn | 1. Mở dropdown môn (`span.select2-selection.select2-selection--multiple`). <br>2. Chọn 1 hoặc nhiều môn. | `span.select2-selection.select2-selection--multiple` | 2.1 Môn được thêm vào danh sách hiển thị. |
| AUTO-SET-009 | Xóa môn đã chọn | 1. Click icon X cạnh môn muốn xóa. | `span.select2-selection__choice__remove` | 1.1 Môn bị xóa khỏi danh sách, lưu tự động. |
| AUTO-SET-010 | Chọn nhiều Bộ sách | 1. Tick nhiều checkbox bộ sách. | Ví dụ: `input#book-student-0`, `input#book-student-1`, … | 1.1 Bộ sách đã chọn hiển thị và lưu thành công. |

---

## Ghi chú locator quan trọng
* **Toast cập nhật thành công**:  
  `div.toast-body.toast-message`  (text: “Cập nhật trường thành công”)
* **Menu Cài đặt**:  
  `a[href="https://olm.vn/thong-tin-tai-khoan/setting"]`

---

> File này chỉ giữ các test case **automation khả thi**.  
> Các chức năng xác thực email, xác thực số điện thoại, đổi mật khẩu, kết nối Zalo đã được **loại bỏ**.
