from django.shortcuts import render
from rest_framework.viewsets import generics 
from .models import Event
from .serializers import EventSerializer, EventDetailSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

# Create your views here.


class EventListCreateApiView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-date')
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

class EventRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

#    def get_queryset(self):
        return super().get_queryset()


def event_details(request,pk):
    context = {

    }
    return render(request, 'event_details.html', context)


#class EventListApiView(generics.ListAPIView):
#    queryset = Event.objects.all()
#    serializer_class = EventDetailSerializer
#    permission_classes = [AllowAny]