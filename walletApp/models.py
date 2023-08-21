import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)

class Wallet(models.Model):
    user = models.CharField(max_length=150)
    balance = models.CharField(max_length=150)
    wallet_number = models.CharField(max_length=20, primary_key=True)


class Transaction(models.Model):
    TYPES = [
        ('NONE', 'None'),
        ('WITHDRAW', 'Withdraw'),
        ('DEPOSIT', 'Deposit'),
        ('TRANSFER', 'Transfer'),

    ]
    STATUS = [
        ('NONE', 'None'),
        ('SUCCESSFUL', 'Successful'),
        ('PENDING', 'Pending'),
        ('DECLINED', 'Declined'),

    ]

    type = models.CharField(max_length=50, choices=TYPES, default=None)
    status = models.CharField(max_length=50, choices=STATUS, default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    pk_reference_number = models.UUIDField(primary_key=True, default=uuid.UUID)