from playwright.sync_api import Page

def click_main_button(page: Page, button_texts=None, timeout: int = 10000):
    """
    Click linh hoạt các nút chính trong modal, ví dụ: Tiếp tục, Hoàn thành, Xác nhận,...
    - Nếu button_texts = None -> tự dò các text phổ biến.
    - Có thể truyền danh sách ['Tiếp tục', 'Hoàn thành'] để ưu tiên.
    """
    # Nếu không truyền, dùng danh sách mặc định
    if button_texts is None:
        button_texts = ["Tiếp tục", "Hoàn thành", "Xác nhận", "Bắt đầu", "Gửi"]

    button_locator = None

    for text in button_texts:
        locator = page.locator(f"button:has-text('{text}')").first
        if locator.count():
            # Chờ hiển thị và bật
            page.wait_for_selector(f"button:has-text('{text}')", state="visible", timeout=timeout)
            locator.scroll_into_view_if_needed()
            button_locator = locator
            found_text = text
            break

    if not button_locator:
        raise ValueError(f"❌ Không tìm thấy nút nào trong: {button_texts}")

    # Click cưỡng chế (phòng overlay che hoặc animation)
    button_locator.click(force=True)
    print(f"➡️ Đã click nút '{found_text}' thành công.")
