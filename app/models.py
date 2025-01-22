from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)

    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.email or "Unnamed User"
