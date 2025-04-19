from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request):
    queryset = PageVisit.objects.filter(path=request.path)
    
    my_title = "CoinLaunch"
    my_context = {
        "title": my_title,
        "content": "Welcome to CoinLaunch!",
        "featured": True,
        "page_visit_count": queryset.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path) 
    return render(request, html_template, my_context)


def about_page_view(request):
    my_title = "About CoinLaunch"
    my_context = {
        "title": my_title,
        "content": "CoinLaunch is a platform for launching new cryptocurrencies.",
        "featured": True,
    }
    html_template = "about.html"
    
    return render(request, html_template, my_context)