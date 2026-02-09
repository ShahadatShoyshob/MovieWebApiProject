# Script to load movie data from a CSV file into the Django database
import sys
import os
import pandas as pd
from django.utils.dateparse import parse_date

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieWebApiProject.settings')
import django
django.setup()

from MovieWebApi.models import DataSet

# Function to load and process movie data from a CSV file
def load_dataset_data(csv_file):
    df = pd.read_csv(csv_file)
    print(f"Total rows in CSV: {len(df)}")

    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    print(f"Columns in CSV: {df.columns.tolist()}")

    required_columns = ['id', 'title', 'release_date', 'original_language', 'original_title', 'overview', 'popularity', 'vote_average', 'vote_count']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df.dropna(subset=['id', 'title', 'release_date'])
    print(f"Rows after dropping missing id/title/release_date: {len(df)}")

    # Function to parse dates in multiple formats with fallback
    def parse_date_with_fallback(date_str):
        if pd.isna(date_str):
            return None
        parsed_date = parse_date(date_str)
        if parsed_date:
            return parsed_date
        try:
            return pd.to_datetime(date_str, format='%d/%m/%Y').date()
        except (ValueError, TypeError):
            pass
        try:
            return pd.to_datetime(date_str, format='%m-%d-%Y').date()
        except (ValueError, TypeError):
            return None

    df['release_date'] = df['release_date'].apply(parse_date_with_fallback)
    print(f"Rows after parsing release_date: {len(df)}")

    df = df[df['release_date'].notna()]
    print(f"Rows after filtering invalid release_dates: {len(df)}")

    if len(df) == 0:
        print("No rows to load after filtering. Check date formats or data quality.")
        return

    for _, row in df.iterrows():
        DataSet.objects.update_or_create(
            id=int(row['id']),
            defaults={
                'original_language': str(row['original_language']),
                'original_title': str(row['original_title']),
                'overview': str(row['overview']) if pd.notna(row['overview']) else '',
                'popularity': float(row['popularity']),
                'release_date': row['release_date'],
                'title': str(row['title']),
                'vote_average': float(row['vote_average']),
                'vote_count': int(row['vote_count'])
            }
        )
    print(f"Loaded {len(df)} datasets into the database.")

# Main execution block
if __name__ == '__main__':
    csv_file = 'TMDB 10000 Movies Dataset.csv'
    load_dataset_data(csv_file)