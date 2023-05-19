from django.urls import path
from accounts.views import register_user,get_accounts

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('list',get_accounts, name= 'get_accounts')
]
