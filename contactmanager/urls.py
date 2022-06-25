from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]
