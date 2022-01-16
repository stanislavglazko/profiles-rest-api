from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradition Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
