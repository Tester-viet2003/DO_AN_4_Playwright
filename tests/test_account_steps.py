import re
import pytest
import allure
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.account_page import AccountPage
from utils.logger_utils import get_logger


scenarios("../features/account.feature")


@pytest.fixture
def account_page(login):
    return AccountPage(login)


logger = get_logger("account_test")


@given("người dùng đã đăng nhập")
def user_logged_in(account_page):
    with allure.step("Người dùng đã đăng nhập sẵn vào hệ thống"):
        logger.info("Kiểm tra trạng thái đăng nhập người dùng.")
        expect(account_page.page).to_have_url(re.compile(r".*olm.vn.*"))
        account_page.open_info_menu()
        logger.info(" Người dùng đã đăng nhập và mở menu tài khoản thành công.")


@when('người dùng chọn mục "Cài đặt tài khoản" từ menu')
def open_setting(account_page):
    with allure.step("Người dùng chọn 'Cài đặt tài khoản' từ menu"):
        logger.info("Người dùng chọn menu 'Cài đặt tài khoản'.")
        account_page.open_info_menu()
        logger.info(" Đã mở giao diện Cài đặt tài khoản.")


@then("hệ thống hiển thị giao diện cài đặt tài khoản")
def verify_setting_loaded(account_page):
    with allure.step("Hệ thống hiển thị trang Cài đặt tài khoản"):
        expect(account_page.page).to_have_url("https://olm.vn/thong-tin-tai-khoan/setting")
        logger.info(" Trang cài đặt tài khoản đã hiển thị thành công.")


# ==============================
# --- Chọn tỉnh / thành phố ---
# ==============================
@given("người dùng đang ở giao diện cài đặt tài khoản")
def already_on_setting_page(account_page):
    with allure.step("Đảm bảo người dùng đang ở trang cài đặt tài khoản"):
        logger.info("Xác minh trang hiện tại là Cài đặt tài khoản.")
        account_page.open_info_menu()
        logger.info(" Người dùng đang ở giao diện Cài đặt tài khoản.")


@when("người dùng chọn một tỉnh/thành phố")
def select_province(account_page):
    with allure.step("Người dùng chọn tỉnh/thành phố"):
        logger.info("Người dùng chọn tỉnh 'Tỉnh Quảng Ninh'.")
        account_page.chon_tinh("Tỉnh Quảng Ninh")
        logger.info(" Đã chọn tỉnh thành công.")


@then("hệ thống hiển thị danh sách xã/phường tương ứng")
def verify_commune_displayed(account_page):
    with allure.step("Hệ thống hiển thị danh sách xã/phường"):
        expect(account_page.page.locator("span[id^='select2-commune']")).to_be_visible()
        logger.info(" Danh sách xã/phường đã hiển thị đúng.")


# ==============================
# --- Chọn xã / phường ---
# ==============================
@given("người dùng đã chọn tỉnh/thành phố")
def province_selected(account_page):
    with allure.step("Đảm bảo người dùng đã chọn tỉnh/thành phố"):
        logger.info("Chọn lại tỉnh 'Tỉnh Quảng Ninh' để đảm bảo trạng thái.")
        account_page.open_info_menu()
        account_page.chon_tinh("Tỉnh Quảng Ninh")


@when("người dùng chọn một xã/phường")
def select_commune(account_page):
    with allure.step("Người dùng chọn xã/phường"):
        logger.info("Chọn xã/phường 'Phường Hạ Long'.")
        account_page.chon_xa_phuong("Phường Hạ Long")


@then("hệ thống hiển thị danh sách trường học tương ứng")
def verify_school_displayed(account_page):
    with allure.step("Hệ thống hiển thị danh sách trường học"):
        expect(account_page.page.locator("select[name='school']")).to_be_visible()
        logger.info(" Danh sách trường học đã hiển thị đúng.")


# ==============================
# --- Chọn trường học ---
# ==============================
@given("người dùng đã chọn xã/phường")
def commune_selected(account_page):
    with allure.step("Đảm bảo người dùng đã chọn xã/phường"):
        logger.info("Chọn tỉnh + xã để chuẩn bị chọn trường.")
        account_page.open_info_menu()
        account_page.chon_tinh("Tỉnh Quảng Ninh")
        account_page.chon_xa_phuong("Phường Hạ Long")


@when("người dùng chọn một trường học")
def select_school(account_page):
    with allure.step("Người dùng chọn trường học"):
        logger.info("Chọn trường 'Trường THPT Hạ Long'.")
        account_page.chon_truong("Trường THPT Hạ Long")


@then("hệ thống hiển thị tên trường đã chọn")
def verify_school_selected(account_page):
    with allure.step("Hệ thống hiển thị tên trường đã chọn"):
        account_page.verify_success_all()
        logger.info(" Tên trường được hiển thị chính xác.")


@then(parsers.parse('hiển thị thông báo "{msg}" ở góc trái màn hình'))
def verify_success_toast(account_page, msg):
    with allure.step(f"Kiểm tra thông báo '{msg}' hiển thị"):
        toast = account_page.page.get_by_text(msg).first
        expect(toast).to_be_visible(timeout=5000)
        logger.info(f" Thông báo '{msg}' hiển thị thành công.")


