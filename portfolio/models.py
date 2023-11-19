from django.db import models

# Create your models here.
#Esta es la parte en la que aplico POO
class Project(models.Model): #Esta clase esta heredando de models
    title = models.CharField(max_length=200, verbose_name= "Titulo")  #Esto es en la basde de datos una cadena de caracteres con 200 caracteres
    description= models.TextField( verbose_name= "Descripcion") #Campo de texto mas grande
    image = models.ImageField( verbose_name= "Imagen", upload_to = "projects") #Campo de imagen
    link = models.URLField( verbose_name= "Direccion web" ,null= True, blank=True)
    created = models.DateTimeField(auto_now_add =True , verbose_name= "Fecha de creacion") #Campo de fecha y hora
    updated = models.DateTimeField(auto_now=True , verbose_name= "Fecha de edicion") #Este se ejecuta cada ves que se actualiza la info
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.title
    
