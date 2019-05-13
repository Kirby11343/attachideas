from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Profile


# Create your views here.
def signUp(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Аккаунт, {username}, был успешно создан.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/signUp.html', {'form': form})

# @login_required
# def profile(request):
# 	if request.method == 'POST':
# 		u_form = UserUpdateForm(request.POST, instance=request.user)
# 		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()
# 			messages.success(request, f'Изменения пришли в силу.')
# 			return redirect('profile')
# 	else:
# 		u_form = UserUpdateForm(instance=request.user)
# 		p_form = ProfileUpdateForm(instance=request.user.profile)

# 	context = {
# 		'u_form': u_form,
# 		'p_form': p_form
# 	}

# 	return render(request, 'users/profile.html', context)

class ProfileListView(ListView):
    model = Profile
    template_name = 'main/list_profiles.html' # type of path: <app>/<model>_<viewtype>.html
    context_object_name = 'profiles'
    ordering = ['-date']
    paginate_by = 5

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_edit.html'
    fields = ['image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Profile = self.get_object()
        if self.request.user == Profile.user:
            return True
        return False

