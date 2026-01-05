import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/"

def test_authentication():
    print("🔐 Testing Authentication API\n")
    
    # 1. Register a test user
    print("1. Testing Registration...")
    register_data = {
            "username": "usertest",
            "email": "usertest@example.com",
            "password": "testpass123",
            "role": "user"
    }
    
    try:
        response = requests.post(BASE_URL + "auth/register/", json=register_data)
        print(f"   Status: {response.status_code}")
        if response.status_code == 201 or response.status_code == 200:
            print("   ✅ Registration successful!")
            token = response.json().get('token')
            user = response.json().get('user')
            print(f"   Token received: {token[:20]}...")
        else:
            print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n2. Testing Login...")
    login_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(BASE_URL + "auth/login/", json=login_data)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Login successful!")
            token = response.json().get('token')
            print(f"   Token: {token[:30]}...")
            
            # 3. Test authenticated request
            print("\n3. Testing Students API with token...")
            headers = {"Authorization": f"Token {token}"}
            response = requests.get(BASE_URL + "students/", headers=headers)
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                print("   ✅ Students API accessible!")
                print(f"   Response: {response.json()}")
            else:
                print(f"   Response: {response.json()}")
                
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    test_authentication()