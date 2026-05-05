# 🚀 **FastAPI Blog Management System**

A modern blog management web application built using **FastAPI**, allowing users to **create, update, delete, and search** blog posts with a clean UI.

---

## 📌 **Features**

* ✍️ **Create** new blog posts
* 🔄 **Update** existing blogs
* 🗑️ **Delete** blogs
* 👀 **View** all blogs
* 🔍 **Search** blogs by keyword
* 🎨 **Clean UI** using HTML & CSS
* ⚡ **Fast performance** with FastAPI

---

## 🛠️ **Tech Stack**

* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Frontend:** HTML, CSS (**Jinja2 Templates**)
* **Server:** Uvicorn

---

## 📂 **Project Structure**

```
project/
 ┣ main.py
 ┣ database.py
 ┣ models/
 ┣ schemas/
 ┣ routers/
 ┣ templates/
 ┣ static/
 ┗ requirements.txt
```

---

## ⚙️ **Installation & Setup**

### 1️⃣ **Clone the repository**

```
git clone https://github.com/Shrddha19/fastapi-blog-system.git
cd fastapi-blog-system
```

### 2️⃣ **Create virtual environment**

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ **Install dependencies**

```
pip install -r requirements.txt
```

### 4️⃣ **Configure Database**

Update your database connection in **`database.py`**:

```
mysql+pymysql://username:password@localhost/db_name
```

---

## ▶️ **Run the Application**

```
uvicorn main:app --reload
```

Open in browser:
**http://127.0.0.1:8000/**

---

## 🔍 **API Documentation**

FastAPI provides built-in interactive docs:

* **Swagger UI →** `/docs`
* **ReDoc →** `/redoc`

---

## 📸 **Screenshots**
<img width="816" height="644" alt="image" src="https://github.com/user-attachments/assets/9c760b5d-8f2a-4e24-a670-9d7dcb673d1a" />





---

## 💡 **Future Improvements**

* 🔐 **JWT Authentication**
* 👤 **User login & authorization**
* 💬 **Comment system**
* ❤️ **Like system**
* 📂 **Blog categories**

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to **fork this repository** and submit a **pull request**.

---

## 📜 **License**

This project is **open-source** and available under the **MIT License**.

---

## 👩‍💻 **Author**

**Shradha**
🔗 GitHub: https://github.com/Shrddha19

---
⭐ If you like this project, don’t forget to star the repo!

⭐ **If you like this project, don’t forget to star the repo!**
