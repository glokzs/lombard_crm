from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views import UserDetailView, UserCreateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('create/', UserCreateView.as_view(), name='create')
]
