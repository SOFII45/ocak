# Association Management System - Django Backend

Complete Django backend implementation for the association management system with all 6 mandatory sections.

## Project Structure

```
association_system/
├── manage.py
├── requirements.txt
├── .env.example
├── association_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── announcements/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── projects/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── education/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── martyrs/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── about/
    ├── models.py
    ├── admin.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Database

Create PostgreSQL database:

```sql
CREATE DATABASE association_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE association_db TO postgres;
```

### 3. Configure Environment

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

### 7. Access Admin Panel

Navigate to: `http://localhost:8000/admin/`

## API Endpoints

### Authentication
- POST `/api/v1/auth/login/` - Login and get JWT token
- POST `/api/v1/auth/refresh-token/` - Refresh JWT token

### Home
- GET `/api/v1/home/` - List all active home content
- GET `/api/v1/home/{id}/` - Get single home content

### Announcements
- GET `/api/v1/announcements/` - List all active announcements (paginated)
- GET `/api/v1/announcements/{id}/` - Get single announcement
- GET `/api/v1/announcements/featured/` - Get featured announcements

### Projects
- GET `/api/v1/projects/` - List all active projects (paginated)
- GET `/api/v1/projects/{id}/` - Get single project
- GET `/api/v1/projects/?status=active` - Filter by status

### Education
- GET `/api/v1/education/` - List all active programs (paginated)
- GET `/api/v1/education/{id}/` - Get single program
- GET `/api/v1/education/?program_type=scholarship` - Filter by type

### Martyrs
- GET `/api/v1/martyrs/` - List all active martyrs (paginated)
- GET `/api/v1/martyrs/{id}/` - Get single martyr profile
- GET `/api/v1/martyrs/?year=2023` - Filter by year

### About Us
- GET `/api/v1/about/` - List all active about sections
- GET `/api/v1/about/{id}/` - Get single about section
- GET `/api/v1/about/?section_type=contact` - Filter by section type

## Admin Panel Features

All 6 sections have fully functional admin panels with:

- ✅ CRUD operations
- ✅ Image upload and preview
- ✅ Rich text editing
- ✅ Active/inactive toggle
- ✅ Bulk actions
- ✅ Search and filter
- ✅ Role-based permissions

## Production Deployment

### 1. Update Settings

In `settings.py`:
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS`
- Set proper `SECRET_KEY`
- Configure production database

### 2. Collect Static Files

```bash
python manage.py collectstatic
```

### 3. Use Production Server

Use Gunicorn or uWSGI:

```bash
pip install gunicorn
gunicorn association_project.wsgi:application
```

## Database Schema

All tables are created automatically via migrations:
- home_homecontent
- announcements_announcement
- projects_project
- education_educationprogram
- martyrs_martyr
- about_aboutus

## Notes

- All apps support image uploads to their respective media folders
- All APIs return JSON with `success` and `data` fields
- Pagination is automatic for list endpoints (10 items per page)
- All endpoints support filtering, searching, and ordering
- JWT authentication is required for write operations
- Public read access is allowed for all content endpoints
