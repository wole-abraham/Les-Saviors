from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.

roles = [
    ('Student', 'Student'),
    ('Teacher', 'Teacher')
]

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    role = models.CharField(choices=roles, default='Student', max_length=10)    


    def initials(self):
        return f"{self.first_name}.{self.last_name[0].title()}"
    
    def __str__(self):
        return f"{self.email}"



class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',
                                         blank=True,
                                         null=True,
                                         default="defaults/default_profile_image.png"
                                        )
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
