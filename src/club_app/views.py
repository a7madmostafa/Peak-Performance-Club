from django.shortcuts import render
from .models import Branch, Member, Trainer, GymClass, Equipment
from django.db.models import Count

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
    base_qs = (
                GymClass.objects
                .select_related("trainer")
                .prefetch_related("members")
                .annotate(num_members=Count("members"))
            )

    context = {
                "classes": base_qs,
                "trending_classes": base_qs.trending(),
            }
    return render(request, "classes.html", context)

def equipments(request):
    context = {
        "equipments": Equipment.objects.all(),
    }
    return render(request, "equipments.html", context)

