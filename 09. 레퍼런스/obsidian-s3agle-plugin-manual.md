---
title: S3agle File Management for Obsidian
aliases:
  - Plugin
  - obsidian
  - 옵시디언플러그인
creation date: 2025-10-04
modification date: 2025-10-04
tags:
  - obsidian/plugin
  - 플러그인
  - 설명서
  - file-management
  - s3
  - eagle
categories:
  - Plugin Documentation
plugin_category: file management
plugin_status: active
difficulty_level: hard
GitHub_Repository: https://github.com/turnercore/s3agle
---
## 📋 플러그인 기본 정보

| 항목 | 내용 |
|---|---|
| **플러그인 이름** | S3agle File Management for Obsidian |
| **개발자** | turnercore |
| **버전** | 0.5.9 |
| **최종 업데이트** | |
| **GitHub 저장소** | [https://github.com/turnercore/s3agle](https://github.com/turnercore/s3agle) |
| **공식 문서** | [https://github.com/turnercore/s3agle](https://github.com/turnercore/s3agle) |
| **라이센스** | |
| **코어 플러그인** | No |

## 🎯 플러그인 개요

### 📝 주요 기능
- **자동 파일 업로드:** 노트에 이미지, 비디오, PDF 등 파일을 드래그 앤 드롭하거나 붙여넣으면 S3 호환 스토리지 및/또는 Eagle 앱으로 자동 업로드합니다.
- **링크 변환:** 로컬 파일 링크를 S3의 공개 URL로 자동 변환하여 노트에 삽입합니다.
- **Eagle 앱 통합:** 디지털 자산 관리 앱인 Eagle과 연동하여 파일을 체계적으로 관리하고, S3 링크를 Eagle의 메타데이터에 저장합니다.
- **파일 동기화 명령어:** Vault의 모든 파일을 S3/Eagle로 업로드하거나, S3의 모든 파일을 로컬로 다운로드하는 명령어를 제공합니다.
- **임베딩 지원:** PDF나 PPT 파일을 Google/Microsoft 뷰어를 통해 노트에 직접 임베딩할 수 있습니다.

### 💡 사용 목적
> Obsidian Vault의 크기를 가볍게 유지하고, 첨부 파일(이미지, PDF 등)을 클라우드(S3)나 전문 자산 관리 도구(Eagle)에서 체계적으로 관리하기 위해 사용합니다. 이를 통해 Vault의 동기화 속도를 높이고, 여러 장치에서 파일 접근성을 확보하며, 첨부 파일의 중앙 관리를 용이하게 합니다.

### 🚀 핵심 장점
1. **Vault 용량 관리:** 첨부 파일을 외부 스토리지로 옮겨 Vault의 크기를 획기적으로 줄일 수 있습니다.
2. **자동화된 워크플로우:** 파일을 노트에 추가하는 것만으로 업로드와 링크 변환이 자동으로 처리되어 매우 편리합니다.
3. **S3 및 Eagle 연동:** 검증된 클라우드 스토리지와 전문 자산 관리 도구를 함께 사용하여 파일 관리의 안정성과 효율성을 모두 높일 수 있습니다.

## ⚙️ 설치 및 설정

### 📥 설치 방법
1. `Settings` → `Community plugins`에서 "S3agle"을 검색하여 설치하고 활성화합니다.
2. **S3 설정 (필수):**
   - AWS S3 또는 S3 호환 스토리지(Cloudflare R2, MinIO 등)에 버킷을 생성합니다.
   - 버킷 정책을 'Public Read'로 설정하고, CORS 정책을 구성합니다.
   - 쓰기 권한이 있는 IAM 사용자의 `accessKeyId`와 `secretAccessKey`를 발급받습니다.
   - S3agle 플러그인 설정에 버킷 이름, 리전, 키 값 등을 정확하게 입력합니다.
3. **Eagle 설정 (선택):**
   - [Eagle 앱](https://eagle.cool)을 설치하고 실행합니다.
   - S3agle 플러그인 설정에서 Eagle 연동을 활성화합니다.

## 🚀 사용법 및 예시

### 📖 기본 사용법
1. 플러그인 설정에서 S3 및/또는 Eagle 설정을 완료합니다.
2. 이미지 파일을 Obsidian 노트 편집기에 드래그 앤 드롭합니다.
3. 파일이 자동으로 S3에 업로드되고, 노트에는 `![S3-URL]` 형식의 마크다운 링크가 삽입됩니다.
4. 로컬 Vault에는 파일이 저장되지 않습니다.

### 💡 활용 예시
#### 예시 1: 모바일에서 캡처한 이미지 관리
- 모바일 Obsidian 앱에서 사진을 찍어 노트에 첨부합니다.
- 데스크톱 Obsidian에서 동기화한 후, `S3agle: Upload ALL files to S3/Eagle` 명령을 실행합니다.
- 모바일에서 추가된 모든 이미지가 S3로 올라가고 링크가 변환되어, Vault 용량을 차지하지 않게 됩니다.

## ⚖️ 장단점 분석

### ✅ 장점
- 대용량 첨부 파일이 많은 사용자의 Vault 관리 부담을 크게 덜어줍니다.
- 파일 관리 워크플로우를 자동화하여 시간을 절약해 줍니다.
- S3라는 표준적이고 안정적인 서비스를 기반으로 합니다.

### ❌ 단점
- **S3 버킷 생성 및 IAM 정책 설정 등 초기 설정 과정이 매우 복잡하고 어렵습니다.**
- S3 서비스는 사용량에 따라 비용이 발생할 수 있습니다.
- 외부 스토리지에 의존하므로, 인터넷 연결이 없으면 파일을 볼 수 없습니다.

### ⚠️ 주의사항
- **S3 버킷의 권한 설정(Public Read, CORS)을 잘못하면 파일이 보이지 않거나 보안 문제가 발생할 수 있습니다.**
- `accessKeyId`와 `secretAccessKey`는 매우 민감한 정보이므로 절대 외부에 노출해서는 안 됩니다.
- 플러그인 설정에서 로컬에 파일을 저장하지 않도록 설정한 경우, S3에서 파일이 삭제되면 복구할 수 없습니다.

## 🔗 연관 플러그인

### 🤝 함께 사용하면 좋은 플러그인
- **[[Obsidian Git]] / [[Obsidian Sync]]**: S3agle로 첨부 파일을 분리하면, 텍스트 중심의 Vault는 Git이나 Sync로 훨씬 빠르고 효율적으로 동기화할 수 있습니다.
