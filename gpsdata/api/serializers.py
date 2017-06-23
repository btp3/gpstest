from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)

from gpsdata.models import Location

class LocationSerializer(ModelSerializer):

	class Meta:
		model=Location
		fields=[
			'id',
			'user',
			'latitude',
			'longitude',


		]
