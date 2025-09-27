from rest_framework.routers import DefaultRouter
from chat.api.views import UserProfileViewSet

router = DefaultRouter()
router.register('users', UserProfileViewSet, basename='user')
urlpatterns = router.urls