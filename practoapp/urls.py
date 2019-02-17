from django.urls import path

from . import views

urlpatterns = [
    path('', views.DoctorList.as_view()),
    path('<int:pk>/', views.DoctorDetail.as_view()),
]