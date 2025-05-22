from django.contrib import auth
from django.urls import path,re_path,include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/',obtain_auth_token,name='login')
]
