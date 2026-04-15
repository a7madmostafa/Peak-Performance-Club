from django.shortcuts import render
from .models import Branch, Member, Trainer, GymClass, Equipment

# Create your views here.

def home(request):
    context = {
        "branches": Branch.objects.all(),
        "members": Member.objects.all(),
        "trainers": Trainer.objects.all(),
        "classes": GymClass.objects.all(),
        "equipment": Equipment.objects.all(),
    }
    return render(request, "home.html", context)

def branches(request):
    context = {
        "branches": Branch.objects.all(),
    }
    return render(request, "branches.html", context)

def members(request):
    context = {
        "members": Member.objects.all(),
    }
    return render(request, "members.html", context)

def trainers(request):
    context = {
        "trainers": Trainer.objects.all(),
    }
    return render(request, "trainers.html", context)

def classes(request):
    context = {
        "classes": GymClass.objects.all()
    }
    return render(request, "classes.html", context)

def equipments(request):
    context = {
        "equipments": Equipment.objects.all(),
    }
    return render(request, "equipments.html", context)

