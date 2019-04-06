import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")
    import django

    django.setup()

    from app01 import models

    # 正向查询
    # 基于对象查询

    # book_obj = models.Book.objects.filter(id=5).first()
    # print(book_obj.title)
    # print(book_obj.publisher)
    # print(book_obj.publisher.id)
    # print(book_obj.publisher.name)

    # 基于字段查询
    # ret = models.Book.objects.filter(publisher__name='沙河出版社')
    ret = models.Book.objects.filter(publisher__id=1)
    # print(ret)
    # for i in ret:
    #     print(i.publisher.name)

    # 反向查询
    # 没有指定related_name，使用pub_obj.book_set.all() 拿所有出版社关联的书籍对象
    # ret = models.Publisher.objects.get(id=1)
    # print(ret.book_set.all())

    # 指定related_name = 'books'，使用pub_obj.books.all() 拿所有出版社关联的书籍对象
    # print(ret.books.all())

    # 基于字段查询
    ret = models.Publisher.objects.filter(books__title='跟金老板学开车')
    print(ret)