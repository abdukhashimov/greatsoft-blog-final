from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet, TagView, CategoryView


router = DefaultRouter()
router.register('posts', PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
    path('tag/', TagView.as_view(), name='tag-list-create'),
    path('category/', CategoryView.as_view(), name='cat-list-create'),
]
