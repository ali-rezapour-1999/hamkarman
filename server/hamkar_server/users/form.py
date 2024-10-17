from django import forms
from .models import UserInformation, Skill 

class UserInformationForm(forms.ModelForm):
    skills = forms.CharField(required=False, help_text="Enter skills separated by commas")

    class Meta:
        model = UserInformation
        fields = ['user', 'birthday', 'gender', 'user_image', 'cv_file', 'describe' ,'skills', 'telegram', 'instagram', 'linkedin' , 'git_repository' ,'whatsapp' ]

    def save(self, commit=True):
        user_info = super().save(commit=False)
        
        if self.cleaned_data['skills']:
            skills = [skill.strip() for skill in self.cleaned_data['skills'].split(',')]
            for skill in skills:
                skill, created = Skill.objects.get_or_create(name=skill)  # Create tag if it does not exist
                user_info.skills.add(skill)

        if commit:
            user_info.save()
        return user_info
