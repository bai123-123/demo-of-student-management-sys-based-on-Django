from django.shortcuts import render,HttpResponse
from app1 import models
# Create your views here.

def login(request):

    if request.method == "POST":
        name = request.POST.get('user')
        pwdd = request.POST.get('pwd')


        if name =="zrb" and pwdd =="123456":
            return render(request,"HomePage.html")


    return render(request,"login.html")


def get_students(request):
    stu_list = models.Students.objects.all()

    return render(request,"student_list.html",locals())

