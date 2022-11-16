from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (CitySearchForm, PublicationSearchForm,
                    PublicationForm, AuthorSearchForm,
                    AuthorPseudonymUpdateForm, AuthorCreationForm)
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


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    context_object_name = "city_list"
    template_name = "stories/city_list.html"
    paginate_by = 5
    queryset = City.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = CitySearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = CitySearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class CityCreateView(LoginRequiredMixin, generic.CreateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("stories:city-list")


class CityUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("stories:city-list")


class CityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy("stories:city-list")


class PublicationListView(LoginRequiredMixin, generic.ListView):
    model = Publication
    context_object_name = "publication_list"
    template_name = "stories/publication_list.html"
    paginate_by = 2
    queryset = Publication.objects.all().select_related("city")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = PublicationSearchForm(initial={"title": title})

        return context

    def get_queryset(self):
        form = PublicationSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )

        return self.queryset


class PublicationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Publication


class PublicationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy("stories:publication-list")


class PublicationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy("stories:publication-list")


class PublicationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Publication
    success_url = reverse_lazy("stories:publication-list")


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 10
    queryset = Author.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = AuthorSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        form = AuthorSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return self.queryset


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    queryset = Author.objects.all().prefetch_related("publications__city")


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm
    success_url = reverse_lazy("stories:author-list")


class AuthorPseudonymUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    form_class = AuthorPseudonymUpdateForm
    success_url = reverse_lazy("stories:author-list")


class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Author
    success_url = reverse_lazy("stories:author-list")


@login_required
def toggle_assign_to_publication(request, pk):
    author = Author.objects.get(id=request.user.id)
    if (
        Publication.objects.get(id=pk) in author.publications.all()
    ):
        author.publications.remove(pk)
    else:
        author.publications.add(pk)
    return HttpResponseRedirect(reverse_lazy("stories:publication-detail", args=[pk]))
