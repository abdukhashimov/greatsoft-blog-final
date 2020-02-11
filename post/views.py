from post.models import Post
from post.serializers import PostListSerializer, PostDetailSerializer
from post.permissions import IsAuthorOrReadOnly
from post.pagination import PostPageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
