from django.urls import path
from .views import *

app_name = 'pawnshop'

urlpatterns = [
    path('clients/list/', ClientListAjaxView.as_view(), name='client_list_ajax'),
    path('clients/', ClientDetailAjaxView.as_view(), name='client_detail_ajax'),
    path('confirm_documents/create/', ConfirmDocumentCreateView.as_view(), name='confirm_document_create'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:client_pk>/choose/', ClientChooseView.as_view(), name='client_choose'),
    path('credits/', CreditListView.as_view(), name='credit_list'),
    path('pledge_items/create/', PledgeItemCreateView.as_view(), name='pledge_item_create'),
    path('subcategories/', SubcategoryDetailAjaxView.as_view(), name='subcategory_detail_ajax'),
    path('loan/calculate/', LoanCalculateAjaxView.as_view(), name='loan_calculate_ajax'),
    path('loan/create/', LoanCreateView.as_view(), name='loan_create'),
]
