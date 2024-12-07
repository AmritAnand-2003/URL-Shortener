# 🌐 URL Shortener Web App

This is a **simple and efficient URL shortener** web application built with Django. It allows users to shorten long URLs, track usage statistics, and manage expiration times. The app also includes a scheduled job to automatically delete expired URLs.

---

## 🚀 Key Features

- **🔗 Shorten URLs**: Convert long URLs into short, unique links.
- **⏳ URL Expiration**: Set an expiration time (TTL) for each shortened URL.
- **🗄️ Database**: Persistent storage using SQLite for URL mappings and metadata.
- **⚙️ Automatic Cleanup**: Expired URLs are deleted daily via a cron job.

---

## 📐 Design Decisions

1. **Model Design**: 
   - `URL` model stores long URLs, their shortened versions, TTL, and expiration times.
   - Expiration logic is calculated using the `expires_at` timestamp.

2. **URL Shortening Algorithm**: 
   - A **Base62 encoding** is used to generate unique and compact short URLs.

3. **Expiration Cron Job**: 
   - A system cron job queries the database daily to remove expired URLs. This ensures minimal manual intervention.

4. **Database**: 
   - SQLite is used for simplicity, making the application lightweight and easy to set up.

---

## 🛠️ Challenges Faced

1. **URL Generation**: Choosing an efficient and collision-free algorithm for shortening URLs was critical.
2. **Handling Expirations**: Managing time zones and ensuring expired URLs are correctly identified required meticulous testing.
3. **Migrations**: Initial hiccups in database migrations were resolved with careful schema planning.

---

## 📋 Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### Create and Activate a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```

---

## ⚙️ Setting Up the Cron Job for Expired URLs

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to schedule the cron job for deleting expired URLs daily:
   ```bash
   0 0 * * * /path/to/your/venv/bin/python /path/to/your/project/manage.py delete_expired_urls
   ```

   Replace `/path/to/your/venv` and `/path/to/your/project` with your environment and project paths.

3. Save and exit the crontab editor.

---

## 📚 Technologies Used

- **Django**: Backend framework for building the web application.
- **SQLite**: Lightweight database for storing URL mappings.
- **HTML/CSS**: For the frontend interface.
- **Cron**: Scheduling tool for managing expired URLs.

---

## 🎯 Future Improvements

- **🔍 Analytics Dashboard**: Track usage statistics for each shortened URL.
- **📊 Access Statistics**: Show how often each URL has been accessed.
- **🔒 Authentication**: Add user accounts for personalized URL management.

---
