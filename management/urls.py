from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
]
