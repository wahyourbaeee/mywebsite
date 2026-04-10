import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

application = get_wsgi_application()

# --- KODE PALU GADA DIMULAI ---
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    # Pake get_or_create biar gak error kalau udah ada
    user, created = User.objects.get_or_create(
        username='wahyuadmin',
        defaults={'email': 'wwahyutirta@gmail.com'}
    )
    user.set_password('WahyuGacor2026!')
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("MANTAP! Akun admin udah siap dicolok King!")
except Exception as e:
    print(f"Gagal bikin admin: {e}")
