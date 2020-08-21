# MOVIE COLLECTIONS: CREDY

### Introduction:
_**MOVIE COLLECTIONS**_ is a collection creating application where the user can register/sign in with the application and get list of movies. Once user is successfully authenticated, receives a JWT Token. User can create multiple collections of movies with a title and description. Also, user can perform CRUD operations on the collections.


### Follow the steps to _run the application_:

1. Install all the required packages(python modules):

    ```pip install -r requirements.txt```

2. Migrate all the models to the database(Assuming that the DB is sqlite as of now)
 
    ```python manage.py migrate```
    
3. When the migrations are successfully completed, we can run the server:

    ```python manage.py runserver```
    
    If the steps are followed correctly, the server will be up and running.
 
 4. To gather all static files(not necessary as the system does not serve any static file):
   
    ```python manage.py collectstatic```

## API Endpoints:

#### User APIs:
##### 1. User Registration: ```<base_url>/user/register/``` [POST]

   Request Payload:
   
    {
        "username": <desired username>,
        "password": <desired username>,
    }
    
   Response:
   
    {
       "access_token": <access_token>
    }

##### 2. User Login: ```<base_url>/user/login/``` [POST]

   Request Payload:
   
    {
        "username": <desired username>,
        "password": <desired username>,
    }
    
   Response:
   
    {
       "access_token": <access_token>
    }
_____

**_`Note: Please add the 'user token' as the 'Authorization Header' for all below APIs`_**)


example:
    
    Authorization: 'Token <jwt_token>

#### Movie APIs:
##### 1. Movie list: ```<base_url>/movies/list/``` [GET]
 
   Response:
   
    {
    “count”: <total number of movies>,
    “next”: <link for next page, if present>,
    “previous”: <link for previous page>,
    “data”: [
        {
        “title”: <title of the movie>,
        “description”: <a description of the movie>,
        “genres”: <a comma separated list of genres, if
        present>,
        “uuid”: <a unique uuid for the movie>
        },
    ...
        ]
    }
   
##### 2. Create collection: ```<base_url>/movies/collection/``` [POST]

   Request Payload:
   
    {
    "title": <desired_title>,
    "description": <description>,
    "movies": [
        <movie_uuid_1>,
        <movie_uuid_2>,
        <movie_uuid_3>,
        ...
        ]
    }
    
   Response:
   
    {
       "collection_uuid": <uuid of the collection item>
    }

##### 3. Get collection list: ```<base_url>/movies/collection/``` [GET]

   Response:
   
    {
        'is_success': True,
        'data': {
            'collections': [
            "title": <desired_title>,
            "description": <description>,
            "movies": [
                <movie_uuid_1>,
                <movie_uuid_2>,
                <movie_uuid_3>,
                ...
                    ]
                ...
                ]
            }
        }
    
##### 4. Retrieve collection details ```<base_url>/movies/collection/<collection_uuid>``` [GET]
   Response:
   
    {
    "title": <desired_title>,
    "description": <description>,
    "movies": [
        <movie_uuid_1>,
        <movie_uuid_2>,
        <movie_uuid_3>,
        ...
        ]
    }
   
##### 5. Update collection details ```<base_url>/movies/collection/<collection_uuid>``` [PUT]
   Request Payload:
   
       {
        "title": <Updated title>,
        "description": <updated description>,
        "movies": [
            <optional updated movie list>
            ]
        }
        
   Response:
   
        {
        "collection_uuid": <collection_uuid>
        }
        
##### 6. Delete collection details ```<base_url>/movies/collection/<collection_uuid>``` [DELETE]
   Response:
   
        {
            'message': 'movie collection deleted successfully.'
        }

#### Request Counter APIs:
##### 1. Get request count ```<base_url>/request-count/``` [GET]
   Response:
   
       {
        "requests": <request_count>
       }

##### 2. Reset request count ```<base_url>/request-count/reset/``` [POST]
   Response:
   
       {
        "message": "request count reset successfully"
       }

