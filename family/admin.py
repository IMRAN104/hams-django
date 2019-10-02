from django.contrib import admin

# Register your models here.
from .models import Family,Child


admin.site.register(Family)
admin.site.register(Child)