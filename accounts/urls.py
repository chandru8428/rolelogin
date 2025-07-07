from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # 👈 this handles the root URL
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('user-home/', views.user_home, name='user_home'),
]
