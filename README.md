# 📚 Library Management System (LMS)

A simple Django-based Library Management System with features for user login, book inventory, borrowing and returning books, and admin book tracking. This project is ideal for learning Django basics and organizing multi-app projects.

---

## 🔧 Features

- ✅ User login/logout
- 📖 Browse available books
- 📚 My Borrowed Books & Returned Books
- 🔁 Return books
- 📦 Admin: Manage inventory and categories
- 🧩 Edition formatting using custom template filters
- 🎥 Demo walkthrough included

---

## 🗂️ Project Structure

LMS/

├── accounts/ # User authentication views

├── borrowing/ # Book borrowing & return logic

├── inventory/ # Inventory and book models

├── templates/ # HTML templates

│ ├── accounts/

│ ├── borrowing/

│ └── inventory/

├── video/

│ └── Demo.mp4 # Demo video of app usage

├── db.sqlite3 # Database file

├── manage.py # Django project entry

├── README.md # Project documentation


---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system

```
### 2. Create and Activate Virtual Environment
```bash

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies
```bash

pip install django


```
### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate

```
### 5. Create Superuser (optional for admin access)
```bash
python manage.py createsuperuser

```

### 6. Run the Development Server
```bash
python manage.py runserver

```

## Then go to http://127.0.0.1:8000


## 🎬 Demo
#### 📁 Check the demo video here: video/Demo.mp4



#### 🙋‍♂️ Author
KANISHKA RANI
3rd Year CSE Student | kanishka22043@gmail.com


### 💡 License
This project is open-source and free to use for educational purposes.Please note that this is a basic implementation and may not cover all edge cases or be production-ready.


