from rest_framework.viewsets import ModelViewSet

from .models import Task
from .serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
