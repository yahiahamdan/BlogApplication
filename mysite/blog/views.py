from django.shortcuts import render
from django.http import Http404,HttpRequest
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.

class PostListView(ListView):
  """
  alternative to post_list views
  """
  queryset=Post.PublishedM.all()
  context_object_name='posts'
  paginate_by=3
  template_name='blog/post/list.html'

def post_share(request,post_id):
  post=get_object_or_404(Post,id=post_id,status=Post.Status.PUBLISHED)
  sent=False
  if request.method=='POST':
    #FORM WITH SUBMITTED
    form=EmailPostForm(request.POST)
    if(form.is_valid()):
      #forms field passed vlaidationi
      cd=form.cleaned_data
      #send email 
      post_url=request.build_absolute_uri(post.get_absolute_url())
      subject=f"{cd['name']} recommends you read {[post.title]} "
      message=(f'read {post.title} at {post_url}\n'
               f'{cd['name']}\'s comments :{cd['comments']}'
              )
      send_mail(subject,message,'hamdanyahia2@gmail.com',[cd['to']])
      sent=True
  else:
      form=EmailPostForm()
  return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})


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