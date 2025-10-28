# OLM.vn – Test Cases: Đăng nhập (Môi trường thực tế)

## Điều kiện tiên quyết
- Mở trình duyệt và truy cập **trang chủ** https://olm.vn/
- Click nút **Đăng nhập** trên header để mở form đăng nhập

## Tài khoản kiểm thử
- **Username hợp lệ:** 12a10_phanthanhviet
- **Mật khẩu hợp lệ (môi trường thực tế):** Vietba"123

## Locator Mapping

| Alias                 | Locator / HTML                                                                                                                                            | Ghi chú |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [open_login_button]   | `<a href="https://olm.vn/dangnhap?redirect=..." class="header-btn fw-500 btn olm-btn-primary ...">Đăng nhập</a>`                                            | Nút mở form đăng nhập trên header |
| [username_input]      | `<input type="text" class="style2-input pl-5 form-control text-grey-900 font-xsss fw-600" name="username" required="">`                                     | Trường nhập tên đăng nhập hoặc email |
| [password_input]      | `<input type="Password" class="style2-input pl-5 form-control text-grey-900 font-xss ls-3 input-password" name="password" required="">`                      | Trường mật khẩu |
| [toggle_password]     | `<i class="position-absolute left-unset right-10-p cursor-pointer far fa-eye" onclick="MAIN_UI.showPassword(this)"></i>`                                    | Icon mắt ẩn/hiện mật khẩu |
| [remember_me]         | `<input type="checkbox" class="custom-control-input mt-2" name="remember" id="remember-me" checked="">`                                                     | Checkbox Ghi nhớ đăng nhập |
| [login_button]        | `<button class="form-control btn-submit text-center style2-input text-white fw-600 olm-btn-primary border-0 p-0 ">Đăng nhập</button>`                       | Nút Đăng nhập trong form |
| [forgot_link]         | `<a href="https://olm.vn/quen-mat-khau" class="fw-600 font-xsss olm-text-link mt-1 float-right">Quên mật khẩu</a>`                                          | Link Quên mật khẩu |
| [register_link]       | `<a href="https://olm.vn/dang-ky" class="fw-700 ml-1 olm-text-link">Đăng ký</a>`                                                                            | Link Đăng ký |
| [google_login]        | `<a href="https://olm.vn/social/google/redirect" class="form-control style2-input text-white fw-600 bg-youtube border-0 p-0 mb-2">…</a>`                     | Nút Đăng nhập bằng Google |
| [error_banner_empty]  | `<div class="alert alert-danger mb-2" role="alert"><b>Vui lòng nhập đầy đủ: <b>Tên đăng nhập/Email</b> và <b>Mật khẩu</b></b></div>`                        | Thông báo khi bỏ trống |
| [error_banner_short]  | `<b>Vui lòng nhập đúng định dạng <b>Tên đăng nhập/Email</b> (tên đăng nhập phải tối thiểu 4 ký tự)</b>`                                                     | Thông báo tên đăng nhập quá ngắn |
| [error_banner_wrong]  | `<div class="box-error"><div class="alert alert-danger mb-2" role="alert"><b>Tên đăng nhập hoặc mật khẩu của bạn không chính xác…</b></div></div>`           | Thông báo sai tài khoản/mật khẩu |
| [user_avatar]         | `<div class="d-flex align-items-center">…<span class="ml-1 font-weight-bold text-white opacity-header…">Phan Thanh Việt</span></div>`                        | Dấu hiệu đã đăng nhập thành công |

## Test Case Chi Tiết

> **Điều kiện tiên quyết chung cho tất cả:**  
> Mở trình duyệt → truy cập https://olm.vn/ → click **Đăng nhập** trên header để mở form đăng nhập.

