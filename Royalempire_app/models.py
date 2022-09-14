from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model



red = "red"
blue = "blue"
yellow = "yellow"
green = "green"
black = "black"
white = "white"
colours = [(green,"green"), (yellow,"yellow"), (blue,"blue"), (red,"red"), (black,"black"), (white,"white")]

class usersname(models.Model):
    User  = get_user_model

class available_items(models.Model):
    # username = models.ForeignKey(usersname, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    item_color  = models.CharField(max_length=20, choices=colours)
    item_img = models.ImageField(upload_to="media")
    date_added = models.DateTimeField(auto_now_add=True)
    
class chart(models.Model):
    # user = models.ForeignKey(usersname, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    item_color = models.CharField(max_length=12, choices=colours)
    quantity = models.IntegerField(default=1)
    price = models.CharField(max_length=30)
    item_image = models.ImageField(upload_to="media")
    date_created = models.DateTimeField(auto_now_add=True)
    check_output = models.BooleanField(default=False)
    

class selected(models.Model):
    # usersname = models.ForeignKey(usersname, models.CASCADE)
    # item_id = models.ForeignKey(chart, on_delete=models.CASCADE, related_name='item_name')
    item_name = models.CharField(max_length=30)
    # items_obeject = models.ForeignKey(chart, on_delete=models.CASCADE )