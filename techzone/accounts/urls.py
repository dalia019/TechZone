from django.urls import path
from . import views

urlpatterns = [
   path('signup/', views.signup, name='signup'),  # صفحة التسجيل
    path('login/', views.login_view, name='login'),  # صفحة الدخول
    path('admins/', views.admins_list, name='admins_list'),  # قائمة المشرفين
    
]
