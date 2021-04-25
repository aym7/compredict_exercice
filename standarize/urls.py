from standarize import views

from django.urls import path

urlpatterns = [
    path('standarize/', views.Standarizer.as_view(), name="standarize"),
]
