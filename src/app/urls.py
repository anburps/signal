from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_list, name='register_list'),
    path('register/create/', views.register_create, name='register_create'),
    path('register/<int:pk>/up', views.register_update, name='register_update'),
    path('register/<int:pk>/de', views.register_delete, name='register_delete'),
]