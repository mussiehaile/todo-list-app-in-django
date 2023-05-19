from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Tasks
# Create your views here.

@api_view(['GET'])
def task_list(request):
    tasks = Tasks.objects.all()
    serialiser = TaskSerializers(tasks, many =True)
    return Response(serialiser.data)