# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    # 만약 앱이 여러개면 아래와 같이 추가됩니다.
    # path("blog/", include("blog.urls") # blog 앱에 urls.py가 있어야 합니다.
    # path("shop/", include("shop.urls") # shop 앱에 urls.py가 있어야 합니다.
]
