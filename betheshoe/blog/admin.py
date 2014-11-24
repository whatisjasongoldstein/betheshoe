from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["title", "subtitle", "author", "created_at", "published"]

admin.site.register(Post, PostAdmin)