from standarize import views

from django.urls import path

urlpatterns = [
    path('standarize/', views.StandarizerView.as_view(), name="standarize"),
]
