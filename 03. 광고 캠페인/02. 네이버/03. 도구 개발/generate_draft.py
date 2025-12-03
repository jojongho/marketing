import pandas as pd
import itertools

# 1. 키워드 소스 정의
regions = ["아산", "배방", "천안", "탕정", "불당"]
types = ["아파트", "오피스텔", "분양", "전세", "월세", "임대", "민간임대", "모델하우스", "홍보관"]
suffixes = ["정보", "시세", "전망", "순위", "추천", "미분양", "줍줍"]

# 2. 조합 로직 (Cartesian Product)
# 조합 1: 지역 + 유형 (예: 아산 아파트, 배방 전세)
comb1 = list(itertools.product(regions, types))
keywords1 = [f"{r} {t}" for r, t in comb1]

# 조합 2: 지역 + 유형 + 접미사 (예: 아산 아파트 시세, 천안 분양 정보)
comb2 = list(itertools.product(regions, types, suffixes))
keywords2 = [f"{r} {t} {s}" for r, t, s in comb2]

# 3. 데이터프레임 생성
all_keywords = keywords1 + keywords2
df = pd.DataFrame(all_keywords, columns=["Keyword"])

# 4. 예상 입찰가 및 그룹 분류 (가상 데이터)
df["Group"] = "에펠탑_일반"
df["Est_Bid"] = 70 # 최저가 가정

# 5. CSV 저장
output_path = "keyword_draft_v1.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Generated {len(df)} keywords.")
print(df.head(10))
