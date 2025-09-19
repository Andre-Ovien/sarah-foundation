from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListCreateApiView.as_view()),
    path('events/', views.events, name="event"),
]