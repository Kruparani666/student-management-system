import requests
import json

url = "http://127.0.0.1:8000/api/auth/register/"
test_users = [
    {
        "username": "testuser1",
        "email": "test1@example.com",
        "password": "testpass123",
        "role": "user"
    },
    {
        "username": "adminuser",
        "email": "admin@example.com",
        "password": "adminpass123",
        "role": "admin"
    }
]

print("🔍 Testing Django Registration API...\n")

for user_data in test_users:
    print(f"Testing registration for: {user_data['username']}")
    try:
        response = requests.post(url, json=user_data, timeout=5)
        print(f"  Status Code: {response.status_code}")
        
        if response.status_code in [200, 201]:
            print(f"  ✅ Success! Token: {response.json().get('token', 'No token')[:30]}...")
            print(f"  User: {response.json().get('user')}")
        else:
            print(f"  ❌ Error: {response.json()}")
            
    except Exception as e:
        print(f"  ❌ Connection Error: {e}")
    
    print("-" * 50)