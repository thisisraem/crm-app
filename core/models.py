from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os

# Create your models here.
class Malls(models.Model):
    name = models.CharField(max_length=30)
    brands = models.ManyToManyField('Brands', related_name='malls')

    class Meta:
        verbose_name_plural = 'Malls'

    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class CustomerRecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    AGE_CHOICES = (
        ('12-18', '12-18'),
        ('18-25', '18-25'),
        ('25-35', '25-35'),
        ('35-50', '35-50'),
        ('more-than-50', 'more than 50'),
    )
    age = models.CharField(max_length=15, choices=AGE_CHOICES)
    email = models.EmailField(max_length=254,blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    malls = models.ManyToManyField(Malls, related_name='customers')
    brands = models.ManyToManyField(Brands, related_name='customers')
    comments = models.TextField(max_length=1600, blank=True, null=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def save(self, *args, **kwargs):
            if self.is_checked:
                self.is_checked = True
            else:
                self.is_checked = False

            if not self.created_at:
                self.created_at = timezone.now()

            self.updated_at = timezone.now()

            super().save(*args, **kwargs)
            
def validate_png_image(image):
    ext = os.path.splitext(image.name)[1]
    valid_extensions = ['.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_("Only PNG images are allowed."))



class Settings(models.Model):
    logo = models.ImageField(upload_to='media/settings', blank=True, null=True, validators=[validate_png_image])
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return "Settings of Webpage"

