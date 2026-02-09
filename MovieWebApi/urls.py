from django.urls import path
from .views import  *

# Define routes for movie-related API endpoints
urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/popular/', PopularMoviesView.as_view(), name='popular-movies'),
    path('movies/top-rated/', TopRatedMoviesView.as_view(), name='top-rated-movies'),
    path('movies/language/', MoviesByLanguageView.as_view(), name='movies-by-language'),
    path('movies/recent/', RecentMoviesView.as_view(), name='recent-movies'),
    path('movies/add/', AddMovieView.as_view(), name='add-movie'),
]