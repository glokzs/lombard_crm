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

class AdminView(DetailView):
    template_name = 'admin_cabine.html'
    pk_url_kwarg = 'user_pk'
    # user_pk or pk
    model = User


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'


# def register_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             user.save()
#             login(request, user)
#             return redirect('webapp:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'user_create.html', context={'form': form})
