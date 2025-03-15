from django.db import models
from django.utils import timezone

# Create your models here.

class EggPrice(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=100, default='API')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"${self.price} on {self.date.strftime('%Y-%m-%d')}"
