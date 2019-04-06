import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")
    import django

    django.setup()

    from app01 import models

    author_obj = models.Author.objects.first()
    # print(author_obj.books.all())
    # print(type(author_obj.books))

    # author_obj.books.create(title='跟金老板学美容美发', publisher_id=1)
    # 1. 先创建书籍对象
    # 2. 创建author_obj和新建书籍对象的对应关系

    # shahe = models.Publisher.objects.first()
    #
    # shahe.books.create(title='跟金老板学烫头3')
    # author_obj.books.set([])

    book_obj = models.Book.objects.first()
    # author_obj.books.clear()

    pub_obj = models.Publisher.objects.first()
    pub_obj.books.clear()