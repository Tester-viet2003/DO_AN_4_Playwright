from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url

    # Locators
    @property
    def goto_login(self):
        return self.page.locator("text=Đăng nhập")

    @property
    def username_input(self):
        return self.page.locator("input[name='username']")

    @property
    def password_input(self):
        return self.page.locator("input[name='password']")

    @property
    def login_button(self):
        return self.page.locator("button:has-text('Đăng nhập')")

    @property
    def error_banner_empty(self):
        return self.page.locator("div.box-error div[role='alert']")

    @property
    def error_banner_invalid(self):
        return self.page.locator("div.alert.alert-danger.mb-2[role='alert'] b")

    @property
    def forgot_password_link(self):
        return self.page.locator("a[href='https://olm.vn/quen-mat-khau']")

    @property
    def register_link(self):
        return self.page.locator("a[href='https://olm.vn/dang-ky']")

    @property
    def remember_me_checkbox(self):
        return self.page.locator("input#remember-me")

    @property
    def google_login_button(self):
        return self.page.locator("a[href='https://olm.vn/social/google/redirect']")

    # Methods
    def open(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        
        self.goto_login.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self, banner_type: str) -> str:
        if banner_type == "empty":
            return self.error_banner_empty.inner_text().strip()
        elif banner_type == "invalid":
            return self.error_banner_invalid.inner_text().strip()
        return ""

    def get_logged_in_name(self) -> str:
        return self.page.inner_text("h3.mt-0").strip()

    def toggle_password_visibility(self):
        self.page.locator("i.cursor-pointer.far.fa-eye").click()

    def login_with_google(self):
        self.google_login_button.click()