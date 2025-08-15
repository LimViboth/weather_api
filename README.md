# Weather API (Django + DRF)

A simple REST API for managing cities, weather records and user favorite cities built with Django and Django REST Framework.

## Quick overview
- Django project: `weather_api`
- App: `weather`
- Authentication: JWT (djangorestframework-simplejwt) and optional session login for browsable API
- API docs: Swagger UI at `/swagger/`

## Requirements
- Python 3.11+ (your environment may be newer)
- A virtual environment (recommended)

## Setup (Windows PowerShell)
```powershell
# create venv (if not already created)
py -3 -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# apply migrations
py manage.py makemigrations
py manage.py migrate

# create a superuser
py manage.py createsuperuser

# optionally seed sample data
py manage.py seed

# run server
py manage.py runserver
```

Server will be available at: http://127.0.0.1:8000/

## Seed command
A management command `seed` is included to populate the DB with sample users, cities, weather records and favorites:

```powershell
py manage.py seed
```

Default seeded users: `user1`, `user2`, `user3` (password: `password`).

## API endpoints
- `GET /api/cities/` - list cities
- `GET /api/weather/` - list weather records
- `GET /api/favorites/` - list current user's favorite cities (requires auth)
- `POST /api/token/` - obtain JWT (`username` + `password`)
- `POST /api/token/refresh/` - refresh JWT

## Swagger UI
Open `http://127.0.0.1:8000/swagger/` for API documentation and interactive testing.

To authorize requests in Swagger, click **Authorize** and enter:
```
Bearer <your_access_token>
```
(you can obtain the token from `POST /api/token/` in Swagger.)

## Browsable API login
To log in via the browsable API (no token required for browser testing), visit:

```
http://127.0.0.1:8000/api-auth/login/
```

This uses Django session authentication.

## Using the API (examples)
cURL (get cities):
```powershell
curl http://127.0.0.1:8000/api/cities/
```

cURL (obtain token):
```powershell
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"password"}' http://127.0.0.1:8000/api/token/
```

cURL (authenticated request):
```powershell
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/api/favorites/
```

## Notes
- Administrators can create/edit/delete cities and weather; regular users can manage their own favorites.
- If you want non-admin users to create cities or weather, modify the view permissions in `weather/views.py`.

## Troubleshooting
- `TemplateDoesNotExist drf-yasg/swagger-ui.html` — make sure `drf-yasg` is installed and added to `INSTALLED_APPS`.
- `no such table` — run migrations.
- `Authentication credentials were not provided.` — include the `Authorization` header or log in via `/api-auth/login/`.

If you want I can add an example Postman collection or export runnable example scripts.
