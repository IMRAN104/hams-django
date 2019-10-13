from datetime import date

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
        return self.spouseName


class Child(models.Model):
    # childName = models.CharField(max_length=100, null=True, blank=True)
    # childDOB = models.DateField(null=True)
    # childPicture = models.ImageField(upload_to='spouse_pic', null=True)

    child_name = models.CharField(max_length=100, null=True, blank=True)
    child_date_of_birth = models.DateField(
        default=date.today, null=True, blank=True)
    child_picture = models.ImageField(
        upload_to='child_pic', default='default.jpg', null=True, blank=True)
    Family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.child_name
# # TODO
# class Family(models.Model):
#     spouse_name = models.CharField(max_length=100, null=True,blank=True )
#     spouse_date_of_birth =  models.DateField(default=date.today, null=True,blank=True )
#     spouse_email = models.EmailField(null=True,blank=True )
#     spouse_mobile = models.CharField(max_length=14, null=True, blank=True)
#     spouse_picture = models.ImageField(upload_to='profile_pics',default='default.jpg', null=True,blank=True )

#     def __str__(self):
#         return self.spouse_name
