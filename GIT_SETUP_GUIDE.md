# Git & GitHub 동기화 설정 가이드

Windows와 macOS 간 프로젝트 동기화를 위한 Git 설정 가이드입니다.

## 1. Git 초기 설정 (Windows에서 먼저 실행)

### Git 저장소 초기화
```bash
cd D:\Projects\marketing
git init
```

### Git 사용자 정보 설정 (처음 한 번만)
```bash
git config --global user.name "당신의 이름"
git config --global user.email "your-email@example.com"
```

### 줄바꿈 문자 자동 변환 설정 (중요!)
Windows와 macOS 간 호환성을 위해 자동 변환을 활성화합니다:

```bash
# Windows에서 실행
git config --global core.autocrlf true

# macOS에서 실행 (집에 가서)
git config --global core.autocrlf input
```

이 설정으로:
- **Windows**: 저장 시 CRLF → 커밋 시 LF로 변환
- **macOS**: 저장 시 LF 유지, 체크아웃 시 그대로 유지

## 2. GitHub 저장소 생성

1. GitHub.com에 로그인
2. 우측 상단 `+` 버튼 → `New repository` 클릭
3. Repository name: `marketing` (또는 원하는 이름)
4. **Public 또는 Private 선택**
5. **README, .gitignore, license는 추가하지 않음** (이미 있으므로)
6. `Create repository` 클릭

## 3. 첫 커밋 및 푸시 (Windows)

```bash
# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: 마케팅 프레임워크 프로젝트"

# GitHub 원격 저장소 연결 (YOUR_USERNAME을 실제 사용자명으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/marketing.git

# 또는 SSH 사용 시
git remote add origin git@github.com:YOUR_USERNAME/marketing.git

# 메인 브랜치 이름 설정 (GitHub 기본값에 맞춤)
git branch -M main

# 첫 푸시
git push -u origin main
```

## 4. macOS에서 클론 및 작업

집에 가서 Mac에서:

```bash
# 원하는 위치로 이동
cd ~/Projects  # 또는 원하는 디렉토리

# 저장소 클론
git clone https://github.com/YOUR_USERNAME/marketing.git

# 또는 SSH 사용 시
git clone git@github.com:YOUR_USERNAME/marketing.git

# 프로젝트 폴더로 이동
cd marketing

# Git 설정 확인 및 수정
git config --global core.autocrlf input
```

## 5. 일상적인 작업 흐름

### Windows에서 작업 후
```bash
git add .
git commit -m "작업 내용 설명"
git push
```

### macOS에서 작업 후
```bash
git add .
git commit -m "작업 내용 설명"
git push
```

### 다른 컴퓨터에서 최신 버전 가져오기
```bash
git pull
```

## 6. CSV 파일 인코딩 주의사항

네이버 파워링크 CSV 파일은 **UTF-8 with BOM** 형식이 필요할 수 있습니다.

### Windows에서 CSV 생성 시
- Excel: "다른 이름으로 저장" → "CSV UTF-8(쉼표로 구분)(*.csv)" 선택
- 또는 텍스트 에디터에서 UTF-8 with BOM으로 저장

### macOS에서 CSV 생성 시
- Numbers: "내보내기" → "CSV" 선택 (UTF-8 자동)
- 또는 텍스트 에디터에서 UTF-8로 저장

**문제 발생 시**: Git에서 파일을 받은 후 인코딩을 확인하고 필요시 변환하세요.

## 7. 충돌 해결 (Conflict Resolution)

만약 두 컴퓨터에서 동시에 같은 파일을 수정했다면:

```bash
git pull
# 충돌 발생 시 파일을 열어서 수동으로 해결
# <<<<<<< HEAD
# Windows에서 수정한 내용
# =======
# macOS에서 수정한 내용
# >>>>>>> branch-name

# 충돌 해결 후
git add .
git commit -m "충돌 해결"
git push
```

## 8. 권장 워크플로우

1. **작업 시작 전**: `git pull`로 최신 버전 가져오기
2. **작업 중**: 정기적으로 커밋하기 (작은 단위로)
3. **작업 종료 전**: `git push`로 업로드하기
4. **다른 컴퓨터에서**: `git pull`로 동기화하기

## 9. .gitignore에 포함된 항목

- OS별 시스템 파일 (.DS_Store, Thumbs.db 등)
- 에디터 설정 파일 (.vscode/, .idea/ 등)
- Obsidian 워크스페이스 설정 (개인 설정은 제외)
- 임시 파일 (*.tmp, *.bak 등)

**PDF, Excel, CSV 파일은 포함됩니다** - 필요시 .gitignore에서 제외할 수 있습니다.

## 10. 문제 해결

### 인코딩 문제
```bash
# 파일 인코딩 확인 (macOS)
file -I filename.csv

# Git에서 인코딩 강제 설정
git config --global core.quotepath false
```

### 줄바꿈 문자 문제
```bash
# 현재 설정 확인
git config --get core.autocrlf

# 설정 변경
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # macOS
```

## 추가 팁

- **작은 단위로 자주 커밋**: 큰 변경사항보다 작은 단위가 관리하기 쉬움
- **의미 있는 커밋 메시지**: 나중에 찾기 쉽도록 명확하게 작성
- **브랜치 활용**: 큰 기능 추가 시 브랜치를 만들어 작업 후 병합

