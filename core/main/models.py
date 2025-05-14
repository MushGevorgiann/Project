from django.db import models

# Create your models here.

class Support(models.Model):
    
    name = models.CharField('Support name',max_length=50)
    email = models.EmailField('Support email')
    text = models.TextField('Support text')
    
    def __str__(self) -> str:
        return self.name
    


class Brand(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    
    brend = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='cat_car')
    name = models.CharField('Car name',max_length=50)
    img = models.ImageField('Car image',upload_to='images/')
    price = models.PositiveIntegerField('Car price')
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'