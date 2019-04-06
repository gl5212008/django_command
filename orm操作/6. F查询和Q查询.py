import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")
    import django

    django.setup()

    from app01 import models
    # ret = models.Book.objects.filter(id__gt=1)
    # print(ret)

    from django.db.models import F, Q

    # ret = models.Book.objects.filter(kucun__lt=F('sale'))
    # for i in ret:
    #     print(i.title,i.kucun,i.sale)

    # book_obj = models.Book.objects.get(id=1)
    # book_obj.title= '跟金老板学开潜艇'
    # book_obj.save()

    # models.Book.objects.all().update(kucun=F('kucun')* 10)

    from django.db.models.functions import Concat
    from django.db.models import Value

    # models.Book.objects.all().update(title=F('title')+'(第一版)')

    # models.Book.objects.all().update(title=Concat(F('title'),Value('(第一版)')))

    ret = models.Book.objects.filter(Q(id__lt=3) | Q(id__gt=5))

    ret = models.Book.objects.filter(~Q(id=3), id__lt=5)

    print(ret)
