from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from encyclopedia import util

class EntryForm(forms.Form):
    title=forms.CharField(label='Title:')
    content=forms.CharField(label='Type content in Markdown:', widget=forms.Textarea(attrs={'rows':5}))

def add (request):
    entries=util.list_entries()
    for i in range(0,len(entries)-1):
        entries[i]=entries[i].lower()
    if request.method=='POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            title=title.capitalize()
            content=form.cleaned_data["content"]
            entry=f"#{title}\n\n {content}"

            if title.lower() in entries:
                return render(request, 'newEntry/add.html',{
                'form':form,
                'message':"Article with that title already exists!"
                })
            else:
                util.save_entry(title, entry)
                return HttpResponseRedirect(reverse('entry:index', args=[title]))


    return render(request, 'newEntry/add.html',{
    'form':EntryForm,
    })
