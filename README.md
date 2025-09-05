# 🍴 SmartRecipeHub  

SmartRecipeHub is a **Django-based Recipe Management System** that allows users to upload, browse, search, update, and delete recipes with ease. The project demonstrates clean Django backend development, database integration, and practical web app functionality.  

---

## 🚀 Features  

- ✅ **Upload Recipes** with image, name, and description.  
- ✅ **View All Recipes** with **pagination** (6 per page).  
- ✅ **Single Recipe Detail Page** to explore full content.  
- ✅ **Search Recipes** by name (case-insensitive).  
- ✅ **Update Recipes** to edit existing details.  
- ✅ **Delete Recipes** to manage stored data.  
- ✅ **Database Integration** using Django ORM (SQLite by default).  
- ✅ Responsive design with HTML & CSS for frontend.  

---

## 🛠️ Tech Stack  

- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS  
- **Database**: SQLite (default, can be swapped with PostgreSQL/MySQL)  
- **Template Engine**: Django Templates  

---

## 📂 Project Structure  

```

SmartRecipeHub/
│
├── recipe\_app/               # Main Django app
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   │   └── recipe\_app/
│   ├── static/               # CSS & static files
│   │   └── recipe\_app/
│   ├── views.py              # Application logic
│   ├── models.py             # Database models
│   ├── urls.py               # App-level URLs
│
├── SmartRecipeHub/           # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3                # Database file
├── manage.py                 # Django management script

````

---

## ⚙️ Installation  

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/SmartRecipeHub.git
   cd SmartRecipeHub
````

2. Create and activate a virtual environment

   ```bash
   python -m venv env
   source env/bin/activate   # On Linux/Mac
   env\Scripts\activate      # On Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the server

   ```bash
   python manage.py runserver
   ```

6. Open in browser:

   ```
   http://127.0.0.1:8000/
   ```

---


## 🎯 Learning Goals

This project demonstrates:

* Django Models, Views, and Templates (MVT)
* Database operations with Django ORM
* Handling forms and CRUD operations
* Search and filtering
* Pagination in Django
* Clean project structure

---


## 🤝 Contribution

Feel free to fork this repo, create issues, or submit pull requests to improve the project.

---

## 📜 License

This project is licensed under the MIT License – free to use and modify.

