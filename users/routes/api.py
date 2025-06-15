from django.urls import path
from drf_yasg.views import get_schema_view
from users.Http.Controllers import LoginController
from users.Http.Controllers import UserProfileController
from users.Http.Controllers import RegisterUserController

from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('login/', LoginController.as_view(), name='login'),
    path('profile/', UserProfileController.as_view(), name='user-profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserController.as_view(), name='register'),
]