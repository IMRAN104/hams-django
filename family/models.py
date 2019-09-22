from django.contrib.auth.models import User
from django.db import models


class Family(models.Model):
    spousename=models.CharField(max_length=100,default="Selena Gomez")
    # logo=models.ImageField(upload_to='companies_logo',default='companies_logo/default.jpg')
    childname=models.CharField(max_length=100,default="rich kid")
    def __str__(self):
        return "spouse name" + self.spousename + " , "+ "child name: "+ self.childname 