from django.shortcuts import render
from .models import UserInformation
from rest_framework import permissions , viewsets
from .serializers import UserInformationSerializer

class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field ='slug_id'
