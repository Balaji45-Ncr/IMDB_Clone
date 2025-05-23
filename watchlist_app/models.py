from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

# class Movie(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.CharField(max_length=200)
#     active=models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


class StreamingPlatform(models.Model):
    name=models.CharField(max_length=50)
    about= models.CharField(max_length=200)
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name




class WatchList(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    platform=models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE,related_name='watchlist',default=1)
    avg_rating_per_movie= models.FloatField(default=0)
    number_of_ratings_per_movie=models.IntegerField(default=0)
    total_avg_ratings=models.FloatField(default=0)
    total_ratings=models.IntegerField(default=0)
    def __str__(self):
        return self.title


class Review(models.Model):
    #
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    description=models.TextField(null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return f"{self.rating} stars review by {self.created.strftime('%Y-%m-%d')}"

