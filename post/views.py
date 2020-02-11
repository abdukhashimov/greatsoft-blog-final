from post.serializers import (
    PostDetailSerializer,
    PostCreateSerializer,
    PostListSerializer,
    CategorySerializer,
    TagSerializer
)
from post.models import Post, Tag, Category
from post.permissions import IsAuthorOrReadOnly
from post.pagination import PostPageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView


class PostViewSet(ModelViewSet):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny, ]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, ]
        else:
            permission_classes = [IsAuthorOrReadOnly, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
