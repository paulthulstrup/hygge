from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/profile/', views.profile, name='profile'),
    path('<int:user_id>/allocate/', views.allocate, name='allocate')
]
