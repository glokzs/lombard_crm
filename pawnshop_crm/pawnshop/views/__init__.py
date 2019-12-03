from .client_views import ClientCreateView, ClientChooseView, ClientDetailAjaxView, ClientListAjaxView
from .confirm_document_views import ConfirmDocumentCreateView
from .pledge_item_views import PledgeItemCreateView, PledgeItemCreateAjaxView, PledgeItemListView
from .subcategory_views import SubcategoryListAjaxView
from .loan_views import LoanCalculateAjaxView, LoanCreateView, LoanListView, LoanListAjaxView, LoanDetailView, \
    LoanBuyoutView, LoanProlongationView, LoanProlongationCalculateAjaxView
from .criteria_views import CriteriaValueCreateView, CriteriaValueCreateAjaxView, CriteriaListAjaxView
from .index_views import IndexView
from .operation_views import OperationListView
from .ticket_views import TicketDownloadView
