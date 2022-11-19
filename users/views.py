from django.contrib.auth import login
from django.core.exceptions import ValidationError
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer, UserSerializer


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        login(request, user)

        return super(LoginView, self).post(request, format=None)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # try:
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response({
            "user": UserSerializer(user).data,
            "token": token
        })
        # except ValidationError as e:
        #     return Response(data={e.code: [e.message]}, status=status.HTTP_400_BAD_REQUEST)
