from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('salary/', views.salary, name="salary"),
    path('save/', views.save, name="save"),
    path('job/', views.job, name="job"),
    path('savejob/', views.save_job, name="save_job"),
    path('list/', views.list_salary, name="list"),
    path('id/<int:id>', views.id_salary, name="id_salary")
]
