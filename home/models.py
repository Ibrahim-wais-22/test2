from django.db import models
from django.utils.text import slugify
from django.db.models.fields import CharField, DateField, SlugField
from django.contrib.auth.models import User


class The_user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)

    def __str__(self) :
        return self.name

        
class Blog(models.Model):
    owner = models.ForeignKey(User, related_name='blog_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contant = models.TextField( max_length=5000)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='blog/')
    slug = models.SlugField(blank=True,null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)

        super(Blog, self).save(*args, **kwargs) # Call the real save() method
 

    def __str__(self) :
        return self.title

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


class Comment(models.Model):
    id_post = models.ForeignKey('Blog',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    comment = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)


    def __str__(self) :
        return self.comment