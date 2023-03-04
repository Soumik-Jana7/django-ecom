from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, default="")
    email = models.CharField(max_length=122, default="")
    phone = models.CharField(max_length=122, default="")
    desc = models.CharField(max_length=122, default="")
    date = models.DateField(default="2023-01-30")

    def __str__(self):
        return self.name