from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from students.models import student
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.
def register(request):
    if (request.method == "POST"):
        u=request.POST['u']
        p= request.POST['p']
        c= request.POST['c']
        e= request.POST['e']
        f= request.POST['f']
        l= request.POST['l']
        if(p==c):
           user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
           user.save()
           return redirect('books:h')
        else:
            return HttpResponse("Password are not same")

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        n=request.POST['n']
        d=request.POST['d']
        user=authenticate(username=n,password=d)
        if user:
            login(request,user)
            return redirect('books:h')
        else:
            return HttpResponse("Invalid credentials")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('students:login')
def viewstudent(request):
    s=student.objects.all()
    return render(request,'viewstudent.html',{'d':s})
