from rest_framework import serializers
from .models import Account
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerialiser


class CustomUserSerializer(BaseUserRegistrationSerialiser):
    class Meta(BaseUserRegistrationSerialiser.Meta):
        fields = ('id', 'username', 'password', 'email','age')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
