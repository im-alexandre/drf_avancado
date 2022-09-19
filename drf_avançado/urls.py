from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drf_app.api.viewsets import RobotViewSet, RobotTypeViewSet, RobotCategoryViewSet

route = routers.DefaultRouter()

route.register(r'api/robot', RobotViewSet, basename='Robot')
route.register(r'api/type', RobotTypeViewSet, basename='Type')
route.register(r'api/category', RobotCategoryViewSet, basename='Category')

urlpatterns = [
    path('', include(route.urls)),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
