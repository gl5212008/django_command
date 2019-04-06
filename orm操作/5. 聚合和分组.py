import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")
    import django

    django.setup()

    from app01 import models

    from django.db.models import Avg, Sum, Max, Min, Count

    # ret = models.Book.objects.aggregate(Sum('price'),Count('id'),pingjun=Avg('price'),)
    # print(ret)

    ret = models.Book.objects.annotate(Count('author'),).values()
    for i in ret:
        print(i)

    # ret = models.Publisher.objects.annotate(min_price=Min('books__price')).values()
    # for i in ret:
    #     print(i)

    # ret = models.Book.objects.annotate(author_num=Count('author')).filter(author_num__gt=1)
    # for i in ret:
    #     print(i)
    #
    # ret = models.Book.objects.annotate(author_num=Count("author")).order_by("-author_num")
    # print(ret)
    #

    # ret = models.Author.objects.annotate(Sum('books__price')).values()
    # print(ret)

