from django.contrib import admin
from .models.User import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'document_number', 'is_staff', 'is_active')
    fields = ('email', 'name', 'last_name', 'document_number', 'password', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ['name']
    ordering = ('name',)

