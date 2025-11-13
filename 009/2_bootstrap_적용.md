# Bootstrap 템플릿 적용 가이드

내가 지금 명령어.md 파일에 있는 모든 명령어를 수행해서 블로그를 만들었어. 이제 이 페이지에 bootstrap이 적용된 blog 템플릿을 입히고 싶어. 아래 요구사항을 따라줘.

## 요구사항

### 1. 파일 복사
`startbootstrap-clean-blog-gh-pages` 폴더 안에 있는 HTML, CSS, JS 파일들을 Django 프로젝트의 적절한 위치로 복사해줘.
- static 파일들은 적절한 static 폴더로
- HTML 파일들은 templates 폴더로

### 2. base.html 수정
Django의 템플릿 상속 기능을 사용하여 `base.html` 파일을 수정해줘.
- {% load static %} 태그 추가
- static 파일 경로를 Django static 태그로 변경
- {% block %} 태그들을 적절히 배치

### 3. 기존 블로그 기능 통합
기존 블로그 기능들(글 목록, 상세보기, 작성, 수정, 삭제, 검색, 카테고리/태그 필터링 등)을 bootstrap 템플릿의 적절한 위치에 통합해줘.
- 만약 bootstrap 템플릿에 해당 기능을 표현할 UI가 없다면 bootstrap 스타일에 맞게 생성해줘.

### 4. Tailwind 제거
tailwind 관련 파일 및 코드를 모두 제거해줘.
- HTML에서 tailwind 클래스 제거
- tailwind CSS 링크 제거
- 관련 설정 파일 삭제

### 5. 모든 페이지에 Bootstrap 적용
모든 페이지(목록, 상세, 작성, 수정)에 bootstrap이 일관되게 적용되도록 해줘.
- 기존 Django 템플릿 태그와 URL 태그들은 반드시 유지
- 폼 필드들도 bootstrap 스타일 적용

### 6. Settings 설정 확인
settings.py의 STATIC_URL과 STATICFILES_DIRS 설정을 확인하고 필요시 수정해줘.
