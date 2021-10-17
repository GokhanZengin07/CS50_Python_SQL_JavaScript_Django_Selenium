from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"]
        })

def add(request):
    pass
