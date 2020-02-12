from post.models import Post, Category, Tag
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    PrimaryKeyRelatedField,
    SerializerMethodField,
    StringRelatedField,
    ModelSerializer,
)
from comment.serializers import CommentSerializer


class PostListSerializer(ModelSerializer):
    author = StringRelatedField()
    url = HyperlinkedIdentityField(
        view_name='post:post-detail',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('url', 'title', 'thumbnail', 'author', 'timestamp')


class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    tag = StringRelatedField(many=True, read_only=True)
    category = StringRelatedField(many=True, read_only=True)
    comment = SerializerMethodField()
    timestamp = SerializerMethodField()

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

    def get_timestamp(self, obj):
        return str(obj.timestamp)

class PostCreateSerializer(ModelSerializer):
    tag = PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    category = PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'thumbnail',
                  'content', 'tag', 'category')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
