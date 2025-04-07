from rest_framework import viewsets
from .models import Transaction, FraudReport, BankAccount, UserProfile
from .serializers import TransactionSerializer, FraudReportSerializer, BankAccountSerializer, UserProfileSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class FraudReportViewSet(viewsets.ModelViewSet):
    queryset = FraudReport.objects.all()
    serializer_class = FraudReportSerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer