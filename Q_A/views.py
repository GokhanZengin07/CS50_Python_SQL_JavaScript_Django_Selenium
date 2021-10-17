from django.shortcuts import render
from .models import SC,Urun
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,"Q_A/index.html",{"SC":SC.objects.all(),"Urun":Urun.objects.all()})

def soru(request,soru_id):
    soru=SC.objects.get(id=soru_id)
    return render(request,"Q_A/soru.html",{
        "SC":SC.objects.all(),"Urun":Urun.objects.all()
        })

def book(request,soru_postid):
    if request.method=="POST":
        soru_postid =SC.objects.get(pk=soru_postid)
        answer=sc.SC.objects.get(pk=int(request.POST["answer"]))
        answer.question_text.add(answer)
        return HttpResponseRedirect(reverse("book"),args=(soru_postid))
        
