from rest_framework import viewsets
from chat.models import UserProfile
from chat.api.serializer import UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from chat.services import parse_foods
import openai
import os

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):        
        raw_responses = serializer.validated_data.get('raw_responses', '')
        
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if not openai.api_key:
            raise RuntimeError("OPENAI_API_KEY not set in environment")
        
        foods, is_vegetarian = parse_foods(raw_responses)
        serializer.save(foods=foods, is_vegetarian=is_vegetarian)
        
    @action(detail=False, methods=['get'], url_path='vegetarians')
    def vegetarian_list(self, request):
        veg_qs = self.get_queryset().filter(is_vegetarian=True).order_by('created_at')
        serializer = self.get_serializer(veg_qs, many=True)
        return Response(serializer.data)