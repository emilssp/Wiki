from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from random import randint
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def randomEntry(request):
    entryList=util.list_entries()
    idx=randint(0,len(entryList)-1)
    return HttpResponseRedirect(reverse('entry:index', args=[entryList[idx]]))