# ==============================
# --- Tìm kiếm trường ---
# ==============================
@when("người dùng nhập tên trường hoặc tên gần đúng vào ô tìm kiếm")
def search_school(account_page):
    with allure.step("Người dùng nhập tên trường vào ô tìm kiếm"):
        logger.info("Tìm kiếm trường có tên gần đúng 'Hạ Long'.")
        account_page.tim_kiem_truong("Hạ Long")


@then("hệ thống hiển thị kết quả tìm kiếm nếu có")
def verify_search_result(account_page):
    with allure.step("Hệ thống hiển thị kết quả tìm kiếm"):
        expect(account_page.page.locator("select[name='school']")).to_be_visible()
        logger.info(" Kết quả tìm kiếm trường được hiển thị thành công.")


@then("nếu không có kết quả thì vẫn giữ thông tin của lần tìm kiếm gần nhất")
def verify_previous_result(account_page):
    with allure.step("Kiểm tra giữ lại thông tin tìm kiếm trước"):
        expect(account_page.page.locator("select[name='school']")).to_be_visible()
        logger.info(" Giữ lại dữ liệu tìm kiếm gần nhất.")


# ==============================
# --- Checkbox nhận thông báo ---
# ==============================
@when("người dùng chọn checkbox nhận thông báo qua Zalo và email")
def select_notifications(account_page):
    with allure.step("Người dùng chọn nhận thông báo qua Zalo và Email"):
        logger.info("Chọn checkbox: Zalo, Email.")
        account_page.chon_theo_ten_sach("Zalo")
        account_page.chon_theo_ten_sach("Email")


@then("hệ thống cập nhật ngay lập tức")
def verify_notify_update(account_page):
    with allure.step("Hệ thống cập nhật ngay lập tức"):
        account_page.verify_success_all()
        logger.info(" Hệ thống cập nhật ngay lập tức sau khi chọn checkbox.")


# ==============================
# --- Khóa chức năng nhắn tin ---
# ==============================
# @when("người dùng chọn checkbox khóa chức năng nhắn tin")
# def disable_chat(account_page):
#     with allure.step("Người dùng chọn checkbox khóa chức năng nhắn tin"):
#         logger.info("Chọn checkbox: Khóa chức năng nhắn tin.")
#         account_page.chon_theo_ten_sach("Khóa chức năng nhắn tin")


@then("hệ thống hiển thị thông báo xác nhận")
def verify_confirm_dialog(account_page):
    with allure.step("Kiểm tra hiển thị hộp thoại xác nhận"):
        dialog = account_page.page.locator("#modal-verify2fa").first
        dialog.wait_for(state="visible", timeout=8000)
        confirm_button = dialog.locator("button:has-text('Xác nhận')").first
        expect(confirm_button).to_be_visible()
        logger.info(" Hộp thoại xác nhận hiển thị thành công.")


# ==============================
# --- Chọn lớp học ---
# ==============================
@when("người dùng chọn một hoặc nhiều lớp học")
def select_classes(account_page):
    with allure.step("Người dùng chọn các lớp học"):
        logger.info("Chọn lớp 1 và lớp 9.")
        account_page.cb_class1.click()
        account_page.cb_class9.click()


@then("hệ thống cập nhật ngay lập tức")
def verify_class_update(account_page):
    with allure.step("Hệ thống cập nhật thông tin lớp học"):
        account_page.verify_success_all()
        logger.info(" Cập nhật lớp học thành công.")


# ==============================
# --- Chọn môn học ---
# ==============================
@when("người dùng chọn một hoặc nhiều môn học")
def select_subjects(account_page):
    with allure.step("Người dùng chọn môn học"):
        logger.info("Chọn môn Toán và Tiếng Anh.")
        account_page.them_mon_hoc_if_available("Toán")
        account_page.them_mon_hoc_if_available("Tiếng Anh")


@then("người dùng có thể xoá môn bằng biểu tượng dấu X")
def delete_subject(account_page):
    with allure.step("Người dùng xoá môn học bằng biểu tượng X"):
        logger.info("Xoá môn Toán.")
        account_page.xoa_mon_hoc("Toán")
        logger.info(" Môn học đã được xoá thành công.")


@then("hệ thống mở rộng ô chứa môn học nếu cần")
def verify_subject_box_opened(account_page):
    with allure.step("Hệ thống mở rộng ô chứa môn học"):
        box = account_page.page.locator("ul.select2-selection__rendered")
        expect(box).to_be_visible()
        logger.info(" Ô chứa môn học đã mở rộng hiển thị đúng.")


# ==============================
# --- Chọn bộ sách ---
# ==============================
@when("người dùng chọn một hoặc nhiều bộ sách")
def select_books(account_page):
    with allure.step("Người dùng chọn bộ sách"):
        logger.info("Chọn bộ sách 'Kết nối tri thức với cuộc sống'.")
        account_page.chon_theo_ten_sach("Kết nối tri thức với cuộc sống")


@then('hiển thị thông báo "Cập nhật trường thành công"')
def verify_update_message(account_page):
    with allure.step("Hệ thống hiển thị thông báo cập nhật thành công"):
        account_page.verify_success_all()
        logger.info(" Thông báo 'Cập nhật trường thành công' hiển thị đúng.")
