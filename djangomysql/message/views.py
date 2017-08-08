from django.shortcuts import render,HttpResponse
from .models import message
# Create your views here.
def getmessage(request):
    pass
    return render(request,'message.html')

def test(request):
    a = message()
    if request.method == 'POST':
        a.nickname = request.POST.get('nickname', '')
        a.email = request.POST.get('email', '')
        a.address = request.POST.get('address', '')
        a.message = request.POST.get('message', '')
        a.save()
    a = message.objects.all()
    return render(request, 'test.html',{'htmla':a})
    # return HttpResponse(len(a))