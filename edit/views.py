from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from encyclopedia import util
from newEntry.views import EntryForm


def edit (request, title):
    entries=util.list_entries()
    for i in range(0,len(entries)-1):
        entries[i]=entries[i].lower()
    if request.method=='POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            content=form.cleaned_data["content"]
            entry=f"#{title}\n\n {content}"
            if title.lower() in entries:
                util.save_entry(title, entry)
                return HttpResponseRedirect(reverse('entry:index', args=[title]))
            else:
                message='This page does not exist'
                return render(request, 'edit/edit.html',{
                    'form':form,
                    'title':title,
                    'message':message,

                    })
    item = util.get_entry(title)
    item = str(item).split(" ")
    form = EntryForm({'title': title, 'content':" ".join(item[1:])})
    return render(request, 'edit/edit.html',{
        'form':form,
        'title':title,

        })
