from django.shortcuts import render
from rest_framework import viewsets, generics

from .serializers import TaskSerializer, ResetPasswordEmailRequestSerializer

from .models import Task
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

class RequestPasswordResetView(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)