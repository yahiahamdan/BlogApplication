from django import template
from ..models import Post
register=template.Library()

@register.simple_tag
def total_post():
    return Post.PublishedM.count()
@register.inclusion_tag('blog/post/lastest_posts.html')
def show_lastest_posts(count=5):
    lastest_posts=Post.PublishedM.order_by('-publish')[:count]
    return {'lastest_Posts':lastest_posts}