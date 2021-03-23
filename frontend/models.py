from django.db import models
from django.utils.safestring import mark_safe

class Country(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name="country_name", null=True)
    name = models.CharField(max_length=250, unique=True)


    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, related_name="state_name", null=True)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    key = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    status = models.BooleanField(default=0)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    last_login = models.DateTimeField(auto_now_add=True)


    def image_tag(self):
        if self.document:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.document.url)
        else:
            return 'No Image Found'

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    title_description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    meta_description = models.TextField(max_length=100)
    status = models.BooleanField(default=0)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title