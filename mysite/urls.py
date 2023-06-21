from django.urls import path
from .import views


app_name = 'mysite'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail')
]
