from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.Home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
]
