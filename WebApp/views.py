from django.shortcuts import render
from WebApp.models import Manager
# Create your views here.
def Filter_Data(request):
    datalist=Manager.objects.all()
    m1={"datalist":datalist}
    return render(request,'welcome.html',m1)
