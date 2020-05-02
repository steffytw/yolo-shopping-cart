from django.db import models

# Create your models here.
class userRegistration(models.Model):
    
    username = models.CharField(max_length=20)
    email =  models.CharField(max_length = 30)
    mobile_number =  models.IntegerField()
    password = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural="User Registration Details"
    def __str__(self):

        return self.username

class productInformation(models.Model):
    
    serialNo = models.IntegerField()
    product =  models.CharField(max_length = 50)
    product_details =  models.CharField(max_length = 50)
    price = models.CharField(max_length = 20)
    quantity = models.IntegerField()
    subtotal = models.CharField(max_length = 20)
    
    class Meta:
        verbose_name_plural="Shopping Cart Product Details"
    def __str__(self):

        return self.product

