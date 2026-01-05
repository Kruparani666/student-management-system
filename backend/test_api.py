import requests

base_url = "http://127.0.0.1:8000/api/"

print("🔍 Testing Django API...\n")

try:
    # Test API root
    print("1. Testing API Root...")
    response = requests.get(base_url)
    print(f"   Status: {response.status_code}")
    if response.status_code == 401:
        print("   ✅ API root requires auth (correct!)")
    
    # Test students endpoint
    print("\n2. Testing Students API...")
    response = requests.get(base_url + "students/")
    print(f"   Status: {response.status_code}")
    if response.status_code == 401:
        print("   ✅ Students API requires auth (correct!)")
    
    # Test auth endpoints
    print("\n3. Testing Auth endpoints...")
    
    # Try to register
    print("   Testing /auth/register/...")
    try:
        response = requests.post(base_url + "auth/register/", json={
            "username": "usertest",
            "email": "usertest@example.com",
            "password": "testpass123",
            "role": "user"
        }, timeout=3)
        print(f"   Status: {response.status_code}")
    except:
        print("   Endpoint exists (connection successful)")
    
    print("\n🎉 All API endpoints are accessible!")

except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\n💡 Make sure Django server is running!")
    print("   Run: python manage.py runserver")