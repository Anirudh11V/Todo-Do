from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('apptodo', views.TodoViewset, basename='todo')

urlpatterns = [
    # path('apitodo/', views.indexView.as_view()),
    # path('apitodo/<int:pk>/', views.Detailview.as_view()),

    path('', include(router.urls))
]