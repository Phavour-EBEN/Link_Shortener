from django.shortcuts import render, get_object_or_404, redirect
from .models import Link


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }
    return render(request, "links/index.html", context)

def root_link(request, slug_link):
    link = get_object_or_404(Link, slug=slug_link)
    link.click()
    
    return redirect(link.original_url)