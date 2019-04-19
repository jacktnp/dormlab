from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('annouce/', views.user_annouce, name='user_annouce'),
    path('bill/', views.user_bill, name='user_bill'),
    path('payment/', views.user_payment, name='user_payment'),
    path('report/', views.user_report, name='user_report'),
]
