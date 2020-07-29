from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterationFrom, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import os
# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterationFrom(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account has been created. Please Log in.')
			return redirect('login')
	else:
		form = UserRegisterationFrom()
	return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
	designs = request.user.design_set.all().order_by('-datetime_posted')
	paginator = Paginator(designs, 10)
	page_number = request.GET.get('page')
	page_obj =	paginator.get_page(page_number)
	return render(request, 'users/profile.html', { 'designs' : designs, 'page_obj' : page_obj })

@login_required
def edit_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,
								   instance=request.user.profile
								   )
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, 'Profile updated successfully.')
			return redirect('edit-profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	return render(request, 'users/edit-profile.html', {
												'u_form':u_form,
												'p_form':p_form
												})
