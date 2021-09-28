from myapi.models import Task, TaskLog
from myapi.serializers import TaskSerializer, TaskLogSerializer, UserSerializerWithToken, UserSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
import logging

from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from rest_framework.viewsets import ModelViewSet

from rest_framework.authtoken.models import Token

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError

from django.contrib.sites.shortcuts import get_current_site

from rest_framework.response import Response
from django.urls import reverse

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from django.http import Http404
from django_filters import rest_framework as filters

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

UserModel = get_user_model()

# Create your views here.

logger = logging.getLogger(__name__)


class PasswordTokenCheckAPI(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token invalid'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as indentifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)

    class Meta:
      app_label = "myapi"
