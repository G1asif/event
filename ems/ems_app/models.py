from django.db import models

# Create your models here.
class table(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    eventname=models.CharField(max_length=100)


class Meta:
    db_table="table"