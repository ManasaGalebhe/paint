from django.db import models

# Create your models here.
class Employee(models.Model):
    painting_name =models.CharField(max_length=100)
    description_name =models.CharField(max_length=100)
    photo =models.ImageField(upload_to='images')
    """email_address= models.EmailField(max_length=20,unique=True) """


    def __str__(self):
        return self.painting_name  