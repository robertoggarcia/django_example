from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('payments', views.payments, name='payments'),
]
