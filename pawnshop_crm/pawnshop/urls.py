from django.urls import path
from .views import *

app_name = 'pawnshop'

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('clients/list/', ClientListAjaxView.as_view(), name='client_list_ajax'),
    path('clients/', ClientDetailAjaxView.as_view(), name='client_detail_ajax'),
    path('clients/<int:client_pk>/confirm_documents/create/', ConfirmDocumentCreateView.as_view(),
         name='confirm_document_create'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/choose/', ClientChooseView.as_view(), name='client_choose'),
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('clients/<int:client_pk>/pledge_items/create/', PledgeItemCreateView.as_view(), name='pledge_item_create'),
    path('subcategories/', SubcategoryDetailAjaxView.as_view(), name='subcategory_detail_ajax'),
    path('loan/calculate/', LoanCalculateAjaxView.as_view(), name='loan_calculate_ajax'),
    path('clients/<int:client_pk>/pledge_items/<int:pledge_item_pk>/loans/create/', LoanCreateView.as_view(),
         name='loan_create'),
    path('clients/<int:client_pk>/pledge_items/<int:pledge_item_pk>/criteria_list/create/',
         CriteriaValueCreateView.as_view(), name='criteria_value_create'),
)
