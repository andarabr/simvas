from django.shortcuts import render
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "employee/dashboard.html")
    else:
        return redirect('/accounts/login/')
