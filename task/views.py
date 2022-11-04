from .models import TaskData
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class TaskList(APIView):

    def get(self, request, *args, **kwargs):
        task_instance = TaskData.objects.filter(user=request.user.id)
        task_serializer = TaskSerializer(task_instance, many=True)
        
        return Response(task_serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
     
        task_serializer = TaskSerializer(data=request.data)
        task_serializer.is_valid(raise_exception=True)
        task_serializer.save(user=request.user)

        return Response(task_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        task_instance = TaskData.objects.get(id=id)
        task_serializer = TaskSerializer(task_instance, data=request.data)
        task_serializer.is_valid(raise_exception=True)
        task_serializer.save(user=request.user)
        
        return Response(task_serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        task_instance = TaskData.objects.get(id=id)
        task_instance.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    
    

