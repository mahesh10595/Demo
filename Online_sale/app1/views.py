import json
import random

from django.shortcuts import render


# Create your views here.
def showindex(request):
    return render(request,"index.html")


def loginCheck(request):
    username = request.POST.get("uname")
    password = request.POST.get("pass")
    if username == "admin":
        if password == "admin":
            return render(request, "usercheck.html",{"message": "Welcome Admin"})
        else:
            return render(request, "index.html", {"message": "Incorrect PASSWORD"})
    else:
        return render(request, "index.html", {"message": "Incorrect USERNAME"})


def addMarchant(request):
    qs = MarchantModel.objects.all()
    return render(request, "addmarchant.html", {"data": qs})


from .models import MarchantModel
def saveMarchant(request):
    # id = request.POST.get("i")
    na = request.POST.get("n")
    con = request.POST.get("c")
    em = request.POST.get("e")
    # password = random.randint(10000,99999)
    res = MarchantModel.objects.values_list("idno")
    l = len(res)
    if l == 0:
        id = 1001
    else:
        id = res[l-1][0]+1

    try:
        pid=id
        pname=len(na)
        padd=str(pid+pname)
        pcon=list(con)
        pemail=em
        passwd = pemail[0]+padd[:2]+pcon[-1]+pemail[1]+pcon[0]+pemail[2]

        MarchantModel(idno=id,name=na,contact=con,email=em, password=passwd).save()
        qs = MarchantModel.objects.all()
        return render(request, "addmarchant.html", {"data": qs})
    except ValueError:
        qs = MarchantModel.objects.all()
        return render(request, "addmarchant.html", {"message": "invalid data"})

def deleteMarchant(request):
      mid = request.GET.get("id")
      MarchantModel.objects.filter(idno=mid).delete()
      qs = MarchantModel.objects.all()
      return render(request, "addmarchant.html", {"data": qs})

from django.views.generic import View
from  django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import MarchantForm,ProductForm
from django.core.serializers import serialize

@method_decorator(csrf_exempt, name='dispatch')
class MachantLogin(View):
    def post(self,request):
        data = request.body
        d1 = json.loads(data)
        print(d1)
        uname=d1['username']
        upass = d1['password']

        try:
            res = MarchantModel.objects.filter(email=uname, password=upass)
            print(res)
            msg = {"massage": "Valid Credentials"}
            json_data = json.dumps(msg)
            return HttpResponse(json_data, content_type="application/json",status=400)
        except:
            d1 = {"msg": "Invalid credentials"}
            json_data = json.dumps(d1)
            return HttpResponse(json_data, content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class Addproduct(View):
    def post(self,request):
        data = request.body
        d1 = json.loads(data)
        print(d1)
        print(type(d1))
        pf = ProductForm(d1)
        res = pf.save(commit=True)
        return HttpResponse(res)

