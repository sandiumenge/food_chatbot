from rest_framework import serializers
from chat.models import Conversation, ConversationMessage, UserProfile

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserProfile
        fields = '__all__'