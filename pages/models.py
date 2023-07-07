from django.db import models

# Create your models here.

class info(models.Model):
    

    name=models.CharField(max_length=50)
    whatsapp=models.CharField(max_length=11)
    parent_number=models.CharField(max_length=11)
    center=models.CharField(max_length=11,null=True)
    academic_year=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    