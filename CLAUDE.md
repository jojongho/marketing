# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **real estate marketing framework** for managing multi-channel advertising campaigns and landing pages for apartment sales (분양) projects in Korea. The framework emphasizes reusability, data-driven optimization, and systematic documentation through an Obsidian-based knowledge management system.

**Primary Goal:** Create reusable marketing assets and processes that can be applied across multiple real estate projects while continuously learning and improving.

**Technology Stack:**
- **Documentation:** Obsidian (Markdown + YAML frontmatter)
- **Landing Pages:** Figma → Figma Site, Notion Bullet Builder
- **Advertising Platforms:** Naver PowerLink (primary), Kakao, Meta, Danggeun (당근마켓)
- **Analytics:** GA4, Naver Analytics
- **Automation:** Python scripts for keyword generation and CSV processing
- **File Management:** CSV exports for bulk keyword uploads to Naver PowerLink

## Python Development Environment

**Key Python Scripts Location:** `03. 광고 캠페인/02. 네이버/03. 도구 개발/`

**Core Tools:**

- `generate_draft.py` - Generates keyword combinations using itertools (regions × types × suffixes)
- `create_combiner_tool.py` - Creates Excel-based keyword combiner with formulas
- `populate_db.py` - Populates Smart_Keyword_DB.xlsx from source Excel files
- `create_db_template.py` - Creates template database structure
- `analyze_excels.py` - Analyzes existing Excel files for data extraction
- `inspect_source_files.py` - Inspects source Excel structure

**Running Python Tools:**

```bash
# Navigate to tools directory
cd "03. 광고 캠페인/02. 네이버/03. 도구 개발"

# Generate keyword draft CSV
python generate_draft.py

# Create Excel keyword combiner tool
python create_combiner_tool.py

# Populate database from source files
python populate_db.py
```

**Dependencies:**

- pandas
- openpyxl (for Excel file manipulation)
- itertools (standard library, for Cartesian product keyword combinations)

## Repository Structure

```
marketing/
├─ 00. 프레임워크 코어/          # Reusable templates and checklists
├─ 01. 브랜드 아이덴티티/         # Brand strategy, personas
├─ 02. 랜딩페이지/               # Landing page designs and copy
│  ├─ 01. Figma 디자인 시스템/
│  └─ 02. 섹션별 카피 템플릿/
├─ 03. 광고 캠페인/              # Ad campaigns by platform
│  ├─ 01. 광고 소재 제작/
│  ├─ 02. 네이버/
│  ├─ 03. 당근마켓/
│  ├─ 04. 메타 광고/
│  └─ 05. 카카오 비즈니스/
├─ 04. 콘텐츠 전략/              # YouTube, blog, SNS content
│  ├─ 01. 블로그 콘텐츠/
│  ├─ 02. 소셜미디어/
│  └─ 03. 유튜브 채널 전략/
├─ 05. 퍼스널 브랜딩/            # Portfolio and personal branding
├─ 06. 데이터 분석/              # Analytics and performance tracking
│  └─ 01. 전환 추적 설정/
├─ 07. 프로젝트 데이터베이스/     # Project-specific data
│  ├─ 01. 재사용 자산 라이브러리/
│  └─ 02. 현장별 프로젝트/       # Individual project folders
│     └─ 01. [프로젝트명]/       # Per-project organization
│        ├─ README.md           # Project overview
│        ├─ 00. 레퍼런스/       # Research materials
│        ├─ 01. 광고 캠페인/    # Campaign files
│        ├─ 02. 랜딩페이지/     # Landing page content
│        ├─ 03. 브랜드 전략/    # Brand messaging
│        └─ 04. 콘텐츠/         # Media assets
├─ 08. 학습 노트/                # Learning notes and documentation
├─ 09. 레퍼런스/                 # Reference materials by category
│  ├─ 01. 경쟁사 분석/
│  ├─ 02. 기술 문서/
│  ├─ 03. 마케팅/
│  ├─ 04. 마케팅 사례/
│  └─ 05. 업계 트렌드/
└─ templates/                   # Obsidian templates
```

## YAML Frontmatter System

All Markdown files use YAML frontmatter for metadata. Common properties:

```yaml
---
type: 프로젝트|학습노트|레퍼런스|광고캠페인|랜딩페이지
project_name: 아산배방우방아이유쉘
status: 진행중|완료|대기
date_created: YYYY-MM-DD
tags:
  - 프로젝트
  - 분양전환
primary_kpi: 전화문의|상담신청
---
```

**Important:** Preserve YAML frontmatter when editing files. This metadata is used for Obsidian queries and organization.

## Working with Projects

### Starting a New Project

1. Copy `templates/프로젝트_현장_템플릿.md`
2. Create folder: `07. 프로젝트 데이터베이스/02. 현장별 프로젝트/01. [현장명]/`
3. Fill in YAML frontmatter with project details
4. Follow checklist in template

### Project File Organization

