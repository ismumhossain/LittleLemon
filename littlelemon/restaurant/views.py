from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    
    def get_queryset(self, *args, **kwargs):
                query = Menu.objects.filter(id=self.kwargs['pk'])
                return query
            
class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer