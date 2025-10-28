# drivers/driver_script.py
from pathlib import Path
from keyWord.kw_playwright import KEYWORD_MAP
from utils.data_loader import load_excel_data, load_data

def execute_keyword_test(excel_file_path: str, md_file_path: str | None = None) -> None:
    """
    Đọc file Excel (Keyword-Driven)
    + kết hợp với file .md (Data-Driven) nếu có
    """
    file_path = Path(excel_file_path)
    if not file_path.exists():
        print(f"❌ Không tìm thấy file Excel: {excel_file_path}")
        return

    # 1️⃣ Đọc dữ liệu keyword từ Excel
    df = load_excel_data(excel_file_path)

    # 2️⃣ Nếu có file .md (Data-Driven)
    md_data = []
    if md_file_path:
        md_path = Path(md_file_path)
        if md_path.exists():
            md_data = load_data(md_path.name)
            print(f"📋 Đã load {len(md_data)} dòng test data từ {md_path.name}")
        else:
            print(f"⚠️ Không tìm thấy file MD: {md_file_path}")

    # 3️⃣ Lặp qua từng bộ dữ liệu (nếu có), nếu không thì chạy 1 lần
    data_sets = md_data if md_data else [()]
    for data_set in data_sets:
        print(f"\n🧩 ====== BẮT ĐẦU BỘ TEST DATA: {data_set} ======")
        test_cases = df["TS_ID"].unique()

        for tc_id in test_cases:
            print(f"\n🚀 === BẮT ĐẦU TEST CASE: {tc_id} ===")
            test_steps = df[df["TS_ID"] == tc_id]

            for _, row in test_steps.iterrows():
                keyword = str(row["Action Keyword"]).strip()
                po_locator = str(row["Page Object/Locator"]).strip() if row["Page Object/Locator"] else ""
                test_data = str(row["Test Data"]).strip() if row["Test Data"] else ""
                verify_data = str(row["Verification Data"]).strip() if row["Verification Data"] else ""

                # Nếu file MD có dữ liệu user/pass, thay thế vào
                if "{username}" in test_data and len(data_set) >= 1:
                    test_data = test_data.replace("{username}", data_set[0])
                if "{password}" in test_data and len(data_set) >= 2:
                    test_data = test_data.replace("{password}", data_set[1])

                print(f"➡️  Thực thi: {keyword} ({po_locator or test_data})")

                if keyword in KEYWORD_MAP:
                    try:
                        KEYWORD_MAP[keyword](po_locator or test_data)
                    except Exception as e:
                        print(f"❌ Lỗi tại bước '{keyword}': {e}")
                else:
                    print(f"⚠️ Keyword '{keyword}' chưa có trong KEYWORD_MAP")

        print(f"✅ Hoàn thành Test Data: {data_set}")
