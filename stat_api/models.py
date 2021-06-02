from django.db import models

# Create your models here.
class Stats(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
