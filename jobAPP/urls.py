from django.urls import path
from . import views


app_name = 'jobAPP'

urlpatterns = [
# post views
    path('', views.job_list, name='job_list'),
    path('<int:id>/', views.job_detail, name='job_detail'),
    path('<int:post_id>/application/', views.post_application, name='post_application'),
]