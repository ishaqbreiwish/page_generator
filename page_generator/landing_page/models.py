from django.db import models

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Submissions")
    email = models.EmailField()
    message = models.TextField()

class MyModel(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Submissions")
    email = models.EmailField()
    message = models.TextField()
    

    def __str__(self):
        return self.name