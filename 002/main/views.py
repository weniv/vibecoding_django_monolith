# main/views.py
from django.http import HttpResponse


def home(request):
    return HttpResponse("홈 페이지")


def about(request):
    return HttpResponse("소개 페이지")


def contact(request):
    return HttpResponse("연락처 페이지")


def blog_index(request):
    return HttpResponse("블로그 메인 페이지")


def blog_post(request, post_id):
    return HttpResponse(f"블로그 글 페이지: {post_id}")


def blog_tag(request, tag_name):
    return HttpResponse(f"'{tag_name}' 태그의 블로그 글 페이지")
