from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/', include('post.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('docs/', include_docs_urls(title='Great Soft Blog',
                                    permission_classes=[AllowAny, ], authentication_classes=[]))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
