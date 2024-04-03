from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    date=models.DateField(auto_now=True)

    def __str__(self) :
        return self.name
class detail(models.Model):
    name = models.CharField(max_length=100)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
