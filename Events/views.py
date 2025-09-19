from django.shortcuts import render
from rest_framework.viewsets import generics 
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

# Create your views here.


class EventListCreateApiView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

def events(request):
    context = {

    }
    return render(request, 'event.html',context)