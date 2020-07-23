from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterationFrom, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
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
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	return render(request, 'users/profile.html', {
												'u_form':u_form,
												'p_form':p_form
												})
