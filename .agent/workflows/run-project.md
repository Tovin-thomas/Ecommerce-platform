---
description: How to run the Brokart Django e-commerce project
---

# Running the Brokart E-Commerce Project

This is a Django-based e-commerce application with products, customers, orders, and themes functionality.

## Prerequisites

1. **Python**: Ensure Python 3.10+ is installed
   - Check with: `python --version`
   
2. **pip**: Python package manager should be available
   - Check with: `pip --version`

## Step-by-Step Setup Instructions

### 1. Navigate to the Project Directory

```bash
cd d:\ecarts\brokart
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**On Windows (CMD):**
```bash
venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

If you get an execution policy error in PowerShell, run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Install Django and Dependencies

Since there's no `requirements.txt` file, install the required packages manually:

```bash
pip install django==5.0.1
pip install pillow
```

**Note**: Pillow is typically needed for Django projects with image handling (media files).

### 5. Apply Database Migrations

The project uses SQLite database. Run migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin Account)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create:
- Username
- Email (optional)
- Password

### 7. Collect Static Files (if needed)

```bash
python manage.py collectstatic --noinput
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

### 9. Access the Application

- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

Use the superuser credentials you created in Step 6 to log into the admin panel.

## Common Issues and Solutions

### Issue 1: "No module named django"
**Solution**: Make sure you've activated the virtual environment and installed Django:
```bash
pip install django==5.0.1
```

### Issue 2: Migration errors
**Solution**: Delete the database and migration files (except `__init__.py`), then recreate:
```bash
# Delete db.sqlite3
# Delete migration files in products/migrations/, customers/migrations/, orders/migrations/, themes/migrations/
python manage.py makemigrations
python manage.py migrate
```

### Issue 3: Static files not loading
**Solution**: Check `STATIC_URL` in settings.py and ensure static files are in the correct directory:
```bash
python manage.py collectstatic
```

### Issue 4: Port already in use
**Solution**: Run the server on a different port:
```bash
python manage.py runserver 8080
```

## Project Structure

```
brokart/
├── brokart/          # Main project settings
├── products/         # Products app
├── customers/        # Customers app
├── orders/           # Orders app
├── themes/           # Themes app
├── templates/        # HTML templates
├── static/           # Static files (CSS, JS, images)
├── media/            # User-uploaded files
├── db.sqlite3        # SQLite database
└── manage.py         # Django management script
```

## Next Steps After Running

1. **Explore the Admin Panel**: Add products, manage customers, and view orders
2. **Check the Templates**: Review the HTML templates in the `templates/` directory
3. **Test Functionality**: Navigate through the site to identify any errors
4. **Review Apps**: Check each app (products, customers, orders, themes) for models and views

## Stopping the Server

Press `Ctrl + C` in the terminal where the server is running.

## Deactivating the Virtual Environment

When you're done working:
```bash
deactivate
```
