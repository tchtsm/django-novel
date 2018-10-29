from django.shortcuts import render
from book.models import Book

# Create your views here.
def content(request,code):
    res = Book.objects.get(code=code)
    return render(request,'web/content.html',{'content':res})