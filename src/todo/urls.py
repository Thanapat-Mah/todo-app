from django.urls import path, re_path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.show_all_task, name='show_all_task'),
    path('update_task/<int:task_id>', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
]
