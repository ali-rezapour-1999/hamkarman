from rest_framework import serializers
from .models import UserInformation, Skill
from rest_framework.authtoken.models import Token
from users.serializers import CustomUserSerializer

class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill 
        fields = ['tag']

class UserInformationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)  
    skills = SkillTagSerializer(many=True, read_only=True)  

    class Meta:
        model = UserInformation 
        fields = [
            'user',
            'birthday',
            'gender',
            'user_image',
            'skills',
            'telegram',
            'instagram',
            'linkedin',
            'git_repository',
            'whatsapp',
            'cv_file',
            'describe'
        ]
