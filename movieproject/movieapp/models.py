from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=100)
    mini_desc=models.TextField()
    desc=models.TextField()
    Year=models.IntegerField()
    img=models.ImageField(upload_to='photo')

    def __str__(self):
        return self.name

