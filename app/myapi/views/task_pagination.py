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


class TaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_params = 'page_size'

    class Meta:
      app_label = "myapi"

