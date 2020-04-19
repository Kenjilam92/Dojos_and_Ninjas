from django.db import models

class Dojo(models.Model):
    name= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    desc= models.TextField(default="old Dojo")
    def __repr__(self):
        return f'{self.name}'

class Ninja(models.Model):
    dojo_location= models.ForeignKey(Dojo, related_name="students",on_delete=models.CASCADE)
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    def __repr__(self):
        return f'{self.first_name}'
# Create your models here.
