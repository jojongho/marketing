import pandas as pd
import os

files = [
    r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\부동산 마케팅 키워드.xlsx",
    r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\키워드추출_ cso9858_naver.xlsx",
    r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\아산 배방 우방아이유쉘 키워드.xlsx"
]

for file_path in files:
    print(f"=== File: {os.path.basename(file_path)} ===")
    try:
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            print(f"\n--- Sheet: {sheet_name} ---")
            df = pd.read_excel(file_path, sheet_name=sheet_name, nrows=5)
            print(f"Columns: {list(df.columns)}")
            print(df.to_string())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    print("\n" + "="*50 + "\n")
