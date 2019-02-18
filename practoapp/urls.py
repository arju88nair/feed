from django.urls import path

from . import views

urlpatterns = [
    path('doctors', views.DoctorList.as_view()),
    path('doctors/<int:pk>/detail', views.DoctorDetail.as_view()),
]