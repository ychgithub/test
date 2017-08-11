from django.contrib import admin
from .models import usertest,verification_code
# Register your models here.

class usertestAdmin(admin.ModelAdmin):
    list_display = ['username','nickname','phonenum','sex','birthday']
    search_fields = ['username','nickname','sex']
    list_filter = ['sex','birthday']
class verification_codeAdmin(admin.ModelAdmin):
    list_display = ['code','email','type']

admin.site.register(usertest,usertestAdmin)
admin.site.register(verification_code,verification_codeAdmin)