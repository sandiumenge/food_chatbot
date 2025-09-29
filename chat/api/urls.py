from rest_framework.routers import DefaultRouter
from chat.api.views import UserProfileViewSet
from django.urls import path
from chat.api import views

router = DefaultRouter()
router.register('users', UserProfileViewSet, basename='user')

urlpatterns = router.urls
urlpatterns = router.urls + [
    path('health/', views.health, name='health'),
]