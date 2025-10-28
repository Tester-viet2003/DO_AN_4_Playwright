import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import os
import allure
from datetime import datetime

# ====================================================
# 1️⃣ Cấu hình URL gốc
# ====================================================
@pytest.fixture(scope="session")
def base_url():
    return "https://olm.vn"


# ====================================================
# 2️⃣ Fixture gốc 'page' — cần cho pytest-bdd nhận diện
# ====================================================
@pytest.fixture(scope="function")
def page(base_url):
    """Tạo fixture 'page' gốc để pytest-bdd và playwright dùng."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-size=1920,1080"])
        context = browser.new_context(viewport={"width": 1600, "height": 900})
        page = context.new_page()
        page.goto(base_url, timeout=60000)
        yield page
        context.close()
        browser.close()


# ====================================================
# 3️⃣ Fixture mở trình duyệt (nếu bạn vẫn muốn dùng tên 'setup')
# ====================================================
@pytest.fixture(scope="function")
def setup(page):
    """Alias cho 'page' để các test cũ vẫn hoạt động."""
    yield page


# ====================================================
# 4️⃣ Fixture đăng nhập sẵn
# ====================================================
@pytest.fixture(scope="function")
def login(setup, base_url):
    """Đăng nhập sẵn vào tài khoản OLM."""
    page = setup
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("12a10_phanthanhviet", 'Vietba"123')
    page.wait_for_load_state("networkidle")
    yield page


# ====================================================
# 5️⃣ Screenshot khi test lỗi
# ====================================================
def _take_screenshot(page, name_prefix="error"):
    """Hàm phụ chụp ảnh lỗi và lưu vào thư mục reports/screenshots"""
    if not page:
        return
    screenshot_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(screenshot_dir, f"{name_prefix}_{timestamp}.png")
    try:
        page.screenshot(path=file_path, full_page=True)
        allure.attach.file(
            file_path,
            name=f"Screenshot - {name_prefix}",
            attachment_type=allure.attachment_type.PNG
        )
        print(f"📸 Đã chụp ảnh lỗi: {file_path}")
    except Exception as e:
        print(f"⚠️ Không thể chụp ảnh: {e}")


# ====================================================
# 6️⃣ Hook tự động chụp ảnh nếu test fail
# ====================================================
def pytest_runtest_makereport(item, call):
    """Hook tự động chạy khi test bị lỗi"""
    if call.when == "call" and call.excinfo is not None:
        page = None
        # Tự động tìm biến page trong fixture
        for arg in item.funcargs.values():
            if hasattr(arg, "screenshot"):  # Nếu là Playwright Page object
                page = arg
                break
            # Nếu là đối tượng chứa page (như login_page, qna_page,...)
            if hasattr(arg, "page"):
                page = getattr(arg, "page")
                break
        if page:
            _take_screenshot(page, item.name)
