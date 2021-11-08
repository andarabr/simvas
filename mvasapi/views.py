from django.shortcuts import render
from django.shortcuts import redirect, render
from mvasapi.models import Transaction

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.all().order_by('id');
        context = {'transactions' : transactions}
        return render(request, "mvasapi/index.html", context)
    else:
        return redirect('/accounts/login/')
