from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import FoodLog
from .serializers import FoodLogSerializer

class FoodViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        # list  categories per current loggedin user
        queryset = FoodLog.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = FoodLogSerializer
    def create(self, request):
        # check if category already exists for current logged in user
        log = FoodLog.objects.filter(
            name_of_food=request.data.get('name_of_food'),
            owner=request.user
        )
        return super().create(request)
    # user can only delete category he created
    def destroy(self, request, *args, **kwargs):
        log = FoodLog.objects.get(pk=self.kwargs["pk"])
        if not request.user == log.owner:
            raise PermissionDenied("You can not delete this category")
        return super().destroy(request, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FoodEditSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = FoodLog.objects.all().filter(pk=self.kwargs["pk"], owner=self.request.user)
        return queryset
    serializer_class = FoodLogSerializer

class PublicFoodSet(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = FoodLog.objects.filter(is_public=True)
        return queryset
    serializer_class = FoodLogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)