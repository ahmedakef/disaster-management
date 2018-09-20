from django.contrib.auth.models import User
from rest_framework import serializers

from disasters.models import Disaster, GeoJSON
from disasters.helpers import create_point


class DisasterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        lang = validated_data.get("lang")
        lat = validated_data.get("lat")

        validated_data["center_point"] = create_point(lang, lat)

        return Disaster.objects.create(**validated_data)

    class Meta:
        model = Disaster
        fields = ('id','diameter', 'lat','lang','level_of_danger','created','owner','title', 'description')
        depth  = 1 # generate nested representations
