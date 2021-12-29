from django.urls import path
from . import views

urlpatterns = [
    path('',views.public),
    path('about/', views.about),
    path('user/',views.registration_form),
]