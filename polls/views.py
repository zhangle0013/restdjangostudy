# Create your views here.
from polls.models import OUsers
from rest_framework import viewsets
from polls.serializers import OUsersSerializer


class OUsersViewSet(viewsets.ModelViewSet):
    queryset = OUsers.objects.all()
    serializer_class = OUsersSerializer

