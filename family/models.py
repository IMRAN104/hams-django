from django.contrib.auth.models import User
from django.db import models


class Family(models.Model):
    spouseName = models.CharField(max_length=100, null=True, blank=True)
    spouseDOB = models.DateField(null=True)
    spouseEmail = models.CharField(max_length=50, null=True, blank=True)
    spouseNID = models.CharField(max_length=50, null=True)
    spouseMobile = models.CharField(max_length=50, null=True)
    spousePicture = models.ImageField(upload_to='spouse_pic', null=True)
    spouseNIDPicture = models.ImageField(upload_to='spouse_nid_pic', null=True)

    def __str__(self):
        return "spouse name" + self.spousename


class Child(models.Model):
    childName = models.CharField(max_length=100, null=True, blank=True)
    childDOB = models.DateField(null=True)
    childPicture = models.ImageField(upload_to='spouse_pic', null=True)
    Family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
