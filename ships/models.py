from django.db import models

# Create your models here.

class Ship(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre de la Nave',)
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Imagen de la Nave',)
    type = models.CharField(max_length=100, null=True, verbose_name='Tipo de Nave',)
    country = models.CharField(max_length=100, null=True, verbose_name='País de Origen',)
    years = models.CharField(max_length=50, null=True, verbose_name='Años de Operación',)
    description = models.TextField(null=True, verbose_name='Descripción de la Nave',)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
