from django.urls import path

from . import views
app_name='quiz'
urlpatterns=[
     path('', views.IndexView.as_view(), name='index'),
      path('/register', views.RegView.as_view(), name='register'),
       path('/login', views.LoginView.as_view(), name='login'),

]