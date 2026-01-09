import re
import pytest
import allure
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from pages.qNa_page import QnAPage
from utils.logger_utils import get_logger


logger = get_logger("qna_test")


scenarios("../features/q&a.feature")

@pytest.fixture
def qna_page(login):
    """Mở trang Hỏi bài sau khi đã login."""
    qna = QnAPage(login)
    qna.open_qna_page()
    return qna


@given("học viên đã đăng nhập")
def user_logged_in(qna_page):
    with allure.step("Học viên đã đăng nhập"):
        logger.info(" Học viên đã đăng nhập thành công và sẵn sàng thao tác.")

@given("học viên đang ở giao diện hỏi bài")
def at_qna_page(qna_page):
    with allure.step("Học viên đang ở giao diện hỏi bài"):
        expect(qna_page.page).to_have_url(re.compile(r"hoi-dap"))
        expect(qna_page.all).to_be_visible()
        logger.info(" Đang ở trang Hỏi bài.")

# ======================================================
#                SCENARIO 1: TRUY CẬP HỎI BÀI
# ======================================================
@when('học viên chọn mục "Hỏi bài" từ menu')
def open_qna_from_menu(qna_page):
    with allure.step("Học viên chọn mục 'Hỏi bài' từ menu"):
        qna_page.open_qna_page()
        logger.info(" Đã mở trang Hỏi bài từ menu.")

@then("hệ thống hiển thị danh sách câu hỏi của người dùng khác theo thứ tự mới nhất")
def verify_qna_page_loaded(qna_page):
    with allure.step("Hệ thống hiển thị danh sách câu hỏi mới nhất"):
        expect(qna_page.verify_card_any).to_be_visible(timeout=10000)
        logger.info(" Danh sách câu hỏi mới nhất hiển thị thành công.")

@then("hiển thị bộ lọc lớp học và môn học ở thanh menu bên trái")
def verify_filters_visible(qna_page):
    with allure.step("Hệ thống hiển thị bộ lọc lớp học và môn học"):
        expect(qna_page.ask_good).to_be_visible(timeout=10000)
        expect(qna_page.btn_ask_vip).to_be_visible(timeout=10000)
        logger.info(" Bộ lọc lớp học & môn học hiển thị đầy đủ.")

# ======================================================
#                SCENARIO 2: XEM MỚI NHẤT
# ======================================================
@when('học viên chọn tiêu chí "Mới nhất"')
def select_latest_filter(qna_page):
    with allure.step("Học viên chọn tiêu chí 'Mới nhất'"):
        qna_page.filter_newest.click()
        logger.info("Đã chọn tiêu chí 'Mới nhất'.")

@then("hệ thống hiển thị danh sách các câu hỏi được đăng gần đây nhất")
def verify_latest_loaded(qna_page):
    with allure.step("Hệ thống hiển thị câu hỏi mới nhất"):
        expect(qna_page.filter_newest).to_be_visible(timeout=10000)
        logger.info(" Câu hỏi mới nhất hiển thị thành công.")

# ======================================================
#                SCENARIO 3: CÂU HỎI HAY
# ======================================================
@when('học viên chọn tiêu chí "Câu hỏi hay"')
def select_good_question(qna_page):
    with allure.step("Học viên chọn tiêu chí 'Câu hỏi hay'"):
        qna_page.ask_good.click()
        logger.info(" Đã chọn tab 'Câu hỏi hay'.")

@then("hệ thống hiển thị danh sách các câu hỏi được đánh giá cao hoặc được nhiều lượt tương tác")
def verify_good_question(qna_page):
    with allure.step("Hệ thống hiển thị danh sách Câu hỏi hay"):
        expect(qna_page.vrf_ask_good).to_be_visible(timeout=10000)
        logger.info(" Danh sách 'Câu hỏi hay' hiển thị thành công.")

# ======================================================
#                SCENARIO 4: CÂU HỎI VIP
# ======================================================
@when('học viên chọn tiêu chí "Câu hỏi VIP"')
def select_vip_question(qna_page):
    with allure.step("Học viên chọn tiêu chí 'Câu hỏi VIP'"):
        qna_page.btn_ask_vip.click()
        logger.info(" Đã chọn tab 'Câu hỏi VIP'.")

@then("hệ thống hiển thị danh sách các câu hỏi của tài khoản VIP được ưu tiên hiển thị")
def verify_vip_question(qna_page):
    with allure.step("Hệ thống hiển thị danh sách Câu hỏi VIP"):
        expect(qna_page.verify_ask_vip).to_be_visible(timeout=15000)
        logger.info(" Danh sách 'Câu hỏi VIP' hiển thị thành công.")

# ======================================================
#                SCENARIO 5: LỌC THEO MÔN HỌC
# ======================================================
@when("học viên chọn một môn học từ danh sách")
def select_subject(qna_page):
    with allure.step("Học viên chọn một môn học từ danh sách"):
        qna_page.select_subject("Vật lý")
        logger.info(" Đã chọn môn học Vật lý.")

@then("hệ thống hiển thị danh sách câu hỏi thuộc môn học đã chọn")
def verify_subject_loaded(qna_page):
    with allure.step("Hệ thống hiển thị câu hỏi thuộc môn học đã chọn"):
        expect(qna_page.verify_subject_physics).to_be_visible(timeout=10000)
        logger.info(" Câu hỏi thuộc môn học đã chọn hiển thị thành công.")

# ======================================================
#                SCENARIO 7–9: XẾP HẠNG
# ======================================================
@when('học viên chọn mục "Xếp hạng theo năm"')
def select_rank_year(qna_page):
    with allure.step("Học viên chọn 'Xếp hạng theo năm'"):
        qna_page.open_rank_year()
        logger.info(" Đã chọn 'Xếp hạng theo năm'.")

@then("hệ thống hiển thị bảng xếp hạng người dùng theo điểm hỏi đáp")
def verify_rank_year(qna_page):
    with allure.step("Hệ thống hiển thị bảng xếp hạng theo năm"):
        expect(qna_page.verify_rank_table).to_be_visible(timeout=10000)
        logger.info(" Bảng xếp hạng năm hiển thị thành công.")

@when('học viên chọn mục "Xếp hạng theo tháng"')
def select_rank_month(qna_page):
    with allure.step("Học viên chọn 'Xếp hạng theo tháng'"):
        qna_page.open_rank_month()
        logger.info(" Đã chọn 'Xếp hạng theo tháng'.")

@then("học viên có thể chọn bộ lọc theo môn học hoặc theo tuần/tháng/năm")
def verify_rank_month(qna_page):
    with allure.step("Hệ thống hiển thị bảng xếp hạng theo tháng"):
        expect(qna_page.verify_rank_table.first).to_be_visible(timeout=10000)
        logger.info(" Bảng xếp hạng tháng hiển thị thành công.")

@when('học viên chọn mục "Xếp hạng theo tuần"')
def select_rank_week(qna_page):
    with allure.step("Học viên chọn 'Xếp hạng theo tuần'"):
        qna_page.open_rank_week()
        logger.info(" Đã chọn 'Xếp hạng theo tuần'.")

@then("học viên có thể chọn bộ lọc theo môn học hoặc theo tuần/tháng/năm")
def verify_rank_week(qna_page):
    with allure.step("Hệ thống hiển thị bảng xếp hạng theo tuần"):
        expect(qna_page.verify_rank_table).to_be_visible(timeout=10000)
        logger.info(" Bảng xếp hạng tuần hiển thị thành công.")
