from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
# Create your views here.


def post_list(request):
    post_list=Post.PublishedM.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page',1)
    try:
     posts=paginator.page(page_number)
    except PageNotAnInteger:
     posts=paginator.page(1)
    except EmptyPage:
     posts=paginator.page(paginator.num_pages)
       
    return render(request,'blog/post/list.html',
                  {'posts':posts}   
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