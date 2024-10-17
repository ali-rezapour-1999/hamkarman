from django.db import models
from users.models import CustomUser
from base.models import BaseModel 

class Skill(BaseModel):
    tag = models.CharField(max_length=100, unique=True)  
    
    def __str__(self):
        return self.tag


class UserInformation (models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE )
    firstname =models.CharField(max_length = 255 , blank=True , null = True)
    lastname =models.CharField(max_length = 255 , blank=True , null = True)
    birthday = models.DateField(null=True, blank=True)
    user_image = models.ImageField(upload_to='user/image/', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    skills = models.ManyToManyField(Skill , blank=True)  
    describe = models.TextField(blank=True)
    telegram = models.URLField(max_length=255, blank=True)  
    instagram = models.URLField(max_length= 255 , blank =True)
    linkedin = models.URLField(max_length= 255 , blank =True)
    git_repository = models.URLField(max_length= 255 , blank =True)
    whatsapp = models.URLField(max_length=255 , blank=True)
    cv_file = models.FileField(upload_to='user/file_cv/' ,blank=True,null=True)

    
    def __str__(self):
        return f"{self.firstname}'s Information"

