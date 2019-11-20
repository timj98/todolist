from .models import *
from rest_framework import serializers

class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = '__all__'