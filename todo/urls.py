from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.AddTaskView.as_view(), name="create-task"),
    path('delete-task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete-task'),
    path('edit-task/<int:pk>/', views.EditTaskView.as_view(), name='edit-task'),
    path('complete/<int:pk>/', views.DoneTaskView.as_view(), name='done-task'),
]
