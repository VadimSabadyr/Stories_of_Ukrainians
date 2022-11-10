from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import City, Author, Publication


@login_required
def index(request):
    """View function for the home page of the site."""

    num_authors = Author.objects.count()
    num_publications = Publication.objects.count()
    num_cities = City.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_authors": num_authors,
        "num_publications": num_publications,
        "num_cities": num_cities,
        "num_visits": num_visits + 1,
    }

    return render(request, "stories/index.html", context=context)
