from django.contrib import admin
from .models import Skill , UserInformation

class SkillAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    search_fields = ('tag',)

    fieldsets = (
        (None, {'fields': ('tag','is_del')}),
    )

class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)

    fieldsets = (
        (None, {'fields': ('user', 'firstname' ,'lastname', 'birthday', 'gender', 'user_image', 'cv_file', 'describe' ,'skills', 'telegram', 'instagram', 'linkedin' , 'git_repository' ,'whatsapp' )}),
    )


admin.site.register(Skill , SkillAdmin)
admin.site.register(UserInformation, UserInformationAdmin)
