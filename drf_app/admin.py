from django.contrib import admin
from .models import RobotCategory, RobotType, Robot

admin.site.register(RobotType)
admin.site.register(RobotCategory)
admin.site.register(Robot)