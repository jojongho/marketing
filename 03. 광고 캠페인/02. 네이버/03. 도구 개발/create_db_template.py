import pandas as pd
import os

# 1. 시트별 데이터 정의

# Sheet 1: Basic_Info (기본 정보)
basic_data = {
    "Region_L1": ["충남", "충남", "충남", "충남", "충남"],
    "Region_L2": ["아산", "천안", "배방", "탕정", "불당"],
    "Suffix_Info": ["정보", "시세", "전망", "순위", "추천"],
    "Suffix_Action": ["분양", "매매", "전세", "월세", "임대"]
}

# Sheet 2: Real_Estate (부동산 키워드)
re_data = {
    "Type": ["아파트", "오피스텔", "빌라", "원룸", "투룸"],
    "Feature": ["민간임대", "공공임대", "신축", "미분양", "대단지"],
    "Target": ["신혼부부", "1인가구", "투자자", "갭투자", "실거주"]
}

# Sheet 3: Life_Interest (생활/업종 키워드 - 에펠탑 효과)
life_data = {
    "Category": ["식음료", "식음료", "편의시설", "편의시설", "공공기관"],
    "Brand_Name": ["메가커피", "스타벅스", "타이마사지", "헬스장", "아산시청"],
    "Location_Detail": ["공수리", "배방역", "탕정역", "불당동", "북수리"],
    "Search_Intent": ["메뉴", "가격", "위치", "전화번호", "민원"]
}

# Sheet 4: Project_Specific (현장 전용 - 매번 바뀜)
# 모든 리스트의 길이가 같아야 함 (최대 길이 5로 맞춤)
project_data = {
    "Project_Name": ["아산배방우방아이유쉘", "배방우방아이유쉘", "우방아이유쉘", "", ""],
    "Competitors": ["탕정푸르지오", "아산자이", "한화포레나", "더샵센트로", "칸타빌"],
    "USP_Keywords": ["즉시입주", "회사보유분", "전세형", "4년전세", "확정분양가"]
}

# Sheet 5: Rules (필터링 규칙)
# 모든 리스트의 길이가 같아야 함 (최대 길이 4로 맞춤)
rule_data = {
    "Exclude_Contains": ["회룡리 아파트", "공수리 빌라", "성인", "도박"],
    "Must_Include": ["", "", "", ""],
    "Replace_From": ["우방 아이유쉘", "", "", ""],
    "Replace_To": ["우방아이유쉘", "", "", ""]
}

# 2. 엑셀 파일 생성
output_path = "Smart_Keyword_DB.xlsx"

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    pd.DataFrame(basic_data).to_excel(writer, sheet_name='Basic_Info', index=False)
    pd.DataFrame(re_data).to_excel(writer, sheet_name='Real_Estate', index=False)
    pd.DataFrame(life_data).to_excel(writer, sheet_name='Life_Interest', index=False)
    pd.DataFrame(project_data).to_excel(writer, sheet_name='Project_Specific', index=False)
    pd.DataFrame(rule_data).to_excel(writer, sheet_name='Rules', index=False)

print(f"Created {output_path} with 5 sheets.")
