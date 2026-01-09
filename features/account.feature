Feature: Cài đặt tài khoản

  Scenario: Truy cập cài đặt tài khoản
    Given người dùng đã đăng nhập
    When người dùng chọn mục "Cài đặt tài khoản" từ menu
    Then hệ thống hiển thị giao diện cài đặt tài khoản

  Scenario: Chọn tỉnh/thành phố
    Given người dùng đang ở giao diện cài đặt tài khoản
    When người dùng chọn một tỉnh/thành phố
    Then hệ thống hiển thị danh sách xã/phường tương ứng

  Scenario: Chọn xã/phường
    Given người dùng đã chọn tỉnh/thành phố
    When người dùng chọn một xã/phường
    Then hệ thống hiển thị danh sách trường học tương ứng

  Scenario: Chọn trường học
    Given người dùng đã chọn xã/phường
    When người dùng chọn một trường học
    Then hệ thống hiển thị tên trường đã chọn
    And hiển thị thông báo "Cập nhật trường thành công" ở góc trái màn hình

  Scenario: Tìm kiếm trường học theo tên
    Given người dùng đang ở giao diện cài đặt tài khoản
    When người dùng nhập tên trường hoặc tên gần đúng vào ô tìm kiếm
    Then hệ thống hiển thị kết quả tìm kiếm nếu có
    And nếu không có kết quả thì vẫn giữ thông tin của lần tìm kiếm gần nhất

  Scenario: Chọn nhận thông báo từ OLM
    Given người dùng đang ở giao diện cài đặt tài khoản
    When người dùng chọn checkbox nhận thông báo qua Zalo và email
    Then hệ thống cập nhật ngay lập tức
    And hiển thị thông báo "Cập nhật trường thành công"

  # Scenario: Khóa chức năng nhắn tin
  #   Given người dùng đang ở giao diện cài đặt tài khoản
  #   When người dùng chọn checkbox khóa chức năng nhắn tin
  #   Then hệ thống hiển thị thông báo xác nhận
  #   And nếu xác nhận thì chức năng nhắn tin sẽ bị xoá và không thể chọn lại

  Scenario: Chọn lớp học
    Given người dùng đang ở giao diện cài đặt tài khoản
    When người dùng chọn một hoặc nhiều lớp học
    Then hệ thống cập nhật ngay lập tức
    And hiển thị thông báo "Cập nhật trường thành công"

  Scenario: Chọn môn học
    Given người dùng đang ở giao diện cài đặt tài khoản
    When người dùng chọn một hoặc nhiều môn học
    Then hệ thống mở rộng ô chứa môn học nếu cần
    And người dùng có thể xoá môn bằng biểu tượng dấu X

  Scenario: Chọn bộ sách đang học
    Given người dùng đang ở giao diện cài đặt tài khoản
    When người dùng chọn một hoặc nhiều bộ sách
    Then hệ thống cập nhật ngay lập tức
    And hiển thị thông báo "Cập nhật trường thành công"
