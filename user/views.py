from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView


from . import serializers
from .permissions import IsAccountOwnerOrReadOnly
from .send_mail import send_confirmation_email

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = serializers.RegisterApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user)
            # TODO add send email logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Successfully activated'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer


class CustomLogoutView(LogoutView):
    """
    Endpoint for logout from account
    """
    permission_classes = (permissions.IsAuthenticated,)
    

class UserListView(generics.ListAPIView):
    """
    Endpoint for retrieve all users
    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Endpoint for detail 1 user
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    """
    Endpoint for update account
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAccountOwnerOrReadOnly, )


class UserDestroyView(generics.DestroyAPIView):
    """
    Endpoint for delete user
    """
    permission_classes = (IsAccountOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
