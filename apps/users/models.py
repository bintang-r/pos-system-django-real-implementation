from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Menambahkan pilihan Role
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('CASHIER', 'Cashier'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CASHIER')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"