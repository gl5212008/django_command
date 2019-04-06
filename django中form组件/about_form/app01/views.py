from django.shortcuts import render, HttpResponse
from app01 import models
from app01.forms import RegForm
# Create your views here.


# 注册
def register(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get("name")
        pwd = request.POST.get("pwd")
        # 对注册信息做校验
        if len(username) < 6:
            # 用户长度小于6位
            error_msg = "用户名长度不能小于6位"
        else:
            # 将用户名和密码存到数据库
            return HttpResponse("注册成功")
    return render(request, "register.html", {"error_msg": error_msg})


# 使用form组件的注册方式
def register2(request):
    form_obj = RegForm()
    if request.method == "POST":
        # 实例化form对象的时候，把post提交过来的数据直接传进去
        form_obj = RegForm(request.POST)
        # 调用form_obj校验数据的方法
        if form_obj.is_valid():
            # form_obj.cleaned_data  # 所有经过校验的数据
            # models.UserInfo.objects.create(
            #     name=request.POST.get("name"),
            #     pwd=request.POST.get("pwd")
            # )
            # # 等价于上面的创建记录的操作
            # models.UserInfo.objects.create(**form_obj.cleaned_data)
            return HttpResponse("登陆成功")
    return render(request, "register2.html", {"form_obj": form_obj})