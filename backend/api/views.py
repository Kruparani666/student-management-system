from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, StudentSerializer
from students.models import Student
from django.contrib.auth import login
from rest_framework import status
from rest_framework.reverse import reverse



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'auth': {
            'register': reverse('register', request=request, format=format),
            'login': reverse('login', request=request, format=format),
            'user': reverse('user', request=request, format=format),
            'logout': reverse('knox_logout', request=request, format=format),
        },
        'students': reverse('student-list', request=request, format=format),
    })

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, status=201)  # Explicitly return 201 status

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

@api_view(['GET'])
def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        return Response(UserSerializer(user).data)
    return Response({'error': 'Not authenticated'}, status=401)



# Student Views
class StudentListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            return Student.objects.all()
        return Student.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            return Student.objects.all()
        return Student.objects.filter(created_by=self.request.user)
    
    
    