from django.db import models


class RobotType(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RobotCategory(models.Model):
    name = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Robot(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(RobotType, on_delete=models.CASCADE)
    category = models.ForeignKey(RobotCategory, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()


class Track(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
