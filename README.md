Вот пример `README.md` для репозитория `task_manager_lecture`, который включает FastAPI-бэкенд, фронтенд, авторизацию и Docker-инфраструктуру:

---

```markdown
# 📝 Task Manager Lecture

Полноценное учебное приложение "Менеджер задач" с бэкендом на FastAPI, авторизацией, фронтендом и развёртыванием через Docker Compose.

## 🚀 Функции

- ✅ REST API на FastAPI
- 🔐 JWT-аутентификация (регистрация, логин, `/me`)
- 📄 CRUD задачи
- 🌐 Фронтенд-интерфейс
- 🐳 Docker + Docker Compose
- 🗃️ SQLite база данных (`taskdb.db`)

---

## 🧱 Структура проекта

```

.
├── app/                  # Бэкенд: FastAPI
├── frontend/             # Фронтенд (React/Vite или другой стек)
├── Dockerfile            # Docker для API
├── docker-compose.yml    # Compose для всего приложения
├── requirements.txt      # Python зависимости
└── taskdb.db             # SQLite база

````

---

## 🛠️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/<your-username>/task_manager_lecture.git
cd task_manager_lecture
````

### 2. Запуск с Docker Compose

```bash
docker compose up --build
```

🔎 API будет доступен на: `http://localhost:8000`
🌐 Фронтенд (если включён): `http://localhost:3000` *(уточните порт во `frontend`)*

---

## 🧪 Основные эндпоинты API

* `POST /register` — регистрация
* `POST /login` — авторизация
* `GET /me` — информация о пользователе
* `POST /create_task` — создать задачу
* `GET /get_tasks` — список задач

---

## 📦 Требования

* Docker и Docker Compose
* Python 3.10+ (если запускаете локально)

Установить зависимости вручную:

```bash
pip install -r requirements.txt
```

---

## 🤝 Авторы

* 👤 [SIMMONA-hub](https://github.com/SIMMONA-hub)

---

## 📄 Лицензия

MIT — свободное использование в образовательных целях.

```

---
