from django import forms
from app01 import models
from django.core.validators import RegexValidator  # 导入Django内置的正则校验规则
from django.core.exceptions import ValidationError  # 导入Django内置的校验异常的类


# 自定义校验的方法
def name_check(value):
    if '金瓶梅' in value:
        raise ValidationError("不符合社会主义核心价值观！")
    else:
        return value


# 按照Django form组件的要求自己写一个类
class RegForm(forms.Form):
    name = forms.CharField(
        min_length=6,
        max_length=12,
        label="用户名",
        initial="孟孟",
        error_messages={
            "min_length": "用户名不能少于6位",
            "required": "用户名不能为空"
        },
        # validators=[name_check, ],
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"}
        )
    )
    pwd = forms.CharField(
        label="密码",
        error_messages={
            "required": "密码不能为空"
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'},  # 给生成的标签添加属性
            render_value=True  # 返回报错信息的时候要不要展示密码
        )
    )
    re_pwd = forms.CharField(
        label="确认密码",
        error_messages={
            "required": "确认密码不能为空"
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'},  # 给生成的标签添加属性
            render_value=True  # 返回报错信息的时候要不要展示密码
        )
    )
    phone = forms.CharField(
        label="手机",
        validators=[RegexValidator(r'^1[3|4|5|6|7|8|9]\d{9}$', "手机号码格式不正确！"), ]

    )

    def clean_name(self):
        print("我看了源码，你应该会帮我执行这个方法！")
        value = self.cleaned_data.get("name")
        if "金瓶梅" in value:
            raise ValidationError("不符合社会主义核心价值观！")
        else:
            return value

    def clean(self):
        print("我可是看过源码的人，我知道你肯定会执行这个方法！")
        # 重写父类的clean方法
        # 该clean方法， 在每个字段都校验通过之后才调用执行
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if re_pwd and re_pwd == pwd:
            # 确认密码和密码相同， 正常
            return self.cleaned_data
        else:
            # 确认密码和密码不同
            self.add_error('re_pwd', "两次密码不一致")
            raise ValidationError("两次密码不一致")
    gender = forms.ChoiceField(
        label="性别",
        choices=((1, "男"), (2, "女"), (3, "保密")),
        initial=3,
        widget=forms.widgets.RadioSelect()
    )
    remember = forms.ChoiceField(
        label="记住密码",
        widget=forms.widgets.CheckboxInput()
    )
    hobby = forms.ChoiceField(
        label="爱好",
        choices=((1, "篮球"), (2, "足球"), (3, "双色球")),
        widget=forms.widgets.CheckboxSelectMultiple()
    )
    job = forms.ChoiceField(
        label="职业",
        choices=models.Job.objects.all().values_list("id", "name"),
        widget=forms.widgets.Select()
    )
    jobs = forms.ChoiceField(
        label="兼职",
        choices=((1, "送外卖"), (2, "搬砖"), (3, "送快递")),
        widget=forms.widgets.SelectMultiple()
    )
    memo = forms.CharField(
        label="个人简介",
        required=False,
        widget=forms.widgets.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields["job"].choices = models.Job.objects.all().values_list("id", "name")
