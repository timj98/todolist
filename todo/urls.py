from django.urls import include, path
from rest_framework import routers
from todo import views
from .models import Todo

app_name = 'todo'

router = routers.DefaultRouter()
router.register('todo', views.TodoListViewSet, basename=Todo)

urlpatterns = [
    path('', include(router.urls)),
]