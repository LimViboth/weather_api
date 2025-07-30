# 🌦 Weather API - Django REST Framework

A RESTful API built with **Django** and **Django Rest Framework (DRF)** for managing weather data, cities, and user favorite locations.  
This project implements **JWT authentication**, **role-based access control**, **CRUD operations**, **pagination**, and **Swagger API documentation**.

---

## 📌 Features
- **CRUD Operations** for:
  - Cities
  - Weather records
  - User favorite cities
- **JWT Authentication** for secure access
- **Role-Based Access Control**
  - Admin users: Can add, edit, delete all data
  - Regular users: Can only view data and manage their own favorites
- **Pagination** for large datasets
- **Swagger API Documentation**
- **Unit Tests** for API endpoints

---

## 📂 Project Structure

weather_api/
│
├── weather_api/ # Project settings
│ ├── settings.py # DRF & JWT configuration
│ ├── urls.py # Root API routes
│
├── weather/ # Weather app
│ ├── models.py # Database models
│ ├── serializers.py # DRF serializers
│ ├── views.py # API views
│ ├── permissions.py # Custom permissions
│ ├── urls.py # App-specific routes
│ ├── tests.py # Unit tests
│
├── manage.py
├── requirements.txt
└── README.md


---

## 🛠 Installation

Follow these steps to run the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/weather-api.git
cd weather-api

2. Create and Activate a Virtual Environment

python -m venv venv
# Activate for Mac/Linux
source venv/bin/activate
# Activate for Windows
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Admin)

python manage.py createsuperuser

Enter your desired username, email (optional), and password.
6. Run the Server

python manage.py runserver

Server will start at:
http://127.0.0.1:8000/
🔑 Authentication

This API uses JWT Authentication.
1. Get Token

POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}

2. Use Token in Requests

Include the token in your request header:

Authorization: Bearer <your_access_token>
