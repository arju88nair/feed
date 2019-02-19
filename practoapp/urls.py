from django.urls import path

from . import views

urlpatterns = [
    path('doctors', views.DoctorList.as_view()),
    path('doctors/<int:pk>/detail', views.DoctorDetail.as_view()),
    path('likes', views.InteractionsList.as_view()),
    path('likes/<int:pk>', views.InteractionsDetail.as_view()),
    path('like',views.addlike),
    path('availability', views.AvailabilityList.as_view()),
    path('availability/<int:pk>/detail', views.AvailabilityDetail.as_view()),
]