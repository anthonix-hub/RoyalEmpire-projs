from distutils.command.upload import upload
from itertools import product
from platform import mac_ver
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=30, null="True")
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True )
    digital = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False )
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
    # to get the total amount on cart
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems ])
        return total
    
    # to get the total items on cart
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems ])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for digital_check in orderitems:
            if digital_check.product.digital == False:
                shipping = True
        return shipping
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)    
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=400,null=False )
    city = models.CharField(max_length=400,null=False )
    state = models.CharField(max_length=400,null=False )
    zipcode = models.CharField(max_length=400,null=False )
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    
    