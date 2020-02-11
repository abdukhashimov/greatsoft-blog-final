from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls))
]