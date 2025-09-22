from playwright.sync_api import Page, expect  # type hint cho Pylance

class StuDy:
    def __init__(self, page: Page):  # page thay cho driver
        self.page = page
        self.menu_study = page.get_by_role("link", name="Học tập")
        self.lop_1 = page.get_by_role("link", name="Lớp 1")
        self.lop_12 = page.get_by_role("link", name="Lớp 12")
        self.DH_CD = page.get_by_role("link", name="Lớp 13")
        ###########################################################
        # chọn 1 bài toán lớp 1 cái này có thể verify click
        self.math_1 = page.get_by_role(
            "link",
            name="Toán lớp 1 (Hỗ trợ học bộ Kết nối tri thức với cuộc sống)"
        )
        # Chọn bài học từ bài toán lớp 1
        self.lesson_1 = page.get_by_role("link", name="Bài 1: Các số 0, 1, 2, 3, 4, 5")
        # Lý thuyết
        self.theory = page.get_by_role("link", name="Các số 0, 1, 2, 3, 4, 5")
        # Thực hành
        self.practice = page.locator('a[title="[Luyện tập] Nhận biết các số từ 0 đến 5"]')
        # Nút hướng dẫn làm PPT
        self.verify_theory = page.get_by_role("link", name="Hướng dẫn làm PPT")
        # verify pratice nút nộp bài
        self.verify_practice = page.locator("button.btn.olm-btn-primary.btn-done")
        # Xác nhận nộp bài
        self.submit = page.locator("button.btn.btn-confirm.olm-btn-two")
        # verify khi nộp bài
        self.verify_submit = page.locator("h3.review")
        ####################################################
        # locator lớp 12
        self.course_12 = page.locator("h1.fw-700.font-lg.mr-2")
        # Bộ sách chọn
        self.math_12_1 = page.get_by_role(
            "link",
            name="Toán 12 (Hỗ trợ học bộ Kết nối tri thức với cuộc sống)"
        )
        # Nếu khóa học này đã chọn trước đó sẽ có chữ đang học
        self.studying = page.locator('//span[normalize-space()="Đang học"]')
        # chọn tính đơn điệu của hàm số
        self.studying_unit1 = page.get_by_role(
            "link",
            name="Bài 1. Tính đơn điệu và cực trị của hàm số"
        )
        # Lý thuyết
        self.theory_12 = page.get_by_role(
            "link",
            name="Xét tính đơn điệu khi biết đồ thị hàm số hoặc bảng biến thiên"
        )
        # Thực hành
        self.practice_12 = page.get_by_role("link", name="Xác định cực trị của hàm số")
        # Vào bài lý thuyết
        self.goto_theory_12 = page.locator(
            '//h1[normalize-space()="Xét tính đơn điệu khi biết đồ thị hàm số hoặc bảng biến thiên"]'
        )
        # Khi đã vào học trc đó sẽ có nút tiếp tục xem
        self.continue_study = page.locator("#btn-pause")
        # Khi chưa có Vi[ mà ấn học lại video
        self.studying_again_msg = page.locator(
            '//div[normalize-space()="Để làm lại bài, hãy nhờ giáo viên xóa bài cũ hoặc nâng cấp lên tài khoản VIP."]'
        )
        # Nút học lại video
        self.studying_again = page.get_by_role("link", name="Học lại video")
        #######################################
        # Nút Báo lỗi
        self.report_error = page.locator("#btn-send-err")
        # Verify vào cửa sổ báo lỗi
        self.verify_report = page.locator('//label[normalize-space()="Loại lỗi:"]')
        # checkbox Hình Ảnh
        self.checkbox_img = page.locator("#type-feedback-1")
        # checkbox Âm thanh
        self.checkbox_audio = page.locator("#type-feedback-2")
        # Msg thông báo khi làm ppt khi là tài khoản học sinh
        # arena nội dung click vào đó rồi mới nhập nội dung
        self.arena_content = page.locator(
            "//div[@role='textbox' and @contenteditable='true' and contains(@class,'ContentEditable__root')]"
        )
        # Báo lỗi thành công
        self.msg_report_success = page.locator(
            "button.btn.olm-btn-primary.text-white.btn-submit.mb-0"
        )
        # Hủy báo lỗi
        self.cancel_report = page.locator("button.btn.btn-secondary.btn-cancel")
        #####################################
        # thông báo ppt
        self.msg_ppt = page.locator(
            "h3.fw-600.text-grey-900.display2-size.display4-md-size"
        )
        # nút PPT
        self.btn_ppt = page.get_by_role("link", name="Hướng dẫn làm PPT")
        #####################################
        # arena nhập bình luận nên cuộn xuống
        self.arena_content_comment = page.locator("p.card-text.text-grey-600")
        # nút tạo câu hỏi
        self.btn_create_question = page.locator(
            '//button[normalize-space()="Tạo câu hỏi"]'
        )
        # Nút hủy bình luận
        self.btn_cancel_comment = page.locator("button.btn.olm-btn-four")
        # Lịch sử làm bài
        #####################################################################################
        # Đăng ký khóa học
        self.bt_register_course = page.locator(
            '//span[normalize-space()="Đăng ký khóa học"]/ancestor::div[contains(@class,"add-more-course")]'
        )
        # nút checkbox lớp 9 và xử lý khi nó đã được tích
        self.checkbox_class_9 = page.locator("#select-grade-9")
        self.continue_class_9 = page.get_by_role("button",name="Tiếp tục")
        # checkbox toán 9 hỗ trợ
        self.checkbox_math_9 = page.locator("#select-course-880191141")
        # Nút Hoàn thành
        self.btn_complete = page.locator('//button[normalize-space()="Hoàn thành"]')
        # Verify khi hoàn thành
        self.verify_complete = page.get_by_role(
            "link",
            name="Toán 9 (Hỗ trợ học bộ Kết nối tri thức với cuộc sống)"
        )

    ################################################
    # kiểm tra checkbox sau toán lớp 9
    def check_click_math_9(self):
        # Nếu chưa được tick thì click
        if not self.page.locator("#select-course-880191141").is_checked():
            self.page.locator("#select-course-880191141").click()

    # nếu đã tích thì không click nữa
    def check_click_9(self):
        if not self.page.locator("#select-grade-9").is_checked():
            self.page.locator("#select-grade-9").click()

    #xem khóa học lớp 1 chọn lý thuyết
    def check_class_1_theory(self):
        self.menu_study.click()
        self.lop_1.click()
        expect(self.page).to_have_url("https://olm.vn/lop-1")
        expect(self.math_1).to_be_visible()
        self.math_1.click()
        self.lesson_1.click()
        expect(self.page).to_have_url("https://olm.vn/bg/toan-1-ket-noi-tri-thuc-voi-cuoc-song/")
        expect(self.theory).to_be_visible()
        self.theory.click()
        expect(self.verify_theory).to_be_visible()
    #xem khóa học lớp 1 chọn thực hành
    def check_class_1_practice(self):
        self.menu_study.click()
        self.lop_1.click()
        expect(self.page).to_have_url("https://olm.vn/lop-1")
        expect(self.math_1).to_be_visible()
        self.math_1.click()
        self.lesson_1.click()
        expect(self.page).to_have_url("https://olm.vn/bg/toan-1-ket-noi-tri-thuc-voi-cuoc-song/")
        expect(self.practice).to_be_visible()
        self.practice.click()
        expect(self.verify_practice).to_be_visible()
        self.verify_practice.click()
        self.submit.click()
        self.verify_submit.is_visible()
        
    #xem khóa học lớp 12 
    def check_class_12(self):
        self.menu_study.click()
        self.lop_12.click()
        #expect(self.page).to_have_url("https://olm.vn/lop-12")
        expect(self.course_12).to_be_visible()
        self.course_12.click()
        expect(self.math_12_1).to_be_visible()
        self.math_12_1.click()
        expect(self.studying).to_be_visible()
        self.studying.click()
        expect(self.studying_unit1).to_be_visible()
        self.studying_unit1.click()
        expect(self.goto_theory_12).to_be_visible()
        self.goto_theory_12.click()
        self.continue_study.click()
        expect(self.continue_study).to_be_visible()        
        self.studying_again.click()
        expect(self.studying_again_msg).to_be_visible()
        
        
    #đăng ký khóa học lớp 9
    def reGister_9(self):
        self.menu_study.click()
        self.bt_register_course.scroll_into_view_if_needed()
        self.check_click_math_9
        self.continue_class_9
        self.check_click_9
        self.btn_complete
        expect(self.verify_complete).to_be_visible()
        