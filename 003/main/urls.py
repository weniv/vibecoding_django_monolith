# main/urls.py (새로 생성)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<int:post_id>/", views.blog_post, name="blog_post"),
    path("blog/<str:tag_name>/", views.blog_tag, name="blog_tag"),
]
