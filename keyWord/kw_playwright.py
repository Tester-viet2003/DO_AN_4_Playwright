# keywords/kw_playwright.py
import time
import importlib
from typing import Optional, Any, cast
from playwright.sync_api import Page, expect

# ============================================================
# 🔹 Biến toàn cục lưu trang hiện tại
# ============================================================

PAGE: Optional[Page] = None


# ============================================================
# 🔹 1. HÀM TIỆN ÍCH
# ============================================================

def _check_page_initialized() -> None:
    """Đảm bảo Playwright Page đã được khởi tạo."""
    global PAGE
    if PAGE is None:
        raise Exception("❌ PAGE chưa được khởi tạo. Hãy gọi 'openBrowser' trước khi thực thi keyword.")


def _resolve_locator(page_object_str: str) -> str:
    """
    Nhận chuỗi 'LoginPage.username_input' → trả về locator tương ứng.
    """
    try:
        page_name, locator_name = page_object_str.split(".")
        module = importlib.import_module(f"pages.{page_name}")
        po_class = getattr(module, page_name)
        locator = getattr(po_class, locator_name)
        return locator
    except Exception as e:
        raise ValueError(f"❌ Không thể lấy locator từ '{page_object_str}'. Lỗi: {e}")


# ============================================================
# 🔹 2. HÀM KEYWORDS CHÍNH
# ============================================================

def openBrowser(page: Page) -> None:
    """Gán đối tượng Page (được fixture khởi tạo)."""
    global PAGE
    PAGE = page
    print("✅ Đã khởi tạo Playwright Page.")


def navigate(url: str, *args: Any) -> None:
    """Điều hướng đến URL."""
    _check_page_initialized()
    page = cast(Page, PAGE)  # ✅ ép kiểu để Pylance biết chắc không None
    page.goto(url, timeout=60000)
    print(f"🌐 Điều hướng đến: {url}")


def setText(po_element: str, value: str, *args: Any) -> None:
    """Nhập văn bản vào input field."""
    _check_page_initialized()
    page = cast(Page, PAGE)
    locator = _resolve_locator(po_element)
    element = page.locator(locator)
    element.fill(value)
    print(f"⌨️ Nhập '{value}' vào {po_element}")


def clickElement(po_element: str, *args: Any) -> None:
    """Click vào một phần tử."""
    _check_page_initialized()
    page = cast(Page, PAGE)
    locator = _resolve_locator(po_element)
    element = page.locator(locator)
    element.click()
    print(f"🖱️ Click vào {po_element}")


def verifyTextContains(po_element: str, expected_text: str, *args: Any) -> None:
    """Xác minh nội dung văn bản của phần tử có chứa chuỗi mong đợi."""
    _check_page_initialized()
    page = cast(Page, PAGE)
    locator = _resolve_locator(po_element)
    element = page.locator(locator)
    actual_text = element.inner_text(timeout=5000)
    assert expected_text in actual_text, f"❌ FAIL: '{expected_text}' không có trong '{actual_text}'"
    print(f"✅ PASS: Text '{expected_text}' có trong '{actual_text}'")


def pauseExecution(seconds: str, *args: Any) -> None:
    """Tạm dừng việc thực thi trong vài giây."""
    try:
        delay = float(seconds)
        if delay > 0:
            print(f"⏸️ Dừng {delay}s...")
            time.sleep(delay)
            print("▶️ Tiếp tục thực thi.")
    except ValueError:
        print(f"⚠️ Giá trị không hợp lệ cho thời gian dừng: '{seconds}'")


def closeBrowser(*args: Any) -> None:
    """Đóng browser hiện tại."""
    global PAGE
    if PAGE:
        page = cast(Page, PAGE)
        page.context.close()
        PAGE = None
        print("🧹 Đã đóng trình duyệt.")
    else:
        print("⚠️ Không có trình duyệt nào đang mở để đóng.")


# ============================================================
# 🔹 3. ÁNH XẠ KEYWORD → HÀM
# ============================================================

KEYWORD_MAP = {
    "openBrowser": openBrowser,
    "navigate": navigate,
    "setText": setText,
    "clickElement": clickElement,
    "verifyTextContains": verifyTextContains,
    "pauseExecution": pauseExecution,
    "closeBrowser": closeBrowser,
}
