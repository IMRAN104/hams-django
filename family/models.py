from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Family(models.Model):
    spouse_name = models.CharField(max_length=100, null=True, blank=True)
    spouse_date_of_birth = models.DateField(null=True)
    spouse_email = models.CharField(max_length=50, null=True, blank=True)
    spouse_NID = models.CharField(max_length=50, null=True)
    spouse_mobile = models.CharField(max_length=50, null=True)
    spouse_picture = models.ImageField(upload_to='spouse_pic', null=True)
    spouse_NID_picture = models.ImageField(
        upload_to='spouse_nid_pic', null=True)

    def __str__(self):
        return self.spouse_name


class Child(models.Model):
    # childName = models.CharField(max_length=100, null=True, blank=True)
    # childDOB = models.DateField(null=True)
    # childPicture = models.ImageField(upload_to='spouse_pic', null=True)

    child_name = models.CharField(max_length=100, null=True, blank=True)
    child_date_of_birth = models.DateField(
        default=date.today, null=True, blank=True)
    child_picture = models.ImageField(
        upload_to='child_pic', default='default.jpg', null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.child_name
# # TODO    #Already Done
