from django.shortcuts import render

# Create your views here.

@action(detail=True, methods=['post'])
    def transfer(self, sender_wallet_number, amount, receiver_wallet_number):
        sender = Wallet.objects.get(pk=sender_wallet_number)
        receiver = Wallet.objects.get(pk=receiver_wallet_number)

        transaction = Transaction.objects.create()
        transaction.transaction_type = 'TRANSFER'
        transaction.date_time = datetime.datetime.now()
        transaction.amount = amount
        transaction.wallet = sender
        transaction.reference_number = uuid.uuid4()

        if sender.balance > amount and sender.balance > 0:
            sender.balance -= amount
            receiver.balance += amount
            transaction.transaction_status = 'SUCCESSFUL'
            transaction.save()
            sender.save()
            receiver.save()

    @action(detail=True, methods=['post'])
    def deposit(self, amount, receiver_wallet_number):
        receiver = Wallet.objects.get(pk=receiver_wallet_number)

        transaction = Transaction.objects.create()
        transaction.transaction_type = 'DEPOSIT'
        transaction.date_time = datetime.datetime.now()
        transaction.amount = amount
        transaction.reference_number = uuid.uuid4()

        receiver.balance += amount
        transaction.transaction_status = 'SUCCESSFUL'
        transaction.save()
        receiver.save()
