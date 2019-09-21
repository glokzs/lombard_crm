from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.shortcuts import redirect, render


#
# def user_login_view(request):
#     context = {}
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         next_url = request.POST.get('next')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             if next_url:
#                 return redirect(next_url)
#             return redirect('pawnshop:credits')
#         else:
#             context['has_error'] = True
#             context['next'] = next_url
#             context['email'] = email
#     else:
#         context = {'next': request.GET.get('next')}
#     return render(request, 'registration/login.html', context=context)
from accounts.models import User


def user_login_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = User.objects.get(email__exact=f'{email}').username
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(f'user {user}')
        print (f'when user changed password: {user.initial_password_changed_at}')
        if user:
            login(request, user)
            return redirect('accounts:login')
        else:
            context['has_error'] = True
    return render(request, 'user/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


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
