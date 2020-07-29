from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from designs.models import Design
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
	return render(request, 'designs/index.html')

class DesignCreateView(LoginRequiredMixin, CreateView):
	model=Design
	fields=['image_preview', 'title', 'description', 'file']
	template_name='designs/create.html'
	success_url='/designs'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class DesignListView(ListView):
	model=Design
	template_name='designs/index.html'
	ordering=['-datetime_posted']
	paginate_by=12

class DesignDetailView(DetailView):
	model=Design
	template_name='designs/detail.html'