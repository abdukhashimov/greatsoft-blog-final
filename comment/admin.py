from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    fields = ('comment', 'parent', 'post')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Comment, CommentAdmin)
