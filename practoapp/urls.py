from django.urls import path

from . import views

urlpatterns = [
    path('doctors', views.DoctorList.as_view()),
    path('doctors/<int:pk>/detail', views.DoctorDetail.as_view()),
    path('likes', views.InteractionsList.as_view()),
    path('likes/<int:pk>', views.InteractionsDetail.as_view()),
]