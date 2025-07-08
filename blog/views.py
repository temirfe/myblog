from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts':posts}
    )

from django.http import Http404
def post_detail1(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No post found.')
    return render(request,'blog/post/detail.html',{'post':post})


from django.shortcuts import get_object_or_404
def post_detail(request,id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post':post}
    )