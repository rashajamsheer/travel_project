from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Name


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Name.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
#def demo2(request):
    #return render(request,'about.html')

#def demo3(request):
    #return render(request,'content.html')
#def demo4(request):
   # return HttpResponse('this is demo4 function')