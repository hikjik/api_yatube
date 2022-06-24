from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
]
