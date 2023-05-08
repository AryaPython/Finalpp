from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=250,null=True)

    def __str__(self):
        return (self.name)

class Courses(models.Model):
    name=models.CharField(max_length=300,null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return (self.name)


