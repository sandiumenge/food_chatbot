from rest_framework.routers import DefaultRouter
from chat.api.views import ConversationViewSet, ConversationMessageViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('conversations', ConversationViewSet, basename='conversation')
router.register('messages', ConversationMessageViewSet, basename='message')
router.register('users', UserProfileViewSet, basename='user')

urlpatterns = router.urls