from django.db import models
from django.contrib.auth.models import User

class Harcama(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.date}"