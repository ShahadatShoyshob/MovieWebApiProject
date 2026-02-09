from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import DataSet
from .serializers import MovieSerializer
from django.db.models import Q
from datetime import datetime, timedelta

# Custom pagination class to set page size to 1000
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 500

# View to list all movies in the database
class MovieListView(APIView):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        movies = DataSet.objects.all().order_by('-created_at')
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

# View to retrieve the top 10 most popular movies
class PopularMoviesView(APIView):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        movies = DataSet.objects.order_by('-popularity', '-created_at')[:10]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# View to fetch movies with a vote average of 8.0 or higher
class TopRatedMoviesView(APIView):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        movies = DataSet.objects.filter(vote_average__gte=8.0).order_by('-vote_average', '-created_at')
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

# View to filter movies by their original language
class MoviesByLanguageView(APIView):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        language = request.query_params.get('lang', 'en')
        movies = DataSet.objects.filter(original_language=language).order_by('-created_at')
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

# View to list movies released within the last 5 years
class RecentMoviesView(APIView):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        five_years_ago = datetime.now().date() - timedelta(days=5*365)
        movies = DataSet.objects.filter(release_date__gte=five_years_ago).order_by('-created_at')
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

# View to add a new movie to the database
class AddMovieView(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)