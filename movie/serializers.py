from django.db import transaction
from rest_framework import serializers

from movie.models import UserMovieCollection, CollectedMovie


class MovieCollectionSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    movies = serializers.ListField(required=True)

    @transaction.atomic()
    def create(self, validated_data):
        # requested user
        user = self.context.get('user')
        # creating user movie collection
        collection = UserMovieCollection.objects.create(user=user, title=validated_data['title'],
                                                        description=validated_data['description'])

        collection_movies = [
            CollectedMovie(collection=collection, movie_uuid=movie) for movie in validated_data['movies']
        ]

        # creating user collected movies
        CollectedMovie.objects.bulk_create(collection_movies)

        return collection

    @transaction.atomic()
    def update(self, instance, validated_data):
        # optional movie list
        movies = validated_data.pop('movies')
        # updating movie collection
        UserMovieCollection.objects.filter(pk=instance.pk).update(**validated_data)

        # checking whether movie list is empty or not
        if len(movies) > 0:
            # updating movie list if the payload is not empty
            CollectedMovie.objects.filter(collection=instance).delete()
            collection_movies = [
                CollectedMovie(collection=instance, movie_uuid=movie) for movie in movies
            ]

            CollectedMovie.objects.bulk_create(collection_movies)

        return instance

    def to_representation(self, instance):
        def get_movies():
            # movies in the collection list
            return [movie for movie in instance.collection_movies.values_list('movie_uuid', flat=True)]

        return {
            'title': instance.title,
            'uuid': instance.uuid,
            'description': instance.description,
            'movies': get_movies()
        }
