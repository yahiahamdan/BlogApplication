from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Post
# Create your views here.


def post_list(request):
    post=Post.PublishedM.all()
    return render(request,'blog/post/list.html',
                  {'posts':post}   
                  )

def post_detail(request,year,month,day,post):
    # try:
    #     post=Post.PublishedM.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("no post found with this id")
    # return render(request,'blog/post/detail.html',{'post':post})
    post=get_object_or_404(Post,
                          status= Post.Status.PUBLISHED,
                          slug=post,
                          publish__year=year,
                          publish__month=month,
                          publish__day=day
                           )
    return render(request,'blog/post/detail.html',{'post':post})