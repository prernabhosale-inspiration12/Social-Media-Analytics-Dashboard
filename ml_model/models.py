from django.db import models


class Prediction(models.Model):

    likes = models.IntegerField()

    comments = models.IntegerField()

    shares = models.IntegerField()

    prediction = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prediction