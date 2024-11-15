from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:id>/edit/', views.task_update, name='task_update'),
    path('task/<int:id>/delete/', views.task_delete, name='task_delete'),
]
