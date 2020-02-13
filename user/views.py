from user.serializers import UserSerializer, UserInfoSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]


class CreateUserInfoView(generics.CreateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
