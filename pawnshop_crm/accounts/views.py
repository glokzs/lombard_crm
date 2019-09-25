from django.contrib.auth import login, authenticate, logout

# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from accounts.forms import UserForm
from accounts.models import User


def user_login_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            username = User.objects.get(email__exact=f'{email}').username
        except:
            context['has_error'] = True
            return render(request, 'user/login.html', context=context)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('accounts:login')
        else:
            context['has_error'] = True
    return render(request, 'user/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class UserDetailView(ListView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name = 'user/create.html'
    model = User
    form_class = UserForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            last_name=data['last_name'],
            email=data['email'],
            user_type=data['user_type'],

        )
        self.object = user
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'user_pk': 1})
