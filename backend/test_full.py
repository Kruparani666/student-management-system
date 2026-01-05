import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/"

def test_complete_flow():
    print("🎯 Testing Complete Student Management System Flow\n")
    
    # 1. Register a user
    print("1. Registering user...")
    register_data = {
            "username": "usertest",
            "email": "usertest@example.com",
            "password": "testpass123",
            "role": "user"
    }
    
    try:
        response = requests.post(BASE_URL + "auth/register/", json=register_data)
        if response.status_code in [200, 201]:
            print(f"   ✅ Registration successful!")
            print(f"   User: {response.json().get('user')}")
            token = response.json().get('token')
            print(f"   Token: {token[:30]}...")
        else:
            print(f"   ❌ Registration failed: {response.status_code}")
            print(f"   Error: {response.json()}")
            return
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return
    
    # 2. Test authenticated access
    print("\n2. Testing authenticated access...")
    headers = {"Authorization": f"Token {token}"}
    
    # Get current user
    user_response = requests.get(BASE_URL + "auth/user/", headers=headers)
    print(f"   User endpoint: {user_response.status_code}")
    if user_response.status_code == 200:
        print(f"   ✅ Current user: {user_response.json()}")
    
    # 3. Create a student
    print("\n3. Creating a student...")
    student_data = {
        "student_id": "STU001",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@school.com",
        "phone": "1234567890",
        "date_of_birth": "2005-05-15",
        "gender": "M",
        "address": "123 Main Street, City"
    }
    
    student_response = requests.post(BASE_URL + "students/", 
                                    json=student_data, 
                                    headers=headers)
    print(f"   Create student: {student_response.status_code}")
    if student_response.status_code in [200, 201]:
        print(f"   ✅ Student created: {student_response.json()}")
        student_id = student_response.json().get('id')
    else:
        print(f"   ❌ Error: {student_response.json()}")
    
    # 4. List all students
    print("\n4. Listing all students...")
    list_response = requests.get(BASE_URL + "students/", headers=headers)
    print(f"   List students: {list_response.status_code}")
    if list_response.status_code == 200:
        students = list_response.json()
        print(f"   ✅ Found {len(students)} student(s)")
        for student in students:
            print(f"     - {student.get('student_id')}: {student.get('first_name')} {student.get('last_name')}")
    
    # 5. Logout
    print("\n5. Testing logout...")
    logout_response = requests.post(BASE_URL + "auth/logout/", headers=headers)
    print(f"   Logout: {logout_response.status_code}")
    if logout_response.status_code == 204:
        print("   ✅ Logout successful!")
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    test_complete_flow()