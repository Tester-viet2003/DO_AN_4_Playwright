import pytest
from pages.account_page import AccountPage

def test_view_account_info(setup):
    account_page = AccountPage(setup)
    account_page.open_info_page()
    # Verify readonly fields
    readonly_fields = ["Tên hiển thị", "Tên đăng nhập", "Email", "Email phụ huynh", "Số điện thoại"]
    for field in readonly_fields:
        assert account_page.page.locator(f"input[readonly][name='{field}']").is_visible(), f"Field {field} is not readonly or visible"

def test_update_province(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    account_page.select_province("Hưng Yên")
    assert "Cập nhật trường thành công" in account_page.get_toast_message()

def test_update_commune(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    account_page.select_commune("Xã bất kỳ")
    # Verify school list is loaded
    assert account_page.page.locator("select.custom-select.select-address[name='school']").is_visible(), "School list not loaded"

def test_update_school(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    account_page.select_school("Trường Tiểu học Hợp Hưng")
    assert "Cập nhật trường thành công" in account_page.get_toast_message()

def test_search_valid_school(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    search_box = account_page.page.locator("input.form-control[name='search']")
    search_box.fill("Trường Tiểu học Hợp Hưng")
    assert account_page.page.locator("li:has-text('Trường Tiểu học Hợp Hưng')").is_visible(), "Search result not displayed"

def test_toggle_zalo_notifications(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    zalo_checkbox = account_page.page.locator("input#subscribe-zalo[name='subscribe_zalo']")
    initial_state = zalo_checkbox.is_checked()
    zalo_checkbox.click()
    assert zalo_checkbox.is_checked() != initial_state, "Zalo notification toggle failed"

def test_toggle_email_notifications(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    email_checkbox = account_page.page.locator("input#subscribe-email[name='subscribe']")
    initial_state = email_checkbox.is_checked()
    email_checkbox.click()
    assert email_checkbox.is_checked() != initial_state, "Email notification toggle failed"

def test_select_multiple_grades(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    grades = ["input#select-grade-1", "input#select-grade-2"]
    for grade in grades:
        checkbox = account_page.page.locator(grade)
        checkbox.click()
        assert checkbox.is_checked(), f"Grade {grade} not selected"

def test_select_multiple_subjects(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    subjects_dropdown = account_page.page.locator("span.select2-selection.select2-selection--multiple")
    subjects_dropdown.click()
    account_page.page.locator("li:has-text('Toán')").click()
    account_page.page.locator("li:has-text('Văn')").click()
    assert account_page.page.locator("span.select2-selection__choice:has-text('Toán')").is_visible(), "Subject 'Toán' not selected"
    assert account_page.page.locator("span.select2-selection__choice:has-text('Văn')").is_visible(), "Subject 'Văn' not selected"

def test_remove_selected_subject(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    account_page.page.locator("span.select2-selection__choice:has-text('Toán') span.select2-selection__choice__remove").click()
    assert not account_page.page.locator("span.select2-selection__choice:has-text('Toán')").is_visible(), "Subject 'Toán' not removed"

def test_select_multiple_books(setup):
    account_page = AccountPage(setup)
    account_page.open_setting_page()
    books = ["input#book-student-0", "input#book-student-1"]
    for book in books:
        checkbox = account_page.page.locator(book)
        checkbox.click()
        assert checkbox.is_checked(), f"Book {book} not selected"