import pandas as pd
import os

files = [
    r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\부동산 마케팅 키워드.xlsx",
    r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\키워드추출_ cso9858_naver.xlsx",
    r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\아산 배방 우방아이유쉘 키워드.xlsx"
]

for file_path in files:
    print(f"--- Analyzing: {os.path.basename(file_path)} ---")
    try:
        if os.path.exists(file_path):
            df = pd.read_excel(file_path, nrows=10)
            print(df.to_string())
            print("\n")
        else:
            print(f"File not found: {file_path}\n")
    except Exception as e:
        print(f"Error reading {file_path}: {e}\n")
