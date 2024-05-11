from django import template
from ..models import Post
register=template.Library()

@register.simple_tag
def total_post():
    return Post.PublishedM.count()
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts=Post.PublishedM.order_by('-publish')[:count]
    return {'last_post':latest_posts}