from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .tasks import send_welcome_email


# 1. User Registration View (public)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)  # Call Celery task


# 2. Public API View (no authentication required)
class PublicHelloView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({'message': 'Hello, world! This is a public endpoint.'})


# 3. Protected API View (requires JWT token)
class ProtectedHelloView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Hello, {request.user.username}! You are authenticated.'})
