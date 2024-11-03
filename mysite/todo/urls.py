from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', views.mark_complete, name='mark_complete'),
]
