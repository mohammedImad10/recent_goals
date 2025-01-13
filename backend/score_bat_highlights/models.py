from datetime import date
from django.db import models


class BatHighlight(models.Model):
    title = models.CharField(max_length=50)
    competition = models.CharField(max_length=70)
    date = models.DateField(default=date.today)
    embed_video = models.TextField()


class VideoDetails(models.Model):
    name = models.CharField(max_length= 30)

