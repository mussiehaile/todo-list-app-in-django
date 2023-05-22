from django.urls import path
from accounts.views import register_user,get_accounts,get_user_detail,user_profile


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('list',get_accounts, name= 'get_accounts'),
    path('users/<int:user_id>/', get_user_detail, name='user-detail'),
     path('profile/', user_profile, name='user-profile')
]
