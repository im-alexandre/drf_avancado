from rest_framework import viewsets, permissions, generics, status
from ..models import Robot, RobotCategory, RobotType
from rest_framework.response import Response

from .serializers import RobotSerializer, RobotTypeSerializer, RobotCategorySerializer, RegisterSerializer


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(id),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RobotViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RobotSerializer
    queryset = Robot.objects.all()


class RobotTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = RobotTypeSerializer
    queryset = RobotType.objects.all()


class RobotCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = RobotCategorySerializer
    queryset = RobotCategory.objects.all()

