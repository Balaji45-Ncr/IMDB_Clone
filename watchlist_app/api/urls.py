
from django.urls import path
from . import views  # or import the exact views you need

urlpatterns = [
    #path('', views.home, name='home'),  # Replace `home` with your actual view name
    path('',views.movie_list,name='movie_list'),
    path('movie/<int:pk>', views.movie_details, name='movie_detail'),
]
