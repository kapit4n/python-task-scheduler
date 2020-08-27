# serializers.py
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from rest_framework import serializers

from .models import Task, TaskLog

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()


class TaskSerializer(serializers.ModelSerializer):

    logs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        fields = ('id', 'description', 'status',
                  'priority', 'time', 'estimated_time', 'logs')


class TaskLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskLog
        fields = ('id', 'status', 'task', 'start_date', 'end_date')


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']


class UserSerializerWithToken(serializers.ModelSerializer):
    pass


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # validated_data['username']
        user = UserModel.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'first_name', 'last_name',)


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
