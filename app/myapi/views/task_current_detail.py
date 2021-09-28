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


class TaskCurrentDetail(APIView):
    serializer_class = TaskSerializer

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        currentTask = self.get_object(pk)
        serializer = TaskSerializer(currentTask)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # then save status
        currentTask = self.get_object(pk)
        print(currentTask.status == 'progress')
        curserializer = TaskSerializer(currentTask, data=request.data)

        if request.data['status'] == 'progress':
            queryset2 = Task.objects.filter(status='progress')
            for item in queryset2:
                if item.pk is not pk:
                    print('item')
                    print(item)
                    item.status = 'pending'
                    item.save()

        if curserializer.is_valid():
            curserializer.save()
            return Response(curserializer.data)
        return Response(curserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Meta:
      app_label = "myapi"

