from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')  # أو أي قالب HTML محتاج تستخدمه

