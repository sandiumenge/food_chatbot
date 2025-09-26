from rest_framework.routers import DefaultRouter
from chat.api.views import CustomUserViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='user')
urlpatterns = router.urls