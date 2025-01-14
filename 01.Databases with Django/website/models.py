from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()

    # This method basically returns the names of the fields on admin panel as strings
    def __str__(self):
        return self.fname + " " + self.lname
