from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

from .models import AppUser


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password', 'user_knowledge_level', 'credit_coins', ]
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer[AppUser]):
    # class Meta:
    #     model = AppUser
    #     fields = ['email', 'username', 'user_knowledge_level', 'credit_coins', ]

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        # token['user_knowledge_level'] = user.user_knowledge_level
        # token['credit_coins'] = user.credit_coins

        return token
