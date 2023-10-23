from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'type', 'user_id', 'full_name', 'username', 'language', 'register_time', 'balance']