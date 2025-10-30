from django.db import models
from django.contrib.auth.models import User

class ClickEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    element_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} clicou em {self.element_name} ({self.timestamp:%d/%m/%Y %H:%M})"
