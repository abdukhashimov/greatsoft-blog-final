from django.db import models
from post.models import Post
from django.contrib.auth import get_user_model
from django.contrib.admin.utils import NestedObjects


class CommentManager(models.Manager):
    def get_parent_comment(self, id):
        return super(
            CommentManager, self
        ).get_queryset().filter(id=id, parent_id__isnull=True)

    def get_child_comment(self, id):
        parents = Comment.objects.filter(id=id)
        collector = NestedObjects(using='default')
        collector.collect(parents)
        collector.data[parents[0].__class__].remove(parents[0])
        return collector.data[parents[0].__class__]


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', related_name='reply', null=True,
        blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at', ]

    objects = CommentManager()

    def __str__(self):
        if self.parent is None:
            return "{}'s comment".format(str(self.user))
        return "{}'s reply".format(str(self.user))

    @property
    def child_comments(self):
        return Comment.objects.get_child_comment(self.id)
