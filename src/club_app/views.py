from django.shortcuts import render
from .models import Branch, Member, Trainer, GymClass, Equipment

# Create your views here.

def home(request):
    return render(request, "home.html")

def branches(request):
    context = {
        "branches": Branch.objects.all(),
    }
    return render(request, "branches.html", context)

def members(request):
    context = {
        "members": Member.objects.select_related("branch").all(),
    }
    return render(request, "members.html", context)

def trainers(request):
    context = {
        "trainers": Trainer.objects.select_related("branch").all(),
    }
    return render(request, "trainers.html", context)

def classes(request):
    context = {
        "classes": GymClass.objects.select_related("trainer").prefetch_related("members").all(),
        "trending_classes": GymClass.objects.trending().select_related("trainer").prefetch_related("members").all(),    
    }
    return render(request, "classes.html", context)

def equipments(request):
    context = {
        "equipments": Equipment.objects.all(),
    }
    return render(request, "equipments.html", context)

