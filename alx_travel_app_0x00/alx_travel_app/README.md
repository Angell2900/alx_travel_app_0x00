# ALX Travel App - Database Modeling and Data Seeding

## Project Overview
This project implements database models, serializers, and a seeding command for a travel booking platform.

## Models
- **Listing**: Property listings with UUID, host, title, description, location, price_per_night
- **Booking**: User bookings with dates, total_price, and status
- **Review**: User reviews with rating (1-5) and comments

## Installation
```bash
pip install django djangorestframework
python3 manage.py migrate
python3 manage.py seed
```

## Technologies
- Django 5.x
- Django REST Framework
- SQLite
- Python 3.x
