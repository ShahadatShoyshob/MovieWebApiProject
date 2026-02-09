from rest_framework import serializers
from .models import DataSet
from datetime import date

# Serializer class for handling movie data
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = ['original_language', 'original_title', 'overview', 'popularity', 'release_date', 'title', 'vote_average', 'vote_count']

    # Validate the release_date field to ensure it is not in the future
    def validate_release_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value