from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import User
from pprint import pprint

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            users = User.objects.select_related('employee').order_by('id');
            # pprint(users)
            context = {'users' : users}
            return render(request, "employee/dashboard.html", context)
        else:
            return redirect('index-report')
    else:
        return redirect('/accounts/login/')

def reset_pass(id):
    return "test"
