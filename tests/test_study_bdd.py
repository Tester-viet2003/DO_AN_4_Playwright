import pytest
import re
import allure
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.Study_page import StuDy
from utils.logger_utils import get_logger

logger = get_logger("study_test")


scenarios("../features/Study.feature")



@pytest.fixture
def study_page(login, base_url):
    """Dùng page đã đăng nhập sẵn."""
    return StuDy(login, base_url)


# ================================================================
# SCENARIO 1: Truy cập học bài khi chưa đăng nhập
# ================================================================
@pytest.fixture
def study_page_guest(setup, base_url):
    """Trang học bài khi chưa đăng nhập."""
    return StuDy(setup, base_url)

@given("người dùng chưa đăng nhập")
def user_not_logged_in(study_page_guest):
    with allure.step("Người dùng chưa đăng nhập"):
        study_page_guest.page.goto(study_page_guest.url)
        logger.info(" Người dùng chưa đăng nhập.")

@when('người dùng truy cập vào mục "Học bài" trên thanh menu')
def access_study_menu(study_page_guest):
    with allure.step("Người dùng truy cập menu Học bài"):
        study_page_guest.study.click()
        logger.info(" Click menu 'Học bài'.")

@then("hệ thống hiển thị danh sách lớp theo khối học")
def verify_class_list(study_page_guest):
    with allure.step("Hệ thống hiển thị danh sách lớp học"):
        expect(study_page_guest.lbclass1).to_be_visible()
        expect(study_page_guest.lbclass9).to_be_visible()
        expect(study_page_guest.lbclass12).to_be_visible()
        logger.info(" Hiển thị danh sách lớp thành công.")

@then("người dùng có thể luyện tập tối đa 5 lần")
def practice_limit_info():
    with allure.step("Kiểm tra giới hạn luyện tập "):
        logger.info("  Kiểm tra giới hạn luyện tập tối đa 5 lần.")


# ================================================================
# SCENARIO 3: Hiển thị thông tin sau khi đăng nhập
# ================================================================
@given("người dùng đã đăng nhập và đã đăng ký khóa học")
def logged_in():
    with allure.step("Người dùng đã đăng nhập và có khóa học"):
        logger.info(" Người dùng đã đăng nhập và có khóa học.")

@when('người dùng truy cập mục "Học bài"')
def open_study_after_login(study_page):
    with allure.step("Người dùng truy cập mục Học bài sau khi đăng nhập"):
        study_page.study.click()
        logger.info(" Click menu 'Học bài' sau đăng nhập.")

@then("hệ thống hiển thị bài học tuần này của OLM")
def verify_weekly_lessons(study_page):
    with allure.step("Hệ thống hiển thị bài học tuần này"):
        expect(study_page.study_today).to_be_visible()
        logger.info(" Bài học tuần này hiển thị.")

@then("hiển thị danh sách các khóa học đã đăng ký")
def verify_course_list(study_page):
    with allure.step("Hệ thống hiển thị danh sách khóa học"):
        expect(study_page.course_studying).to_be_visible()
        logger.info(" Danh sách khóa học đã đăng ký hiển thị.")

@then('người dùng có thể click "Xem tất cả" hoặc xóa khóa học')
def click_view_all(study_page):
    with allure.step("Người dùng click 'Xem tất cả' khóa học"):
        study_page.btn_view_all.first.click(force=True)
        logger.info(" Click 'Xem tất cả' thành công.")


# ================================================================
# SCENARIO 4: Xem nội dung khóa học
# ================================================================
@given("người dùng đã đăng nhập")
def user_logged_in():
    with allure.step("Người dùng đã đăng nhập"):
        logger.info(" Người dùng đã đăng nhập sẵn.")

@when("người dùng click vào một khóa học")
def open_course(study_page):
    with allure.step("Người dùng click vào khóa học"):
        study_page.bt_continue_viewcourse.click(force=True)
        logger.info(" Click vào khóa học.")

@then("hệ thống hiển thị nội dung chi tiết của khóa học")
def verify_course_detail(study_page):
    with allure.step("Hệ thống hiển thị nội dung chi tiết khóa học"):
        expect(study_page.practice_class9).to_be_visible()
        logger.info(" Hiển thị chi tiết nội dung khóa học.")


# ================================================================
# SCENARIO 5: Chọn bài học và chuyển sang giao diện học
# ================================================================
@given("người dùng chọn bài học và chọn 'Lý thuyết' hoặc 'Luyện tập'")
def choose_lesson(study_page):
    with allure.step("Người dùng chọn bài học và chế độ học"):
        study_page.seLect_class_9()
        logger.info(" Chọn bài học lớp 9.")

