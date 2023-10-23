from rest_framework import generics, status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .exceptions import UserNotFoundException
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from . import serializers
from rest_framework import generics
from .models import User


@authentication_classes([TokenAuthentication])
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


@authentication_classes([TokenAuthentication])
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return User.objects.get(user_id=user_id)


# CURD
@authentication_classes([TokenAuthentication])
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


@authentication_classes([TokenAuthentication])
class UserUpdate(generics.UpdateAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        try:
            user_id = self.kwargs['user_id']
            return User.objects.get(user_id=user_id)
        except UserNotFoundException:
            raise UserNotFoundException()


@authentication_classes([TokenAuthentication])
class UserDelete(generics.DestroyAPIView):
    serializer_class = serializers.UserSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            user_id = self.kwargs['user_id']
            user = User.objects.get(user_id=user_id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserNotFoundException:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UserCheck(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        return Response({'detail': True}, status=status.HTTP_200_OK)
