from django.shortcuts import render,get_list_or_404,get_object_or_404
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_details(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data,status=status.HTTP_200_OK)