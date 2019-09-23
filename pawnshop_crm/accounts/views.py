from django.contrib.auth import login, authenticate, logout

# Create your views here.
from django.shortcuts import redirect, render


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



# class UserListAjaxView(View):
#     def get(self, request, *args, **kwargs):
#         query = self.request.GET.get('query')
#         first_name_query = Q(first_name__icontains=query)
#         middle_name_query = Q(first_name__icontains=query)
#         last_name_query = Q(last_name__icontains=query)
#
#         iin_query = Q(confirm_document__iin__icontains=query)
#         users = User.objects.filter(first_name_query | last_name_query | iin_query)
#
#         data = {
#             'users': []
#         }
#         if not query:
#             return JsonResponse(data)
#
#         for user in users:
#             user_object = {
#                 'pk': user.pk,
#                 'first_name': user.first_name,
#                 'last_name': user.last_name,
#                 'middle_name': user.middle_name,
#                 'birth_date': user.birth_date,
#                 'iin': user.confirm_document.iin
#             }
#             data['users'].append(user_object)
#         return JsonResponse(data)

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
