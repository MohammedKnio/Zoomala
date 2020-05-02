from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Opportunity
from django.http import HttpResponseForbidden


class OpportunitiesListView(LoginRequiredMixin,ListView):
    
    template_name = "opportunities/opportunities.html"
    success_url='./'
    paginate_by= 25

    def get_queryset(self):
        searchParams = self.request.GET.get('q', None)
        if searchParams !=None:
            return Opportunity.objects.search_by_generic(searchParams)
        return Opportunity.objects.all().order_by('-date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        searchParams = self.request.GET.get('q', None)
        context['opportunities']= self.get_queryset()
        context['searchParams']= searchParams
        return context


