from rest_framework import serializers
from ..models import Actor,Movie
from .review import ReviewListSerializer

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','overview',)


class MovieActorserializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    
    actors = MovieActorserializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'