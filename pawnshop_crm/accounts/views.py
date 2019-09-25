from django.contrib.auth import login, authenticate, logout

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

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

class UserDetailView(DetailView):
    template_name = 'user/detail.html'
    pk_url_kwarg = 'user_pk'
    model = User
