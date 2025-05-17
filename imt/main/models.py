from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.text import slugify


class IMT(models.Model):
    weight=models.IntegerField(validators=[MaxValueValidator(250),MinValueValidator(35)])
    height=models.IntegerField(validators=[MaxValueValidator(230),MinValueValidator(120)])
    time_create=models.DateTimeField(auto_now_add=True)
    imt=models.PositiveIntegerField(null=True)

    def get_imt(self):
        self.imt=self.weight/((self.height/100)**2)
        return round(self.imt,2)
    

class Dish(models.Model):
    title=models.CharField(max_length=100)
    recipe=models.TextField(max_length=600)
    img=models.ImageField(upload_to="img/", default=None,
                              blank=True, null=True)
    slug=models.SlugField(unique=True)
    cat=models.ForeignKey('Category',on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    ingridients=models.TextField(max_length=600,default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Dish, self).save(*args, **kwargs)

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


class Dietary(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=600)
    slug=models.SlugField(unique=True)
    cat=models.ForeignKey('catDietary',on_delete=models.PROTECT)
    food=models.ManyToManyField('Dish')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('diet', kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Dietary, self).save(*args, **kwargs)



class catDietary(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category1', kwargs={"slug": self.slug})






