from django.db import models

# Create your models here.
# movies/models.py
class Movie(models.Model):
    title = models.CharField(max_length=255,default="Untitled")
    directed_by = models.CharField(max_length=255, default="Unknown")
    starring = models.CharField(max_length=255, default="N/A")
    language = models.CharField(max_length=100, default="English")
    theaters = models.CharField(max_length=255, default="N/A"   )
    location = models.CharField(max_length=255, default="N/A")
    image = models.URLField()

    def __str__(self):
        return self.title
