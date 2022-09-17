from datetime import datetime

from rest_framework import serializers

from drf_app.models import Album, Track, Robot, RobotType, RobotCategory


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Album
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    Album = AlbumSerializer(many=False)

    class Meta:
        model = Track
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
