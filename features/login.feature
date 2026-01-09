Feature: Kiểm thử chức năng đăng nhập

  Scenario Outline: Đăng nhập không thành công với thông tin không hợp lệ
    Given người dùng truy cập trang đăng nhập
    When người dùng nhập tên đăng nhập "<username>" và mật khẩu "<password>"
    And nhấn nút "Đăng nhập"
    Then hệ thống hiển thị thông báo lỗi "<expected_message>"

    Examples:
      | username              | password       | expected_message                                                                 |
      | user!@#              | Vietba"123     | Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu. |
      | 0987654321           | Vietba"123     | Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu. |
      | abc                  | Vietba"123     | Vui lòng nhập đúng định dạng Tên đăng nhập/Email (tên đăng nhập phải tối thiểu 4 ký tự) |
      | user.domain.com      | Vietba"123     | Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu. |
      | 12a10_phanthanhviet  | <EMPTY>        | Vui lòng nhập đầy đủ: Tên đăng nhập/Email và Mật khẩu                            |
      | 12a10_phanthanhviet  | abc1           | Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu. |
      | 12a10_phanthanhviet  | WrongPass1!    | Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu. Lưu ý: Nếu nhập mật khẩu sai quá 5 lần sẽ bị khóa tài khoản, bạn chỉ được nhập sai 1 lần nữa |

  Scenario: Đăng nhập thành công với thông tin hợp lệ
    Given người dùng truy cập trang đăng nhập
    When người dùng nhập tên đăng nhập "12a10_phanthanhviet" và mật khẩu "Vietba"123"
    And nhấn nút "Đăng nhập"
    Then hệ thống chuyển hướng đến trang chủ