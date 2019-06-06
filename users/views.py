from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FileFieldForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Profile
from django.views.generic.edit import FormView

from django.contrib.auth.models import User
from homepage.models import Post


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

class ProfileListView(ListView):
    model = Profile
    template_name = 'main/list_profiles.html' # type of path: <app>/<model>_<viewtype>.html
    context_object_name = 'profiles'
    ordering = ['-date']
    paginate_by = 15

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        field_name = 'id'
        obj = self.get_object()
        field_object = Profile._meta.get_field(field_name)
        field_value = field_object.value_from_object(obj)

        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['user_content'] = Post.objects.filter(author=field_value).order_by('-date')
        return context

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.object.filter(author=user).order_by('-date.posted')

    # def get_object(self):
    #     return get_object_or_404(Profile, slug__iexact=self.kwargs['slug'])

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

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'users/profile_edit.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# class UserPostListView(ListView): #sort by Username
#     model = Post
#      # type of path: <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date']
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.object.filter(author=user).order_by('-date.posted')