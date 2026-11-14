from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Agricultor, Cultivo

admin.site.register(Agricultor)
admin.site.register(Cultivo)