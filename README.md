
# Django celery-bot Project

A full-featured Django REST API with:
- ✅ User registration
- 🔐 JWT authentication
- 📩 Welcome email using Celery & Redis
- 🤖 Telegram bot integration
- 🔧 Environment-based configuration
- 🧪 DRF browsable APIs for quick testing

---

## 🚀 Tech Stack
- Django & Django REST Framework
- Simple JWT for authentication
- Celery + Redis for async tasks
- Telegram Bot API integration
- Python-Decouple for environment config

---

## 🧱 Project Structure
```
backend/         # Django project
├── core/        # Your main app
├── templates/   # For login or future use
├── .env         # NOT included in GitHub (use .env.template)
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo and install dependencies

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Add a `.env` file

Copy `.env.template` and rename it to `.env`, then fill in your secrets:

```bash
cp .env.template .env
```

### 3. Apply migrations and create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Redis and Celery (in separate terminal)

```bash
celery -A backend worker --loglevel=info
```

### 5. Run Django server

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

| URL                        | Method | Access     | Description                    |
|----------------------------|--------|------------|--------------------------------|
| `/api/register/`           | POST   | Public     | Register a new user            |
| `/api/token/`              | POST   | Public     | Obtain JWT token               |
| `/api/token/refresh/`      | POST   | Public     | Refresh JWT token              |
| `/api/public-hello/`       | GET    | Public     | Test open access endpoint      |
| `/api/protected-hello/`    | GET    | Auth Only  | Test protected endpoint        |

Use `Authorization: Bearer <token>` for protected views.

---

## 🤖 Telegram Bot

Run the bot using:

```bash
python core/telegram_bot.py
```

On `/start`, it will store the user’s Telegram ID and username in the DB.

---

## 🧪 Testing

You can use:
- Django admin at `/admin/`
- DRF's browsable API at `/api/`
- Postman / Thunder Client

---

## 📁 .env.template

```
SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
TELEGRAM_BOT_TOKEN=your-bot-token
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

## 📜 License
MIT – Use freely for learning or demo purposes.
