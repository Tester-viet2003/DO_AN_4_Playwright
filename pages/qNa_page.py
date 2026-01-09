from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import re
import time


class QnAPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # ======================================================
        #                     LOCATORS CHÍNH
        # ======================================================
        self.lb_ask = self.page.get_by_role("link", name="Hỏi bài")
        self.all = self.page.get_by_role("link", name="Tất cả", exact=True)
        self.sl_grade = self.page.locator(
            "select[name*='grade'], button.dropdown-toggle:has-text('Xếp hạng'), div.ranking-filter-subject button.dropdown-toggle"
        )
        self.sl_subject = self.filter_newest = self.page.get_by_role("link", name="Mới nhất")
        self.filter_newest = self.page.locator("a.nav-link.olm-text-link", has_text="Mới nhất").first

        # Thông báo lỗi
        self.verify_msg = self.page.locator("div.alert.alert-danger li")

        # ======================================================
        #                BỘ LỌC & XẾP HẠNG (CHUẨN HÓA)
        # ======================================================
        # Nút xếp hạng theo tuần / tháng / năm
        self.btn_rank_week = self.page.locator("li.user-board-order-trigger[data-order='sweek']")
        self.btn_rank_month = self.page.locator("li.user-board-order-trigger[data-order='smonth']")
        self.btn_rank_year = self.page.locator("li.user-board-order-trigger[data-order='sum_all']")
        self.verify_rank_table = self.page.locator("ul.list-user-board li.list-group-item")


        # ======================================================
        #                     CÁC TAB HỎI BÀI
        # ======================================================
        self.ask_good = self.page.get_by_role("link", name="Câu hỏi hay")
        self.vrf_ask_good = self.page.locator("#card-post-9465090441732 div").filter(has_text="Câu hỏi hay").nth(3)

        # Câu hỏi VIP
        self.btn_ask_vip = self.page.get_by_role("link", name="Câu hỏi vip")
        self.verify_ask_vip = self.page.get_by_text("VIP", exact=False)

        # Xác minh thẻ câu hỏi bất kỳ (dùng thay cho Mua VIP)
        self.verify_card_any = self.page.locator("div.card-post").first

        # Câu hỏi của tôi / cập nhật / xóa
        self.btn_my_question = self.page.get_by_role("link", name="Câu hỏi của tôi")
        self.btn_three_dots = self.page.locator("#card-post-9466159622651 i").nth(4)
        self.option_edit_ask = self.page.get_by_role("link", name="Cập nhật")
        self.input_edit_ask = self.page.get_by_role("paragraph")
        self.btn_update_ask = self.page.get_by_role("button", name="Cập nhật")
        self.confirm_update_ask = self.page.get_by_text("Cập nhật câu hỏi thành công")
        self.option_delete_ask = self.page.get_by_role("link", name="Xóa")
        self.confirm_delete_ask = self.page.get_by_text("Đã xóa câu hỏi thành công")

        # Locator xác minh theo môn
        self.verify_subject_physics = self.page.get_by_role("link", name=re.compile("Vật lý", re.IGNORECASE)).first

        # Xếp hạng cụ thể
        self.verify_rank_year_user = self.page.get_by_role("link", name="Nguyễn Thị Thương Hoài")
        self.verify_rank_week_user = self.page.get_by_role("link", name="ミ★ＣＵＳＨＩＮＶＮ★彡")
        self.verify_rank_month_user = self.page.get_by_role("link", name="Sinh Viên NEU")

    # ======================================================
    #                    FIXED METHODS
    # ======================================================

    def open_qna_page(self):
        """Mở trang hỏi bài an toàn — auto scroll, fallback URL."""
        try:
            expect(self.lb_ask).to_be_visible(timeout=10000)
            self.lb_ask.scroll_into_view_if_needed()
            self.lb_ask.click(timeout=5000)
            print(" Click menu Hỏi bài thành công.")
        except Exception as e:
            print(f" Không thể click trực tiếp 'Hỏi bài': {e}")
            self.page.goto("https://olm.vn/hoi-dap", timeout=60000)
            print(" Fallback sang URL trực tiếp /hoi-dap")

        try:
            expect(self.all).to_be_visible(timeout=30000)
            print(" Trang Hỏi bài load thành công.")
        except Exception:
            print("Trang Hỏi bài load chậm — thử lại 1 lần cuối.")
            self.page.goto("https://olm.vn/hoi-dap", timeout=60000)
            expect(self.all).to_be_visible(timeout=30000)
            print("Đã vào trang Hỏi bài thành công sau khi reload.")

    def select_grade(self, grade_value_or_text: str):
        """Chọn khối lớp linh hoạt, tự scroll."""
        self.sl_grade.scroll_into_view_if_needed()
        if grade_value_or_text.isdigit():
            self.sl_grade.select_option(grade_value_or_text)
        else:
            self.sl_grade.select_option(label=grade_value_or_text)
        print(f" Đã chọn khối lớp: {grade_value_or_text}")

        skip_values = ["0", "13", "Mẫu giáo", "ĐH-CĐ"]
        if grade_value_or_text in skip_values:
            print(" Khối đặc biệt (Mẫu giáo/ĐH-CĐ) — không chọn môn.")
            return
        time.sleep(1.5)

    def select_subject(self, subject_name):
        """Chọn môn học trong dropdown Bootstrap (OLM style)."""
        try:
            dropdown_button = self.page.locator("button.dropdown-toggle", has_text="Chọn môn học")
            expect(dropdown_button).to_be_visible(timeout=10000)
            dropdown_button.click()
            print(" Đã mở menu chọn môn học.")

            option = self.page.locator(".dropdown-item", has_text=subject_name).first
            expect(option).to_be_visible(timeout=10000)
            option.click()
            print(f" Đã chọn môn học: {subject_name}")

        except Exception as e:
            print(f" Lỗi khi chọn môn '{subject_name}': {e}")
            raise

    def get_text_verify_msg(self) -> str:
        """Lấy nội dung cảnh báo lỗi (nếu có)."""
        expect(self.verify_msg.first).to_be_visible(timeout=10000)
        text = self.verify_msg.first.inner_text().strip()
        print(f"Thông báo lỗi: {text}")
        return text

    def update_ask(self, new_content: str):
        """Cập nhật nội dung câu hỏi đã đăng."""
        self.btn_three_dots.click()
        print(" Đã click nút 3 chấm mở tùy chọn.")
        self.option_edit_ask.click()
        print(" Đã chọn tùy chọn Cập nhật.")
        self.input_edit_ask.fill(new_content)
        print(f" Đã nhập nội dung mới cho câu hỏi: {new_content}")
        self.btn_update_ask.click()
        print(" Đã click nút Cập nhật câu hỏi.")

    # ======================================================
    #                  PHƯƠNG THỨC XẾP HẠNG
    # ======================================================

    def open_rank_week(self):
        expect(self.btn_rank_week).to_be_visible(timeout=10000)
        self.btn_rank_week.scroll_into_view_if_needed()
        print(" Đã click chọn tab 'Xếp hạng theo Tuần'.")
        self.page.wait_for_load_state("networkidle")
        expect(self.verify_rank_week_user).to_be_visible(timeout=15000)
        print("Danh sách xếp hạng theo Tuần hiển thị thành công.")

    def open_rank_month(self):
        expect(self.btn_rank_month).to_be_visible(timeout=10000)
        self.btn_rank_month.scroll_into_view_if_needed()
        self.btn_rank_month.click()
        print(" Đã click chọn tab 'Xếp hạng theo Tháng'.")
        self.page.wait_for_load_state("networkidle")
        expect(self.verify_rank_table.first).to_be_visible(timeout=15000)
        print("Danh sách xếp hạng theo Tháng hiển thị thành công.")

    def open_rank_year(self):
        expect(self.btn_rank_year).to_be_visible(timeout=10000)
        self.btn_rank_year.scroll_into_view_if_needed()
        self.btn_rank_year.click()
        print(" Đã click chọn tab 'Xếp hạng theo Năm'.")
        self.page.wait_for_load_state("networkidle")
        expect(self.verify_rank_table.first).to_be_visible(timeout=15000)
        print(" Danh sách xếp hạng theo Năm hiển thị thành công.")
