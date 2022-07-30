from django.shortcuts import render
from django.http import HttpResponse
from encyclopedia import util
import markdown2


def index(request, title):
    return render(request, "entry/index.html",{
    'title':title.upper(),
    'entry':markdown2.markdown(util.get_entry(title)),
    })
