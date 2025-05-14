from django.urls import path
from . import views

urlpatterns = [
    path('admins/', views.admins_list, name='admins_list'),
]
