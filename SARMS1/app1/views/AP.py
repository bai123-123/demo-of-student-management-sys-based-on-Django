from django.shortcuts import render,HttpResponse,redirect
from app1 import models
# Create your views here.



def get_ap(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        print(nid)
        st =models.Students.objects.filter(student_ID= nid).first()
        ap = models.AP.objects.filter(AP_id=st.student_AP_id).first()

        return render(request, "PA.html", locals())


def edit_ap(request):

    if request.method == "GET":
        nid = request.GET.get('nid')
        stu = models.Students.objects.filter(student_ID=nid).first()
        ap = models.AP.objects.filter(AP_id=nid).first()

        return render(request, "edit_PA.html", locals())
    elif request.method == "POST":
        id = request.POST.get("id")
        w1a = request.POST.get("w1a")
        w1p = request.POST.get("w1p")
        w2a = request.POST.get("w2a")
        w2p = request.POST.get("w2p")
        w3a = request.POST.get("w3a")
        w3p = request.POST.get("w3p")
        w4a = request.POST.get("w4a")
        w4p = request.POST.get("w4p")
        w5a = request.POST.get("w5a")
        w5p = request.POST.get("w5p")
        w6a = request.POST.get("w6a")
        w6p = request.POST.get("w6p")
        w7a = request.POST.get("w7a")
        w7p = request.POST.get("w7p")
        w8a = request.POST.get("w8a")
        w8p = request.POST.get("w8p")
        w9a = request.POST.get("w9a")
        w9p = request.POST.get("w9p")
        w10a = request.POST.get("w10a")
        w10p = request.POST.get("w10p")


        models.AP.objects.filter(AP_id=id).update(
            week1_p=w1p,
            week1_A=w1a,
            week2_p=w2p,
            week2_A=w2a,
            week3_p=w3p,
            week3_A=w3a,
            week4_p=w4p,
            week4_A=w4a,
            week5_p=w5p,
            week5_A=w5a,
            week6_p=w6p,
            week6_A=w6a,
            week7_p=w7p,
            week7_A=w7a,
            week8_p=w8p,
            week8_A=w8a,
            week9_p=w9p,
            week9_A=w9a,
            week10_p=w10p,
            week10_A=w10a,



        )


        return redirect("/AP/?nid={}".format(id))



