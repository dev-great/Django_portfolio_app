from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField()
    message = models.TextField()

    def __str__(self):
        return self.email
