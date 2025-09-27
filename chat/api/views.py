from rest_framework import viewsets
from chat.models import UserProfile
from chat.api.serializer import UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=['get'], url_path='vegetarians')
    def vegetarian_list(self, request):
        veg_qs = self.get_queryset().filter(is_vegetarian=True).order_by('-created_at')
        serializer = self.get_serializer(veg_qs, many=True)
        return Response(serializer.data)