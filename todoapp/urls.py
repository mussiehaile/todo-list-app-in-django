"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from tasks.views import task_list,create_task,update_task,delete_task,register_user
from djoser import serializers as djoser_serialiser
from djoser.views import UserViewSet


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/tasks',task_list, name = 'task_list'),
    # path('api/tasks/create',create_task, name = 'create_task'),
    # path('api/tasks/<int:pk>',update_task, name='update_task'),
    # path('api/tasks/<int:pk>/delete', delete_task, name='delete_task'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('accounts.urls')),
]
