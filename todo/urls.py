from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.AddTaskView.as_view(), name="create-task"),
    # path("all/", views.TaskListView.as_view(), name="all-tasks"),
    path('delete-task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),

]
