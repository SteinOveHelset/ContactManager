from django.urls import path

from . import views

app_name='contact'
urlpatterns = [
    path('add/', views.add, name='add'),
    path('contacts/<int:pk>/', views.edit, name='edit'),
    path('contacts/<int:pk>/delete/', views.delete, name='delete'),
]