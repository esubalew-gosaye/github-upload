from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40,null=False,blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=50,null=False, blank=False)
    verified = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    description = models.TextField(blank=False, max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(default='ethio_future.jpg', null=False, blank=False)

    def __str__(self):
        return self.description