@when('người dùng chọn bài học và chọn "Lý thuyết" hoặc "Luyện tập"')
def select_lesson_and_mode(study_page):
    with allure.step("Người dùng chọn chế độ Lý thuyết hoặc Luyện tập"):
        study_page.seLect_class_9()
        logger.info(" Người dùng đã chọn bài học và chế độ học.")

@then("hệ thống chuyển sang giao diện học tương ứng")
def verify_study_interface(study_page):
    with allure.step("Hệ thống chuyển sang giao diện học"):
        expect(study_page.practice_again).to_be_visible()
        logger.info(" Chuyển sang giao diện học thành công.")


# ================================================================
# SCENARIO 6: Học lý thuyết
# ================================================================
@given("người dùng chọn học lý thuyết")
def open_theory(study_page):
    with allure.step("Người dùng chọn học lý thuyết"):
        study_page.seLect_class_12()
        logger.info(" Người dùng chọn học lý thuyết lớp 12.")

@when("nội dung bài học được hiển thị")
def verify_theory_content(study_page):
    with allure.step("Nội dung bài học hiển thị"):
        expect(study_page.continue_view).to_be_visible()
        logger.info(" Nội dung lý thuyết hiển thị.")

@then("hệ thống hiển thị bộ đếm thời gian, nút in bài, câu hỏi luyện tập đan xen")
def theory_elements():
    with allure.step("Kiểm tra phần tử hiển thị trong lý thuyết (manual)"):
        logger.info(" Kiểm tra bộ đếm, nút in bài (manual).")

@then("hiển thị chức năng hỏi đáp và bình luận")
def qa_comment_section():
    with allure.step("Kiểm tra khu vực hỏi đáp và bình luận (manual)"):
        logger.info(" Kiểm tra khu vực hỏi đáp & bình luận (manual).")


# ================================================================
# SCENARIO 8: Nộp bài khi chưa chọn đáp án
# ================================================================
@given("người dùng đang làm bài luyện tập")
def doing_practice(study_page):
    with allure.step("Người dùng đang làm bài luyện tập"):
        study_page.seLect_class_9()
        logger.info(" Người dùng đang làm bài luyện tập.")

@when('người dùng click "Nộp bài" mà chưa chọn đáp án')
def click_submit_without_answer(study_page):
    with allure.step("Người dùng click 'Nộp bài' khi chưa chọn đáp án"):
        study_page.submit_btn.click()
        logger.info(" Người dùng click 'Nộp bài' khi chưa chọn đáp án.")

@then("hệ thống hiển thị popup cảnh báo")
def verify_popup():
    with allure.step("Kiểm tra popup cảnh báo (manual)"):
        logger.info(" (Manual) Kiểm tra popup cảnh báo khi chưa chọn đáp án.")


# ================================================================
# SCENARIO 9: Xem thống kê học bạ
# ================================================================
@given("người dùng đã học bài")
def studied():
    with allure.step("Người dùng đã học bài (giả lập)"):
        logger.info(" Người dùng đã học bài (giả lập).")

@when('người dùng chọn "Học bạ"')
def open_report(study_page):
    with allure.step("Người dùng chọn mục Học bạ"):
        study_page.study_hb()
        logger.info(" Người dùng click 'Học bạ'.")

@then("hệ thống hiển thị thống kê kết quả học tập")
def verify_report(study_page):
    with allure.step("Hệ thống hiển thị thống kê học bạ"):
        expect(study_page.check_study).to_be_visible()
        logger.info(" Học bạ hiển thị thành công.")


# ================================================================
# SCENARIO 10: Đăng ký khóa học mới
# ================================================================
@given("người dùng đã đăng nhập")
def logged_in_for_register():
    with allure.step("Người dùng đã đăng nhập"):
        logger.info(" Người dùng đã đăng nhập.")

@when('người dùng cuộn xuống phần "Đăng ký khóa học"')
def scroll_to_register(study_page):
    with allure.step("Người dùng cuộn xuống phần Đăng ký khóa học"):
        study_page.click_btn_dkkh()
        logger.info(" Cuộn xuống phần đăng ký khóa học.")

@when("chọn lớp và khóa học")
def select_class_course(study_page):
    with allure.step("Người dùng chọn lớp và khóa học"):
        study_page.chon_checkbox("Lớp 9")
        study_page.click_continue_dk()
        study_page.click_finish_dk()
        logger.info(" Người dùng đã đăng ký khóa học mới.")

@then("hệ thống hiển thị danh sách khóa học đã đăng ký")
def verify_registered_course(study_page):
    with allure.step("Hệ thống hiển thị khóa học mới sau đăng ký"):
        expect(study_page.vry_finish9).to_be_visible()
        logger.info(" Khóa học mới hiển thị sau khi đăng ký.")
