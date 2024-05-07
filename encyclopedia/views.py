from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, entryName):
    return render(request, "encyclopedia/display.html", {
        "entry": util.get_entry(entryName),
        "title": entryName,
    })