from django.contrib import admin

# Register your models here.
from .models import Shelter, Dog

admin.site.register(Shelter)
admin.site.register(Dog)
