from pyexpat import model
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    d=models.CharField(max_length=300)
    pub_date=models.DateField()
    
    
    


    def __str__(self):
        return self.product_name
    

class contact(models.Model):
     
     content=models.TextField()
     
     email=models.CharField( max_length=50)

     def __str__(self):
        return self.content


class bloghome(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    name=models.CharField(max_length=100)
    slu=models.SlugField(max_length=100)
    def __str__(self):
        return self.name
    


class prod(models.Model):
    botlength=models.TextField(max_length=3)
    botdiameter=models.TextField(max_length=3)
    bottype=models.TextField(max_length=50)

    def __str__(self):
        return self.bottype
    