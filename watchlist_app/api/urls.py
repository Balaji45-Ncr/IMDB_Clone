
from django.urls import path
from . import views  # or import the exact views you need

urlpatterns = [
    #path('', views.home, name='home'),  # Replace `home` with your actual view name
    path('',views.WatchListAV.as_view(),name='movie_list'),
    path('movie/<int:pk>', views.WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/',views.StreamingListAV.as_view(), name='streaming_list'),
    path('stream/<int:pk>/', views.StreamingDetailAV.as_view(), name='streaming_detail'),
]
