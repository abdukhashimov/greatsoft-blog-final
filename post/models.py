from django.db import models
from post.validators.validate_post import (
    validate_name,
    validate_post_title
)
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Category of the Posts"""
    name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, validators=[validate_post_title])
    thumbnail = models.ImageField(
        upload_to="thumbnails", blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = RichTextField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.title) > 20:
            return "{}: {}".format(str(self.author), str(self.title)[:20]) +\
                '...'
        return "{}: {}".format(str(self.author), str(self.title))

    @property
    def get_comments(self):
        return self.comments.filter(parent_id__isnull=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.title = str(self.title).title()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
