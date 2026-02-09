## requirements.txt
Django==5.0.6
djangorestframework==3.15.1
pandas==2.2.2

## Development Environment
- Windows
- Python Version: 3.11
- Django Version: 5.0.6

## Installation Instructions
1. Clone the repository:
   ```
   git clone <repository_url>
   cd MovieWebApiProject
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```
   - Username: admin123
   - Password: admin123
   - Email: (can be left blank)

6. Load movie data:
   ```
   python Scripts/load_data.py
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application:
   - Main page: https://<your-domain>/
   - Admin site: https://<your-domain>/admin/ (use username: admin, password: admin123)
   - API endpoints: https://<your-domain>/api/movies/, etc.

## Running Unit Tests
Run the unit tests with:
```
python manage.py test MovieWebApi
```

## Data Loading Script
The data loading script is located at `Scripts/load_data.py`. It loads data from `TMDB 10000 Movies Dataset.csv` into the SQLite database. Ensure the CSV file is in the project root before running:
```
python Scripts/load_data.py
```
