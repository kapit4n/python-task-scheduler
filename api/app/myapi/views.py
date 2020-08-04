from .models import Task
from .serializers import TaskSerializer, UserSerializerWithToken, UserSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token


from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError

from django.contrib.sites.shortcuts import get_current_site

from .utils import Util

from rest_framework.response import Response
from django.urls import reverse

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your views here.

logger = logging.getLogger(__name__)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

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


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserList(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserInfo(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, email=self.request.user)
        return obj


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


class SetNewPasswordAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
