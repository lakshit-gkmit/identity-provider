from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError('Must include "username" and "password".')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise serializers.ValidationError('User not found.')

        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect password.')

        return user
