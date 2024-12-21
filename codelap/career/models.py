from django.db import models

# Create your models here.
class Careers(models.Model): 
    
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
