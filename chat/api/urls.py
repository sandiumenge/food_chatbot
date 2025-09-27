from rest_framework.routers import DefaultRouter
from chat.api.views import ConversationViewSet, ConversationMessageViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('users', ConversationViewSet, basename='user')
router.register('messages', ConversationMessageViewSet, basename='message')
router.register('profiles', UserProfileViewSet, basename='profile')

urlpatterns = router.urls