| ID | Mô tả | Bước thực hiện | Kết quả mong đợi |
|----|------|---------------|------------------|
| FUNC-LOGIN-001 | Đăng nhập thành công bằng username | 1. Nhập `12a10_phanthanhviet` vào [username_input]. <br>2. Nhập `Vietba"123` vào [password_input]. <br>3. Click [login_button]. | 3.1 Chuyển về trang chủ, hiển thị [user_avatar]. |
| FUNC-LOGIN-002 | Đăng nhập thành công bằng email | 1. Nhập email hợp lệ đã đăng ký vào [username_input]. <br>2. Nhập `Vietba"123` vào [password_input]. <br>3. Click [login_button]. | 3.1 Chuyển về trang chủ, hiển thị [user_avatar]. |
| FUNC-LOGIN-003 | Bỏ trống cả hai trường | 1. Để trống [username_input] và [password_input]. <br>2. Click [login_button]. | 2.1 Hiển thị [error_banner_empty]. |
| FUNC-LOGIN-004 | Username chỉ khoảng trắng | 1. Nhập toàn khoảng trắng vào [username_input]. <br>2. Nhập `Vietba"123`. <br>3. Click [login_button]. | 3.1 Hiển thị [error_banner_short]. |
| FUNC-LOGIN-005 | Username chứa ký tự đặc biệt | 1. Nhập `user!@#` vào [username_input]. <br>2. Nhập `Vietba"123`. <br>3. Click [login_button]. | 3.1 Hiển thị [error_banner_short]. |
| FUNC-LOGIN-006 | Username là số điện thoại | 1. Nhập `0987654321` vào [username_input]. <br>2. Nhập `Vietba"123`. <br>3. Click [login_button]. | 3.1 Hiển thị lỗi username không hợp lệ. |
| FUNC-LOGIN-007 | Username/email < 4 ký tự | 1. Nhập `abc` vào [username_input]. <br>2. Nhập `Vietba"123`. <br>3. Click [login_button]. | 3.1 Hiển thị [error_banner_short]. |
| FUNC-LOGIN-008 | Username/email > 155 ký tự | 1. Nhập chuỗi 156 ký tự vào [username_input]. <br>2. Nhập `Vietba"123`. <br>3. Click [login_button]. | 3.1 Hiển thị lỗi vượt quá 155 ký tự. |
| FUNC-LOGIN-009 | Email sai định dạng | 1. Nhập `user.domain.com` vào [username_input]. <br>2. Nhập `Vietba"123`. <br>3. Click [login_button]. | 3.1 Hiển thị [error_banner_short]. |
| FUNC-LOGIN-010 | Mật khẩu trống | 1. Nhập `12a10_phanthanhviet` vào [username_input]. <br>2. Để trống [password_input]. <br>3. Click [login_button]. | 3.1 Hiển thị [error_banner_empty]. |
| FUNC-LOGIN-011 | Mật khẩu thiếu yêu cầu | 1. Nhập `12a10_phanthanhviet`. <br>2. Nhập `abc1` vào [password_input]. <br>3. Click [login_button]. | 3.1 Hiển thị thông báo yêu cầu mật khẩu tối thiểu 4 ký tự gồm chữ hoa, số, ký tự đặc biệt. |
| FUNC-LOGIN-012 | Sai mật khẩu | 1. Nhập `12a10_phanthanhviet`. <br>2. Nhập `WrongPass1!` vào [password_input]. <br>3. Click [login_button]. | 3.1 Hiển thị [error_banner_wrong]. |
| FUNC-LOGIN-013 | Icon “mắt” ẩn/hiện mật khẩu | 1. Nhập bất kỳ mật khẩu. <br>2. Click [toggle_password] 1 lần. <br>3. Click lần 2. | 3.1 Trường mật khẩu chuyển password ↔ text, giữ nguyên giá trị. |
| FUNC-LOGIN-014 | Submit bằng phím Enter | 1. Nhập `12a10_phanthanhviet`. <br>2. Nhập `Vietba"123`. <br>3. Nhấn Enter. | 3.1 Đăng nhập thành công như khi click [login_button]. |
| FUNC-LOGIN-015 | Ghi nhớ đăng nhập | 1. Nhập `12a10_phanthanhviet`. <br>2. Nhập `Vietba"123`. <br>3. Tick [remember_me]. <br>4. Click [login_button]. <br>5. Đóng trình duyệt, mở lại https://olm.vn/. | 5.1 Vẫn hiển thị [user_avatar] (giữ trạng thái đăng nhập). |
| FUNC-LOGIN-016 | Quên mật khẩu | 1. Click [forgot_link]. | 1.1 Chuyển đến giao diện lấy lại mật khẩu. |
| FUNC-LOGIN-017 | Đăng ký tài khoản mới | 1. Click [register_link]. | 1.1 Chuyển đến giao diện đăng ký. |
| FUNC-LOGIN-018 | Đăng nhập bằng Google – thành công | 1. Click [google_login]. <br>2. Chọn tài khoản Google hợp lệ, chấp thuận. | 2.1 Đăng nhập thành công, về trang chủ. |
| FUNC-LOGIN-019 | Đăng nhập bằng Google – hủy | 1. Click [google_login]. <br>2. Hủy hoặc đóng popup. | 2.1 Ở lại trang đăng nhập, không đăng nhập thành công. |
