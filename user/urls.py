from django.urls import path, include

from user.views import CreateUserView, CreateUserInfoView

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('create-info/', CreateUserInfoView.as_view(), name='create_info'),
    # path('info-readupdate/<int:pk>/', RetriveUpdateUserInfo.as_view(),
        #  name='info_readupdate'),
]
