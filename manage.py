def create_admin():
    try:
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        User = get_user_model()
        # Cari user, kalau ada kita update passwordnya biar pasti bener
        user, created = User.objects.get_or_create(
            username='wahyuadmin',
            defaults={'email': 'wwahyutirta@gmail.com'}
        )
        user.set_password('WahyuGacor2026!')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("Admin account ready to use!")
    except Exception as e:
        print(f"Admin creation skipped: {e}")