
from rest_framework import viewsets
from django.db.models import Q
# Create your views here.

from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    
    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.query_params.get('q')

        if query:
            # Perform case-insensitive search on title and director fields
            queryset = queryset.filter(
                Q(title__icontains=query)  
            )

        return queryset