Each project folder contains (numbered subfolders):
- **README.md:** Project overview, SWOT, roadmap
- **00. 레퍼런스/:** Research data, competitor analysis
- **01. 광고 캠페인/:** Keyword lists, ad copy, campaign plans
- **02. 랜딩페이지/:** Page structure, copy by section
- **03. 브랜드 전략/:** Brand messaging, positioning
- **04. 콘텐츠/:** Video scripts, blog posts, media

## Advertising Campaign Workflows

### Naver PowerLink (Primary Platform)

**Keyword Management:**
- Use CSV format for bulk uploads (광고그룹ID, 키워드, 입찰가, 매칭옵션, 사용여부)
- Organize keywords by tiers (Tier 1-5) based on search intent
- Default to 확대 (broad match) for maximum exposure
- Test files: `TEST_파워링크_키워드_500개_업로드용.csv` pattern

**Strategy:**
- "Eiffel Tower Effect" (에펠탑 효과): High-frequency, low-cost exposure for brand awareness
- Create 100 ad groups × 1,000 keywords = 100,000 total capacity
- Bidding: 70-200 KRW per keyword based on tier

**File Naming:**
- Keyword lists: `[NN]_키워드_리스트_[설명].md`
- Campaign plans: `[NN]_광고그룹_설계서_[플랫폼].md`
- Ad copy: `[NN]_광고카피_라이브러리_[특징].md`

### Landing Page Development

**Platform:** Notion Bullet Builder (CMS-based rapid deployment)

**Process:**
1. Create site structure: `00_사이트구조_설계서.md`
2. Write detailed content for each page: `01_메인_홈페이지.md`, `02_3대_특별혜택.md`, etc.
3. Each MD file → Notion page via Notion agent
4. Implement with mobile optimization, floating CTAs, phone click tracking

**Page Phases:**
- Phase 1 (1-2 days): Main home, benefits, contact form
- Phase 2 (3-4 days): Facilities, location, pricing
- Phase 3 (5-7 days): Target-specific pages (신혼부부, 직장인, 가족, 투자자)

## Document Conventions

### Variable Substitution Pattern

Templates use `{변수명}` for easy replacement:
- `{현장명}` - Project name
- `{지역명}` - Area name
- `{역명}` - Station name
- `{핵심강점}` - Key differentiators

### Korean Marketing Terminology

- **분양:** Apartment pre-sales
- **분양전환:** Conversion from rental to sales
- **즉시입주:** Immediate move-in available
- **초품아:** Elementary school within complex
- **역세권:** Station area (near subway)
- **실거주:** Actual residence (vs investment)

### File Naming Conventions

**Folders:** Use number + period + space format
- Top-level: `00. 프레임워크 코어/`, `01. 브랜드 아이덴티티/`
- Subfolders: `01. 광고 소재 제작/`, `02. 네이버/`
- Projects: `01. 아산배방우방아이유쉘/`

**Documents:** Use descriptive Korean names with underscores
- Campaign docs: `브랜드_메시지_아키텍처.md`
- Numbered sequences: `01_메인_홈페이지.md`, `02_3대_특별혜택.md`
- Landing pages: Sequential numbering within project folders

## CSV Export Requirements

When creating keyword CSV files for Naver PowerLink:

**Required columns:**

```csv
광고그룹ID,키워드,입찰가,매칭옵션,사용여부
```

**Format rules:**

- Leave 광고그룹ID empty for bulk upload
- 입찰가: Integer (70-200 typical range)
- 매칭옵션: 확대 (broad match)
- 사용여부: Y or N
- UTF-8 encoding with BOM for Korean characters
- Maximum 10,000 rows per file (1,000 keywords per ad group limit)

**Naver Template Files:** Located in `templates/` directory

- `ko_add_keyword_template(키워드 등록 템플릿).csv` - Keyword registration template
- `ko_keyword_estimate_template(키워드 견적 템플릿).csv` - Keyword estimation template
- `ko_add_ad_template(단일형 소재등록 템플릿).csv` - Single ad creative template
- `ko_add_rsa_ad_template(반응형 소재등록 템플릿).csv` - Responsive ad creative template

## Keyword Generation Architecture

**Cartesian Product Approach:**

The `generate_draft.py` script uses Python's `itertools.product()` to create keyword combinations:

```python
# Example from generate_draft.py
regions = ["아산", "배방", "천안", "탕정", "불당"]
types = ["아파트", "오피스텔", "분양", "전세", "월세"]
suffixes = ["정보", "시세", "전망", "순위", "추천"]

# Combination 1: regions × types
keywords1 = [f"{r} {t}" for r, t in itertools.product(regions, types)]

# Combination 2: regions × types × suffixes
keywords2 = [f"{r} {t} {s}" for r, t, s in itertools.product(regions, types, suffixes)]
```

**Excel Formula Approach:**

The `create_combiner_tool.py` creates an Excel file with dynamic formulas that auto-generate keywords as users input data in columns A, B, C:

- Column A: 지역 (regions)
- Column B: 업종/유형 (types)
- Column C: 세부/관심사 (suffixes)
- Column E: Auto-generated 1차 조합 (A + B)
- Column F: Auto-generated 2차 조합 (E + C)

**Smart Keyword Database:**

