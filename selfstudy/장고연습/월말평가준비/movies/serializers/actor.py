
from rest_framework import serializers
from ..models import Actor,Movie

class ActorListserializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class ActorMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = ActorMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'
