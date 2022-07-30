from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from encyclopedia import util

class SearchForm(forms.Form):
    q=forms.CharField()

def index(request):
    entryList=util.list_entries()
    for i in range(0,len(entryList)):
        entryList[i]=entryList[i].lower()

    items=[]

    if request.method == 'POST':
        res = SearchForm(request.POST)
        if res.is_valid():
            res=res.cleaned_data['q']
            if str(res).lower() in entryList:
                return HttpResponseRedirect(reverse('entry:index', args=[str(res)]))
            for entry in entryList:
                if str(res) in entry:
                    items.append(entry)
    return render(request, "search/index.html", {
        "results": items,
    })
