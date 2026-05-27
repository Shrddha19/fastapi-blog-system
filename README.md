````markdown
# 🚀 FastAPI Blog Management System

A modern and interactive blog management web application built using **FastAPI**, allowing users to create, update, delete, search, like, and comment on blog posts with an attractive UI.

---

# 📌 Features

* ✍️ Create new blog posts
* 🔄 Update existing blogs
* 🗑️ Delete blogs
* 👀 View all blogs
* 🔍 Search blogs by keyword
* ❤️ Like system with animated like button
* 💬 Comment system for each blog
* 🔐 User Login & Logout System
* 🧩 Session-based authentication
* 🎨 Modern responsive UI with animations
* ⚡ Fast performance using FastAPI
* 🧩 Jinja2 template rendering
* 📱 Responsive design for mobile devices

---

# 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Frontend:** HTML, CSS, JavaScript
* **Template Engine:** Jinja2
* **Server:** Uvicorn

---

# 📂 Project Structure

```bash
project/
 ┣ main.py
 ┣ database.py
 ┣ routers/
 ┣ models/
 ┣ templates/
 ┣ static/
 ┣ requirements.txt
 ┗ README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Shrddha19/fastapi-blog-system.git
cd fastapi-blog-system
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Database

Update your database connection inside `database.py`

```python
mysql+pymysql://username:password@localhost/db_name
```

---

# ▶️ Run Application

```bash
uvicorn main:app --reload
```

Open in browser:

```bash
http://127.0.0.1:8000/
```

---

# 🔍 API Documentation

FastAPI automatically provides API docs:

* Swagger UI → `/docs`
* ReDoc → `/redoc`

---

## 🔐 Authentication System

Users can:
* Register new account
* Login securely
* Logout functionality
* Session management using FastAPI middleware

---

# 🎨 UI Improvements

* Modern glassmorphism design
* Gradient backgrounds
* Animated cards & buttons
* Sidebar navigation
* Responsive homepage
* Hover effects & transitions

---

# 💡 Future Improvements

* 📂 Blog categories
* 🖼️ Upload blog images
* 📊 Admin dashboard
* 🌙 Dark mode
* 📈 Blog analytics

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository and submit a pull request.

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👩‍💻 Author

## Shradha

🔗 GitHub:  
https://github.com/Shrddha19
````

