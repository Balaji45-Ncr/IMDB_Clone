from watchlist_app.models import WatchList,StreamingPlatform,Review
from rest_framework import serializers
class ReviewSerializer(serializers.ModelSerializer):
     review_user=serializers.StringRelatedField(read_only=True)
     class Meta:    
          model=Review
          #fields='__all__'
          exclude=('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
   # len_name=serializers.SerializerMethodField()
    reviews=ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'
#         read_only_fields = ('id',)  
#         # depth=1  # to include related fields in response
#         # validators=[validate_name,validate_description]   # to add validation rules on fields
#         # error_messages={'name': {'required': 'Name field is required.'},}   # to customize error messages
#         # extra_kwargs={'name': {'help_text': 'Name of the movie'},'description': {'help_text': 'Description of the movie'}}   # to add help text to fields
#         # validators=[validate_name,validate_description]   # to add validation rules on fields 
#     def get_len_name(self, obj):
#         return len(obj.name)
 

# # class MovieSerializer(serializers.Serializer):
# #     id =serializers.IntegerField(read_only=True)
# #     name=serializers.CharField()
# #     description=serializers.CharField()
# #     active=serializers.BooleanField()

# #     def create(self, validated_data):
# #         return Movie.objects.create(**validated_data)
# #     def update(self, instance,validated_data):
# #         instance.name=validated_data.get('name',instance.name)
# #         instance.description=validated_data.get('description',instance.description)
# #         instance.active=validated_data.get('active',instance.active)
# #         instance.save()
# #         return instance
    
# #     def validate_name(self,value):
# #         if len(value)<5 :
# #             raise serializers.ValidationError('Name should be at least 5 characters long')  
# #         return value
# #     def validate_description(self,value):
# #         if len(value)<10 :
# #             raise serializers.ValidationError('Description should be at least 10 characters long')  
# #         return value
# #     def validate(self, data):
# #         if data['name'] ==data['description']:
# #             raise serializers.ValidationError('Name and Description should not be same')    
# #         return data
# #     def validate_active(self, value):   
# #         if value not in [True,False]:
# #             raise serializers.ValidationError('Active should be either True or False')  
# #         return value    
   
class StreamingPlatformSerializer(serializers.ModelSerializer):
        watchlist=WatchListSerializer(many=True,read_only=True)
        #watchlist= serializers.StringRelatedField(many=True)
        #watchlist=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #     watchlist=serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie_detail'
    # )
        class Meta:
           model=StreamingPlatform
           fields='__all__'
