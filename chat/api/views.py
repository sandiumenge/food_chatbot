from rest_framework import viewsets
from chat.models import UserProfile
from chat.api.serializer import UserProfileSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from chat.services import parse_foods
from django.http import JsonResponse
import openai
import os

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # The instructions are a bit ambiguous about authentication,
    # and although it only specifically asks for authentication
    # for 'vegetarian_list' I will also block the actions that allow
    # modifying the db for security (for if someone stumbles on the API).
    def get_permissions(self):
        if self.action in ['vegetarian_list', 'create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

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
        data = [
            {
                'username': user.username,
                'foods': user.foods
            }
            for user in veg_qs
        ]    
        return Response(data)

def health(request):
    return JsonResponse({"status": "ok"})