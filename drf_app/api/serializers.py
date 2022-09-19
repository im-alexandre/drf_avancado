from datetime import datetime

from rest_framework import serializers

from drf_app.models import Robot, RobotType, RobotCategory


class RobotTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotType
        fields = ['name']


class RobotCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotCategory
        fields = ['name']


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='robot@hotmail.com', content='robot e-mail')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)
    created = serializers.DateTimeField()
