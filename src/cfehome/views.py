from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = Path(__file__).resolve().parent

queryset = PageVisit.objects.all()

def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count()
    }

    path = request.path
    print("Path", path)

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    # Use render to load the home.html template
    return render(request, html_template, my_context)
