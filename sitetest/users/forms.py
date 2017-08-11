from django import forms
from captcha.fields import CaptchaField

class loginform(forms.Form):
    username=forms.CharField(required=True,min_length=5,max_length=15)
    # 这个username是模板表单中的name参数,两者必须设置一致才能完成数据传递.
    password=forms.CharField(required=True,min_length=5,max_length=15)
    captcha = CaptchaField()



class newform(forms.Form):
    nickname=forms.CharField(required=True,min_length=5,max_length=15)
    username=forms.CharField(required=True,min_length=5,max_length=15)
    password=forms.CharField(required=True,min_length=9,max_length=18)
    email=forms.EmailField(required=True)
    phonenum=forms.CharField(required=True,max_length=11)
    sex=forms.CharField(required=True)
    captcha=CaptchaField()
