# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import TaskSerializers
# from .models import Tasks
# from djoser.views import UserViewSet as DjoserUserViewSet
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# # Create your views here.

# @api_view(['GET'])
# def task_list(request):
#     tasks = Tasks.objects.all()
#     serialiser = TaskSerializers(tasks, many =True)
#     return Response(serialiser.data)


# @api_view(['POST'])
# def create_task(request):
#     serialiser = TaskSerializers(data =request.data)
#     if serialiser.is_valid():
#         serialiser.save()
#         return Response(serialiser.data,status =201)
#     return Response(serialiser.errors,status=400)


# @api_view(['PATCH'])
# def update_task(request,pk):
#     try:
#         task = Tasks.objects.get(pk =pk)
#     except Tasks.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
   
#     serialiser = TaskSerializers(task, data =request.data, partial =True)
#     if serialiser.is_valid():
        
#         serialiser.save()
#         return Response(serialiser.data,status =201)
#     return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
               

# @api_view(['DELETE'])             
# def delete_task(request,pk):
#     try:
#         task = Tasks.objects.get(pk =pk)
#     except Tasks.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
   
#     task.delete()
    # return Response(status=status.HTTP_404_NOT_FOUND)
    
  
    
