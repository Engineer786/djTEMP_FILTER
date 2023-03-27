from django.contrib import admin
from WebApp.models import Manager
# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name','sal','email','address']
admin.site.register(Manager,ManagerAdmin)
