from django.db import models

# Create your models here.

class Lieux(models.Model):
    nom = models.CharField(max_length=120)
    description = models.TextField()
    open = models.BooleanField(default=False)

    def _str_(self):
        return self.title