Excel-based database structure (`Smart_Keyword_DB.xlsx`):

- `Basic_Info` sheet: Region hierarchy (L1, L2)
- `Real_Estate` sheet: Property types, targets, attributes
- `Life_Interest` sheet: Location details, brand names, categories
- `Project_Specific` sheet: Project-specific keywords
- `Rules` sheet: Combination rules and logic

## Working with This Codebase

### When Creating Marketing Materials

1. **Check templates first:** Always look in `templates/` for reusable patterns
2. **Maintain YAML frontmatter:** Essential for Obsidian organization
3. **Use variable substitution:** Make content reusable across projects
4. **Document learnings:** Add insights to `08_학습_노트/`

### When Editing Projects

1. **Read README.md first:** Understand project status and goals
2. **Update checklists:** Mark completed items in project roadmap
3. **Preserve file structure:** Keep organized folder hierarchy
4. **Link related documents:** Use Obsidian `[[WikiLinks]]` for cross-references

### When Creating Landing Page Content

1. **One MD file per page:** Each landing page = separate markdown document
2. **Include all sections:** Hero, features, CTA, FAQ, mobile optimization notes
3. **Add Notion implementation guide:** Block types, layout instructions
4. **Mobile-first:** Always include mobile optimization checklist

### Primary KPI Focus

**전화문의 (Phone inquiries) is the #1 conversion metric** for all projects. When creating:
- Landing pages → Optimize for click-to-call
- Ad copy → Drive phone action
- Analytics → Track phone button clicks
- CTAs → Floating phone buttons on mobile

## Common Tasks

### Generate Keyword List for New Project

#### Option 1: Using Python Script

```bash
cd "03. 광고 캠페인/02. 네이버/03. 도구 개발"
python generate_draft.py
# Output: keyword_draft_v1.csv with auto-generated combinations
```

#### Option 2: Using Excel Combiner Tool

```bash
cd "03. 광고 캠페인/02. 네이버/03. 도구 개발"
python create_combiner_tool.py
# Output: Keyword_Combiner_Tool.xlsx
# Then manually input regions, types, suffixes in columns A, B, C
```

#### Post-generation

1. Review generated keywords for relevance
2. Apply Tier 1-5 classification (based on search intent)
3. Set appropriate bid prices (입찰가: 70-200 KRW)
4. Export as CSV with proper UTF-8-BOM encoding
5. Name: `TEST_파워링크_키워드_[N]개_업로드용.csv`

### Create Landing Page Structure

1. Start with `00_사이트구조_설계서.md` (11-page sitemap)
2. Create Phase 1 essential pages first (메인, 혜택, 상담)
3. Each page as separate MD with full content
4. Ready for Notion agent implementation

### Set Up New Project

1. Use `templates/프로젝트_현장_템플릿.md`
2. Create folder: `07. 프로젝트 데이터베이스/02. 현장별 프로젝트/[NN]. [현장명]/`
3. Create subfolders:
   - `00. 레퍼런스/` - Research and competitor analysis
   - `01. 광고 캠페인/` - Campaign files and keywords
   - `02. 랜딩페이지/` - Landing page content
   - `03. 브랜드 전략/` - Brand messaging
   - `04. 콘텐츠/` - Media assets
   - `05. 성과 데이터/` - Analytics and performance data
4. Complete SWOT analysis in README.md
5. Define 3 target personas
6. Identify 8 key differentiators
7. Follow `QUICK_START.md` workflow

### Working with Excel Data Sources

**Source Excel Files Location:** `03. 광고 캠페인/02. 네이버/05. 엑셀/`

Key files:

- `부동산 마케팅 키워드.xlsx` - Real estate marketing keyword library
- `아산 배방 우방아이유쉘 키워드.xlsx` - Project-specific keywords
- `키워드추출_cso9858_naver.xlsx` - Extracted keywords from Naver account

**Inspecting Excel files:**

```bash
cd "03. 광고 캠페인/02. 네이버/03. 도구 개발"
python inspect_source_files.py  # Analyze Excel structure
python analyze_excels.py        # Extract data patterns
```

### Converting CSV Encoding for Naver Upload

When exporting CSV for Naver PowerLink, ensure UTF-8 with BOM encoding:

```python
# In pandas
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
```

The `-sig` parameter adds the BOM marker required for Korean characters in Naver's system.

## Reference Documents

- **Overall guide:** [README.md](README.md)
- **Quick start:** [QUICK_START.md](QUICK_START.md)
- **Active project example:** `07. 프로젝트 데이터베이스/02. 현장별 프로젝트/01. 아산배방우방아이유쉘/`
- **Naver guide:** `03. 광고 캠페인/02. 네이버/README.md`
- **Reference materials:** `09. 레퍼런스/03. 마케팅/`

## Key Principles

1. **Reusability First:** Every asset should be template-ready for next project
2. **Data-Driven:** Measure everything, optimize based on metrics
3. **Mobile-Optimized:** 70%+ traffic from mobile devices
4. **Learning by Doing:** Document insights after each campaign
5. **Phone Calls Win:** Optimize for phone inquiries above all else
