from django.contrib import admin

# Register your models here.
from .models import Child, Family

admin.site.register(Family)
admin.site.register(Child)
