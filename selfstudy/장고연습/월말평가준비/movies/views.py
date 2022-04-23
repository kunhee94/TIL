from django.shortcuts import render,get_object_or_404
from .models import Actor,Movie,Review
from .serializers.actor import ActorListserializer,ActorSerializer
from .serializers.movie import MovieListSerializer,MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view()
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListserializer(actors, many=True)
    return Response(serializer.data)


@api_view()
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor,pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

    
@api_view()
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view()
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'review {review_pk} is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review,request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)