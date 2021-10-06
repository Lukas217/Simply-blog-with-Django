from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=5)
    email=models.EmailField(max_length=5)
    phone=models.IntegerField()
    message=models.CharField(max_length=5)

    def __str__(self):
        return self.name