from post.serializers import (
    PostDetailSerializer,
    PostCreateSerializer,
    PostListSerializer,
    CategorySerializer,
    TagSerializer
)
from post.models import Post, Tag, Category
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from post.pagination import PostPageNumberPagination
from rest_framework.generics import ListCreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from comment.serializers import CreateCommentSerializer, SaveCommentSerializer
from post.permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly, IsPostCorrect


class PostViewSet(ModelViewSet):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny, ]
        elif self.action in ('create', 'post_comment'):
            permission_classes = [IsAuthenticated, IsPostCorrect]
        else:
            permission_classes = [IsAuthorOrReadOnly, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'post_comment':
            return CreateCommentSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['POST'], detail=True, url_path='post-comment')
    def post_comment(self, request, pk=None):
        """Posts a comment"""
        output = {}
        post = self.get_object()
        output = request.data.copy()
        output['post'] = post.id
        output['user'] = request.user.id
        serializer = SaveCommentSerializer(data=output)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK)
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST)


class TagView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]


class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]
