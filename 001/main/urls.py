# '/' : 홈 페이지
# '/about': 소개 페이지
# '/contact': 연락처 페이지
# '/blog': 블로그 메인 페이지
# '/blog/1': 블로그 1번 글 페이지
# '/blog/2': 블로그 2번 글 페이지
from django.urls import path
from . import views

urlpatterns = [
    # path(URL, 함수이름 또는 메서드 이름, URL패턴 이름)
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<int:post_id>/", views.blog_post, name="blog_post"),
]
