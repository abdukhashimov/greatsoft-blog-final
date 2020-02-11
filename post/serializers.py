from post.models import Post
from rest_framework.serializers import (
    StringRelatedField,
    SerializerMethodField,
    HyperlinkedIdentityField,
    ModelSerializer
)
from comment.serializers import CommentSerializer


class PostListSerializer(ModelSerializer):
    author = StringRelatedField()
    # url = HyperlinkedIdentityField(
    #     view_name='post-detail',
    #     read_only=True,
    # )

    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'author', 'timestamp')


class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    tag = StringRelatedField(many=True, read_only=True)
    category = StringRelatedField(many=True, read_only=True)
    comment = SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'author',
                  'content', 'tag', 'category', 'timestamp', 'comment')

    def get_author(self, obj):
        user = {}
        user['author'] = str(obj.author)
        user['profice_picture'] = obj.author.get_profile_picture
        return user

    def get_comment(self, obj):
        comments = {}
        for index, comment in enumerate(obj.get_comments):
            comments[str(index)] = CommentSerializer(comment).data

        return comments
