from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# Model For News
class noticia(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null= True)
    shortDescription = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img/') 
    created = models.DateTimeField(auto_now=True)
    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.shortDescription = self.description[0:29]

        super(noticia,self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural ='Noticias'
        ordering = ['id']
        db_table = 'noticias'


#Model for Roles review

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

#Model For Documentos

class documento(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    shortDescription = models.CharField(max_length=30)
    file = models.FileField(max_length=100,upload_to='doc/')
    rolId = models.ForeignKey(rol , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.shortDescription = self.description[0:29]

        super(documento,self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['id']
        db_table = 'Documentos'

#Model for training
class training(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(max_length=200,upload_to='training/')
    created = models.DateTimeField(auto_now=True)
    update = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural= 'Training'
        ordering = ['id']
        db_table= 'Training'



#Model For Trainig_User

class training_user(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    training_id = models.ForeignKey(training, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        self.user_id

    class Meta:
        verbose_name ='Training User'
        verbose_name_plural= 'Training Users'
        ordering= ['id']
        db_table= 'Training_User'



#Model For Forms

class forms(models.Model):
    description = models.TextField(max_length=300)

    def __str__(self):
        self.description

    class Meta:
        verbose_name='Form'
        verbose_name_plural= 'Forms'
        ordering = ['id']
        db_table= 'Forms'


#Model Fro Training Status  
class training_status(models.Model):
    training_user_id = models.ForeignKey(training_user, on_delete=models.CASCADE)
    form_id= models.ForeignKey(forms, on_delete=models.CASCADE)
    answer = models.TextField(models.TextField, max_length=200)

    def __str__(self):
        self.training_user_id

    class Meta:
        verbose_name = 'Training Status'
        verbose_name_plural = 'Training Status'
        ordering = ['id']
        db_table= 'Training_Status'