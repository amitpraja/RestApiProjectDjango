from django.db import models

# Create your models here.
class project(models.Model):
    project = models.CharField(max_length=100)

class client(models.Model):
    project = models.ForeignKey(project,related_name='client',on_delete=models.CASCADE)
    client_name  = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)