from django.db import models

class ServiceModels(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name