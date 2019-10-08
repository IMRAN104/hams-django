from django.db import models


# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(
        max_length=200, null=True, blank=True)

    def __str__(self):
        summary = self.summary.split()[:5]
        return " ".join(summary)
