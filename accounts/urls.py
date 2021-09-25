from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('userinfo_change/', views.userinfo_change, name="userinfo_change"),
    path('password/', views.password, name="password"),
    path('delete/', views.delete, name="delete"),
]