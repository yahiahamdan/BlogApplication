from django.contrib import admin

# Register your models here.
from .models import Post,Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','created','active']
    list_filter=['active','created','updated']
    search_fields=['name','email','body']