from django.shortcuts import render
from book.models import Book
from django.db.models.aggregates import Count

# Create your views here.
def index(request):
    over = Book.objects.values('name','user','intro','type','score').filter(status='完结')
    count = Book.objects.filter(status='完结').aggregate(count=Count('id'))
    return render(request,'web/index.html',{'over':over,'overcount':count['count']})
