from django.db import models

# Create your models here.
class jobs(models.Model):
    image = models.ImageField(upload_to="images/")
    summery = models.CharField(max_length = 200)

    def __str__(self):
        return self.summery