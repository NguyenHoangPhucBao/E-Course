from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m')


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=100, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to='course/%y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='lesson/%Y/%m')
    content = RichTextField(null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.name