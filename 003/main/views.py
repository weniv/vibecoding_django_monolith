# main/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def home(request):
    return HttpResponse("홈 페이지")


def about(request):
    return HttpResponse("소개 페이지")


def contact(request):
    return HttpResponse("연락처 페이지")


def blog_index(request):
    posts = Post.objects.filter(is_published=True)
    posts_html = "<br>".join(
        [f"<a href='/blog/{post.id}/'>{post.title}</a>" for post in posts]
    )
    return HttpResponse(f"<h1>블로그 메인 페이지</h1>{posts_html}")


def blog_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    tags_html = ", ".join(
        [f"<a href='/blog/{tag.slug}/'>{tag.name}</a>" for tag in post.tags.all()]
    )
    return HttpResponse(
        f"<h1>{post.title}</h1><p>{post.content}</p><p>태그: {tags_html}</p>"
    )


def blog_tag(request, tag_name):
    tag = get_object_or_404(Tag, slug=tag_name)
    posts = tag.posts.filter(is_published=True)
    posts_html = "<br>".join(
        [f"<a href='/blog/{post.id}/'>{post.title}</a>" for post in posts]
    )
    return HttpResponse(f"<h1>'{tag.name}' 태그의 블로그 글</h1>{posts_html}")
