from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown
from django.db.models import Count
register=template.Library()

@register.simple_tag
def total_post():
    return Post.PublishedM.count()
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts=Post.PublishedM.order_by('-publish')[:count]
    return {'last_post':latest_posts}
@register.simple_tag
def get_most_commented_posts(count=5):
 posts= Post.PublishedM.annotate(
  total_comments=Count('comments')
 ).order_by('-total_comments')
 return posts
    #return {'posts',PostList}
@register.filter(name='markdown')
def markdown_format(text):
   return mark_safe(markdown.markdown(text))