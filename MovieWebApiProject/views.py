from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings

# Define the homepage view for the Movie API
def home(request):
    domain = request.get_host() 
    scheme = 'http'
    base_url = f"{scheme}://{domain}"

    html = f"""
    <html>
        <body>
            <h1>Movie API</h1>
            <p>Python version: 3.11</p>
            <p>Django version: 5.0.6</p>
            <p>Packages used: Django 5.0.6, djangorestframework 3.15.1, pandas 2.2.2</p>
            <p>Admin site: <a href="{base_url}/admin/">{base_url}/admin/</a> (username: admin, password: admin123)</p>
            <h2>API Endpoints</h2>
            <ul>
                <li>GET <a href="{base_url}/api/movies/">List all movies</a> - Retrieves a list of all movies in the database. <a href="{base_url}/api/movies/">{base_url}/api/movies/</a></li>
                <li>GET <a href="{base_url}/api/movies/popular/">Most popular movies</a> - Displays the top 10 movies sorted by popularity. <a href="{base_url}/api/movies/popular/">{base_url}/api/movies/popular/</a></li>
                <li>GET <a href="{base_url}/api/movies/top-rated/">Top rated movies</a> - Shows movies with an average rating of 8.0 or higher. <a href="{base_url}/api/movies/top-rated/">{base_url}/api/movies/top-rated/</a></li>
                <li>GET <a href="{base_url}/api/movies/language/">Movies by language</a> - Filters movies by their original language (default is English). <a href="{base_url}/api/movies/language/">{base_url}/api/movies/language/</a></li>
                <li>GET <a href="{base_url}/api/movies/recent/">Recent movies</a> - Lists movies released within the last 5 years. <a href="{base_url}/api/movies/recent/">{base_url}/api/movies/recent/</a></li>
                <li>POST <a href="{base_url}/api/movies/add/">Add a new movie</a> - Allows adding a new movie to the database via a POST request. <a href="{base_url}/api/movies/add/">{base_url}/api/movies/add/</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)