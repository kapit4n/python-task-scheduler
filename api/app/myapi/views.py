from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProjectSerializer

from .models import Task
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
