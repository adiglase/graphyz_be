from django.urls import path
from rest_framework import routers

from users.views import LoginView, RegisterView, UserView

router = routers.DefaultRouter()
router.register(r'user', UserView, basename='user')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
urlpatterns += router.urls
