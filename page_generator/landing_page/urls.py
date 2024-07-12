from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.my_view, name='my_view'),
    path('success/', views.success_view, name='success'),
]
