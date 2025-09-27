from rest_framework import viewsets
from chat.models import Conversation, ConversationMessage, UserProfile
from chat.api.serializer import ConversationSerializer, ConversationMessageSerializer, UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        conversation = self.get_object()
        messages = conversation.messages.all()
        serializer = ConversationMessageSerializer(messages, many=True)
        return Response(serializer.data)

class ConversationMessageViewSet(viewsets.ModelViewSet):
    queryset = ConversationMessage.objects.all()
    serializer_class = ConversationMessageSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer