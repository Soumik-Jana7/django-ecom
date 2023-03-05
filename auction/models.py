from django.db import models
import datetime
import time

# Create your models here.
class AuctionProduct(models.Model):
    prod_id = models.CharField(max_length=122, default="")
    prod_image = models.ImageField(upload_to="images/", default="something.img")
    prod_name = models.CharField(max_length=122, default="")
    prod_desc = models.CharField(max_length=122, default="")
    seller = models.CharField(max_length=122, default="")
    artist = models.CharField(max_length=122, default="")
    prod_start_price = models.IntegerField(default=0)
    prod_price = models.IntegerField(default=0)
    start_time = models.DateTimeField(default=datetime.datetime.now())
    duration_hours = models.PositiveIntegerField(default = 0)
    duration_mins = models.PositiveIntegerField(default=5)
    end_time = models.DateTimeField(default=datetime.datetime.now())
    # status = models.CharField(max_length=10, default='closed')


    def __str__(self):
        return self.prod_name

class User(models.Model):
    user_name = models.CharField(max_length=122, default="")
    user_id  = models.AutoField(primary_key=True)        #user id set as primary key and auto increment
    user_email = models.CharField(max_length=122, default="", unique='true')
    password = models.CharField(max_length=122, default="")

    def __str__(self):
        return self.user_name
    
