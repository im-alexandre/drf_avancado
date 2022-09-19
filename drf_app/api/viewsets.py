from rest_framework import viewsets, permissions
from ..models import Robot, RobotCategory, RobotType

from .serializers import RobotSerializer, RobotTypeSerializer, RobotCategorySerializer


class RobotViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RobotSerializer
    queryset = Robot.objects.all()


class RobotTypeViewSet(viewsets.ModelViewSet):
    permissions = [permissions.IsAdminUser]
    serializer_class = RobotTypeSerializer
    queryset = RobotType.objects.all()


class RobotCategoryViewSet(viewsets.ModelViewSet):
    permissions = [permissions.IsAdminUser]
    serializer_class = RobotCategorySerializer
    queryset = RobotCategory.objects.all()

