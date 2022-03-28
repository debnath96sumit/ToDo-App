from django.shortcuts import render

from django.http import HttpResponse
import mysql.connector as sql
# Create your views here.
em = ''
pswd = ''
def login(request):
    global em, pswd
    if request.method =='POST':
        database = sql.connect(host = 'localhost', user = 'root' ,password = '12345', database = 'youtube')
        cursor = database.cursor()
        data = request.POST
        for key, value in data.items():
            if key == 'email':
                em = value
            if key == 'password':
                pswd = value
        c = "select * from student where email = '{}' and password = '{}'".format( em, pswd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t !=():
            return render(request, 'index.html')
        else:
            return render(request, 'error.html')
                
    return render(request, 'login.html')
