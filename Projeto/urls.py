from django.urls import path
from .import views

urlpatterns = [
    path('',views.raissa),
    path('evlyn',views.evlyn),
]