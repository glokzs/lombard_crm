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
    path('operations/', OperationListView.as_view(), name='operation_list'),
    path('subcategories/', SubcategoryListAjaxView.as_view(), name='subcategory_list_ajax'),
    path('criteria_list/', CriteriaListAjaxView.as_view(), name='criteria_list_ajax'),
    path('loan/calculate/', LoanCalculateAjaxView.as_view(), name='loan_calculate_ajax'),
    path('loans/<int:loan_pk>/', LoanDetailView.as_view(), name='loan_detail'),
    path('clients/<int:client_pk>/loans/create/', LoanCreateView.as_view(), name='loan_create'),
    path('pledge_items/create/', PledgeItemCreateAjaxView.as_view(), name='pledge_item_create_ajax'),
    path('pledge_items/', PledgeItemListView.as_view(), name='pledge_items'),
    path('criteria_list/create/', CriteriaValueCreateAjaxView.as_view(),
      name='criteria_value_create_ajax'),
    path('loans/<int:loan_pk>/ticket/', TicketDownloadView.as_view(), name='loan_ticket'),
    path('loans/<int:loan_pk>/buyout/', LoanBuyoutView.as_view(), name='loan_buyout'),
    path('loans/<int:loan_pk>/prolongation/', LoanProlongationView.as_view(), name='loan_prolongation'),
)
