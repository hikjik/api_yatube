from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet

router = SimpleRouter()
router.register(r'v1/groups', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
