from rest_framework import routers
from .views import TransactionViewSet, FraudReportViewSet, BankAccountViewSet, UserProfileViewSet
from django.urls import path, include
router=routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'fraud-reports', FraudReportViewSet)
router.register(r'bank-accounts', BankAccountViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
#or
#urlpatterns =router.urls