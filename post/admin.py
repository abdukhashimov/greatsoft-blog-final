from django.contrib import admin
from post.models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'thumbnail', 'content', 'tag', 'category')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
