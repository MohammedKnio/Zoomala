from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from profiles.models import Profile
from .forms import ComposeForm


class SearchProfileView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'searchProfile/searchProfile.html'
    form_class = ComposeForm
    success_url = './'
    paginate_by= 25

    def get_queryset(self,*args, **kwargs):
        request = self.request
        searchParams = request.GET.get('q', None)
        if searchParams !=None:
            return Profile.objects.search(searchParams)
        return Profile.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searchParams = self.request.GET.get('q', None)
        context['form'] = self.get_form()
        context['profiles'] = self.get_queryset()
        context['searchParams'] = searchParams
        return context

    # def get(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()
    #     self.object = self.get_object_list()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # def form_valid(self, form):
    #     thread = self.get_object()
    #     user = self.request.user
    #     message = form.cleaned_data.get("message")
    #     return super().form_valid(form)