from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app01.forms import RegForm
from django.contrib.auth.models import User
from app01 import models

# Create your views here.


def login(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get("name")
        pwd = request.POST.get("pwd")
        # 去数据库校验用户名和密码是否正确
        user = auth.authenticate(request, username=username, password=pwd)
        if user:
            # 表示用户名密码正确
            # 1. 让当前用户登录,给cookie和session写入数据
            auth.login(request, user)
            # 2. 上一步操作执行之后，用户的浏览器有了cookie,session表里有了对应的数据

            # 2.1 session中根据cookie 在session中找到 user信息  --> user_obj/匿名用户
            # 2.2 request.user = user_obj/匿名用户
            return redirect("/index/")
        else:
            # 用户名或密码错误
            error_msg = "用户名或密码错误"
    return render(request, "login.html", {"error_msg": error_msg})


@login_required
def index(request):
    print(request.user, request.user.is_authenticated())
    return render(request, "index.html")


def logout(request):
    # 注销
    auth.logout(request)
    return redirect("/login/")


def reg(request):
    form_obj = RegForm()
    if request.method == "POST":
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 校验成功，去注册
            print(form_obj.cleaned_data)
            # User.objects.create(username=form_obj.cleaned_data.get("username"),password=)
            # 把re_pwd从 cleaned_data中移除
            form_obj.cleaned_data.pop("re_password")
            User.objects.create_user(**form_obj.cleaned_data)  # ?
            # models.UserInfo.objects.create_user(**form_obj.cleaned_data)

            return HttpResponse("OK")
    return render(request, "reg.html", {"form_obj": form_obj})

