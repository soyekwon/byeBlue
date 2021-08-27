from django.db import models


class Mbti(models.Model):
    image = models.ImageField(upload_to="images", null=True)