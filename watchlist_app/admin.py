from django.contrib import admin
from .models import StreamingPlatform,WatchList,Review
# Register your models here.
# from .models import Movie

admin.site.register(StreamingPlatform)
admin.site.register(WatchList)
admin.site.register(Review)