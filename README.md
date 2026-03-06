# nash_Edadil

Сервис для подбора и оптимизации продуктовой корзины.

## Быстрый старт

1. Скопируйте переменные окружения:
   - `cp .env.example .env`
2. Создайте Python-окружение и установите зависимости:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
3. Запустите backend:
   - `python shopping/backend/manage.py migrate`
   - `python shopping/backend/manage.py runserver 8000`
4. В отдельном терминале запустите frontend:
   - `cd shopping/frontend`
   - `npm install`
   - `npm start`

Frontend: `http://localhost:3000`  
Backend API: `http://localhost:8000`
