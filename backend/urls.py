from django.urls import path
from .views import task_list, create_task, task_detail

urlpatterns = [
    path('todo/', task_list, name='task-list'),
    path('todo/create/', create_task, name='create-task'),
    path('todo/<int:pk>/', task_detail, name='task_detail')
]