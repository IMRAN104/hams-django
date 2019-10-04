from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Text(models.Model):
    text = models.CharField(max_length=1000)
    no_of_words = models.IntegerField(default=0)

    def __str__(self):
        text = self.text.split()[:5]
        return " ".join(text) + " : " + str(self.no_of_words)
