from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Model class representing a movie dataset
class DataSet(models.Model):
    id = models.AutoField(primary_key=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    popularity = models.FloatField(validators=[MinValueValidator(0.0)])
    release_date = models.DateField()
    title = models.CharField(max_length=255)
    vote_average = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ['-created_at']

    # Return the movie title as the string representation of the model
    def __str__(self):
        return self.title