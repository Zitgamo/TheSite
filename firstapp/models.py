from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here:

# tao Topic (bảng topic có id và name)
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name        

#tao Webpage (bảng webpage có id, name, url, khóa ngoại là topic)
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name

#tao Content (bảng content có id, name, content, image, khóa ngoại là webpage)
class Content(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    content = models.CharField(max_length=264,unique=True)
    image = models.ImageField(upload_to = "images/")
    def __str__(self):
        return str(self.name)    

class Category(models.Model):
    name = models.CharField(max_length=264,unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    duration = models.IntegerField()
    fee = models.IntegerField()
    description = models.TextField()
    certificateion = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "images/")
    def __str__(self):
        return str(self.name)

class Ckeditor(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = RichTextUploadingField()
    def __str__(self):
        return str(self.name)

