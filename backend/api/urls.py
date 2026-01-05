from django.urls import path, include
from knox import views as knox_views
from .views import (
    api_root,
    RegisterAPI, 
    LoginAPI, 
    get_user_data,
    StudentListCreateView,
    StudentDetailView
)



urlpatterns = [
    path('', api_root, name='api-root'),  # Add this line
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/user/', get_user_data, name='user'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
from django.urls import path, include
from .views import (
    api_root,  # Add this
    RegisterAPI, 
    LoginAPI, 
    get_user_data,
    StudentListCreateView,
    StudentDetailView
)

