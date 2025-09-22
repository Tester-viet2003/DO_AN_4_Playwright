import pytest
from pages.login_page import LoginPage
from conftest import setup, base_url
from playwright.sync_api import expect

def test_login_success_username(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("12a10_phanthanhviet", 'Vietba"123')
    assert "Phan Thanh Việt" in login_page.get_logged_in_name(), "Login failed!"
#Không có email
# def test_login_success_email(setup, base_url):
#     page = setup
#     login_page = LoginPage(page, base_url)
#     login_page.login("test_email@domain.com", 'Vietba"123')
#     assert "Phan Thanh Việt" in login_page.get_logged_in_name(), "Login failed!"

def test_login_empty_fields(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("", "")
    assert login_page.error_banner_empty.is_visible(), "Thông báo lỗi không hiển thị!"
    assert login_page.get_error_message("empty") == "Vui lòng nhập đầy đủ: Tên đăng nhập/Email và Mật khẩu", "Nội dung thông báo không đúng!"
    
def test_login_invalid_username(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("user!@#", "password123")
    assert login_page.error_banner_invalid.is_visible(), "Thông báo lỗi không hiển thị!"
    assert login_page.get_error_message("invalid") == "Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu.", "Nội dung thông báo không đúng!"

def test_login_invalid_password(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("12a10_phanthanhviet", "wrong_password")
    assert login_page.error_banner_invalid.is_visible(), "Thông báo lỗi không hiển thị!"
    assert login_page.get_error_message("invalid") == "Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu.", "Nội dung thông báo không đúng!"

def test_login_short_username(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("abc", "password123")
    assert login_page.error_banner_invalid.is_visible(), "Thông báo lỗi không hiển thị!"
    assert login_page.get_error_message("invalid") == "Vui lòng nhập đúng định dạng Tên đăng nhập/Email (tên đăng nhập phải tối thiểu 4 ký tự)", "Nội dung thông báo không đúng!"

def test_login_long_username(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    long_username = "a" * 156  # Tạo chuỗi dài hơn 155 ký tự
    login_page.login(long_username, "password123")
    assert login_page.error_banner_invalid.is_visible(), "Thông báo lỗi không hiển thị!"
    assert login_page.get_error_message("invalid") == "Vượt quá 155 ký tự", "Nội dung thông báo không đúng!"

def test_login_username_with_spaces(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("   ", 'Vietba"123')
    print(page.content())
    assert login_page.get_error_message("error_banner_short") == "Vui lòng nhập đầy đủ: Tên đăng nhập/Email và Mật khẩu", "Thông báo lỗi không hiển thị đúng!"
    msg = page.inner_text("div[role='alert']")
    print(repr(msg))
    



def test_login_username_with_special_chars(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("user!@#", 'Vietba"123')
    assert login_page.get_error_message("error_banner_short") == "Vui lòng nhập đúng định dạng Tên đăng nhập/Email và Mật khẩu", "Thông báo lỗi không hiển thị đúng!"

def test_login_username_as_phone_number(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("0987654321", 'Vietba"123')
    assert login_page.get_error_message("error_banner_short") == "Tên đăng nhập hoặc mật khẩu của bạn không chính xác. Hãy thử lại hoặc sử dụng chức năng quên mật khẩu để lấy lại mật khẩu.", "Thông báo lỗi không hiển thị đúng!"

def test_login_invalid_email_format(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("user.domain.com", 'Vietba"123')
    assert login_page.get_error_message("error_banner_short"), "Thông báo lỗi không hiển thị đúng!"

def test_login_empty_password(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("12a10_phanthanhviet", "")
    assert login_page.get_error_message("error_banner_empty") == "Vui lòng nhập đầy đủ: Tên đăng nhập/Email và Mật khẩu", "Thông báo lỗi không hiển thị đúng!"

def test_login_password_too_short(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("12a10_phanthanhviet", "abc1")
    assert login_page.get_error_message("error_banner_short") == "Mật khẩu tối thiểu 4 ký tự", "Thông báo lỗi không hiển thị đúng!"
#Không tìm thấy icon mắt
def test_toggle_password_visibility(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.goto_login.click()
    login_page.password_input.fill("password123")
    login_page.toggle_password_visibility()
    assert login_page.password_input.get_attribute("type") == "text", "Password visibility toggle failed!"
    login_page.toggle_password_visibility()
    assert login_page.password_input.get_attribute("type") == "password", "Password visibility toggle failed!"

def test_remember_me_functionality(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.goto_login.click()
    login_page.remember_me_checkbox.check()
    assert login_page.remember_me_checkbox.is_checked(), "Remember me functionality failed!"

def test_forgot_password_link(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.goto_login.click()
    login_page.forgot_password_link.click()
    assert "quen-mat-khau" in page.url, "Forgot password link failed!"
#pas
def test_register_link(setup, base_url):
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.goto_login.click()
    login_page.register_link.click()
    assert "dang-ky" in page.url, "Register link failed!"

# def test_google_login_success(setup, base_url):
#     page = setup
#     login_page = LoginPage(page, base_url)
#     login_page.open()
#     login_page.goto_login.click()
#     login_page.login_with_google()
#     # Assuming a mock or a valid Google account is used for testing
#     assert "Phan Thanh Việt" in login_page.get_logged_in_name(), "Google login failed!"