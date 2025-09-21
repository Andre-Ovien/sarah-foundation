from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListCreateApiView.as_view()),
    path('list/', views.events, name="event"),
    path('details/<pk>/', views.event_details, name="event_details"),
    path('events-details/<pk>/', views.EventRetrieveUpdateDeleteApiView.as_view(), name="event-detail"),
#    path('events/', views.EventListApiView.as_view()),
]