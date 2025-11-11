from django.urls import path

from . import views

app_name = 'drinks_counter'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.drink_display, name='drink_display'),
]
