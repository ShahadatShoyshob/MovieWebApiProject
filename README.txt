# Movie Web API (Django REST Framework)

A university project that provides a simple **Movie Web API** built with **Django** and **Django REST Framework (DRF)**.
It exposes endpoints to list movies, fetch popular/top-rated/recent movies, filter by language, and add new movies.

The project includes:
- A Django app (`MovieWebApi`) with a `DataSet` model for movie records
- DRF APIViews + pagination
- A CSV loader script to import a movie dataset into SQLite
- Unit tests for the API endpoints

---

## Tech Stack

- Python 3.11
- Django 5.0.6
- Django REST Framework 3.15.1
- pandas 2.2.2
- SQLite (db.sqlite3)

---

## Project Structure

```
MovieWebApiProject-final/
├─ manage.py
├─ db.sqlite3
├─ requirements.txt
├─ TMDB 10000 Movies Dataset.csv
├─ Scripts/
│  └─ load_data.py
├─ MovieWebApi/                 # Django app (API)
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests.py
└─ MovieWebApiProject/          # Django project
   ├─ settings.py
   ├─ urls.py
   └─ views.py
```

---

## Data Model (Movie)

Each movie record includes:

- `id` (integer)
- `original_language` (string)
- `original_title` (string)
- `overview` (string)
- `popularity` (float)
- `release_date` (YYYY-MM-DD)
- `title` (string)
- `vote_average` (float, 0–10)
- `vote_count` (integer, >= 0)

---

## Setup & Run Locally

### 1) Create and activate a virtual environment

**Windows (PowerShell)**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run migrations
```bash
python manage.py migrate
```

### 4) (Optional) Load dataset from CSV into the database
This project includes a loader script using pandas:

```bash
python Scripts/load_data.py
```

> Note: The script reads `TMDB 10000 Movies Dataset.csv` and inserts/updates records into SQLite.

### 5) Start the server
```bash
python manage.py runserver
```

Open:
- Home page: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- API base: `http://127.0.0.1:8000/api/`

---

## API Endpoints

Base path: `/api/`

### 1) List all movies (paginated)
**GET** `/api/movies/`

Pagination notes:
- Default page size is **500**
- You can use:
  - `?page=2`
  - `?page_size=100` (max 500)

### 2) Popular movies (top 10)
**GET** `/api/movies/popular/`

Returns the **top 10** movies ordered by popularity (descending).

### 3) Top-rated movies (vote_average >= 8.0, paginated)
**GET** `/api/movies/top-rated/`

Returns movies with `vote_average >= 8.0` sorted by rating (descending).

### 4) Filter by language (paginated)
**GET** `/api/movies/language/?lang=en`

Query parameter:
- `lang` (default: `en`)

### 5) Recent movies (last 5 years, paginated)
**GET** `/api/movies/recent/`

Returns movies released within the last **5 years**.

### 6) Add a movie
**POST** `/api/movies/add/`

Example JSON body:
```json
{
  "title": "New Movie",
  "original_title": "New Movie",
  "original_language": "en",
  "overview": "Short summary here",
  "popularity": 60.0,
  "release_date": "2021-01-01",
  "vote_average": 8.1,
  "vote_count": 200
}
```

Validation:
- `release_date` cannot be in the future
- `vote_average` must be between 0 and 10
- `popularity` must be >= 0
- `vote_count` must be >= 0

---

## Running Tests

This repository includes unit tests for the API routes:

```bash
python manage.py test
```

Tests cover:
- movie list
- popular movies
- top-rated movies
- movies filtered by language
- recent movies
- adding a movie via POST

---

## Admin (Optional)

Create an admin user:

```bash
python manage.py createsuperuser
```

Then log in at:
`http://127.0.0.1:8000/admin/`

---

## Notes / Limitations

- This is a coursework project intended for learning REST APIs, Django models, serialization, pagination, and testing.
- SQLite is used for simplicity (easy local setup). For production, you would typically use PostgreSQL/MySQL and environment variables for configuration.
