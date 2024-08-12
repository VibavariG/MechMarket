from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_description = models.CharField(max_length=1000)
    date_released = models.DateTimeField("date released")

    def __str__(self):
        return self.product_name

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - timedelta(days=1) <= self.pub_date <= now

class Customer(models.Model):
    customer_firstname = models.CharField(max_length=80)
    customer_lastname = models.CharField(max_length=80)
    customer_org = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=254)
    #todo
    #customer_phone
    
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text