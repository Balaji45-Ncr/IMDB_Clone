from django.shortcuts import render,get_list_or_404,get_object_or_404
from watchlist_app.models import WatchList,StreamingPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamingPlatformSerializer,ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from watchlist_app.api.permissions import AdminOrReadOnly,ReviewOwnerOrReadOnly
from django.db.models import Avg
# @api_view(['GET','POST'])
# def movie_list(request):
    # movies=Movie.objects.all()
    # if request.method=='POST':
    #     serializer=MovieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # serializer=MovieSerializer(movies,many=True)
    # return Response(serializer.data,status=status.HTTP_200_OK)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
    # movie=Movie.objects.get(pk=pk)
    # if request.method=='PUT':
    #     serializer=MovieSerializer(movie,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # elif request.method=='DELETE':
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    # serializer=MovieSerializer(movie)
    # return Response(serializer.data,status=status.HTTP_200_OK)

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#      queryset = Review.objects.all()
#      serializer_class = ReviewSerializer

#      def get(self,request,*args,**kwargs):
#           return self.list(request,*args,**kwargs)
     
#      def post(self,request,*args,**kwargs):
#           return self.create(request,*args,**kwargs)
     
class ReviewDetailAV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer

     def get(self,request,pk,*args,**kwargs):
          return self.retrieve(request,pk,*args,**kwargs)
     def put(self,request,pk,*args,**kwargs):   
          return self.update(request,pk,*args,**kwargs)
     def delete(self,request,pk,*args,**kwargs):
          return self.destroy(request,pk,*args,**kwargs)
     
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset=Review.objects.all()
     serializer_class = ReviewSerializer
     lookup_field='pk'
     permission_classes=[ReviewOwnerOrReadOnly]

