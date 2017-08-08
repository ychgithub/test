from django.db import models

# Create your models here.
class message(models.Model):
    nickname=models.CharField('昵称',max_length=20)
    email=models.EmailField('邮箱',blank=True)
    address=models.CharField(verbose_name='联系地址',max_length=100,blank=True)
    message=models.CharField('留言',max_length=500)

    class Meta:
        verbose_name='用户留言'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.nickname