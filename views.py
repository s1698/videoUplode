from django.shortcuts import render

from .models import Vedio

# Create your views here.
def index(request):
    vedio=Vedio.objects.all()
    return render(request,"Vedio/index.html",{"vedio":vedio})
# Create your views here.
