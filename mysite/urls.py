from django.urls import path
from .import views


app_name = 'mysite'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', views.CreateBlogView.as_view(), name='blog_new'),
    path('blog/<int:pk>/edit/', views.BlogEditView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('about/', views.AboutView.as_view(), name='about')
]
