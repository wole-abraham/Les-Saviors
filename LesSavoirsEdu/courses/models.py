from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='course_image/', null=True, blank=True)
    instructor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="courses", null=True, blank=True)

    def __str__(self):
        return f"{self.title} instructor by {self.instructor}" 