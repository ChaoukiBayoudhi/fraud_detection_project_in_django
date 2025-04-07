# Generated by Django 5.2 on 2025-04-07 13:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BankAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "account_number",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{10,20}$", "Enter a valid account number."
                            )
                        ],
                    ),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("currency_type", models.CharField(max_length=10)),
                (
                    "account_status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=10,
                    ),
                ),
            ],
            options={
                "db_table": "bank_account",
                "ordering": ["account_number"],
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0.01)],
                    ),
                ),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[
                            ("deposit", "Deposit"),
                            ("withdrawal", "Withdrawal"),
                            ("transfer", "Transfer"),
                        ],
                        max_length=20,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("location", models.CharField(max_length=255)),
                (
                    "bank_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="fraud_app.bankaccount",
                    ),
                ),
            ],
            options={
                "db_table": "transaction",
                "ordering": ["-timestamp"],
            },
        ),
        migrations.CreateModel(
            name="FraudReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reason_for_suspicion", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("reviewed", "Reviewed")],
                        default="pending",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "reported_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fraud_reports",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fraud_reports",
                        to="fraud_app.transaction",
                    ),
                ),
            ],
            options={
                "db_table": "fraud_report",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                (
                    "phone_number",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\+?[0-9]{9,15}$", "Enter a valid phone number."
                            )
                        ],
                    ),
                ),
                ("address", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_profile",
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="TransactionAlert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "alert_type",
                    models.CharField(
                        choices=[
                            ("ai_generated", "AI Generated"),
                            ("manual_review", "Manual Review"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "severity",
                    models.CharField(
                        choices=[
                            ("low", "Low"),
                            ("medium", "Medium"),
                            ("high", "High"),
                        ],
                        max_length=10,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alerts",
                        to="fraud_app.transaction",
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alerts",
                        to="fraud_app.userprofile",
                    ),
                ),
            ],
            options={
                "db_table": "transaction_alert",
                "ordering": ["-timestamp"],
            },
        ),
        migrations.AddField(
            model_name="bankaccount",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bank_accounts",
                to="fraud_app.userprofile",
            ),
        ),
    ]
