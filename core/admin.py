from django.contrib import admin
from .models import TelegramUser, Profile

admin.site.register(TelegramUser)
admin.site.register(Profile)
