from django.db import models
from datetime import datetime
# Create your models here.
class Recommend(models.Model):
    name = models.CharField(max_length=30,verbose_name='Enter Name')
    bookname = models.CharField(max_length=50,verbose_name='Enter BookName')
    author = models.CharField(max_length=30,verbose_name='Enter Author Name')
    price = models.IntegerField(verbose_name='Enter Book Price',help_text='You can also specify the approximate price')
    mail = models.EmailField(verbose_name='Enter Email Id')
    genre = models.CharField(max_length=20,choices=[('Thriller','Thriller'),('Comedy','Comedy'),('Historical','Historical'),('Romance','Romance'),('Crime','Crime'),('Fantasy','Fantasy'),("Others","Others")],default="Others")


class FavBooks(models.Model):
    bookName = models.CharField(max_length=50,verbose_name='Enter Book Name')
    image = models.TextField()
