import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day68_orm.settings")
    import django

    django.setup()

    from app01 import models

    # all 查询所有数据  ——》QuerySet
    ret = models.Person.objects.all()
    # print(ret)

    # get 获取一个对象  如果查询没有或者多个  就报错
    ret = models.Person.objects.get(id=1)
    ret = models.Person.objects.get(name='和尚')
    # print(ret)

    # filter 查询所有满足条件的对象  ——》QuerySet
    ret = models.Person.objects.filter(id=1)
    ret = models.Person.objects.filter(name='杜举飞1')

    # exclude 查询所有不满足条件的对象  ——》QuerySet
    ret = models.Person.objects.exclude(id=1)

    # values 不写参数 取对象的所有字段数据  指定参数  取对象指定字段的参数 ——》QuerySet  元素是字典
    ret = models.Person.objects.values('name','age')
    # print(ret)

    # print('*'*120)
    # for i in ret:
    #     print(i,type(i))

    # values_list
    # 不写参数 取对象的所有字段数据 元组形式
    # 指定参数 取对象指定字段的参数 ——》QuerySet  按照你参数顺序排序
    ret = models.Person.objects.values_list('age','name')
    # print(ret)
    #
    # print('*'*120)
    # for i in ret:
    #     print(i,type(i))

    # order_by 按照指定字段排序 默认升序  加负号降序
    # 可以多字段排序
    ret =models.Person.objects.all().order_by('age','-id')
    # for i in ret:
    #     print(i,i.id,i.age)


    # reverse 对已经排序的QuerySet进行反向排序
    # 用了order_by  要不用了ordering
    ret =models.Person.objects.all().order_by('age','-id').reverse()
    # for i in ret:
    #       print(i,i.id,i.age)

    # ret = models.Person.objects.all()
    # print(ret)
    # ret = models.Person.objects.all().reverse()
    # print(ret)

    # distinct 去重


    # count() 计数  对QuerySet的对象进行计数
    ret = models.Person.objects.filter(id=100).count()

    # first 取QuerySet中的第一元素
    ret = models.Person.objects.all().first()


    ret = models.Person.objects.last()

    # print(ret)
    ret = models.Person.objects.filter(id=100).exists()
    print(ret)


"""
返回QuerySet的方法：
1. all()
2. filter()
3. exclude()
4. values()
5. values_list()
6. reverse()
7. distinct()
8. order_by()

返回具体对象的方法：
1. get()
2. first()
3. last()

返回数字的方法：
1. count()

返回布尔值：
1. exists()
"""

