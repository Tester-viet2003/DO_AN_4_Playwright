from playwright.sync_api import Page,expect


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
        return self.page.locator("button").filter(has_text="Đăng nhập")

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

    
    def msg_error(self):
        return self.page.locator("div.alert.alert-danger.mb-2")
    
    
    # Methods
    def open(self):
        print("[DEBUG] Đang truy cập:", self.url)
        self.page.goto(self.url)
        print("[DEBUG] Đã truy cập xong:", self.url)

        

    def login(self, username: str, password: str):  
        expect(self.goto_login).to_be_visible()
        self.goto_login.click()

        expect(self.username_input).to_be_visible()
        self.username_input.fill(username)

        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)

        expect(self.login_button).to_be_visible()
        self.login_button.click(timeout=120000)

        # Chờ trang chuyển hoặc xác nhận đăng nhập thành công
        self.page.wait_for_load_state("networkidle")



    def get_error_message(self, banner_type: str) -> str:
        if banner_type == "empty":
            return self.error_banner_empty.inner_text().strip()
        elif banner_type == "invalid":
            return self.error_banner_invalid.inner_text().strip()
        return ""

    def get_logged_in_name(self) -> str:
        return self.page.inner_text("h3.mt-0").strip()
        
    def get_text_msg_error(self) -> str:
        return self.msg_error().inner_text().strip()
    
    