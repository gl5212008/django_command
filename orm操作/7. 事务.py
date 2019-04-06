import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")
    import django
    django.setup()

    from app01 import models

    try:
        from django.db import transaction
        with transaction.atomic():
            models.Publisher.objects.create(name='沙河银行')
            models.Publisher.objects.get(id=100)

    except Exception as e:
        print(str(e))