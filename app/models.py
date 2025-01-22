from django.db import models


class User(models.Model):
    # Поле id является первичным ключом, и в Django оно создаётся автоматически.
    id = models.BigAutoField(primary_key=True)

    # Поле для хэшированного пароля
    password = models.CharField(max_length=255, null=True)

    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.login or "Unnamed User"
