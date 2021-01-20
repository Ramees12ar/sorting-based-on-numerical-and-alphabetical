from django.shortcuts import render
from app.models import *

# Create your views here.
def home(request):
    return render(request,"index.html",{})

def adding(request):
    n=request.POST.get("data")
    if n.isdigit()==True:
        print("int")
        dat=numeric(data=n)
        dat.save()
    elif n.isalpha()==True:
        print("string")
        dat=alphabet(data=n)
        dat.save()
    else:
        print("alphanum")
        dat=alpha_numer(data=n)
        dat.save()
    a=numeric.objects.all()
    b=alphabet.objects.all()
    c=alpha_numer.objects.all()
    return render(request,"index.html",{"num":a,"alp":b,"alnum":c})

def clear(request):
    a=numeric.objects.all()
    b=alphabet.objects.all()
    c=alpha_numer.objects.all()
    a.delete()
    b.delete()
    c.delete()
    return render(request,"index.html",{"num":a,"alp":b,"alnum":c})

def delete(request):
    n=request.POST.get("val")
    m=request.POST.get("id")
    if m=="1":
        obj=alphabet.objects.filter(lid=n)
        obj.delete()
    elif m=="2":
        obj=numeric.objects.filter(lid=n)
        obj.delete()
    elif m=="3":
        obj=alpha_numer.objects.filter(lid=n)
        obj.delete()
    a=numeric.objects.all()
    c=alpha_numer.objects.all()
    b=alphabet.objects.all()
    return render(request,"index.html",{"num":a,"alp":b,"alnum":c})
