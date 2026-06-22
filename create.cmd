REM # Create and navigate into directory
mkdir django_headless
cd django_headless

REM # Start project and app
django-admin startproject headless_project .
python manage.py startapp headless_api
