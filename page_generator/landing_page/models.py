from django.db import models

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Form Submission'
        verbose_name_plural = 'Form Submissions'

    def __str__(self):
        return self.name