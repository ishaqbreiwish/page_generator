from django.urls import path
from . import views
from .views import ReactView


urlpatterns = [
    path('forms/', views.my_view, name='my_view'),
    path('success/', views.success_view, name='success'),
     path('api/react-form/', ReactView.as_view(), name='react_form_api'),
]
