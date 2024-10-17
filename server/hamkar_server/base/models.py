import random
from django.db import models

class BaseModel(models.Model):
    slug_id = models.CharField(max_length=8, unique=True, blank=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_del = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Ensure this is abstract to prevent DB table creation

    def save(self, *args, **kwargs):
        if not self.slug_id:
            self.slug_id = self.generate_unique_slug_id()
        super().save(*args, **kwargs)

    def generate_unique_slug_id(self):
        """Generate a unique 8-digit slug_id"""
        while True:
            slug_id = str(random.randint(10000000, 99999999))  # Generate 8-digit number
            if not self.__class__.objects.filter(slug_id=slug_id).exists():
                return slug_id
