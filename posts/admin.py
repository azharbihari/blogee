from django.contrib import admin
from posts.models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class CommentAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
