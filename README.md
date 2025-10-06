# Kanmind – Fullstack Django Project

## 📌 Project Description
Kanmind is a fullstack web application built with Django for managing Kanban boards and tasks.
It combines both backend logic (API, authentication, database) and a Django-based frontend (templates & static assets) in one project.

## 🛠 Technologies
🧩 Backend
    Python 3.x
    Django
    SQLite (default) or PostgreSQL (optional)
    python-dotenv

🎨 Frontend
    Django Templates (HTML, CSS, JavaScript)
    Static file management via Django
    Responsive layouts for Kanban boards, dashboards, and auth pages

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Takoua852/Kanmind_backend.git
cd Kanmind_backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
env\Scripts\activate # On Windows
source env/bin/activate  # On Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root and add your settings (example):
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

Then open your browser at:
👉 http://127.0.0.1:8000/

## 📂 Project Structure
```
Kanmind/
├── core/                    # Project settings, URLs, middleware
├── kanban_app/              # Boards, columns, and Kanban logic
├── tasks_app/               # Task management (CRUD, comments, etc.)
├── users_auth_app/          # Authentication & user management
│
├── templates/
│   ├── pages/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── board/
│   │   │   └── index.html
│   │   ├── boards/
│   │   │   └── index.html
│   │   ├── dashboard/
│   │   │   └── index.html
│   │   ├── privacy
│   │   │    └── index.html
│   │   ├── imprint.html
│   │   │    └── index.html
│   │   └── index.html
├── static/
│   ├── assets/
│   │   └── fonts
│   │   └── icons
│   ├── auth/
│   │    └── auth.css
│   ├── board/css/js
│   ├── boards/css/js
│   ├── dashboard/css/js
│   └── shared/css/js
│
├── manage.py
├── requirements.txt
└── README.md
```


## 💡 Notes
- The `.gitignore` file ensures that sensitive data and the virtual environment are not included in the repository.
- For production, configure your database and secret keys securely.
- More documentation will be added soon.

---

Feel free to adjust project names, paths, or add more details as needed!


## 📚 API Endpoints

| Method | Endpoint                               | Description                             |
|--------|----------------------------------------|-----------------------------------------|
🔑 Authentication
| POST   | /api/registration/                     | Register a new user                     |
| POST   | /api/login/                            | User login                              |
| GET    | /api/email-check/                      | Check if an email is already registered |
|--------|----------------------------------------|-----------------------------------------|
📋 Boards
| GET    | /api/boards/                           | List all boards                         |
| POST   | /api/boards/                           | Create a new board                      |
| GET    | /api/boards/{id}/                      | Retrieve board by ID                    |
| PATCH  | /api/boards/{id}/                      | Partially update board by ID            |
| DELETE | /api/boards/{id}/                      | Delete board by ID                      |
|--------|----------------------------------------|-----------------------------------------|
✅ Tasks
| GET    | /api/tasks/assigned-to-me/             | List tasks assigned to the current user |
| GET    | /api/tasks/reviewing/                  | List tasks the current user is reviewing|
| POST   | /api/tasks/                            | Create a new task                       |
| PATCH  | /api/tasks/{id}/                       | Partially update task by ID             |
| DELETE | /api/tasks/{id}/                       | Delete task by ID                       |
| GET    | /api/tasks/{id}/comments/              | List comments for a specific task       |
| POST   | /api/tasks/{id}/comments/              | Add a comment to a specific task        |
| DELETE | /api/tasks/{id}/comments/{comment_id}/ | Delete a specific comment from a task   |


## 🧠 Frontend Usage & Development Notes

Template Inheritance

All pages are located under templates/pages/ and can extend a shared base layout:
    
    
``` html
    {% extends 'base.html' %}
    {% block content %}
    <!-- Page-specific content -->
    {% endblock %}
```
Static Files

Static assets (CSS/JS) are organized by section under static/assets/.
To load them in templates, use:

``` html
    {% load static %}
<link rel="stylesheet" href="{% static 'assets/dashboard/css/style.css' %}">
<script src="{% static 'assets/dashboard/js/main.js' %}"></script>

```

## 💡 Notes

This repository now includes both backend and frontend code.
The .gitignore excludes sensitive data, .env, and virtual environments.
Configure DEBUG=False, ALLOWED_HOSTS, and production database before deployment.
Templates and static files are modular for scalability and reusability.

## 📜 License

This project is licensed under the [MIT License](LICENSE).