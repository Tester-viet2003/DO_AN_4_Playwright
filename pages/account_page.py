from pages.base_page import BasePage
from playwright.sync_api import Page

class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # Locators
    @property
    def avatar_dropdown(self):
        return self.page.locator("span.ml-1.font-weight-bold.text-white.opacity-header.text-truncate.align-text-top.d-none.d-xl-inline-block.mw-100")

    @property
    def info_menu(self):
        return self.page.get_by_role("link", name="Thông tin")


    @property
    def setting_menu(self):
        return self.page.get_by_role("link", name="Cài đặt tài khoản")

    @property
    def province_dropdown(self):
        return self.page.locator("span.select2-selection.select2-selection--single[aria-labelledby='select2-province-rx-container']")

    @property
    def commune_dropdown(self):
        return self.page.locator("span.select2-selection.select2-selection--single[aria-labelledby='select2-commune-ll-container']")

    @property
    def school_dropdown(self):
        return self.page.locator("select.custom-select.select-address[name='school']")

    @property
    def toast_message(self):
        return self.page.locator("div.toast-body.toast-message")

    @property
    def username_input(self):
        return self.page.get_by_role("textbox", name="Tên đăng nhập hoặc email")

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Mật khẩu")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Đăng nhập")

    @property
    def user_menu(self):
        return self.page.locator("span", has_text="Phan Thanh Việt")

    @property
    def info_link(self):
        return self.page.get_by_role("link", name=" Thông tin")

    @property
    def search_school_input(self):
        return self.page.get_by_role("textbox", name="Nhập vào tên trường")

    @property
    def search_button(self):
        return self.page.get_by_role("button", name=" Tìm")

    @property
    def grade_checkboxes(self):
        return self.page.locator("#setting-account div", has_text="Lớp")

    @property
    def success_toast(self):
        return self.page.get_by_text("Cập nhật thành công")

    @property
    def subject_list(self):
        return self.page.get_by_text("×Toán×Tiếng Nga×BD Tiếng Anh×")

    # Methods
    def open_info_page(self):
        self.avatar_dropdown.wait_for(state="visible")
        self.avatar_dropdown.hover()
        self.info_menu.click()

    def open_setting_page(self):
        self.avatar_dropdown.hover()
        self.setting_menu.click()

    def select_province(self, province_name: str):
        self.province_dropdown.click()
        self.page.locator(f"li:has-text('{province_name}')").click()

    def select_commune(self, commune_name: str):
        self.commune_dropdown.click()
        self.page.locator(f"li:has-text('{commune_name}')").click()

    def select_school(self, school_name: str):
        self.school_dropdown.select_option(school_name)

    def get_toast_message(self):
        return self.toast_message.inner_text()

    def login_and_open_info_page(self, username: str, password: str):
        self.page.goto("https://olm.vn/dangnhap?redirect=https%3A%2F%2Folm.vn%2Fthong-tin-tai-khoan%2Finfo")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.user_menu.click()
        self.info_link.click()

    def search_school(self, school_name: str):
        self.search_school_input.fill(school_name)
        self.search_button.click()

    def select_grades(self, grades: list):
        for grade in grades:
            self.page.get_by_text(grade).click()

    def update_subjects(self, subject_name: str):
        self.subject_list.click()
        self.page.get_by_role("option", name=subject_name).click()

    def confirm_success(self):
        self.success_toast.first.click(button="right")