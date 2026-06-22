from django.contrib import admin
from django.urls import path
from headless_api.views import run_task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/run-task/', run_task_view, name='run_task'),
]
