from user.serializers import UserSerializer, UserInfoSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from user.permissions import IsUserCorrect
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from user.models import UserInfo
from rest_framework.parsers import MultiPartParser


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]


class CreateUserInfoView(generics.CreateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated, IsUserCorrect]
    parser_classes = [MultiPartParser, ]

    def post(self, request, *args, **kwargs):
        # print('here')
        profile_picture = request.data.get('profile_picture', None)
        bio = request.data.get('bio', None)
        user_info = UserInfo.objects.create(
            user=self.request.user,
            bio=bio,
            profile_picture=profile_picture
        )
        try:
            user_info.save()
            return Response(status=HTTP_201_CREATED)
        except Exception:
            return Response(status=HTTP_400_BAD_REQUEST)
