Feature: Chức năng hỏi bài

  Scenario: Truy cập chức năng hỏi bài
    Given học viên đã đăng nhập
    When học viên chọn mục "Hỏi bài" từ menu
    Then hệ thống hiển thị danh sách câu hỏi của người dùng khác theo thứ tự mới nhất
    And hiển thị bộ lọc lớp học và môn học ở thanh menu bên trái

  Scenario: Xem danh sách câu hỏi mới nhất
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn tiêu chí "Mới nhất"
    Then hệ thống hiển thị danh sách các câu hỏi được đăng gần đây nhất

  Scenario: Xem câu hỏi hay
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn tiêu chí "Câu hỏi hay"
    Then hệ thống hiển thị danh sách các câu hỏi được đánh giá cao hoặc được nhiều lượt tương tác

  Scenario: Xem câu hỏi VIP
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn tiêu chí "Câu hỏi VIP"
    Then hệ thống hiển thị danh sách các câu hỏi của tài khoản VIP được ưu tiên hiển thị

  Scenario: Lọc câu hỏi theo môn học
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn một môn học từ danh sách
    Then hệ thống hiển thị danh sách câu hỏi thuộc môn học đã chọn


  Scenario: Xem bảng xếp hạng hỏi đáp theo năm
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn mục "Xếp hạng theo năm"
    Then hệ thống hiển thị bảng xếp hạng người dùng theo điểm hỏi đáp
    And học viên có thể chọn bộ lọc theo môn học hoặc theo tuần/tháng/năm
  
  Scenario: Xem bảng xếp hạng hỏi đáp theo tháng
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn mục "Xếp hạng theo tháng"
    Then hệ thống hiển thị bảng xếp hạng người dùng theo điểm hỏi đáp
    And học viên có thể chọn bộ lọc theo môn học hoặc theo tuần/tháng/năm
  
  Scenario: Xem bảng xếp hạng hỏi đáp theo tuần
    Given học viên đang ở giao diện hỏi bài
    When học viên chọn mục "Xếp hạng theo tuần"
    Then hệ thống hiển thị bảng xếp hạng người dùng theo điểm hỏi đáp
    And học viên có thể chọn bộ lọc theo môn học hoặc theo tuần/tháng/năm
