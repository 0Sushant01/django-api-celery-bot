import os
import django
from decouple import config
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import TelegramUser


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    telegram_id = str(user.id)
    username = user.username or ""

    # Save or get the Telegram user
    obj, created = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={'username': username}
    )

    if created:
        update.message.reply_text(f"👋 Hello @{username}, you’ve been registered!")
    else:
        update.message.reply_text(f"👋 Welcome back @{username}!")


def main():
    token = config('TELEGRAM_BOT_TOKEN')
    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
