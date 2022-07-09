from django.db import models


class Member(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN"
        REGULAR = "REGULAR"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.REGULAR)

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
