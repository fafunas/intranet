from django.db import models

# Create your models here.



# Clase Noticias
class noticia(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null= True)
    image = models.ImageField(upload_to='img/') 
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural ='Noticias'
        ordering = ['id']
        db_table = 'noticias'


#Clase Roles

class rol(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name= 'Rol'
        verbose_name_plural= 'Roles'
        ordering = ['id']
        db_table = 'Roles'

#Clase Documentos

class documento(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(max_length=100,upload_to='doc/')
    rolId = models.ForeignKey(rol , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['id']
        db_table = 'Documentos'