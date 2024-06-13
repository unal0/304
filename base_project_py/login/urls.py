from django.urls import path
from .views import login_home, login_view, signup_view, login_home
from . import views

urlpatterns = [
    path('', login_home, name='login_home'),
    path('login/', login_view, name='login'),
    path('hello/', login_home, name='hello'),
    path('sign_up/', signup_view, name='patient_signup'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
]



