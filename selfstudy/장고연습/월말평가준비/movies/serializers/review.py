from rest_framework import serializers
from ..models import Review,Movie

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)


class RevieMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)


class ReviewSerializer(serializers.ModelSerializer):

    movie = RevieMovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)