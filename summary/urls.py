from django.urls import path
from .import views

app_name = 'summary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('txt/', views.file_download_view, name='txt'),
]
