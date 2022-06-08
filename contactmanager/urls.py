from django.contrib import admin
from django.urls import path, include

from core.views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]
