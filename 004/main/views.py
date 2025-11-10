# main/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def home(request):
    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def blog_index(request):
    posts = Post.objects.filter(is_published=True)
    context = {"posts": posts}
    return render(request, "main/blog_index.html", context)


def blog_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    context = {"post": post}
    return render(request, "main/blog_post.html", context)


def blog_tag(request, tag_name):
    tag = get_object_or_404(Tag, slug=tag_name)
    posts = tag.posts.filter(is_published=True)
    context = {"tag": tag, "posts": posts}
    return render(request, "main/blog_tag.html", context)
