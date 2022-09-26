from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(null=False, max_length=50)
    photo = models.ImageField(upload_to="imagenes", null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    descriptions = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    
    