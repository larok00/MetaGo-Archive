from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    context = {}
    return render(request, 'MetaGo/index.html', context)

def photo_id(request):
    if request.method == "POST":
        raise KeyError(request.POST)
    else:
        return HttpResponseRedirect(reverse('MetaGo:index'))