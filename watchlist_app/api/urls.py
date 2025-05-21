
from django.urls import path
from . import views  # or import the exact views you need

urlpatterns = [
    #path('', views.home, name='home'),  # Replace `home` with your actual view name
    path('',views.WatchListAV.as_view(),name='movie_list'),
    path('movie/<int:pk>', views.WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/',views.StreamingListAV.as_view(), name='streaming_list'),
    path('stream/<int:pk>/', views.StreamingDetailAV.as_view(), name='streaming_detail'),
    # path('reviews/',views.ReviewListAV.as_view(), name='review_list'),
    path('stream/review/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

    #we want to create the url to show the review for a specific movie
    path('stream/<int:pk>/review/',views.ReviewList.as_view(),name='review-list'),
    path('stream/<int:pk>/review-create/',views.ReviewCreate.as_view(),name='review-create')

]
