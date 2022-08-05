from multiprocessing import context
from sqlite3 import Cursor
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    # return HttpResponse("hello world")
    cursor = connection.cursor()
    cursor.execute("SELECT * from post where softdelete = 0")
    columns = [col[0] for col in cursor.description]
    post =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    # print(post)
    context = {
        'keyposts' : post
    }
    return render(request,'productapp/home.html',context)

def create(request):
    return render(request,'productapp/form.html')

def insert(request):
    name = request.POST['name']
    summary = request.POST['summary']
    color = request.POST['color']
    size = request.POST['size']
    price = request.POST['price']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO post (`name`,`summary`,`color`,`size`,`price`) VALUES ( %s, %s, %s, %s, %s );", (name, summary, color, size, price))
    cursor = connection.cursor()
    cursor.execute("SELECT * from post where softdelete = 0")
    print(request)
    return redirect('/product/home')

