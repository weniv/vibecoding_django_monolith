# config/urls.py
from django.contrib import admin
from django.urls import path, include

# include는 다른 앱의 url을 포함시킬 때 사용

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),  # main 앱의 urls.py를 포함시키기 위해 추가
]
