from rest_framework import viewsets
from chat.models import CustomUser
from chat.api.serializer import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer