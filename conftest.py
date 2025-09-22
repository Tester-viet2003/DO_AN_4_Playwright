import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

# @pytest.fixture(scope="function")
# def driver():
#     # Setup
#     options = Options()
#     options.add_argument("--start-maximized")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(5)  # chờ ngầm 5s (best practice)

#     yield driver  # trả driver cho test dùng

#     # Teardown
#     driver.quit()
    
@pytest.fixture(scope="session")
def base_url():
    return "https://olm.vn"

@pytest.fixture(scope="function")
def setup(base_url):
    """
    Fixture Playwright: mở Chromium có giao diện full 1920x1080.
    (Để bật quay video: bỏ comment record_video_dir/record_video_size)
    """
    with sync_playwright() as p:
        # Ép kích thước cửa sổ ngay từ lúc launch
        browser = p.chromium.launch(
            headless=False,
            args=["--window-size=1920,1080"]
        )

        # Context với viewport 1920x1080
        context = browser.new_context(
            viewport={"width": 1600, "height": 900}
            # record_video_dir="videos",
            # record_video_size={"width": 1920, "height": 1080}
        )

        page = context.new_page()
        page.goto(base_url, timeout=60000)  # Tăng thời gian chờ lên 60 giây

        # Đăng nhập trước khi chạy test
        login_page = LoginPage(page, base_url)
        login_page.login("12a10_phanthanhviet", "Vietba\"123")

        yield page  # trả page cho test

        # Đóng và giải phóng tài nguyên
        context.close()
        browser.close()