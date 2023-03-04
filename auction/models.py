from django.db import models

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

    def __str__(self):
        return self.prod_name