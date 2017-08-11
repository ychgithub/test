from random import Random
from django.core.mail import send_mail
from sitetest.settings import EMAIL_FROM

from users.models import verification_code



def random_str(randomlength=8):
    str = ''
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_code_email(email, send_type='register'):
    email_cord = verification_code()
    code = random_str(16)
    email_cord.code = code
    email_cord.email = email
    email_cord.type = send_type
    email_cord.save()

    if send_type == 'register':
        email_title = '这是悠然生活的验证码邮件测试'
        email_body = '点击网址激活账号:http://127.0.0.1:8000/active/{0}'.format(code)
        send_mail(email_title, email_body, EMAIL_FROM, [email])


    if send_type=='forget':
        email_title='这个是用来找回密码验证的,其实都是一样'
        email_body='点击这个链接什么乱七八糟的东西反正只要看见邮件就表示成功了对吧.'
        send_mail(email_title, email_body, EMAIL_FROM, [email])
