from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util


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
            return render(request, "encyclopedia/search.html", {
                "entries": tmp,
                "query": q,
            })
    else:
        return HttpResponseRedirect("/")