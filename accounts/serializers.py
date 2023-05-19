
from rest_framework import serializers
from .models import Account
# from .models import Tasks
from djoser.serializers import UserCreateSerializer


class CustomUserSerialiser(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'password','email')
        
        



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
