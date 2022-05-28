from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index),
    path('create/', views.Create),
    path('feedback/', views.Feedback),
    path('index/', views.Index)
]