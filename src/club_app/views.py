from django.shortcuts import render
from .models import Branch

# Create your views here.

def branches(request):
    context = {
        "branches": Branch.objects.all(),
    }
    return render(request, "branches.html", context)
