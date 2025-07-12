from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Link
from .forms import Link_form


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

def create_link(request):
    if request.method == 'POST':
        form = Link_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = Link_form()
    content = {
        "form": form
    }
    # form = Link_form()
    # content = {
    #     "form": form
    # }
    return render(request, "links/create.html", content)