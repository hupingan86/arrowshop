from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from .models import VerifyCode
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("name", "namephoto", "lianxiren")


class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='用户名', help_text='用户名', required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')])
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", help_text="密码", write_only=True
    )

    class Meta:
        model = User
        fields =("username", "namephoto", "password")