from .serializers import DemandaSerializer
from .models import Demanda
from rest_framework import viewsets, serializers
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly


class DemandaList(viewsets.ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (IsAuthenticated),
    action_permissions = {
        IsOwnerOrReadOnly: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['list', 'retrieve'],
    }

    def perform_create(self, serializer):
        serializer.save(anunciante=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Demanda.objects.filter(anunciante=user)