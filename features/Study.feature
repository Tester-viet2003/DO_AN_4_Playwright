Feature: Quản lý khóa học

  Scenario: Truy cập học bài khi chưa đăng nhập
    Given người dùng chưa đăng nhập
    When người dùng truy cập vào mục "Học bài" trên thanh menu
    Then hệ thống hiển thị danh sách lớp theo khối học
    And người dùng có thể luyện tập tối đa 5 lần

  Scenario: Hiển thị thông tin sau khi đăng nhập
    Given người dùng đã đăng nhập và đã đăng ký khóa học
    When người dùng truy cập mục "Học bài"
    Then hệ thống hiển thị bài học tuần này của OLM
    And hiển thị danh sách các khóa học đã đăng ký
    And người dùng có thể click "Xem tất cả" hoặc xóa khóa học

  Scenario: Xem nội dung khóa học
    Given người dùng đã đăng nhập
    When người dùng click vào một khóa học
    Then hệ thống hiển thị nội dung chi tiết của khóa học

  Scenario: Chọn bài học và chuyển sang giao diện học
    Given người dùng đã đăng nhập
    When người dùng chọn bài học và chọn "Lý thuyết" hoặc "Luyện tập"
    Then hệ thống chuyển sang giao diện học tương ứng

  Scenario: Học lý thuyết
    Given người dùng chọn học lý thuyết
    When nội dung bài học được hiển thị
    Then hệ thống hiển thị bộ đếm thời gian, nút in bài, câu hỏi luyện tập đan xen
    And hiển thị chức năng hỏi đáp và bình luận

  Scenario: Nộp bài khi chưa chọn đáp án
    Given người dùng đang làm bài luyện tập
    When người dùng click "Nộp bài" mà chưa chọn đáp án
    Then hệ thống hiển thị popup cảnh báo


  Scenario: Xem thống kê học bạ
    Given người dùng đã học bài
    When người dùng chọn "Học bạ"
    Then hệ thống hiển thị thống kê kết quả học tập

  Scenario: Đăng ký khóa học mới
    Given người dùng đã đăng nhập
    When người dùng cuộn xuống phần "Đăng ký khóa học"
    And chọn lớp và khóa học
    Then hệ thống hiển thị danh sách khóa học đã đăng ký
