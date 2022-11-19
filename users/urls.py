from django.urls import include, path
from rest_framework import routers

from users.views import LoginView, RegisterView
#
# router = routers.DefaultRouter()
#
# router.register(r'register', RegisterView.as_view, basename='register')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
