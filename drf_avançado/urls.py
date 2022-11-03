from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_app.api.viewsets import Register

from drf_app.api.viewsets import RobotViewSet, RobotTypeViewSet, RobotCategoryViewSet

route = routers.DefaultRouter()

route.register(r'api/robot', RobotViewSet, basename='Robot')
route.register(r'api/type', RobotTypeViewSet, basename='Type')
route.register(r'api/category', RobotCategoryViewSet, basename='Category')

urlpatterns = [
    path('', include(route.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/refresh/', TokenRefreshView.as_view()),
    path('api/sign-up/', Register.as_view(), name='sign-up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
