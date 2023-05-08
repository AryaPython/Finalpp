from .import views
from django.urls import path

appname='schoolapp'

urlpatterns = [

    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout', views.logout, name="logout"),
    path('new',views.new,name="new"),
    path('base',views.base,name="base"),
    path('home',views.home,name="home"),

]
