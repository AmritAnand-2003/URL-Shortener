# URL Shortener Web App

This is a simple URL shortener web application built using Django. The application allows users to shorten long URLs and manage them. The app also includes an automatic cron job to delete expired URLs.

## Approach

The URL shortener app follows a basic approach:

- **URL Generation**: When a user submits a long URL, a unique shortened URL is generated and saved in the database.
- **Expiration Time**: Each shortened URL has an expiration time (TTL), after which the URL becomes invalid and is deleted.
- **Database**: The application uses SQLite as the database to store URL mappings and other metadata.
- **Expiration Cron Job**: A cron job is implemented to run daily and delete expired URLs automatically.

### Key Features
- **Shorten URLs**: Users can submit a long URL, and the app will generate a unique shortened URL.
- **Expiration**: Each shortened URL expires after a defined TTL (Time To Live), and expired URLs are automatically deleted by a cron job.
- **Database**: URLs and their details are stored in a SQLite database.

## Design Decisions

1. **Model Design**: 
   - `URL` model is used to store long URLs, their shortened version, TTL, and expiration date.
   - The TTL value is used to calculate the `expires_at` field when creating a new shortened URL.

2. **Expiration Logic**: 
   - URLs are marked as expired based on the `expires_at` timestamp, and expired URLs are deleted using a cron job that runs daily.

3. **Cron Job**:
   - The cron job is manually set up without additional libraries (such as `django-cron`), but it can be enhanced using libraries for better scheduling.
   - The cron job queries the database for expired URLs and deletes them automatically.

4. **SQLite Database**: 
   - SQLite was chosen for simplicity and because it is sufficient for a small web application.
   
## Challenges Faced

1. **URL Shortening Algorithm**: 
   - Deciding on an appropriate algorithm for generating unique and short URLs was challenging. A base62 encoding was chosen for this purpose.
   
2. **Expiration Handling**:
   - Ensuring that expired URLs are automatically deleted required careful handling of timezones and scheduled tasks. I initially tried setting up the cron job using a third-party library, but ended up using system cron jobs for simplicity.

3. **Database Migrations**: 
   - Initially, there were issues with database migrations and model changes, but they were resolved after careful database management.

## Setup

To set up the application, follow these steps:

1. Clone the repository: 
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener

2. Create and Activate a Virtual Environment: 
python3 -m venv env
source env/bin/activate  


3. Install Dependencies: 
pip install -r requirements.txt

4. Apply Migrations
Run the following commands to create the database and apply migrations: 
python manage.py makemigrations
python manage.py migrate

6. Start the Development Server: 
python manage.py runserver

