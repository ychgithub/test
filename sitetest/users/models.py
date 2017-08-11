from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class usertest(AbstractUser):
    nickname=models.CharField('昵称',max_length=20)
    phonenum=models.CharField('手机号',max_length=11)
    sex=models.CharField('性别',choices=(('man','男'),('woman','女'),('futa','小姐姐')),max_length=10,default='futa')
    pic=models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100)
    birthday=models.DateTimeField('生日',null=True,blank=True)

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

class verification_code(models.Model):
    code=models.CharField('验证码',max_length=20)
    email=models.EmailField('邮箱',max_length=50)
    type=models.CharField(choices=(('register','注册'),('forget','忘记密码')),max_length=10)

    class Meta:
        verbose_name='验证码'
        verbose_name_plural=verbose_name