# macOS 설정 가이드

집에서 Mac으로 프로젝트를 동기화하는 방법입니다.

## 1. 저장소 클론

```bash
# 원하는 위치로 이동
cd ~/Projects  # 또는 원하는 디렉토리

# 저장소 클론
git clone https://github.com/jojongho/marketing.git

# 프로젝트 폴더로 이동
cd marketing
```

## 2. Git 설정 (중요!)

```bash
# macOS에서 줄바꿈 문자 자동 변환 설정
git config --global core.autocrlf input
```

이 설정은 **한 번만** 하면 됩니다.

## 3. 일상적인 작업 흐름

### 작업 시작 전 (최신 버전 가져오기)
```bash
git pull
```

### 작업 후 (변경사항 업로드)
```bash
git add .
git commit -m "작업 내용 설명"
git push
```

## 4. 빠른 참조

| 작업 | 명령어 |
|------|--------|
| 최신 버전 가져오기 | `git pull` |
| 변경사항 확인 | `git status` |
| 변경사항 추가 | `git add .` |
| 커밋 | `git commit -m "메시지"` |
| 업로드 | `git push` |

## 5. 주의사항

- **작업 전 항상 `git pull`**: 다른 컴퓨터에서 작업한 내용이 있을 수 있습니다
- **작업 후 `git push`**: 변경사항을 GitHub에 업로드해야 다른 컴퓨터에서도 사용 가능합니다
- **CSV 파일**: UTF-8 인코딩 유지 (네이버 파워링크는 UTF-8 with BOM 필요할 수 있음)

## 문제 해결

### 충돌 발생 시
```bash
git pull
# 충돌 파일을 수동으로 수정 후
git add .
git commit -m "충돌 해결"
git push
```

### 원격 저장소 확인
```bash
git remote -v
```

---

**저장소 URL**: https://github.com/jojongho/marketing


