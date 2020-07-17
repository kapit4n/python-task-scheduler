from .models import Task
from .serializers import TaskSerializer, UserSerializer, ResetPasswordEmailRequestSerializer
from django.shortcuts import render
from rest_framework import viewsets, generics, status

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_bytes

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


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class RequestPasswordResetEmail(generics.GenericAPIView):
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
            absurl = 'http://' + current_site + relativeLink
            email_body = 'Hello use this link below to reset your password \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to rest your password '}, status=status.HTTP_200_OK)


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
