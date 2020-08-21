from django.utils.deprecation import MiddlewareMixin

from user.models import RequestCount


class RequestCounterMiddleware(MiddlewareMixin):
    '''middleware for counting the number of requests hit the server'''

    def process_request(self, request):
        # getting the request counter
        request_count = RequestCount.objects.first()
        if request_count is None:
            # creating new request count if no count data is available
            count = RequestCount.objects.create(count=1)
            return None
        else:
            # incrementing count by one per request
            request_count.count += 1
            request_count.save()
            return None
