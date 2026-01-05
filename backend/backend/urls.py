"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Add this import

# Simple homepage view
def home(request):
    return HttpResponse("""
        <html>
        <head>
            <title>Student Management System</title>
            <style>
                body { font-family: Arial; margin: 40px; }
                h1 { color: #333; }
                a { 
                    display: inline-block; 
                    margin: 10px; 
                    padding: 10px 20px; 
                    background: #4CAF50; 
                    color: white; 
                    text-decoration: none; 
                    border-radius: 5px;
                }
                a:hover { background: #45a049; }
            </style>
        </head>
        <body>
            <h1>🎓 Student Management System</h1>
            <p>Django backend is running successfully!</p>
            <div>
                <a href="/admin/">Admin Panel</a>
                <a href="/api/">API Root</a>
                <a href="/api/students/">Students API</a>
            </div>
        </body>
        </html>
    """)

urlpatterns = [
    path('', home),  # Homepage
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]