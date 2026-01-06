# Student Management System 🎓
A full-stack web application for managing student records with user authentication and role-based access control.

## 📋 Features
# 🔐 Authentication & Authorization
User registration and login

Token-based authentication (Django Knox)

Role-based access (Admin/User)

Secure password storage

# 👨‍🎓 Student Management (CRUD Operations)
Create new student records

View student lists with details

Update student information

Delete student records

Search and filter students

# 👥 User Roles
Admin: Full system access (create, read, update, delete all records)

User: Limited access (manage own created students)

# 🛠️ Tech Stack
Backend (Django REST Framework)
Framework: Django 4.2 + Django REST Framework

Authentication: Django Knox

Database: SQLite (Development) / MySQL (Production)

CORS: django-cors-headers

# Frontend (React)
Library: React 18

Routing: React Router DOM

UI Framework: React Bootstrap

HTTP Client: Fetch API

State Management: React Hooks (useState, useEffect)

🚀 Installation & Setup
Prerequisites
Python 3.8+

Node.js 16+

MySQL (optional, for production)

# 1. Backend Setup
bash
# Clone the project
git clone <repository-url>
cd student-management-system/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework django-cors-headers django-rest-knox python-dotenv

# Configure environment variables
cp .env.example .env
# Edit .env with your settings

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
2. Frontend Setup
bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
📁 Project Structure
text
student-management-system/
├── backend/                    # Django Backend
│   ├── accounts/              # Custom user model & authentication
│   ├── api/                   # REST API endpoints
│   ├── students/              # Student models and views
│   ├── backend/               # Django project settings
│   ├── .env                   # Environment variables
│   ├── db.sqlite3             # SQLite database
│   └── manage.py
│
└── frontend/                  # React Frontend
    ├── public/
    ├── src/
    │   ├── components/        # React components
    │   │   ├── auth/         # Login, Register components
    │   │   ├── students/     # Student CRUD components
    │   │   └── layout/       # Navbar, Layout components
    │   ├── App.js            # Main App component
    │   └── index.js          # Entry point
    ├── package.json
    └── README.md
🔧 API Endpoints
Authentication
POST /api/auth/register/ - Register new user

POST /api/auth/login/ - Login user

POST /api/auth/logout/ - Logout user

GET /api/auth/user/ - Get current user info

Students
GET /api/students/ - List all students (requires auth)

POST /api/students/ - Create new student (requires auth)

GET /api/students/{id}/ - Get student details

PUT /api/students/{id}/ - Update student

DELETE /api/students/{id}/ - Delete student

👤 Default Users
After setup, you can use these test accounts:

Username	Password	Role	Access
admin	admin123	Admin	Full system access
teacher	teacher123	User	Manage own students
student	student123	User	Manage own students
testuser	test123	User	Manage own students
🎨 Frontend Pages
Login Page (/login) - User authentication

Register Page (/register) - New user registration

Students List (/students) - View all students

Add Student (/students/new) - Create new student

Edit Student (/students/:id/edit) - Update student info

🔐 Security Features
Password Hashing: Bcrypt password storage

Token Authentication: Secure API access

CORS Protection: Configured allowed origins

Input Validation: Both client and server-side

Role-Based Permissions: Admin/User access control

🔄 Database Models
User Model
username (unique)

email (unique)

password (hashed)

role (admin/user)

Student Model
student_id (unique)

first_name

last_name

email (unique)

phone

date_of_birth

gender

address

enrollment_date

created_by (foreign key to User)

🚀 Deployment
Backend (Production)
bash
# Install production dependencies
pip install gunicorn psycopg2-binary

# Configure production settings
# Update ALLOWED_HOSTS, DEBUG=False, Database settings

# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn backend.wsgi:application
Frontend (Production)
bash
# Build for production
npm run build

# Serve with Nginx/Apache or
npm install -g serve
serve -s build
🧪 Testing
Backend Tests
bash
cd backend
python manage.py test
API Testing with curl
bash
# Register user
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"test123","role":"user"}'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'

# Get students (with token)
curl -H "Authorization: Token YOUR_TOKEN" \
  http://127.0.0.1:8000/api/students/
🛠️ Development Commands
Backend
bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Check project status
python manage.py check
Frontend
bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Fix linting issues
npm run lint
🔍 Troubleshooting
Common Issues
CORS Errors: Ensure CORS_ALLOWED_ORIGINS includes http://localhost:3000

Database Errors: Run python manage.py migrate

Authentication Failures: Check token in localStorage

API Connection: Verify Django server is running on port 8000

Debug Mode
Set DEBUG = True in backend/backend/settings.py for detailed error messages.

📚 API Documentation
Visit http://127.0.0.1:8000/api/ for browsable API documentation when Django server is running.

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Authors
Your Name - Initial work

🙏 Acknowledgments
Django REST Framework team

React team

Bootstrap team

All contributors and testers

📞 Support
For support, email me-puttabanthikruparani@gmail.com or create an issue in the repository.

Made with ❤️ for educational purposes

Quick Start Commands Summary
bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Frontend
cd frontend
npm install
npm start

# Access the application
 # Frontend: http://localhost:3000
 # Backend API: http://127.0.0.1:8000/api/
 # Django Admin: http://127.0.0.1:8000/admin/
