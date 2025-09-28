from rest_framework import serializers
from chat.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['foods', 'is_vegetarian', 'created_at']