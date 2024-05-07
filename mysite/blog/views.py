from django.shortcuts import render
from django.http import Http404
from .models import Post
# Create your views here.
def post_list(request):
    post=Post.PublishedM.all()
    return render(request,'blog/post/list.html',
                  {'posts':post}   
                  )
def post_detail(request,id):
    try:
        post=Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("no post found with this id")
    return render(request,'blog/post/detail.html',{'post':post})