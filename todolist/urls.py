from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.index, name = "list"),
    path('update_task/<int:pk>/', views.update_task, name ="update_task"),
    path('deleteTasks/<int:pk>/', views.deleteTasks, name ="deleteTasks")
]
