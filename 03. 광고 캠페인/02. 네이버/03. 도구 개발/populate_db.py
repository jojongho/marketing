import pandas as pd
import os

# 파일 경로 정의
db_path = "Smart_Keyword_DB.xlsx"
source_files = {
    "marketing": r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\부동산 마케팅 키워드.xlsx",
    "project": r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\아산 배방 우방아이유쉘 키워드.xlsx",
    "extracted": r"c:\Users\jojognho\project\marketing\03. 광고 캠페인\02. 네이버\05. 엑셀\키워드추출_ cso9858_naver.xlsx"
}

# 1. 기존 DB 로드 (없으면 템플릿 생성 스크립트 실행 필요, 여기서는 있다고 가정)
try:
    xls_db = pd.ExcelFile(db_path)
    # 기존 데이터 읽기
    df_basic = pd.read_excel(xls_db, sheet_name='Basic_Info')
    df_re = pd.read_excel(xls_db, sheet_name='Real_Estate')
    df_life = pd.read_excel(xls_db, sheet_name='Life_Interest')
    df_project = pd.read_excel(xls_db, sheet_name='Project_Specific')
    df_rules = pd.read_excel(xls_db, sheet_name='Rules')
except FileNotFoundError:
    print("DB file not found. Please run create_db_template.py first.")
    exit()

# 2. 데이터 추출 및 병합 함수
def extract_column(file_key, sheet_index, col_idx):
    try:
        # sheet_name에 정수(인덱스) 사용
        df = pd.read_excel(source_files[file_key], sheet_name=sheet_index)
        return df.iloc[:, col_idx].dropna().unique().tolist()
    except Exception as e:
        print(f"Error extracting from {file_key}/Sheet{sheet_index}: {e}")
        return []

# --- A. Basic_Info 업데이트 ---
# '아산 배방...' 파일의 Index 7 (랜드마크 키워드 추정) -> 2번째 컬럼(1)
landmarks = extract_column("project", 7, 1)
current_regions = df_basic['Region_L2'].dropna().tolist()
new_regions = list(set(current_regions + landmarks))
df_basic_new = pd.DataFrame({'Region_L2': new_regions})
df_basic = pd.concat([df_basic, df_basic_new], axis=0).drop_duplicates(subset=['Region_L2']).reset_index(drop=True)


# --- B. Real_Estate 업데이트 ---
# '부동산 마케팅...' 파일의 Index 3 (건물형태 추정) -> 1번째 컬럼(0)
types = extract_column("marketing", 3, 0)
current_types = df_re['Type'].dropna().tolist()
new_types = list(set(current_types + types))
df_re_new = pd.DataFrame({'Type': new_types})
df_re = pd.concat([df_re, df_re_new], axis=0).drop_duplicates(subset=['Type']).reset_index(drop=True)

# '아산 배방...' 파일의 Index 6 (타겟 별 키워드 추정) -> 2번째 컬럼(1)
targets = extract_column("project", 6, 1)
current_targets = df_re['Target'].dropna().tolist()
new_targets = list(set(current_targets + targets))
df_re['Target'] = pd.Series(new_targets)


# --- C. Life_Interest 업데이트 ---
# '아산 배방...' 파일의 Index 2 (아산 테스트 500 추정) -> '키워드' 컬럼 (보통 2번째, 인덱스 1)
life_keywords = extract_column("project", 2, 1)
parsed_life = []
for kw in life_keywords:
    parts = str(kw).split()
    if len(parts) >= 2:
        parsed_life.append({"Location_Detail": parts[0], "Brand_Name": " ".join(parts[1:]), "Category": "기타"})
    else:
        parsed_life.append({"Location_Detail": "아산", "Brand_Name": kw, "Category": "기타"})

df_life_new = pd.DataFrame(parsed_life)
df_life = pd.concat([df_life, df_life_new], axis=0).drop_duplicates(subset=['Brand_Name']).reset_index(drop=True)


# --- D. Project_Specific 업데이트 ---
# '아산 배방...' 파일의 Index 1 (메인 추정) -> 1번째 컬럼(0)
main_kws = extract_column("project", 1, 0)
df_project_new = pd.DataFrame({'Project_Name': main_kws})
df_project = pd.concat([df_project, df_project_new], axis=0).drop_duplicates(subset=['Project_Name']).reset_index(drop=True)


# 3. 저장 (새 파일명 사용)
output_path = "Smart_Keyword_DB_populated.xlsx"
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_basic.to_excel(writer, sheet_name='Basic_Info', index=False)
    df_re.to_excel(writer, sheet_name='Real_Estate', index=False)
    df_life.to_excel(writer, sheet_name='Life_Interest', index=False)
    df_project.to_excel(writer, sheet_name='Project_Specific', index=False)
    df_rules.to_excel(writer, sheet_name='Rules', index=False)

print(f"Updated {output_path} with extracted data.")
print(f"- Basic Regions: {len(df_basic)}")
print(f"- Real Estate Types: {len(df_re)}")
print(f"- Life Keywords: {len(df_life)}")
print(f"- Project Keywords: {len(df_project)}")
