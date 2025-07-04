from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/',include("django.contrib.auth.urls")),
    
    path('', views.home, name='hpage'),
    path("ed/<str:pk>/", views.Edit, name='edit'),
    path("del/<str:pk>/", views.delete, name='del'),
    path("signup/", views.authView, name='authView'),

    path('logout/', views.logout_user, name='logout')
]