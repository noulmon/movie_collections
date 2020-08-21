from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.services import UserService, RequestCounterService

user_service = UserService()
request_counter_service = RequestCounterService()


class UserRegisterView(APIView):
    '''view for user registration'''
    permission_classes = [AllowAny]

    def post(self, request):
        return user_service.register(data=request.data)


class UserLoginView(APIView):
    '''view for user login'''
    permission_classes = [AllowAny]

    def post(self, request):
        return user_service.login(data=request.data)


class RequestCountView(APIView):
    '''view for retrieving request count on the server'''
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        return request_counter_service.get_count()


class RequestCountResetView(APIView):
    '''view for resetting request count on the server'''
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        return request_counter_service.reset()
