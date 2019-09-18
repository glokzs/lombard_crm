from django.urls import path
from .views import *

app_name = 'pawnshop'

urlpatterns = [
    path('credits/', CreditListView.as_view(), name='credit_list'),
    path('credits/create/', CreditCreateView.as_view(), name='credit_create'),
]
