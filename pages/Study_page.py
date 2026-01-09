from playwright.sync_api import Page, expect  # type hint cho Pylance
from common.common_actions import click_main_button
import re
class StuDy:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url
        #Vào học bài khi đăng nhập gọi khi trường hợp đăng nhập không vào luôn trang học bài
        self.study = self.page.get_by_role("link", name="Học bài")
        #từng lớp  
        self.lbclass1 = self.page.get_by_role("link", name="Lớp 1", exact=True)
        self.lbclass9 = self.page.get_by_role("link", name="Lớp 9", exact=True)
        self.lbclass12 = self.page.get_by_role("link", name="Lớp 12", exact=True)
        #Nút Nộp bài chung
        self.submit_btn = self.page.get_by_role("button", name=" Nộp bài!")
        #nút tiếp tục làm bài chung
        self.continue_btn = self.page.get_by_role("button", name="TIếp tục làm bài")
        #xác nhận nộp bài chung
        self.confirm_submit = self.page.get_by_role("button", name="Nộp bài", exact=True)
        #verify khi xác nhập nộp bài
        self.verify_submit = self.page.get_by_role("button", name=" Tiếp tục làm bài")
        self.btn_dkkh = self.page.locator("#list-course-studied div").filter(has_text="Đăng ký khóa học").nth(1)
        #nút tiếp tục đăng ký khóa học
        self.continue_dk = self.page.get_by_role("button", name="Tiếp tục")
        #nút hoàn thành đăng ký khóa học
        self.finish_dk = self.page.get_by_role("button", name="Hoàn thành")
        #Xem học bà khi ấn vào học bài
        self.view_study = self.page.get_by_role("link", name="Học bạ")
        #check khi vào học bạ
        self.check_study = self.page.get_by_role("heading", name="Phan Thanh Việt")

        
        #click luyện tập lại cái này chỉ click thôi không được vì yêu cầu Vip
        self.practice_again = self.page.get_by_role("link", name=" Luyện tập lại")
        #thông báo khi click luyện tập lại không có vip 
        self.msg_practice = self.page.get_by_text("Để làm lại bài, hãy nhờ giáo")
        ###############################Riêng cho toán lớp 1#####################################
        #lớp toán 1
        #chọn khóa học toán
        self.namecourse1 = self.page.get_by_role("link", name="Toán lớp 1 (Hỗ trợ học bộ Kết nối tri thức với cuộc sống)", exact=True).first
        #chọn luyện tập toán 1
        self.practice_class1 = self.page.get_by_title("Nhận biết các số từ 0 đến")     
        ###############################Riêng cho toán lớp 9#####################################
        #lớp toán 9
        self.namecourse9 = self.page.get_by_text("Toán 9 (Hỗ trợ học bộ Kết nối")
        self.practice_class9 = self.page.locator("#accordion-chapter-2322514472").get_by_role("link", name="").first
        ###############################Riêng cho toán lớp 12#####################################
        #lớp toán 12
        self.namecourse12 = self.page.get_by_text("Toán 12 (Hỗ trợ học bộ Kết nối tri thức với cuộc sống)", exact=True).first
        #xem bài giảng
        self.view_lecture = self.page.locator("#accordion-chapter-2323530307").get_by_role("link", name="").first
        #Tiếp tục xem hết vip cũng không xem đc
        self.continue_view = self.page.get_by_role("button", name="Tiếp tục xem")
        
        #nút đăng ký khóa học
        self.bt_dkkh = self.page.locator("#list-course-studied div").filter(has_text="Đăng ký khóa học").first
        #checkbox lớp 1
        self.ckb_class1 = self.page.locator("#setting-step1").get_by_text("Lớp 1", exact=True)
        #click tiếp tục rồi verify
        self.vry_l1 = self.page.get_by_role("heading", name="Lớp 1", exact=True)
        #checkbox lớp 9
        self.ckb_class9 = self.page.locator("#setting-step1").get_by_text("Lớp 9")
        #verify lớp 9
        self.vry_l9 = self.page.get_by_role("heading", name="Lớp 9")
        #checkbox lớp 12
        self.ckb_class12 = self.page.locator("#setting-step1").get_by_text("Lớp 12")
        #verify lớp 12
        self.vry_l12 = self.page.get_by_role("heading", name="Lớp 12")
        #nút tiếp tục
        self.bt_continue = self.page.get_by_role("button", name="Tiếp tục")
        #nút hoàn thành
        self.bt_finish = self.page.get_by_role("button", name="Hoàn thành")
        #verify hoàn thành lớp 1
        self.vry_finish = self.page.get_by_role("link", name="Toán lớp 1 (Hỗ trợ học bộ Kết")
        #verify hoàn thành lớp 9
        self.vry_finish9 = self.page.get_by_role("link", name="Toán 9 (Hỗ trợ học bộ Kết nối")
        #verify hoàn thành lớp 12
        self.vry_finish12 = self.page.get_by_role("heading", name="Toán 12 (Hỗ trợ học bộ Kết nối tri thức với cuộc sống)")
        #Hiển thị bài học tuần này
        self.study_today = self.page.get_by_role("heading", name="Bài học tuần này của OLM")
        #Hiển thị các khóa học đã được đăng ký
        self.course_studying = self.page.get_by_role("heading", name="Khóa học bạn đang học")
        #Hiển thị nút xem tất cả 
        self.btn_view_all = self.page.get_by_role("link", name="Xem tất cả").nth(0)
        #xem nội dung khóa họ thì chọn vào lớp 9
        self.bt_continue_viewcourse = self.page.get_by_role("heading", name="Toán 9 (Hỗ trợ học bộ Kết nối")
        #verify chuyển sang giao diện học
        
    def seLect_class_1(self):
        self.lbclass1.click()
        expect(self.namecourse1).to_be_visible()
        self.namecourse1.click()
        self.practice_class1.click()
        expect(self.submit_btn).to_be_visible(timeout=20000)

    def seLect_class_9(self):
        self.lbclass9.click()
        expect(self.namecourse9).to_be_visible()
        self.namecourse9.click()
        expect(self.practice_class9).to_be_visible()
        self.practice_class9.click()
        expect(self.submit_btn).to_be_visible(timeout=20000)

    def seLect_class_12(self):
        self.lbclass12.click()
        expect(self.namecourse12).to_be_visible()
        self.namecourse12.click()
        self.view_lecture.click()
        self.continue_view.click()
        
    def verify_practice_all(self):
        expect(self.msg_practice).to_be_visible()
    
    
    def dk_khoahoc(self, class_key: str):
        checkbox_attr = f"ckb_{class_key}"
        verify_attr = f"vry_{class_key}"
        checkbox = getattr(self, checkbox_attr)
        verify_heading = getattr(self, verify_attr)

        if not checkbox.is_checked():
            checkbox.click()
        self.bt_continue.click()
        expect(verify_heading).to_be_visible()
    
    def click_btn_dkkh(self):
        self.btn_dkkh.scroll_into_view_if_needed()
        self.bt_dkkh.click()
    

    def chon_checkbox(self, label_text: str):
    # Nếu là "Lớp 9", "Lớp 12"... lấy số để build id input
        num = ''.join(filter(str.isdigit, label_text))
        if num:
            cb   = self.page.locator(f"input#select-grade-{num}")                  
            lbl  = self.page.locator(f"label[for='select-grade-{num}']")           
            if cb.count() and not cb.is_checked():                                  
                lbl.click(force=True)
            return

        # Trường hợp checkbox theo tên môn/loại (không có số)
        lbl = self.page.locator(f"label:has-text('{label_text}')").first
        if lbl.count():
            for_id = lbl.get_attribute("for")
            if for_id:
                cb = self.page.locator(f"#{for_id}")
                if cb.count() and not cb.is_checked():                              
                    lbl.click(force=True)
            else:
                lbl.click(force=True)  



    def click_continue_dk(self):
        if self.continue_dk.count() > 0:
            self.continue_dk.click(force=True)
            print("Click Tiếp tục")

    def click_finish_dk(self):
        if self.finish_dk.count() > 0:
            self.finish_dk.click(force=True)
            print(" Click Hoàn thành")

    def study_hb(self):
        self.study.click()
        expect(self.view_study).to_be_visible()
        self.view_study.click()
        expect(self.check_study).to_be_visible(timeout=10000)
