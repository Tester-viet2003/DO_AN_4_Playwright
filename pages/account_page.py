from pages.base_page import BasePage
from playwright.sync_api import Page
from playwright.sync_api import expect
from common.common_actions import click_main_button

class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    # Locators
    @property
    def avatar_dropdown(self):
        return self.page.locator("span").filter(has_text="Phan Thanh Việt")
    @property
    def info_menu(self):
        return self.page.get_by_role("link", name=" Thông tin")
    @property
    def setting_menu(self):
        return self.page.get_by_role("link", name=" Cài đặt tài khoản")
    # @property
    # def username_input(self):
    #     return self.page.get_by_role("textbox", name="Tên đăng nhập hoặc email")
    @property
    def cb_class1(self):
        return self.page.get_by_text("Lớp 1", exact=True)

    @property
    def cb_class9(self):
        return self.page.get_by_text("Lớp 9")

    @property
    def cb_class12(self):
        return self.page.get_by_text("Lớp 12", exact=True)
    #khi sửa 1 cái nào đó sẽ hiện ra cái này
    @property
    def lb_tc(self):
        return self.page.get_by_text("Cập nhật thành công").nth(0)

    @property
    def user_menu(self):
        return self.page.locator("span", has_text="Phan Thanh Việt")

    @property
    def info_link(self):
        return self.page.get_by_role("link", name=" Thông tin")


    @property
    def search_button(self):
        return self.page.get_by_role("button", name=" Tìm")

    @property
    def grade_checkboxes(self):
        return self.page.locator("#setting-account div", has_text="Lớp")
    #Chọn tỉnh phù hợp
    def chon_tinh(self, ten_tinh: str):
        self.page.locator("span[id^='select2-province']").click()
        self.page.wait_for_selector(".select2-container--open", state="visible")
        self.page.locator(".select2-container--open input.select2-search__field").fill(ten_tinh)
        self.page.wait_for_selector(".select2-results__option", state="visible")
        self.page.locator(f"li.select2-results__option:has-text('{ten_tinh}')").click()

    #chọn xã phù hợp
    def chon_xa_phuong(self, ten_xa: str):
        self.page.wait_for_selector("span[id^='select2-commune']", state="visible")
        self.page.locator("span[id^='select2-commune']").click()
        self.page.wait_for_selector(".select2-container--open", state="visible")
        self.page.locator(".select2-container--open input.select2-search__field").fill(ten_xa)
        self.page.wait_for_selector(".select2-results__option", state="visible")
        option = self.page.locator(f"li.select2-results__option:has-text('{ten_xa}')").first
        option.scroll_into_view_if_needed()
        option.click()

    #chọn trường phù hợp
    def chon_truong(self, ten_truong: str):
        self.page.locator("select[name='school']").select_option(label=ten_truong)
    # gọi với  trường hợp tích checkbox
    def check_cb(self, checkbox_locator):
        """
        Nếu checkbox chưa được tick thì tick.
        Không làm gì thêm.
        """
        if not checkbox_locator.is_checked():
            checkbox_locator.click()
            print(" Checkbox chưa được chọn, đã chọn.")
        else:
            print(" Checkbox đã được chọn, không cần làm gì.")

    #kiểm tra khi có thay dổi
    def verify_success_all(self):
        self.lb_tc.wait_for(state="visible")
        assert self.lb_tc.is_visible(), "Thông báo không hiển thị."
    #Thêm môn học
    def them_mon_hoc_if_available(self, ten_mon: str):
        print(f"[DEBUG] Đang thêm môn học: {ten_mon}")

        # B1. Mở dropdown đúng selector (Select2 container)
        dropdown_trigger = self.page.locator("ul.select2-selection__rendered")
        expect(dropdown_trigger).to_be_visible(timeout=20000)
        dropdown_trigger.scroll_into_view_if_needed()
        dropdown_trigger.click(force=True)
        print("[DEBUG] Đã click mở dropdown chọn môn học.")
        self.page.wait_for_selector(".select2-container--open", state="visible", timeout=20000)
        search_box = self.page.locator(".select2-container--open input.select2-search__field")
        expect(search_box).to_be_visible(timeout=10000)
        search_box.fill(ten_mon)
        print(f"[DEBUG] Đang nhập '{ten_mon}'...")
        self.page.wait_for_selector(".select2-results__option", state="visible", timeout=10000)
        ket_qua = self.page.locator(f"li.select2-results__option:has-text('{ten_mon}')")
        if ket_qua.count() > 0:
            ket_qua.first.scroll_into_view_if_needed()
            ket_qua.first.click()
            print(f" Đã thêm môn '{ten_mon}'.")
        else:
            print(f" Không tìm thấy môn '{ten_mon}' trong danh sách.")

        # B6. Chờ giao diện cập nhật
        self.page.wait_for_timeout(1500)


    #Xóa môn học
    def xoa_mon_hoc(self, ten_mon: str):
        """
        Xóa môn học khỏi dropdown nếu đang được chọn.
        - Kiểm tra xem môn có tồn tại trong danh sách đã chọn
        - Nếu có thì click nút xóa
        - Nếu không thì bỏ qua
        """
        mon_locator = self.page.locator(f"li.select2-selection__choice[title='{ten_mon}']")
        if mon_locator.count() > 0:
            mon_locator.locator("span.select2-selection__choice__remove").click()
            print(f" Đã xóa môn '{ten_mon}' khỏi danh sách.")
        else:
            print(f" Môn '{ten_mon}' chưa được chọn, không cần xóa.")
        # Methods
    def open_info_menu(self):
        self.avatar_dropdown.hover()
        self.info_menu.click()
        self.setting_menu.click()
        
    def chon_theo_ten_sach(self, ten_muc: str):
        print(f"[DEBUG] Đang tìm và chọn mục: {ten_muc}")
        muc = self.page.locator("label, span, div", has_text=ten_muc)
        muc.first.scroll_into_view_if_needed()
        expect(muc.first).to_be_visible(timeout=10000)
        muc.first.click(force=True)
        print(f" Đã chọn mục: {ten_muc}")
        
    def tim_kiem_truong(self, ten_truong: str):
        print(f"[DEBUG] Đang tìm kiếm trường: {ten_truong}")
        self.page.get_by_role("textbox", name="Nhập vào tên trường").click()
        self.page.get_by_role("textbox", name="Nhập vào tên trường").fill(ten_truong)
        self.page.get_by_role("button", name=" Tìm").click()
        self.page.wait_for_timeout(1500)
        print(" Đã tìm kiếm trường học xong.")


        
    