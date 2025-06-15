from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, email,  document_number, password=None, **extra_fields):
        if not email and not document_number:
            raise ValueError('El email o el número de documento son obligatorios')
        
        email = self.normalize_email(email)
        user = self.model(email=email, document_number=document_number, **extra_fields)
        
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, document_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, document_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, unique=True)
    last_name = models.CharField(max_length=30, blank=True)
    document_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    objects = UserManager()

# definen cómo se maneja la autenticación y qué campos son obligatorios al crear un superusuario:

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'document_number']

    def __str__(self):
        return self.email