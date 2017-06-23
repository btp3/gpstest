from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import LocationSerializer
from gpsdata.models import Location

from rest_framework import permissions

class LocationListView(ListAPIView):
	queryset=Location.objects.all()
	serializer_class=LocationSerializer
	permission_classes =(permissions.IsAuthenticatedOrReadOnly,)

class LocationCreateView(CreateAPIView):
	queryset=Location.objects.all()
	serializer_class=LocationSerializer

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)	