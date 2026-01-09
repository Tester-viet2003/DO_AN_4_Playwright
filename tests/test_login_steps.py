import pytest
import allure
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.logger_utils import get_logger

scenarios("../features/login.feature")
@pytest.fixture
def login_page(page, base_url):
    return LoginPage(page, base_url)

@given("người dùng truy cập trang đăng nhập")
def open_login_page(login_page):
    logger = get_logger("login_test")
    with allure.step("Người dùng truy cập trang đăng nhập"):
        logger.info("Mở trang đăng nhập OLM.vn")
        login_page.open()
        logger.info("Trang đăng nhập đã được mở thành công ")
def normalize(value):
    return "" if value in ["<EMPTY>", None] else value
@when(parsers.parse('người dùng nhập tên đăng nhập "{username}" và mật khẩu "{password}"'))
def fill_credentials(login_page, username, password):
    username = normalize(username)
    password = normalize(password)
    logger = get_logger("login_test")
    with allure.step(f"Nhập thông tin đăng nhập: username='{username}', password='******'"):
        logger.info(f"Nhập username: {username} và password: {password}")
        login_page.login(username, password)
        logger.info("Hoàn tất nhập thông tin đăng nhập")
@when('nhấn nút "Đăng nhập"')
def click_login(login_page):
    logger = get_logger("login_test")
    with allure.step("Nhấn nút 'Đăng nhập'"):
        logger.info("Nhấn nút Đăng nhập")
        logger.info("Đã nhấn nút Đăng nhập")


@then(parsers.parse('hệ thống hiển thị thông báo lỗi "{expected_message}"'))
def verify_error_message(login_page, expected_message):
    logger = get_logger("login_test")
    with allure.step("Kiểm tra thông báo lỗi hiển thị đúng"):
        actual = login_page.get_text_msg_error()
        
        # Log thô từ UI
        logger.info(f"Raw UI error message: {actual}")

        # ----------- FIX LỖI XUỐNG DÒNG & KHOẢNG TRẮNG -----------

        # Chuyển xuống dòng \n -> khoảng trắng
        actual_clean = actual.replace("\n", " ").replace("  ", " ").strip()
        expected_clean = expected_message.replace("\n", " ").replace("  ", " ").strip()

        logger.info(f"Clean UI error message: {actual_clean}")
        logger.info(f"Clean EXPECTED: {expected_clean}")

        # So sánh theo dạng chuỗi sạch
        assert expected_clean in actual_clean, (
            f" Thông báo lỗi không khớp!\n"
            f"EXPECTED: {expected_clean}\n"
            f"ACTUAL: {actual_clean}"
        )

        logger.info(" Thông báo lỗi hiển thị đúng theo kỳ vọng")



@then("hệ thống chuyển hướng đến trang chủ")
def verify_success_redirect(login_page):
    logger = get_logger("login_test")
    with allure.step("Kiểm tra chuyển hướng thành công đến trang chủ"):
        logger.info("Xác minh chuyển hướng sau khi đăng nhập thành công")
        expect(login_page.page.locator("h3.mt-0")).to_be_visible()
        display_name = login_page.get_logged_in_name()
        logger.info(f"Tên người dùng hiển thị: {display_name}")
        assert "Phan Thanh Việt" in display_name
        logger.info(" Đăng nhập thành công và chuyển hướng đúng trang chủ")
