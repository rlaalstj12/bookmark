from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkCreateView(ListView):
    model = Bookmark


class BookmarkListView(CreateView):
    model = Bookmark
    fields = ["site_name", "url"]
    success_url = reverse_lazy("list")

    template_name_suffix = "_create"


class BookmarkDetailView(DeleteView):
    model = Bookmark
