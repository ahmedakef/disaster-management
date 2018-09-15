from django.contrib.auth.models import User
from rest_framework import serializers

from disasters.models import Disaster


class DisasterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = Disaster
        fields = ('id','diameter', 'lat','lang','level_of_danger','created','owner','title', 'description')
        depth  = 1 # generate nested representations
