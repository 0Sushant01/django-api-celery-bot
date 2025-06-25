from django.db import models
from django.contrib.auth.models import User


class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"@{self.username or 'unknown'} ({self.telegram_id})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_user = models.OneToOneField(TelegramUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
