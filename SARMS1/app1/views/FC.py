from django.shortcuts import render,HttpResponse,redirect
from app1 import models
# Create your views here.



def get_fc(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        st =models.Students.objects.filter(student_ID=nid).first()
        fc = models.FC.objects.filter(id=st.student_AP_id).first()

        return render(request, "FC.html", locals())


def edit_fc(request):

    if request.method == "GET":
        nid = request.GET.get('nid')
        st = models.Students.objects.filter(student_ID=nid).first()
        fc = models.FC.objects.filter(id=st.student_AP_id).first()

        return render(request, "edit_FC.html", locals())
    elif request.method == "POST":
        nid = request.POST.get("id")
        f = request.POST.get("fd")
        c = request.POST.get("co")



        models.FC.objects.filter(id = nid).update(
            feedback = f,
            comments = c,
        )






        return redirect("/FC/?nid= {}".format(nid))
