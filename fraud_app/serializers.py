from rest_framework import serializers
from .models import Transaction, FraudReport, BankAccount, UserProfile

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class FraudReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudReport
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'


class FraudReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudReport
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


