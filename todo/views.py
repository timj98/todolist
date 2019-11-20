from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from .models import Todo
from .serializers import TodoListSerializer
from .permissions import IsOwnerOrReadOnly

class TodoListViewSet(viewsets.ModelViewSet):
    """
    Viewset for model todo that will create CRUD in the most efficient manner
    """
    #queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Todo.objects.filter(owner=self.request.user)
        return queryset