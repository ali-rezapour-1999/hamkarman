from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = CustomUser
        fields = ('phone_number','email' , 'is_active', 'is_staff')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('slug_id', 'phone_number', 'email',  'is_active')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ( 'slug_id' ,'email', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_del' ,'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ( 'phone_number', 'email')
    ordering = ('created_at',)
    readonly_fields=('slug_id' , 'created_at' , 'last_login',)


admin.site.register(CustomUser, CustomUserAdmin)
