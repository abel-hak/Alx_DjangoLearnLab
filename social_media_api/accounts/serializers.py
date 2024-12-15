from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    bio = serializers.CharField()
    profile_picture = serializers.ImageField(required=False)
    token = serializers.SerializerMethodField()  # Add token field

    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        # Retrieve or create the token for the registered user
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key
    
from rest_framework import serializers
from .models import CustomUser

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'followers', 'following']
