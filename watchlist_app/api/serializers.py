from watchlist_app.models import Movie
from rest_framework import serializers



class MovieSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    def update(self, instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
    # def validate_name(self, value):
    #     if len(value)<5 or len(value)>50:
    #         raise serializers.ValidationError('Name should be between 5 and 50 characters long.')
    #     return value
    
    # def validate_description(self, value):  
    #     if len(value)<10 or len(value)>1000:
    #         raise serializers.ValidationError('Description should be between 10 and 1000 characters long.')
    #     return value
    # def validate_active(self, value):
    #     if value not in [True,False]:
    #         raise serializers.ValidationError('Active should be either True or False.')
    #     return value
    # def validate_id(self, value):
    #     movie=Movie.objects.filter(id=value).first()
    #     if not movie:
    #         raise serializers.ValidationError('Movie with given id does not exist.')
    #     return value

       