#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def create_admin():
    try:
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='wahyuadmin').exists():
            User.objects.create_superuser('wahyuadmin', 'wwahyutirta@gmail.com', 'WahyuGacor2026!')
            print("Admin account created successfully!")
    except Exception as e:
        print(f"Admin creation skipped: {e}")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
    
    # Cek apakah ini perintah runserver atau gunicorn (saat web startup)
    # Kita bikin admin cuma pas server mau jalan aja biar gak ganggu proses lain
    if len(sys.argv) > 1 and sys.argv[1] in ['runserver', 'gunicorn']:
        create_admin()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()