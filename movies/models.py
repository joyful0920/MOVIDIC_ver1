from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    trailer_url = models.TextField()  # 추가 필드
    description = models.TextField()
    review = models.TextField()  # 추가 필드
