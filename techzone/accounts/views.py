from .models import Admin
from django.shortcuts import render

def dashboard_view(request):
    admins = Admin.objects.all()
    return render(request, 'dashboard/index.html', {'admins': admins})
def admins_list(request):
    return render(request, 'accounts/admins_list.html')