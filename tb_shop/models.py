from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='category',blank=True)
    desciption= models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
    #human readible repesentation of the model
    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    desciption = models.TextField(blank=True)
    #if product will be deleted all info in the category will be deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #price of product
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #the image of the product
    img = models.ImageField(upload_to='product', blank=True)
    #if product is available
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    #the date when the product is created
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
