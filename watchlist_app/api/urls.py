
from django.urls import path
from . import views  # or import the exact views you need

urlpatterns = [
    #path('', views.home, name='home'),  # Replace `home` with your actual view name
    path('',views.Movie_List.as_view(),name='movie_list'),
    path('movie/<int:pk>', views.Movie_Details.as_view(), name='movie_detail'),
]
