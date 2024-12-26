from django.shortcuts import render

from django.db.models import Sum
from tracker.models import Transaction

# Create your views here.
from django.shortcuts import render, redirect
from tracker.models import Transaction

from django.shortcuts import render
from tracker.models import Transaction

def index(request):
    error_message = ''
    success_message = ''
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        print(description, amount)
        if not description or not amount:
            error_message = 'Description and Amount cannot be empty.'
        else:
            Transaction.objects.create(description=description, amount=amount)
            success_message = 'Transaction added successfully.'
    
    context = {
        'transactions': Transaction.objects.all(),
        'error_message': error_message,
        'success_message': success_message,
        'balance': Transaction.objects.all().aggregate(total_balance=Sum('amount'))['total_balance'] or 0,
        'income': Transaction.objects.filter(amount__gt=0).aggregate(total_income=Sum('amount'))['total_income'] or 0,
        'expense': Transaction.objects.filter(amount__lt=0).aggregate(total_expense=Sum('amount'))['total_expense'] or 0,
    }
    return render(request, 'index.html', context)

def delete_transaction(request, uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect('/')