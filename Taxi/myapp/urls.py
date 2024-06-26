from django.urls import path
from . import views
from .views import register, login_view
from .views import admin_dashboard, driver_dashboard, client_dashboard



urlpatterns = [
    path("",views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('driver_dashboard/', driver_dashboard, name='driver_dashboard'),
    path('client_dashboard/', client_dashboard, name='client_dashboard'),
    
    
]