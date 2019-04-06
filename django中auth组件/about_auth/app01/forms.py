from django import forms


class RegForm(forms.Form):
    username = forms.CharField(
        label="用户名"
    )
    password = forms.CharField(
        label="密码",
        widget=forms.widgets.PasswordInput()
    )
    re_password = forms.CharField(
        label="确认密码",
        widget=forms.widgets.PasswordInput()
    )