class ReviewListAV(generics.ListCreateAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer

class WatchListAV(APIView):
    def get(self,request,*args,**kwargs):
        movie=WatchList.objects.all()
        serializer=WatchListSerializer(movie,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class WatchDetailAV(APIView):
    def get(self,request,pk,*args,**kwargs):
        movie=get_object_or_404(WatchList,pk=pk)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk,*args,**kwargs):
        movie=get_object_or_404(WatchList,pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,*args,**kwargs):
        movie=get_object_or_404(WatchList,pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def get_queryset(self):
    #     return Movie.objects.all()

    # def get_object(self, pk):

    #     return get_object_or_404(Movie, pk=pk)
    # def perform_create(self, serializer):
    #     serializer.save()
    # def perform_update(self, serializer):
    #     serializer.save()
    # def perform_destroy(self, instance):
    #     instance.delete()
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return MovieSerializer
    #     else:
    #         return MovieSerializer_Create
    # def get_serializer_context(self):
    #     return {'request': self.request}
    # def filter_queryset(self, queryset):
    #     search_query = self.request.query_params.get('search', None)
    #     if search_query is not None:
    #         queryset = queryset.filter(title__icontains=search_query)
    #     return queryset
    # def get_paginated_response(self, data):
    #     page = self.paginate_queryset(data)
    #     serializer = self.get_serializer(page, many=True) 
    #     return self.get_paginated_response_with_serializer(serializer)
    # def get_paginated_response_with_serializer(self, serializer):

    #     return Response(serializer.data,
    #                     pagination_info=self.get_paginated_info(page),
    #                     status=status.HTTP_200_OK)

    #     def get_paginated_info(self, page):
    #         return {
    #             'current_page': page.number,
    #             'total_pages': page.paginator.num_pages,
    #             'total_results': page.paginator.count,
    #         }

    #     def get_permissions(self):
    #         if self.request.method in ['POST', 'PUT', 'DELETE']:
    #             return [IsAuthenticated()]
    #         return []
    #     def get_queryset(self):
    #         queryset = Movie.objects.all()
    #         return queryset
    #     def get_object(self, pk):
    #         return get_object_or_404(Movie, pk=pk)
    #     def perform_create(self, serializer):
    #         serializer.save()
    #     def perform_update(self, serializer):
    #         serializer.save()
    #     def perform_destroy(self, instance):
    #         instance.delete()
    #     def get_serializer_class(self):
    #         if self.request.method == 'GET':
    #             return MovieSerializer
    #         else:
    #             return MovieSerializer_Create
    #     def get_serializer_context(self):
    #         return {'request': self.request}
    #     def filter_queryset(self, queryset):
    #         search_query = self.request.query_params.get('search', None)
    #         if search_query is not None:
    #             queryset = queryset.filter(title__icontains=search_query)
    #         return queryset
    #     def get_paginated_response(self, data):
    #         page = self.paginate_queryset(data)
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response_with_serializer(serializer)
    #     def get_paginated_response_with_serializer(self, serializer):
    #         return Response(serializer.data,
    #                         pagination_info=self.get_paginated_info(page),
    #                         status=status.HTTP_200_OK)
    #     def get_paginated_info(self, page):
    #         return {
    #             'current_page': page.number,
    #             'total_pages': page.paginator.num_pages,
    #             'total_results': page.paginator.count,
    #         }
    #     def get_permissions(self):
    #         if self.request.method in ['POST', 'PUT', 'DELETE']:
    #             return [IsAuthenticated()]
    #         return []

    #     def get_queryset(self):
    #         queryset = Movie.objects.all()
    #         return queryset
    #     def get_object(self, pk):
    #         return get_object_or_404(Movie, pk=pk)
    #     def perform_create(self, serializer):
    #         serializer.save()
    #     def perform_update(self, serializer):
    #         serializer.save()
    #     def perform_destroy(self, instance):
    #         instance.delete()
    #     def get_serializer_class(self):
    #         if self.request.method == 'GET':
    #             return MovieSerializer
    #         else:
    #             return MovieSerializer_Create
    #     def get_serializer_context(self):
    #         return {'request': self.request}
    #     def filter_queryset(self, queryset):
    #         search_query = self.request.query_params.get('search', None)
    #         if search_query is not None:
    #             queryset = queryset.filter(title__icontains=search_query)
    #         return queryset
    #     def get_paginated_response(self, data):
    #         page = self.paginate_queryset(data)
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response_with_serializer(serializer)
    #     def get_paginated_response_with_serializer(self, serializer):
    #         return Response(serializer.data,
    #                         pagination_info=self.get_paginated_info(page),
    #                         status=status.HTTP_200_OK)
    #     def get_paginated_info(self, page):
    #         return { 
    #             'current_page': page.number,
    #             'total_pages': page.paginator.num_pages,
    #             'total_results': page.paginator.count,
    #         }
    #     def get_permissions(self):
    #         if self.request.method in ['POST', 'PUT', 'DELETE']:
    #             return [IsAuthenticated()]
    #         return []
    #     def get_queryset(self):
    #         queryset = Movie.objects.all()
    #         return queryset
    #     def get_object(self, pk):
    #         return get_object_or_404(Movie, pk=pk)
    #     def perform_create(self, serializer):
    #         serializer.save()
    #     def perform_update(self, serializer):
    #         serializer.save()
    #     def perform_destroy(self, instance):
    #         instance.delete()
    #     def get_serializer_class(self):
    #         if self.request.method == 'GET':
    #             return MovieSerializer
    #         else:
    #             return MovieSerializer_Create
    #     def get_serializer_context(self):
    #         return {'request': self.request}
    #     def filter_queryset(self, queryset):

class StreamingListAV(APIView):
        def get(self, request, *args, **kwargs):
            streamings=StreamingPlatform.objects.all()
            serializer=StreamingPlatformSerializer(streamings,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        def post(self, request, *args, **kwargs):
            serializer=StreamingPlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StreamingDetailAV(APIView):
    def get_object(self, pk):   
        try:
            return StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, *args, **kwargs):
            streaming=self.get_object(pk)
            serializer=StreamingPlatformSerializer(streaming)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request, pk, *args, **kwargs):
            streaming=self.get_object(pk)
            serializer=StreamingPlatformSerializer(streaming,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, *args, **kwargs):
            streaming=self.get_object(pk)
            streaming.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReviewListAVI(generics.ListCreateAPIView):
     queryset=Review.objects.all()
     serializer_class=ReviewSerializer

class ReviewList(generics.ListAPIView):
     serializer_class=ReviewSerializer
     permission_classes=[AdminOrReadOnly]
     #permi=[AdminOrReadOnly]
     def get_queryset(self):
          pk=self.kwargs.get('pk')
          return Review.objects.filter(watchlist=pk)
          
class ReviewCreate(generics.CreateAPIView):
     serializer_class=ReviewSerializer
     permission_classes=[AdminOrReadOnly]

     def get_queryset(self):
          return Review.objects.filter(review_user=self.request.user)

     def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        overall_movie = WatchList.objects.all()
        user = self.request.user

        # Check if user already reviewed this movie
        review_queryset = Review.objects.filter(review_user=user, watchlist=movie)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        # Update movie's average rating
        if movie.number_of_ratings_per_movie == 0:
            movie.avg_rating_per_movie = serializer.validated_data['rating']
        else:
            movie.avg_rating_per_movie = (
                movie.avg_rating_per_movie + serializer.validated_data['rating']
            ) / 2

        movie.number_of_ratings_per_movie += 1
        movie.save()

        serializer.save(watchlist=movie, review_user=user)

        # Calculate total review count and average
        reviews_count = Review.objects.count()
        print(f'total reviews are :--->{reviews_count}')
        total_avg_ratings = Review.objects.aggregate(avg=Avg('rating'))['avg']
        print(f'avg_of all ratings:{total_avg_ratings}')

        # Handle None case
        if total_avg_ratings is None:
            total_avg_ratings = 0

        # Update all movies (this might not be necessary unless you have a reason)


        overall_movie.update(
            total_avg_ratings=total_avg_ratings,
            total_ratings=reviews_count
        )
