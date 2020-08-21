from rest_framework.response import Response

from movie.models import UserMovieCollection
from movie.serializers import MovieCollectionSerializer
from movie.utils import fetch_movie_list


class MovieService:
    def movie_list(self, page):
        ''' Third party movie list API '''
        response = fetch_movie_list(page)
        return response

    def create(self, request):
        ''' Create new movie collection '''
        serializer = MovieCollectionSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'collection_uuid': serializer.data['uuid']
            })
        # returning validation errors
        return Response({
            'error': serializer.errors
        })

    def list(self, request):
        # fetching movie collection list for the user
        queryset = UserMovieCollection.objects.prefetch_related('collection_movies').filter(user=request.user,
                                                                                            is_delete=False,
                                                                                            is_active=True)
        serializer = MovieCollectionSerializer(queryset, many=True)
        return Response({
            'is_success': True,
            'data': {
                'collections': serializer.data
            }
        })

    def retrieve(self, instance):

        # retrieving movie collection details
        serializer = MovieCollectionSerializer(instance)
        return Response({
            'collections': serializer.data
        })

    def update(self, request, instance):

        # updating movie collection data
        serializer = MovieCollectionSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'collection_uuid': serializer.data['uuid']
            })
        return Response({
            'error': serializer.errors
        })

    def delete(self, instance):

        # deactivating collection
        instance.is_active = False
        # deleting collection
        instance.is_delete = True
        instance.save()
        return Response({
            'message': 'movie collection deleted successfully.'
        })
