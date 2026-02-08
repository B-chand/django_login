# Django Login App

A simple Django project that implements:
- Login / logout
- Signup (create a new user)
- Protected dashboard page (requires authentication)
- SQLite database (default)

## Tech
- Python 3.x
- Django
- SQLite (db.sqlite3)

## Quick start (Windows / PowerShell)

1) Create and activate a virtual environment
- `python -m venv .venv`
- `.\.venv\Scripts\Activate.ps1`

2) Install dependencies
- `pip install django`

3) Run migrations
- `python manage.py migrate`

4) Create a user (pick one option)

Option A: Create your own superuser
- `python manage.py createsuperuser`

Option B: Create/reset the demo user (also sets staff + superuser)
- `python manage.py create_demo_user`
  - Demo credentials: username `admin`, password `admin12345`

5) Start the server
- `python manage.py runserver`

Open the app:
- Login page: http://127.0.0.1:8000/
- Signup page: http://127.0.0.1:8000/signup/
- Dashboard (login required): http://127.0.0.1:8000/dashboard/
- Admin: http://127.0.0.1:8000/admin/
- Logout: http://127.0.0.1:8000/logout/

## URL routes
- `/` → login
- `/signup/` → signup
- `/dashboard/` → dashboard (protected)
- `/logout/` → logout
- `/admin/` → Django admin

## Project structure (high level)
- accounts: authentication views + URLs + a demo management command
- config: project settings/urls
- templates: HTML templates (login, signup, dashboard)

## Notes
- This project uses SQLite by default (db.sqlite3).
- For production, set `DEBUG = False`, add `ALLOWED_HOSTS`, and change the secret key.
