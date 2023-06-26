from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout')
]
