import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response


def fetch_movie_list(page):
    try:
        fetched = False
        attempt = 0
        # third party url
        api_url = 'https://demo.credy.in/api/v1/maya/movies/'
        # checking for page number
        if page is not None:
            api_url += f'?page={page}'
        # checking whether the retry attempt is success or not
        while not fetched:
            attempt += 1
            print(attempt)
            # api response
            response = requests.get(api_url, auth=HTTPBasicAuth(settings.MOVIE_LIST_API_CLIENT_ID,
                                                                settings.MOVIE_LIST_API_CLIENT_SECRET))

            if response.status_code is 200:
                # setting the attempt is success
                fetched = True
                return Response(response.json())
    except requests.exceptions.ConnectionError:
        return Response({
            'error': 'Please connect to the internet.'
        })
