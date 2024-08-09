
from django.core.paginator import EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import AuthorForm, BookForm
# Create your views here.
from .models import Book


def listbook(request):

    books=Book.objects.all()


    return render(request,'listbook.html',{'books':books}
                  )

def specificbook(request,books_id):
    books=Book.objects.get(id=books_id)

    return render(request,'specificbook.html',{'books':books})



def updatebook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form= BookForm(request.POST,files=request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BookForm()
        return render(request,'book.html',{'form':form})


def deletebook(request,book_id):
    book=Book.objects.get(id=book_id)

    if request.method=='POST':
      book.delete()
      return redirect('/')

    return render(request,'deletebook.html',{'book':book})

def createbook(request):
    books=Book.objects.all()

    if request.method=='POST':
        form= BookForm(request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= BookForm()
    return render(request,'book.html',{'form':form,'books':books})

def createauthor(request):
    if request.method=='POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form= AuthorForm()
    return render(request,'author.html',{'form':form})

def new_index(request):
    return render(request,'base.html')

def Search_Book(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}

    return render(request,'search.html',context)



