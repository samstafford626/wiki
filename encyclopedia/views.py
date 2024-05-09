from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util
from django.contrib import messages
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def display(request, entryName):
    return render(request, "encyclopedia/display.html", {
        "entry": util.get_entry(entryName),
        "title": entryName,
    })

def search(request):
    if request.method == "POST":
        q = request.POST.get("q")
        entries = util.list_entries()
        
        if q in entries:
            return render(request, "encyclopedia/display.html", {
                "entry": util.get_entry(q),
                "title": q,
            })
        else:
            tmp = list()
            for entry in entries:
                if q.lower() in entry.lower():
                    tmp.append(entry)
            entries = tmp
            if not entries:
                entries = ["No results found"]
            return render(request, "encyclopedia/search.html", {
                "entries": entries,
                "query": q,
            })
    else:
        return HttpResponseRedirect("/")
    
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if not util.get_entry(title):
            util.save_entry(title, content)
        else:
            messages.error(request, "Entry already exists")
            return render(request, "encyclopedia/create.html")

        return HttpResponseRedirect(f"/display/{title}")
    else:

        return render(request, "encyclopedia/create.html")
    

def edit(request, entryName):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        util.save_entry(title, content)

        return HttpResponseRedirect(f"/display/{title}")
    else:
        return render(request, "encyclopedia/edit.html", {
            "entry": util.get_entry(entryName),
            "title": entryName,
        })
    

def randompage(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return HttpResponseRedirect(f"/display/{entry}")