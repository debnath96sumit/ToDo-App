from django.shortcuts import redirect, render

from django.http import HttpResponse
import mysql.connector as sql
# Create your views here.
fn = ''
ln = ''
em = ''
pswd = ''
def signup(request):
    global fn, ln, em, pswd
    context = {'success' : False, "name" :"Sumit"}
    if request.method =='POST':
        database = sql.connect(host = 'localhost', user = 'root' ,password = '12345', database = 'youtube')
        cursor = database.cursor()
        data = request.POST
        for key, value in data.items():
            if key =='firstname':
                fn = value
            if key =='lastname':
                ln = value
            if key =='email':
                em = value
            if key == 'password':
                pswd = value
            c = "Insert into student values('{}', '{}', '{}', '{}')".format(fn, ln, em, pswd)
            cursor.execute(c)
            database.commit()
        # return render(request, 'login.html')
        context = {'success' : True}
    return render(request, 'signup.html', context)
    
