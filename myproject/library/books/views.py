from books.forms import bookform
from django.db.models import Q
from django.shortcuts import render
from books.models import Book
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# Create your views here.
def home(request):

    return render(request,'home.html')
@login_required
def addbooks(request):
    if(request.method=="POST"):#after submission
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']

        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbooks(request)
    return render(request,'addbooks.html')
@login_required
def viewbooks(request):
    k = Book.objects.all()
    return render(request,'viewbooks.html',{'b':k})
@login_required
def addbooks1(request):
    if(request.method=="POST"):#after submission:
        form=bookform(request.POST)#create form object initialized with values inside request.POST
        if form.is_valid():
            form.save()#saves form object in db model Book
            return viewbooks(request)
    form=bookform()#create empty form object
    return render(request,'addbooks1.html',{'form':form})
@login_required
def factorial(request):
    if(request.method=="POST"):
        num=int(request.POST['n'])
        # return HttpResponse(num)
        f=1
        for i in range(1,num+1):
          f=f*i
        return render(request,'factorial.html',{'factorial':f})
    return render(request,'factorial.html')

def detail(request,p):

    b=Book.objects.get(id=p)
    return render(request,'bookdetail.html',{'b':b})
@login_required
def edit(request,p):
    b= Book.objects.get(id=p)

    if (request.method == "POST"):# after submission:

        form = bookform(request.POST,request.FILES,instance=b)  # create form object initialized with values inside request.POST
        if form.is_valid():
            form.save()  # saves form object in db model Book
            return viewbooks(request)

    form=bookform(instance=b)
    return render(request,'edit.html',{'form':form})

def search(request):
    b=None
    q=""
    if(request.method=="POST"):
        q=request.POST['q']
        b=Book.objects.filter(Q(title__icontains=q)| Q(author__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})

@login_required
def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return viewbooks(request)






