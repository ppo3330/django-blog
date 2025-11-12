# Junseok Django Blog

Django로 개발한 개인 블로그 프로젝트입니다.  
기본적인 CRUD 기능(글 작성, 수정, 삭제, 조회)과  
댓글 기능, 검색, 페이지네이션, 스타일 통일 등을 구현했습니다.

---

# 프로젝트 소개

이 블로그는 Django 학습의 일환으로 직접 설계하고 구현한 프로젝트입니다.  
Python과 Django의 핵심 기능을 연습하면서 실제 웹 서비스 형태로 발전시켰습니다.

# 주요 기능
- 글 작성 / 수정 / 삭제 / 목록 보기
- 댓글 작성 / 수정 / 삭제
- 검색 기능 (엔터로 검색)
- 페이지네이션 (글 목록 나누기)
- 스타일 통일
- base.html 기반 템플릿 구조

---

# 기술 스택

 사용 기술 
- Backend: Django 5.2, Python 3.12
- Frontend: HTML, CSS
- DB: SQLite3 (기본 내장)
- Tools: Git, GitHub, CMD
- Editor: Python IDLE , VS CODE

---

# 실행 방법

bash
- 가상환경 생성 및 활성화
python -m venv env
env\Scripts\activate   # (Windows)

- Django 설치
pip install django

- 마이그레이션
python manage.py migrate

- 개발 서버 실행
python manage.py runserver

- 블로그 접속
브라우저에서 http://127.0.0.1:8000/blog/ 접속

---

# 실행 방법

Django의 MVC 구조 (Model-View-Template)
ORM을 활용한 데이터베이스 조작
URL routing과 view 연결
Template 상속(base.html)
GitHub를 통한 버전 관리 및 협업 흐름 익히기

---

# 마무리
이 프로젝트는 학습용으로 제작되었습니다.
자유롭게 참고 및 수정 가능합니다.