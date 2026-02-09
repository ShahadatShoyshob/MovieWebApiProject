from django.contrib import admin
from django.urls import path, include
from .views import home

# Configure URL routing for the Django project, including admin, API, and homepage routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('MovieWebApi.urls')),
    path('', home, name='home'),
]