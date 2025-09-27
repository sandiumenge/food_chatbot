from rest_framework import viewsets
from chat.models import Conversation, ConversationMessage, UserProfile
from chat.api.serializer import ConversationSerializer, ConversationMessageSerializer, UserProfileSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class ConversationMessageViewSet(viewsets.ModelViewSet):
    queryset = ConversationMessage.objects.all()
    serializer_class = ConversationMessageSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer