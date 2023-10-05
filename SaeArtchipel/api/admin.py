from django.contrib import admin
from .models import Lieu

class LieuAdmin(admin.ModelAdmin):
    list_display = ("idLieu","nomLieu")

# Register your models here.

admin.site.register(Lieu, LieuAdmin)