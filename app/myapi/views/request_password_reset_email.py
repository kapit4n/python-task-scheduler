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

from myapi.utils import Util

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


class RequestPasswordResetEmail(GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data['email']

        if UserModel.objects.filter(email=email).exists():
            user = UserModel.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token}
            )
            absurl = 'http://localhost:4200/reset-password-complete?url=http://' + \
                current_site + relativeLink
            email_body = 'Hello use this link below to reset your password \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to rest your password '}, status=status.HTTP_200_OK)

    class Meta:
      app_label = "myapi"
