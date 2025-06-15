from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from models import User

class UserProfileController(APIView):
    permission_classes = [IsAuthenticated]
    
    def handle_exception(self, exc):
        if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
            return Response({
                "status": "error",
                "message": "Invalid token or no token provided."
            }, status=401)
        return super().handle_exception(exc)
    
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({
                "status": "success",
                "data": {
                    "name": user.name,
                    "document_number": user.document_number,
                    "email": user.email
                }
            }, status=status.HTTP_200_OK)