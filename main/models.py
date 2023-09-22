from django.db import models

# Create your models here.

class Product(models.Model):
    first_product_image_link = models.CharField(max_length=500)
    first_product_name = models.CharField(max_length=100)
    first_product_text = models.CharField(max_length=500)
    first_product_description = models.CharField(max_length=500)
    first_product_previous_price = models.FloatField()
    first_product_current_price = models.FloatField()
    first_product_link = models.CharField(max_length=5000)

    # Second Product
    second_product_image_link = models.CharField(max_length=500, blank=True)
    second_product_name = models.CharField(max_length=100, blank=True)
    second_product_text = models.CharField(max_length=500, blank=True)
    second_product_description = models.CharField(max_length=500, blank=True)
    second_product_previous_price = models.FloatField(blank=True)
    second_product_current_price = models.FloatField(blank=True)
    second_product_link = models.CharField(max_length=5000, blank=True)

    # Third Product
    third_product_image_link = models.CharField(max_length=500, blank=True)
    third_product_name = models.CharField(max_length=100, blank=True)
    third_product_text = models.CharField(max_length=500, blank=True)
    third_product_description = models.CharField(max_length=500, blank=True)
    third_product_previous_price = models.FloatField(blank=True)
    third_product_current_price = models.FloatField(blank=True)
    third_product_link = models.CharField(max_length=5000, blank=True)


    def __str__(self):
        return self.first_product_name + ' | ' + self.second_product_name + ' | ' + self.third_product_name