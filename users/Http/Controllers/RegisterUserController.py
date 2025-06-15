from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User

class RegisterUserController(APIView):

    def post(self, request):
        name = request.data.get('name')
        document_number = request.data.get('document_number')
        email = request.data.get('email')
        password = request.data.get('password')
        if not name or not document_number or not email or not password:
            return Response({'detail': 'Name, document number, email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        if email and User.objects.filter(email=email).exists():
            return Response({'detail': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(
            name=name,
            document_number=document_number,
            email=email,
            password=password
        )

        if user:
            return Response({
                'status': 'success',
                'message': 'User registered successfully.',
            }, status=status.HTTP_201_CREATED)