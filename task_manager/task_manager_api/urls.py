from django.urls import path
from .views import ListTaskView, DetailTaskView, ListTaskViewFilter

urlpatterns = [
    path("tasks/<int:task_id>", DetailTaskView.as_view(), name='detail-task'),
    path('tasks/<str:filter_str>', ListTaskViewFilter.as_view(), name='task-list-filtered'),
    path('tasks', ListTaskView.as_view(), name='task-list'),
]
