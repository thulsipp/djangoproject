from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def allcategories(request):
    m = Category.objects.all()
    return render(request,'category.html',{'m':m})

def product(request,p):

    m=Category.objects.get(name=p)
    p=Product.objects.filter(category=m)
    return render(request,'product.html',{'m':m,'p':p})

def details(request,c):
    p= Product.objects.get(name=c)
    return render(request,'details.html',{'p':p})


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        # o=request.POST['o']
        # a=request.POST['a']
        if(p==cp):
            user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return redirect('shop:cate')
        else:
            return HttpResponse("Password are not same")
    return render(request,'register.html')


def user_login(request):
    if(request.method=="POST"):
        r=request.POST['r']
        w=request.POST['w']
        user=authenticate(username=r,password=w)
        if user:
            login(request,user)
            return redirect('shop:cate')
        else:
            return HttpResponse("Invalid credentials")

    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)

    return redirect('shop:log')






