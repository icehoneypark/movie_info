from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()


    def __str__(self):
        return self.title

