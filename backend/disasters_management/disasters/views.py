from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from disasters.permissions import IsOwnerOrReadOnly
from disasters.serializers import DisasterSerializer
from rest_framework.response import Response

from disasters.models import Disaster
from disasters.repository import DisasterRepository

class DisasterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = DisasterSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def get_queryset(self):


        disasters = Disaster.objects.all()
        

        return disasters

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        disaster_repository = DisasterRepository(response.data)
        disaster_repository.send_nearest_email()

        return  response

    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)

