import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")

    import django
    django.setup()

    from app01 import models
    ret = models.Person.objects.filter(id__gt=1)
    ret = models.Person.objects.filter(id__lt=5)   # less than
    ret = models.Person.objects.filter(id__gte=3)
    ret = models.Person.objects.filter(id__lte=3)
    ret = models.Person.objects.filter(id__gte=3,id__lte=5)

    ret = models.Person.objects.filter(id__in=[1,3,5,7,9,])     # in
    ret = models.Person.objects.exclude(id__in=[1,3,5,7,9,])    # not in

    ret = models.Person.objects.filter(name__contains='du')
    ret = models.Person.objects.filter(name__icontains='du')

    ret = models.Person.objects.filter(id__range=[1,5])
    ret = models.Person.objects.filter(name__startswith='杜')
    ret = models.Person.objects.filter(name__endswith='飞')

    # ret = models.Person.objects.filter(birth__contains='2018-06')
    # ret = models.Person.objects.filter(birth__month=6)
    # ret = models.Person.objects.filter(birth__day=1)

    print(ret)

