from django.urls import path

from . import views
app_name='quiz'
urlpatterns=[
      path('register/',views.register_user),
      #path('signin/',views.signin_user),
]