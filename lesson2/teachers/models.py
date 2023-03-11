from django.db import models

# Create your models here.
class Teacher(models.Model):
    KAFEDRA_CHOICES = [
        ('Aniq', 'Aniq fanlar'),
        ('Tabiiy', 'Tabiiy fanlar'),
        ('Maxsus', 'Maxsus fanlar'),
    ]
    
    ILMIY_CHOICES = [
        ('Dotsent', 'Dotsent'),
        ('Doktor', 'Doktor'),
        ('Magistr', 'Magistr'),
    ]
    
    ism = models.CharField(max_length=255)
    familya = models.CharField(max_length=255)
    kafedra = models.CharField(max_length=10, choices=KAFEDRA_CHOICES)
    fan_nomi = models.CharField(max_length=255)
    ilmiy_daraja = models.CharField(max_length=255, choices=ILMIY_CHOICES)
    
    def __str__(self):
        return self.ism

    