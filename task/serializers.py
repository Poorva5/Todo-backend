from rest_framework import serializers
from .models import TaskData

class TaskSerializer(serializers.ModelSerializer):

    user = serializers.CharField(required=False)
    class Meta:   
        model = TaskData
        fields = ["title", "completed", "user"]
