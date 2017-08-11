from django.shortcuts import render,HttpResponse
from .models import usertest,verification_code
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .forms import loginform,newform
from email_about.send_email import send_code_email


# 自定义后台认证,邮箱,手机号,用户名
class testBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            x=usertest.objects.get(Q(username=username)|Q(email=username))
            if x.check_password(password):
                return x
        except Exception as e:
            return None

def index(request):
    return render(request,'index.html')

class logintest(View):
    def get(self,request):
        x=loginform()
        return render(request, 'login.html',{'html_login_forms':x})
    def post(self,request):
        x=loginform(request.POST)
        if x.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            confirm = authenticate(username=user_name, password=pass_word)
            if confirm is not None:
                login(request, confirm)
                return render(request, 'index.html', {'html_username': confirm.username})
            else:
                x.errors['false']='账号或密码错误'
                return render(request,'login.html',{'html_login_forms':x})
        else:
            return render(request,'login.html',{'html_login_forms':x})



# def logintest(request):
#     if request.method == 'POST':
#         user_name=request.POST.get('username','')
#         pass_word=request.POST.get('password','')
#         confirm=authenticate(username=user_name,password=pass_word)
#         if confirm is not None:
#             login(request,confirm)
#             return render(request,'index.html',{'html_username':confirm.username})
#         else:
#             return HttpResponse('账号或密码错误')
#     else:
#         return render(request,'login.html')

def logouttest(request):
    logout(request)
    return render(request,'index.html')

class new(View):
    def get(self,request):
        x=newform()
        return render(request, 'new.html',{'html_new_forms':x})
    def post(self,request):
        x=newform(request.POST)
        html_new_messages={
            'html_new_forms':x,
            'html_new_date':request.POST,
        }
        if x.is_valid():
            a = usertest()
            a.nickname = request.POST.get('nickname', '')
            a.username = request.POST.get('username', '')
            password = request.POST.get('password', )
            password_again = request.POST.get('password_again','')
            a.set_password(password)
            a.email = request.POST.get('email', '')
            a.phonenum = request.POST.get('phonenum', '')
            a.sex = request.POST.get('sex', '')
            if password==password_again:
                a.save()
                send_code_email(a.email,"register")
                return render(request, 'login.html')
            else:
                x.errors['false'] = '两次密码不一致'
                return render(request, 'new.html', context=html_new_messages)
        else:
            return render(request,'new.html',context=html_new_messages)



# def new(request):
#     a = usertest()
#     if request.method == 'POST':
#         a.nickname = request.POST.get('nickname', '')
#         a.username = request.POST.get('username', '')
#         password = request.POST.get('password',)
#         a.set_password(password)
#         a.email = request.POST.get('email', '')
#         a.phonenum = request.POST.get('phonenum', '')
#         a.sex=request.POST.get('sex','')
#         a.save()
#         return render(request, 'login.html')
#     else:
#         return render(request,'new.html')


class forget(View):
    def get(self,request):
        return render(request,'forget.html')
    def post(self,request):
        x=request.POST.get('email')
        send_code_email(x,"forget")
        return render(request,'index.html')

class active(View):
    def get(self,request,code_back):
        x='这是一个简单的返回页面,按理说会在这里加入更多的逻辑代码,让功能更佳完善,不过今天周五了.<p></p>验证码是{}'.format(code_back)
        return HttpResponse(x)