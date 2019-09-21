from django.urls import path
from .views import *

app_name = 'pawnshop'

urlpatterns = [
    path('clients/list/', ClientListAjaxView.as_view(), name='client_list_ajax'),
    path('clients/', ClientDetailAjaxView.as_view(), name='client_detail_ajax'),
    path('clients/<int:client_pk>/confirm_document_create/', ConfirmDocumentCreateView.as_view(), name='confirm_document_create'),
    path('credits/', CreditListView.as_view(), name='credit_list'),
    path('credits/client_create/', ClientCreateView.as_view(), name='client_create'),
    path('pledge_items/create/', PledgeItemCreateView.as_view(), name='pledge_item_create'),
]
