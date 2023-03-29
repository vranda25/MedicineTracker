from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = '__all__'