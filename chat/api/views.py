from rest_framework import viewsets
from chat.models import UserProfile
from chat.api.serializer import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer