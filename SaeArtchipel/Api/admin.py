from django.contrib import admin
from .models import Lieux

class LieuxAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'open')

# Register your models here.

admin.site.register(Lieux, LieuxAdmin)