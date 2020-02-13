from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import UserInfo


class UserSerializer(serializers.ModelSerializer):
    """Serializers for the users object"""
    token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'token')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5,
                         'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class UserInfoSerializer(serializers.ModelSerializer):
    profile_picture = serializers.FileField()
    class Meta:
        model = UserInfo
        fields = ('bio', 'profile_picture')
