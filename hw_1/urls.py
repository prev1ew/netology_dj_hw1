from django.urls import path, include
from .views import current_time, index, work_dir

urlpatterns = [
    path('', index, name='index'),
    path('current_time/', current_time, name='current_time'),
    path('work_dir/', work_dir, name='work_dir'),
]
