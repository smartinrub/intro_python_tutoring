from django.urls import path

from . import views

urlpatterns = [
    path('uppercase/<str:name>/', views.toUpperCase),
]
