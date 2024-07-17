from django.urls import path
from .views import ReactView


urlpatterns = [
     path('api/react-form/', ReactView.as_view(), name='react_form_api'),
]
