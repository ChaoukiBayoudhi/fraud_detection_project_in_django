from rest_framework import viewsets
from .models import Transaction, FraudReport, BankAccount, UserProfile
from .serializers import TransactionSerializer, FraudReportSerializer, BankAccountSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(methods=['GET'], detail=False)
    def get_account_transactions(self,request,account_id):
        account=BankAccount.objects.filter(id=account_id)
        if not account.exists():
            return Response(data={'message':f'The account with id = {account_id} is not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        #or using get_object_or_404()
        #account=get_object_or_404(BankAccount,id=account_id)
        transactions=BankAccount.objects.filter(bank_account=account)
        if not transactions.exists():
            return Response(data={'message':f'There is no transactions for the account with id = {account_id}.'},
                            status=status.HTTP_204_NO_CONTENT)
        #serilize the result
        result=TransactionSerializer(transactions,many=True)
        return Response(data=result.data,status=status.HTTP_200_OK)

    @action(
        # Specify that this endpoint only accepts GET requests
        methods=['GET'],
        # detail=False means this is a list action that doesn't operate on a single instance
        detail=False,
        # Define the URL pattern with regex to capture account_id as a number
        url_path='account-transactions-v2/(?P<account_id>[0-9]+)',
        # Define a unique name for this URL pattern for reverse lookup
        url_name='account_transactions_v2',
        # Restrict access to authenticated users only
        permission_classes=[IsAuthenticated],
        # Provide API documentation description
        description='Get all transactions for a specific bank account'
    )
    def get_account_transactions_v2(self, request, account_id):
        try:
            # Get the account or raise 404 if not found
            account = get_object_or_404(BankAccount, id=account_id)
            
            # Get all transactions for this account in a single query
            transactions = Transaction.objects.filter(bank_account=account)
            
            if not transactions.exists():
                return Response(
                    data={'message': f'No transactions found for account {account_id}'},
                    status=status.HTTP_204_NO_CONTENT
                )
            
            # Serialize the transactions
            serializer = TransactionSerializer(transactions, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                data={'message': f'Error retrieving transactions: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class FraudReportViewSet(viewsets.ModelViewSet):
    queryset = FraudReport.objects.all()
    serializer_class = FraudReportSerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer