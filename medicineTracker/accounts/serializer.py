from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name', 'is_verified']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
# class AllergiesSerializer(serializers.ModelSerializer):
#     user = ProfileSerializer()
#     class Meta:
#         model = Allergies
#         fields = '__all__'
#
# class HistorySerializer(serializers.ModelSerializer):
#     user = ProfileSerializer()
#     class Meta:
#         model = Allergies
#         fields = '__all__'