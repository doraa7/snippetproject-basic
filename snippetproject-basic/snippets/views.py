from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Snippet
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import SnippetFilter

class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = SnippetFilter(self.request.GET, queryset = self.get_queryset())
        return context
    


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'
