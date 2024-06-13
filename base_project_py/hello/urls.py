from django.urls import path
from .views import homePageView, say_hello

urlpatterns = [
    path('', homePageView, name='home'),
    path('2/',say_hello, name='sayhello')
]