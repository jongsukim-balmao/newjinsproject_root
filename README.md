# newjinsdocker / newjinsproject

본 저장소는 개발/배포를 염두에 둔 Django(Backend, Gunicorn) + MySQL + NGINX + React(Frontend) 도커 환경(newjinsdocker)과 Django API Server(newjinsproject)를 구성하기 위한 템플릿입니다.

## 빠른 시작 (로컬, Docker 기반)

1. 필수 소프트웨어 설치
   - Docker Desktop
   - GitHub 계정(선택: GHCR, Actions로 배포 시)
2. 환경변수 파일 생성
   - `.env`를 루트에 생성하고 `.env.example`를 참고해 값 입력
3. 컨테이너 빌드/실행
   - `docker compose up -d --build`
4. Django 초기화
   - `docker compose exec web python manage.py migrate`
   - `docker compose exec web python manage.py createsuperuser`
   - `docker compose exec web python manage.py collectstatic --noinput`
5. 접속
   - NGINX: http://localhost
   - Django Admin: http://localhost/admin

## 디렉토리 구조
- backend/ (Django + Gunicorn)
- frontend/ (React)
- nginx/ (Nginx 설정 및 정적파일 마운트 경로)
- docker-compose.yml

## GitHub Actions (CI/CD)
- `.github/workflows/ci.yml` 기본 CI 제공
- Docker 이미지 빌드 및(옵션) GHCR 푸시. 배포는 환경마다 상이하여 placeholder 주석 제공

## 추가 고려/질문 체크리스트
- 보안/비밀정보
  - 프로덕션용 SECRET_KEY 관리 방식은? (예: GitHub Secrets, Vault) 
  - DB 비밀번호/접속은 어떻게 관리하나요? RDS 등 외부 DB 사용 계획?
- 네트워크/도메인
  - 서비스 도메인, 서브도메인, SSL/TLS 인증서(예: Let’s Encrypt) 발급 방법은?
  - 프론트/백엔드 도메인이 분리되나요? CORS 정책 범위 결정 필요
- 배포 환경
  - 단일 서버 vs. 멀티 노드? Docker Swarm/Kubernetes 사용 계획?
  - 로깅/모니터링(Stackdriver, ELK, Grafana+Prometheus 등) 요구사항은?
- 스토리지
  - Django media 파일 보관: 로컬 볼륨 vs. 오브젝트 스토리지(S3 등)?
- 성능/확장
  - Gunicorn 워커/스레드 수, 타임아웃 정책? Nginx 캐시/압축 설정? 
  - 정적/미디어 파일 CDN 사용 계획?
- CI/CD
  - 어떤 브랜치 전략? (git-flow, trunk) 과 배포 트리거(태그, main push)?
  - 마이그레이션 자동화/롤백 전략은?
- 보안/규정
  - 보안 스캔(SAST/DAST), 이미지 취약점 스캔(Trivy) 필요?
  - 개인정보/로그 마스킹/보관기간 정책?

자세한 내용은 각 파일 주석과 `.env.example`를 참고해 주세요.
