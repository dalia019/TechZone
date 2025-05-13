from django.db import models


# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Storage(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size

class Product(models.Model):

    product_category_choices = [
        ('smartphones', 'smartphones'),
        ('laptops', 'laptops'),
        ('accessories', 'accessories'),

    ]

    # product_color_choices = [
    #     ('Space Black', 'Space Black'),
    #     ('Silver', 'Silver'),
    #     ('Gold', 'Gold'),
    #     ('White', 'White'),
    # ]

    # product_storage_choices = [
    #     ('128GB', '128GB'),
    #     ('256GB', '256GB'),
    #     ('512GB', '512GB'),
    # ]



    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10 , decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='images/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)

    product_category = models.CharField(max_length=100, choices= product_category_choices,null=True)
    product_key_features = models.TextField(help_text="Separate each feature with a semicolon (;)",null =True , blank=True)


    available_colors = models.ManyToManyField(Color, blank=True )
    available_storage = models.ManyToManyField(Storage, blank=True )

    def get_feature_list(self):
        return [feature.strip() for feature in self.product_key_features.split(';') if feature.strip()]



    def __str__(self):
        return self.product_name
    
    # class Meta:
    #     verbose_name = 'Product'
    #     verbose_name_plural = 'Products'
    

