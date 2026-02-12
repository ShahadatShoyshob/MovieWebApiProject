# Movie Web API (Django REST Framework) — TMDB Dataset

A university project that provides a simple **RESTful Movie API** built with **Django** and **Django REST Framework (DRF)**.  
The API supports listing movies (paginated), retrieving popular/top‑rated/recent movies, filtering by language, and adding new movies.

---

## Tech Stack

- Python **3.11**
- Django **5.0.6**
- Django REST Framework **3.15.1**
- pandas **2.2.2**
- Database: **SQLite** (`db.sqlite3`)

---

## Project Structure

```
MovieWebApiProject-final/
├─ manage.py
├─ requirements.txt
├─ db.sqlite3
├─ TMDB 10000 Movies Dataset.csv
├─ Scripts/
│  └─ load_data.py
├─ MovieWebApi/                  # Django app (API)
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests.py
└─ MovieWebApiProject/           # Django project
   ├─ settings.py
   ├─ urls.py
   └─ views.py                   # home page with endpoint links
```

---

## Data Model

The API uses a `DataSet` model for movies:

- `original_language` (string)
- `original_title` (string)
- `overview` (text, optional)
- `popularity` (float, >= 0)
- `release_date` (date)
- `title` (string)
- `vote_average` (float, 0–10)
- `vote_count` (int, >= 0)
- `created_at` (timestamp)

---

## Setup & Run (Local)

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
This repo includes a CSV loader script (uses pandas). From the project root, run:

```bash
python Scripts/load_data.py
```

> The CSV file `TMDB 10000 Movies Dataset.csv` is included in this repository.

### 5) Start the server
```bash
python manage.py runserver
```

Open in your browser:
- Home page: `http://127.0.0.1:8000/`
- API base: `http://127.0.0.1:8000/api/`
- Admin: `http://127.0.0.1:8000/admin/`

---

## API Endpoints

Base path: `/api/`

### 1) List all movies (paginated)
**GET** `/api/movies/`

Pagination:
- Default page size: **500**
- Custom page size (max 500): `?page_size=100`
- Page number: `?page=2`

Example:
```
/api/movies/?page=1&page_size=200
```

### 2) Popular movies (top 10)
**GET** `/api/movies/popular/`  
Returns the **top 10** movies ordered by `popularity` (descending).

### 3) Top‑rated movies (paginated)
**GET** `/api/movies/top-rated/`  
Returns movies where `vote_average >= 8.0`, ordered by rating (descending).

### 4) Movies by language (paginated)
**GET** `/api/movies/language/?lang=en`  
Query param:
- `lang` (defaults to `en` if not provided)

### 5) Recent movies (paginated)
**GET** `/api/movies/recent/`  
Returns movies released within the **last 5 years**.

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

This repository includes API unit tests.

```bash
python manage.py test
```

---

## Admin Notes (Coursework)

The home page view may display example admin credentials for demonstration.  
If you publish this repo publicly, **change/remove any default credentials** and create your own superuser:

```bash
python manage.py createsuperuser
```

---
