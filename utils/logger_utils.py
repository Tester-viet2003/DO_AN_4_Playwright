import logging
import os
from datetime import datetime

def get_logger(test_name: str):
    """
    Tạo logger riêng cho từng test case.
    Ghi log ra cả console và file trong thư mục reports/logs/
    """

    # Tạo thư mục log nếu chưa có
    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)

    # Tên file log dạng YYYYMMDD_HHMM_testname.log
    log_filename = f"{datetime.now().strftime('%Y%m%d_%H%M')}_{test_name}.log"
    log_path = os.path.join(log_dir, log_filename)

    # Cấu hình logger
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    # Nếu logger đã tồn tại (tránh nhân đôi handler)
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%H:%M:%S"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
