from django.test import TestCase
from rest_framework.test import APIClient
from .models import DataSet
from datetime import timedelta, date

# Test class for Movie API functionality
class MovieAPITests(TestCase):    
    def setUp(self):
        # Initialize API client and create a sample movie for testing
        self.client = APIClient()
        DataSet.objects.create(
            id=1,
            title="Test Movie",
            original_title="Test Movie",
            original_language="en",
            overview="A test movie",
            popularity=50.0,
            release_date=date(2020, 1, 1),
            vote_average=7.5,
            vote_count=100
        )

    def get_results(self, response):
        if isinstance(response.data, list):
            return response.data
        return response.data.get('results', response.data)
    
    # Test the movie list endpoint
    def test_movie_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        movies = self.get_results(response)
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0]['title'], "Test Movie")

    # Test the popular movies endpoint
    def test_popular_movies(self):
        response = self.client.get('/api/movies/popular/')
        self.assertEqual(response.status_code, 200)
        movies = self.get_results(response)
        self.assertLessEqual(len(movies), 10)

    # Test the top-rated movies endpoint
    def test_top_rated_movies(self):
        response = self.client.get('/api/movies/top-rated/')
        self.assertEqual(response.status_code, 200)
        movies = self.get_results(response)
        self.assertTrue(all(movie['vote_average'] >= 8.0 for movie in movies))

    # Test the movies by language endpoint
    def test_movies_by_language(self):
        response = self.client.get('/api/movies/language/?lang=en')
        self.assertEqual(response.status_code, 200)
        movies = self.get_results(response)
        self.assertTrue(all(movie['original_language'] == 'en' for movie in movies))

    # Test the recent movies endpoint
    def test_recent_movies(self):
        response = self.client.get('/api/movies/recent/')
        self.assertEqual(response.status_code, 200)
        movies = self.get_results(response)
        cutoff_date = date.today() - timedelta(days=5*365)
        self.assertTrue(all(date.fromisoformat(movie['release_date']) >= cutoff_date for movie in movies))

    # Test the add movie endpoint
    def test_add_movie(self):
        data = {
            'title': 'New Movie',
            'original_title': 'New Movie',
            'original_language': 'fr',
            'overview': 'A new movie',
            'popularity': 60.0,
            'release_date': '2021-01-01',
            'vote_average': 8.0,
            'vote_count': 200
        }
        response = self.client.post('/api/movies/add/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'New Movie')