import os 
import django 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') 
django.setup() 
 
from accounts.models import User 
 
# Delete existing test users (optional) 
User.objects.filter(username__in=['admin', 'teacher', 'student', 'testuser']).delete() 
 
# Create users 
users_data = [ 
    {'username': 'admin', 'email': 'admin@school.com', 'password': 'admin123', 'role': 'admin'}, 
    {'username': 'teacher', 'email': 'teacher@school.com', 'password': 'teacher123', 'role': 'user'}, 
    {'username': 'student', 'email': 'student@school.com', 'password': 'student123', 'role': 'user'}, 
    {'username': 'testuser', 'email': 'test@example.com', 'password': 'test123', 'role': 'user'}, 
] 
 
for data in users_data: 
    user, created = User.objects.get_or_create( 
        username=data['username'], 
        defaults={ 
            'email': data['email'], 
            'role': data['role'] 
        } 
    ) 
    user.set_password(data['password']) 
    user.save() 
    status = "Created" if created else "Updated" 
    print(f"{status}: {user.username} ({user.role})") 
 
print("\n? Test users created!") 
print("======================") 
print("1. Username: admin, Password: admin123 (Admin)") 
print("2. Username: teacher, Password: teacher123 (User)") 
print("3. Username: student, Password: student123 (User)") 
print("4. Username: testuser, Password: test123 (User)") 
