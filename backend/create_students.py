import os 
import django 
from datetime import date 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') 
django.setup() 
 
from students.models import Student 
from accounts.models import User 
 
# Get admin user 
admin_user = User.objects.get(username='admin') 
 
students_data = [ 
    { 
        'student_id': 'STU001', 
        'first_name': 'John', 
        'last_name': 'Doe', 
        'email': 'john.doe@school.com', 
        'phone': '1234567890', 
        'date_of_birth': date(2005, 5, 15), 
        'gender': 'M', 
        'address': '123 Main Street, New York', 
        'created_by': admin_user 
    }, 
    { 
        'student_id': 'STU002', 
        'first_name': 'Jane', 
        'last_name': 'Smith', 
        'email': 'jane.smith@school.com', 
        'phone': '0987654321', 
        'date_of_birth': date(2006, 3, 22), 
        'gender': 'F', 
        'address': '456 Oak Avenue, Boston', 
        'created_by': admin_user 
    }, 
    { 
        'student_id': 'STU003', 
        'first_name': 'Robert', 
        'last_name': 'Johnson', 
        'email': 'robert.j@school.com', 
        'phone': '5551234567', 
        'date_of_birth': date(2004, 11, 8), 
        'gender': 'M', 
        'address': '789 Pine Road, Chicago', 
        'created_by': admin_user 
    } 
] 
 
for data in students_data: 
    student, created = Student.objects.get_or_create( 
        student_id=data['student_id'], 
        defaults=data 
    ) 
    status = "Created" if created else "Exists" 
    print(f"{status}: {student.student_id} - {student.first_name} {student.last_name}") 
 
print("\n? Test students created!") 
