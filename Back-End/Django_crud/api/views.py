from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieTitleSerializer(movies, many=True)
        return Response(serializer.data)
